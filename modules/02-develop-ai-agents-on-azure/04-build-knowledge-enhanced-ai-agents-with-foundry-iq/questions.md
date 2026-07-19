# Practice questions — Build knowledge-enhanced AI agents with Foundry IQ (Introduction to Foundry IQ)

## Introduction

**Q1.** According to the module, what is the primary engineering burden that leads organizations to duplicate effort when multiple teams each build their own knowledge-enabled agent?
A. Provisioning separate Azure subscriptions per agent to isolate billing and quota limits
B. Connecting to data sources, implementing chunking strategies, building vector databases, and managing access controls
C. Writing separate large language models for each business domain from scratch every time
D. Configuring separate Azure Active Directory tenants per agent for isolation and compliance
**Answer:** B — The module explicitly lists these four repeated engineering tasks as the burden every team re-solves. A, C, and D are not mentioned and are not realistic RAG-building tasks.

**Q2.** Which statement best defines Foundry IQ per the module introduction?
A. A new large language model architecture optimized specifically for enterprise question-answering tasks
B. Microsoft's unified knowledge platform that transforms how AI agents access organizational data via a shared knowledge-management system
C. A replacement for Azure AI Search that uses a proprietary, in-house vector engine built internally
D. A monitoring dashboard for tracking AI agent token usage and per-query billing costs over the billing cycle
**Answer:** B — This is the module's verbatim definition. C is a distractor because Foundry IQ is built ON Azure AI Search, not a replacement for it; D confuses it with observability tooling.

**Q3.** Which of the following are listed as limitations of traditional/simple AI agents that RAG and Foundry IQ address? (Choose two.)
A. Constrained by knowledge cutoff dates
B. Inability to call any external APIs whatsoever
C. Generation of generic responses without company context
D. Excessive GPU cost during model training
**Answer:** A, C — The module lists knowledge cutoff dates and lack of private-data/context (generic responses) as limitations, along with fabricated responses and scalability issues. B and D are not stated limitations in this module.

## Understanding RAG for agents

**Q4.** In the module's three-step RAG process, what happens during the "Augment" step?
A. The system searches configured knowledge bases for relevant content matches
B. Retrieved content is combined with the user's question to provide factual context
C. The agent creates a response using training data and retrieved information
D. Documents are chunked and embedded into a vector index during ingestion
**Answer:** B — Retrieve finds content, Augment combines it with the query for context, Generate produces the final response. D describes indexing, which is a separate Foundry IQ data-source pipeline step, not part of the three RAG steps.

**Q5.** Which THREE advantages does the module attribute directly to RAG? (Choose three.)
A. Real-time updates without requiring retraining
B. Source transparency showing which documents informed a response
C. Automatic fine-tuning of the underlying LLM
D. Factual grounding that eliminates fabricated information
**Answer:** A, B, D — The module states RAG delivers real-time updates, source transparency, and factual grounding. C is a distractor; RAG does not fine-tune the model.

**Q6.** A support agent answers "Most companies typically offer flexible return windows" instead of citing the organization's actual return policy document. Per the module's RAG framing, what limitation does this best illustrate?
A. Scalability issues from duplicated engineering effort
B. Lack of private data access / context, producing a generic response
C. A search index health failure requiring a manual reindex operation
D. An MCP protocol misconfiguration between the client and server
**Answer:** B — This matches the "Lack of context → Irrelevant advice" and "Private data access → Generic responses only" limitations table. C and D are unrelated failure categories not implicated by a generic response.

**Q7.** True or false style (single answer): Per the module, does RAG require retraining the language model whenever organizational documents change?
A. Yes, retraining is required for every document update
B. No — RAG retrieves updated content at query time, avoiding retraining
C. Yes, but only for Azure OpenAI models, not other model providers
D. No, but only if semantic ranking is explicitly disabled beforehand
**Answer:** B — This directly corresponds to the module's "real-time updates... without requiring retraining" advantage, and the knowledge-check distractor "RAG automatically retrains the language model whenever organizational documents change" is explicitly wrong.

## Explore Foundry IQ

**Q8.** What underlying Azure service is Foundry IQ built on, per the module?
A. Azure Cosmos DB
B. Azure AI Search
C. Azure Data Lake Storage
D. Azure Cognitive Services Language
**Answer:** B — "Foundry IQ is a managed knowledge platform for AI agents built on Azure AI Search." The other services are not mentioned as the foundation.

