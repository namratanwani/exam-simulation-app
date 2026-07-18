# Create a multimodal analysis solution with Azure Content Understanding

Source: https://learn.microsoft.com/en-us/training/modules/analyze-content-ai/

(Note: the Learn catalog lists this module's title as "Create a multimodal analysis solution with Azure Content Understanding"; it is the module referenced by the task as "Analyze content with Azure AI Content Understanding" — same module, `analyze-content-ai`.)

## Learning objectives

After completing this module, you will be able to:

- Describe capabilities of Azure Content Understanding.
- Use Azure Content Understanding to build a content analyzer.
- Consume a Content Understanding analyzer by using the API.

Prerequisites: familiarity with Azure services/the Azure portal, and some familiarity with APIs.

## Exam relevance

This module maps directly to the following AI-103 skill bullets:

- **Implement computer vision solutions — Design and implement multimodal understanding workflows:**
  - "implement visual understanding by configuring Azure Content Understanding in Foundry Tools to extract visual characteristics"
  - "implement video analysis workflows to process and interpret video segments"
  - "configure single-task and pro-mode Content Understanding pipelines" (documented here as **Standard mode vs Pro mode**)
  - "implement solutions that identify objects, components, or regions within images or video"
- **Implement information extraction solutions — Build retrieval and grounding pipelines:**
  - "ingest and index content such as documents, images, audio, and video"
  - "implement enrichment using custom or built-in skills for text, images, and layout"
  - "configure RAG ingestion flow including documents and using OCR"
- **Implement information extraction solutions — Extract content from documents:**
  - "extract information using multimodal pipelines combining OCR, layout analysis, field extraction"
  - "produce clean, grounded representations for agents/RAG using Content Understanding"
  - "implement analyzers for generating structured or markdown outputs using Content Understanding"
- **Plan and manage an Azure AI solution — Choose the appropriate Foundry services:** "Choose the appropriate Foundry services for generative tasks, grounding, vector search, agent workflows, or multimodal processing" — Content Understanding is the canonical Foundry Tool for multimodal (document/image/audio/video) extraction.

**Important scope note:** The Microsoft Learn training module text itself (units 1–5, 7) is fairly high-level and does **not** use the terms "single-task"/"pro-mode" or spell out field-method types, video shot detection, etc. in detail. Because the exam skill outline explicitly calls out "single-task and pro-mode Content Understanding pipelines," this file supplements the module's own text with the primary Microsoft Learn product documentation that the module links to directly (Content Understanding overview, document/image/audio/video overview pages, the Standard/Pro modes concept page, and the analyzer reference) so the pro-mode distinction and field-schema mechanics are captured in full, exam-ready detail. Supplemented sections are clearly labeled "(supplementary — linked docs)".

---

## Unit 1: Introduction

Organizations rely on information locked inside content assets such as documents, images, videos, and audio recordings. Extracting this information is challenging and organizations often previously needed multiple technologies depending on content format.

**Azure Content Understanding** is a multimodal service that simplifies the creation of AI-powered **analyzers** that can extract information from content in practically any format (documents, images, audio, video).

The module explores the capabilities of Azure Content Understanding and how to use it to build custom analyzers.

---

## Unit 2: What is Azure Content Understanding?

Azure Content Understanding is a **generative AI service** used to extract insights and data from multiple kinds of content. It lets you quickly build applications that analyze complex data and generate outputs that can be used to automate and optimize processes.

Content Understanding is available through **Microsoft Foundry**. To use it you must provision a **Microsoft Foundry resource** in your Azure subscription. You can develop and manage a Content Understanding solution in three ways:

- In the **Microsoft Foundry portal**
- In **Content Understanding Studio**
- By using the **Content Understanding API**

### Multimodal content analysis

A single service, with a consistent development process, covers these content types:

- **Documents and forms** — analyze documents/forms and retrieve specific field values (e.g., extract key data from an invoice to automate payment processing).
- **Images** — infer information from visuals such as charts, identify physical defects in products, detect the presence of specific objects/people, or determine other visual information.
- **Audio** — automate tasks like summarizing conference calls, determining sentiment of recorded customer conversations, or extracting key data from telephone messages.
- **Video** — extract insights such as key points from video conference recordings, summarize presentations, or detect specific activity in security footage.

### (supplementary — linked docs) Content Understanding overview details

Azure Content Understanding in Foundry Tools is a **Foundry Tool** available as part of the **Microsoft Foundry Resource** in the Azure portal. It uses generative AI to process/ingest documents, images, videos, and audio into a **user-defined output format**.

**Why use Content Understanding — key benefits:**
- Simplify and streamline workflows — standardizes extraction/classification across content types into one process.
- Simplify field extraction — define a schema to extract, classify, or generate field values with no complex prompt engineering.
- Enhance accuracy — multiple AI models cross-validate information simultaneously.
- Confidence scores and grounding — minimizes cost of human review.
- Classify content types — unified classification in the Analyze API.
- Industry-specific prebuilt analyzers — tax prep, procurement, contract analysis, call center analytics, media analysis, etc.

**Use cases:** Intelligent document processing (IDP), agentic applications (clean markdown for reasoning workflows, or schema-aligned key-value fields with confidence/grounding), search/RAG ingestion, robotic process automation (RPA), analytics/reporting, classification-based workflow routing.

**Key components of the Content Understanding framework** (inputs → analyzer → structured output):

| Component | Description |
|---|---|
| **Inputs** | Documents, Images, Video, Audio |
| **Analyzer** | Core component defining how content is processed: content extraction settings, field extraction schema, model deployments. Prebuilt analyzers for common scenarios; supports custom analyzers. |
| **Content extraction** | Transforms unstructured input into normalized, structured text and metadata: OCR, selection marks, barcodes, formulas, layout (paragraphs, sections, tables). For audio/video: transcribes speech and identifies key visual elements. |
| **Segmentation** | Divides documents or videos into logical sections. Configured via `enableSegment` property in the analyzer schema. E.g., split a document by document type, or a video into scenes. |
| **Field extraction** | Generates structured key-value pairs from your defined schema. Three methods: **Extract** (documents only — pull values verbatim, e.g., dates from receipts), **Classify** (categorize content into predefined categories, e.g., call sentiment, chart type), **Generate** (freely generate values, e.g., summarize an audio conversation, generate scene descriptions). |
| **Confidence scores** | Reliability estimate **0 to 1** per extracted field value. Enabled via `estimateFieldSourceAndConfidence` setting in document analyzers. |
| **Grounding** | Identifies the specific regions in content where a value was extracted/generated — traces values back to source. Enabled via the same `estimateFieldSourceAndConfidence` setting. |
| **Contextualization** | Prepares context for generative models and post-processes output: normalization/formatting, source grounding calculation, confidence score computation, context engineering. |
| **Foundry models** | LLMs and embedding models that power generative capabilities — you bring your own model deployments. |
| **Structured output** | Final result as **Markdown** (search/retrieval scenarios) or structured **JSON** matching your schema (automation/analytics). |

**Content Understanding experiences:**
- **Content Understanding in Foundry (new) portal (coming soon)** — build advanced agentic workflows with the Content Understanding Tool.
- **Content Understanding Studio** — complementary UX, good migration path from Document Intelligence; supports analyzer performance improvement via data labeling and classification-based custom analyzers.

**Responsible AI / content filtering:** Content Understanding integrates **Azure AI Content Safety** results into its output. Each Foundry model deployment has an associated **Guardrails** instance evaluating prompts and completions. Flagged content appears as a `content_filters` array in the analyze response, with per-category severity (`hate`, `sexual`, `violence`, `self_harm` — each `safe`/`low`/`medium`/`high`). You can adjust Guardrails thresholds or switch **Block ↔ Annotate** per category on the model deployment.

**Face capabilities:** Content Understanding can generate detailed descriptions of faces in video/image content (facial hair, expression, identify prominent people/celebrities) when enabled — this is a **Limited Access** feature requiring registration; set `disableFaceBlurring: true` in the analyzer config to enable it.

---

## Unit 3: Create a Content Understanding analyzer

A Content Understanding solution is based on creating an **analyzer** — trained to extract specific information from a particular type of content based on a **schema** you define.

**High-level process:**
1. Create a Foundry resource.
2. Define a Content Understanding **schema** for the information to extract (can be based on a content sample and an **analyzer template**).
3. Build an **analyzer** based on the completed schema.
4. Use the analyzer to extract or generate fields from new content.

Numerous **analyzer templates** are provided to develop an analyzer quickly. Because of Content Understanding's generative AI capabilities, you can define a schema by example using minimal training data — the service often identifies the data values that map to schema elements automatically, though you can also explicitly **label fields** in content (e.g., documents) to improve analyzer performance.

### Creating an analyzer with Content Understanding Studio

While a complete solution can be built through the API/SDK, **Content Understanding Studio** provides a visual interface to create a project, define a schema, and build/test an analyzer.

> Tip: Only certain **prebuilt models** are available directly in the Microsoft Foundry portal. For **custom analyzer creation and testing**, use **Content Understanding Studio** (https://ai.azure.com/contentunderstanding).

**Creating a Content Understanding project:** In Content Understanding Studio, create a new project associated with a Microsoft Foundry resource. Creating a project provisions supporting Azure resources, including **storage** and a **key vault** resource to store sensitive details like credentials/keys.

> Note: Content Understanding schemas can only be created in Azure locations where the service is supported (see Content Understanding region and language support).

**Defining a schema:** After creating a project, define a schema for the content type and information to extract. The schema editor lets you upload a file (document, image, audio, or video) on which the schema is based, apply an appropriate **schema template**, and define the specific fields the analyzer should identify.

> Note: The templates and field types available in a schema **depend on the content type** of the file the schema is based on. Some content types support additional optional functionality (e.g., extracting barcodes and formulae from text in documents). Content-type-specific docs referenced: Content Understanding document solutions, image solutions, audio solutions, video solutions.

**Testing:** Test the analyzer schema at any time by running analysis on the sample file (or other uploaded files). Test results include extracted field values and the **JSON format output** returned to client applications.

**Building an analyzer:** Once satisfied with schema performance, **build** the analyzer — this makes it accessible to client applications through the endpoint of the Microsoft Foundry resource associated with the project. After building, you can continue testing and refine the schema to create **new named versions** with different capabilities.

### (supplementary — linked docs) Analyzer concepts, types, and full configuration reference

An **analyzer** is a configurable processing unit defining:
- What type of content to process (documents, images, audio, or video)
- What elements to extract (text, layout, tables, fields, transcripts)
- How to structure output (markdown, JSON fields, segments)
- Which AI models to use for processing

**Analyzer types:**
- **Base analyzers** — foundational, core processing capability per content type: `prebuilt-document`, `prebuilt-audio`, `prebuilt-video`, `prebuilt-image`. Used as building blocks for custom analyzers.
- **RAG analyzers** — optimized for retrieval-augmented generation, e.g. `prebuilt-documentSearch`, `prebuilt-videoSearch`.
- **Domain-specific analyzers** — preconfigured for specific document types/industries, e.g. `prebuilt-invoice`, `prebuilt-receipt`, `prebuilt-idDocument`, `prebuilt-contract`, `prebuilt-callCenter`, `prebuilt-audioSearch`.
- **Custom analyzers** — extend base analyzers with custom field schemas/configurations.

**Analyzer configuration JSON — top-level properties:**

```json
{
  "analyzerId": "myCustomInvoiceAnalyzer",
  "description": "Extracts vendor information, line items, and totals from commercial invoices",
  "baseAnalyzerId": "prebuilt-document",
  "config": {
    "enableOcr": true
  },
  "fieldSchema": {
    "fields": {
      "vendorName": { "type": "string" }
    }
  },
  "models": {
    "completion": "gpt-5.2",
    "embedding": "text-embedding-3-large"
  }
}
```

Key top-level properties:
- **`analyzerId`** — unique identifier used to reference the analyzer in API calls (letters, numbers, dots, underscores).
- **`name`** — human-readable display name.
- **`description`** — used by the AI model as context during field extraction; clearer descriptions improve accuracy.
- **`baseAnalyzerId`** — parent analyzer to inherit config from: `prebuilt-document`, `prebuilt-audio`, `prebuilt-video`, `prebuilt-image`.
- **`models`** — `completion` (model name for field extraction/segmentation/figure analysis) and `embedding` (for knowledge base use). These are **model names from the Foundry catalog, not deployment names** — the service maps them to actual deployments at runtime.

**`config` object — processing options (selected, with defaults):**

| Property | Default | Applies to | Description |
|---|---|---|---|
| `returnDetails` | `false` (varies) | all | Include confidence scores, bounding boxes, text spans, metadata |
| `enableOcr` | `true` | Document | OCR for scanned/image-based text |
| `enableLayout` | `true` | Document | Paragraphs, lines, words, reading order |
| `enableFormula` | `true` | Document | LaTeX-format math formulas |
| `enableBarcode` | `true` | Document | Barcode/QR detection (QR, PDF417, UPC-A/E, Code 39/128/93, EAN-8/13, DataBar, Codabar, ITF, Micro QR, Aztec, Data Matrix, MaxiCode) |
| `tableFormat` | `"html"` | Document | `"html"` or `"markdown"` |
| `chartFormat` | `"chartjs"` | Document | Chart.js-compatible structured chart data |
| `enableFigureDescription` | `false` | Document | Natural-language descriptions of figures/diagrams (alt text) |
| `enableFigureAnalysis` | `false` | Document | Deeper figure analysis (chart data extraction, diagram components) |
| `annotationFormat` | `"markdown"` | Document | Format for returned annotations |
| `estimateFieldSourceAndConfidence` | `false` (varies) | Document (invoice, receipt, ID, tax) | Source location + confidence score per extracted field |
| `locales` | `[]` | `prebuilt-audio`, `prebuilt-video`, `prebuilt-callCenter` | BCP-47 language codes, e.g. `["en-US","es-ES"]` |
| `disableFaceBlurring` | `false` | `prebuilt-image`, `prebuilt-video` | `true` = faces not blurred (Limited Access) |
| `contentCategories` | not set | Document, video (video: one category only) | Categories for classification/segmentation routing; each has `description` (required, acts as a prompt) and optional `analyzerId` |
| `enableSegment` | `false` | Document, video | Enables segmentation using `contentCategories` |
| `segmentPerPage` | `false` | Document | One segment per page |
| `omitContent` | `false` | Document | Excludes original content object from response, returning only structured/subanalyzer results |

**Field schema (`fieldSchema`) structure and field `method` types:**

```json
{
  "fieldSchema": {
    "name": "InvoiceAnalysis",
    "fields": {
      "VendorName": { "type": "string", "description": "Name of the vendor or supplier", "method": "extract" },
      "InvoiceTotal": { "type": "number", "description": "Total amount due on the invoice", "method": "extract" },
      "LineItems": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "Description": { "type": "string" },
            "Quantity": { "type": "number" },
            "UnitPrice": { "type": "number" },
            "Amount": { "type": "number" }
          }
        },
        "description": "List of items on the invoice, typically in a table format",
        "method": "generative"
      }
    }
  }
}
```

Field `type` values: `"string"`, `"number"`, `"boolean"`, `"date"`, `"object"`, `"array"`.

Field `method` values (the exam-relevant "generate/classify/extract" distinction):
- **`"extract"`** — pull values verbatim as they appear in the content (literal text extraction from a specific location). Requires `estimateSourceAndConfidence: true` for that field.
- **`"classify"`** — classify content against a predefined set of categories (use with `enum`).
- **`"generate"`** — freely generate/infer values using the AI model (best for complex/variable fields requiring interpretation, e.g., summaries).

If `method` isn't specified, the system infers the best method from field type/description. `estimateSourceAndConfidence` (field-level) overrides the analyzer-level `estimateFieldSourceAndConfidence`.

**Configuration support by content type (quick reference):**
- **Document** (`prebuilt-document`): `returnDetails`, `omitContent`, `enableOcr`, `enableLayout`, `enableFormula`, `enableBarcode`, `tableFormat`, `chartFormat`, `enableFigureDescription`, `enableFigureAnalysis`, `enableAnnotations`, `annotationFormat`, `enableSegment`, `segmentPerPage`, `estimateFieldSourceAndConfidence`, `contentCategories`.
- **Audio** (`prebuilt-audio`): `returnDetails`, `locales`.
- **Video** (`prebuilt-video`): `returnDetails`, `locales`, `contentCategories`, `enableSegment`, `omitContent`, `disableFaceBlurring`.
- **Image** (`prebuilt-image`): `returnDetails`, `disableFaceBlurring`.

**Creating a custom analyzer via REST:**

```bash
curl -X PUT "https://{endpoint}/contentunderstanding/analyzers/{analyzerId}?api-version=2025-11-01" \
  -H "Content-Type: application/json" \
  -H "Ocp-Apim-Subscription-Key: {key}" \
  -d @analyzer-definition.json
```

Response: `201 Created` with an `Operation-Location` header to track analyzer-creation status.

---

## Unit 4: Use the Content Understanding API

The Content Understanding API is a programmatic interface used to **create, manage, and consume** analyzers.

To use it, a client application submits **HTTP calls** to the **Content Understanding endpoint** for your Microsoft Foundry resource, passing an **authorization key** in the header. You obtain the endpoint and keys in the Azure portal or Microsoft Foundry portal. You can also use the **Microsoft Foundry API** to connect to the project programmatically with your **Entra ID**.

### Using the API to analyze content

A common pattern: submit content to an existing analyzer, then retrieve analysis results. The analysis request returns an **operation ID** representing an **asynchronous task**. The client must then poll with a second request using that operation ID until the operation completes and results are returned as **JSON**.

**Example — analyze a document (POST):**

```json
POST {endpoint}/contentunderstanding/analyzers/{analyzer}:analyze?api-version=2025-11-01
{
  "inputs": [
    {
      "url": "https://host.com/doc.pdf"
    }
  ]
}
```

> Note: You can specify a URL for the content file location as shown. To submit **binary file data directly**, use the **`analyzeBinary`** operation instead.

**Example response (async operation started):**

```http
Operation-Id: 1234abcd-1234-abcd-1234-abcd1234abcd
Operation-Location: {endpoint}/contentunderstanding/analyzerResults/1234abcd-1234-abcd-1234-abcd1234abcd?api-version=2025-11-01
{
  "id": "1234abcd-1234-abcd-1234-abcd1234abcd",
  "status": "NotStarted"
}
```

**Polling for status/result (GET):**

```http
GET {endpoint}/contentunderstanding/analyzerResults/1234abcd-1234-abcd-1234-abcd1234abcd?api-version=2025-11-01
```

When the operation succeeds, the response contains a JSON payload with the analysis results; the specific shape depends on the content and schema used.

> For more information about the Content Understanding API, see the reference documentation (`/rest/api/contentunderstanding/operation-groups`).

---

## Unit 5: Exercise — Extract information from multimodal content

Hands-on lab (40 minutes): use Azure Content Understanding to extract information from **documents, images, audio files, and videos**. Requires an Azure subscription with administrative access. The exercise is launched via an external fwlink to a Microsoft Learn sandbox lab — content not further detailed on the unit page itself (interactive lab, not additional reference text).

---

## Unit 7: Summary

Azure Content Understanding is a multimodal AI service that lets you extract information from many kinds of content. In this module you learned how to use **Content Understanding Studio** to create a Content Understanding project and build an **analyzer**.

(Unit 6, "Module assessment," is an interactive knowledge-check quiz page with no additional reference content to extract.)

---

## Supplementary deep-dive: Standard mode vs Pro mode (the "single-task vs pro-mode" pipeline distinction)

*(supplementary — linked docs: this is the material behind the exam skill "configure single-task and pro-mode Content Understanding pipelines." Source: Azure Content Understanding in Foundry Tools standard and pro modes (preview) concept doc.)*

> As of the `2025-05-01-preview` API version, Content Understanding offers two modes: **`standard`** and **`pro`**. (Preview API versions `2024-12-01-preview` and `2025-05-01-preview` are being retired by July 15, 2026 in favor of the GA `2025-11-01` API version.)

### Standard mode

- The **default** mode for processing diverse content types.
- Optimized for **efficient, single-shot schema extraction** tailored to a specific task, across all data formats (documents, images, video, audio, text).
- Emphasizes **cost-effectiveness and reduced latency**.
- Does **not** support data inferencing/multi-step reasoning.
- Supports schema creation/customization and **data labeling for document data** to improve output quality.
- Use cases: powering RAG search workflows (integrating with Azure AI Search), extracting data for Microsoft Fabric, screening advertising videos for content guidelines, segmenting video into chapters/ad breaks, extracting sports-game data points for recaps.

### Pro mode

- Designed for **advanced use cases requiring multi-step reasoning and complex decision-making** — e.g., identifying inconsistencies, drawing inferences, making decisions.
- Supports **multiple input documents** and lets you provide **reference data** at analyzer-creation time (adds context for validation/enrichment).
- **Currently available only for document data** (not images/audio/video).
- **Multi-step reasoning** decomposes complex problems into simpler tasks — goes beyond extracting/aggregating structured data to letting you draw conclusions, reducing the need for human review. Example questions pro mode can answer:
  - Does x match y?
  - Does x pass the outlined criteria?
  - Does x document follow the required guidelines?
  - Does the total equal the sum of the items?
  - Find all inconsistencies between the invoice and the contract.
- **Reference data**: at analyzer creation you can supply reference documents (e.g., a contract) that give context when analyzing input documents (e.g., an invoice + purchase order) — the service reasons over inputs against the reference data to flag discrepancies. The system operates in "**lookup mode**" when referencing documents — for exhaustive recovery of data, put the content into the input set instead of reference data.

### Standard vs Pro — feature comparison table

| Feature | Standard mode | Pro mode |
|---|---|---|
| Large documents | Yes | Yes |
| Field mode | Yes | Yes |
| Extract, classify, and generate fields | Yes | Supports `classify` and `generate` only — **no `extract`** |
| Grounding and confidence scores | Yes | **No** |
| Input document type | Documents, images, video, audio | **Documents only** |
| Max fields | 100 | 100 |
| Multiple input document processing | No | Yes |
| Reference dataset integration | No | Yes |
| Multi-step reasoning | No | Yes |

### Applying Standard vs Pro — worked scenarios

| Scenario | Standard mode | Pro mode |
|---|---|---|
| Invoice analysis | Extract PO number, total, due date, line items at scale for RAG/DB entry | "Does this invoice fulfill the contractual agreement with this client? Does it need further review?" |
| Call center transcript analytics | Extract sentiment, main issues, average call length across volumes | "Did the employee introduce themselves? Did the answer *pass* certain criteria?" |
| Mortgage application processing | Extract year submitted, names on application | "Do the names and SSNs on the application match the supporting documentation?" |

### Pro mode known limitations and best practices

- No confidence scores or grounding.
- Supports `classify`/`generate` fields only, not `extract`.
- Only documents are supported today.
- Operates in lookup mode for reference documents — put content in the input set if you need exhaustive recovery.
- Design schemas with the highest specificity (distinct fields per inconsistency type rather than one generic list; reference specific sections to review).
- Keep reference documents concise/focused to improve retention and recall.

You can try both modes in the **Microsoft Foundry** portal (no-code) to compare fit for your scenario.

---

## Supplementary deep-dive: Video analysis — segmentation, shot detection, transcription

*(supplementary — linked docs, source: Content Understanding video overview)*

The **prebuilt video analyzer** `prebuilt-videoAnalysis` / RAG-oriented `prebuilt-videoSearch` outputs RAG-ready content:
- **Markdown** output includes: inline **Transcript** in standard **WEBVTT** format, and ordered **Key Frame** thumbnails.
- **JSON** output additionally contains: **Description** (natural-language segment descriptions with visual + speech context) and **Segmentation** (automatic scene segmentation into logical chunks based on categories you define).

This output can drop straight into a vector store for an agent/RAG workflow with no post-processing required. From there, you can customize the analyzer: define custom fields, generate custom segments (e.g., split a news broadcast into chapters by topic), and identify prominent people via **face description** (e.g., label `Satya Nadella` using the model's world knowledge).

**Two-stage processing pipeline:**
1. **Content extraction** — foundational metadata: transcripts and shots.
   - **Transcription**: converts speech to WebVTT transcripts. Sentence-level timestamps available when `"returnDetails": true`. Supports the full set of Azure Speech in Foundry Tools speech-to-text languages.
   - **Diarization**: distinguishes speakers, attributing transcript parts to specific speakers.
   - **Multilingual transcription**: per-phrase language/locale detection; enabled when no locale specified or `locale = auto`. Unsupported locales fall back to the closest supported locale (possibly incorrect) — configure locales explicitly to avoid quality issues.
   - **Key frame extraction**: extracts key frames representing each shot, to give field extraction enough visual detail.
   - **Shot detection**: identifies segments aligned with shot boundaries; output is a list of millisecond timestamps in **`cameraShotTimesMs`**, only returned when `"returnDetails": true`.
2. **Field extraction and segmentation** — a generative model tags scenes, summarizes actions, and slices footage into segments per your schema (`fieldSchema`).

**Custom fields example:**

```json
"fieldSchema": {
  "description": "Extract brand presence and sentiment per scene",
  "fields": {
    "brandLogo": {
      "type": "string",
      "method": "generate",
      "description": "Brand being promoted in the video. Include the product name if available."
    },
    "Sentiment": {
      "type": "string",
      "method": "classify",
      "description": "Ad categories",
      "enum": ["Consumer Packaged Goods", "Groceries", "Technology"]
    }
  }
}
```

**Face description fields** (Limited Access, requires enabling `disableFaceBlurring: true`): example fields include `facialHairDescription` (`beard`, `mustache`, `clean-shaven`), `nameOfProminentPerson` (e.g., `Satya Nadella`), `faceSmilingFrowning`.

**Segmentation modes** — controlled by `enableSegment`:
- **Whole-video** (`enableSegment: false`) — the entire file is treated as one segment; metadata extracted across the full duration. Use for: compliance checks anywhere in an ad, full-length descriptive summaries.
- **Custom segmentation** (`enableSegment: true`) — you describe segmentation logic in natural language via `contentCategories`; the model creates variable-length segments (seconds to minutes). **Video only supports one `contentCategories` object.**

```json
{
  "config": {
    "enableSegment": true,
    "contentCategories": {
      "news-story": {
        "description": "Segment the video based on each distinct news segment. Use the timestamp of each image to identify the start and end time of each segment, no overlap segments. Ignore non-news segments like ads or promotion.",
        "analyzerId": "NewsAnalyzer"
      }
    }
  }
}
```

> Note: Setting segmentation invokes the generative model and consumes tokens even if no fields are defined.

**Key benefits vs other video analysis solutions:** segment-based **multi-frame** analysis (not single-frame), customizable fields/segmentation, natural-language-driven extraction, optimized preprocessing (transcription + scene detection) feeding rich context to the generative model.

**Technical constraints/limits:**
- **Frame sampling ~1 FPS** — rapid motion or single-frame events may be missed.
- **Frame resolution 512×512 px** — small text/distant objects can be lost.
- **Speech only** — music, sound effects, ambient noise are ignored (not transcribed).

**Video capabilities are currently limited to:** Content extraction, Field extraction. (Face identification/grouping is preview-only, not in GA.)

---

## Supplementary deep-dive: Audio analysis — transcription, diarization, prebuilt analyzers

*(supplementary — linked docs, source: Content Understanding audio overview)*

Audio analyzers enable **transcription and diarization** for conversational audio and extract structured fields (summaries, sentiment, key topics). Common scenarios: customer insight/summarization/sentiment, call-center quality/compliance, podcast summaries/metadata.

**Content extraction (audio):**
- **Transcription** → searchable WebVTT transcripts; word/sentence-level timestamps on request.
- **Diarization** → attributes transcript segments to speakers.
- **Speaker role detection** → maps speakers to roles (agent/customer) for contact-center data.
- **Multilingual transcription** → per-phrase language/locale; enabled when `locales` unset or `auto`.
- **Language detection** → auto-detects dominant language/locale when multiple locales specified.

**`locales` configuration — file-size/latency matrix:**

| Locale setting | File size | Processing | Result latency |
|---|---|---|---|
| `auto`/empty | ≤300 MB and/or ≤2 hours | Multilingual transcription | Near-real-time |
| `auto`/empty | >300 MB and >2h, ≤4h | Multilingual transcription | Regular |
| single locale | ≤1 GB and/or ≤4 hours | Single-language transcription | Near-real-time or Regular depending on size |
| multiple locales | ≤1 GB and/or ≤4 hours | Single-language (via language detection) | Near-real-time or Regular depending on size |

**Field extraction (audio):** extract structured data — summaries, sentiments, mentioned entities from call logs — via a prebuilt template or a custom schema.

**Prebuilt audio analyzers:**
- **`prebuilt-callCenter`** (Post-call analysis) — generates: transcript with speaker-role detection, call **Summary**, call **Sentiment**, top 5 mentioned **Topics/articles**, mentioned **Companies**, mentioned **People** (name + role), relevant call **Categories**.
- **`prebuilt-audioSearch`** (Conversation analysis, RAG-oriented) — generates: conversation transcript, conversation **Summary**.

Both output WEBVTT transcripts separated by speaker; prebuilt analyzers default to multilingual transcription with `returnDetails` enabled.

Example `prebuilt-callCenter` JSON response shape (abridged):

```json
{
  "id": "bc36da27-004f-475e-b808-8b8aead3b566",
  "status": "Succeeded",
  "result": {
    "analyzerId": "prebuilt-callCenter",
    "apiVersion": "2025-11-01",
    "contents": [
      {
        "markdown": "# Audio: 00:00.000 => 00:32.183\n\nTranscript\n```\nWEBVTT\n...\n```",
        "fields": {
          "Summary": { "type": "string", "valueString": "..." },
          "Topics": { "type": "array", "valueArray": [ /* ... */ ] },
          "Companies": { "type": "array", "valueArray": [ /* ... */ ] },
          "People": { "type": "array", "valueArray": [ /* {Name, Role} objects */ ] },
          "Sentiment": { "type": "string", "valueString": "Positive" },
          "Categories": { "type": "array", "valueArray": [ /* ... */ ] }
        },
        "kind": "audioVisual",
        "startTimeMs": 0,
        "endTimeMs": 32183,
        "transcriptPhrases": [
          { "speaker": "Agent", "startTimeMs": 80, "endTimeMs": 640, "text": "Good day.", "words": [] }
        ]
      }
    ]
  }
}
```

Related solution accelerator: **Conversational Knowledge Mining** — combines Microsoft Foundry, Azure Content Understanding, Azure OpenAI in Microsoft Foundry Models, and **Azure AI Search** to map unstructured dialogue to structured insights (topic modeling, key-phrase extraction, speech-to-text, interactive chat).

---

## Supplementary deep-dive: Image analysis — field extraction, use cases

*(supplementary — linked docs, source: Content Understanding image overview)*

Content Understanding standardizes extraction of data from **images**. You define schemas specifying fields, descriptions, and output types; the service returns structured data. Use cases:
- **RAG applications** — extract image details to power a chat index.
- **Financial analysis/BI** — analyze charts/trend images for reporting.
- **Manufacturing quality control** — automate defect/anomaly detection (scratches, cracks, misalignments).
- **Shelf analysis/inventory management** — detect/count/describe retail products.

**Face description fields** (Limited Access; `disableFaceBlurring: true`): `facialHairDescription`, `nameOfProminentPerson`, `faceSmilingFrowning` — same mechanism as video.

> Note: Image analyzers are **not optimized** for scenarios primarily about extracting/analyzing text from images — if the main goal is text extraction from an image, use a **document field extraction schema** instead.

---

## Supplementary deep-dive: Content Understanding vs Document Intelligence vs Azure AI Search skillsets (commonly confused on the exam)

*(supplementary — linked docs, source: "Choose the right Azure AI tool for document processing")*

Azure Content Understanding **brings together** Azure Document Intelligence's high-accuracy deterministic extraction with LLM-powered capabilities for complex/unstructured/multimodal content. Both are **Foundry Tools**.

- **Azure Content Understanding** — powered by generative AI/LLMs; strong for unstructured documents, varying layouts, multimodal content, inferred fields, complex reasoning; **no labeled training data required to start** (zero-shot schema-based extraction).
- **Azure Document Intelligence** — specialized AI models purpose-trained for document parsing/extraction; ideal for **structured documents with common templates** where consistency, low latency, and proven accuracy matter most; supports **custom models with as few as 5 labeled samples**; only option for **on-premises/air-gapped deployment** (via **DI containers**).
- **Azure-hosted LLMs (Foundry models directly)** — for teams needing full control over models/prompts/infrastructure; requires manual preprocessing, prompt tuning, orchestration, and building your own confidence scoring (no built-in confidence/grounding).

> Important: If you're already running Document Intelligence in production, your APIs/endpoints/SDKs/billing are unchanged — no migration required. This guidance is for new workloads/expansion.

### Quick-reference decision guide (ACU `2025-11-01` GA vs ADI `4.0` GA)

| Scenario | Recommended tool | Why |
|---|---|---|
| OCR or layout extraction only | CU `prebuilt-read` or `prebuilt-layout` | Lower cost, richer layout extraction |
| Multimodal analysis or RAG-ready preprocessing | CU prebuilt or custom analyzers | Search ingestion, grounded summaries, multimodal (image/audio/video) |
| Standard structured forms (invoice, receipt, ID, tax, mortgage) | **DI prebuilt model** | High accuracy on common structured templates |
| Mostly unstructured docs (contracts, legal agreements) | **CU `prebuilt-contract`** | Better suited to semi-structured/unstructured docs needing reasoning/inferred fields |
| Custom extraction without labels / unstructured docs (policies, referral letters) | **CU custom analyzer** (zero-shot or with knowledge source) | Describe fields in plain language, iterate fast |
| Custom extraction with labels for highly structured docs (claims, standard applications) | **DI custom model** | Neural model training with as few as 5 labeled samples |
| On-premises / air-gapped deployment | **DI containers** | Only option today |

### Content Understanding/Document Intelligence vs "build your own with Azure OpenAI"

| Feature | CU or DI (managed) | Build your own (Azure OpenAI/Foundry models) |
|---|---|---|
| Input types | Documents, images, audio, video | Any, but requires preprocessing |
| OCR | Industry-leading, built-in | Requires preprocessing |
| Field extraction | Wide range of specialized (DI) and LLM-based (CU) prebuilt & custom models | Requires full customization via prompt engineering |
| Reasoning & validation | Built-in | Requires manual chaining/logic |
| Confidence & grounding | Yes | No — requires custom implementation |
| Ease of use | Zero-shot schema-based extraction, no labeling needed | Requires prompt tuning, orchestration, engineering |
| Scalability | Fully managed | Manual scaling required |

**Azure AI Search skillsets note:** the module content itself does not directly cover Azure AI Search enrichment skillsets, but the doc set positions Content Understanding as the modern, unified alternative/complement for **ingesting multimodal content (documents, images, audio, video) into a search index** for RAG — where classic AI Search "cognitive skills" pipelines historically chained separate Cognitive Services (OCR skill, image analysis skill, key phrase extraction skill, etc.) for enrichment, Content Understanding centralizes this into a single **analyzer** that outputs ready-to-index Markdown/JSON directly. Do not confuse: **AI Search enrichment skillsets** operate as part of an **indexer pipeline** producing an index; **Content Understanding analyzers** are a standalone Foundry Tool that produces structured/markdown output which can then be *fed into* a search index — Content Understanding is a content-processing/extraction service, not a search/indexing service itself.

---

## Consolidated glossary of exact service/API/parameter names (for quick recall)

- **Service names:** Azure Content Understanding (in Foundry Tools), Microsoft Foundry, Content Understanding Studio (`https://ai.azure.com/contentunderstanding`), Azure AI Content Safety / Guardrails, Azure Document Intelligence, Azure AI Search, Azure Speech (Foundry Tools).
- **Core concept:** **analyzer** — configurable processing unit; created from a **schema**.
- **Analyzer base IDs:** `prebuilt-document`, `prebuilt-audio`, `prebuilt-video`, `prebuilt-image`.
- **RAG analyzers:** `prebuilt-documentSearch`, `prebuilt-videoSearch`/`prebuilt-videoAnalysis`, `prebuilt-audioSearch`.
- **Domain analyzers:** `prebuilt-invoice`, `prebuilt-receipt`, `prebuilt-idDocument`, `prebuilt-contract`, `prebuilt-callCenter`, `prebuilt-read`, `prebuilt-layout`.
- **Modes:** `standard` (default, single-task schema extraction) vs `pro` (multi-step reasoning, reference data, multi-document, documents only, no confidence/grounding, no `extract` method).
- **Field methods:** `extract`, `classify`, `generate`/`generative`.
- **Field types:** `string`, `number`, `boolean`, `date`, `object`, `array`.
- **Key config parameters:** `enableOcr`, `enableLayout`, `enableFormula`, `enableBarcode`, `tableFormat`, `chartFormat`, `enableFigureDescription`, `enableFigureAnalysis`, `annotationFormat`, `estimateFieldSourceAndConfidence` (analyzer-level) / `estimateSourceAndConfidence` (field-level), `locales`, `disableFaceBlurring`, `contentCategories`, `enableSegment`, `segmentPerPage`, `omitContent`, `returnDetails`.
- **REST operations:** `PUT .../analyzers/{analyzerId}?api-version=2025-11-01` (create analyzer) → `201 Created` + `Operation-Location`; `POST .../analyzers/{analyzer}:analyze?api-version=2025-11-01` (analyze by URL) or `analyzeBinary` (analyze raw bytes) → returns `Operation-Id`/`Operation-Location` + `status: NotStarted`; `GET .../analyzerResults/{operationId}?api-version=2025-11-01` (poll for result).
- **Current GA API version:** `2025-11-01`. Retiring preview versions: `2024-12-01-preview`, `2025-05-01-preview` (retirement by **July 15, 2026**).
- **Output formats:** Markdown, structured JSON.
- **Confidence score range:** 0 to 1.
- **Video technical limits:** ~1 FPS frame sampling, 512×512 px frame resolution, speech-only transcription (no music/SFX).
- **Video shot-detection output field:** `cameraShotTimesMs` (requires `returnDetails: true`).
- **Audio prebuilt analyzers:** `prebuilt-callCenter`, `prebuilt-audioSearch`.
- **Transcript format:** WEBVTT.
