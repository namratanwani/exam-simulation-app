# Create an Azure Content Understanding client application

Source: https://learn.microsoft.com/en-us/training/modules/analyze-content-ai-api/

## Learning objectives

After completing this module, you will be able to:

- Use the Azure Content Understanding API to build a content analyzer.
- Use the Azure Content Understanding API to consume an analyzer.

Prerequisites: familiarity with Azure services/portal; some familiarity with Python and APIs.

Module facts: Intermediate level, roles = AI Engineer / Developer, product area = Foundry Tools / Microsoft Foundry, 7 units.

Related module (build analyzers via UI, not API): "Create a multimodal analysis solution with Azure Content Understanding" (`/en-us/training/modules/analyze-content-ai/`) — that module covers Content Understanding **Studio** (visual/no-code); THIS module covers the **Python SDK and REST API** (client application/programmatic access).

## Exam relevance

Maps to **Implement computer vision solutions (10-15%)**:
- "Implement visual understanding by configuring Azure Content Understanding in Foundry Tools to extract visual characteristics" — this module is the client-app/API path for that.
- "Configure single-task and pro-mode Content Understanding pipelines" — schema/analyzer definition (single-task style) shown here.

Maps to **Implement information extraction solutions (10-15%)**:
- "Extract information using multimodal pipelines combining OCR, layout analysis, field extraction" — the business-card example combines OCR (words/lines/paragraphs) with field extraction.
- "Produce clean, grounded representations for agents/RAG using Content Understanding" — the `markdown` output field in analysis results.
- "Implement analyzers for generating structured or markdown outputs using Content Understanding" — analyzer schema (`fieldSchema`) produces structured JSON; `contents[].markdown` produces markdown.
- "Ingest and index content (documents, images, audio, video)" — Content Understanding analyzes documents, images, audio files, and videos.

Maps to **Manage, monitor, and secure AI systems**:
- "Configure security including managed identity, private networking, keyless credentials, role policies" — API key auth (`AzureKeyCredential` / `Ocp-Apim-Subscription-Key` header) vs. Microsoft Entra ID auth via the Microsoft Foundry SDK when working inside a Foundry project.

Maps to **Build generative applications by using Foundry**:
- "Integrate generative workflows into applications by using Foundry SDKs and connectors" — `azure-ai-contentunderstanding` Python SDK, `ContentUnderstandingClient`.
- "Configure an application to connect to a Foundry project" — endpoint + key retrieval from Azure portal or Foundry portal project home page.

## Introduction

Azure Content Understanding is a **multimodal service** that simplifies creation of AI-powered **analyzers** that extract information from multiple content formats: **documents, images, audio files, and videos**.

Two ways to develop client applications that use Content Understanding analyzers:
- **Python SDK**
- **REST API**

(This module focuses on both, as the client-development path — contrasted with the Content Understanding **Studio** UI-based module.)

Goal of the module: write code using the Python SDK and REST API to submit a content file to an analyzer and process the results.

## Prepare to use the AI Content Understanding API

### Provisioning the resource

Before using the Azure Content Understanding API, you need a **Microsoft Foundry resource** in your Azure subscription. Two provisioning routes:

- Create a **Microsoft Foundry** resource directly in the Azure portal.
- Create a **Microsoft Foundry project**, which includes a Microsoft Foundry resource by default.

Tip: Creating a Microsoft Foundry **project** enables you to use visual tools to create/manage Content Understanding **schemas** and **analyzers** (i.e., Content Understanding Studio-style tooling).

### Credentials needed

After provisioning, to connect to the Content Understanding API from a client app you need:
- The Microsoft Foundry resource **endpoint**
- One of the **API keys** associated with the endpoint

