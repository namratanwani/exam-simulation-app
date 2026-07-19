# Practice questions — Create a multimodal analysis solution with Azure Content Understanding

Grounded in `content.md` for this module. Questions flagged "(general Azure knowledge)" draw on well-established platform knowledge beyond the fetched unit text.

## Learning objectives / Exam relevance

**Q44.** Which of the following is one of the three stated learning objectives for this module?
A. Consume a Content Understanding analyzer by using the API
B. Train a custom neural network for document classification
C. Configure an Azure AI Search enrichment skillset
D. Deploy a Sora 2 video generation model in Microsoft Foundry
**Answer:** A — The three objectives are: describe capabilities of Azure Content Understanding, use Azure Content Understanding to build a content analyzer, and consume a Content Understanding analyzer by using the API.

**Q45.** Under the exam skill "configure single-task and pro-mode Content Understanding pipelines," how does this module's own unit text (units 1-5, 7) compare to the supplementary linked-docs material on this topic?
A. The module's own unit text fully spells out Standard vs Pro mode in detail, including a field-method compatibility table for each mode
B. The module's own unit text is high-level and does not use the terms "single-task"/"pro-mode" or detail field-method types; that depth comes from supplementary linked product documentation
C. The module's own unit text covers Pro mode but not Standard mode, despite Standard being the documented default and lower-cost option
D. Neither the unit text nor any linked docs cover this exam skill, leaving it entirely untested on the AI-103 exam despite appearing in the skills outline
**Answer:** B — The module explicitly notes this scope gap and supplements the training text with the primary product documentation to cover the pro-mode distinction in exam-ready detail.

## Unit 1: Introduction

**Q1.** Which Azure service is described as a multimodal service that simplifies the creation of AI-powered analyzers to extract information from content in practically any format (documents, images, audio, video)?
A. Azure AI Document Intelligence
B. Azure Content Understanding
C. Azure AI Vision Image Analysis
D. Azure AI Search cognitive skills
**Answer:** B — Azure Content Understanding is the multimodal service purpose-built for creating analyzers across documents, images, audio, and video.

**Q2.** Before Content Understanding existed, why did organizations often need multiple separate technologies to extract information from content?
A. Because Azure did not support any document processing services prior to 2023, per the module's historical framing
B. Because different content formats (documents, images, video, audio) traditionally required different, format-specific technologies
C. Because Azure Content Understanding requires a separate resource per format, unlike its unified analyzer model today
D. Because only text files could be analyzed by Azure AI services, with images and audio needing third-party tools
**Answer:** B — the module states organizations needed to build solutions based on multiple technologies depending on content format before a unified multimodal service existed.

**Q3.** What is the core reusable building block that Content Understanding uses to extract information from a given type of content?
A. A skillset
B. An analyzer
C. A cognitive index
D. A pipeline template
**Answer:** B — Content Understanding solutions are built around creating an analyzer trained against a schema.

## Unit 2: What is Azure Content Understanding?

**Q4.** Which Azure resource must you provision before you can use Azure Content Understanding?
A. Azure Cognitive Search resource
B. Microsoft Foundry resource
C. Azure Databricks workspace
D. Azure Kubernetes Service cluster
**Answer:** B — Content Understanding is available through Microsoft Foundry; you provision a Microsoft Foundry resource in your Azure subscription to use it.

**Q5.** Which THREE of the following are valid ways to develop and manage a Content Understanding solution? (Choose three.)
A. The Microsoft Foundry portal
B. Content Understanding Studio
C. The Content Understanding API
D. Azure DevOps Boards
E. Azure Monitor Workbooks
**Answer:** A, B, C — the module explicitly lists these three development/management surfaces for Content Understanding.

**Q6.** Which field-extraction method should you choose to summarize an audio conversation or generate a scene description for a video, where the value does not appear verbatim in the source content?
A. Extract
B. Classify
C. Generate
D. Segment
**Answer:** C — Generate produces values freely from input data via the AI model (e.g., summaries, scene descriptions), as opposed to Extract (literal values) or Classify (predefined categories).

**Q7.** In the Content Understanding framework, which component is responsible for identifying the specific regions in the source content where an extracted or generated field value came from, enabling users to trace values back to their origin?
A. Contextualization
B. Grounding
C. Segmentation
D. Content extraction
**Answer:** B — Grounding identifies the source regions for extracted/generated values, enabled via the `estimateFieldSourceAndConfidence` setting.

**Q8.** What numeric range do Content Understanding confidence scores fall within?
A. 0 to 100
B. -1 to 1
C. 0 to 1
D. 1 to 10
**Answer:** C — Confidence scores are reliability estimates from 0 to 1 for each extracted field value.

