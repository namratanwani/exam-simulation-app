# Extract data with Azure Document Intelligence

Source: https://learn.microsoft.com/en-us/training/modules/extract-data-with-document-intelligence/

Module: 8 units, Intermediate level. Part of Learning Path 4 "Extract insights from visual data on Azure" (Module 7).
Product tags on the module: Foundry Tools, Azure AI Document Intelligence, Microsoft Foundry.

Module description (from overview page): "Azure Document Intelligence uses OCR and deep learning models to extract text, key-value pairs, tables, and structured data from forms and documents. Learn how to use prebuilt and custom models to automate document processing."

Prerequisites: Familiarity with Azure and the Azure portal; programming experience with C# or Python.

## Learning objectives

By the end of this module, you'll be able to:

- Describe the capabilities and components of Azure Document Intelligence.
- Use the Document Intelligence Studio to explore and test models.
- Use prebuilt models to extract data from common document types.
- Train and use custom models for industry-specific forms.

## Exam relevance

Maps to **Implement information extraction solutions (10–15%)**, in EXAM_SKILLS.md:

- **Build retrieval and grounding pipelines** — "Ingest and index content, such as documents, images, audio, and video"; "Implement enrichment by using custom or built-in skills for text, images, and layout"; "Configure RAG ingestion flow, including documents and using OCR." Document Intelligence's read/layout models are a primary OCR + layout enrichment mechanism you'd wire into a RAG ingestion pipeline (e.g., as a custom skill in Azure AI Search, or as a preprocessing step before chunking/embedding).
- **Extract content from documents** — "Extract information by using multimodal pipelines that combine OCR, layout analysis, and field extraction." Document Intelligence is the classic, purpose-built service for this bullet, though the exam skill text explicitly calls out **Content Understanding** for "clean, grounded representations" and "structured or markdown outputs for downstream reasoning" — meaning the exam expects you to know when Document Intelligence (structured field/table/KV extraction, prebuilt/custom document models) is the right choice vs. when Content Understanding (multimodal analyzers, schemas, markdown output, pro-mode) is the right choice. See the dedicated comparison section below.
- Indirectly relevant to **Plan and manage an Azure AI solution** — "Choose the appropriate Foundry services ... for grounding ... or multimodal processing" (choosing Document Intelligence vs. Content Understanding vs. Azure AI Vision Read is exactly this kind of service-selection decision) and to "Configure security, including managed identity, private networking, keyless credentials, and role policies" (resource creation options below).

## Unit 1: Introduction

Scenario framing: a company processes thousands of invoices, receipts, and tax forms monthly and wants to automate key-data extraction to reduce manual effort and improve accuracy.

**Definition:** Azure Document Intelligence is a cloud-based service **in Microsoft Foundry** that uses **optical character recognition (OCR)** and deep learning models to extract text, key-value pairs, tables, and structured data from forms and documents.

Three capability categories introduced here (detailed later):
- Prebuilt models for common document types.
- Document analysis models for general text extraction.
- Ability to train custom models for your specific forms.

## Unit 2: What is Azure Document Intelligence?

**Azure Document Intelligence** = cloud-based AI service in Microsoft Foundry using OCR + deep learning to extract text, key-value pairs, selection marks, and tables from documents.

- OCR captures document structure by creating **bounding boxes** around detected objects in an image; bounding box locations are recorded as coordinates relative to the page.
- Output format: structured **JSON** that preserves relationships from the original document.
- Building a high-accuracy extraction model from scratch requires deep learning expertise, large compute, and long training times — Document Intelligence's prebuilt models are already trained on thousands of form examples, giving high accuracy with minimal effort.

### Document Intelligence service components (three categories)

1. **Document analysis models** — extract text, structure, tables, and selection marks from documents.
   - **read** model: extracts text, detects languages.
   - **layout** model: adds table and structure extraction on top of read.
2. **Prebuilt models** — extract information from common document types (invoices, receipts, tax forms, ID documents, etc.) with **no training required**.
3. **Custom models** — extract data from forms specific to your business using your own labeled datasets. Options: custom template models, custom neural models, composed models, and custom classifiers.

### Access methods

- **REST API** — direct HTTP calls.
- **Client library SDKs** — Python, C#, Java, and JavaScript.
- **Document Intelligence Studio** — online visual tool for exploring, testing, building solutions.
- **Microsoft Foundry portal** — integrates Document Intelligence with other Foundry tools.

> Tip called out in the module: the module's exercise focuses on the **Python SDK**; underlying REST services can be used by any language.

