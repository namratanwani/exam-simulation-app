# Practice questions — Create a multimodal analysis solution with Azure Content Understanding

Grounded in `content.md` for this module. Questions flagged "(general Azure knowledge)" draw on well-established platform knowledge beyond the fetched unit text.

## Unit 1: Introduction

**Q1.** Which Azure service is described as a multimodal service that simplifies the creation of AI-powered analyzers to extract information from content in practically any format (documents, images, audio, video)?
A. Azure AI Document Intelligence
B. Azure Content Understanding
C. Azure AI Vision
D. Azure AI Search
**Answer:** B — Azure Content Understanding is the multimodal service purpose-built for creating analyzers across documents, images, audio, and video.

**Q2.** Before Content Understanding existed, why did organizations often need multiple separate technologies to extract information from content?
A. Because Azure did not support any document processing services
B. Because different content formats (documents, images, video, audio) traditionally required different, format-specific technologies
C. Because Azure Content Understanding requires a separate resource per format
D. Because only text files could be analyzed by Azure AI services
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
A. A virtual network and a load balancer
B. Storage and a key vault resource (for credentials/keys)
C. A SQL Database and a Redis cache
D. An Azure Kubernetes Service cluster
**Answer:** B — creating a project provisions storage and a key vault resource to store sensitive details like credentials and keys.

**Q14.** A schema you're editing in Content Understanding Studio doesn't show the barcode/formula extraction options you expected. What is the most likely reason?
A. Those options require a Pro mode subscription
B. The templates and field types available in a schema depend on the content type of the file the schema is based on
C. Barcode and formula extraction were deprecated
D. You must enable them via Azure Policy first
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

**Q17. (Single-task vs Pro-mode)** Which statement correctly distinguishes Content Understanding's Standard mode from its Pro mode?
A. Standard mode supports multi-step reasoning across multiple input documents; Pro mode is limited to a single-shot schema extraction on one document
B. Standard mode is optimized for efficient single-shot schema extraction across all modalities; Pro mode adds multi-step reasoning, multi-document input, and reference-data support, but is currently limited to documents only
C. Pro mode and Standard mode support exactly the same set of modalities and field methods, differing only in price
D. Standard mode is only available in Content Understanding Studio, while Pro mode is only available via the REST API
**Answer:** B — Standard mode is the default, cost-effective, low-latency, single-task schema extraction mode across documents/images/video/audio; Pro mode adds multi-step reasoning and reference-data/multi-document support but currently only for document data.

## Unit 4: Use the Content Understanding API

**Q18.** What must a client application include in the HTTP header when calling the Content Understanding endpoint?
A. A shared access signature (SAS) token only
B. An authorization key (or Entra ID via the Foundry API)
C. A client certificate thumbprint
D. A refresh token issued by Content Understanding Studio
**Answer:** B — the client passes one of the authorization keys in the header; alternatively you can use the Microsoft Foundry API to connect programmatically with Entra ID.

**Q19.** After submitting a POST request to analyze content with an existing analyzer, what does the initial response return that the client must use to check the result later?
A. The final JSON result immediately
B. An operation ID representing an asynchronous task, to be polled via another request
C. A SAS URL to download the result file
D. A WebSocket connection for streaming results
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
A. A completed Azure AI-102 certification
B. An Azure subscription in which you have administrative access
C. A pre-existing Azure AI Search index
D. A GitHub Copilot license
**Answer:** B — the exercise note states you need an Azure subscription in which you have administrative access.

## Unit 7: Summary

**Q24.** According to the module summary, which tool did you use to create a Content Understanding project and build an analyzer?
A. Azure AI Search Studio
B. Content Understanding Studio
C. Azure Machine Learning Studio
D. Power Automate
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
B. ~30 FPS; processing cost is very high
C. ~1 frame per minute; only long static scenes can be analyzed
D. Full frame rate of the source video; no information is ever lost
**Answer:** A — the analyzer samples at approximately 1 frame per second, meaning rapid motion or single-frame events can be missed.

**Q32.** What transcript format does the prebuilt video analyzer embed inline in its Markdown output?
A. SRT
B. WEBVTT
C. Plain unstructured text
D. TTML
**Answer:** B — transcripts are output in standard WEBVTT format, both for video and audio analyzers.