**Q9.** Which analyzer schema property, when configured, divides documents or videos into logical sections for targeted processing (such as splitting a document by document type or a video into scenes)?
A. `contentCategories`
B. `enableSegment`
C. `omitContent`
D. `estimateFieldSourceAndConfidence`
**Answer:** B — Segmentation is configured using the `enableSegment` property in the analyzer schema (in conjunction with `contentCategories` to define the category logic).

**Q10.** Which two structured output formats can a Content Understanding analyzer return to client applications? (Choose two.)
A. Markdown
B. XML
C. Structured JSON matching the defined schema
D. YAML
E. Protobuf
**Answer:** A, C — the final result is supplied as Markdown (for search/retrieval scenarios) or structured JSON matching the defined schema (for automation/analytics workflows).

**Q46.** Which Content Understanding experience is described as "coming soon" and intended for building advanced agentic workflows with the Content Understanding Tool, distinct from Content Understanding Studio?
A. Content Understanding in Foundry (new) portal
B. Azure AI Search Studio's query playground
C. Power Automate Content Understanding connector
D. Azure Machine Learning Designer's pipeline canvas
**Answer:** A — "Content Understanding in Foundry (new) portal (coming soon) — build advanced agentic workflows with the Content Understanding Tool," positioned alongside Content Understanding Studio (a complementary UX and good migration path from Document Intelligence).

**Q47.** How does Content Understanding surface responsible-AI content filtering results in its analyze response, and which service powers this filtering?
A. As a `content_filters` array with per-category severity levels, powered by Azure AI Content Safety / Guardrails
B. As an HTTP 451 error with no further detail, terminating the analyze request entirely
C. As a separate manual review queue in Content Understanding Studio only, disconnected from the API response
D. Content Understanding performs no content filtering of any kind, deferring entirely to the calling application
**Answer:** A — Each Foundry model deployment has an associated Guardrails instance; flagged content appears as a `content_filters` array in the analyze response, with per-category severity for categories like `hate`, `sexual`, `violence`, and `self_harm`.

**Q48.** Which four severity levels can each Guardrails content-filter category (`hate`, `sexual`, `violence`, `self_harm`) report, and what per-category action can you configure on the model deployment?
A. Severity: `safe`/`low`/`medium`/`high`; action: switch between Block and Annotate per category
B. Severity: `pass`/`fail`; action: quarantine the entire request, with no per-category granularity
C. Severity: numeric 1-10 score only; no configurable action, since thresholds are fixed platform-wide
D. Severity levels are not reported, only a boolean flag indicating whether any category triggered
**Answer:** A — Each category reports `safe`/`low`/`medium`/`high` severity, and you can adjust Guardrails thresholds or switch Block ↔ Annotate per category on the model deployment.

**Q49.** What must you do to enable Content Understanding's face description capabilities (detailed descriptions of facial hair, expression, or identifying prominent people), beyond setting `disableFaceBlurring: true`?
A. Nothing else — the config flag alone enables full production access
B. Register for the feature, since it is a Limited Access capability
C. Purchase a separate Face API license through Azure Marketplace
D. Face description cannot be enabled under any circumstances
**Answer:** B — Face description is called out as a Limited Access feature requiring registration, in addition to setting `disableFaceBlurring: true` in the analyzer config.

## Unit 3: Create a Content Understanding analyzer

**Q11.** What are the four high-level steps to build a Content Understanding solution, in the correct order?
A. Build analyzer → Create Foundry resource → Define schema → Use analyzer
B. Create Foundry resource → Define schema → Build analyzer → Use analyzer to extract/generate fields
C. Define schema → Create Foundry resource → Use analyzer → Build analyzer
D. Create Foundry resource → Build analyzer → Define schema → Test analyzer
**Answer:** B — 1) Create a Foundry resource, 2) define a schema (based on a content sample and analyzer template), 3) build an analyzer from the schema, 4) use the analyzer to extract/generate fields from new content.

**Q12.** Which tool should you use specifically for creating and testing **custom** analyzers, as opposed to only using certain prebuilt models available directly in the Microsoft Foundry portal?
A. Azure AI Search Studio
B. Content Understanding Studio
C. Azure Data Factory Studio
D. Bot Framework Composer
**Answer:** B — the module's Tip explicitly states that only certain prebuilt models are available directly in the Foundry portal, and for custom analyzer creation/testing you should use Content Understanding Studio.

**Q13.** When you create a new project in Content Understanding Studio, which Azure resources are automatically provisioned to support the solution?
A. A virtual network and a load balancer for traffic distribution
B. Storage and a key vault resource (for credentials/keys)
C. A SQL Database and a Redis cache for session state
D. An Azure Kubernetes Service cluster for hosting custom containers
**Answer:** B — creating a project provisions storage and a key vault resource to store sensitive details like credentials and keys.

