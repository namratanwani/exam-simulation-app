# Build knowledge-enhanced AI agents with Foundry IQ (Introduction to Foundry IQ)

Source: https://learn.microsoft.com/en-us/training/modules/introduction-foundry-iq/

## Learning objectives

In this module, you:

- Explain how RAG solves the knowledge problem by connecting agents to real-time information
- Describe how Foundry IQ provides a shared knowledge platform that multiple agents can access
- Configure data sources for knowledge bases including Azure AI Search, Blob Storage, SharePoint, and OneLake
- Configure agent instructions to control retrieval behavior and ensure consistent citations
- Test and monitor agent retrieval to maintain quality in production

Prerequisites: basic understanding of Azure cloud services; familiarity with AI and machine learning concepts.

Module facts: Intermediate level, 8 units, roles = AI Engineer / Developer / Solution Architect, product = Azure / Microsoft Foundry.

## Exam relevance

This module is the primary source for the **knowledge/retrieval-integration** slice of Learning Path 2 ("Develop AI agents on Azure"). It maps to EXAM_SKILLS.md bullets:

- **Plan and manage an Azure AI solution → Choose the appropriate Foundry services for generative AI and agents**
  - "Choose the appropriate Foundry services for generative tasks, grounding, vector search, agent workflows, or multimodal processing" — Foundry IQ vs. raw Azure AI Search vs. building custom RAG.
  - "Choose an appropriate method for retrieval and indexing" — Azure AI Search Index vs. Blob Storage vs. Web (Bing) vs. SharePoint (Remote/Indexed) vs. OneLake data source types.
  - "Choose appropriate memory, tool, and knowledge integration services for agent solutions" — Foundry IQ knowledge bases as a shared knowledge-integration service surfaced to agents as an MCP tool.
- **Manage, monitor, and secure AI systems**
  - "Monitor data ingestion quality, search index health, and relevance performance" — testing/monitoring retrieval behavior, citation frequency, fallback frequency (Unit 5).
- **Implement generative AI and agentic solutions → Build generative applications by using Foundry**
  - "Implement retrieval-augmented generation (RAG) in an application" — the Retrieve/Augment/Generate cycle (Unit 2).
- **Build agents by using Foundry**
  - "Build agents that integrate retrieval, function-calling, and conversation memory" and "Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions" — connecting a `PromptAgentDefinition` to a knowledge base via `MCPTool` (Units 3 and 5).
- **Implement information extraction solutions → Build retrieval and grounding pipelines**
  - "Ingest and index content, such as documents, images, audio, and video" — Discovery/Processing/Indexing/Monitoring pipeline for data sources (Unit 3).
  - "Configure semantic search, hybrid search, and vector search for grounding" — semantic ranking, custom scoring, chunking/embedding described for Foundry IQ knowledge bases (Units 3 and 4).
  - "Connect retrieval pipelines directly to workflows and agent tools" — knowledge base exposed to an agent as a tool over MCP.

**Distinguishing note:** Foundry IQ is **not** a new search engine — it is a managed knowledge-base layer **built on top of Azure AI Search** that automates indexing/embedding/retrieval-strategy-selection and exposes the result to agents as a shared **MCP** tool, so multiple agents reuse the same knowledge base instead of each agent (or team) standing up its own RAG/vector-search pipeline.

## Introduction

Organizations adopting AI agents hit a scaling wall: agents are useful for simple, predefined tasks, but real power comes from letting agents access organizational knowledge (policies, procedures, product docs, support articles, domain expertise).

**Limitations of traditional/simple AI agents:**
- Can't access private/organizational data
- Constrained by model knowledge-cutoff dates
- Generate generic responses lacking company context
- Fabricate ("hallucinate") information when they lack factual grounding

Building knowledge-enabled agents yourself requires: connecting to data sources, implementing chunking strategies, building vector databases, and managing access controls — engineering work every team ends up repeating.

**Foundry IQ** is defined as: *Microsoft's unified knowledge platform that transforms how AI agents access organizational data.* Instead of rebuilding custom RAG pipelines per project, you get a shared knowledge-management system. Multiple agents can access the same knowledge bases, and improvements to a knowledge base benefit every connected agent immediately.

## Understanding RAG for agents

### Simple AI agent limitations (table)