### Creating a resource — two options

- **Foundry resource**: multi-service subscription providing access to multiple AI services under a single endpoint and key.
- **Azure Document Intelligence resource**: single-service resource used only with Document Intelligence.

Guidance: create a Foundry resource if you plan to access multiple Foundry tools under one endpoint/key; create a dedicated Document Intelligence resource for Document-Intelligence-only access.

### Input requirements (exact limits — memorize for exam)

- Formats: **JPEG, PNG, BMP, PDF** (text or scanned), or **TIFF**. The **read** model also accepts Microsoft Office file formats.
- File size: **< 500 MB** (standard tier) / **< 4 MB** (free tier).
- Image dimensions: between **50 x 50 pixels** and **10,000 x 10,000 pixels**.
- PDF dimensions: less than **17 x 17 inches** (A3 paper size).
- PDF documents must **not be password-protected**.

Learn-more links cited: `/azure/ai-services/document-intelligence/overview`, `/azure/ai-services/document-intelligence/model-overview`.

## Unit 3: Use the Document Intelligence Studio

**Document Intelligence Studio** — online tool for visually exploring, understanding, and integrating Document Intelligence features: analyze form layouts, extract data with prebuilt models, train custom models, all via a visual interface.

**URL: https://documentintelligence.ai.azure.com**

### Studio project types

- **Document analysis models** — test read and layout models against your own documents (view extracted text, tables, structure).
- **Prebuilt models** — analyze documents using any available prebuilt model (invoices, receipts, ID documents, tax forms, etc.).
- **Custom models** — build, label, train, and test custom extraction models and custom classifiers.

### Workflow: analyze documents with prebuilt models (in Studio)

1. Create an Azure Document Intelligence or Foundry Tools resource in the Azure portal.
2. Open the Studio and select a prebuilt model (e.g., Invoice, Receipt, or ID Document).
3. Provide your resource **endpoint and key**.
4. Upload or provide a URL to the document to analyze.
5. Review extracted fields and their **confidence scores**.

### Workflow: build custom model projects (in Studio)

The Studio handles the entire labeling/training/testing process **without manually creating JSON files** — it auto-generates the required `ocr.json`, `labels.json`, and `fields.json` files.

1. Create an Azure Document Intelligence or Foundry resource.
2. Upload **at least 5–6 sample forms** to an Azure Blob Storage container.
3. Configure **CORS** (cross-origin resource sharing) so the Studio can access the storage container.
4. Create a custom model project in the Studio, linking the storage container and Document Intelligence resource.
5. Label fields in sample documents using the Studio's visual interface.
6. Train the model and review accuracy metrics.
7. Test the model against a new document not used during training.

### Add-on capabilities (optional, some are premium/extra cost)

| Capability | Description |
| --- | --- |
| High resolution extraction | Extract text from high-resolution documents with greater accuracy. |
| Formula extraction | Detect and extract mathematical formulas. |
| Font property extraction | Extract font information — style, weight, color. |
| Barcode extraction | Detect and read barcodes. |
| Searchable PDF | Convert scanned documents into searchable PDF files. |
| Query fields | Use natural language queries to extract specific fields. |
| Key-value pairs | Extract key-value pair relationships using the layout model. |

Learn-more links: Studio URL, `/azure/ai-services/document-intelligence/concept-add-on-capabilities`.

## Unit 4: Use prebuilt models

Prebuilt models extract data from common form types **with no training required**; Microsoft trains them on large numbers of sample documents for accurate, reliable results on standard document types.

### Document analysis models (the foundation prebuilt models build on)

**Read model**
- Extracts printed and handwritten text from documents/images.
- Detects the **language** of each text line.
- Classifies whether text is **handwritten or printed**.
- Used as the foundation for text extraction in all other Document Intelligence models.
- Supports a **`pages`** parameter for multi-page PDF/TIFF files, to specify a page range to analyze.
- Ideal for documents with **no fixed or predictable structure**.

**Layout model**
- Extends read's text extraction with detection of **selection marks, tables, and document structure**.
- Supports an optional **`keyValuePairs`** feature to extract key-value pairs.
- Handles angled scans and complex table structures (merged cells, incomplete rows).
- Each table cell extracted with: content, bounding box position, row/column indexes.
- Selection marks (checkboxes/radio buttons) extracted with: bounding box, confidence level, whether selected.

> **Note (deprecation):** The *general document model* existed in earlier Document Intelligence versions but was **deprecated in the `2023-10-31-preview` release**. Its key-value pair / entity extraction functionality was folded into the **layout model** and other features. (Exam relevance: if you see "general document model" as an answer option, treat it as legacy/deprecated — the layout model is the current answer.)