**Q14.** A schema you're editing in Content Understanding Studio doesn't show the barcode/formula extraction options you expected. What is the most likely reason?
A. Those options require a Pro mode subscription that hasn't been activated on this resource
B. The templates and field types available in a schema depend on the content type of the file the schema is based on
C. Barcode and formula extraction were deprecated in the most recent API version release
D. You must enable them via Azure Policy first, using a custom compliance initiative
**Answer:** B — available templates/field types depend on content type; barcode and formula extraction are examples of optional functionality supported specifically for documents.

**Q15.** In an analyzer's field schema, which `method` value REQUIRES `estimateSourceAndConfidence` to be set to `true` for that field?
A. `generate`
B. `classify`
C. `extract`
D. `segment`
**Answer:** C — fields using `method: "extract"` require `estimateSourceAndConfidence: true` since extract is about literally pulling and grounding a value from the source location.

**Q16.** Which base analyzer IDs would you use as the `baseAnalyzerId` for a custom document analyzer versus a custom video analyzer, respectively?
A. `prebuilt-read` and `prebuilt-videoSearch`
B. `prebuilt-document` and `prebuilt-video`
C. `document-base` and `video-base`
D. `prebuilt-layout` and `prebuilt-videoAnalysis`
**Answer:** B — the four base analyzers are `prebuilt-document`, `prebuilt-audio`, `prebuilt-video`, and `prebuilt-image`.

**Q17.** (Single-task vs Pro-mode) Which statement correctly distinguishes Content Understanding's Standard mode from its Pro mode?
A. Standard mode supports multi-step reasoning across multiple input documents; Pro mode is limited to a single-shot schema extraction on one document, positioned as the main cost-saving option
B. Standard mode is optimized for efficient single-shot schema extraction across all modalities; Pro mode adds multi-step reasoning, multi-document input, and reference-data support, but is currently limited to documents only
C. Pro mode and Standard mode support exactly the same set of modalities and field methods, differing only in price, since both share the same reasoning engine
D. Standard mode is only available in Content Understanding Studio, while Pro mode is only available via the REST API, with no overlap in tooling between the two surfaces
**Answer:** B — Standard mode is the default, cost-effective, low-latency, single-task schema extraction mode across documents/images/video/audio; Pro mode adds multi-step reasoning and reference-data/multi-document support but currently only for document data.

**Q50.** After you "build" an analyzer in Content Understanding Studio once satisfied with schema testing, what happens, and what can you subsequently do?
A. The analyzer becomes accessible to client apps through the Foundry resource's endpoint, and you can continue refining the schema to create new named versions
B. The analyzer is permanently locked and can never be modified again, requiring a brand-new analyzer for any change
C. Building an analyzer immediately deletes the underlying schema, since the schema only exists during the build step
D. Building only generates documentation; it has no runtime effect until a separate deploy step is run against the Foundry resource
**Answer:** A — Building makes the analyzer accessible to client applications through the endpoint of the Microsoft Foundry resource associated with the project, and you can continue testing/refining to create new named versions with different capabilities.

**Q51.** In an analyzer configuration's `models` object (e.g., `"completion": "gpt-5.2", "embedding": "text-embedding-3-large"`), what do these values actually reference?
A. Specific Azure resource deployment names unique to your subscription, requiring manual lookup before use
B. Model names from the Foundry catalog, which the service maps to actual deployments at runtime — not deployment names themselves
C. Docker container image tags pinned to a specific model build and registry namespace
D. Regional availability zone identifiers used for latency-based deployment routing decisions
**Answer:** B — The module explicitly clarifies these are model names from the Foundry catalog, not deployment names — the service maps them to actual deployments at runtime.

**Q52.** If you omit the `method` property for a field in a Content Understanding field schema, what happens?
A. The analyzer build fails validation immediately with a missing-method schema error
B. The field is silently dropped from the schema without any warning in the build response
C. The system infers the best method to use based on the field's type and description
D. The field defaults to `method: "extract"` in all cases, regardless of its declared type
**Answer:** C — "If method isn't specified, the system infers the best method from field type/description."

**Q53.** Which HTTP method and response combination is used to create a new custom analyzer via the Content Understanding REST API?
A. `POST` to `/analyzers`, returning `200 OK` with the analyzer body, matching most other Azure REST APIs
B. `PUT` to `/analyzers/{analyzerId}?api-version=...`, returning `201 Created` with an `Operation-Location` header to track creation status
C. `PATCH` to `/analyzers/{analyzerId}`, returning `202 Accepted` with no headers, since updates don't need tracking
D. `PUT` to `/analyzers`, returning `204 No Content`, identical to how DELETE requests are typically handled
**Answer:** B — `curl -X PUT ".../contentunderstanding/analyzers/{analyzerId}?api-version=2025-11-01" ...` returns `201 Created` with an `Operation-Location` header to track analyzer-creation status.