These are obtained from the Azure portal (resource's Keys and Endpoint-style settings). If working within a Microsoft Foundry **project**, endpoint and key for the associated Foundry resource can be found on the **Foundry portal project home page**.

### Authentication options

- **API key** authentication (shown throughout this module): `AzureKeyCredential` (Python SDK) or `Ocp-Apim-Subscription-Key` HTTP header (REST).
- **Microsoft Entra ID authentication**: When working within a Microsoft Foundry project, you can write code using the **Microsoft Foundry SDK** to connect to the project using Microsoft Entra ID authentication, and retrieve the connection details (endpoint/credentials) for the associated Foundry resource programmatically.

### Installing the Python SDK

Package name: `azure-ai-contentunderstanding`

```bash
pip install azure-ai-contentunderstanding
```

Note: Requires **Python 3.9 or later**. The REST API can be used directly from any language that supports HTTP requests (no SDK dependency).

### Required model deployments (prerequisite)

Important: Before using the Content Understanding API, you must set up **default model deployments** for your Microsoft Foundry resource. Content Understanding requires these model deployments:
- `GPT-4.1`
- `GPT-4.1-mini`
- `text-embedding-3-large`

These can be configured in the Azure portal or via the API. (Referenced doc: "Set up model deployments" / migration-preview-to-ga#prerequisites.)

Related module for deeper Foundry SDK programming: "Develop an AI app with the Microsoft Foundry SDK" (`/en-us/training/modules/ai-foundry-sdk/`).

## Create a Content Understanding analyzer

Guidance: In most scenarios, create/test analyzers using the **visual interface in Content Understanding Studio**. But you can alternatively create an analyzer by submitting a **JSON definition of the schema** to the API directly (the programmatic path covered here).

### Defining a schema for an analyzer

Analyzers are based on **schemas** that define the fields to extract or generate from a content file. A schema is a set of fields specified as JSON. Example analyzer definition (business card):

```json
{
    "description": "Simple business card",
    "baseAnalyzerId": "prebuilt-document",
    "config": {
        "returnDetails": true
    },
    "fieldSchema": {
        "fields": {
            "ContactName": {
                "type": "string",
                "method": "extract",
                "description": "Name on business card"
            },
            "EmailAddress": {
                "type": "string",
                "method": "extract",
                "description": "Email address on business card"
            }
        }
    },
    "models": {
        "completion": "gpt-4.1",
        "embedding": "text-embedding-3-large"
    }
}
```

Key elements of the schema/definition:
- `description` — free-text description of the analyzer.
- `baseAnalyzerId` — the pre-built analyzer this custom analyzer is based on, e.g. `prebuilt-document` (a **pre-built document analyzer**).
- `config.returnDetails` — boolean; `true` returns extra detail in results (e.g., OCR layout).
- `fieldSchema.fields` — dictionary of field definitions, each with:
  - `type` — data type, e.g. `string`.
  - `method` — how the value is obtained: `extract` means the value must literally exist in the document and is "read" out (as opposed to a field that is *generated* by inferring information about the content).
  - `description` — describes what the field represents (helps the model locate/generate it).
- `models` — the generative models the analyzer uses for processing:
  - `completion`: `gpt-4.1`
  - `embedding`: `text-embedding-3-large`

Note: this is a deliberately minimal example. Real schemas typically include more fields of different types and more configuration settings, and may include a sample document. Full reference: Azure Content Understanding API docs, **Content Analyzers — Create or Replace** operation (`/en-us/rest/api/contentunderstanding/content-analyzers/create-or-replace`).

### Using the Python SDK to create an analyzer

Class: **`ContentUnderstandingClient`** (module `azure.ai.contentunderstanding`)
Method: **`begin_create_analyzer`** — handles the asynchronous creation process (returns a poller).

```python
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client
endpoint = "<YOUR_ENDPOINT>"
credential = AzureKeyCredential("<YOUR_API_KEY>")
client = ContentUnderstandingClient(endpoint=endpoint, credential=credential)

# Define the analyzer
analyzer_name = "business_card_analyser"
analyzer_definition = {
    "description": "Simple business card",
    "baseAnalyzerId": "prebuilt-document",
    "config": {"returnDetails": True},
    "fieldSchema": {
        "fields": {
            "ContactName": {
                "type": "string",
                "method": "extract",
                "description": "Name on business card"
            },
            "EmailAddress": {
                "type": "string",
                "method": "extract",
                "description": "Email address on business card"
            }
        }
    },
    "models": {
        "completion": "gpt-4.1",
        "embedding": "text-embedding-3-large"
    }
}

# Create the analyzer and wait for completion
poller = client.begin_create_analyzer(analyzer_name, body=analyzer_definition)
result = poller.result()
print(f"Analyzer created: {result.analyzer_id}")
```

Notable API shape: `begin_create_analyzer(analyzer_name, body=analyzer_definition)` returns a **poller**; `.result()` blocks until done and returns an object with `.analyzer_id`.

### Using the REST API to create an analyzer

- The JSON schema is submitted as a **`PUT`** request to the endpoint, with the API key in the request header.
- The response from the `PUT` request includes an **`Operation-Location`** header — a callback URL used to poll status via **`GET`**.

Exact URL pattern:
```
{endpoint}/contentunderstanding/analyzers/{analyzer_name}?api-version=2025-11-01
```
API version used in examples: **`2025-11-01`**.

Header for auth: **`Ocp-Apim-Subscription-Key: <YOUR_API_KEY>`**, plus `Content-Type: application/json`.

Full example (create analyzer from `card.json`, then poll):

```python
import json
import requests

# Get the business card schema
with open("card.json", "r") as file:
    schema_json = json.load(file)

# Use a PUT request to submit the schema for a new analyzer
analyzer_name = "business_card_analyser"

headers = {
    "Ocp-Apim-Subscription-Key": "<YOUR_API_KEY>",
    "Content-Type": "application/json"}

url = f"{<YOUR_ENDPOINT>}/contentunderstanding/analyzers/{analyzer_name}?api-version=2025-11-01"

response = requests.put(url, headers=headers, data=json.dumps(schema_json))

# Get the response and extract the ID assigned to the operation
callback_url = response.headers["Operation-Location"]

# Use a GET request to check the status of the operation
result_response = requests.get(callback_url, headers=headers)

# Keep polling until the operation is complete
status = result_response.json().get("status")
while status == "Running":
    result_response = requests.get(callback_url, headers=headers)
    status = result_response.json().get("status")

print("Done!")
```

Async pattern (creation): **`PUT` create → read `Operation-Location` header from response → `GET` that URL repeatedly → status field is `"Running"` while in progress** (loop shown checks `status == "Running"`; implicitly other terminal values like `"Succeeded"` end the loop).

## Analyze content

To analyze a file's contents, submit it to the Content Understanding API endpoint, referencing the analyzer to use. Content can be specified as:
- A **URL** (file hosted at an Internet-accessible location), or
- **Uploaded binary file data** directly (e.g., a `.pdf` document, `.png` image, `.mp3` audio file, `.mp4` video file).

Analysis is an **asynchronous operation**: after submitting the request you receive an **operation ID** used to check status and retrieve results once complete.

Example scenario continued: analyze a scanned business card image with the previously created `business_card_analyser`.

### Using the Python SDK

SDK package: `azure-ai-contentunderstanding`. Class: **`ContentUnderstandingClient`**. The SDK handles authentication, request formatting, and **automatic polling** for async operations.

```python
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput
from azure.core.credentials import AzureKeyCredential

# Authenticate the client
endpoint = "<YOUR_ENDPOINT>"
credential = AzureKeyCredential("<YOUR_API_KEY>")
client = ContentUnderstandingClient(endpoint=endpoint, credential=credential)

# Analyze the business card using the custom analyzer
analyzer_name = "business_card_analyser"
poller = client.begin_analyze(
    analyzer_id=analyzer_name,
    inputs=[AnalysisInput(url="https://host.com/business-card.png")]
)

# Wait for the operation to complete and get the results
result = poller.result()

# Extract field values from the results
content = result.contents[0]
if content.fields:
    for field_name, field_data in content.fields.items():
        if field_data.type == "string":
            print(f"{field_name}: {field_data.value}")
```

Key API shape:
- Method: **`client.begin_analyze(analyzer_id=..., inputs=[AnalysisInput(url=...)])`** — returns a poller.
- `AnalysisInput` — model class representing one input (here constructed with `url=`).
- `poller.result()` — automatically handles polling until operation completes; returns an **`AnalysisResult`**-type object.
- `result.contents` — list of content objects (one per analyzed content item/page-group).
- `content.fields` — dict of extracted field name → field data object; `field_data.type`, `field_data.value`.

Tip called out explicitly: "The SDK's `begin_analyze` method returns a poller object. Calling `.result()` on the poller automatically handles polling until the operation completes, so you don't need to write your own polling loop."

### Using the REST API

Client applications submit HTTP calls to the Content Understanding endpoint for the Foundry resource, with the API key in the header.

Analyze-by-URL request pattern — **`POST`**:
```
{endpoint}/contentunderstanding/analyzers/{analyzer_name}:analyze?api-version=2025-11-01
```

Request body:
```json
{
    "inputs": [
        {
            "url": "https://host.com/business-card.png"
        }
    ]
}
```

Full example:

```python
import json
import requests

## Use a POST request to submit the file URL to the analyzer
analyzer_name = "business_card_analyser"

headers = {
        "Ocp-Apim-Subscription-Key": "<YOUR_API_KEY>",
        "Content-Type": "application/json"}

url = f"{<YOUR_ENDPOINT>}/contentunderstanding/analyzers/{analyzer_name}:analyze?api-version=2025-11-01"

request_body = {
    "inputs": [
        {
            "url": "https://host.com/business-card.png"
        }
    ]
}

response = requests.post(url, headers=headers, json=request_body)

# Get the response and extract the ID assigned to the analysis operation
response_json = response.json()
id_value = response_json.get("id")

# Use a GET request to check the status of the analysis operation
result_url = f"{<YOUR_ENDPOINT>}/contentunderstanding/analyzerResults/{id_value}?api-version=2025-11-01"

result_response = requests.get(result_url, headers=headers)

# Keep polling until the analysis is complete
status = result_response.json().get("status")
while status == "Running":
        result_response = requests.get(result_url, headers=headers)
        status = result_response.json().get("status")

# Get the analysis results
if status == "Succeeded":
    result_json = result_response.json()
```

Async pattern (analysis): **`POST` analyze → response JSON contains `id` → poll `GET {endpoint}/contentunderstanding/analyzerResults/{id}?api-version=2025-11-01` → check `status` field (`"Running"` while in progress, `"Succeeded"` when complete)**.

Note: This shows URL-based submission. To submit **binary file data directly**, use the **`analyzeBinary`** operation instead (named explicitly as the alternative to the URL-based `:analyze` operation).

### Processing analysis results

Results depend on:
- The **kind** of content the analyzer analyzes (document, video, image, or audio).
- The **schema** for the analyzer.
- The **contents of the file** analyzed.

For the document-based business card analyzer, the response contains:
- The **extracted fields**.
- The **OCR layout** of the document — locations of lines of text, individual words, and paragraphs on each page.

#### Using the Python SDK

`AnalysisResult` object gives typed access to results. `contents` property = list of content objects, each with `fields`, `markdown`, and metadata.

```python
# (continued from previous SDK code example)

content = result.contents[0]
if content.fields:
    for field_name, field_data in content.fields.items():
        if field_data.type == "string":
            print(f"{field_name}: {field_data.value}")
```

#### Using the REST API — full JSON response shape

Complete example JSON response for the business card analysis:

```json
{
    "id": "00000000-0000-0000-0000-a00000000000",
    "status": "Succeeded",
    "result": {
        "analyzerId": "biz_card_analyser_2",
        "apiVersion": "2025-11-01",
        "createdAt": "2025-05-16T03:51:46Z",
        "warnings": [],
        "contents": [
            {
                "markdown": "John Smith\nEmail: john@contoso.com\n",
                "fields": {
                    "ContactName": {
                        "type": "string",
                        "valueString": "John Smith",
                        "spans": [
                            {
                                "offset": 0,
                                "length": 10
                            }
                        ],
                        "confidence": 0.994,
                        "source": "D(1,69,234,333,234,333,283,69,283)"
                    },
                    "EmailAddress": {
                        "type": "string",
                        "valueString": "john@contoso.com",
                        "spans": [
                            {
                                "offset": 18,
                                "length": 16
                            }
                        ],
                        "confidence": 0.998,
                        "source": "D(1,179,309,458,309,458,341,179,341)"
                    }
                },
                "kind": "document",
                "startPageNumber": 1,
                "endPageNumber": 1,
                "unit": "pixel",
                "pages": [
                    {
                        "pageNumber": 1,
                        "angle": 0.03410444,
                        "width": 1000,
                        "height": 620,
                        "spans": [
                            {
                                "offset": 0,
                                "length": 35
                            }
                        ],
                        "words": [
                            {
                                "content": "John",
                                "span": { "offset": 0, "length": 4 },
                                "confidence": 0.992,
                                "source": "D(1,69,234,181,234,180,283,69,283)"
                            },
                            {
                                "content": "Smith",
                                "span": { "offset": 5, "length": 5 },
                                "confidence": 0.998,
                                "source": "D(1,200,234,333,234,333,282,200,283)"
                            },
                            {
                                "content": "Email:",
                                "span": { "offset": 11, "length": 6 },
                                "confidence": 0.995,
                                "source": "D(1,75,310,165,309,165,340,75,340)"
                            },
                            {
                                "content": "john@contoso.com",
                                "span": { "offset": 18, "length": 16 },
                                "confidence": 0.977,
                                "source": "D(1,179,309,458,311,458,340,179,341)"
                            }
                        ],
                        "lines": [
                            {
                                "content": "John Smith",
                                "source": "D(1,69,234,333,233,333,282,69,282)",
                                "span": { "offset": 0, "length": 10 }
                            },
                            {
                                "content": "Email: john@contoso.com",
                                "source": "D(1,75,309,458,309,458,340,75,340)",
                                "span": { "offset": 11, "length": 23 }
                            }
                        ]
                    }
                ],
                "paragraphs": [
                    {
                        "content": "John Smith Email: john@contoso.com",
                        "source": "D(1,69,233,458,233,458,340,69,340)",
                        "span": { "offset": 0, "length": 34 }
                    }
                ],
                "sections": [
                    {
                        "span": { "offset": 0, "length": 34 },
                        "elements": [ "/paragraphs/0" ]
                    }
                ]
            }
        ]
    }
}
```

Response shape notes (exam-relevant field names):
- Top-level: `id`, `status` (e.g. `"Succeeded"`), `result`.
- `result`: `analyzerId`, `apiVersion`, `createdAt`, `warnings` (array), `contents` (array).
- Each `contents[]` item: `markdown` (grounded markdown representation of the content — useful for RAG/agent grounding), `fields` (extracted/generated field values), `kind` (e.g. `"document"`), `startPageNumber`, `endPageNumber`, `unit` (e.g. `"pixel"`), `pages`, `paragraphs`, `sections`.
- Each field object: `type`, `valueString` (type-specific value key — for a string field it's `valueString`), `spans` (offset/length into the markdown/text), `confidence` (0-1 float), `source` (a bounding-region/polygon descriptor string, format `D(page, x1,y1,x2,y2,x3,y3,x4,y4)`).
- `pages[]`: `pageNumber`, `angle` (skew angle), `width`, `height`, `spans`, `words[]` (each with `content`, `span`, `confidence`, `source`), `lines[]` (each with `content`, `source`, `span`).
- `sections[]`: `span`, `elements` (references to other structural elements, e.g. `"/paragraphs/0"`).

Client-side parsing example (REST/JSON path):

```python
# (continued from previous code example)

# Iterate through the fields and extract the names and type-specific values
contents = result_json["result"]["contents"]
for content in contents:
    if "fields" in content:
        fields = content["fields"]
        for field_name, field_data in fields.items():
            if field_data['type'] == "string":
                print(f"{field_name}: {field_data['valueString']}")
```

Output:
```
ContactName: John Smith
EmailAddress: john@contoso.com
```

Key contrast — Python SDK vs REST API field access:
- SDK: `field_data.value` (attribute access on typed `AnalysisResult`/field objects; SDK abstracts away the `valueString`/`valueNumber`/etc. naming).
- REST/raw JSON: `field_data['valueString']` (must use the **type-specific value key**, e.g. `valueString` for a `"type": "string"` field — dict access on raw parsed JSON).

## Exercise - Develop a Content Understanding client application

Hands-on lab (40 minutes). Uses the Azure Content Understanding API to extract information from content by submitting a file to an analyzer. Requires an Azure subscription with administrative access. Exercise is launched via an external Microsoft Learn sandbox link (not textual content to capture further).

## Summary

Azure Content Understanding is a multimodal AI service that enables you to extract information from many different kinds of content. The Python SDK and REST API for the service enable you to create client applications that analyze content to extract and generate field values.

Further reading pointer: Azure Content Understanding documentation (`/en-us/azure/ai-services/content-understanding/`).

## Cross-cutting exam-relevant summary

| Concern | Python SDK | REST API |
|---|---|---|
| Package/base | `azure-ai-contentunderstanding` (Python ≥3.9) | any HTTP-capable language |
| Client/auth object | `ContentUnderstandingClient(endpoint=, credential=AzureKeyCredential(...))` | header `Ocp-Apim-Subscription-Key` |
| Create analyzer | `client.begin_create_analyzer(analyzer_name, body=analyzer_definition)` → poller → `.result()` → `.analyzer_id` | `PUT {endpoint}/contentunderstanding/analyzers/{name}?api-version=2025-11-01`; poll `Operation-Location` header via `GET` |
| Analyze content (URL) | `client.begin_analyze(analyzer_id=, inputs=[AnalysisInput(url=...)])` → poller → `.result()` | `POST {endpoint}/contentunderstanding/analyzers/{name}:analyze?api-version=2025-11-01` with `{"inputs":[{"url": ...}]}`; response has `id`; poll `GET {endpoint}/contentunderstanding/analyzerResults/{id}?api-version=2025-11-01` |
| Analyze content (binary upload) | (not shown explicitly; implied via SDK input types) | use `analyzeBinary` operation instead of `:analyze` |
| Polling | Automatic (`poller.result()`) | Manual loop on `status` field (`"Running"` → `"Succeeded"`) |
| Result field values | `content.fields[name].type`, `.value` | `content["fields"][name]["type"]`, `["valueString"]` (type-specific key) |
| Required model deployments | `GPT-4.1`, `GPT-4.1-mini`, `text-embedding-3-large` | same (resource-level prerequisite, not SDK-specific) |
| API version referenced | — | `2025-11-01` |
| Base analyzer example | `baseAnalyzerId: "prebuilt-document"` | same |