| Limitation | Impact | Example |
|---|---|---|
| Knowledge cutoff dates | No access to recent information | Can't help with newly released features or updated policies |
| Private data access | Generic responses only | Missing company procedures, support knowledge, product specs |
| Lack of context | Irrelevant advice | Ignores specific security requirements or approval workflows |
| Fabricated responses | Compliance and security risks | Confident-sounding but incorrect information |
| Scalability issues | Duplicated engineering effort | Every team rebuilds the same RAG infrastructure |

### How RAG solves these problems

RAG (Retrieval Augmented Generation) connects agents to organizational knowledge sources in real time, moving from static training data to dynamic knowledge retrieval.

**The RAG process — three coordinated steps (exact terms used):**
1. **Retrieve**: System searches knowledge bases for relevant content related to the query
2. **Augment**: Combines retrieved content with the user's question to provide factual context
3. **Generate**: Agent creates a response using both training data and retrieved information

**Three critical advantages RAG delivers:**
- **Real-time updates** — keeps agents current with policies/procedures without retraining
- **Source transparency** — shows users which documents informed each response (trust + verification)
- **Factual grounding** — anchors responses in actual organizational content, eliminating fabrication, ensuring compliance

RAG solves the knowledge problem, but building it requires significant technical expertise — this is the gap Foundry IQ fills.

## Explore Foundry IQ

### What is Foundry IQ?

> "Foundry IQ is a managed knowledge platform for AI agents **built on Azure AI Search**. It provides the retrieval capabilities you learned about in RAG, but as a shared service that multiple agents can use."

Scenario: product docs in SharePoint, customer policies in Azure Blob Storage, training materials in OneLake. Traditional RAG = index each source separately per agent. Foundry IQ = create knowledge bases **once**, connect any number of agents to them.

### How knowledge bases organize information

Knowledge bases are organized **by business domain**, not by technical storage location. Agents search a concept like "Product Documentation" or "HR Policies," not "SharePoint Site A" or "Blob Container B." One knowledge base can aggregate multiple underlying sources — e.g., a "Product Documentation" knowledge base might combine:
- Technical specifications from SharePoint
- API documentation from Azure Blob Storage
- Usage analytics from OneLake
- Support tickets from an existing search index

To agents this looks like one unified knowledge source.

### Connecting data sources — the 4-step pipeline

When you add a data source to a knowledge base, Foundry IQ performs:
1. **Discovery** — scans your storage location for documents
2. **Processing** — documents are chunked and embedded for semantic search
3. **Indexing** — content becomes searchable through the knowledge base
4. **Monitoring** — changes to your documents trigger automatic reindexing

Configuration is done once per data source; every agent connected to that knowledge base benefits from updates automatically.

### Built-in retrieval intelligence

When an agent queries a knowledge base, the platform automatically:
- **Analyzes the question** — e.g., "What's our return policy for damaged items?" needs different retrieval than "List all return policies"
- **Selects retrieval strategies** based on the query — simple factual questions use keyword search; complex questions combine semantic search with query expansion
- **Ranks results** using relevance scoring — most contextually appropriate info surfaces first, reducing tokens needed for agent responses
- **Provides citations** so agents can reference source documents

This runs without custom code — you define knowledge base contents; Foundry IQ determines retrieval mechanics.

### Connecting agents to knowledge — code sample

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, MCPTool

project_client = AIProjectClient(endpoint=project_endpoint, credential=credential)

# Connect to the product documentation knowledge base
knowledge_tool = MCPTool(
    server_label="product-docs",
    server_url=f"{search_endpoint}/knowledgebases/product-documentation/mcp"
)