**Q54.** For a document analyzer, which config property controls whether extracted tables are returned as HTML or as Markdown, and what is its default value?
A. `chartFormat`, default `"chartjs"`
B. `tableFormat`, default `"html"`
C. `annotationFormat`, default `"markdown"`
D. `enableLayout`, default `true`
**Answer:** B — `tableFormat` controls table output format (`"html"` or `"markdown"`), defaulting to `"html"`.

**Q55.** What is the distinction between `enableFigureDescription` and `enableFigureAnalysis` in a document analyzer's config?
A. They are aliases for the exact same setting, kept for backward compatibility with older schema versions predating the current API
B. `enableFigureDescription` produces natural-language descriptions of figures/diagrams (alt text); `enableFigureAnalysis` performs deeper analysis such as chart data extraction and diagram components
C. `enableFigureDescription` is for video only; `enableFigureAnalysis` is for documents only, since video figures aren't structurally identifiable
D. `enableFigureAnalysis` must be disabled whenever `enableFigureDescription` is enabled, to avoid duplicate processing charges on the same detected figure
**Answer:** B — `enableFigureDescription` (default `false`) gives natural-language descriptions/alt text of figures; `enableFigureAnalysis` (default `false`) does deeper analysis like extracting structured chart data or diagram components.

**Q56.** Which config property, when set to `true`, excludes the original content object from the analysis response and returns only structured/subanalyzer results?
A. `omitContent`
B. `segmentPerPage`
C. `returnDetails`
D. `enableAnnotations`
**Answer:** A — `omitContent` (default `false`), when `true`, excludes the original content object from the response, returning only structured/subanalyzer results.

## Unit 4: Use the Content Understanding API

**Q18.** What must a client application include in the HTTP header when calling the Content Understanding endpoint?
A. A shared access signature (SAS) token only
B. An authorization key (or Entra ID via the Foundry API)
C. A client certificate thumbprint registered in Key Vault
D. A refresh token issued by Content Understanding Studio
**Answer:** B — the client passes one of the authorization keys in the header; alternatively you can use the Microsoft Foundry API to connect programmatically with Entra ID.

**Q19.** After submitting a POST request to analyze content with an existing analyzer, what does the initial response return that the client must use to check the result later?
A. The final JSON result immediately, with no polling required at all
B. An operation ID representing an asynchronous task, to be polled via another request
C. A SAS URL to download the result file once processing finishes in the background
D. A WebSocket connection for streaming results as each field is extracted
**Answer:** B — the analysis request returns an operation ID for an asynchronous task; the client polls the `analyzerResults` endpoint with that operation ID until status is complete.

**Q20.** Given this request:
```json
POST {endpoint}/contentunderstanding/analyzers/{analyzer}:analyze?api-version=2025-11-01
{
  "inputs": [ { "url": "https://host.com/doc.pdf" } ]
}
```
What should you use instead if you need to submit binary file data directly rather than a URL?
A. The `analyzeBinary` operation
B. The `uploadBinary` operation
C. A `PUT` request to the same `:analyze` endpoint
D. The `analyzerResults` endpoint with a multipart body
**Answer:** A — the module notes that to submit binary file data directly (instead of a content URL), you use the `analyzeBinary` operation instead.

**Q21.** In the asynchronous analyze response below, which endpoint should the client poll and with which HTTP verb to retrieve the final result?
```http
Operation-Id: 1234abcd-1234-abcd-1234-abcd1234abcd
Operation-Location: {endpoint}/contentunderstanding/analyzerResults/1234abcd-1234-abcd-1234-abcd1234abcd?api-version=2025-11-01
```
A. `POST` to the `Operation-Location` URL
B. `GET` to the `analyzerResults/{operationId}` endpoint
C. `DELETE` to the `analyzers/{analyzer}` endpoint
D. `PATCH` to the `Operation-Id` endpoint
**Answer:** B — the client submits a GET request to the `analyzerResults` endpoint with the operation ID to check status until it succeeds/fails.

## Unit 5: Exercise — Extract information from multimodal content

**Q22.** In the module's hands-on exercise, which four content types does the learner practice extracting information from using Azure Content Understanding?
A. Documents, spreadsheets, presentations, and emails
B. Documents, images, audio files, and videos
C. Web pages, PDFs, images, and databases
D. Text files, JSON files, XML files, and CSV files
**Answer:** B — the exercise description states you use Content Understanding to extract information from documents, images, audio files, and videos.

