# Practice questions — Create a knowledge mining solution with Azure AI Search

Grounded in `content.md`. Questions marked **[General knowledge]** draw on well-established Azure AI Search facts beyond what this specific Learn module states, because the exam skill area (semantic/vector/hybrid search) is only lightly touched by the module content itself.

## Learning objectives / Exam relevance

**Q41.** Which of the following is one of the four stated learning objectives for this module?
A. Implement indexing with Azure AI Search
B. Train a custom neural network for document classification
C. Deploy a Sora 2 video-generation model
D. Configure Pro mode Content Understanding pipelines
**Answer:** A — The four objectives are: implement indexing with Azure AI Search, use AI skills to enrich data in an index, search an index to find relevant information, and persist extracted information in a knowledge store.

**Q42.** What prerequisites does the module state a learner should have?
A. No prerequisites at all; complete beginners are welcome
B. Familiarity with Azure, plus some knowledge of AI concepts
C. Certification in Azure Data Engineering (DP-203) or equivalent
D. Deep hands-on experience with Lucene query syntax
**Answer:** B — Prerequisites listed are familiarity with Azure and some knowledge of AI concepts.

## Unit 1-2 — Introduction / What is Azure AI Search?

**Q1.** A company wants to help employees find information scattered across internal SharePoint sites and file shares. Which Azure AI Search application scenario does this describe?
A. Knowledge mining
B. Enterprise search
C. Retrieval augmented generation
D. Data orchestration
**Answer:** B — Enterprise search is defined in the module as helping employees or customers find information in websites or applications.

**Q2.** Which Azure AI Search application scenario is described as using "vector-based indexes for prompt grounding data" in generative AI applications?
A. Enterprise search portal experience
B. Knowledge mining pipeline output
C. Retrieval augmented generation (RAG)
D. Document cracking stage output
**Answer:** C — RAG is the named scenario that uses vector-based indexes to ground generative AI prompts.

**Q3.** In the knowledge mining scenario, what is the primary purpose of the indexing process according to the module?
A. To replace the source data store with Azure AI Search, eliminating the original store
B. To infer insights and extract granular data assets from documents to support data analytics
C. To translate documents into multiple languages automatically using a built-in skill
D. To provide a managed database for transactional workloads, replacing a relational database
**Answer:** B — Knowledge mining uses indexing to infer insights and extract granular data assets from documents to support data analytics.

**Q4.** Which of the following are core capabilities Azure AI Search provides, per the module? (Choose two.)
A. Index documents and data from a range of sources
B. Store extracted insights in a knowledge store
C. Host relational transactional databases
D. Train custom large language models from scratch
**Answer:** A, B — the module explicitly lists indexing data from a range of sources and storing extracted insights in a knowledge store as core capabilities (alongside using AI skills to enrich index data).

**Q43.** What is the four-step roadmap the module follows to teach Azure AI Search, in order?
A. Query and filter results → core concepts and indexing → AI skills enrichment → knowledge store, reversing the module's actual sequence
B. Core concepts (data sources/indexes) → how indexing/AI skills enrichment works → querying/filtering with full-text search → using the knowledge store to persist enriched data
C. Knowledge store → AI skills → indexing → querying, inverted from the module's real ordering
D. AI skills enrichment → knowledge store → core concepts → querying, an order the module never follows
**Answer:** B — The module roadmap is: 1) core concepts of connecting to data sources and creating indexes, 2) how indexing and AI skill enrichment work, 3) querying/filtering with full-text search, 4) using the knowledge store to persist enriched data.

**Q44.** Which of the following are explicitly listed as insights that Azure AI Search indexes can contain, per Unit 2? (Choose two.)
A. Text inferred or read using OCR from images
B. Entities and key phrases detected through text analytics
C. Real-time video frame timestamps
D. SQL execution plans
**Answer:** A, B — The module lists text inferred/read via OCR from images, and entities/key phrases detected through text analytics, among the insights an index can contain (plus "other derived information based on AI skills").

## Unit 3 — Extract data with an indexer

**Q5.** Which Azure AI Search component is responsible for automating the extraction and indexing of data fields through the enrichment pipeline?
A. The skillset
B. The indexer
C. The knowledge store
D. The semantic configuration
**Answer:** B — The indexer automates extraction and indexing of data fields through the enrichment pipeline, applying document cracking and building the JSON document.

