# Create a knowledge mining solution with Azure AI Search

Source: https://learn.microsoft.com/en-us/training/modules/ai-knowldge-mining/

(Note: the URL slug is spelled "knowldge" — a known typo in the Microsoft Learn URL, not a transcription error here. The user-facing module title used in the learning path listing is sometimes rendered as "Implement knowledge mining with Azure AI Search"; the actual Microsoft Learn page title is "Create a knowledge mining solution with Azure AI Search". Both refer to the same module/uid `learn.wwl.ai-knowledge-mining`.)

Level: Intermediate | Roles: AI Engineer, Developer | Product: Foundry Tools | 9 Units

## Learning objectives

After completing this module, you'll be able to:

- Implement indexing with Azure AI Search
- Use AI skills to enrich data in an index
- Search an index to find relevant information
- Persist extracted information in a knowledge store

Prerequisites: familiarity with Azure; some knowledge of AI concepts.

## Exam relevance

Maps primarily to **Implement information extraction solutions (10-15%)** → "Build retrieval and grounding pipelines":
- Ingest and index content, such as documents, images, audio, and video → Unit 3 (indexers, data sources, document cracking).
- Implement enrichment by using custom or built-in skills for text, images, and layout → Unit 4 (built-in skills, custom skills).
- Configure RAG ingestion flow, including documents and using OCR → Units 3-4 (OCR skill, normalized_images, merge skill).
- Configure semantic search, hybrid search, and vector search for grounding → **NOT covered in depth by this module** (see note below). Unit 5 covers only classic full-text (Lucene/BM25-style) search, filtering, facets, and sorting — no semantic ranker, vector fields, or hybrid query syntax appear in the module's source text. Supplementary notes are added at the end of Unit 5 for exam completeness, clearly flagged as outside this module's content.
- Connect retrieval pipelines directly to workflows and agent tools → touched on in Unit 2 (RAG use case), not elaborated with code.

Also maps to **Plan and manage an Azure AI solution (25-30%)**:
- "Choose an appropriate method for retrieval and indexing" → Unit 2 (enterprise search vs. RAG vs. knowledge mining use cases for Azure AI Search).
- "Choose appropriate memory, tool, and knowledge integration services for agent solutions" → Unit 2 (Azure AI Search as grounding/vector index source for RAG).
- "Monitor data ingestion quality, search index health, and relevance performance" → Unit 5 (relevance scoring/TF-IDF), Unit 3 (indexer/enrichment pipeline as the ingestion mechanism to monitor).

Secondary relevance to **Implement text analysis solutions** (Unit 4's Azure Language-based skills: language detection, key phrase extraction, entity recognition, PII detection, translation) and **Implement computer vision solutions** (Unit 4's Azure Vision-based skills: OCR, image captioning/tagging).

---

## Unit 1: Introduction

Azure AI Search is described as "a powerful cloud-based service that enables you to extract, enrich, and explore information from a wide variety of data sources."

The module roadmap:
1. Core concepts of Azure AI Search — connecting to data sources, creating indexes.
2. How the indexing process works, and how AI skills enrich data (language detection, key phrase extraction, image analysis are given as examples).
3. Querying and filtering results using full-text search.
4. Using the knowledge store to persist enriched data for further analysis and integration with other systems.

(Module is offered in both video and text format; text format is noted to contain more detail than the video.)

## Unit 2: What is Azure AI Search?

Azure AI Search provides a cloud-based solution for **indexing and querying** a wide range of data sources, for creating comprehensive and high-scale search solutions. It provides infrastructure and tools to build search solutions that extract data from **structured, semi-structured, and non-structured (unstructured)** documents and other data sources.

Core capabilities:
- Index documents and data from a range of sources.
- Use AI skills to enrich index data.
- Store extracted insights in a **knowledge store** for analysis and integration.

Azure AI Search indexes contain insights extracted from data, including:
- Text inferred or read using **OCR** from images.
- **Entities** and **key phrases** detected through text analytics.
- Other derived information based on AI skills integrated into the indexing process.

### Three named applications/use cases for Azure AI Search (exam-relevant distinctions)