**Q33. (Choose two)** Which two of the following are explicitly listed as technical constraints of Content Understanding video processing?
A. Frame resolution is downsampled to 512×512 pixels
B. Only spoken words are transcribed — music and ambient noise are ignored
C. Videos longer than 10 minutes are rejected
D. Only MP4 container format is supported
E. Maximum of 3 custom fields per analyzer
**Answer:** A, B — documented constraints are ~1 FPS frame sampling, 512×512 px frame resolution, and speech-only transcription (music/sound effects/ambient noise ignored).

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
A. The request fails immediately with an error
B. The service produces a result based on the closest supported locale, which is likely incorrect — a known/expected behavior
C. The unsupported segment is silently omitted from the transcript
D. The service automatically translates the audio into English before transcribing
**Answer:** B — this is documented as expected behavior; to avoid quality issues, explicitly configure `locales` instead of relying on multilingual/auto detection.

## Supplementary: Image analysis

**Q37.** A team wants to extract and analyze mostly printed/handwritten text visible within scanned images. What does Microsoft's guidance recommend instead of using an image field-extraction schema?
A. Use a video field-extraction schema
B. Use a document field-extraction schema
C. Use Pro mode exclusively
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
A. Azure Content Understanding Pro mode
B. Azure Document Intelligence prebuilt or custom model
C. A hand-built Azure OpenAI pipeline
D. Azure AI Search enrichment skillset only
**Answer:** B — for standardized/known-variant structured forms, Document Intelligence prebuilt or custom models (trainable with as few as 5 labeled samples) are recommended for consistency, low latency, and proven accuracy.

**Q40.** A team needs to extract inferred details (e.g., deriving a contract end date from a start date and duration, or identifying jurisdiction from party addresses) from highly variable, unstructured legal contracts, with no labeled data available. Which is the recommended approach?
A. Document Intelligence custom model trained from scratch
B. Content Understanding prebuilt (`prebuilt-contract`) or custom analyzer, using zero-shot schema extraction
C. Azure AI Search semantic ranker alone
D. A DI container deployed on-premises
**Answer:** B — for unstructured documents requiring inference/reasoning without labeled data, Content Understanding's `prebuilt-contract` or a custom analyzer (zero-shot) is recommended; CU can infer fields not explicitly present in the text.

**Q41.** Which deployment requirement can ONLY be satisfied today by Azure Document Intelligence (not Content Understanding)?
A. Multilingual transcription of audio
B. On-premises / air-gapped deployment via DI containers
C. Producing Markdown output for RAG ingestion
D. Defining a custom field schema with `generate` methods
**Answer:** B — per the decision guide, on-premises/air-gapped deployment is only available today via Document Intelligence containers; Content Understanding has no equivalent offline/container option in this guidance.

**Q42.** Which statement best characterizes the relationship between Azure Content Understanding analyzers and Azure AI Search enrichment skillsets? (general Azure knowledge, consistent with the module's positioning of Content Understanding for RAG ingestion)
A. They are the same service under two different names
B. Content Understanding analyzers are indexers that directly create and manage Azure AI Search indexes
C. Content Understanding is a content-processing/extraction service that produces structured JSON or Markdown output which can then be ingested into an Azure AI Search index; classic AI Search skillsets instead chain individual enrichment skills inside an indexer pipeline to produce that enriched content
D. Azure AI Search skillsets replace the need for any OCR or layout analysis when using Content Understanding
**Answer:** C — Content Understanding centralizes multimodal extraction into a single analyzer producing ready-to-index output; AI Search enrichment skillsets are a separate indexer-pipeline mechanism for chaining cognitive skills. They are complementary, not identical, and Content Understanding itself is not a search/indexing service.

**Q43. (Choose two)** Which two of the following are advantages of using Azure Content Understanding or Document Intelligence over building a custom extraction pipeline directly on Azure OpenAI / Foundry models?
A. Built-in confidence scores and grounding without custom implementation
B. Guaranteed zero cost regardless of usage volume
C. Fully managed scalability instead of manual scaling
D. Automatic conversion of all field types to `extract` method only
E. No need to ever define a schema
**Answer:** A, C — the comparison table shows CU/DI provide built-in confidence & grounding and fully managed scalability, versus "build your own," which requires custom confidence implementation and manual scaling. (B, D, E are not supported claims.)
