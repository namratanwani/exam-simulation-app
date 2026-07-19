# Practice questions — Create an Azure Content Understanding client application

## Learning objectives / Exam relevance

**Q27.** Which of the following is one of the two stated learning objectives for this module?
A. Use the Azure Content Understanding API to build a content analyzer
B. Train a custom classification model on labeled business cards
C. Configure Azure AI Search enrichment skillsets for indexing pipelines
D. Deploy a Sora 2 video-generation model in Microsoft Foundry
**Answer:** A — The two objectives are: use the Azure Content Understanding API to build a content analyzer, and use the Azure Content Understanding API to consume an analyzer.

**Q28.** How does this module's scope differ from the related module "Create a multimodal analysis solution with Azure Content Understanding"?
A. They are identical, just duplicated content presented under two separate module titles for search-engine indexing purposes
B. This module covers building analyzers via the Python SDK and REST API (client applications/programmatic access); the related module covers Content Understanding Studio (the visual/no-code UI)
C. This module only covers video analysis; the related module only covers document analysis, with no overlap in supported content types
D. This module covers Pro mode exclusively; the related module covers Standard mode exclusively, splitting the two modes across separate modules
**Answer:** B — The module explicitly distinguishes itself (Python SDK/REST API, client-application path) from the related Studio-based (visual/no-code) module.

## Introduction

**Q1.** Which two client development options does this Microsoft Learn module cover for building a client application against Azure Content Understanding analyzers? (Choose 2.)
A. Content Understanding Studio visual designer
B. Python SDK
C. REST API
D. Azure CLI `az content-understanding` command group
**Answer:** B, C — The module states you can develop client applications that use Azure Content Understanding analyzers by using the Python SDK or the REST API. Content Understanding Studio is covered by a *different* module ("Create a multimodal analysis solution with Azure Content Understanding"), and there is no `az content-understanding` CLI command group.

**Q2.** Azure Content Understanding is best described as which type of service?
A. A single-purpose OCR engine for scanned documents only, with no image or video support
B. A multimodal service that extracts information from documents, images, audio, and video via AI-powered analyzers
C. A vector database for semantic search over embeddings, requiring a separate index resource
D. A speech-to-text transcription API limited to converting spoken audio into plain text
**Answer:** B — Azure Content Understanding is a multimodal service that simplifies creation of AI-powered analyzers that extract information from documents, images, audio files, and videos.

## Prepare to use the AI Content Understanding API

**Q3.** Before you can call the Azure Content Understanding API, which Azure resource must exist in your subscription?
A. Azure AI Search service
B. Microsoft Foundry resource
C. Azure Cognitive Services multi-service resource (legacy)
D. Azure Data Factory pipeline
**Answer:** B — You need a Microsoft Foundry resource, provisioned either directly in the Azure portal or implicitly by creating a Microsoft Foundry project (which includes a Foundry resource by default).

**Q4.** Which two pieces of information does a client application need to connect to the Azure Content Understanding API using key-based authentication? (Choose 2.)
A. The Microsoft Foundry resource endpoint
B. One of the API keys associated with the endpoint
C. The Azure subscription ID
D. The resource group's ARM template
**Answer:** A, B — You need the Microsoft Foundry resource endpoint and one of the API keys associated with it, obtainable from the Azure portal or, for a Foundry project, the Foundry portal project home page.

**Q5.** A developer is working inside a Microsoft Foundry project and wants to avoid managing API keys directly in code. What authentication approach does the module describe for this scenario?
A. Shared Access Signature (SAS) tokens issued by the Foundry resource's key vault and rotated every 24 hours
B. Microsoft Entra ID authentication via the Microsoft Foundry SDK, retrieving connection details for the Foundry resource
C. Basic authentication with username and password stored in an environment variable on the client machine
D. Anonymous access with IP allowlisting configured on the resource's networking blade and firewall rules
**Answer:** B — When working within a Microsoft Foundry project, you can write code that uses the Microsoft Foundry SDK to connect to the project using Microsoft Entra ID authentication and retrieve the connection details for the associated Foundry resource.