### Prebuilt models for specific document types

**Financial and legal documents**

| Model | Description |
| --- | --- |
| Invoice | Customer name, vendor details, PO number, invoice/due dates, billing/shipping addresses, line items, totals. |
| Receipt | Merchant details, transaction date/time, line items, totals. Supports single-page hotel receipt processing. |
| Bank statement | Account information, beginning/ending balances, transaction details. |
| Check | Payee, amount, date, other relevant info. |
| Pay stub | Wages, hours, deductions, net pay, other common fields. |
| Credit card | Payment card information. |
| Contract | Agreement and party details. |

**US tax documents**

| Model | Description |
| --- | --- |
| Unified US tax | Single model extracting from any supported US tax form type. |
| W-2 | Taxable compensation details. |
| 1098 (and variations) | Mortgage interest and related details. |
| 1099 (and variations) | Income from various sources. |
| 1040 (and variations) | Individual income tax return details. |

**US mortgage documents**

| Model | Description |
| --- | --- |
| 1003 (URLA) | Loan application details. |
| 1004 (URAR) | Property appraisal information. |
| 1005 | Validation-of-employment information. |
| 1008 | Loan transmittal details. |
| Closing disclosure | Final closing loan terms. |

**Personal identification documents**

| Model | Description |
| --- | --- |
| ID document | US driver's licenses, EU IDs/driver's licenses, international passports — names, DOB, document numbers, endorsements/restrictions. |
| Health insurance card | Common fields from US health insurance cards. |
| Marriage certificate | Certified marriage information. |

> **Important (compliance):** The ID document model extracts personal information covered by data protection laws in most jurisdictions — ensure you have the individual's permission to store their data and comply with applicable legal requirements.

> Note: the module lists prebuilt models by category/description rather than by their literal API model-ID strings (e.g. `prebuilt-invoice`). The `prebuilt-<name>` ID convention (`prebuilt-read`, `prebuilt-layout`, `prebuilt-invoice`, `prebuilt-receipt`, `prebuilt-idDocument`, `prebuilt-businessCard` [retired in some regions/versions — verify current availability], `prebuilt-tax.us.*`, `prebuilt-contract`, `prebuilt-healthInsuranceCard.us`, `prebuilt-check.us`) is documented in the official Document Intelligence model-overview reference and is the identifier you pass as `modelId`/`model_id` to `AnalyzeDocument`/`begin_analyze_document`. Know the mapping between plain-English model name (as used in this module) and its `prebuilt-*` ID for the exam.

### Features common across prebuilt models

- **Text extraction**: all prebuilt models extract lines and words from handwritten and printed text.
- **Key-value pairs**: spans of text identifying a label and its response (e.g., **Weight** → **31 kg**).
- **Selection marks**: checkboxes/radio buttons, including selected state.
- **Tables**: cell data, column/row counts, headings, merged cells.
- **Fields**: models trained for a specific form type identify a fixed set of fields (e.g., invoice model extracts `CustomerName` and `InvoiceTotal`).

### When to use prebuilt vs. custom models

Prebuilt models cover the most common document types. For an industry-specific or unique form type, a **custom model** may give more accurate results — but custom models require time and sample data to train. **Always check whether a prebuilt model exists for your scenario before investing in custom model development.**

Learn-more links: model-overview, prebuilt read, prebuilt layout, prebuilt invoice, prebuilt receipt, prebuilt ID document.

## Unit 5: Train and use custom models

Used when prebuilt models don't cover your specific document types. Azure Document Intelligence supports **supervised machine learning**: you label sample documents with the fields to extract, and the service trains a model to recognize those fields in new documents.

### Custom model types (two extraction types + one classification type)

**Custom template models**
- Rely on a **consistent visual template** to extract labeled data.
- Best for structured forms with a static layout across instances (questionnaires, applications, standard government forms).
- Accurately extract: labeled key-value pairs, selection marks, tables, regions, and **signatures**.
- Training takes **only a few minutes**.
- **100+ languages** supported.
- Fast to train, cost-effective to run — good starting point for uniform-layout documents.

**Custom neural models**
- Use **deep learning**, fine-tuned on your labeled data.
- Combine layout + language features to extract fields from **structured, semi-structured, and unstructured** documents.
- Support: overlapping fields, signature detection, table/row/cell-level confidence.
- Higher accuracy than template models, especially for semi-structured/unstructured documents with varying layout.
- Take longer to train, consume more resources; support fewer languages than template models.

