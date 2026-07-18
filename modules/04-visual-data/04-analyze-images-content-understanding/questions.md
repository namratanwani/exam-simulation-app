# Practice questions — Analyze images with Content Understanding

Grounded in `content.md` for this module. Questions flagged **[general knowledge]** draw on well-established Azure facts beyond the module's unit text.

## Unit 1: Introduction

**Q1.** What is the primary problem that Azure Content Understanding is designed to solve?

A. Training custom object-detection models from scratch
B. Extracting valuable information from unstructured content (images, documents, etc.) that's hard to extract automatically
C. Replacing Azure Kubernetes Service for container orchestration
D. Providing real-time speech translation for call centers

**Answer:** B — Per Unit 1: "Images, documents, and other unstructured content often contain valuable information that's hard to extract automatically. Azure Content Understanding solves this problem by using generative AI to analyze content and return structured data."

---

**Q2.** With Azure Content Understanding, how does a developer specify what data should be extracted from an image?

A. By writing a regular expression against the raw image bytes
B. By training a custom neural network on labeled images
C. By defining a schema that describes the desired data
D. By selecting from a fixed list of built-in tags only

**Answer:** C — "you define a schema describing the data you want, and the service extracts it from your images and documents."

---

**Q3.** Which two types of analyzers does the module say you'll learn to use when analyzing images with Content Understanding? (Choose two.)

A. Prebuilt analyzers
B. Federated analyzers
C. Custom analyzers
D. Streaming analyzers

**Answer:** A, C — "you'll learn how to analyze images with Content Understanding using both prebuilt and custom analyzers."

---

## Unit 2: What is Content Understanding?

**Q4.** Azure Content Understanding is best categorized as which of the following in the Microsoft Foundry ecosystem?

A. A Foundry Tool
B. A standalone virtual machine image
C. A Kubernetes operator
D. A load-balancing service

**Answer:** A — "Azure Content Understanding is a Foundry Tool that uses generative AI to process and extract insights from many types of content, including documents, images, videos, and audio."

---

**Q5.** Which of the following content types can Azure Content Understanding process? (Choose three.)

A. Documents
B. Images
C. Video
D. Relational database schemas

**Answer:** A, B, C — (Audio is also supported, but only 3 options can be marked here; the fourth listed, "Relational database schemas," is not a supported content type.) Correct set from content: documents, images, video, and audio.

---

**Q6.** In the Content Understanding pipeline, which component is responsible for identifying the specific regions in the source content where each extracted value was found?

A. Field extraction
B. Confidence scores
C. Grounding
D. Content extraction

**Answer:** C — Per the components table: "Grounding — Identifies specific regions in content where each value was extracted."

---

**Q7.** A developer needs the Content Understanding pipeline stage that turns unstructured input (e.g., a scanned image) into normalized text and metadata using OCR, speech transcription, and layout detection. Which stage is this?

A. Field extraction
B. Content extraction
C. Structured output
D. Analyzer

**Answer:** B — "Content extraction — Transforms unstructured input into normalized text and metadata using OCR, speech transcription, and layout detection."

---

**Q8.** When you create a Content Understanding analyzer, which of the following do you configure? (Choose three.)

A. The base analyzer type (document, image, audio, or video)
B. The AI models to use for processing
C. The field schema that defines what data to extract
D. The Azure region failover priority list

**Answer:** A, B, C — Per Unit 2: "When you create an analyzer, you configure: The base analyzer type (document, image, audio, or video); The AI models to use for processing; The field schema that defines what data to extract; Options like confidence scoring and content segmentation." Region failover priority is not part of analyzer configuration in the module content.

---

**Q9.** Which Azure service does Content Understanding integrate with to detect and prevent harmful content?

A. Azure AI Content Safety
B. Azure Purview
C. Azure Sentinel
D. Azure Policy

**Answer:** A — "The service integrates Azure AI Content Safety to detect and prevent harmful content."

---

**Q10.** [Content Understanding vs Azure AI Vision vs Document Intelligence] A team needs to build a single unified pipeline that extracts a custom set of business fields — with confidence scores and source grounding — from a mix of product images, PDFs, and call-center audio recordings. Which Azure capability best fits this requirement, and why?

A. Azure AI Vision Image Analysis, because it returns tags, captions, and objects across image formats
B. Azure Content Understanding, because it lets you define a custom field schema and produces structured output with confidence scores and grounding across documents, images, video, and audio in one framework
C. Azure AI Document Intelligence, because it supports prebuilt invoice and receipt models
D. A raw GPT-4o vision call, because it can reason over any image content

**Answer:** B — Content Understanding is explicitly described as processing "documents, images, videos, and audio" through one framework using a defined field schema, with built-in confidence scores and grounding. Azure AI Vision's outputs (tags/captions/objects) are fixed, not schema-driven; Document Intelligence is document/OCR-centric and doesn't natively cover audio; a raw multimodal LLM call has no built-in confidence/grounding structure.