**Q6.** Which command installs the Python SDK for Content Understanding, and what is the minimum supported Python version?
A. `pip install azure-contentunderstanding-sdk`; Python 3.7+
B. `pip install azure-ai-contentunderstanding`; Python 3.9+
C. `pip install azure-cognitiveservices-contentunderstanding`; Python 3.8+
D. `pip install azure-ai-formrecognizer`; Python 3.9+
**Answer:** B — `pip install azure-ai-contentunderstanding`, requiring Python 3.9 or later. (`azure-ai-formrecognizer` is a different, older SDK package for Form Recognizer/Document Intelligence.)

**Q7.** Which three model deployments must be set up on your Microsoft Foundry resource before you can use Content Understanding? (Choose 3.)
A. GPT-4.1
B. GPT-4.1-mini
C. text-embedding-3-large
D. Whisper
**Answer:** A, B, C — Content Understanding requires GPT-4.1, GPT-4.1-mini, and text-embedding-3-large model deployments. Whisper is not mentioned as a requirement in this module.

**Q8.** True or false framed as MCQ: If you don't want to use the Python SDK, can you still call Content Understanding from, say, a Java or Node.js application?
A. No, only Python is supported; other languages must proxy calls through a Python service
B. Yes, via the REST API, which works from any language that supports HTTP requests
C. Yes, but only via a .NET-specific SDK requiring a Windows runtime
D. No, a Foundry SDK is mandatory for all languages, even when calling REST directly
**Answer:** B — The REST API can be used directly from any language that supports HTTP requests; the Python SDK is just a convenience wrapper.

## Create a Content Understanding analyzer

**Q9.** In most scenarios, what does the module recommend as the primary way to create and test analyzers, reserving the JSON/API approach for special cases?
A. Using the visual interface in Content Understanding Studio
B. Writing raw cURL scripts directly against the REST endpoint
C. Using Azure Data Factory mapping data flows
D. Using Azure Logic Apps designer with a custom connector
**Answer:** A — In most scenarios, you should consider creating and testing analyzers using the visual interface in Content Understanding Studio; submitting a JSON schema directly to the API is presented as an alternative for some cases.

**Q10.** In an analyzer definition JSON, which property specifies the pre-built analyzer that a custom analyzer is based on?
A. `analyzerTemplate`
B. `baseAnalyzerId`
C. `parentAnalyzer`
D. `sourceSchema`
**Answer:** B — `baseAnalyzerId`, e.g. `"prebuilt-document"` in the business card example.

**Q11.** In a field definition inside `fieldSchema.fields`, setting `"method": "extract"` means:
A. The field value is generated by the model inferring information not literally present in the document
B. The field value must exist verbatim in the content and is read/extracted from it
C. The field is computed using a regular expression defined elsewhere in the schema
D. The field is ignored during analysis unless a default value is set
**Answer:** B — `extract` means the string value is expected to exist in the document so it can be "read," as opposed to a field that is *generated* by inferring information about the content.

**Q12.** Which two properties appear under the top-level `models` object of an analyzer definition in this module's example, and what values are used? (Choose 2.)
A. `completion`: `"gpt-4.1"`
B. `embedding`: `"text-embedding-3-large"`
C. `moderation`: `"content-safety-v2"`
D. `vision`: `"gpt-4-vision"`
**Answer:** A, B — The example's `models` object specifies `"completion": "gpt-4.1"` and `"embedding": "text-embedding-3-large"` as the generative models the analyzer uses for processing.

**Q13.** Which Python SDK class and method are used to create an analyzer asynchronously?
A. `ContentAnalyzerClient.create_analyzer()`
B. `ContentUnderstandingClient.begin_create_analyzer()`
C. `FormRecognizerClient.begin_build_model()`
D. `ContentUnderstandingClient.submit_analyzer()`
**Answer:** B — `ContentUnderstandingClient` provides a `begin_create_analyzer` method that handles the asynchronous creation process; you call `.result()` on the returned poller to get the completed result, which has an `.analyzer_id` attribute.

**Q14.** When creating an analyzer via the REST API, which HTTP verb is used to submit the JSON schema, and which response header provides the callback URL for checking status?
A. `POST`; `Retry-After`
B. `PUT`; `Operation-Location`
C. `PATCH`; `Location`
D. `PUT`; `Content-Location`
**Answer:** B — The JSON schema is submitted as a `PUT` request; the response includes an `Operation-Location` header containing the callback URL, which you poll with `GET`.