**Q6.** What is the term for the initial step in the enrichment pipeline where an indexer extracts the contents of source documents?
A. Skillset execution
B. Document cracking
C. Field mapping
D. Projection generation
**Answer:** B — Document cracking is the process of extracting the contents of source documents at the start of the enrichment pipeline.

**Q7.** When source documents contain images, the indexer can extract image data into which collection within the constructed JSON document?
A. merged_content
B. extracted_images
C. normalized_images
D. image_index_field
**Answer:** C — Image data is placed in a normalized_images collection (e.g., image0, image1), enabling image-based skills to use it as input.

**Q8.** A skillset includes a skill that combines a document's original text content with OCR-extracted text from images into a single field. What is this type of skill called, and what is a plausible name for its output field, per the module's example?
A. A translation skill; output field "translated_content"
B. A merge skill; output field "merged_content"
C. An entity recognition skill; output field "entities"
D. A projection skill; output field "combined_text"
**Answer:** B — The module describes a merge skill that combines original content with image-extracted text into a merged_content field.

**Q9.** Which two statements correctly describe how fields are mapped from the enrichment pipeline to index fields? (Choose two.)
A. Fields extracted directly from source data can be implicitly mapped to index fields with the same name
B. Output fields from skills are always implicitly mapped based on name matching
C. Fields extracted directly from source data can be explicitly mapped, often to rename them or apply a transform function
D. Skill output fields cannot be mapped to the index under any circumstances
**Answer:** A, C — Source-extracted fields can be mapped implicitly (same name) or explicitly (renamed/transformed); skill output fields, by contrast, must always be explicitly mapped from their hierarchical location to a target index field (making B and D incorrect).

**Q10.** In the enrichment pipeline's hierarchical JSON document, skills are applied to a specific what, enabling a skill to run once per item at a given level (e.g., once per image)?
A. Index
B. Projection
C. Context
D. Facet
**Answer:** C — Skills are applied to a specific context within the document hierarchy, such as running an OCR skill once per image in the normalized_images collection.

## Unit 4 — Enrich extracted data with AI skills

**Q11.** Which of the following are built-in skill capabilities listed in the module for Azure AI Search skillsets? (Choose three.)
A. Extracting text from images (OCR)
B. Detecting and extracting key phrases
C. Training a custom neural network from labeled data
D. Identifying and extracting personally identifiable information (PII)
**Answer:** A, B, D — OCR, key phrase extraction, and PII detection/extraction are all listed built-in skill capabilities. Training a custom neural network is not something built-in skills do; that would require custom logic outside Azure AI Search's built-in offering.

**Q12.** Which two Foundry Tools services are named as the source of built-in skill functionality in Azure AI Search skillsets?
A. Azure Vision and Azure Language
B. Azure Document Intelligence and Azure OpenAI
C. Azure Cognitive Search and Azure Functions
D. Azure Translator and Azure Machine Learning
**Answer:** A — The module names Azure Vision and Azure Language as the Foundry Tools services underlying built-in skills.

**Q13.** By default, using the built-in skills through Azure AI Search's own restricted, bundled Foundry Tools access limits indexing to how many documents?
A. 5 or fewer
B. 20 or fewer
C. 100 or fewer
D. 1,000 or fewer
**Answer:** B — The restricted Azure AI Search resource included in the service is limited to indexing 20 or fewer documents; beyond that you must attach your own Foundry Tools resource.

**Q14.** When attaching your own Foundry Tools resource to use built-in skills at scale, what regional constraint applies?
A. The Foundry Tools resource must be in a different region than the Azure AI Search resource for redundancy
B. The Foundry Tools resource must be in the same region as the Azure AI Search resource
C. There is no regional constraint; any region combination is allowed
D. The Foundry Tools resource must be in the "Global" region specifically
**Answer:** B — The attached Foundry Tools resource must be in the same region as the Azure AI Search resource.

**Q15.** A team needs to extract structured form fields (e.g., invoice number, total) using Azure Document Intelligence within an Azure AI Search enrichment pipeline. Which approach does the module describe for this?
A. Use the built-in Entity Recognition skill directly, since it can be configured to output structured fields
B. Use the built-in Key Phrase Extraction skill directly, since it can be configured to output invoice totals
C. Implement a custom skill, e.g., as an Azure Function, that calls the Azure Document Intelligence model
D. This is not possible within an Azure AI Search skillset, since custom skills only support translation and OCR
**Answer:** C — The module's example of a custom skill is an Azure Function that passes document data to an Azure Document Intelligence model to extract form fields — this is not something a built-in skill does.