**Q23.** What prerequisite does the exercise require before you can complete it?
A. A completed Azure AI-102 certification, verified against your Microsoft Learn profile
B. An Azure subscription in which you have administrative access
C. A pre-existing Azure AI Search index populated with sample documents
D. A GitHub Copilot license tied to your GitHub organization
**Answer:** B — the exercise note states you need an Azure subscription in which you have administrative access.

## Unit 7: Summary

**Q24.** According to the module summary, which tool did you use to create a Content Understanding project and build an analyzer?
A. Azure AI Search Studio
B. Content Understanding Studio
C. Azure Machine Learning Studio
D. Power Automate connectors
**Answer:** B — the summary states you learned how to use Content Understanding Studio to create a project and build an analyzer.

## Supplementary: Standard vs Pro mode deep dive

**Q25.** Which of the following capabilities are available in Pro mode but NOT in Standard mode? (Choose two.)
A. Multi-step reasoning
B. Grounding and confidence scores
C. Reference dataset integration at analyzer-creation time
D. Field mode (defining a fieldSchema)
E. Support for images, video, and audio as input
**Answer:** A, C — Pro mode adds multi-step reasoning and reference dataset integration; it actually loses grounding/confidence scores (B is Standard-only) and image/video/audio input support (E is Standard-only); field mode (D) is supported by both.

**Q26.** A solutions architect wants to validate that invoice totals match a signed contract on file, flagging any inconsistencies for review, using multiple related input documents plus a separate reference document. Which Content Understanding mode should they configure?
A. Standard mode with `enableSegment: true`
B. Pro mode
C. Standard mode with a `prebuilt-invoice` analyzer only
D. Standard mode with `contentCategories` classification
**Answer:** B — this is the canonical Pro-mode scenario: multi-document input, reference data, and multi-step reasoning to validate consistency and draw conclusions (e.g., "does this invoice fulfill the contractual agreement?").

**Q27.** Which field extraction `method` is explicitly NOT supported in Pro mode?
A. `generate`
B. `classify`
C. `extract`
D. All three methods are unsupported in Pro mode
**Answer:** C — Pro mode's known limitations state it supports `classify` and `generate` fields but does not support `extract` fields.

**Q28.** Which input content types does Pro mode currently support?
A. Documents, images, and video
B. Documents only
C. Audio and video only
D. All content types supported by Standard mode
**Answer:** B — Pro mode is currently available only for document data; other modalities are not yet supported.

## Supplementary: Video analysis — segmentation, shot detection, transcription

**Q29.** Which analyzer configuration property, when set to `true` on a video analyzer, returns shot-boundary timestamps in the `cameraShotTimesMs` output field?
A. `enableSegment`
B. `returnDetails`
C. `disableFaceBlurring`
D. `contentCategories`
**Answer:** B — sentence-level transcript timestamps and the `cameraShotTimesMs` shot-detection output are only returned when `"returnDetails": true` is set.

**Q30.** For a video analyzer, how many `contentCategories` objects are currently supported when `enableSegment` is set to `true`?
A. Unlimited
B. Up to 5
C. Only one
D. Exactly two — one for the start and one for the end
**Answer:** C — for video, only one `contentCategories` object is supported (unlike documents, which can define multiple categories).

**Q31.** Approximately what frame sampling rate does the Content Understanding video analyzer use when inspecting video content, and what is a direct consequence of this rate?
A. ~1 FPS; rapid motions or single-frame events might be missed
B. ~30 FPS; processing cost is very high for long videos
C. ~1 frame per minute; only long static scenes can be analyzed
D. Full frame rate of the source video; no information is ever lost
**Answer:** A — the analyzer samples at approximately 1 frame per second, meaning rapid motion or single-frame events can be missed.

**Q32.** What transcript format does the prebuilt video analyzer embed inline in its Markdown output?
A. SRT subtitle format
B. WEBVTT
C. Plain unstructured text
D. TTML captions
**Answer:** B — transcripts are output in standard WEBVTT format, both for video and audio analyzers.

**Q33.** (Choose two) Which two of the following are explicitly listed as technical constraints of Content Understanding video processing?
A. Frame resolution is downsampled to 512×512 pixels
B. Only spoken words are transcribed — music and ambient noise are ignored
C. Videos longer than 10 minutes are rejected
D. Only MP4 container format is supported
E. Maximum of 3 custom fields per analyzer
**Answer:** A, B — documented constraints are ~1 FPS frame sampling, 512×512 px frame resolution, and speech-only transcription (music/sound effects/ambient noise ignored).

**Q57.** For the prebuilt video analyzer, which output elements appear ONLY in the JSON output (not in the Markdown output)?
A. Transcript and Key Frame thumbnails, both already embedded inline in the Markdown
B. Description (natural-language segment descriptions) and Segmentation (automatic scene segmentation)
C. WEBVTT-formatted captions, which only ever appear in the Markdown output
D. `cameraShotTimesMs` timestamps only, gated behind `returnDetails: true`
**Answer:** B — Markdown output includes an inline Transcript (WEBVTT) and ordered Key Frame thumbnails; the JSON output additionally contains Description and Segmentation, which are not part of the Markdown output.