**Q15.** What is the exact REST endpoint URL pattern (path + query) shown in this module for creating an analyzer via `PUT`?
A. `{endpoint}/contentunderstanding/analyzers/{name}?api-version=2025-11-01`
B. `{endpoint}/contentunderstanding/analyzers/{name}:create?api-version=2025-11-01`
C. `{endpoint}/analyzers/{name}?api-version=2024-01-01`
D. `{endpoint}/contentunderstanding/v1/analyzers/{name}`
**Answer:** A — `{endpoint}/contentunderstanding/analyzers/{analyzer_name}?api-version=2025-11-01`, submitted with the `Ocp-Apim-Subscription-Key` header for authentication.

**Q29.** In the Python SDK example, which model class is used to represent one item of content submitted for analysis, and how is a URL-based input constructed with it?
A. `ContentInput(source=url, cache=True, timeout=30)`
B. `AnalysisInput(url="https://host.com/business-card.png")`
C. `AnalyzerRequest(fileUrl=url, retry=3, backoff="linear")`
D. `InputDocument.from_url(url, timeout=30)`
**Answer:** B — Inputs are passed as a list of `AnalysisInput` objects, e.g. `inputs=[AnalysisInput(url="https://host.com/business-card.png")]`, to `client.begin_analyze(analyzer_id=..., inputs=...)`.

## Analyze content

**Q16.** When submitting content for analysis by URL versus uploading binary data directly, which REST operation should you use for binary uploads instead of the URL-based `:analyze` operation?
A. `:uploadBinary`
B. `analyzeBinary`
C. `:submitFile`
D. `binaryAnalyze`
**Answer:** B — The module notes: "To submit binary file data directly, use the `analyzeBinary` operation instead" of the URL-based `:analyze` operation.

**Q17.** Which Python SDK method starts an analysis operation, and what does calling `.result()` on its return value do?
A. `client.analyze()`; it returns immediately without waiting, blocking on the socket internally
B. `client.begin_analyze()`; it returns a poller, and `.result()` automatically handles polling until the operation completes
C. `client.submit_analysis()`; it requires a manual polling loop checking a `status` field in the body
D. `client.start_job()`; it only works for video content, raising a `NotImplementedError` for documents and images
**Answer:** B — `client.begin_analyze(analyzer_id=..., inputs=[AnalysisInput(url=...)])` returns a poller object; calling `.result()` automatically handles polling until the operation completes, so you don't need to write your own polling loop.

**Q18.** In the REST API analysis flow, after `POST`-ing to the `:analyze` endpoint, which field in the JSON response body is used to build the polling URL?
A. `operationId`
B. `id`
C. `requestId`
D. `jobId`
**Answer:** B — The response JSON's `id` field is extracted and used to construct the polling URL: `{endpoint}/contentunderstanding/analyzerResults/{id}?api-version=2025-11-01`.

**Q19.** Which status string, when returned by the polling `GET` request, indicates the analysis operation is still in progress in the code shown in this module?
A. `"Pending"`
B. `"InProgress"`
C. `"Running"`
D. `"NotStarted"`
**Answer:** C — The polling loop checks `while status == "Running":` and continues polling; a terminal value such as `"Succeeded"` ends the loop.

**Q20.** Content submitted for analysis can be specified in which two ways according to the module? (Choose 2.)
A. A URL pointing to an Internet-accessible file
B. Uploaded binary file data (e.g., .pdf, .png, .mp3, .mp4)
C. A base64-encoded string embedded in the analyzer schema only
D. A SharePoint document library connector
**Answer:** A, B — You can specify content as a URL for a file hosted in an Internet-accessible location, or upload binary file data directly (for example a .pdf, .png, .mp3, or .mp4 file).

**Q21.** In the JSON analysis result, what is the purpose of the `markdown` property found in each `contents[]` item?
A. It stores the original analyzer schema used, including every field's method, enum options, and description text
B. It provides a grounded, human-readable markdown representation of the extracted content, useful for downstream RAG/agent consumption
C. It lists the confidence scores for every field, aggregated into a single top-level document-wide number
D. It is only populated for video content, never documents, since document markdown appears elsewhere
**Answer:** B — Each `contents[]` item includes a `markdown` field (e.g., `"John Smith\nEmail: john@contoso.com\n"`) providing a markdown-formatted representation of the content — this maps to the exam skill "produce clean, grounded representations for agents/RAG using Content Understanding."