**Q16.** Which statement best distinguishes built-in skills from custom skills in Azure AI Search, per the module?
A. Built-in skills require an Azure Function; custom skills do not, since built-in skills execute entirely outside the Search service boundary
B. Built-in skills draw on Foundry Tools functionality (e.g., Azure Vision, Azure Language) already provided by Azure AI Search; custom skills perform custom logic (often as a wrapper around another service such as an Azure Function) to produce field values not covered by built-in capability
C. Custom skills can only be used with the knowledge store, not the index, since projections are their only supported output format
D. Built-in skills and custom skills cannot coexist in the same skillset, since the schema only permits one skill category per build
**Answer:** B — This is the module's core distinction: built-in skills leverage existing Foundry Tools capabilities, while custom skills implement custom logic (commonly wrapping an external service like an Azure Function) for capabilities not otherwise available.

## Unit 5 — Search an index

**Q17.** Which index field attribute allows a field to be included in filter expressions to return only documents matching specified constraints?
A. searchable
B. filterable
C. facetable
D. retrievable
**Answer:** B — filterable fields can be used in filter expressions.

**Q18.** By default, which index field attribute applies to all fields unless explicitly removed?
A. searchable
B. sortable
C. facetable
D. retrievable
**Answer:** D — All fields are retrievable by default unless this attribute is explicitly removed.

**Q19.** Which two field attributes would you need on a "price" field to allow both ordering search results by price and presenting a set of discrete price-range filter options in the UI?
A. sortable and facetable
B. searchable and key
C. filterable and key
D. retrievable and searchable
**Answer:** A — sortable enables ordering results by the field; facetable enables using its values to build UI faceted-filter options.

**Q20.** Azure AI Search full-text queries are based on which query syntax, and what are its two supported variants?
A. SQL syntax; Basic and Advanced
B. Lucene syntax; Simple and Full
C. OData syntax; Simple and Extended
D. Regex syntax; Standard and Extended
**Answer:** B — Full-text search queries use Lucene query syntax, with Simple and Full variants.

**Q21.** A user searches an index for "comfortable hotel" with searchMode=Any versus searchMode=All. What is the difference in results?
A. Any and All return identical results; searchMode only affects sort order, with the same document set returned
B. Any returns documents containing "comfortable", "hotel", or both; All restricts results to documents containing both terms
C. Any returns only exact phrase matches; All returns documents containing either term, reversing the real meaning
D. Any applies stemming; All disables stemming, applying case normalization instead of a matching change
**Answer:** B — searchMode=Any matches any of the terms; searchMode=All requires all terms to be present.

**Q22.** Put the four stages of Azure AI Search query processing in the correct order.
A. Scoring → Query parsing → Lexical analysis → Document retrieval
B. Query parsing → Lexical analysis → Document retrieval → Scoring
C. Lexical analysis → Query parsing → Scoring → Document retrieval
D. Document retrieval → Query parsing → Scoring → Lexical analysis
**Answer:** B — The order is query parsing, lexical analysis, document retrieval, then scoring (a relevance score based on TF/IDF).

**Q23.** During lexical analysis, which of the following occur? (Choose two.)
A. Text is converted to lower case and stopwords such as "the" and "a" are removed
B. Words are converted to their root form (e.g., "comfortable" simplified to "comfort")
C. A relevance score is computed using TF/IDF
D. The search expression is reconstructed as a tree of subqueries
**Answer:** A, B — Lexical analysis handles case normalization, stopword removal, and stemming to root form. C describes the scoring stage and D describes query parsing.

**Q24.** Which query subquery type would match the search term "air*", matching "airway", "air-conditioning", and "airport"?
A. Term query
B. Phrase query
C. Prefix query
D. Facet query
**Answer:** C — A prefix query finds terms with a specified prefix, such as "air*".

**Q25.** Which OData query parameter would you use with queryType=Full to filter results to documents where the author field equals 'Reviewer'?
A. searchMode=Reviewer author
B. $filter=author eq 'Reviewer'
C. $orderby=author eq 'Reviewer'
D. facet=author eq 'Reviewer'
**Answer:** B — The $filter parameter with an OData expression like `author eq 'Reviewer'` filters results in Full syntax.

