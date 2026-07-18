# Practice questions — Create a knowledge mining solution with Azure AI Search

Grounded in `content.md`. Questions marked **[General knowledge]** draw on well-established Azure AI Search facts beyond what this specific Learn module states, because the exam skill area (semantic/vector/hybrid search) is only lightly touched by the module content itself.

## Unit 1-2 — Introduction / What is Azure AI Search?

**Q1.** A company wants to help employees find information scattered across internal SharePoint sites and file shares. Which Azure AI Search application scenario does this describe?
A. Knowledge mining
B. Enterprise search
C. Retrieval augmented generation
D. Data orchestration
**Answer:** B — Enterprise search is defined in the module as helping employees or customers find information in websites or applications.

**Q2.** Which Azure AI Search application scenario is described as using "vector-based indexes for prompt grounding data" in generative AI applications?
A. Enterprise search
B. Knowledge mining
C. Retrieval augmented generation (RAG)
D. Document cracking
**Answer:** C — RAG is the named scenario that uses vector-based indexes to ground generative AI prompts.

**Q3.** In the knowledge mining scenario, what is the primary purpose of the indexing process according to the module?
A. To replace the source data store with Azure AI Search
B. To infer insights and extract granular data assets from documents to support data analytics
C. To translate documents into multiple languages automatically
D. To provide a managed database for transactional workloads
**Answer:** B — Knowledge mining uses indexing to infer insights and extract granular data assets from documents to support data analytics.

**Q4.** Which of the following are core capabilities Azure AI Search provides, per the module? (Choose two.)
A. Index documents and data from a range of sources
B. Store extracted insights in a knowledge store
C. Host relational transactional databases
D. Train custom large language models from scratch
**Answer:** A, B — the module explicitly lists indexing data from a range of sources and storing extracted insights in a knowledge store as core capabilities (alongside using AI skills to enrich index data).

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
D. image_index
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
C. There is no regional constraint; any region is allowed
D. The Foundry Tools resource must be in the "Global" region specifically
**Answer:** B — The attached Foundry Tools resource must be in the same region as the Azure AI Search resource.

**Q15.** A team needs to extract structured form fields (e.g., invoice number, total) using Azure Document Intelligence within an Azure AI Search enrichment pipeline. Which approach does the module describe for this?
A. Use the built-in Entity Recognition skill directly
B. Use the built-in Key Phrase Extraction skill directly
C. Implement a custom skill, e.g., as an Azure Function, that calls the Azure Document Intelligence model
D. This is not possible within an Azure AI Search skillset
**Answer:** C — The module's example of a custom skill is an Azure Function that passes document data to an Azure Document Intelligence model to extract form fields — this is not something a built-in skill does.

**Q16.** Which statement best distinguishes built-in skills from custom skills in Azure AI Search, per the module?
A. Built-in skills require an Azure Function; custom skills do not
B. Built-in skills draw on Foundry Tools functionality (e.g., Azure Vision, Azure Language) already provided by Azure AI Search; custom skills perform custom logic (often as a wrapper around another service such as an Azure Function) to produce field values not covered by built-in capability
C. Custom skills can only be used with the knowledge store, not the index
D. Built-in skills and custom skills cannot coexist in the same skillset
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
A. Any and All return identical results; searchMode only affects sort order
B. Any returns documents containing "comfortable", "hotel", or both; All restricts results to documents containing both terms
C. Any returns only exact phrase matches; All returns documents containing either term
D. Any applies stemming; All disables stemming
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
A. searchMode=Reviewer
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

**Q28. [General knowledge]** Which algorithm does Azure AI Search use by default to rank results in keyword (full-text) search, refining the module's described TF/IDF-based relevance scoring?
A. HNSW
B. BM25
C. Reciprocal Rank Fusion
D. Cosine similarity
**Answer:** B — BM25 is the ranking algorithm Azure AI Search uses for full-text/keyword relevance scoring (a refinement of classic TF/IDF). This is general Azure AI Search knowledge, as the module itself only describes TF/IDF-style scoring without naming BM25 explicitly.

**Q29. [General knowledge]** Which Azure AI Search capability adds a secondary reranking pass over initial keyword search results, using a semantic configuration to reorder the top matches and can generate answer captions with highlighted passages?
A. Vector search
B. Semantic search (semantic ranker)
C. Faceted search
D. Hybrid search
**Answer:** B — Semantic search applies a semantic ranker on top of initial results using a semantic configuration defined on the index. This is general knowledge supplementing the module, which does not describe semantic search.

**Q30. [General knowledge]** An index field storing document embeddings for similarity search, typically searched using an approximate nearest-neighbor algorithm such as HNSW, is called what kind of field in Azure AI Search?
A. A facetable field
B. A vector field
C. A retrievable field
D. A key field
**Answer:** B — Vector fields store embeddings and are searched using algorithms such as HNSW (Hierarchical Navigable Small World) for approximate nearest neighbor search. General knowledge, not covered by this module's text.

**Q31. [General knowledge]** Which technique does Azure AI Search commonly use to combine and rerank result sets from keyword search and vector search in a hybrid query?
A. Term frequency/inverse document frequency (TF/IDF)
B. Reciprocal Rank Fusion (RRF)
C. Document cracking
D. Lexical analysis
**Answer:** B — Reciprocal Rank Fusion (RRF) is used to merge and rerank BM25 keyword results with vector similarity results in hybrid search. General knowledge, not covered by this module's text.

**Q32. [General knowledge]** Which distinction correctly separates vector search from hybrid search in Azure AI Search?
A. Vector search only works with text fields; hybrid search only works with numeric fields
B. Vector search matches documents purely by embedding similarity; hybrid search combines keyword (BM25) search with vector search in a single query, typically merged via RRF
C. Vector search and hybrid search are the same feature with different names
D. Vector search requires a semantic configuration; hybrid search does not
**Answer:** B — Vector search alone ranks by embedding similarity; hybrid search issues both a keyword and a vector query and fuses the ranked lists (commonly via RRF). Semantic configuration is associated with semantic ranking, not a prerequisite of vector search itself.

## Unit 6 — Persist extracted information in a knowledge store

**Q33.** What is the term for the enriched-data outputs (JSON objects, tables, or image files) that Azure AI Search generates and persists into a knowledge store?
A. Skillsets
B. Projections
C. Indexers
D. Facets
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
A. Within the data source definition
B. Within the skillset that encapsulates the enrichment pipeline
C. Within the index schema definition
D. Within the search client application code
**Answer:** B — The knowledge store is defined in the skillset that encapsulates the enrichment pipeline; projections are generated and persisted there when the indexer runs.

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