**Q58.** True statement about enabling segmentation (`enableSegment: true`) on a video analyzer even when no custom fields are defined in the schema?
A. It has no cost impact since no fields are extracted from the segments, so the generative model is never actually invoked
B. Setting segmentation invokes the generative model and consumes tokens even if no fields are defined
C. It disables the generative model entirely, relying only on deterministic shot detection
D. Segmentation is free but requires a separate paid add-on for token usage
**Answer:** B — The module explicitly notes: "Setting segmentation invokes the generative model and consumes tokens even if no fields are defined."

**Q59.** What is the key difference in orientation between the `prebuilt-videoAnalysis` analyzer and the `prebuilt-videoSearch` analyzer?
A. There is no difference; they are identical, just marketed under two IDs for discoverability in the catalog
B. `prebuilt-videoAnalysis` is the general prebuilt video analyzer, while `prebuilt-videoSearch` is the RAG-oriented variant optimized for retrieval-augmented generation scenarios
C. `prebuilt-videoSearch` only works on audio-only files, rejecting any analyzer request that contains video frames
D. `prebuilt-videoAnalysis` requires Pro mode; `prebuilt-videoSearch` requires Standard mode, reflecting a pricing-tier split between the two prebuilts
**Answer:** B — The content lists "the prebuilt video analyzer `prebuilt-videoAnalysis` / RAG-oriented `prebuilt-videoSearch`," distinguishing the RAG analyzer from the base/general one.

## Supplementary: Audio analysis — transcription, diarization, prebuilt analyzers

**Q34.** Which prebuilt audio analyzer would you use to generate a call summary, sentiment, mentioned companies, and speaker-role–attributed transcripts from a customer service recording?
A. `prebuilt-audioSearch`
B. `prebuilt-callCenter`
C. `prebuilt-videoAnalysis`
D. `prebuilt-read`
**Answer:** B — `prebuilt-callCenter` (post-call analysis) generates transcripts with speaker-role detection, a summary, sentiment, topics/articles, companies, people, and categories.

**Q35.** Which Content Understanding capability distinguishes between speakers in a conversation and attributes transcript segments to specific speakers?
A. Diarization
B. Segmentation
C. Grounding
D. Contextualization
**Answer:** A — diarization distinguishes between speakers in a conversation, attributing parts of the transcript to specific speakers.

**Q36.** According to the audio `locales` configuration guidance, what happens if multilingual transcription is used on a file containing an unsupported locale?
A. The request fails immediately with an error listing the unsupported locale code and the nearest supported alternative
B. The service produces a result based on the closest supported locale, which is likely incorrect — a known/expected behavior
C. The unsupported segment is silently omitted from the transcript, leaving a gap in the WEBVTT timeline
D. The service automatically translates the audio into English before transcribing, adding noticeable latency
**Answer:** B — this is documented as expected behavior; to avoid quality issues, explicitly configure `locales` instead of relying on multilingual/auto detection.

**Q60.** Per the audio `locales` file-size/latency matrix, what happens when you leave `locales` empty/`auto` on a file larger than 300 MB and longer than 2 hours (but at or under 4 hours)?
A. The request is rejected outright, requiring the caller to explicitly set `locales` before resubmitting
B. It still uses multilingual transcription, but result latency shifts from near-real-time to regular (rather than near-real-time)
C. It automatically switches to single-language transcription with near-real-time latency, ignoring the file's language mix
D. File size and duration have no effect on latency, since the service always uses a fixed worker pool
**Answer:** B — Per the matrix: `auto`/empty with size ≤300MB/≤2h gets multilingual transcription at near-real-time latency; the same auto/empty setting for files >300MB and >2h (up to 4h) still uses multilingual transcription but at "Regular" (non-near-real-time) latency.

**Q61.** Which solution accelerator combines Microsoft Foundry, Azure Content Understanding, Azure OpenAI in Microsoft Foundry Models, and Azure AI Search to map unstructured dialogue into structured insights like topic modeling and key-phrase extraction?
A. Conversational Knowledge Mining
B. Intelligent Document Processing Accelerator
C. Azure AI Language Studio
D. Cognitive Search Enrichment Accelerator
**Answer:** A — "Conversational Knowledge Mining — combines Microsoft Foundry, Azure Content Understanding, Azure OpenAI in Microsoft Foundry Models, and Azure AI Search to map unstructured dialogue to structured insights."

## Supplementary: Image analysis