**Q26.** Is the following statement true or false: OData $filter expressions in Azure AI Search are case-insensitive.
A. True
B. False
**Answer:** B — False. The module explicitly states OData $filter expressions are case-sensitive.

**Q27.** To sort query results so the most recently modified documents appear first, which parameter and value would you use?
A. $filter=last_modified desc
B. searchMode=last_modified desc
C. $orderby=last_modified desc
D. facet=last_modified desc
**Answer:** C — $orderby with a sortable field and "desc" direction controls result ordering; by default results sort by relevance score.

**Q28.** [General knowledge] Which algorithm does Azure AI Search use by default to rank results in keyword (full-text) search, refining the module's described TF/IDF-based relevance scoring?
A. HNSW
B. BM25
C. Reciprocal Rank Fusion
D. Cosine similarity
**Answer:** B — BM25 is the ranking algorithm Azure AI Search uses for full-text/keyword relevance scoring (a refinement of classic TF/IDF). This is general Azure AI Search knowledge, as the module itself only describes TF/IDF-style scoring without naming BM25 explicitly.

**Q29.** [General knowledge] Which Azure AI Search capability adds a secondary reranking pass over initial keyword search results, using a semantic configuration to reorder the top matches and can generate answer captions with highlighted passages?
A. Vector search alone, without any reranking step applied
B. Semantic search (semantic ranker)
C. Faceted search UI component
D. Hybrid search alone, without a secondary reranking pass
**Answer:** B — Semantic search applies a semantic ranker on top of initial results using a semantic configuration defined on the index. This is general knowledge supplementing the module, which does not describe semantic search.

**Q30.** [General knowledge] An index field storing document embeddings for similarity search, typically searched using an approximate nearest-neighbor algorithm such as HNSW, is called what kind of field in Azure AI Search?
A. A facetable field
B. A vector field
C. A retrievable field
D. A key field
**Answer:** B — Vector fields store embeddings and are searched using algorithms such as HNSW (Hierarchical Navigable Small World) for approximate nearest neighbor search. General knowledge, not covered by this module's text.

**Q31.** [General knowledge] Which technique does Azure AI Search commonly use to combine and rerank result sets from keyword search and vector search in a hybrid query?
A. Term frequency/inverse document frequency (TF/IDF)
B. Reciprocal Rank Fusion (RRF)
C. Document cracking step
D. Lexical analysis phase
**Answer:** B — Reciprocal Rank Fusion (RRF) is used to merge and rerank BM25 keyword results with vector similarity results in hybrid search. General knowledge, not covered by this module's text.

**Q32.** [General knowledge] Which distinction correctly separates vector search from hybrid search in Azure AI Search?
A. Vector search only works with text fields; hybrid search only works with numeric fields, per their index schema
B. Vector search matches documents purely by embedding similarity; hybrid search combines keyword (BM25) search with vector search in a single query, typically merged via RRF
C. Vector search and hybrid search are the same feature with different names, issuing an identical query
D. Vector search requires a semantic configuration; hybrid search does not, reversing which feature actually needs one
**Answer:** B — Vector search alone ranks by embedding similarity; hybrid search issues both a keyword and a vector query and fuses the ranked lists (commonly via RRF). Semantic configuration is associated with semantic ranking, not a prerequisite of vector search itself.

**Q45.** Which request would retrieve the set of possible values for a facetable `author` field, ready to present as UI filter options?
A. `search=* & facet=author`
B. `search=author & $filter=facet eq true`
C. `$orderby=author & search=*`
D. `search=* & searchMode=facet`
**Answer:** A — `search=*` combined with `facet=author` retrieves the distinct values for the facetable `author` field; a selected value is then used in a subsequent `$filter=author eq 'selected-facet-value-here'` query.