# Create an agent with knowledge access
agent = project_client.agents.create_version(
    agent_name="product-support-agent",
    definition=PromptAgentDefinition(
        model="gpt-4o-mini",
        instructions="Answer product questions using the knowledge base. Always cite your sources.",
        tools=[knowledge_tool]
    )
)
```

Key SDK elements (exact names):
- `azure.ai.projects.AIProjectClient` — client constructed with `endpoint=project_endpoint, credential=credential`
- `azure.ai.projects.models.PromptAgentDefinition` — agent definition with `model`, `instructions`, `tools`
- `azure.ai.projects.models.MCPTool` — knowledge base tool wrapper, params: `server_label`, `server_url`
- MCP server URL pattern: `{search_endpoint}/knowledgebases/{knowledge_base_name}/mcp`
- `project_client.agents.create_version(agent_name=..., definition=...)` creates/versions the agent
- Model used in examples: `gpt-4o-mini`

The agent retrieves knowledge-base information the same way it would use any other **tool** — no custom retrieval logic or search-infrastructure management required.

### The shared knowledge advantage

Example org with 3 agents (support agent, employee assistant, developer agent): with traditional RAG you'd build/maintain three retrieval systems. With Foundry IQ:
- **Product Documentation** knowledge base serves both the support agent and developer agent
- **HR Policies** knowledge base serves only the employee assistant
- Each agent accesses exactly the knowledge it needs
- Improving a knowledge base (adding sources, refining content) benefits every connected agent immediately

**Protocol note (exam-relevant distinction):** Foundry IQ uses the **Model Context Protocol (MCP)** to connect agents to knowledge bases. MCP provides a standardized way for AI agents to access external tools and data sources securely. (Contrast with A2A protocol, which is for agent-to-agent communication, not agent-to-knowledge-source retrieval — this module only uses MCP.)

## Configure data sources for knowledge bases

A knowledge base is only as good as the data connected to it. Foundry IQ supports **six primary data source types**:

| Data Source | Access Type | Best For |
|---|---|---|
| Azure AI Search Index | Indexed | Enterprise search with custom pipelines |
| Azure Blob Storage | Direct | Document files in Azure Storage |
| Web | Real-time | Current, public information via Bing |
| SharePoint (Remote) | Real-time | Live SharePoint content with Microsoft 365 governance |
| SharePoint (Indexed) | Indexed | Advanced search on SharePoint with custom pipelines |
| OneLake | Direct | Unstructured data in Microsoft Fabric |

With real-time sources you get current information; with internal sources (SharePoint/OneLake) you retain security and governance.

### Azure AI Search Index
Use when you already invested in Azure AI Search and want to reuse existing indexes (which may already aggregate multiple origins). Ideal when you need semantic ranking, filters, or custom scoring profiles.

Key benefits (exact bullets):
- **Semantic ranking** — finds contextually relevant results, not just keyword matches
- **Custom scoring** — prioritizes results based on your business logic
- **Faceted navigation** — filters results by categories or attributes
- **Multi-language support** — handles content in different languages

### Azure Blob Storage
Direct retrieval of documents/files from blob containers — no index to build/maintain (contrast with Azure AI Search Index, which requires building/maintaining an index). Common supported file types: PDF, Microsoft Word (.docx), Text (.txt), Markdown (.md), HTML.

You can organize blobs into containers by topic or access level for governance.

### Web
Grounds the agent with real-time internet content **via Bing**. Useful for recent events/news, current pricing/availability, frequently changing information, topics outside the internal knowledge base.

Important caveat (exact wording): "With web grounding, you're relying on Bing's search results, which means less control over the specific sources your agent references. When accuracy and source verification are critical, consider using indexed, controlled data sources instead." Web can be combined with internal sources as a supplementary fallback.

### Microsoft SharePoint options — Remote vs. Indexed (comparison table)

| Feature | Remote | Indexed |
|---|---|---|
| Access method | Real-time queries | Preprocessed index |
| Response time | Depends on SharePoint | Faster |
| Maintenance | No index to maintain | Requires index updates |
| Advanced search | Limited | Full Azure AI Search capabilities |
| Data freshness | Always current | Depends on indexing schedule |
| Permission handling | Respects SharePoint permissions | Configured during indexing |

**SharePoint Remote**: search capability with Microsoft 365 governance; retrieves content directly from SharePoint in real time without preindexing. Benefits: no index maintenance, always current content, automatically respects existing SharePoint permissions, simpler setup. Use when you need the simplest path to SharePoint data and don't require advanced search features.

**SharePoint Indexed**: indexes SharePoint content into **Azure AI Search** for custom pipelines. Enables: custom analyzers for specialized terminology, enrichment pipelines with AI services, combining SharePoint data with other sources, specialized search experiences. Best when you need advanced search features or are integrating SharePoint data with other sources in an Azure AI Search index.

### Microsoft OneLake
Access to unstructured data in your Microsoft Fabric data lakehouse. Matters when the org uses Microsoft Fabric for data analytics/storage. Use cases: business intelligence reports, data documentation, analytical findings, research outputs.

### Choose the right data source (decision guide)

| If your data is... | And you need... | Choose... |
|---|---|---|
| In SharePoint | Simple setup, always current | SharePoint Remote |
| In SharePoint | Advanced search, custom pipelines | SharePoint Indexed |
| Files in Azure | Direct file access | Azure Blob Storage |
| In Microsoft Fabric | Data lakehouse content | OneLake |
| Already indexed | Existing Azure AI Search investment | Azure AI Search Index |
| Public, current information | Real-time web content | Web |

You can combine multiple sources in one knowledge base (e.g., internal SharePoint as primary + web grounding as supplementary for current events).

## Configure retrieval with Foundry IQ

### The retrieval behavior problem

Without proper configuration, an agent asked "What's our vacation policy?" can behave three different ways:

| Behavior | Example Response | Problem |
|---|---|---|
| Answers from training data | "Most companies offer 2-3 weeks of vacation annually" | Generic, not your actual policy |
| Searches but doesn't cite | "You get 15 days of PTO annually" | Correct but unverifiable, no accountability |
| Searches, cites, and grounds | "You receive 15 days of paid time off annually【doc_id:1†Employee Handbook 2024】" | ✓ Desired behavior |

Only the third (search + cite + ground) is acceptable for enterprise agents.

### Controlling retrieval with instructions

Instructions are "the contract between you and the agent about how it should use knowledge bases." A vague instruction produces inconsistent results:

```python
agent = project_client.agents.create_version(
    agent_name="hr-assistant",
    definition=PromptAgentDefinition(
        model="gpt-4o-mini",
        instructions="Answer HR questions using the knowledge base.",
        tools=[knowledge_tool]
    )
)
```

Problem: "using the knowledge base" doesn't specify *when* to use it or *how* to present results.

**Effective instructions specify three behaviors:**
1. **When to retrieve** — always use the knowledge base, never rely on training data
2. **How to cite** — exact format for source attribution
3. **What to do when unsure** — fallback behavior when information isn't found

Full example:

```python
retrieval_instructions = """You are a helpful HR assistant.

CRITICAL RULES:
- You must ALWAYS search the knowledge base before answering any question
- You must NEVER answer from your own knowledge or training data
- Every answer must include citations in this format: 【doc_id:search_id†source_name】
- If the knowledge base doesn't contain the answer, respond with "I don't have that information in our current documentation. Please contact HR directly at hr@company.com"

Your role is to provide accurate, verifiable information from company documentation."""