1. **Enterprise search** — helping employees or customers find information in websites or applications.
2. **Retrieval augmented generation (RAG)** — supporting generative AI applications "by using vector-based indexes for prompt grounding data." (This is the module's only mention of vector-based indexes — no further elaboration on vector search mechanics is given in this module.)
3. **Knowledge mining** — using the indexing process "to infer insights and extract granular data assets from documents to support data analytics." This module's focus is explicitly stated to be Azure AI Search in **knowledge mining scenarios**.

## Unit 3: Extract data with an indexer

Core concept: an **index** is created and updated by an **indexer**. The index contains your searchable content.

### Indexing pipeline flow
Data source (e.g., an Azure blob storage container full of documents, a database, or another store) → **Indexer** → **enrichment pipeline** → populated **index**.

The indexer automates extraction and indexing of data **fields** through the enrichment pipeline:
1. **Document cracking** — extracts the contents of the source documents.
2. Incremental steps build a hierarchical **JSON-based document** with the fields required by the index definition.

The result is a populated index that can be queried to return specified fields from documents matching query criteria.

### How documents are constructed during indexing

The enrichment pipeline iteratively builds a JSON document per indexed entity, combining metadata from the data source with enriched fields extracted/generated by **skills**.

Initial document structure (metadata mapped directly from source):
```
document
├── metadata_storage_name
├── metadata_author
└── content
```

When source documents contain images, the indexer can be configured to extract image data into a **normalized_images** collection:
```
document
├── metadata_storage_name
├── metadata_author
├── content
└── normalized_images
    ├── image0
    └── image1
```
Normalizing image data this way lets you use the image collection as input for skills that extract information from image data.

Each skill adds fields to the document. Example: a **language detection** skill stores output in a `language` field:
```
document
├── metadata_storage_name
├── metadata_author
├── content
├── normalized_images
│   ├── image0
│   └── image1
└── language
```

Documents are structured **hierarchically**, and skills are applied to a specific **context** within that hierarchy — enabling a skill to run once per item at a particular level. Example: an **OCR** skill run for each image in `normalized_images` to extract text:
```
document
├── metadata_storage_name
├── metadata_author
├── content
├── normalized_images
│   ├── image0
│   │   └── Text
│   └── image1
│       └── Text
└── language
```

Output fields from one skill can feed later skills. Example: a **merge** skill combines original text content with text extracted from images into a new `merged_content` field containing all text (including image text):
```
document
├── metadata_storage_name
├── metadata_author
├── content
├── normalized_images
│   ├── image0
│   │   └── Text
│   └── image1
│       └── Text
├── language
└── merged_content
```

### Field mapping to the index (two mechanisms)

1. **Fields extracted directly from source data** are mapped to index fields either:
   - **Implicitly** — automatically mapped to index fields with the same name, OR
   - **Explicitly** — a mapping is defined to match a source field to an index field, often to rename the field or apply a function to the value during mapping.
2. **Output fields from skills in the skillset** are **explicitly mapped** from their hierarchical location in the enriched document to the target index field.

## Unit 4: Enrich extracted data with AI skills

The enrichment pipeline orchestrated by an indexer uses a **skillset** of AI skills to create AI-enriched fields. The indexer applies each skill **in order**, refining the index document at each step.

### Built-in skills

Azure AI Search provides a collection of **built-in skills** for a skillset. Built-in skills draw on functionality from **Foundry Tools** (the module's term for what is elsewhere called Azure AI services), specifically naming **Azure Vision** and **Azure Language**, enabling enrichments such as:

- Detecting the language that text is written in. (→ Language detection)
- Detecting and extracting places, locations, and other **entities** in text. (→ Entity Recognition)
- Determining and extracting **key phrases** within a body of text. (→ Key Phrase Extraction)
- **Translating** text.
- Identifying and extracting (or removing) **personally identifiable information (PII)** within text.
- Extracting text from images. (→ **OCR**)
- Generating **captions and tags** to describe images. (→ Image Analysis / captioning)

**Resource requirement to use built-in skills:** the indexer must have access to a **Foundry Tools resource**. Two options given:
- Use a **restricted Azure AI Search resource** included in Azure AI Search itself — this is **limited to indexing 20 or fewer documents**.
- Attach a **Foundry Tools resource in your Azure subscription** — this resource **must be in the same region** as your Azure AI Search resource.

(Exam-relevant limit: the free/bundled cognitive skills allotment via the search service's own key is capped at 20 documents; beyond that, or for production scale, you must attach your own Foundry Tools/Azure AI services multi-service resource in the same region.)

### Custom skills

**Custom skills** extend enrichment beyond built-in capability: they perform custom logic on input data from the index document to return new field values incorporated into the index. Custom skills are often described as "wrappers" around services purpose-built to extract data from documents.

Example given: implement a custom skill as an **Azure Function**, using it to pass data from the index document to an **Azure Document Intelligence** model, which extracts fields from a form.

Reference link cited in the module: "Add a custom skill to an Azure AI Search enrichment pipeline" — `/en-us/azure/search/cognitive-search-custom-skill-interface`.

(No code sample for a custom skill web API contract was present on this page — the module points to external documentation for the exact custom skill interface.)

## Unit 5: Search an index

The index is the searchable result of the indexing process: a collection of **JSON documents** with fields containing values extracted during indexing. Client applications query the index to retrieve, filter, and sort information.

### Index field attributes

Each index field can be configured with the following attributes:

- **key** — fields that define a unique key for index records.
- **searchable** — fields that can be queried using full-text search.
- **filterable** — fields that can be included in filter expressions to return only documents matching specified constraints.
- **sortable** — fields that can be used to order results.
- **facetable** — fields that can be used to determine values for **facets** (UI elements used to filter results based on a list of known field values).
- **retrievable** — fields that can be included in search results. **By default, all fields are retrievable unless this attribute is explicitly removed.**

(Note: this module's list does not separately enumerate a "vector" field type or vector-search-specific attributes such as `dimensions` or `vectorSearchProfile` — see the flagged supplementary note below.)

### Full-text search

Full-text search parses text-based document contents to find query terms. Azure AI Search full-text queries are based on the **Lucene** query syntax, which supports two variants:

- **Simple** — an intuitive syntax for basic searches matching literal query terms.
- **Full** — an extended syntax supporting complex filtering, regular expressions, and more sophisticated queries.

### Common query parameters

- **search** — the search expression containing terms to find.
- **queryType** — which Lucene syntax to evaluate (`Simple` or `Full`).
- **searchFields** — the index fields to search.
- **select** — the fields to include in results.
- **searchMode** — criteria for combining multiple search terms:
  - `Any` — returns documents containing any of the terms (e.g., for "comfortable hotel": documents with "comfortable", "hotel", or both).
  - `All` — restricts results to documents containing **all** terms.

### Query processing — four stages

1. **Query parsing** — the search expression is evaluated and reconstructed as a tree of subqueries. Types of subqueries:
   - **Term queries** — specific individual words (e.g., *hotel*).
   - **Phrase queries** — multi-term phrases in quotation marks (e.g., *"free parking"*).
   - **Prefix queries** — terms with a specified prefix (e.g., *air\**, matching *airway*, *air-conditioning*, *airport*).
2. **Lexical analysis** — query terms analyzed/refined by linguistic rules: text lowercased, nonessential **stopwords** (e.g., "the", "a", "is") removed, words reduced to **root form** (e.g., "comfortable" → "comfort"), composite words split into constituent terms.
3. **Document retrieval** — query terms matched against indexed terms; the set of matching documents is identified.
4. **Scoring** — a relevance score is assigned to each result based on a **term frequency/inverse document frequency (TF/IDF)** calculation.

(Reference cited: "Query types and composition in Azure AI Search" — `/en-us/azure/search/search-query-overview`.)

### Filtering results

Two ways to apply filters:
- Include filter criteria directly in a **simple** `search` expression.
- Provide an **OData filter expression** as a `$filter` parameter with a **full** syntax search expression.

Filters can only be applied to **filterable** fields.

Example — find documents containing "London" with `author` = "Reviewer":

Simple syntax:
```
search=London+author='Reviewer'
queryType=Simple
```

Full syntax with OData filter:
```
search=London
$filter=author eq 'Reviewer'
queryType=Full
```

**Important:** OData `$filter` expressions are **case-sensitive**.

### Filtering with facets

**Facets** present users with filtering criteria based on field values in a result set — work best when a field has a small number of discrete values displayable as links/options. Facets require **facetable** fields.

Retrieve possible values for a facetable field (e.g., `author`):
```
search=*
facet=author
```

Use a selected facet value to filter in a subsequent query:
```
search=*
$filter=author eq 'selected-facet-value-here'
```

### Sorting results

By default, results are sorted by the relevancy score (highest first). Override with an OData **`$orderby`** parameter specifying one or more **sortable** fields and a sort direction (`asc` or `desc`).

Example — most recently modified documents first:
```
search=*
$orderby=last_modified desc
```

(Reference cited: "Filters in Azure AI Search" — `/en-us/azure/search/search-filters`.)

### ⚠ Supplementary note (NOT from this module — flagged for exam completeness)

This module's Unit 5 covers only classic Lucene/BM25-style full-text search, OData filtering, facets, and sorting. It does **not** describe semantic search, vector search, or hybrid search mechanics, even though the exam skill area "Configure semantic search, hybrid search, and vector search for grounding" is explicitly tested. Well-established general Azure AI Search knowledge relevant to that skill (not sourced from this module — verify against current Azure AI Search docs when studying):

- **Keyword/full-text search**: ranks results using a **BM25** relevance algorithm (a refinement of the TF/IDF-style scoring this module describes).
- **Semantic search**: adds a secondary ranking pass ("L2 reranker" / **semantic ranker**) over the initial BM25 result set, using a **semantic configuration** on the index (defines title, content, and keyword fields to prioritize) to reorder the top results by semantic relevance and can generate **captions**/answers with highlighted relevant passages.
- **Vector search**: indexes store **vector fields** (embeddings) alongside/instead of text; similarity search uses an approximate nearest neighbor algorithm, typically **HNSW** (Hierarchical Navigable Small World), or exhaustive KNN; a **vectorizer** can be configured on the index to automatically convert text queries to vectors at query time using an embedding model/deployment.
- **Hybrid search**: combines keyword (BM25) search and vector search in a single query, merging result sets typically via **Reciprocal Rank Fusion (RRF)**; can optionally add semantic reranking on top ("hybrid + semantic ranking").
- Relevant SDK/API surface (not named in this module): **`SearchClient`** (query/index documents), **`SearchIndexClient`** (manage index schema), **`SearchIndexerClient`** (manage indexers, data sources, skillsets) in the Azure.Search.Documents SDKs; REST API base pattern `https://<search-service-name>.search.windows.net`.

Treat the bullet list above as background knowledge, not as content verified against this specific Learn module page.

## Unit 6: Persist extracted information in a knowledge store

While the index is the primary output of indexing, the enriched data may be useful in other forms. Stated scenarios:

- Since the index is a collection of JSON objects (one per indexed record), it may be useful to **export the objects as JSON files** for integration into a data orchestration process for **extract, transform, and load (ETL)** operations.
- You may want to **normalize the index records into a relational schema of tables** for analysis and reporting.
- Having extracted embedded images from documents during indexing, you may want to **save those images as files**.

Azure AI Search supports these scenarios via a **knowledge store**, defined in the skillset that encapsulates the enrichment pipeline. The knowledge store consists of **projections** of the enriched data, which can be:
- **JSON objects**
- **Tables**
- **Image files**

When an indexer runs the pipeline to create/update an index, the projections are generated and persisted in the knowledge store.

(Reference cited: "Knowledge store in Azure AI Search" — `/en-us/azure/search/knowledge-store-concept-intro`. The module does not state the underlying storage requirement explicitly on this page, but per the linked concept, knowledge store projections are persisted to an **Azure Storage account** — Blob containers for object/file projections, Table Storage for table projections.)

## Unit 7: Exercise — Create a knowledge mining solution

Hands-on lab (~40 minutes) using Azure AI Search to extract and enrich information from documents into a searchable index and a knowledge store. Requires an Azure subscription with administrative access. Delivered via an external lab launch link (go.microsoft.com fwlink), not inline content — no additional technical detail is present on the module page itself.

## Unit 8: Module assessment

Three knowledge-check questions presented on the Learn platform (verbatim):

1. "Which component of an Azure AI Search solution is scheduled to extract and enrich data to populate an index?" — options: Indexer / Projection / Query. (Correct: **Indexer** — matches Unit 3's definition.)
2. "Which service supports built-in AI skills in Azure AI Search?" — options: Azure Functions / Foundry Tools / Azure Cosmos DB. (Correct: **Foundry Tools** — matches Unit 4.)
3. "Which kind of projection results in a relational data schema for extracted fields?" — options: File / Object / Table. (Correct: **Table** — matches Unit 6.)

## Unit 9: Summary

Recap: Azure AI Search enables building intelligent search and knowledge mining solutions by indexing and enriching data from various sources. The module covered the indexing process, use of AI skills for data enrichment, and persisting enriched data in a knowledge store for further analysis and integration.

Reference cited: "Azure AI Search documentation" — `/en-us/azure/search/`.
