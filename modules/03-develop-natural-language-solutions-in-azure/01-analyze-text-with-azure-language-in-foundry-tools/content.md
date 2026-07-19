# Analyze text with Azure Language in Foundry Tools

Source: https://learn.microsoft.com/en-us/training/modules/analyze-text-ai-language/

Module info: 8 Units, Intermediate level, roles: AI Engineer / Developer, product: Microsoft Foundry.

## Learning objectives

In this module, you learn how to use Azure Language in Foundry Tools to:

- Detect language from text.
- Recognize named entities in text.
- Extract personally identifiable information (PII) in text.

Prerequisites: familiarity with Microsoft Azure and the Azure portal; programming experience.

## Exam relevance

Maps to **Implement text analysis solutions (10–15%)** in EXAM_SKILLS.md, specifically:
- "Apply language model text analysis" → "Implement solutions to extract entities, topics, summaries, and structured JSON outputs by using generative prompting and Foundry Tools" (entity extraction covered here via Azure Language's prebuilt NER).
- "Apply language model text analysis" → "Configure detection of sentiment, tone, safety issues, and sensitive content" (PII detection/redaction is the sensitive-content angle covered here).
- Also touches "Plan and manage an Azure AI solution" → "Configure security, including managed identity, private networking, keyless credentials, and role policies" (Microsoft Entra ID / DefaultAzureCredential vs key-based auth).

## Unit 1: Introduction

Every day the world generates a vast quantity of text-based data (emails, social media posts, online reviews, business documents). AI techniques applying statistical and semantic models let you build applications that extract meaning and insight from this text.

**Azure Language in Foundry Tools** provides an API for common text analysis techniques you can integrate into applications and agents.

You can develop text analytics applications using multiple language-specific SDKs:
- **Microsoft Azure Text Analytics Client Library for Python** — PyPI package `azure-ai-textanalytics`
- **Microsoft Azure Text Analytics Client Library for .NET** — NuGet package `Azure.AI.TextAnalytics`
- **Microsoft Azure Text Analytics Client Library for JavaScript** — npm package `@azure/ai-text-analytics`

Module examples use Python.

## Unit 2: Azure Language in Microsoft Foundry Tools

Azure Language in Foundry Tools is designed to extract information from text, providing functionality for:

- **Language detection** — determining the language in which text is written.
- **Named entity recognition (NER)** — detecting references to entities including people, locations, time periods, organizations, and more.
- **Personally Identifiable Information (PII) extraction** — identifying and redacting personal details in text.

> Note (exam-relevant distinction): Azure Language *also* provides functionality for **sentiment analysis, summarization, key phrase extraction**, and other common language-related tasks, but these are called out as **deprecated capabilities** provided only to support existing applications — the module's live/current focus is language detection, NER, and PII extraction/redaction.

### Using a Microsoft Foundry resource for text analysis

To use Azure Language in Foundry Tools, you must **provision a Microsoft Foundry resource** in your Azure subscription. After provisioning, you use the resource's **endpoint** to call the Azure Language APIs, authenticating via:
1. The **key** associated with the resource, or
2. A **Microsoft Entra ID** identity.

You can call the APIs either via **JSON REST requests** or via a **language-specific SDK**.

**Resource endpoint vs. project endpoint:** The Foundry portal home page shows endpoint/key for your *project*. To see the key/endpoint for the parent *resource*, view it under the **Admin** tab of the **Operate** page. The project and Foundry resource **keys are the same**; the **project endpoint = resource endpoint + `/api/projects/{project_name}`**.
- Example: project endpoint `https://my-ai-app-foundry.services.ai.azure.com/api/projects/my-ai-app` → resource endpoint `https://my-ai-app-foundry.services.ai.azure.com`.

### Authentication — key-based

```python
# run "pip install azure-ai-textanalytics" first to install the package 
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Create client using endpoint and key
credential = AzureKeyCredential("YOUR_FOUNDRY_RESOURCE_KEY")
client = TextAnalyticsClient(endpoint="YOUR_FOUNDRY_RESOURCE_ENDPOINT", 
                             credential=credential)
```

### Authentication — Microsoft Entra ID (recommended for production)

```python
# run "pip install azure-identity azure-ai-textanalytics" first to install the packages 
from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Create client using endpoint and default Azure identity
credential = DefaultAzureCredential()
client = TextAnalyticsClient(endpoint="YOUR_FOUNDRY_RESOURCE_ENDPOINT", 
                             credential=credential)
```

Key class: **`TextAnalyticsClient`** (package `azure.ai.textanalytics`). Microsoft explicitly recommends **Entra ID auth over key auth for greater security in production solutions**.

## Unit 3: Detect language

The **language detection API** evaluates text input and, for each document submitted, returns language identifiers with a confidence **score** (0–1).

Use cases:
- Content stores that collect arbitrary text where the language is unknown.
- Chat applications — detect the user's language at session start to configure responses appropriately.

**Limits:**
- Document size limit: **must be under 5,120 characters** per document.
- Each collection (batch request) is restricted to **1,000 items (IDs)**.

Request payload: a JSON body containing a collection of **documents**, each with a unique **id** and the **text** to analyze.

```python
# Assumes code to create TextAnalyticsClient is above...

# Example text to analyze
documents = ["Hello World!", "Bonjour le monde!"]

# Detect language
response = client.detect_language(documents=documents)
for doc in response:
    print(f"Document: {doc.id}")
    print(f"\tPrimary Language: {doc.primary_language.name}")
    print(f"\tISO6391 Name: {doc.primary_language.iso6391_name}")
    print(f"\tConfidence Score: {doc.primary_language.confidence_score}")
```

Output:
```
Document: 0
        Primary Language: English
        ISO6391 Name: en
        Confidence Score: 0.9
Document: 1
        Primary Language: French
        ISO6391 Name: fr
        Confidence Score: 0.98
```

Method: **`client.detect_language(documents=...)`**. Response fields per document: `doc.id`, `doc.primary_language.name`, `doc.primary_language.iso6391_name`, `doc.primary_language.confidence_score`.

**Edge cases:**
- **Mixed-language content** (e.g., `"I know a cool AI developer. He has a certain je ne sais quoi!"`): the API returns the language with the **largest representation** in the content, but with a **lower** confidence score reflecting the ambiguity.
- **Ambiguous/unparsable content** (e.g., due to character-encoding issues when converting text to a string): language name and ISO code are returned as **`(unknown)`**, and the confidence score is returned as **`0`**.

## Unit 4: Extract entities

**Named Entity Recognition (NER)** identifies entities mentioned in text, grouped into categories and subcategories, e.g.:
- Person
- Location
- DateTime
- Organization
- Address
- Email
- URL
- (Also seen in example output: **PersonType**, e.g., "CEO")

(Full category list lives in the separate NER concepts documentation, not reproduced verbatim on this unit page.)

```python
# Example text to analyze
documents = ["Microsoft was founded on April 4, 1975 by Bill Gates and Paul Allen in Albuquerque, New Mexico.",
             "Satya Nadella became CEO of Microsoft on February 4, 2014."]

# Extract named entities
response = client.recognize_entities(documents=documents)
for doc in response:
    print(f"Entities in document {doc.id}:")
    for entity in doc.entities:
        print(f" - {entity.text} ({entity.category})")
```

Output:
```
Entities in document 0:
 - Microsoft (Organization)
 - April 4, 1975 (DateTime)
 - Bill Gates (Person)
 - Paul Allen (Person)
 - Albuquerque (Location)
 - New Mexico (Location)
Entities in document 1:
 - Satya Nadella (Person)
 - CEO (PersonType)
 - Microsoft (Organization)
 - February 4, 2014. (DateTime)
```

Method: **`client.recognize_entities(documents=...)`**. Response: `doc.entities`, each with `.text` and `.category`.

## Unit 5: Extract personally identifiable information (PII)

Use case: identify and protect sensitive personal info in documents — e.g., removing PII from customer feedback, medical records, or legal documents before sharing.

Azure Language provides **PII detection and redaction** capabilities to identify sensitive information such as: names, addresses, phone numbers, email addresses, social security numbers, and credit card numbers. You can:
1. **Extract** PII entities for analysis, and/or
2. **Redact** (mask) them to protect privacy.

### Extracting PII entities

```python
# Example text to analyze
documents = ["John Smith works at Contoso Ltd. His email is john.smith@contoso.com and his phone number is 555-012-456.",
             "Patient Sarah Johnson, SSN 123-45-6789, was admitted on 03/15/2024."]

# Extract PII entities
response = client.recognize_pii_entities(documents=documents, language="en")
for doc in response:
    print(f"\nPII entities in document {doc.id}:")
    for entity in doc.entities:
        print(f" - {entity.text}: {entity.category} (confidence: {entity.confidence_score:.2f})")
```

Output:
```
PII entities in document 0:
 - John Smith: Person (confidence: 0.99)
 - Contoso Ltd: Organization (confidence: 0.85)
 - john.smith@contoso.com: Email (confidence: 1.00)
 - 555-012-456: PhoneNumber (confidence: 0.80)
PII entities in document 1:
 - Sarah Johnson: Person (confidence: 0.99)
 - 123-45-6789: USSocialSecurityNumber (confidence: 0.99)
 - 03/15/2024: DateTime (confidence: 0.80)
```

Method: **`client.recognize_pii_entities(documents=..., language="en")`** — note the explicit `language` parameter used here (vs. `recognize_entities` example, which didn't specify it). Response entities include `.text`, `.category`, `.confidence_score`.

Category names seen: `Person`, `Organization`, `Email`, `PhoneNumber`, `USSocialSecurityNumber`, `DateTime`.

### Redacting PII entities

The service can return a **redacted version of the text** with PII replaced by asterisks (or a specified character).

```python
# Redact PII entities
response = client.recognize_pii_entities(documents=documents, language="en")
for doc in response:
    print(f"\nDocument {doc.id} (redacted):")
    print(f" {doc.redacted_text}")
```

Output:
```
Document 0 (redacted):
 ********** works at ************. His email is ************************ and his phone number is ********.
Document 1 (redacted):
 Patient *************, SSN ***********, was admitted on **********.
```

Response field: **`doc.redacted_text`** — the same `recognize_pii_entities` call/response provides both the `.entities` list and the `.redacted_text` masked string; you don't need a separate API call to get redaction.

## Unit 6: Exercise — Analyze text

Hands-on exercise (~30 minutes): build a client application using Azure Language in Foundry Tools to analyze text. Requires an Azure subscription with administrative access. Delivered via an external lab launch link (go.microsoft.com/fwlink). Tip: delete Azure resources created during the exercise once done exploring.

## Unit 7: Module assessment

Standard graded knowledge-check quiz (no extractable content beyond the quiz itself — must be taken interactively on Microsoft Learn).

## Unit 8: Summary

Recap of what was learned:
- Detect language from text.
- Recognize named entities in text.
- Extract personally identifiable information (PII) in text.

Further reading pointer: **Azure Language in Foundry Tools documentation** (`/en-us/azure/ai-services/language-service`).