agent = project_client.agents.create_version(
    agent_name="hr-assistant",
    definition=PromptAgentDefinition(
        model="gpt-4o-mini",
        instructions=retrieval_instructions,
        tools=[knowledge_tool]
    )
)
```

Note the exact citation token format used throughout the module: `【doc_id:search_id†source_name】`.

### Testing retrieval behavior

Create a conversation session and send test queries using the **OpenAI-compatible client** obtained from the project client:

```python
openai_client = project_client.get_openai_client()
conversation = openai_client.conversations.create()

# Test query that should trigger retrieval
response = openai_client.responses.create(
    conversation=conversation.id,
    input="How many vacation days do I get?",
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}}
)

print(response.output_text)
```

Key API elements (exact names):
- `project_client.get_openai_client()` — returns an OpenAI-compatible client
- `openai_client.conversations.create()` — creates a conversation session
- `openai_client.responses.create(conversation=..., input=..., extra_body={"agent": {"name": ..., "type": "agent_reference"}})` — sends a test query bound to a specific agent via `agent_reference`
- `response.output_text` — the text output of the response

### What to test (query-type table)

| Query Type | Example Questions | Expected Behavior |
|---|---|---|
| Straightforward factual | "What is our vacation policy?" / "Where can I find the security guidelines?" | Direct retrieval with citations |
| Questions requiring synthesis | "What are the differences between our leave types?" / "How do I request time off?" | Multiple document retrieval, synthesized answer with multiple citations |
| Questions outside knowledge base | "What's the weather like today?" / "Tell me about machine learning" | Graceful fallback ("I don't have that information...") |
| Ambiguous questions | "What about benefits?" / "Tell me more about that" | Clarifying questions or focused search on most relevant topic |

### Evaluating response quality — four characteristics
1. **Grounding** — information comes from knowledge base, not training data
2. **Citation** — every factual claim includes source references
3. **Relevance** — retrieved content actually answers the question
4. **Completeness** — all necessary information provided, not just fragments

### Retrieval strategies for different agent types

**Customer-facing support agents** — high accuracy, must never provide uncertain information:
```python
support_instructions = """You provide customer support using our product documentation.

Rules:
- Search the knowledge base for every product question
- Cite documentation for all technical answers
- If documentation doesn't cover a question, say "Let me connect you with a specialist" rather than guessing
- Focus on official product information, not general knowledge"""
```

**Internal research assistants** — can synthesize across documents, provide broader context:
```python
research_instructions = """You help employees research topics across company documentation.

Rules:
- Search all relevant knowledge bases for comprehensive answers
- Synthesize information from multiple sources when helpful
- Always cite all sources used
- Indicate confidence level when synthesizing across documents
- Suggest related topics that might be useful"""
```

**Specialized domain experts** — focus deeply on a specific domain:
```python
compliance_instructions = """You are a compliance documentation assistant.

Rules:
- Only answer questions about compliance policies and procedures
- Always cite the specific policy document and section
- If a question involves interpretation or legal advice, refer to the compliance team
- Keep answers strictly factual based on written policies
- Note the effective date of any policy you reference"""
```

Pattern: define agent scope → specify retrieval requirements → establish citation standards → handle edge cases explicitly.

### Moving from testing to production — monitoring metrics
Track these patterns in production:
- **Citation frequency** — are agents consistently citing sources?
- **Fallback frequency** — how often do agents say "I don't know"?
- **Query types** — what categories of questions appear most often?
- **Retrieval accuracy** — do retrieved documents actually contain answers?

Use this data to refine instructions, improve knowledge base content, and adjust search configurations. Retrieval quality improves through iteration based on real-world usage.

## Exercise - Integrate an AI agent with Foundry IQ

Hands-on lab (requires an Azure subscription; free trial includes credits for the first 30 days). Steps (per module description): create a Foundry project, set up a knowledge base, and integrate an AI agent with Foundry IQ for knowledge-enhanced interactions. The exercise is launched via an external Microsoft Learn lab link (go.microsoft.com fwlink) — no additional technical detail (parameters, code) is exposed on the module page itself; the actual configuration steps happen inside the interactive lab environment.

## Knowledge check

The module's built-in knowledge check covers 4 questions (used as a check on core facts — see questions.md for full practice-question treatment):

1. Primary advantage of RAG over simple AI agents → **RAG enables agents to ground responses in current organizational information and provide source transparency** (not: eliminating the need for LLMs; not: automatically retraining the model).
2. Which data source gives real-time SharePoint access with Microsoft 365 governance → **SharePoint Remote** (queries SharePoint sites/libraries in real time) — not SharePoint Indexed (preprocesses into Azure AI Search), not Azure Blob Storage.
3. Purpose of scoring profiles in Foundry IQ knowledge bases → **To boost specific fields or attributes so more important results surface first** — not encryption, not chunking/embedding configuration.
4. Why specify retrieval behavior in agent instructions → **Without proper instructions, agents might answer from training data instead of the knowledge base, provide unverifiable responses, or fail to cite sources** — instructions do not control the semantic ranking algorithm and do not make the agent auto-update knowledge base content.

## Summary

- **RAG solves the knowledge problem**: retrieves relevant info, augments the query with factual context, generates a grounded response → real-time updates, source transparency, factual grounding.
- **Foundry IQ provides a shared knowledge platform**: eliminates building custom RAG infrastructure per agent. Knowledge bases are organized by business domain; data sources come from SharePoint, Azure Blob Storage, OneLake, or existing Azure AI Search indexes; any agent can connect; improving a knowledge base benefits every connected agent immediately.
- **Data quality determines retrieval effectiveness** — three key techniques (exact terms):
  - **Scoring profiles** — boost specific fields/attributes to surface more relevant results
  - **Semantic ranking** — uses AI models to understand meaning/context beyond keywords
  - **Custom analyzers** — handle specialized content like HTML, product codes, or technical terminology
- **Instructions control agent behavior**: specify when to retrieve (always use the KB), how to cite (exact citation format), and what to do when unsure (graceful fallback). Test different query types to verify consistent behavior; monitor production usage to refine configuration.