**Q46.** [General knowledge] Which client classes, part of the Azure.Search.Documents SDK family (not named in this module's own text but standard Azure AI Search knowledge), are used respectively to query/index documents, manage index schema, and manage indexers/data sources/skillsets?
A. `SearchClient`, `SearchIndexClient`, `SearchIndexerClient`
B. `DocumentClient`, `IndexClient`, `SkillsetClient`
C. `AzureSearchClient`, `SchemaClient`, `PipelineClient`
D. `QueryClient`, `IndexManagerClient`, `EnrichmentClient`
**Answer:** A — `SearchClient` handles querying/indexing documents, `SearchIndexClient` manages the index schema, and `SearchIndexerClient` manages indexers, data sources, and skillsets — standard Azure.Search.Documents SDK surface, flagged as general knowledge supplementing this module.

## Unit 6 — Persist extracted information in a knowledge store

**Q33.** What is the term for the enriched-data outputs (JSON objects, tables, or image files) that Azure AI Search generates and persists into a knowledge store?
A. Skillsets
B. Projections
C. Indexers
D. Facets list
**Answer:** B — Projections are the JSON objects, tables, or image file outputs of the enrichment pipeline persisted to the knowledge store.

**Q34.** A data analytics team wants the enriched fields from an Azure AI Search indexing pipeline exposed as a normalized relational schema for reporting. Which projection type should they use?
A. Object projection
B. File projection
C. Table projection
D. Facet projection
**Answer:** C — Table projections normalize index records into a relational schema of tables for analysis and reporting.

**Q35.** Which of the following are valid reasons given in the module for using a knowledge store rather than relying solely on the index? (Choose two.)
A. To export enriched records as JSON files for an ETL orchestration process
B. To save embedded images extracted during indexing as files
C. To bypass the need for a data source entirely
D. To eliminate the need for a skillset
**Answer:** A, B — The module cites exporting JSON for ETL integration and saving extracted images as files as scenarios motivating the knowledge store; it does not eliminate the need for a data source or skillset (the knowledge store is defined within the skillset).

**Q36.** Where is the knowledge store defined within an Azure AI Search solution?
A. Within the data source definition, alongside the connection string and container name
B. Within the skillset that encapsulates the enrichment pipeline
C. Within the index schema definition, next to attributes like searchable and sortable
D. Within the search client application code, instantiated alongside the SearchClient
**Answer:** B — The knowledge store is defined in the skillset that encapsulates the enrichment pipeline; projections are generated and persisted there when the indexer runs.

**Q47.** Knowledge store projections (JSON objects, tables, image files) are ultimately persisted to which underlying Azure storage service, per the linked concept documentation referenced by the module?
A. Azure Cosmos DB exclusively, requiring a separate migration step for table projections
B. An Azure Storage account — Blob containers for object/file projections, Table Storage for table projections
C. Azure SQL Database exclusively, requiring a linked-server configuration for JSON projections
D. Azure Data Lake Storage Gen1 only, a deprecated service no longer provisioned
**Answer:** B — Per the module's reference note, knowledge store projections are persisted to an Azure Storage account: Blob containers for object/file projections and Table Storage for table projections.

## Unit 7-9 — Exercise, Assessment, Summary

**Q37.** In the module's own knowledge-check assessment, which component is described as "scheduled to extract and enrich data to populate an index"?
A. Projection
B. Query
C. Indexer
D. Semantic configuration
**Answer:** C — Indexer, consistent with Unit 3's definition of the indexer as the automation component of the enrichment pipeline.

**Q38.** Per the module's assessment, which service supports built-in AI skills in Azure AI Search?
A. Azure Functions
B. Foundry Tools
C. Azure Cosmos DB
D. Azure Data Factory
**Answer:** B — Foundry Tools (encompassing Azure Vision and Azure Language) is the named source of built-in skills.

**Q39.** Which projection type, per the module's assessment, results in a relational data schema for extracted fields?
A. File
B. Object
C. Table
D. Vector
**Answer:** C — Table projections produce a relational schema; object projections produce JSON objects and file projections produce image/other files.

**Q40.** Which Azure resource type does the hands-on exercise in this module require administrative access to in order to complete the lab?
A. An Azure DevOps organization
B. An Azure subscription
C. A GitHub Enterprise account
D. A Microsoft 365 tenant
**Answer:** B — The exercise requires an Azure subscription in which the learner has administrative access.

**Q48.** Approximately how long is the hands-on exercise "Create a knowledge mining solution" estimated to take?
A. 10 minutes
B. 40 minutes
C. 90 minutes
D. 3 hours
**Answer:** B — The exercise is listed as approximately 40 minutes.

---

## Scenario-based questions

**Q49.** *(Scenario)* You configure an indexer over a blob container of scanned PDFs containing embedded images. You want: (1) image text extracted via OCR, (2) that OCR text merged with the original document content into one searchable field, (3) the detected language stored, and (4) all of this queryable and orderable by last-modified date in the resulting index. Which sequence of concepts applies, and which two index field attributes are needed for the last requirement?
A. document cracking → normalized_images → OCR skill (context = each image) → merge skill → language detection skill → explicit field mapping into the index; `searchable` and `sortable` on the relevant fields
B. document cracking → OCR skill → normalized_images → merge skill; no field mapping is needed since Azure AI Search infers every mapping automatically
C. skillset → knowledge store → indexer → projections; `filterable` and `facetable` only, omitting the ordering requirement
D. normalized_images → merge skill → OCR skill → document cracking; `key` and `retrievable` only, reversing the pipeline order
**Answer:** A — The pipeline is: document cracking extracts content, images go into `normalized_images`, an OCR skill runs per-image (context = each image) to extract `Text`, a merge skill combines original content + OCR text into `merged_content`, a language detection skill adds a `language` field — skill outputs must be explicitly mapped to index fields (unlike source fields, which can map implicitly) — and ordering by last-modified date requires the field to be `sortable` (with `searchable` needed if it must also be full-text queryable).

**Q50.** *(Scenario)* Your organization needs to extract invoice line-item fields using Azure Document Intelligence as part of an Azure AI Search enrichment pipeline processing 50,000 documents per month, with the Foundry Tools resource required to be co-located with the Search service. What two things must you do, combining the built-in/custom skill distinction with the resource requirement?
A. Use the built-in Key Phrase Extraction skill; no additional resource attachment is needed, since it can output structured invoice line items
B. Implement a custom skill (e.g., an Azure Function) that calls Azure Document Intelligence, since this isn't a built-in capability; and attach a Foundry Tools resource in your Azure subscription in the same region as your Azure AI Search resource, since the free 20-document allotment is far too small for 50,000 documents/month
C. Use the built-in OCR skill alone; region does not matter for skill execution, since OCR always routes to the nearest endpoint
D. Use a custom skill, but the Foundry Tools resource can be in any region since custom skills bypass regional requirements entirely
**Answer:** B — Structured field extraction via Document Intelligence requires a custom skill (built-in skills only cover OCR, language detection, entity/key-phrase extraction, PII, translation, and image captioning/tagging — not Document Intelligence-style field extraction); and at 50,000 documents/month you must attach your own Foundry Tools resource, which must be in the same region as the Azure AI Search resource, since the bundled/restricted allotment is capped at 20 documents.

**Q51.** *(Scenario)* A product manager describes three separate initiatives: (1) letting employees search internal wikis and SharePoint, (2) grounding a customer-support chatbot's answers using vector-based retrieval over product manuals, and (3) extracting granular structured data assets from thousands of contracts to feed a BI dashboard. Which Azure AI Search use case does each map to?
A. (1) Knowledge mining, (2) Enterprise search, (3) RAG — reversing all three of the actual mappings
B. (1) Enterprise search, (2) Retrieval augmented generation (RAG), (3) Knowledge mining
C. All three are examples of RAG, since RAG subsumes the other two use cases
D. (1) RAG, (2) Knowledge mining, (3) Enterprise search — a full rotation of the correct mapping
**Answer:** B — Enterprise search helps employees/customers find information in websites/applications (1); RAG supports generative AI apps using vector-based indexes for prompt grounding (2); knowledge mining infers insights and extracts granular data assets from documents to support data analytics (3) — exactly the module's three named use cases.

**Q52.** *(Scenario)* After running your enrichment pipeline, you want the enriched data available in three additional forms: raw JSON exported for an ETL process, a normalized relational schema for BI reporting, and the extracted embedded images saved as standalone files. Where do you configure this, what is the mechanism called, and which underlying Azure storage services back each output form?
A. Configure a knowledge store in the skillset; JSON/image outputs use "object"/"file" projections backed by Blob containers, and the relational output uses a "table" projection backed by Table Storage
B. Configure a second indexer pointed at the same data source; no projections are involved, duplicating the original index data into a second copy
C. Configure `$orderby` and `facet` parameters on search queries; storage is handled automatically by the index itself, with no distinction between output forms
D. Configure a custom skill that writes directly to Cosmos DB; knowledge stores are not needed, despite Cosmos DB never appearing in the module
**Answer:** A — The knowledge store, defined within the skillset encapsulating the enrichment pipeline, generates JSON object, table, and image file projections when the indexer runs; per the module's linked reference, object/file projections are backed by Blob containers and table projections by Table Storage within an Azure Storage account.