**Q22.** For a field of `"type": "string"` in the raw REST JSON response, which key holds the actual extracted value?
A. `value` (the SDK-normalized key)
B. `stringValue`
C. `valueString`
D. `content` (the raw text container)
**Answer:** C — Raw JSON field objects use a type-specific value key; for a string field it is `valueString` (e.g., `field_data['valueString']`). This contrasts with the Python SDK, where you access `field_data.value` on the typed object.

**Q23.** Which two pieces of metadata does each extracted field object include in the REST JSON response, beyond its type and value? (Choose 2.)
A. `confidence` (a numeric score)
B. `spans` (offset/length locating the value in the text)
C. `createdBy` (the user who triggered analysis)
D. `retryCount`
**Answer:** A, B — Each field object includes `confidence` (e.g., 0.994) and `spans` (offset/length pairs), as well as a `source` bounding-region descriptor. There is no `createdBy` or `retryCount` shown.

**Q24.** For the document-based business card analyzer, the analysis response contains the extracted fields plus what other category of information, reflecting OCR/layout analysis?
A. Sentiment scores for each line of text, generated by an attached sentiment model
B. The OCR layout of the document, including locations of lines, words, and paragraphs on each page
C. A translated version of the document in multiple languages, auto-detected from the text
D. A PDF/A archival copy of the source file, stored alongside the extracted JSON
**Answer:** B — The response contains the extracted fields and the OCR layout of the document, including the locations of lines of text, individual words, and paragraphs on each page — directly maps to the exam skill of combining OCR, layout analysis, and field extraction.

**Q30.** In the full REST JSON analysis response, an extracted field includes `"source": "D(1,69,234,333,234,333,283,69,283)"`. What does this string represent?
A. A database record identifier, assigned by the storage layer when the field is first persisted
B. A bounding-region/polygon descriptor giving the page number and coordinate points locating where the value was found
C. A digital signature validating the field's authenticity, computed over its raw bytes
D. The Base64-encoded value of the field, re-encoded for transport-safe JSON embedding
**Answer:** B — The `source` string is a bounding-region/polygon descriptor in the format `D(page, x1,y1,x2,y2,x3,y3,x4,y4)`, identifying the region on the page where the extracted value was found — the same format used at the field, word, line, and paragraph level.

**Q31.** At the top level of the full REST analysis result JSON, which properties appear directly under `result` (alongside `contents`)?
A. `analyzerId`, `apiVersion`, `createdAt`, `warnings`
B. `analyzerName`, `region`, `pricingTier`
C. `subscriptionId`, `resourceGroup`, `tags`
D. `httpStatusCode`, `retryAfter`, `requestId`
**Answer:** A — The `result` object contains `analyzerId`, `apiVersion`, `createdAt`, `warnings` (an array), and `contents` (an array), per the full example response shown.

**Q32.** How long is the hands-on exercise for this module estimated to take, and what prerequisite is required?
A. 40 minutes; an Azure subscription with administrative access
B. 10 minutes; no Azure subscription needed, using a shared sandbox environment
C. 2 hours; a Microsoft 365 E5 license with a Copilot add-on enabled
D. 40 minutes; a pre-existing Content Understanding Studio project
**Answer:** A — The exercise is a 40-minute hands-on lab requiring an Azure subscription with administrative access.

## Cross-cutting / SDK vs REST comparison

**Q25.** A developer writes: `content.fields["ContactName"].value` against an `AnalysisResult` returned by the Python SDK's `begin_analyze().result()`. If they instead parsed the raw REST JSON response manually, what would be the equivalent expression for the same string field?
A. `content["fields"]["ContactName"]["value"]`
B. `content["fields"]["ContactName"]["valueString"]`
C. `content["fields"]["ContactName"].value`
D. `content.fields.ContactName.valueString`
**Answer:** B — The Python SDK exposes a normalized `.value` attribute on typed field objects, while raw REST JSON requires reading the type-specific key such as `valueString` via dict-style access.