**Comparison table (from the module):**

| Factor | Custom template | Custom neural |
| --- | --- | --- |
| Best for | Structured forms, consistent visual layout | Semi-structured/unstructured docs, varying layouts |
| Training time | Minutes | Longer (depends on dataset size) |
| Training cost | Lower | Higher |
| Accuracy | High for fixed-layout forms; decreases as layout varies | Higher overall, esp. with format variation |
| Language support | 100+ languages | Fewer languages (check docs for current support) |
| Feature support | Key-value pairs, selection marks, tables, regions, signatures | Overlapping fields, signature detection, table/row/cell confidence |

> Guidance: start with a **custom template model** if forms have a consistent visual layout (faster/cheaper). If accuracy is insufficient or documents vary in format, switch to a **custom neural model**.

**Custom classifiers**
- Identify the **type** of a document before invoking an extraction model.
- Used to route incoming documents to the appropriate extraction model when handling multiple form types.

### Train a custom model (REST/SDK workflow)

1. Store sample forms in an Azure blob container, plus JSON files with layout/label info:
   - `ocr.json` — one per sample form (generated via the Analyze document function).
   - `fields.json` — single file describing fields to extract.
   - `labels.json` — one per sample form, mapping fields to their location in the form.
2. Generate a **shared access signature (SAS) URL** for the container.
3. Call the **Build model** REST API function (or equivalent SDK method).
4. Call the **Get model** REST API function to retrieve the trained model ID.

(Alternatively, train visually via the Document Intelligence Studio — no manual JSON authoring needed, per Unit 3.)

> Tip: use **at least 5–6 sample forms** for training; a larger, more varied dataset produces more accurate models.

### Use a custom model — call Analyze document with your model ID

C# example (uses `DocumentAnalysisClient`, `AnalyzeDocumentFromUriAsync`, `AnalyzeDocumentOperation`, `AnalyzeResult`):

```csharp
string endpoint = "<endpoint>";
string apiKey = "<apiKey>";
AzureKeyCredential credential = new AzureKeyCredential(apiKey);
DocumentAnalysisClient client = new DocumentAnalysisClient(new Uri(endpoint), credential);

string modelId = "<modelId>";
Uri fileUri = new Uri("<fileUri>");

AnalyzeDocumentOperation operation = await client.AnalyzeDocumentFromUriAsync(WaitUntil.Completed, modelId, fileUri);
AnalyzeResult result = operation.Value;
```

Python example (uses `DocumentAnalysisClient`, `begin_analyze_document_from_url`):

```python
endpoint = "YOUR_DOC_INTELLIGENCE_ENDPOINT"
key = "YOUR_DOC_INTELLIGENCE_KEY"

model_id = "YOUR_CUSTOM_BUILT_MODEL_ID"
formUrl = "YOUR_DOCUMENT"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

task = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = task.result()
```

A successful response returns an **`analyzeResult`** object containing extracted content and an array of **pages** with document information.

> SDK naming note: this module's code samples use the (older, GA) **`DocumentAnalysisClient`** class with `AnalyzeDocumentFromUriAsync`/`begin_analyze_document_from_url`. Newer Document Intelligence SDK versions expose a **`DocumentIntelligenceClient`** with an `AnalyzeDocument`/`begin_analyze_document` method that returns similar `AnalyzeResult` output (fields, tables, key-value pairs, styles, pages, paragraphs). Be prepared for exam items referencing either class name — know that both target the same `analyzeResult` JSON shape (fields with confidence scores, tables with cell bounding regions, key-value pairs, selection marks, bounding regions/polygons per page).

### Composed models

You can combine multiple custom models into a single **composed model**. When a document is submitted to a composed model, Document Intelligence **classifies it** to determine the most appropriate component model, then returns extraction results from that model. Useful when handling multiple form types that each need their own extraction model (alternative/complement to a standalone custom classifier).

Learn-more links: custom models, custom neural models, custom template models, composed models.

## Unit 6: Exercise — Analyze documents with Document Intelligence

Hands-on lab (external, via a launch link) where you use Azure Document Intelligence to analyze documents using both a **prebuilt model** and a **custom model**. Requires an Azure subscription with administrative access. Reminder: delete created Azure resources after finishing.