**Q9.** How does Foundry IQ organize information within a knowledge base, according to the module?
A. By technical storage location (e.g., "SharePoint Site A" or "Blob Container B")
B. By business domain (e.g., "Product Documentation," "HR Policies") regardless of underlying storage
C. By Azure region alone, where the underlying data physically resides at rest
D. By the specific embedding model used to vectorize the content during ingestion
**Answer:** B — The module explicitly contrasts domain-based organization ("Product Documentation") against searching by storage location ("SharePoint Site A" or "Blob Container B"), which agents do NOT do.

**Q10.** Place the following in the correct order of Foundry IQ's data source connection pipeline: Discovery, Indexing, Monitoring, Processing.
A. Discovery → Processing → Indexing → Monitoring
B. Processing → Discovery → Monitoring → Indexing
C. Discovery → Indexing → Processing → Monitoring
D. Monitoring → Discovery → Processing → Indexing
**Answer:** A — Module order: Discovery (scan storage) → Processing (chunk/embed) → Indexing (searchable) → Monitoring (reindex on change).

**Q11.** In the code sample that creates a "product-support-agent," which class is used to wrap the knowledge base connection as an agent tool?
A. `KnowledgeBaseTool`
B. `MCPTool`
C. `VectorSearchTool`
D. `RetrievalAugmentedTool`
**Answer:** B — The sample imports `MCPTool` from `azure.ai.projects.models` and constructs it with `server_label` and `server_url` pointing at `{search_endpoint}/knowledgebases/{name}/mcp`.

**Q12.** What protocol does Foundry IQ use to connect agents to knowledge bases?
A. A2A (Agent-to-Agent) protocol
B. REST/GraphQL hybrid protocol
C. Model Context Protocol (MCP)
D. gRPC streaming protocol
**Answer:** C — The module explicitly states: "Foundry IQ uses the Model Context Protocol (MCP) to connect agents to knowledge bases." A2A is a different protocol (for agent-to-agent communication) not used here — a classic exam distractor pairing.

**Q13.** Which class from `azure.ai.projects.models`, combined with `model`, `instructions`, and `tools`, defines an agent's configuration in the sample code?
A. `AgentConfiguration`
B. `PromptAgentDefinition`
C. `AgentToolDefinition`
D. `KnowledgeAgentDefinition`
**Answer:** B — The exact class used in every code sample is `PromptAgentDefinition`, instantiated with `model=`, `instructions=`, `tools=[knowledge_tool]`.

**Q14.** An organization has a support agent, an employee assistant, and a developer agent. Per the module's "shared knowledge advantage," which statement is correct?
A. Each agent must maintain its own separate, fully duplicated copy of every knowledge base it references, per this module
B. The Product Documentation knowledge base can serve both the support agent and developer agent, while the HR Policies knowledge base serves only the employee assistant
C. Only one single agent per organization can ever connect to a given knowledge base at all, per this module's design
D. Knowledge bases must be entirely rebuilt from scratch every single time a new agent is added to the tenant's project
**Answer:** B — This is the module's exact example of shared knowledge base reuse across multiple agents with different scopes.

**Q41.** How does Foundry IQ's built-in retrieval intelligence handle a simple factual question versus a complex, multi-part question, per the module?
A. Both always use identical keyword-only search regardless of question complexity
B. Simple factual questions use keyword search; complex questions combine semantic search with query expansion
C. Simple questions require manual developer intervention; complex questions are fully automated
D. Complex questions are rejected and routed to a fallback response automatically
E. All questions use only semantic search exclusively, never keyword search under any circumstances
**Answer:** B — The module states the platform automatically analyzes the question and selects retrieval strategies based on it: simple factual questions use keyword search, while complex questions combine semantic search with query expansion.

**Q42.** What is the exact URL pattern used to construct the `server_url` for an `MCPTool` pointing at a Foundry IQ knowledge base?
A. `{search_endpoint}/mcp/knowledgebases/{knowledge_base_name}`
B. `{search_endpoint}/knowledgebases/{knowledge_base_name}/mcp`
C. `{project_endpoint}/agents/{agent_name}/knowledgebases`
D. `{search_endpoint}/api/v1/kb/{knowledge_base_name}`
**Answer:** B — The module's code sample constructs `server_url=f"{search_endpoint}/knowledgebases/product-documentation/mcp"`, i.e., the pattern `{search_endpoint}/knowledgebases/{knowledge_base_name}/mcp`.