---

## Unit 3: Analyze images with Content Understanding

**Q11.** Which of the following are supported image input formats for Content Understanding according to the module? (Choose three.)

A. JPEG
B. HEIF
C. GIF
D. TIFF

**Answer:** A, B, D — Supported formats listed: JPEG, PNG, BMP, TIFF, HEIF, PDF. GIF is not listed as supported.

---

**Q12.** Which prebuilt analyzer is designed to extract vendor names, items, totals, and dates specifically from receipt images?

A. prebuilt-invoice
B. prebuilt-image
C. prebuilt-receipt
D. prebuilt-idDocument

**Answer:** C — "prebuilt-receipt: Extract vendor names, items, totals, and dates from receipt images."

---

**Q13.** Which prebuilt analyzer would you use for general-purpose image analysis that includes content extraction and figure description, without a specialized document type?

A. prebuilt-image
B. prebuilt-invoice
C. prebuilt-receipt
D. prebuilt-idDocument

**Answer:** A — "prebuilt-image: General-purpose image analysis with content extraction and figure description."

---

**Q14.** When defining a custom field schema for an image analyzer, which extraction `method` would you use to categorize a product image as "new," "used," or "damaged" from a predefined list of options?

A. extract
B. generate
C. classify
D. summarize

**Answer:** C — "classify: Categorize content from predefined options. Example: Classify image as 'damaged' or 'undamaged'." The example schema uses `"method": "classify"` with an `"enum": ["new", "used", "damaged"]` for the `Condition` field.

---

**Q15.** In a Content Understanding field schema, which extraction method would you use to have the service create a free-text description of what a scene in the image shows, rather than pull an exact value present in the image?

A. extract
B. generate
C. classify
D. detect

**Answer:** B — "generate: Create values based on image analysis. Example: Generate a description of the scene."

---

**Q16.** Which pip package would you install to use the Content Understanding Python SDK?

A. azure-ai-vision
B. azure-cognitiveservices-vision-contentanalysis
C. azure-ai-contentunderstanding
D. azure-ai-formrecognizer

**Answer:** C — `pip install azure-ai-contentunderstanding`

---

**Q17.** In the Content Understanding Python SDK example, which method is called on the `ContentUnderstandingClient` to submit an image for analysis, and what does it return?

A. `client.analyze_image()`, which returns the result synchronously
B. `client.begin_analyze()`, which returns a poller you call `.result()` on
C. `client.submit_job()`, which returns a job ID string only
D. `client.get_analysis()`, which streams results via websocket

**Answer:** B — The example calls `poller = client.begin_analyze(analyzer_id=..., inputs=[AnalysisInput(data=file_bytes)])` then `result: AnalysisResult = poller.result()`, indicating a long-running operation pattern.

---

**Q18.** Which two credential types are shown in the module's Python SDK example for authenticating a `ContentUnderstandingClient`? (Choose two.)

A. `AzureKeyCredential` (key-based authentication)
B. `ManagedIdentityCredential` only
C. `DefaultAzureCredential` (Entra ID authentication)
D. `ClientSecretCredential` explicitly instantiated in the sample

**Answer:** A, C — The code imports `AzureKeyCredential # for key-based authentication` from `azure.core.credentials` and `DefaultAzureCredential # for Entra ID authentication` from `azure.identity`.

---

**Q19.** In the analysis result JSON returned by Content Understanding, which field provides a text representation of the image content that is described as useful for search and RAG scenarios?

A. `fields`
B. `source`
C. `markdown`
D. `contents.summary`

**Answer:** C — "markdown: A text representation of the image content, useful for search and RAG scenarios."

---

**Q20.** An extracted field in a Content Understanding response has a confidence score of 0.72. Per the module's guidance, what should you do with this result?

A. Process it automatically with no review since it exceeds a minimum threshold
B. Reject it outright since it is below 0.9
C. Consider it for human review, since it falls in the medium confidence band (0.7-0.9)
D. Discard it silently and re-run analysis

**Answer:** C — "Medium confidence (0.7-0.9): Consider human review for critical applications."

---

**Q21.** [Content Understanding vs Azure AI Vision] A developer currently uses the Azure AI Vision Image Analysis API to get fixed captions, tags, and detected objects for a photo library, but now needs to extract a custom field like "SerialNumber" from a product label with a confidence score and grounding coordinates. What is the most accurate statement about migrating this requirement?

A. Azure AI Vision Image Analysis already supports arbitrary custom field schemas, so no change is needed
B. Azure Content Understanding is required because it supports defining custom fields (via `extract`/`classify`/`generate` methods) with per-field confidence scores and grounding, which Image Analysis's fixed tag/caption/object output does not provide
C. Document Intelligence must be used instead because Image Analysis cannot process product photos
D. The developer should switch to Azure AI Search's built-in OCR skill, which supports custom field schemas natively