**Q37.** A team wants to extract and analyze mostly printed/handwritten text visible within scanned images. What does Microsoft's guidance recommend instead of using an image field-extraction schema?
A. Use a video field-extraction schema
B. Use a document field-extraction schema
C. Use Pro mode exclusively for all text extraction
D. Use the `prebuilt-audioSearch` analyzer
**Answer:** B — image analyzers are not optimized for text-extraction-primary scenarios; the documentation recommends using a document field extraction schema instead when the main goal is extracting/analyzing text from an image.

**Q38.** Which analyzer configuration parameter controls whether faces are blurred in image (and video) analysis output, and must be set to enable detailed face description fields?
A. `enableFigureDescription`
B. `disableFaceBlurring`
C. `estimateFieldSourceAndConfidence`
D. `enableAnnotations`
**Answer:** B — setting `disableFaceBlurring: true` in the analyzer configuration enables face description capabilities (a Limited Access feature) for both image and video analyzers.

## Supplementary: Content Understanding vs Document Intelligence vs AI Search skillsets

**Q39.** A team needs to process highly structured tax forms that follow a small number of well-known official templates, prioritizing proven accuracy and low latency, and they already have several labeled samples per variant. Which tool does Microsoft's guidance recommend?
A. Azure Content Understanding Pro mode with a custom reference dataset
B. Azure Document Intelligence prebuilt or custom model
C. A hand-built Azure OpenAI pipeline with manually engineered prompts
D. Azure AI Search enrichment skillset only
**Answer:** B — for standardized/known-variant structured forms, Document Intelligence prebuilt or custom models (trainable with as few as 5 labeled samples) are recommended for consistency, low latency, and proven accuracy.

**Q40.** A team needs to extract inferred details (e.g., deriving a contract end date from a start date and duration, or identifying jurisdiction from party addresses) from highly variable, unstructured legal contracts, with no labeled data available. Which is the recommended approach?
A. Document Intelligence custom model trained from scratch, using at least five labeled samples per variant
B. Content Understanding prebuilt (`prebuilt-contract`) or custom analyzer, using zero-shot schema extraction
C. Azure AI Search semantic ranker alone, without any upstream field extraction step
D. A DI container deployed on-premises, requiring no cloud connectivity for reasoning
**Answer:** B — for unstructured documents requiring inference/reasoning without labeled data, Content Understanding's `prebuilt-contract` or a custom analyzer (zero-shot) is recommended; CU can infer fields not explicitly present in the text.

**Q41.** Which deployment requirement can ONLY be satisfied today by Azure Document Intelligence (not Content Understanding)?
A. Multilingual transcription of audio recordings
B. On-premises / air-gapped deployment via DI containers
C. Producing Markdown output for RAG ingestion
D. Defining a custom field schema with `generate` methods
**Answer:** B — per the decision guide, on-premises/air-gapped deployment is only available today via Document Intelligence containers; Content Understanding has no equivalent offline/container option in this guidance.