## Configure data sources for knowledge bases

**Q15.** Foundry IQ supports six primary data source types. Which of the following is NOT one of them?
A. Azure Blob Storage
B. OneLake, accessed through Microsoft Fabric
C. Azure Cosmos DB
D. Web (via Bing)
**Answer:** C — The six types are Azure AI Search Index, Azure Blob Storage, Web, SharePoint (Remote), SharePoint (Indexed), and OneLake. Azure Cosmos DB is not listed as a Foundry IQ data source.

**Q16.** Which data source type provides "Real-time" access via Bing for current, public information?
A. Azure AI Search Index
B. Web
C. SharePoint (Remote)
D. OneLake
**Answer:** B — The data source table marks Web as "Real-time" access, "Best For: Current, public information via Bing." SharePoint (Remote) is also real-time but scoped to SharePoint content, not general public web content.

**Q17.** Which TWO data source types use "Indexed" (rather than Direct or Real-time) access, per the module's data source table? (Choose two.)
A. Azure AI Search Index
B. Azure Blob Storage
C. SharePoint (Indexed)
D. OneLake
**Answer:** A, C — Azure AI Search Index and SharePoint (Indexed) are both categorized as "Indexed" access type. Azure Blob Storage and OneLake are categorized as "Direct."

**Q18.** A team wants agent responses grounded strictly in verifiable, controlled sources and is wary of using an uncontrolled external source. Per the module's caution, which data source should they be cautious about relying on for accuracy-critical answers?
A. Azure AI Search Index
B. Web (Bing grounding)
C. Azure Blob Storage
D. OneLake, accessed via Microsoft Fabric
**Answer:** B — The module states: "With web grounding, you're relying on Bing's search results, which means less control over the specific sources your agent references... consider using indexed, controlled data sources instead."

**Q19.** Which statement correctly distinguishes SharePoint Remote from SharePoint Indexed?
A. SharePoint Remote requires building and maintaining a full search index ahead of time, while SharePoint Indexed queries content live with absolutely no preprocessing step at all
B. SharePoint Remote queries SharePoint in real time and automatically respects existing SharePoint permissions with no index to maintain; SharePoint Indexed preprocesses content into Azure AI Search for faster response and advanced search features
C. Both approaches require identical setup steps, identical maintenance overhead, and offer identical response times in every possible scenario the module describes
D. SharePoint Indexed cannot be combined with any other data source type in the same knowledge base under any configuration described in the module
**Answer:** B — This matches the comparison table exactly (access method, response time, maintenance, advanced search, freshness, permissions). A reverses the two approaches; C and D contradict the module's comparison.

**Q20.** A data science team stores business intelligence reports and research outputs in a Microsoft Fabric data lakehouse and wants an agent to reference them. Which Foundry IQ data source should they configure?
A. Azure Blob Storage
B. OneLake
C. SharePoint (Indexed)
D. Azure AI Search Index
**Answer:** B — OneLake is explicitly described as providing access to unstructured data in a Microsoft Fabric data lakehouse, with business intelligence reports and research outputs listed as example use cases.

**Q21.** Which benefits are explicitly attributed to using an Azure AI Search Index as a Foundry IQ data source? (Choose three.)
A. Semantic ranking
B. Custom scoring
C. Automatic language model retraining
D. Faceted navigation
**Answer:** A, B, D — The module lists semantic ranking, custom scoring, faceted navigation, and multi-language support as the key benefits. Automatic retraining is not a benefit of any data source.

**Q22.** Per the module's file-type guidance, which of the following is NOT listed as a common file type ingested from Azure Blob Storage?
A. PDF documents scanned from paper originals
B. Microsoft Word (.docx)
C. Markdown (.md) files exported from a wiki
D. Executable binaries (.exe)
**Answer:** D — Listed types are PDF, .docx, .txt, .md, and HTML. Executable binaries are not mentioned.

