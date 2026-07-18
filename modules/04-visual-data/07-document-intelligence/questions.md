# Practice questions — Extract data with Azure Document Intelligence

Grounded in `content.md` (source: https://learn.microsoft.com/en-us/training/modules/extract-data-with-document-intelligence/). Questions marked **[general knowledge]** draw on well-established Azure knowledge beyond the fetched module text (flagged inline as instructed).

## Unit 1 — Introduction

**Q1.** Which Microsoft Foundry platform does Azure Document Intelligence belong to, and what two core technologies does it combine to extract text, key-value pairs, tables, and structured data from documents?

A. Azure AI Search; full-text indexing and semantic ranking
B. Microsoft Foundry; optical character recognition (OCR) and deep learning models
C. Azure AI Vision; image classification and object detection
D. Azure Machine Learning; AutoML and hyperparameter tuning

**Answer:** B — The module defines Azure Document Intelligence as "a cloud-based service in Microsoft Foundry that uses optical character recognition (OCR) and deep learning models to extract text, key-value pairs, tables, and structured data from forms and documents."

---

**Q2.** According to the module introduction, which THREE capability categories does Azure Document Intelligence provide? (Choose three.)

A. Prebuilt models for common document types
B. Document analysis models for general text extraction
C. Real-time video object tracking
D. The ability to train custom models for specific forms
E. Automatic language translation of extracted text

**Answer:** A, B, D — The introduction states Document Intelligence "offers prebuilt models for common document types, document analysis models for general text extraction, and the ability to train custom models for your specific forms."

---

**Q3.** A company wants to automate extraction of key data from thousands of invoices, receipts, and tax forms each month, without building a deep-learning model from scratch. Which capability of Document Intelligence directly addresses this, per the module's introductory scenario?

A. Custom neural models trained on 10,000+ labeled examples
B. Prebuilt models, already trained on thousands of form examples
C. A composed model created from five custom classifiers
D. The Azure AI Vision Image Analysis API

**Answer:** B — The scenario is resolved by Document Intelligence's prebuilt models, which require no training and are designed exactly for common, high-volume document types like invoices, receipts, and tax forms.

## Unit 2 — What is Azure Document Intelligence?

**Q4.** What output format does Azure Document Intelligence return, and what does it preserve from the original document?

A. CSV; only the raw extracted text
B. XML; only the table structure
C. Structured JSON; bounding box data and relationships from the original document
D. YAML; the document's file metadata only

**Answer:** C — "Azure Document Intelligence returns bounding box data and other information in a structured JSON format that preserves the relationships from the original document."

---

**Q5.** Which THREE of the following are valid ways to access Azure Document Intelligence, according to the module? (Choose three.)

A. REST API
B. Client library SDKs (Python, C#, Java, JavaScript)
C. Document Intelligence Studio
D. Azure Data Factory pipeline templates
E. Power BI connector

**Answer:** A, B, C — The module lists REST API, client library SDKs (Python, C#, Java, JavaScript), Document Intelligence Studio, and the Microsoft Foundry portal as access methods. Data Factory and Power BI connectors are not mentioned.

---

**Q6.** Your organization needs to use Document Intelligence exclusively — no other Foundry AI services are planned. Which resource type should you create, and why?

A. A Foundry resource, because it always costs less than a single-service resource
B. An Azure Document Intelligence resource — a single-service resource used only with Document Intelligence
C. An Azure AI Search resource, because Document Intelligence requires a search index
D. A Foundry resource, because Document Intelligence cannot be provisioned as a standalone resource

**Answer:** B — Per the module: "Create a Foundry resource if you plan to access multiple Foundry tools under a single endpoint and key. For Document Intelligence access only, create a dedicated Document Intelligence resource."

---

**Q7.** You're validating whether a document meets Azure Document Intelligence's input requirements before submitting it for analysis. Which of the following would cause the request to be REJECTED?

A. A 2 MB PDF submitted against a free-tier resource
B. A password-protected PDF
C. A PNG image sized 500 x 500 pixels
D. A TIFF file

**Answer:** B — PDF documents must not be password-protected. (A is fine, since free tier allows under 4 MB; C is within the 50x50–10,000x10,000 pixel range; D is an accepted format.)

---

**Q8.** What is the maximum file size Azure Document Intelligence accepts under the standard tier, and under the free tier, respectively?

A. 500 MB standard tier / 4 MB free tier
B. 50 MB standard tier / 1 MB free tier
C. 1 GB standard tier / 10 MB free tier
D. 4 MB standard tier / 500 MB free tier

**Answer:** A — File size must be less than 500 MB for the standard tier and 4 MB for the free tier.

## Unit 3 — Use the Document Intelligence Studio

**Q9.** What is the URL used to access the Document Intelligence Studio?

A. https://portal.azure.com/documentintelligence
B. https://ai.azure.com/documentintelligence
C. https://documentintelligence.ai.azure.com
D. https://formrecognizer.azure.com

**Answer:** C — The module states: "You can access the Studio at https://documentintelligence.ai.azure.com."

---

**Q10.** When building a custom model project in the Document Intelligence Studio, what does the Studio generate automatically on your behalf, removing the need to manually create these files?

A. `model.json`, `endpoint.json`, and `key.json`
B. `ocr.json`, `labels.json`, and `fields.json`
C. `schema.json` and `analyzer.json`
D. `train.csv` and `test.csv`

**Answer:** B — "The Studio generates the required `ocr.json`, `labels.json`, and `fields.json` files automatically," avoiding manual JSON authoring.

---

**Q11.** Place the following Studio custom-model workflow steps in the correct order:
1. Configure CORS on the storage container
2. Train the model and review accuracy metrics
3. Upload at least 5–6 sample forms to Azure Blob Storage
4. Label fields using the Studio's visual interface
5. Create the custom model project, linking storage and the Document Intelligence resource

A. 3, 1, 5, 4, 2
B. 1, 3, 4, 5, 2
C. 5, 3, 1, 2, 4
D. 3, 5, 1, 4, 2

**Answer:** A — Correct order per the module: upload sample forms (3) → configure CORS (1) → create the project (5) → label fields (4) → train and review accuracy (2).

---

**Q12.** Which TWO of the following are listed as Document Intelligence add-on capabilities in the module, and are called out as potentially incurring extra cost? (Choose two.)

A. High resolution extraction
B. Real-time speech transcription
C. Barcode extraction
D. Sentiment analysis
E. Automatic PII redaction

**Answer:** A, C — The add-on capabilities table lists high resolution extraction, formula extraction, font property extraction, barcode extraction, searchable PDF, query fields, and key-value pairs — with a note that "some add-on capabilities are premium features that incur extra costs." Speech transcription, sentiment analysis, and automatic PII redaction are not part of this list.

## Unit 4 — Use prebuilt models

**Q13.** You need to extract words and lines of text from a set of scanned documents that have no fixed or predictable structure, and you don't need table or key-value pair extraction. Which document analysis model is the best fit?

A. The layout model
B. The read model
C. The invoice model
D. The general document model

**Answer:** B — "The read model is ideal when you want to extract words and lines from documents with no fixed or predictable structure." The layout model adds structure/table detection you don't need here; the general document model is deprecated (see Q16).

---

**Q14.** Which model extends the read model's capabilities by adding detection of selection marks, tables, and document structure, plus an optional `keyValuePairs` feature?

A. prebuilt-invoice
B. The layout model
C. The read model
D. A custom template model

**Answer:** B — The layout model "extends the read model's text extraction with detection of selection marks, tables, and document structure information," and "supports an optional `keyValuePairs` feature."

---

**Q15.** For a multi-page PDF, which parameter can you use with the read model to restrict analysis to a specific page range?

A. `range`
B. `pageSpan`
C. `pages`
D. `pageLimit`

**Answer:** C — "For multi-page PDF or TIFF files, you can use the `pages` parameter in your request to specify a page range for analysis."

---

**Q16.** The "general document model" that existed in earlier versions of Document Intelligence was deprecated. Which release deprecated it, and where did its key-value pair/entity extraction functionality go?

A. Deprecated in `2022-08-31`; functionality moved to the read model
B. Deprecated in `2023-10-31-preview`; functionality incorporated into the layout model and other features
C. Deprecated in `2024-02-29-preview`; functionality moved to Content Understanding
D. It was never deprecated — it is still the recommended model for key-value extraction

**Answer:** B — "The general document model was available in earlier versions of Document Intelligence, but was deprecated in the `2023-10-31-preview` release. Its functionality for key-value pair and entity extraction has been incorporated into the layout model and other features."

---

**Q17.** A finance team needs to extract customer name, vendor details, purchase order number, dates, billing/shipping addresses, line items, and totals from vendor bills. Which prebuilt model should they use?

A. prebuilt-receipt (Receipt model)
B. prebuilt-invoice (Invoice model)
C. prebuilt-contract (Contract model)
D. prebuilt-layout (Layout model)

**Answer:** B — The Invoice model "extracts customer name, vendor details, purchase order number, invoice and due dates, billing and shipping addresses, line items, and totals" — this is an exact match; the Receipt model instead covers merchant details/transaction time/line items/totals for retail-style receipts.

---

**Q18.** Which TWO of the following prebuilt models fall under the "US tax documents" category described in the module? (Choose two.)

A. Unified US tax
B. W-2
C. Closing disclosure
D. 1003 (URLA)
E. Check

**Answer:** A, B — Unified US tax and W-2 (along with 1098/1099/1040 variations) are US tax documents. Closing disclosure and 1003 (URLA) are US mortgage documents; Check is a financial/legal document.

---

**Q19.** An application needs to extract names, dates of birth, document numbers, and endorsements/restrictions from driver's licenses and passports. Which prebuilt model applies, and what compliance consideration does the module explicitly call out?

A. The ID document model; ensure you have the individual's permission to store their data and comply with applicable data-protection laws
B. The layout model; no special compliance considerations apply
C. The health insurance card model; requires HIPAA-specific Azure regions
D. The marriage certificate model; requires notarization metadata

**Answer:** A — The ID document model extracts exactly these fields, and the module warns: "The ID document model extracts personal information covered by data protection laws in most jurisdictions. Ensure you have the individual's permission to store their data and that you comply with all applicable legal requirements."

---

**Q20.** Before investing time and sample data into training a custom model, what does the module recommend you do?

A. Always train a custom neural model first as a performance baseline
B. Check whether a prebuilt model already exists for your document type
C. Contact Microsoft support to request a new prebuilt model
D. Convert all documents to searchable PDF format first

**Answer:** B — "Always check whether a prebuilt model exists for your scenario before investing in custom model development."

## Unit 5 — Train and use custom models

**Q21.** Your documents have a consistent, static visual layout (e.g., a standardized government application form) and you need fast, low-cost training. Which custom model type is the best fit, and roughly how long does training take?

A. Custom neural model; several hours
B. Custom template model; only a few minutes
C. A composed model; training is not required
D. The layout model; training is not required since it is prebuilt

**Answer:** B — "Custom template models rely on a consistent visual template... Training takes only a few minutes, and more than 100 languages are supported... they're a good starting point when your documents have a uniform visual layout."

---

**Q22.** Which custom model type combines layout and language features via deep learning, supports overlapping fields and signature detection, and gives higher accuracy on semi-structured or unstructured documents where the layout varies between instances?

A. Custom template model
B. Custom classifier
C. Custom neural model
D. Composed model

**Answer:** C — Custom neural models "use deep learning and are fine-tuned on your labeled data... support overlapping fields, signature detection, table/row/cell level confidence... deliver higher accuracy overall, especially for documents with format variation," though they take longer to train and consume more resources.

---

**Q23.** Which TWO factors does the module identify as advantages of custom template models over custom neural models? (Choose two.)

A. Lower training cost
B. Support for overlapping fields
C. Broader language support (100+ languages)
D. Table/row/cell-level confidence scores
E. Higher accuracy on unstructured documents

**Answer:** A, C — Per the comparison table: custom template models have lower training cost and support 100+ languages (vs. neural's "fewer languages"). Overlapping fields, cell-level confidence, and higher accuracy on unstructured documents are neural-model strengths.

---

**Q24.** You need to route incoming documents — some invoices, some receipts, some contracts — to the correct extraction model automatically before extraction happens. Which custom model construct is purpose-built for this?

A. Custom neural model
B. Custom classifier
C. The read model
D. Custom template model

**Answer:** B — "Custom classification models identify the type of a document before invoking an extraction model. You can use a classifier to route incoming documents to the appropriate extraction model when you're handling multiple form types."

---

**Q25.** When training a custom model via the REST API/blob-container workflow (not the Studio), which set of JSON artifacts is required per the module?

A. A single `manifest.json` describing all forms
B. `ocr.json` per sample form, one `fields.json`, and `labels.json` per sample form
C. `schema.json`, `analyzer.json`, and `pipeline.json`
D. Only `labels.json` — `ocr.json` and `fields.json` are optional

**Answer:** B — "An `ocr.json` file for each sample form... A single `fields.json` file describing the fields you want to extract. A `labels.json` file for each sample form, mapping fields to their location in the form."

---

**Q26.** After uploading sample forms and JSON artifacts to blob storage, what must you generate for the container before calling the Build model function?

A. A managed identity role assignment
B. A shared access signature (SAS) URL
C. A CORS policy only (no SAS needed)
D. An Azure Private Link endpoint

**Answer:** B — "Generate a shared access signature (SAS) URL for the container," then "Use the Build model REST API function or the equivalent SDK method."

---

**Q27.** In the module's C# code sample for analyzing a document with a custom model, which class is instantiated with an endpoint and an `AzureKeyCredential`, and which method is called to start the analysis operation?

A. `DocumentIntelligenceClient`; `Analyze()`
B. `FormRecognizerClient`; `StartRecognizeContent()`
C. `DocumentAnalysisClient`; `AnalyzeDocumentFromUriAsync()`
D. `DocumentModelAdministrationClient`; `BuildDocumentModelAsync()`

**Answer:** C — The sample: `DocumentAnalysisClient client = new DocumentAnalysisClient(new Uri(endpoint), credential);` followed by `await client.AnalyzeDocumentFromUriAsync(WaitUntil.Completed, modelId, fileUri);` which returns an `AnalyzeDocumentOperation` whose `.Value` is an `AnalyzeResult`.

---

**Q28.** In the module's Python code sample, which method on `DocumentAnalysisClient` is used to analyze a document at a URL using a custom model ID?

A. `analyze_document(model_id, formUrl)`
B. `begin_analyze_document_from_url(model_id, formUrl)`
C. `recognize_custom_forms(model_id, formUrl)`
D. `submit_document_analysis(formUrl, model_id)`

**Answer:** B — `task = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)` followed by `result = task.result()`.

---

**Q29.** What does a composed model do when a document is submitted to it?

A. It merges the output of all component models into one combined field set regardless of document type
B. It classifies the document to determine the most appropriate component model, then returns extraction results from that model
C. It always applies the read model first, then all component models in sequence
D. It requires you to manually specify which component model to use per request

**Answer:** B — "When you submit a document to a composed model, Document Intelligence classifies it to determine the most appropriate component model, and then returns the extraction results from that model."

## Unit 6 — Exercise

**Q30.** In the hands-on exercise for this module, what two model types does the learner use to analyze documents?

A. A prebuilt model and a custom model
B. Only the read and layout models
C. Two different custom neural models
D. A composed model and a custom classifier only

**Answer:** A — "In this exercise, you use the Azure Document Intelligence service to analyze documents using both a prebuilt model and a custom model."

## Unit 7/8 — Module assessment & Summary

**Q31.** Per the module's own knowledge check, which model should you use to extract text and table structure from documents with varying formats, when you don't need to identify specific labeled fields?

A. The read model
B. The layout model
C. The invoice model
D. A custom template model

**Answer:** B — This is a direct restatement of the official module assessment question; the layout model extracts table/structure without requiring a fixed field schema (unlike a trained prebuilt or custom model), and it goes beyond the read model by adding table/structure detection.

---

**Q32.** According to the module's summary, with which TWO other capabilities/services can Azure Document Intelligence be integrated for broader scenarios? (Choose two.)

A. Azure AI Search, for knowledge mining scenarios
B. Generative AI models, for document summarization
C. Azure Databricks, for distributed model training
D. Azure Kubernetes Service, for custom model hosting

**Answer:** A, B — "You can integrate Document Intelligence with other services, such as Azure AI Search for knowledge mining scenarios or generative AI models for document summarization."

## Document Intelligence vs. Content Understanding vs. Vision Read/OCR

**Q33.** [general knowledge — the module content does not directly compare these services, but the EXAM_SKILLS.md "Extract content from documents" bullet explicitly names Content Understanding] You are designing a pipeline that must ingest mixed content — PDFs, product images, and short audio clips — and produce clean, grounded markdown output to feed directly into a RAG-powered agent, using a custom-defined schema across content types. Which Foundry capability is the better fit, and why?

A. Azure AI Document Intelligence, because its custom neural models support unstructured documents
B. Azure Content Understanding, because it is a general multimodal analyzer framework spanning documents, images, audio, and video, supporting custom schemas and markdown output for downstream reasoning
C. Azure AI Vision Read model, because it produces the most accurate OCR bounding boxes
D. A Document Intelligence composed model, because it can classify any content type automatically

**Answer:** B — Content Understanding is the newer, general multimodal analyzer framework (documents + images + audio + video) built around custom schemas and markdown/structured output specifically designed to feed agent and RAG pipelines — this is exactly what EXAM_SKILLS.md's "Produce clean, grounded representations to use with agents and RAG by using Content Understanding" bullet targets. Document Intelligence (A) is document-only and field/table-centric; the Vision Read model (C) is plain OCR with no schema or markdown output; a composed model (D) only routes among Document Intelligence extraction models, not across modalities.

---

**Q34.** [general knowledge] Which scenario is still the stronger fit for Azure AI Document Intelligence rather than Content Understanding?

A. Building an agent tool that must reason over a mix of video transcripts and product photos
B. Extracting a fixed, well-known set of fields (vendor, PO number, totals) from thousands of standard vendor invoices using an out-of-the-box prebuilt model
C. Producing markdown summaries of audio call recordings for a knowledge base
D. Defining a single custom schema that spans images and documents in one analyzer

**Answer:** B — High-volume, standard financial-document field extraction (invoice, receipt, tax, ID, mortgage forms) using the mature, purpose-built `prebuilt-*` model catalog and Document Intelligence Studio remains the more direct, well-established fit for Document Intelligence, versus Content Understanding's broader multimodal/custom-schema/pro-mode positioning.

---

**Q35.** [general knowledge] Which statement correctly distinguishes Document Intelligence's read model from plain Azure AI Vision OCR/Read functionality?

A. They are unrelated services with no functional overlap
B. Document Intelligence's read model is functionally similar to Vision's Read/OCR (text + line/word extraction with bounding boxes and language detection) but is exposed within the Document Intelligence service and forms the text-extraction foundation for its other prebuilt/layout/custom models
C. Azure AI Vision Read produces key-value pairs and tables, while Document Intelligence's read model does not
D. Document Intelligence's read model requires custom training before first use

**Answer:** B — Both perform core OCR (text, bounding boxes, language/handwriting detection), but Document Intelligence's read model is the shared foundation that layout, prebuilt, and custom models build additional structure (tables, KV pairs, fields) on top of; it is available with no training required, consistent with all Document Intelligence document-analysis and prebuilt models.