**Q42.** Which statement best characterizes the relationship between Azure Content Understanding analyzers and Azure AI Search enrichment skillsets? (general Azure knowledge, consistent with the module's positioning of Content Understanding for RAG ingestion)
A. They are the same service under two different names, merged into one Foundry Tool after the 2024 rebrand with a shared billing meter and unified pricing tier
B. Content Understanding analyzers are indexers that directly create and manage Azure AI Search indexes, bypassing the need for a separate indexer pipeline or search resource
C. Content Understanding is a content-processing/extraction service that produces structured JSON or Markdown output which can then be ingested into an Azure AI Search index; classic AI Search skillsets instead chain individual enrichment skills inside an indexer pipeline to produce that enriched content
D. Azure AI Search skillsets replace the need for any OCR or layout analysis when using Content Understanding, since its output already embeds fully analyzed results and cached layout metadata
**Answer:** C — Content Understanding centralizes multimodal extraction into a single analyzer producing ready-to-index output; AI Search enrichment skillsets are a separate indexer-pipeline mechanism for chaining cognitive skills. They are complementary, not identical, and Content Understanding itself is not a search/indexing service.

**Q43.** (Choose two) Which two of the following are advantages of using Azure Content Understanding or Document Intelligence over building a custom extraction pipeline directly on Azure OpenAI / Foundry models?
A. Built-in confidence scores and grounding without custom implementation
B. Guaranteed zero cost regardless of usage volume
C. Fully managed scalability instead of manual scaling
D. Automatic conversion of all field types to `extract` method only
E. No need to ever define a schema
**Answer:** A, C — the comparison table shows CU/DI provide built-in confidence & grounding and fully managed scalability, versus "build your own," which requires custom confidence implementation and manual scaling. (B, D, E are not supported claims.)

**Q62.** Which Content Understanding API version is the current GA version, and by when are the `2024-12-01-preview` and `2025-05-01-preview` versions being retired?
A. GA is `2025-11-01`; preview versions retire by July 15, 2026
B. GA is `2025-05-01-preview`; there is no retirement date announced
C. GA is `2024-12-01`; preview versions never retire
D. GA is `2026-01-01`; preview versions retired already
**Answer:** A — "As of the `2025-05-01-preview` API version..." with the note that preview API versions `2024-12-01-preview` and `2025-05-01-preview` are being retired by July 15, 2026 in favor of the GA `2025-11-01` API version.

## Scenario-based questions

**Q63.** *(Scenario)* You need a pipeline that ingests scanned invoices, product defect photos, and customer call recordings into one Azure AI Search index for a RAG chatbot, with confidence scores and source grounding on every extracted field, and no labeled training data available up front. Which single Foundry Tool satisfies this, and which two structured output formats would you expect back from the analyzer?
A. Azure Content Understanding; Markdown and structured JSON
B. Azure Document Intelligence; XML and CSV
C. Azure AI Vision; tags and captions only, with no schema support
D. A hand-built Azure OpenAI pipeline; Markdown only, with confidence built in automatically
**Answer:** A — Content Understanding is the unified multimodal (documents/images/audio/video) Foundry Tool with zero-shot schema extraction, built-in confidence and grounding, and it returns either Markdown (for search/retrieval) or structured JSON (for automation/analytics) — exactly the two output formats described throughout the module.

**Q64.** *(Scenario)* A compliance team wants to verify, across a batch of invoices and their corresponding signed contracts, whether each invoice total matches the contract terms and whether any clauses conflict — flagging discrepancies for review rather than just extracting raw field values. They only need this for document files. Which mode should they configure, and what tradeoff must they accept regarding confidence scores?
A. Standard mode; confidence scores remain available, since Standard always returns per-field confidence
B. Pro mode; they must accept the loss of built-in grounding and confidence scores, since Pro mode does not provide them
C. Standard mode with Pro mode enabled simultaneously for a hybrid result combining both modes' strengths
D. Neither mode supports document-to-document reference validation, regardless of configuration
**Answer:** B — This is the canonical Pro-mode use case (multi-document input + reference data + multi-step reasoning to flag inconsistencies), but Pro mode's known limitations explicitly state it has no confidence scores or grounding, unlike Standard mode.

**Q65.** *(Scenario)* You configure a video analyzer for an advertising-compliance use case: you need the whole ad checked for regulatory phrases anywhere in it (not split into segments), but you also separately want face description fields enabled to confirm no unauthorized celebrity likeness is used. What two config settings do you need, and what governance step is required for the face fields?
A. `enableSegment: true` for whole-video mode; `disableFaceBlurring: false`; no governance needed since face blurring only applies during segmentation
B. `enableSegment: false` for whole-video mode; `disableFaceBlurring: true` to enable face description fields; register for the Limited Access feature first
C. `contentCategories` with two objects; `enableFigureAnalysis: true`; no registration needed since these are unrelated settings
D. `enableSegment: true` with `segmentPerPage: true`; face fields are unavailable for video, contradicting the Responsible AI section
**Answer:** B — Whole-video mode (treating the entire file as one segment, appropriate for "compliance checks anywhere in an ad") uses `enableSegment: false`; face description fields require `disableFaceBlurring: true` AND registering for the Limited Access feature, per the module's Responsible AI and video sections.

**Q66.** *(Scenario)* Your team already has a production Document Intelligence integration extracting fields from standardized W-2 forms with 5 labeled training samples per variant, and now separately needs a new capability to summarize call-center recordings and detect sentiment, plus a new capability to reason over whether a claim document is consistent with a referenced policy document. How should these three needs be addressed, per the module's guidance?
A. Migrate the existing W-2 integration to Content Understanding immediately; use Pro mode for the call summarization; use Standard mode for the claim/policy consistency check, reversing the module's no-migration-required guidance
B. Leave the W-2 integration on Document Intelligence (no migration required for existing production workloads); use a Content Understanding `prebuilt-callCenter` analyzer (Standard mode) for call summarization/sentiment; use Content Understanding Pro mode with reference data for the claim-vs-policy consistency reasoning
C. Replace all three with a single Azure AI Search skillset, bypassing Content Understanding and Document Intelligence entirely for all workloads
D. Use Azure AI Vision object detection for all three needs, despite it having no summarization, transcription, or reasoning capability
**Answer:** B — The module explicitly states existing Document Intelligence production workloads require no migration; `prebuilt-callCenter` (Standard mode) is purpose-built for call summary/sentiment; and cross-document consistency reasoning against a reference document is the canonical Pro-mode scenario.