**Q43.** A team already has an established Azure AI Search index combining data from multiple origins, and wants to keep using it as-is without rebuilding pipelines, while a separate team just wants direct access to PDF files sitting in Azure Storage with no index to maintain. Per the module's decision guide, which data sources should each team choose respectively?
A. Both teams should choose OneLake instead, since it works for any file type and origin without extra setup
B. First team: Azure AI Search Index (reuse existing investment); second team: Azure Blob Storage (direct file access, no index to build/maintain)
C. First team: SharePoint Indexed; second team: SharePoint Remote for direct, permission-respecting access
D. First team: Web via Bing grounding for the existing index; second team: Azure AI Search Index for the raw PDF files
**Answer:** B — Per the decision guide: "Already indexed / Existing Azure AI Search investment → Azure AI Search Index" and "Files in Azure / Direct file access → Azure Blob Storage." Blob Storage requires no index to build or maintain, unlike Azure AI Search Index.

## Configure retrieval with Foundry IQ

**Q23.** An agent responds to "What's our vacation policy?" with "You get 15 days of PTO annually" but includes no citation. Per the module's three-behavior table, what problem does this illustrate?
A. It relies on training data and gives generic information
B. It is correct but unverifiable, lacking accountability
C. It exceeds the token limit for grounded responses
D. It violates the Model Context Protocol
**Answer:** B — This is exactly the "Searches but doesn't cite" row: "Correct but unverifiable, no accountability." A describes a different (first) behavior row.

**Q24.** According to the module, effective retrieval instructions must specify which three behaviors?
A. Model temperature, max tokens, and top-p
B. When to retrieve, how to cite, and what to do when unsure
C. Which vector database to use, chunk size, and embedding dimension
D. Agent name, agent version, and deployment region
**Answer:** B — The module explicitly lists these three: when to retrieve (always use the KB), how to cite (exact citation format), what to do when unsure (fallback behavior).

**Q25.** What is the exact citation format shown in the module's retrieval instructions example?
A. `[source: doc_name, page: N]`
B. `【doc_id:search_id†source_name】`
C. `{{citation: doc_id}}` template syntax
D. `<cite ref="doc_id"/>` HTML tag syntax
**Answer:** B — This exact token format, `【doc_id:search_id†source_name】`, appears in both the instructions example and the "Searches, cites, and grounds" example response.

**Q26.** Which method on the project client returns an OpenAI-compatible client used to create conversations and send test queries against an agent?
A. `project_client.get_agent_client()`
B. `project_client.get_openai_client()`
C. `project_client.agents.create_client()`
D. `project_client.retrieval.get_client()`
**Answer:** B — The testing code calls `openai_client = project_client.get_openai_client()`, followed by `openai_client.conversations.create()` and `openai_client.responses.create(...)`.

**Q27.** In the test-query code sample, what value is passed for `extra_body["agent"]["type"]` when calling `openai_client.responses.create()`?
A. `"agent_id"` string literal
B. `"knowledge_agent"`
C. `"agent_reference"`
D. `"mcp_tool"` string literal
**Answer:** C — The sample uses `extra_body={"agent": {"name": agent.name, "type": "agent_reference"}}`.

**Q28.** A tester asks an agent "What's the weather like today?" against an HR knowledge base with strict retrieval instructions in place. What is the expected behavior per the module's query-type table?
A. The agent should answer using general training data since the KB has no relevant content
B. The agent should provide a graceful fallback such as "I don't have that information..."
C. The agent should escalate the query by triggering an automatic reindex operation
D. The agent should switch to web grounding via Bing automatically instead
**Answer:** B — "Questions outside knowledge base" expects "Graceful fallback ('I don't have that information...')" per the table — not answering from training data, which the instructions explicitly forbid.

**Q29.** Which four characteristics does the module use to evaluate response quality during retrieval testing? (Choose four... presented as options — select the set that matches exactly.)
A. Grounding, Citation, Relevance, Completeness
B. Grounding, Speed, Cost, Completeness
C. Citation, Latency, Throughput, Relevance
D. Grounding, Citation, Token count, Accuracy score
**Answer:** A — The module lists exactly: Grounding, Citation, Relevance, and Completeness as the four characteristics of a good response.

**Q30.** A compliance-domain agent's instructions state it should "only answer questions about compliance policies and procedures" and "refer to the compliance team" for interpretation/legal questions. This matches which retrieval strategy pattern from the module?
A. Customer-facing support agent
B. Internal research assistant
C. Specialized domain expert
D. General-purpose knowledge agent
**Answer:** C — This is the module's "Specialized domain experts" pattern, contrasted with support agents (which say "let me connect you with a specialist") and research assistants (which synthesize across multiple sources with confidence levels).