(Exercise content itself is hosted externally and not reproducible here — no additional technical detail on this unit's page beyond the launch link.)

## Unit 7: Module assessment (knowledge check)

Three graded questions on the official module (topics, for awareness — this module's own knowledge check, distinct from the practice questions in questions.md):

1. Model choice for extracting text and table structure from varying-format documents without labeled fields → **the layout model** (vs. read model, vs. invoice model).
2. Required training artifacts for REST API custom model training → **sample forms plus `ocr.json`, `labels.json`, and `fields.json` files in a blob container** (not just raw forms; not "100 labeled forms + trained classifier").
3. Routing invoices and receipts to the correct extraction model behind a single endpoint → **a composed model, or a custom classifier paired with extraction models** (not a custom neural model alone; not the prebuilt read model).

## Unit 8: Summary

Recap of what you learned:
- Capabilities/components of Azure Document Intelligence: document analysis, prebuilt, and custom models.
- Using Document Intelligence Studio to visually explore/test/build document processing solutions.
- Using prebuilt models for common document types (invoices, receipts, tax forms, ID documents).
- Training/using custom template and neural models for industry-specific forms.

Positioning note (from the module): "Azure Document Intelligence is one part of the broader set of AI services available in Microsoft Foundry. You can integrate Document Intelligence with other services, such as **Azure AI Search** for knowledge mining scenarios or **generative AI models** for document summarization."

Learn-more links repeated: overview, model-overview, custom-model, Studio URL, language-support.

## Document Intelligence vs. Content Understanding vs. Azure AI Vision Read/OCR — critical exam distinction

This comparison is **not explicitly spelled out in this module's unit text** (it stays focused on Document Intelligence itself) — it is added here from established Microsoft Foundry positioning/general Azure knowledge to satisfy the exam's information-extraction skill area, which explicitly names Content Understanding. Flagged as supplementary context, not sourced from the fetched module pages.

| Aspect | **Azure AI Document Intelligence** | **Azure AI Content Understanding** | **Azure AI Vision Read/OCR** |
| --- | --- | --- | --- |
| Scope | Document/form-centric: purpose-built prebuilt models (invoice, receipt, ID document, tax forms, mortgage forms, etc.) + custom template/neural models for structured field, table, and key-value extraction | Newer, general **multimodal** analyzer framework: documents, images, audio, **and** video, with custom schemas ("field definitions") you define per analyzer | Pure OCR: printed/handwritten text extraction from images and documents — no field/table semantics |
| Output | Structured fields, tables, key-value pairs, selection marks, bounding regions/polygons, per-field confidence scores (`analyzeResult` JSON) | Structured JSON per your custom schema, or **markdown** output for downstream LLM/RAG reasoning; can emit field extraction plus content markdown in one analyzer | Lines/words with bounding boxes and language detection only |
| Modalities | Documents/images/PDF/TIFF/Office (read model only) | Documents, images, audio, video — one framework across content types | Images and documents (text only) |
| Customization | Custom template (fast, fixed layout) or custom neural (deep learning, varying layout) models trained on labeled samples; composed models; classifiers | Custom **analyzer schemas** defined per use case; supports single-task and **pro-mode** pipelines (per EXAM_SKILLS.md) for more complex, multi-field/multimodal extraction | None — fixed OCR behavior |
| Typical exam framing | "Extract fixed fields from a known document type (invoice/receipt/ID) or train a model for a company-specific static form" → Document Intelligence prebuilt or custom model | "Produce clean, grounded, markdown/structured output from mixed content types (docs+images+audio+video) for an agent/RAG pipeline" or "define a custom schema across content types" → Content Understanding | "Just get text out of an image with no structure" → Vision Read/OCR (or the Document Intelligence **read** model, which is functionally very close) |
| Positioning/migration guidance | Mature, document-specific service; still the right choice when you need the well-established prebuilt financial/tax/mortgage/ID model catalog or fine-grained custom template/neural training control | Positioned by Microsoft as the newer, broader multimodal evolution for building analyzers that produce grounded, structured/markdown outputs feeding directly into agents and RAG — the EXAM_SKILLS.md "Extract content from documents" bullet explicitly calls out Content Understanding (not Document Intelligence) for this | N/A — lowest-level primitive; both Document Intelligence's read model and Content Understanding can sit on top of OCR |

Key exam takeaway: if a question emphasizes **prebuilt financial/legal/tax/mortgage/ID document models**, **custom template vs. neural model training**, or **Document Intelligence Studio**, the answer is **Document Intelligence**. If a question emphasizes **multimodal (video/audio/image+text) analyzers**, **custom schemas**, **markdown output for RAG/agent grounding**, or **pro-mode**, the answer is **Content Understanding**.
