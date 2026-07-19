# Develop AI agents with Microsoft Foundry and Visual Studio Code

Source: https://learn.microsoft.com/en-us/training/modules/develop-ai-agents-azure-vs-code/

> Note on naming: this module (updated 2026-05-01) uses the current product name **Microsoft Foundry** and **Microsoft Foundry Agent Service** throughout (rather than the older "Azure AI Foundry" branding used in the module's URL slug `develop-ai-agents-azure-vs-code`). The extension is the **Microsoft Foundry extension for Visual Studio Code**. Treat "Microsoft Foundry" and "Azure AI Foundry" as the same service for exam purposes — Microsoft has renamed the product over time.

## Learning objectives

By the end of this module, you'll be able to:

- Describe the purpose and capabilities of AI agents
- Explain the key features of Microsoft Foundry Agent Service
- Set up and configure the Microsoft Foundry extension in Visual Studio Code
- Build and configure AI agents using multiple development approaches
- Extend agent capabilities with tools and functions
- Test agents using integrated playgrounds
- Deploy and integrate agents into applications

**Prerequisites:** Familiarity with Azure and the Azure portal; understanding of generative AI; basic familiarity with Visual Studio Code.

**Module stats:** 11 units, Intermediate level, roles: AI Engineer / Developer / Data Scientist / Solution Architect. Products: Microsoft Foundry, Foundry Agent Service.

## Exam relevance

This module maps primarily to the **Implement generative AI and agentic solutions (30–35%)** domain of EXAM_SKILLS.md, specifically:

- **Build agents by using Foundry — Define agent roles, goals, conversation-tracking approach, and tool schemas.** The module covers writing agent instructions (role/goal definition), the Responses API for conversation-state tracking, and defining `tools:` schemas in agent YAML.
- **Build agents by using Foundry — Build agents that integrate retrieval, function-calling, and conversation memory.** Covered via File Search (RAG/retrieval), automatic tool-calling lifecycle (function-calling), and the Responses API (conversation memory/state).
- **Build agents by using Foundry — Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions.** Covered via the tool catalog: Code Interpreter, File Search, Bing Web Search, Azure AI Search, OpenAPI tools, MCP servers, SharePoint, Microsoft Fabric, Browser Automation, Computer Use, Image Generation, Deep Research, Agent-to-Agent.
- **Build agents by using Foundry — Implement orchestrated multi-agent solutions.** Briefly introduced via "Workflow agents" (multi-agent orchestration defined in YAML) and the "Agent-to-Agent" tool, though deep multi-agent orchestration is deferred to later modules.

It also touches the **Plan and manage an Azure AI solution (25–30%)** domain:

- **Set up AI solutions in Foundry — Design Azure infrastructure for AI apps and agent-based solutions / Choose appropriate deployment options / Configure model and agent deployments.** Covered via required resources (Foundry project, model deployments), optional services (Azure AI Search, Azure Storage, Azure Key Vault, Azure Functions), and the deploy vs. publish distinction (Agent Application resources).
- **Manage, monitor, and secure AI systems — Configure security, including managed identity, private networking, keyless credentials, and role policies.** Covered via Entra ID authentication for Agent Applications, the **Azure AI User** RBAC role requirement, and the note that API key auth is *not* supported for Agent Applications.
- **Manage, monitor, and secure AI systems — Monitor model performance...** Covered lightly via Application Insights integration and production monitoring guidance (response times, tool invocation success rates, token consumption).
- **Implement responsible AI across generative AI and agentic systems — Govern agent behavior with oversight modes, constraints, and tool-access controls.** Covered via the AI agent security-risk table (prompt injection, data leakage, over-reliance on autonomous actions, etc.) and mitigation strategies (RBAC, least privilege, human-in-the-loop approvals, logging/traceability).

## Introduction

Scenario framing: a healthcare organization automating patient interactions (scheduling, inquiries, real-time medical info) needs enterprise-grade security without heavy infra management — this is the motivating use case for **Microsoft Foundry Agent Service**, a fully managed platform for building, deploying, and scaling AI agents without managing underlying compute/storage.

Two development surfaces are introduced: the **Foundry portal** and the **Microsoft Foundry extension for Visual Studio Code**. The module teaches configuring agents with custom instructions, extending capabilities with tools, and integrating agents into applications, so you can choose the right approach and deploy production-ready agents.

## Understand AI agents and Microsoft Foundry Agent Service

### Definition
An **AI agent** is a software service that uses generative AI to understand and perform tasks on behalf of users or other programs. Unlike traditional rule-based applications, agents operate independently: understanding context, making decisions, and taking actions toward goals — combining AI models with specialized tools.

### Why AI agents are useful
- **Automation of routine tasks** — frees humans for strategic/creative work.
- **Enhanced decision-making** — agents use advanced algorithms/ML to analyze data and decide autonomously (distinguishing them from simple chat models that only generate text).
- **Scalability** — grow capability without proportional headcount growth.
- **24/7 availability** — continuous operation.

### Example use cases
- **Personal productivity agents** — e.g., Microsoft 365 Copilot (drafting documents, presentations, data analysis).
- **Research agents** — continuous trend monitoring/report generation (finance, healthcare, marketing).
- **Sales agents** — lead research, personalized follow-ups, call scheduling.
- **Customer service agents** — routine inquiries; example cited: **Cineplex** uses an AI agent to process refund requests, reducing handling time.
- **Developer agents** — code review, bug fixing, repo management; example cited: **GitHub Copilot**.

### Security considerations for AI agents
Because agents access sensitive data and act independently, security must be designed in from the start. Risk table (verbatim structure):

| Risk Area | Description | Example Impact |
|---|---|---|
| Data leakage and privacy exposure | Agents access sensitive data; without controls they can expose it | Agent summarizing internal files leaks private data to customers |
| Prompt injection and manipulation attacks | Malicious inputs override intended agent behavior | Hidden instructions cause agent to leak system credentials |
| Unauthorized access and privilege escalation | Weak auth/access controls let agents/attackers reach systems they shouldn't | Agent connected to CRM performs admin-level exports/deletes |
| Data poisoning | Corrupted training/contextual data causes biased/unsafe decisions | Poisoned dataset causes support agent to recommend harmful content |
| Supply chain vulnerabilities | Reliance on external APIs/plugins/model endpoints expands attack surface | Compromised third-party plugin injects malicious code |
| Over-reliance on autonomous actions | Highly autonomous agents execute unintended actions if unconstrained | Agent mistakenly sends payments or publishes unverified content |
| Inadequate auditability and logging | Missing logs make it hard to trace/detect malicious behavior | Security teams can't identify data misuse |
| Model inversion and output leakage | Attackers infer sensitive training/prompt data from outputs | Repeated queries extract private fine-tuning data |

**Mitigation strategies (security-by-design):**
- Enforce **role-based access controls (RBAC)** and **least privilege**
- **Prompt filtering and validation** layers to prevent injection
- Sandbox/gate sensitive operations behind **human-in-the-loop approvals**
- **Comprehensive logging and traceability** for all agent actions
- Audit **third-party dependencies** regularly
- Continuously retrain/validate models to detect **data drift** or poisoning attempts

### Microsoft Foundry Agent Service overview
A fully managed service to securely build, deploy, and scale AI agents without managing compute/storage. Agents are created via custom instructions and advanced tools. Compared to prior approaches requiring significant coding effort against standard APIs, Foundry Agent Service enables building agents (via portal or app code) in **fewer than 50 lines of code**.

### Agent types (exam-critical distinction)
Microsoft Foundry supports **two primary agent types**:

1. **Declarative agents** — defined through *configuration*, not code. Two forms:
   - **Prompt-based agents** — a single agent configured with a model, instructions, tools, and prompts. Most common type; the focus of this module.
   - **Workflow agents** — multi-agent orchestrations defined in **YAML**, enabling multiple agents to collaborate on complex scenarios.
2. **Hosted agents** — containerized agents *created and deployed in code*, then hosted by the Foundry platform. Give full control over agent logic/execution while the platform manages infrastructure.

Distinguishing factor: declarative = configuration-driven (portal forms or YAML); hosted = code-driven containers. Prompt-based (single agent) vs. workflow (multi-agent YAML orchestration) is the split *within* declarative agents.

### Key features of Microsoft Foundry Agent Service
- **Automatic tool calling** — service handles the entire tool-calling lifecycle (running the model, invoking tools, returning results), eliminating complex integration code.
- **Securely managed data** — conversation states are securely managed through the **Responses API**, removing the need for manual state management.
- **Extensive tool catalog** — built-in and community tools: code execution, file search, web search, Azure service/external API integrations.
- **Model selection** — choose from various AI models to match performance/cost.
- **Enterprise-grade security** — data privacy/compliance, keyless authentication, built-in content safety filters.
- **Customizable storage** — platform-managed storage or bring-your-own **Azure Blob storage**.
- **Observability and tracing** — built-in monitoring to track behavior, debug, and optimize in production.

These features are contrasted favorably against developing directly with the **Inference API** (more streamlined/secure with Agent Service).

## Explore development approaches

### Foundry portal development
Web-based, no-code interface. Best for:
- Quick prototyping
- Visual configuration (forms/dropdowns)
- Centralized management (all agents/projects in one place)
- Team collaboration with non-technical stakeholders
- Resource oversight (token usage, latency, evaluation dashboards)

Access: navigate to your Foundry project → Agents section → start building. No extra tools to install.

### Visual Studio Code development
The **Microsoft Foundry extension for Visual Studio Code** brings enterprise-grade AI capabilities into the editor. Suited to developers wanting tight integration with dev workflows.

**Extension structure — three sections:**
1. **Resources** — browse/manage Foundry project assets:
   - Deployed models
   - Declarative agents (prompt-based and workflow)
   - Hosted agents (containerized, code-deployed)
   - Connections (to external services)
   - Vector stores (document collections for File Search)
2. **Tools**:
   - Model Catalog (browse/deploy models)
   - Model Playground (experiment with models)
   - Agent Playgrounds (remote or local)
   - Local Visualizer (debug/visualize agent behavior locally)
   - Deploy Hosted Agents
3. **Help and Feedback** — docs/support.

Also provides: visual **Agent Designer**, integrated **code generation**, direct **YAML configuration** editing.

Best for:
- Developer-centric workflows (agents alongside app code)
- Version control integration (Git)
- Rapid iteration
- Code-first development (direct YAML editing)
- Local/offline development before deploying to Azure

Installs from the Visual Studio Code Marketplace.

### Typical development workflow (applies to both approaches)
1. Connect to your Microsoft Foundry project
2. Create an AI agent (name + purpose) in the Foundry portal
3. Configure agent instructions (portal or VS Code)
4. Add tools
5. Test using integrated playgrounds
6. Iterate
7. Deploy to production
8. Integrate into applications

Portal and VS Code differ mainly in *interface style*, not capability.

### Required Azure resources
- **Microsoft Foundry project** — organizes agents, models, related assets.
- **Model deployments** — e.g., **GPT-4.1** or **Claude Sonnet 4.6** power agents.

Creating a Foundry project auto-provisions needed infrastructure; the service integrates supporting services behind the scenes as capabilities (e.g., File Search) are added. Extending further (e.g., **Foundry IQ**) may require deploying additional Azure services manually.

### Optional Azure services
- **Azure AI Search** — advanced knowledge retrieval (Foundry IQ / File Search tools)
- **Azure Storage** — storing/managing files agents access
- **Azure Key Vault** — secrets/credentials management
- **Azure Functions** — custom tool implementations/business logic

### Choosing your approach
- Portal: visual configuration, centralized management, quick prototyping, no local setup.
- VS Code: developer-centric workflows, tight app-code integration, version-controlled config files.
- Many teams use both — portal for exploration/stakeholder review, VS Code for detailed dev and production deployment.

## Build your first agent in Microsoft Foundry

### Creating an agent in the Foundry portal
1. Navigate to Microsoft Foundry at **https://ai.azure.com** and sign in with Azure credentials
2. Select your project (or create a new one)
3. Select **Build > Agents** in the left navigation
4. Select **Create** to start a new agent
5. Enter agent details:
   - **Name** — descriptive
   - **Description** — clear purpose statement
   - **Model** — select a deployed model from the dropdown, or deploy a new one

### Configuring agent instructions and properties
**Instructions** field defines role, response behavior, scenario handling. Beyond instructions, the portal exposes model parameters:
- **Temperature** — controls response randomness
- **Top P** — controls response diversity

(Detailed configuration is deferred to the VS Code unit.)

### Testing your agent in the portal
Integrated **Playground** tab: start a conversation, validate instructions, try scenarios. The playground maintains conversation history during the session (multi-turn testing, context retention verification).

### Adding basic tools
Accessible via the **Tools** section of agent config or **Build > Tools** in the portal. Tool catalog has three categories:
- **Configured** — built-in, ready to use immediately (e.g., **Code Interpreter**, **File Search**)
- **Catalog** — additional tools to add (e.g., **Bing Web Search**, **Azure AI Search**, **SharePoint**, more)
- **Custom** — your own tools added via **OpenAPI specifications** or **MCP servers**

### Deploying your agent
After satisfactory testing, deploy for production use. Portal shows deployment status and generates connection info for app integration. Post-deployment, access the agent via the **Microsoft Foundry SDK** or **REST APIs**.

## Set up Visual Studio Code for agent development

### Understanding the Microsoft Foundry extension
Provides direct access to Foundry Agent Service capabilities, combining visual design tools with code-based configuration. Same three-section layout as before: Resources, Tools, Help and Feedback.

### Installing and configuring the extension
**Installation steps:**
1. Open VS Code
2. Select **Extensions** pane, or press **Ctrl+Shift+X** (Windows/Linux) / **Cmd+Shift+X** (Mac)
3. Search for **"Foundry"** in the marketplace search box
4. Select the **Microsoft Foundry** extension from results
5. Select **Install**
6. Wait for installation (status shown in Extensions panel)

After install, the Microsoft Foundry icon appears in the VS Code **activity bar**.

**Connecting to Azure:**
1. Select the **Azure** icon in the activity bar
2. In **Azure Resources** pane, sign in to Azure if prompted
3. Expand your **Azure subscription** in the resource tree
4. Expand the **Foundry** section to see projects
5. Right-click your **Microsoft Foundry project**
6. Select **Open in Foundry Extension**

The extension then displays project resources (existing agents, model deployments, connections, vector stores) in the Microsoft Foundry panel.

### Preparing for agent development — Deploying a model
1. In the extension, navigate to **Resources**
2. Expand **Model deployments**
3. Select the **+** icon for a new deployment
4. Choose a model (e.g., **GPT-4o** or **GPT-4**)
5. Configure deployment settings:
   - **Deployment name** — descriptive, used when configuring agents
   - **Model version** — specific version
   - **Capacity settings** — throughput configuration
6. Select **Deploy** and wait for completion

### Working with agents in VS Code
Agents are often created in the Foundry portal, then managed/configured in VS Code via the extension — they appear automatically in the extension's **Resources** section. Changes made in VS Code can be saved directly back to Foundry (bidirectional workflow across platforms).

### Managing multiple agents
- Browse agents in the Resources view (organized by project)
- Switch between agents from the list
- Compare configurations by opening multiple YAML files side by side
- Duplicate agents to create variations
- Archive unused agents

## Configure and manage agents in Visual Studio Code

> Note: this configuration workflow applies to **declarative prompt-based agents**. Hosted agents are configured through code; workflow agents use a *different* YAML schema for multi-agent orchestration.

### Essential configuration options (Agent Designer)
- **Agent name** — descriptive identifier (appears in lists, logs, cross-developer references)
- **Model selection** — dropdown of already-deployed models in your project
- **Description** — concise purpose statement
- **System instructions** — behavior, personality, response style
- **Agent ID** — auto-generated by the extension on creation; used when calling the agent via APIs

### Model configuration options
- **Temperature** — response creativity/randomness.
  - Lower values (**0.1–0.3**) → consistent, focused outputs
  - Higher values (**0.7–1.0**) → creative, varied responses
  - For business agents doing structured tasks: **0.3–0.7** typically works well
- **Top P** — limits vocabulary choices during generation (diversity control).
  - Default: **1.0** works for most scenarios; lower it for more constrained/predictable output

These settings sync between the Designer UI and the YAML file.

### Agent YAML structure — complete example
```yaml
# yaml-language-server: $schema=https://aka.ms/ai-foundry-vsc/agent/1.0.0
version: 1.0.0
name: healthcare-assistant
description: Assists healthcare staff with patient appointment scheduling and information retrieval
id: 'agent-abc123xyz'
metadata:
  authors:
    - developer-name
  tags:
    - healthcare
    - customer-service
    - scheduling
model:
  id: 'gpt-4.1'
  options:
    temperature: 0.5
    top_p: 1
instructions: |
  You're a healthcare assistant helping staff schedule patient appointments and retrieve information.

  Your responsibilities:
  - Help staff find available appointment slots
  - Answer questions about patient scheduling policies
  - Provide information about different appointment types
  - Assist with rescheduling and cancellations

  Important guidelines:
  - Never access or share patient medical information
  - Always verify appointment details before confirming
  - Be professional but friendly in all interactions
  - If you're unsure about policies, advise staff to check with management
tools: []
```

YAML sections: **metadata**, **model configuration**, **instructions**, **tools**.

### Benefits of YAML configuration
- **Version control** — track changes in Git alongside app code
- **Bulk updates** — multiple simultaneous changes
- **Templates** — reusable agent templates
- **Code review** — configs included in standard review processes
- **Automation** — scripts that generate/modify configs programmatically

The extension **validates YAML syntax in real time**, highlighting errors and giving suggestions.

### Best practices for agent configuration
- Version control your YAML files (Git, alongside app code) — enables rollback, review, change tracking
- Use descriptive names and tags
- Document complex instructions with comments
- Test after every change (use the playground)
- Start simple, then iterate
- Keep instructions focused (one clear purpose per agent — agents doing too much perform inconsistently)

## Extend agent capabilities with tools

### Understanding agent tools
Tools = programmatic functions agents invoke to complete tasks. When the agent determines a tool is needed, it calls it automatically, processes results, and incorporates them into the response.

**Tool-calling lifecycle (automatic, no orchestration code needed):**
1. User sends a message to the agent
2. Agent analyzes the request and determines needed tools
3. Agent invokes the appropriate tools with relevant parameters
4. Tools execute and return results
5. Agent incorporates results into a natural-language response
6. Response returned to the user

### Built-in tools overview — tool catalog categories
- **Configured** — ready-to-use built-in tools
- **Catalog** — additional tools from a registry, including **MCP servers**
- **Custom** — your own tools via **OpenAPI specifications** or custom implementations

Accessible via **Build > Tools** in the portal or through the VS Code extension.

### Commonly used built-in tools (detail)

**Code Interpreter** — writes/executes Python code in a secure, sandboxed environment. Use cases: math calculations, data analysis, chart generation, file processing, complex problem-solving. Example: computing compound interest on a $10,000 investment at 5% over 10 years.

**File Search** — provides **retrieval-augmented generation (RAG)** over uploaded documents. Indexes documents in a **vector store**, retrieves relevant info at query time, grounding responses in your knowledge base. Supported formats: **PDF, Word (.docx), plain text (.txt), Markdown (.md), and others**. Workflow: create/select a vector store → upload documents → automatic semantic indexing.

**Bing Web Search** — connects agent to real-time internet info (current events, trending topics, beyond training data). Includes **automatic citation generation**.

**Azure AI Search** — advanced knowledge retrieval from your *existing search indexes*. **Distinguishing factor vs. File Search**: File Search works with documents uploaded directly to the agent (Foundry-managed vector store); Azure AI Search connects to enterprise-scale, already-indexed data sources for structured/unstructured search scenarios.

**OpenAPI tools** — agents interact with external APIs defined by **OpenAPI 3.0 specifications**. You provide the spec; Foundry handles parameter mapping and response parsing.

### Additional built-in tools (catalog table)

| Tool | Description |
|---|---|
| Browser Automation | Interact with web pages, fill forms, extract content |
| Computer Use | Interact with desktop applications |
| Image Generation | Create images from text descriptions |
| SharePoint | Access SharePoint content and document libraries |
| Microsoft Fabric | Connect to Fabric data agents for data analytics |
| Deep Research | In-depth research across multiple sources |
| Agent-to-Agent | Delegate tasks to other agents |
| Custom Code Interpreter | Customizable code execution for specialized environments |

Tool catalog continues expanding — check the portal for latest tools.

### Adding tools via the visual designer
1. Open your agent in the Agent Designer
2. Navigate to the **Tools** section
3. Select **Add Tool** or the **+** icon
4. Browse the tool library
5. Select the tool
6. Configure tool-specific settings
7. Save changes

(Adding File Search prompts you to create/select a vector store.)

### Adding tools through YAML — example
```yaml
version: 1.0.0
name: research-assistant
description: Helps with research tasks using code analysis and web search
model:
  id: 'gpt-4o-deployment'
instructions: |
  You're a research assistant helping users gather and analyze information.
  Use Code Interpreter for data analysis and Bing Search for current information.
tools:
  - type: code_interpreter
  - type: bing_grounding
    bing_grounding:
      connection_id: "your-connection-id"
  - type: file_search
    file_search:
      vector_store_ids:
        - "vectorstore-123"
```
Note the tool `type` values: `code_interpreter`, `bing_grounding` (with `connection_id`), `file_search` (with `vector_store_ids`). Some tools require extra parameters (connection IDs, vector store references).

### Model Context Protocol (MCP) servers
**MCP** = standardized way to add custom tools to agents. Available via the **Catalog** section of the tool catalog; offer reusable tool interfaces consistent across agent implementations.

**Three types of MCP servers:**
- **Remote MCP servers** — hosted externally, accessed over the network. Most common for production.
- **Local MCP servers** — run on your local machine during development; useful for testing custom tools before deploying.
- **Custom MCP servers** — your own implementations for specific needs.

**Benefits:** standardized protocol, reusable components, community-driven tools (via MCP registries), simplified integration.

**Using MCP servers in VS Code:**
1. Browse available MCP servers through the extension's tool registry
2. Add MCP servers to your agent configuration
3. Configure server-specific settings/parameters
4. Test MCP server functionality in the integrated playground
5. Deploy agents with MCP server integrations to production

### Tool configuration best practices
- Start with built-in tools before building custom solutions (tested/maintained/optimized)
- Match tools to requirements — don't add tools without clear purpose (each tool adds latency)
- Provide clear instructions on when/when-not to use each tool
- Keep knowledge bases current for File Search
- Test tool behavior thoroughly in the playground (trigger scenarios, verify invocation, test errors)

Agents can combine multiple tools in one workflow (e.g., Bing Web Search + Code Interpreter + File Search), orchestrated automatically.

(Deeper tools/MCP discussion is deferred to later modules.)

## Test, deploy, and integrate agents

### Testing strategies
Both the Foundry portal and VS Code extension provide playgrounds for interactive testing. Testing approaches:
- **Happy path testing** — common/expected requests
- **Edge case testing** — ambiguous inputs, incomplete info, unusual requests
- **Boundary testing** — out-of-scope requests, confirming instructed boundaries are respected
- **Multi-turn conversation testing** — context retention across exchanges
- **Tool invocation testing** — correct tools called at correct times, results incorporated correctly

Record test results to track improvements and catch regressions.

### Deploying agents to your project
Deploying saves agent configuration to your Foundry project for testing/iteration (keeps agent **within your project workspace**).

**From the Foundry portal:**
1. Navigate to your agent
2. Verify configuration and test results
3. Select **Save**
4. Confirm version and deployment settings

**From Visual Studio Code:**
1. Open your agent in the AI Toolkit
2. Select **Save to Foundry**
3. For hosted agents: open the **+Build** menu in developer tools, select **Deploy to Microsoft Foundry**
4. Select container configuration and confirm

### Publishing agents to an endpoint
**Publishing** moves an agent from the project workspace into a managed Azure resource called an **Agent Application** — this makes the agent externally callable via a stable endpoint.

**Key distinction — Deploy vs. Publish:**
- **Deploy** = keeps the agent within your project (team access, testing).
- **Publish** = creates a dedicated external endpoint that consumers can call *without* needing access to your Foundry project.

**What publishing creates:**
- **Agent Application** — Azure resource with its own invocation URL, authentication policy, and **Entra agent identity**.
- **Deployment** — a running instance of a specific agent version inside the application, with start/stop lifecycle management.

**Publishing from the Foundry portal:**
1. Select the agent version to publish
2. Select **Publish** to create the Agent Application and deployment

**Publishing from Visual Studio Code:**
1. Open Command Palette (**Ctrl+Shift+P**), run **Microsoft Foundry: Deploy Hosted Agent** (for hosted agents)
2. Select target workspace and container configuration
3. Confirm and deploy

After publishing, the agent appears in **Hosted Agents (Preview)** in the AI Toolkit extension tree view.

### The Agent Application endpoint
Published agents expose a stable endpoint using the **Responses API** protocol:
```
https://<foundry-resource-name>.services.ai.azure.com/api/projects/<project-name>/applications/<app-name>/protocols/openai/responses
```
The URL stays the same across version rollouts — downstream consumers aren't disrupted.

### Authentication and identity
- Agent Applications authenticate via **Microsoft Entra ID**.
- Callers must have the **Azure AI User** role on the Agent Application resource.
- **API key authentication is NOT supported for Agent Applications.**

**Important (exam-relevant gotcha):** A published agent receives its own dedicated Entra identity, *separate* from the project's shared identity. Permissions do **not** transfer automatically — you must reassign RBAC roles to the new agent identity for any resources it accesses. Skipping this causes tool calls that worked during development to fail with authorization errors post-publish.

### Verifying the endpoint
```azurecli
az account get-access-token --resource https://ai.azure.com
```
```bash
curl -X POST \
  "https://<foundry-resource-name>.services.ai.azure.com/api/projects/<project-name>/applications/<app-name>/protocols/openai/responses?api-version=2025-11-15-preview" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{"input":"Say hello"}'
```
If you get `403 Forbidden`, confirm the caller has the **Azure AI User** role on the Agent Application resource.

### Updating published agents
1. Make/test changes in your dev environment
2. In the Foundry portal, select **Publish Updates** from the Agent playground
3. The Agent Application routes **100% of traffic** to the new version automatically (no gradual rollout described)

Endpoint URL remains unchanged; existing integrations keep working.

### Generating integration code
Via the Microsoft Foundry VS Code extension:
1. Select your deployed agent in **My Resources**
2. Select **View Code**
3. Choose your folder
4. Extension generates code for authenticating, connecting, sending messages, and processing responses

### Integration patterns
- **Web applications** — send messages to the Responses API endpoint, display responses; store conversation history client-side for multi-turn.
- **API-driven workflows** — call agent endpoint from backend services triggered by events/schedules.
- **Chatbot interfaces** — map user sessions to conversations; real-time message exchange.
- **Background automation** — scheduled agent calls for recurring tasks, feeding system data in and processing outputs to update business systems.

### Production considerations
- **Monitoring** — response times, tool invocation success rates, error patterns, token consumption via **Application Insights integration**.
- **Security** — managed identities, least-privilege access, data retention policies.
- **Cost management** — monitor token usage, set response length limits, implement rate limiting.
- **Error handling** — retry logic with exponential backoff for transient failures; handle rate limiting with backoff; validate inputs before sending.
- **Conversation management** — Agent Application endpoints currently support only the **stateless Responses API**; store conversation history client-side for multi-turn experiences. (Note: this contrasts with the earlier claim that the Responses API "securely manages" conversation state at the *project* level — at the *published Agent Application* endpoint level, state is NOT retained server-side, so the calling application must retain history.)

## Exercise - Build and deploy an AI agent

Hands-on exercise (~30 minutes): build and deploy an AI agent using Microsoft Foundry Agent Service — create an agent, configure instructions and tools, connect via the VS Code extension, and use the agent in an app. Requires an Azure subscription (free account offers credits for the first 30 days). No additional technical content beyond what's covered in units 2–8; exercise is a practical lab, not new exam facts. Reminder to delete Azure resources after completing the exercise to avoid ongoing charges.

## Knowledge check

The module's official knowledge check (4 questions) confirms these key facts:

1. **Primary benefit of Foundry Agent Service vs. standard APIs:** It handles tool calling, state management, and infrastructure automatically (NOT: more powerful models / no subscription needed / portal-only).
2. **How Foundry Agent Service handles conversation state:** Through the **Responses API**, which automatically manages conversation context (NOT: manual history management / external DB / local file storage).
3. **NOT a recommended security practice:** "Allowing agents unrestricted access to all enterprise data" is the incorrect/bad practice (contrasted with RBAC, prompt filtering/validation, and comprehensive logging/traceability, which ARE recommended).
4. **When an agent determines it needs a tool:** It automatically invokes the tool, processes results, and incorporates them into its response (NOT: asks user permission / stops and waits for developer / sends to a separate queue).

## Summary

Recap of the module: AI agents defined and motivated; two primary agent types — **declarative agents** (configured via visual designers and YAML: prompt-based single agent or workflow multi-agent) and **hosted agents** (created/deployed through code). Built agents via both the Foundry portal and the VS Code extension. Configured agents with clear instructions. Extended capabilities via the tool catalog (Code Interpreter, File Search, Bing Web Search, Azure AI Search, and more). Tested via integrated playgrounds, deployed to production, and generated integration code to connect agents to applications.