**Q31.** Which metrics does the module recommend tracking when moving a knowledge-enabled agent from testing to production? (Choose two.)
A. Citation frequency
B. Fallback frequency
C. Number of Azure regions deployed
D. GPU utilization percentage
**Answer:** A, B — The module lists citation frequency, fallback frequency, query types, and retrieval accuracy as the four production metrics to track. C and D are not mentioned.

**Q44.** A tester asks a knowledge-enabled agent "What are the differences between our leave types?" — a question spanning multiple policy documents. Per the module's query-type table, what is the expected behavior?
A. A graceful fallback since no single document fully answers the question
B. Multiple document retrieval with a synthesized answer that includes multiple citations
C. The agent should refuse and ask the user to rephrase as a single-document question
D. Direct retrieval from exactly one document with a single citation
**Answer:** B — "Questions requiring synthesis" (e.g., differences between leave types, how to request time off) expect "Multiple document retrieval, synthesized answer with multiple citations," distinct from the single-document "Straightforward factual" row.

**Q45.** A user asks a knowledge-enabled agent the vague follow-up "What about benefits?" with no prior context established. Per the module's query-type table, what is the expected agent behavior?
A. Immediately fall back with "I don't have that information"
B. Clarifying questions or a focused search on the most relevant topic
C. Answer confidently from general training data since the question is ambiguous
D. Trigger an automatic reindex of the knowledge base
**Answer:** B — "Ambiguous questions" (e.g., "What about benefits?", "Tell me more about that") expect "Clarifying questions or focused search on most relevant topic" per the module's query-type table — distinct from the fallback expected for genuinely out-of-scope questions.

**Q46.** Which retrieval-strategy pattern instructs the agent to say "Let me connect you with a specialist" rather than guessing when documentation doesn't cover a question, and to focus strictly on official product information?
A. Internal research assistant
B. Customer-facing support agent
C. Specialized domain expert
D. General-purpose knowledge agent
**Answer:** B — The module's "Customer-facing support agents" pattern requires high accuracy and never providing uncertain information, instructing the agent to say "Let me connect you with a specialist" instead of guessing, and to focus on official product information rather than general knowledge.

**Q47.** Which retrieval-strategy pattern is designed to synthesize information across multiple knowledge bases, indicate a confidence level when synthesizing, and suggest related topics that might be useful?
A. Customer-facing support agent
B. Internal research assistant
C. Specialized domain expert
D. Compliance documentation assistant only
**Answer:** B — The "Internal research assistants" pattern searches all relevant knowledge bases for comprehensive answers, synthesizes across multiple sources, indicates confidence level when synthesizing, and suggests related topics — broader in scope than the narrowly focused specialized domain expert pattern.

## Exercise - Integrate an AI agent with Foundry IQ

**Q32.** What are the three high-level tasks the hands-on exercise involves, per the module description?
A. Create a Foundry project, set up a knowledge base, and integrate an AI agent with Foundry IQ
B. Deploy an Azure AI Search cluster, train a custom model, and publish an API
C. Configure Azure Active Directory, assign RBAC roles, and enable private networking
D. Build a vector database, write embedding code, and deploy to Azure Kubernetes Service
**Answer:** A — Per the module description: "Hands-on exercise to create a Foundry project, set up a knowledge base, and integrate an AI agent with Foundry IQ for knowledge-enhanced interactions."

**Q33.** What is required to complete the hands-on exercise, and what alternative does Microsoft Learn offer if it's missing?
A. A GitHub account only, tied to a verified student email; no alternative sign-up path is offered
B. An Azure subscription; users without one can sign up for an account that includes credits for the first 30 days
C. A Microsoft Fabric license purchased separately; no alternative sign-up path is offered
D. A paid Microsoft Learn Plus subscription, billed monthly per seat with no free tier
**Answer:** B — The module states the exercise requires an Azure subscription and links to sign-up for an account with 30-day trial credits.

## Knowledge check