**Answer:** B — Image Analysis returns fixed outputs (tags, captions, objects); only Content Understanding's schema-driven field extraction (`extract`, `classify`, `generate`) with confidence + `source` grounding meets this requirement. [Partially general knowledge: Image Analysis's fixed-output behavior is standard Azure AI Vision knowledge, not stated verbatim in this module's unit text.]

---

## Unit 4: Exercise — Analyze images with Content Understanding

**Q22.** In the hands-on exercise for this module, what are the two main tasks a learner performs? (Choose two.)

A. Create a custom image analyzer in the Microsoft Foundry portal
B. Train a custom object-detection CNN model from scratch
C. Create a Python application that uses the Content Understanding API to analyze images programmatically
D. Configure an Azure Kubernetes Service cluster to host the analyzer

**Answer:** A, C — "First, you create a custom image analyzer in the Microsoft Foundry portal. Then, you create a Python application that uses the Content Understanding API to analyze images programmatically and extract structured data."

---

**Q23.** What prerequisite does the exercise state is required to complete it?

A. A GitHub Enterprise account
B. An Azure subscription
C. A Microsoft 365 E5 license
D. A pre-existing Azure AI Vision resource

**Answer:** B — "To complete this exercise, you need an Azure subscription."

---

## Unit 5: Module assessment (knowledge check)

**Q24.** Per the module's official knowledge check, what is the purpose of grounding in Content Understanding?

A. To connect Content Understanding to Azure storage
B. To identify the specific regions in content where each value was extracted
C. To filter out harmful content from images
D. To classify the analyzer's base type

**Answer:** B — This matches the module assessment's stated correct answer and Unit 2's definition of grounding.

---

**Q25.** Per the module's official knowledge check, what does a confidence score of 0.95 indicate for an extracted field?

A. The extraction failed and needs manual review
B. The value can be trusted for automated processing
C. The field was classified rather than extracted
D. The field requires re-analysis with a different analyzer

**Answer:** B — Matches the "High confidence (0.9+): Value can be trusted for automated processing" guidance from Unit 3.

---

**Q26.** Per the module's official knowledge check, which prebuilt analyzer would you use to extract vendor names and item totals from a purchase receipt?

A. prebuilt-image
B. prebuilt-invoice
C. prebuilt-receipt
D. prebuilt-idDocument

**Answer:** C — `prebuilt-receipt` is explicitly described for exactly this purpose in Unit 3; `prebuilt-invoice` is for invoices, a related but distinct document type.

---

## Unit 6: Summary

**Q27.** According to the module summary, which of the following did learners explore in this module? (Choose three.)

A. The components of Content Understanding, including analyzers, field extraction, and confidence scores
B. Using prebuilt analyzers for scenarios like receipts, invoices, and identity documents
C. Defining field schemas with extract, classify, and generate methods
D. Fine-tuning a custom GPT-4o vision model on labeled image datasets

**Answer:** A, B, C — Per the summary: "Understand the components of Content Understanding...Use prebuilt analyzers...Define field schemas with extract, classify, and generate methods...Analyze images using the Content Understanding API." Fine-tuning a custom GPT-4o model is not part of this module.

---

**Q28.** [Content Understanding vs Document Intelligence vs raw multimodal LLM — general knowledge extension] Which statement best distinguishes Azure Content Understanding from a raw multimodal LLM vision call (e.g., prompting GPT-4o directly with an image)?

A. Content Understanding cannot process images at all, only documents
B. A raw multimodal LLM call natively returns per-field confidence scores and grounding coordinates, while Content Understanding does not
C. Content Understanding provides a structured, schema-driven pipeline with built-in per-field confidence scores and source grounding, whereas a raw multimodal LLM call produces free-form output unless you separately engineer structured-output constraints and have no native confidence/grounding metadata
D. Both approaches are functionally identical and differ only in pricing

**Answer:** C — Content Understanding's analyzer output includes `fields` with `confidence` and `source` grounding by design; a bare multimodal LLM prompt/response has no such built-in structure. [Flagged: the multimodal-LLM side of this comparison is general Azure/LLM knowledge, not stated in this module's unit text, though the module implicitly supports the Content Understanding side.]

---

**Q29.** A solutions architect is deciding between Azure Content Understanding and Azure AI Document Intelligence for a new project that must process scanned invoices, product photos, AND customer service call recordings within one consistent extraction pipeline. Which service should they choose, and why?

A. Azure AI Document Intelligence, because it has the most mature prebuilt invoice model
B. Azure Content Understanding, because it is a Foundry Tool that spans documents, images, video, and audio in a single analyzer framework, whereas Document Intelligence is document/OCR-centric and does not natively process audio
C. Azure AI Vision, because Image Analysis supports OCR "Read" across all content types
D. Either service works identically since both use the same underlying models

**Answer:** B — Content Understanding explicitly supports "documents, images, videos, and audio" in one framework; Document Intelligence is positioned (general Azure knowledge, reinforced by this module's scope) as document/OCR-centric and does not cover audio/video natively.
