# Analyze images with Content Understanding

Source: https://learn.microsoft.com/en-us/training/modules/analyze-images-with-content-understanding/

Level: Intermediate | Role: AI Engineer | Product: Microsoft Foundry | 6 Units

## Learning objectives

After completing this module, you'll be able to:

- Deploy a content-understanding AI model in Microsoft Foundry.
- Test an image-based prompt in the chat playground.
- Use the Azure OpenAI SDK to analyze images in Python.

(Note: the module's actual unit content — see below — is centered on Azure Content Understanding's analyzer/schema model rather than raw Azure OpenAI SDK image calls; the stated objectives above are the verbatim text from the module overview page, included as-is per source, but the unit walkthroughs actually teach the `azure-ai-contentunderstanding` Python SDK and analyzer JSON schemas, not the Azure OpenAI SDK directly.)

**Prerequisites:** Experience with deploying generative AI models in Microsoft Foundry; programming experience.

## Exam relevance

Maps to **Implement computer vision solutions (10-15%)** — "Design and implement multimodal understanding workflows":
- Implement visual understanding by configuring Azure Content Understanding in Foundry Tools to extract visual characteristics
- Configure single-task and pro-mode Content Understanding pipelines *(NOT explicitly covered in this module's unit text — see Gap note below)*
- Implement solutions that identify objects, components, or regions within images or video (via grounding)
- Build a solution that analyzes visual context using multimodal models

Maps to **Implement information extraction solutions (10-15%)** — "Extract content from documents":
- Extract information using multimodal pipelines that combine OCR, layout analysis, and field extraction (Content Understanding's "content extraction" stage)
- Produce clean, grounded representations for agents/RAG using Content Understanding (markdown output, grounding regions)
- Implement analyzers for generating structured or markdown outputs using Content Understanding (analyzer JSON schema, `markdown` vs `fields` output)

Also touches **Choose the appropriate Foundry services for generative AI and agents** (Plan and manage an Azure AI solution, 25-30%): Content Understanding is explicitly named a **Foundry Tool**, relevant to "Choose appropriate memory, tool, and knowledge integration services for agent solutions" and "Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions" (Implement generative AI and agentic solutions, 30-35%).

Also touches **Implement responsible AI for multimodal content**: Content Understanding integrates Azure AI Content Safety, filters harmful content, and has specific rules around biometric/face data — relevant to "Implement filters to classify unsafe or disallowed visual content."

**GAP NOTE:** The exam skill "Configure single-task and pro-mode Content Understanding pipelines" is NOT mentioned anywhere in this module's unit content (units 1-6 fetched verbatim below contain no reference to "single-task" or "pro-mode"). This concept must be covered from another module/source — flagging for the orchestrator/GAPS file.

---

## Unit 1: Introduction

Images, documents, and other unstructured content often contain valuable information that's hard to extract automatically. **Azure Content Understanding** solves this problem by using generative AI to analyze content and return structured data.

With Content Understanding, you define a **schema** describing the data you want, and the service extracts it from your images and documents. The output is ready to use in automation workflows, analytics, and search applications.

The module teaches how to analyze images with Content Understanding using both **prebuilt** and **custom analyzers**.

---

## Unit 2: What is Content Understanding?

**Azure Content Understanding is a Foundry Tool** that uses generative AI to process and extract insights from many types of content, including **documents, images, videos, and audio**. It transforms unstructured data into structured, actionable output that you can integrate into automation and analytical workflows.

### Why use Content Understanding?

Content Understanding accelerates time to value by enabling straight-through processing of unstructured data. Key benefits:

- **Simplified workflows**: Standardizes extraction and classification of content from various content types into a unified process
- **Easy field extraction**: Define a schema to extract, classify, or generate field values without complex prompt engineering
- **Enhanced accuracy**: Uses multiple AI models to analyze and cross-validate information simultaneously
- **Confidence scores and grounding**: Ensures accuracy of extracted values while minimizing the cost of human review
- **Content classification**: Categorize document types to streamline processing and route content to appropriate analyzers

### Content Understanding components (pipeline stages)

| Component | Description |
| --- | --- |
| **Inputs** | Source content including documents, images, video, and audio |
| **Analyzer** | Defines how content is processed, including extraction settings and field schema |
| **Content extraction** | Transforms unstructured input into normalized text and metadata using OCR, speech transcription, and layout detection |
| **Field extraction** | Generates structured key-value pairs based on your defined schema |
| **Confidence scores** | Provides reliability estimates from 0 to 1 for each extracted field value |
| **Grounding** | Identifies specific regions in content where each value was extracted |
| **Structured output** | Final result as **Markdown** for search scenarios or **JSON** for automation workflows |

### Analyzers

**Analyzers are the core component that defines how your content is processed.** Content Understanding offers two types:

- **Prebuilt analyzers**: Ready-to-use analyzers designed for common scenarios like invoice processing, receipt extraction, and call center analytics
- **Custom analyzers**: Tailored analyzers you create with your own field schema for specific business needs

When you create an analyzer, you configure:

- The base analyzer type (**document, image, audio, or video**)
- The AI models to use for processing
- The field schema that defines what data to extract
- Options like confidence scoring and content segmentation

### Use cases

| Use case | Description |
| --- | --- |
| **Intelligent document processing** | Convert unstructured documents into structured data for invoice processing, contract analysis, and claims management |
| **Search and RAG** | Ingest multimodal content into search indexes with figure descriptions and layout analysis |
| **Agentic applications** | Transform messy file inputs into predictable, standardized inputs for AI agents |
| **Analytics and reporting** | Extract field outputs to gain insights and make informed decisions |

### Content restrictions (Responsible AI)

Content Understanding includes built-in Responsible AI protections. The service **integrates Azure AI Content Safety** to detect and prevent harmful content:

- Content is filtered for harmful material including violence, hate speech, and exploitation
- **Face description capabilities** can identify facial attributes in video and image content
- **Biometric data processing** requires appropriate notice and consent from data subjects

---

## Unit 3: Analyze images with Content Understanding

Content Understanding can analyze images to extract structured data, identify visual elements, and generate descriptions. You can use prebuilt analyzers for common scenarios or create custom analyzers tailored to your specific needs.

### Supported image formats

| Format | Description |
| --- | --- |
| **JPEG** | Standard photographic images |
| **PNG** | Images with transparency support |
| **BMP** | Bitmap images |
| **TIFF** | High-quality scanned documents |
| **HEIF** | High-efficiency image format |
| **PDF** | Single or multi-page documents with embedded images |

### Prebuilt image analyzers (exact names)

- **`prebuilt-image`**: General-purpose image analysis with content extraction and figure description
- **`prebuilt-receipt`**: Extract vendor names, items, totals, and dates from receipt images
- **`prebuilt-invoice`**: Extract invoice details including line items, amounts, and vendor information
- **`prebuilt-idDocument`**: Extract information from identity documents like driver's licenses and passports

### Define a field schema for images

To extract specific information from images, define a **field schema** that describes the data you want. Each field can use one of **three extraction methods**:

| Method | Description | Example |
| --- | --- | --- |
| **extract** | Pull values directly as they appear in the image | Extract text from a label or sign |
| **classify** | Categorize content from predefined options | Classify image as "damaged" or "undamaged" |
| **generate** | Create values based on image analysis | Generate a description of the scene |

Example schema for analyzing product images:

```json
{
  "description": "Product image analyzer",
  "baseAnalyzerId": "prebuilt-image",
  "fieldSchema": {
    "fields": {
      "ProductName": {
        "type": "string",
        "method": "extract",
        "description": "Name of the product visible in the image"
      },
      "Condition": {
        "type": "string",
        "method": "classify",
        "description": "Condition of the product",
        "enum": ["new", "used", "damaged"]
      },
      "Description": {
        "type": "string",
        "method": "generate",
        "description": "Brief description of what the image shows"
      }
    }
  }
}
```

Note the schema fields: `description` (analyzer description), `baseAnalyzerId` (points to a prebuilt analyzer to extend, e.g. `prebuilt-image`), `fieldSchema.fields` (a map of field name → field definition), each field has `type` (e.g. `"string"`), `method` (`extract` | `classify` | `generate`), `description`, and for `classify` fields an `enum` array of allowed categories.

### Analyze an image — Python SDK

Install the SDK via pip:

```bash
pip install azure-ai-contentunderstanding
```

Submit a request to the analyze endpoint with your analyzer ID and the image URL or file:

```python
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, AnalysisResult
from azure.core.credentials import AzureKeyCredential # for key-based authentication
from azure.identity import DefaultAzureCredential # for Entra ID authentication

# Get a client
credential = AzureKeyCredential(key)
client = ContentUnderstandingClient(endpoint={FOUNDRY_ENDPOINT},
                                    credential={KEY_OR_IDENTITY},
                                    api_version="2025-11-01")

# Analyze an image file
with open("my_image.png", "rb") as f:
            file_bytes = f.read()

try:
    poller = client.begin_analyze(
        analyzer_id={ANALYSER_ID},
        inputs=[AnalysisInput(data=file_bytes)],
    )
    # Get results asynchronously from poller
    result: AnalysisResult = poller.result()

    # Display results
    result_str = json.dumps(result.as_dict(), indent=2)
    print (result_str)

except Exception as ex:
    print(f"[Unexpected Error]: {ex}")
    sys.exit(1)
```

**Exact SDK/API names to remember:**
- Package: `azure-ai-contentunderstanding` (pip package)
- Client class: `ContentUnderstandingClient`
- Models: `AnalysisInput`, `AnalysisResult`
- Auth options: `AzureKeyCredential` (key-based, from `azure.core.credentials`) or `DefaultAzureCredential` (Entra ID, from `azure.identity`)
- Client constructor params: `endpoint`, `credential`, `api_version` (example value: `"2025-11-01"`)
- Method: `client.begin_analyze(analyzer_id=..., inputs=[AnalysisInput(data=file_bytes)])` — this is a **long-running operation returning a poller**; call `.result()` on the poller to get the `AnalysisResult` synchronously/asynchronously.
- Result access: `result.as_dict()` to serialize to a plain dict/JSON.

### Analysis output structure

When analysis completes, the results include:

- **`markdown`**: A text representation of the image content, useful for search and RAG scenarios
- **`fields`**: Extracted field values matching your schema, each with a confidence score
- **`source`**: Grounding information showing where in the image each value was found

Example response for a product image:

```json
{
  "contents": [
    {
      "markdown": "Product label showing 'Contoso Widget Pro' with serial number...",
      "fields": {
        "ProductName": {
          "type": "string",
          "valueString": "Contoso Widget Pro",
          "confidence": 0.95,
          "source": "D(1,100,50,300,50,300,80,100,80)"
        },
        "Condition": {
          "type": "string",
          "valueString": "new",
          "confidence": 0.89
        },
        "Description": {
          "type": "string",
          "valueString": "A silver electronic device in retail packaging with product label visible"
        }
      }
    }
  ]
}
```

Note the top-level `contents` array (one entry per page/segment), each containing `markdown`, and a `fields` object keyed by your schema's field names. Each field result has `type`, a `value<Type>` (e.g. `valueString`), `confidence` (float 0-1), and optionally `source` (the grounding/bounding coordinate string — a polygon expressed as `D(page,x1,y1,x2,y2,x3,y3,x4,y4)`-style coordinates identifying the region in the content where the value was extracted).

### Use confidence scores

Each extracted field includes a **confidence score from 0 to 1**:

- **High confidence (0.9+)**: Value can be trusted for automated processing
- **Medium confidence (0.7-0.9)**: Consider human review for critical applications
- **Low confidence (<0.7)**: Recommend manual verification

Use confidence scores to build automation workflows that route low-confidence extractions to human reviewers while processing high-confidence results automatically.

### Tips for better image analysis

- **Image quality matters**: Higher resolution images produce more accurate extractions
- **Lighting and contrast**: Ensure text and visual elements are clearly visible
- **Single focus**: Images with one clear subject yield better results than cluttered scenes
- **Consistent orientation**: Upright images are processed more reliably than rotated ones

---

## Unit 4: Exercise — Analyze images with Content Understanding

In this hands-on exercise (30 minutes), you:

1. Create a **custom image analyzer in the Microsoft Foundry portal**.
2. Create a **Python application** that uses the Content Understanding API to analyze images programmatically and extract structured data.

Requires an Azure subscription (free account with 30-day credits available). The exercise is launched via an external fwlink to a hosted lab environment (not further content extractable from the static page — the actual lab steps live in the interactive sandbox, not in the fetched page HTML).

---

## Unit 5: Module assessment (knowledge check)

The module's official knowledge check includes these three graded questions (verbatim from the page; correct answers are the ones matching the content in Units 2-3, though the fetched page did not visually flag which option is graded-correct — inferred from unit content and marked below):

1. **What is the purpose of grounding in Content Understanding?**
   - To connect Content Understanding to Azure storage
   - To identify the specific regions in content where each value was extracted *(correct per Unit 2's component table)*
   - To filter out harmful content from images

2. **What does a confidence score of 0.95 indicate for an extracted field?**
   - The extraction failed and needs manual review
   - The value can be trusted for automated processing *(correct — falls in the "High confidence (0.9+)" band from Unit 3)*
   - The field was classified rather than extracted

3. **Which prebuilt analyzer would you use to extract vendor names and item totals from a purchase receipt?**
   - prebuilt-image
   - prebuilt-invoice
   - prebuilt-receipt *(correct per Unit 3's prebuilt analyzer table — "Extract vendor names, items, totals, and dates from receipt images")*

---

## Unit 6: Summary

In this module, you learned how to analyze images using Azure Content Understanding in Microsoft Foundry. You explored how to:

- Understand the components of Content Understanding, including analyzers, field extraction, and confidence scores
- Use prebuilt analyzers for common scenarios like receipts, invoices, and identity documents
- Define field schemas with extract, classify, and generate methods
- Analyze images using the Content Understanding API

Content Understanding transforms unstructured visual content into structured, actionable data. By defining a schema and using prebuilt or custom analyzers, you can automate image analysis for document processing, inventory management, quality inspection, and other business scenarios.

**Further reading pointer (from the module):** [What is Azure Content Understanding?](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) in the Azure AI documentation.

---

## Key exam distinction: Content Understanding vs Azure AI Vision (Image Analysis) vs raw multimodal-LLM vision vs Document Intelligence

This is not explicitly spelled out as a comparison table in the module text, but is synthesized here from the module's content plus well-established Azure knowledge (flagged as general knowledge, not module-sourced, where noted):

| Aspect | **Azure Content Understanding** (this module) | **Azure AI Vision — Image Analysis API** (general Azure knowledge) | **Raw multimodal LLM vision call** (e.g., GPT-4o via Azure OpenAI/Foundry — see Module 1) | **Azure AI Document Intelligence** (Module 7 — general Azure knowledge) |
| --- | --- | --- | --- | --- |
| What it is | A **Foundry Tool**: generative-AI-powered content pipeline that produces **schema-defined structured output** (JSON/Markdown) from images, documents, video, and audio | A dedicated computer-vision REST API/SDK with **fixed, pre-built output types**: captions, dense captions, tags, object detection, people detection, OCR "Read" | Free-form prompting of a large multimodal model with an image as input; output is whatever the prompt asks for, unconstrained unless you add structured-output/JSON-mode constraints yourself | Document/OCR-centric service specializing in **layout extraction** (tables, key-value pairs, selection marks) from scanned documents/forms, with prebuilt models (invoice, receipt, ID, W-2, etc.) and custom-trained models |
| Output shape | You **define a field schema** (`extract` / `classify` / `generate` methods); output includes `markdown`, `fields` (with `confidence` and `source`/grounding), configurable per-analyzer | Fixed output object per feature you request (e.g., `tags`, `caption`, `objects`, `read.blocks`) — not customizable per business schema | Unstructured text response (or structured only if you engineer a JSON schema / function-calling response format yourself) | Fixed layout/field schema per model (prebuilt invoice fields, or your custom-trained fields), strong on tables/forms/key-value pairs |
| Configurability | High — build **custom analyzers** with your own fields, extraction methods, base analyzer type (document/image/audio/video); also has **prebuilt analyzers** (`prebuilt-image`, `prebuilt-receipt`, `prebuilt-invoice`, `prebuilt-idDocument`) | Low — you toggle which fixed visual-feature outputs to request (tags, caption, objects, OCR), no custom schema | Very high (free-form) but no built-in confidence/grounding structure — you must build that yourself | Medium — customizable via custom model training, but schema still centers on document layout/fields, not generic image scene description |
| Confidence & grounding | **Built-in**: every field gets a confidence score (0-1) and a `source` grounding region (bounding coordinates) | Some features return confidence (e.g., tags, objects) but no unified schema-level grounding across a custom field set | Not built-in — no native confidence scoring or bounding-box grounding for free-form answers | Built-in confidence + bounding boxes per extracted field/table cell, similar concept but document-oriented |
| Typical use case | Multimodal RAG ingestion, agent input normalization, structured extraction from mixed content types (docs+images+video+audio) with one consistent pipeline | Quick, cheap, fixed captions/tags/object detection/OCR without needing a custom schema | Open-ended visual reasoning, Q&A, complex scene understanding, accessibility alt-text generation | Structured document/form data extraction (invoices, receipts, IDs, contracts, forms) — historically document/OCR-only, no video/audio |
| Modalities supported | Documents, **images**, video, audio (multimodal, one framework) | Images only (and OCR "Read" over images/PDFs) | Whatever the model natively accepts (image, sometimes video frames) | Documents/images/PDFs (primarily document-shaped content); no native audio/video |

**Exam-critical takeaway:** If a question describes needing a **custom schema of fields extracted from images with confidence scores and grounding**, and possibly across multiple modalities (image + doc + audio/video) in one unified pipeline → **Azure Content Understanding**. If it describes **fixed outputs like tags/captions/objects/OCR read** with no custom schema → **Azure AI Vision Image Analysis**. If it describes **open-ended free-form reasoning/Q&A about an image** → **multimodal LLM vision call (e.g., GPT-4o)**. If it's specifically about **forms/invoices/receipts/tables with heavy OCR+layout emphasis** and no video/audio requirement → **Document Intelligence** (though Content Understanding's `prebuilt-invoice`/`prebuilt-receipt` analyzers overlap functionally — Content Understanding is positioned as the newer, broader, schema-driven successor pattern that also handles images/video/audio, not just documents).