**Q34.** Per the module's built-in knowledge check, what is the primary advantage of RAG over simple AI agents?
A. RAG eliminates the need for large language models by relying entirely on document retrieval
B. RAG enables agents to ground responses in current organizational information and provide source transparency
C. RAG automatically retrains the language model whenever organizational documents change
D. RAG reduces the number of Azure regions needed for global, multi-region deployment
**Answer:** B — This is the correct option per the module's stated RAG advantages (grounding + source transparency); A and C are the module's own distractor options and are factually wrong (RAG augments an LLM, it doesn't replace it or retrain it).

**Q35.** Per the knowledge check, what is the purpose of scoring profiles in Foundry IQ knowledge bases?
A. To encrypt sensitive fields and protect confidential information during retrieval
B. To boost specific fields or attributes so more important results surface first
C. To configure how documents are chunked and embedded for semantic search
D. To define which Azure region hosts the knowledge base index
**Answer:** B — Confirmed in both the knowledge check and the Summary unit: "Scoring profiles boost specific fields or attributes to surface more relevant results." A and C describe unrelated concepts (encryption; chunking/embedding, which scoring profiles do not control).

**Q36.** Per the knowledge check, why is it critical to specify retrieval behavior in agent instructions?
A. Instructions determine the underlying semantic ranking algorithm that Foundry IQ itself applies to search results internally
B. Instructions enable the agent to automatically update knowledge base content when it detects outdated information
C. Without proper instructions, agents might answer from training data instead of the knowledge base, provide unverifiable responses, or fail to cite sources
D. Instructions control which specific Azure subscription the knowledge base's monthly usage is ultimately billed to
**Answer:** C — This is the module's stated correct answer. A and B are distractors: instructions do not control the underlying semantic ranking algorithm nor trigger automatic KB content updates — those are platform/data-source behaviors, not instruction-level behaviors.

## Summary

**Q37.** Per the Summary unit, which THREE techniques does the module identify as improving retrieval effectiveness through data quality? (Choose three.)
A. Scoring profiles
B. Semantic ranking
C. Custom analyzers
D. Automatic model fine-tuning
**Answer:** A, B, C — The Summary states: "You improve retrieval through three key techniques: Scoring profiles... Semantic ranking... Custom analyzers..." Automatic model fine-tuning is not one of them — Foundry IQ retrieval is about search/indexing configuration, not LLM training.

**Q38.** What does "semantic ranking" use to understand meaning and context beyond keywords, per the module summary?
A. Regular expression pattern matching
B. AI models
C. Manual human curation
D. Static keyword weighting rules only
**Answer:** B — "Semantic ranking uses AI models to understand meaning and context beyond keywords" (Summary unit). This distinguishes it from simple keyword search.

**Q39.** Custom analyzers, per the module summary, are best used to handle which type of content?
A. Only PDF documents scanned from paper originals via OCR
B. Specialized content like HTML, product codes, or technical terminology
C. Only real-time Bing web results returned at query time
D. Only OneLake structured tables from a Fabric lakehouse
**Answer:** B — Exact wording: "Custom analyzers handle specialized content like HTML, product codes, or technical terminology."

**Q40.** Which statement best summarizes the relationship between Foundry IQ, Azure AI Search, and MCP as covered across this module?
A. Foundry IQ replaces Azure AI Search entirely and communicates with connected agents using the A2A protocol
B. Foundry IQ is a knowledge-base layer built on Azure AI Search, and it exposes knowledge bases to agents as tools over the Model Context Protocol (MCP)
C. Azure AI Search is actually built on top of Foundry IQ, and both use REST polling to reach connected agents
D. Foundry IQ and Azure AI Search are unrelated, directly competing Microsoft products sold in the same market segment
**Answer:** B — Synthesizing Units 3 and the protocol note: Foundry IQ is built on Azure AI Search (not a replacement) and connects agents via MCP (not A2A, which is a separate agent-to-agent protocol not featured in this module).

## Scenario-based questions

**Q48.** This module is Intermediate level with 8 units. What are its two stated prerequisites?
A. Advanced Python programming and a completed Azure AI Engineer certification
B. Basic understanding of Azure cloud services, and familiarity with AI and machine learning concepts
C. Prior completion of the Semantic Kernel module and an active GitHub account
D. No prerequisites are listed; the module assumes no prior Azure knowledge
**Answer:** B — The module lists exactly these two prerequisites: basic understanding of Azure cloud services, and familiarity with AI and machine learning concepts.

**Q49.** An organization builds a "Product Documentation" knowledge base combining SharePoint technical specs, Blob-stored API docs, and OneLake usage analytics, then connects both a support agent and a developer agent to it. The support agent's instructions say "Answer product questions using the knowledge base" with no further detail. During testing, it sometimes answers from general training data without citations. What two changes, combining concepts from different sections of the module, would most directly fix this while preserving the shared-knowledge benefit?
A. Rebuild a completely separate knowledge base per agent, and disable MCP entirely to force direct, hardcoded API calls between each agent and Azure AI Search instead of using the shared platform
B. Keep the single shared knowledge base (so both agents keep benefiting from the same aggregated sources), but rewrite the instructions to explicitly require always searching the knowledge base, specify the exact citation format, and define fallback behavior when information isn't found
C. Switch the underlying data source from SharePoint to Web grounding via Bing, since Bing is assumed to be inherently more accurate and authoritative for internal product questions than indexed enterprise content
D. Replace `PromptAgentDefinition` with a nonexistent `KnowledgeAgentDefinition` class to force citations automatically, without touching the retrieval instructions at all
**Answer:** B — The knowledge base's multi-source aggregation and cross-agent sharing (Explore Foundry IQ) is independent from retrieval behavior, which is controlled entirely through agent instructions (Configure retrieval with Foundry IQ): vague instructions like "using the knowledge base" produce inconsistent results, while effective instructions specify when to retrieve, how to cite, and fallback behavior. Rebuilding per-agent knowledge bases would forfeit the shared-knowledge advantage unnecessarily, and there is no `KnowledgeAgentDefinition` class in the module.

**Q50.** A compliance-domain agent connects to a knowledge base combining an Azure AI Search Index (existing enterprise index) and SharePoint Indexed content, with strict instructions to cite the specific policy document and section. In production monitoring, the team notices citation frequency is high but fallback frequency is unusually high too, and retrieval accuracy metrics show many retrieved documents don't actually contain the asked-about information. What does this combination of production metrics most likely indicate, and what module-recommended action addresses it?
A. The agent is malfunctioning at the protocol level; switch the underlying MCP connection to the A2A agent-to-agent protocol, which the module frames as the fix for retrieval accuracy problems
B. Retrieval accuracy is low despite frequent citation attempts, suggesting the knowledge base content or search configuration (e.g., scoring profiles, semantic ranking, custom analyzers) needs refinement — the module recommends using production monitoring data to refine instructions, improve knowledge base content, and adjust search configurations
C. High fallback frequency always means the retrieval instructions are too permissive and should simply be loosened, regardless of what the retrieval accuracy metric actually shows in production
D. This pattern is expected and requires no action at all since citations are technically present, even though the cited documents don't actually contain the information the user asked about
**Answer:** B — The module frames citation frequency, fallback frequency, query types, and retrieval accuracy together as signals for iterative improvement: frequent fallbacks combined with low retrieval accuracy point to data-quality/search-configuration issues (addressed via scoring profiles, semantic ranking, or custom analyzers) rather than a protocol failure — MCP vs. A2A is unrelated to retrieval quality.

**Q51.** A developer wants to give one agent access to both a "Product Documentation" knowledge base and a separate self-hosted MCP server for order-status lookups (unrelated to Foundry IQ). Is this combination possible per what's covered across this module and the MCP tools module, and how would it be configured?
A. No — an agent can only ever have one single `MCPTool` registered in its `tools` list at any given time, per the Foundry Agent Service SDK's documented tool-list constraints
B. Yes — since Foundry IQ knowledge bases are themselves exposed to agents as MCP tools via `MCPTool`, and Foundry Agent Service supports connecting to multiple MCP servers simultaneously (each as its own tool with its own `server_label`/`server_url`), both could be added to the same agent's `tools` list
C. Yes, but only if both connected servers are themselves Foundry IQ knowledge bases specifically, since arbitrary self-hosted MCP servers aren't compatible with the `tools` list format
D. No — Foundry IQ knowledge bases use a completely different, incompatible tool type from custom MCP servers, requiring an entirely separate SDK class and registration process
**Answer:** B — This module shows Foundry IQ knowledge bases are connected to agents via `MCPTool` (an MCP server under the hood), and the MCP tools module establishes that an agent can connect to multiple MCP servers simultaneously, each added as a separate tool. Since both are ordinary `MCPTool` instances, they can coexist in one agent's `tools` list.