**Q26.** Which of the following correctly pairs the async operation with its REST polling target?
A. Create analyzer → poll `Operation-Location` header from the `PUT` response; Analyze content → poll `{endpoint}/contentunderstanding/analyzerResults/{id}?api-version=...` built from the `id` in the `POST` response
B. Create analyzer → poll `analyzerResults/{id}`; Analyze content → poll the `Operation-Location` header, reversing which resource polls which endpoint
C. Both operations use the same `Operation-Location` header exclusively, regardless of whether it's creation or analysis being tracked
D. Both operations return results synchronously with no polling required, since both block on the connection until processing finishes
**Answer:** A — For analyzer creation, the `Operation-Location` response header from the `PUT` is the callback/poll URL. For content analysis, the `POST` response body's `id` is used to construct a poll URL against the `analyzerResults` resource.

---

## Scenario-based questions

**Q33.** *(Scenario)* You are building a Python client that creates a `prebuilt-document`-based analyzer for business cards, then analyzes an uploaded image, and finally prints the extracted contact name. Put the correct method calls and access patterns in order.
A. `client.begin_analyze()` → `client.begin_create_analyzer()` → `field_data['valueString']`, calling analyze before the analyzer even exists yet
B. `client.begin_create_analyzer(analyzer_name, body=analyzer_definition)` → `.result()` → `client.begin_analyze(analyzer_id=..., inputs=[AnalysisInput(...)])` → `.result()` → `content.fields["ContactName"].value`
C. `requests.put()` → `requests.post()` → `response.json()["valueString"]` (SDK not involved), reimplementing polling manually for both calls
D. `client.create_analyzer_sync()` → `client.analyze_sync()` → `content.fields.ContactName`, using method names that don't exist anywhere in the SDK
**Answer:** B — Create the analyzer with `begin_create_analyzer(...)`, block on `.result()` to get `.analyzer_id`; then analyze with `begin_analyze(analyzer_id=..., inputs=[AnalysisInput(...)])`, block on `.result()`, then read the typed field via `.value` on the SDK's field object.

**Q34.** *(Scenario)* Your team decided to implement the same create-analyzer-then-analyze workflow using raw REST calls instead of the SDK (e.g., because they're using Go, which has no Content Understanding SDK). Which sequence of HTTP calls and response-parsing steps is correct?
A. `POST` the schema to `/analyzers/{name}`, then immediately parse `response.json()["fields"]` — no polling needed for either step, ignoring that both operations are documented as asynchronous
B. `PUT` the schema to `/analyzers/{name}?api-version=2025-11-01`, poll the `Operation-Location` header via `GET` until done; then `POST` to `/analyzers/{name}:analyze?api-version=2025-11-01`, extract `id` from the response body, poll `GET /analyzerResults/{id}?api-version=2025-11-01` until `status == "Succeeded"`, then read `result.contents[].fields[name].valueString`
C. `PUT` the schema to `/analyzers/{name}:analyze`, then `POST` to `/analyzerResults/{name}`, swapping the endpoint suffixes used for creation and analysis
D. Only the Python SDK supports the create-then-analyze workflow; REST cannot replicate it, despite REST being fully documented and language-agnostic per the module
**Answer:** B — This is exactly the two independent async patterns shown: creation uses `PUT` + `Operation-Location` header polling; analysis uses `POST` + `id`-based polling against `analyzerResults`, with raw JSON requiring the type-specific `valueString` key — and the REST API works from any HTTP-capable language, including Go.

**Q35.** *(Scenario)* Before either the SDK or REST workflow above will succeed, what two prerequisites (independent of which client technology you choose) must already be true of your Microsoft Foundry resource?
A. It must have GPT-4.1, GPT-4.1-mini, and text-embedding-3-large model deployments configured, and you must have the resource's endpoint and an API key (or Entra ID access within a Foundry project)
B. It must be deployed in the East US region only, and billing must be prepaid — restrictions not mentioned anywhere in the module's prerequisites
C. It must have Azure AI Search attached, and a vector index must already exist, even though Content Understanding needs no Search resource at all
D. It must have Content Understanding Studio disabled to allow API-only access, despite Studio and the API being independent, coexisting surfaces
**Answer:** A — Content Understanding requires the GPT-4.1, GPT-4.1-mini, and text-embedding-3-large model deployments on the Foundry resource (a resource-level prerequisite, not SDK-specific), plus the endpoint and either an API key or Entra ID-based Foundry project access for authentication — regardless of whether you call it via SDK or REST.
