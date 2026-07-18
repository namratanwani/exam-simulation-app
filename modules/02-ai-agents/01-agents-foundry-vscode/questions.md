# Practice questions — Develop AI agents with Microsoft Foundry and Visual Studio Code

## Introduction

**Q1.** A healthcare organization wants to automate patient interactions while maintaining enterprise-grade security and without managing underlying compute or storage resources. Which Azure/Microsoft service is purpose-built for this scenario?
A. Azure Logic Apps
B. Microsoft Foundry Agent Service
C. Azure Functions Premium plan
D. Azure Bot Service Standard channel
**Answer:** B — Microsoft Foundry Agent Service is a fully managed platform for building, deploying, and scaling AI agents without managing compute/storage, with enterprise-grade security built in. Logic Apps and Azure Functions are general-purpose automation/compute services, not agent-specific platforms.

**Q2.** Which two development surfaces does this module teach for building AI agents with Microsoft Foundry Agent Service? (Choose two.)
A. The Foundry portal (ai.azure.com)
B. Azure Data Studio
C. The Microsoft Foundry extension for Visual Studio Code
D. Azure Cloud Shell
**Answer:** A, C — The module explicitly teaches building agents via the Foundry portal and via the Microsoft Foundry extension for Visual Studio Code. Azure Data Studio and Cloud Shell aren't agent development surfaces covered in this module.

**Q3.** Which of the following is explicitly listed as a prerequisite for this module?
A. Advanced Python programming experience
B. Familiarity with Azure and the Azure portal
C. A completed Azure AI Engineer certification
D. Experience with Kubernetes
**Answer:** B — The stated prerequisites are familiarity with Azure and the Azure portal, an understanding of generative AI, and basic familiarity with Visual Studio Code. Python experience, a prior certification, and Kubernetes are not listed.

**Q4.** The module offers both video and text formats. What does the introduction note about the relationship between them?
A. The video format contains more detail than the text format
B. The text format contains greater detail than the video, and may be used as supplemental material
C. Only the text format is available; there is no video
D. The two formats contain completely unrelated content
**Answer:** B — The module states the text contains greater detail than the video presentation, so you might refer to it as supplemental material.

**Q5.** Which of the following is one of the module's seven stated learning objectives?
A. Migrate on-premises databases to Azure SQL
B. Extend agent capabilities with tools and functions
C. Configure Azure Kubernetes Service networking
D. Design a disaster recovery plan for AI workloads
**Answer:** B — "Extend agent capabilities with tools and functions" is explicitly listed among the seven learning objectives. The other options are unrelated to this module's scope.

**Q6.** Per the introduction, what can Microsoft Foundry Agent Service let you do without managing underlying infrastructure?
A. Build, deploy, and scale AI agents without managing underlying compute and storage resources
B. Provision virtual machines without an Azure subscription
C. Automatically migrate legacy chatbots to a new tenant
D. Bypass all Azure RBAC requirements
**Answer:** A — The introduction defines Foundry Agent Service as a fully managed platform that empowers you to build, deploy, and scale AI agents without managing underlying compute and storage resources.

## Understand AI agents and Microsoft Foundry Agent Service

**Q7.** What primarily distinguishes an AI agent from a simple chat model, according to this module?
A. AI agents only work within Microsoft 365
B. AI agents use advanced algorithms and machine learning to analyze data and make decisions autonomously, rather than only generating text
C. AI agents cannot maintain conversation context
D. AI agents require no generative AI model
**Answer:** B — Unlike simple chat models that only generate text, agents analyze data and make informed decisions autonomously, understanding context and taking actions toward goals.

**Q8.** A development team is deploying an AI agent that will have access to a CRM system. Which security risk category from this module describes the scenario where weak authentication lets the agent perform admin-level actions like exporting or deleting records?
A. Data poisoning
B. Unauthorized access and privilege escalation
C. Model inversion and output leakage
D. Supply chain vulnerabilities
**Answer:** B — Unauthorized access and privilege escalation is defined as weak authentication/access controls letting agents (or bad actors controlling them) access systems they shouldn't, with the CRM export/delete example given directly in the module.

**Q9.** Which of the following is explicitly listed as a mitigation strategy for AI agent security risks in this module? (Choose three.)
A. Enforcing role-based access controls (RBAC) and least privilege
B. Gating sensitive operations behind human-in-the-loop approvals
C. Disabling all logging to reduce storage costs
D. Maintaining comprehensive logging and traceability for all agent actions
**Answer:** A, B, D — RBAC/least privilege, human-in-the-loop approval gates, and comprehensive logging/traceability are all listed mitigation strategies. Disabling logging is the opposite of the recommended practice (inadequate logging is itself listed as a risk area).

**Q10.** Approximately how many lines of code does Microsoft Foundry Agent Service claim to reduce agent-building effort to, compared to using standard APIs directly?
A. Fewer than 10
B. Fewer than 50
C. Fewer than 500
D. Fewer than 5,000
**Answer:** B — The module states agents can be built via the portal or in your own applications with fewer than 50 lines of code, versus the significant coding effort previously required with standard APIs.

**Q11.** Which statement correctly distinguishes declarative agents from hosted agents in Microsoft Foundry?
A. Declarative agents are containerized and created in code; hosted agents are defined through configuration
B. Declarative agents are defined through configuration (visual designer or YAML); hosted agents are containerized agents created and deployed in code
C. Declarative agents cannot use tools; hosted agents can
D. There is no functional difference between the two
**Answer:** B — Declarative agents are configuration-driven (prompt-based or workflow YAML); hosted agents are containerized and created/deployed via code, with the Foundry platform managing the infrastructure.

**Q12.** Within declarative agents, what is the key difference between a prompt-based agent and a workflow agent?
A. Prompt-based agents are multi-agent orchestrations; workflow agents are single agents
B. A prompt-based agent is a single agent configured with a model, instructions, tools, and prompts; a workflow agent is a multi-agent orchestration defined in YAML
C. Workflow agents cannot be configured in YAML
D. Prompt-based agents require custom code; workflow agents do not
**Answer:** B — Prompt-based = single agent (model + instructions + tools + prompts), the most common and module's focus. Workflow agents = multi-agent orchestrations defined in YAML for agents collaborating on complex tasks.

**Q13.** How does Microsoft Foundry Agent Service manage conversation state for agents, according to the module?
A. Developers must manually persist conversation history to a database
B. Conversation states are securely managed through the Responses API
C. State is stored only in browser cookies
D. State management is not supported
**Answer:** B — The module explicitly states conversation states are securely managed through the Responses API, removing the need for manual state management (at the project/agent-playground level).

**Q14.** Which of the following is NOT listed as a key feature of Microsoft Foundry Agent Service?
A. Automatic tool calling
B. Extensive tool catalog
C. Mandatory use of API keys for all authentication
D. Enterprise-grade security with keyless authentication
**Answer:** C — The module lists automatic tool calling, an extensive tool catalog, and enterprise-grade security with keyless authentication as key features. Mandatory API-key authentication is not listed as a feature — the platform emphasizes keyless authentication instead.

## Explore development approaches

**Q15.** A team wants centralized management of agents across projects and a way for non-technical stakeholders to review agent configurations visually. Which development approach best fits this need?
A. Azure CLI scripting
B. The Foundry portal
C. The Microsoft Foundry extension for Visual Studio Code
D. Azure Resource Manager templates
**Answer:** B — The Foundry portal is designed for visual configuration, centralized management, and team collaboration with stakeholders who prefer visual interfaces, per the module's "When to use the Foundry portal" section.

**Q16.** Which of the following are listed as reasons to prefer the Visual Studio Code extension over the Foundry portal? (Choose two.)
A. Version control integration (tracking agent configs in Git)
B. It is the only approach that supports testing agents
C. Code-first development via direct YAML editing
D. It eliminates the need for a Microsoft Foundry project
**Answer:** A, C — VS Code is favored for version control integration and code-first/YAML-based development. Both approaches support testing via playgrounds (B is false), and both require a Foundry project (D is false).

**Q17.** In the Microsoft Foundry VS Code extension, which section would you look in to find "Vector stores" and "Connections"?
A. Tools
B. Resources
C. Help and Feedback
D. Model Catalog
**Answer:** B — The Resources section covers deployed models, declarative agents, hosted agents, connections, and vector stores. Tools covers Model Catalog, Model Playground, Agent Playgrounds, Local Visualizer, and Deploy Hosted Agents.

**Q18.** Which Azure resource(s) are described as REQUIRED (not optional) to develop agents with Microsoft Foundry Agent Service? (Choose two.)
A. Microsoft Foundry project
B. Azure Key Vault
C. Model deployments (e.g., GPT-4.1 or Claude Sonnet 4.6)
D. Azure Functions
**Answer:** A, C — A Microsoft Foundry project and model deployments are the required resources. Azure Key Vault and Azure Functions are listed as optional services depending on agent capabilities.

**Q19.** Which optional Azure service would you add specifically to enable custom tool implementations and business logic for an agent?
A. Azure Key Vault
B. Azure Storage
C. Azure Functions
D. Azure AI Search
**Answer:** C — Azure Functions is listed as the optional service for custom tool implementations and business logic. Azure Key Vault is for secrets, Azure Storage for files, and Azure AI Search for advanced knowledge retrieval.

**Q20.** What is the typical development workflow step that comes immediately after "Add tools" in the module's described agent-building process?
A. Deploy the agent to production
B. Test the agent using integrated playgrounds
C. Publish the agent to an endpoint
D. Connect to your Microsoft Foundry project
**Answer:** B — The workflow sequence is: Connect → Create → Configure instructions → Add tools → Test → Iterate → Deploy → Integrate. Testing directly follows adding tools.

## Build your first agent in Microsoft Foundry

**Q21.** In the Foundry portal, which menu path do you use to begin creating a new agent?
A. Build > Tools
B. Build > Agents, then select Create
C. Settings > Agents
D. Resources > Deployments
**Answer:** B — The module specifies: select Build > Agents in the left navigation, then select Create to start building a new agent.

**Q22.** Which model parameter controls response randomness, and which controls response diversity, respectively?
A. Top P controls randomness; Temperature controls diversity
B. Temperature controls randomness; Top P controls diversity
C. Both control the same thing
D. Neither is configurable in the Foundry portal
**Answer:** B — Temperature controls response randomness; Top P controls response diversity. Both are exposed in the portal (and later, in more detail, in the VS Code Agent Designer).

**Q23.** In the Foundry portal's tool catalog, which category contains tools like Code Interpreter and File Search that are ready to use immediately without additional setup?
A. Catalog
B. Custom
C. Configured
D. Marketplace
**Answer:** C — "Configured" is the category for built-in tools ready to use immediately. "Catalog" holds additional addable tools (e.g., Bing Web Search, Azure AI Search, SharePoint), and "Custom" holds tools added via OpenAPI specs or MCP servers.

**Q24.** After deploying an agent from the Foundry portal, through which mechanisms can you access the agent, per the module?
A. Only through the Foundry portal playground
B. Through the Microsoft Foundry SDK or REST APIs
C. Only via Azure CLI
D. Agents cannot be accessed programmatically after deployment
**Answer:** B — The module states that after deployment, you can access the agent through the Microsoft Foundry SDK or REST APIs.

**Q25.** Which of the following is one of the three fields you fill in under "Enter agent details" when creating an agent in the Foundry portal?
A. Vector store ID
B. Model (select a deployed model, or deploy a new one)
C. Entra tenant ID
D. Deployment region only
**Answer:** B — The three fields are Name, Description, and Model (select a deployed model from the dropdown, or deploy a new model). Vector store ID and tenant ID are not part of initial agent creation.

**Q26.** What does the Foundry portal's playground maintain during your testing session, allowing you to test multi-turn interactions?
A. Conversation history
B. Billing history
C. Deployment logs only
D. Nothing is retained between messages
**Answer:** A — The module states the playground maintains conversation history during your session, allowing you to test multi-turn interactions and verify the agent maintains context appropriately.

## Set up Visual Studio Code for agent development

**Q27.** What is the correct keyboard shortcut to open the Extensions pane in VS Code on a Mac, as referenced in this module?
A. Cmd+Shift+P
B. Cmd+Shift+X
C. Cmd+Shift+E
D. Cmd+Shift+A
**Answer:** B — The module specifies Ctrl+Shift+X (Windows/Linux) or Cmd+Shift+X (Mac) to open Extensions.

**Q28.** After installing the Microsoft Foundry extension and connecting your Azure account, what must you do to link a specific Foundry project to the extension?
A. Run `az foundry connect` in the integrated terminal
B. Right-click your Microsoft Foundry project in the Azure Resources pane and select "Open in Foundry Extension"
C. Manually enter the project's connection string in settings.json
D. Restart VS Code — projects link automatically with no user action
**Answer:** B — The module's steps: expand your Azure subscription, expand the Foundry section, right-click your Microsoft Foundry project, and select "Open in Foundry Extension."

**Q29.** When deploying a new model in the VS Code extension's Resources > Model deployments section, which of the following are configurable settings? (Choose two.)
A. Deployment name
B. Model version
C. Vector store ID
D. Capacity settings
**Answer:** A, D — Deployment name and Capacity settings are both configurable (Model version is also listed but only two answers were requested here). Vector store ID is unrelated to model deployment — it belongs to File Search tool configuration.

**Q30.** True or false framed as MC: Once an agent is created in the Foundry portal, changes made to it in VS Code cannot be saved back to Foundry.
A. True — VS Code changes are local-only and never sync back
B. False — changes made in VS Code can be saved directly back to Foundry
C. True, unless the agent is a hosted agent
D. False, but only for workflow agents
**Answer:** B — The module states: "Changes to agents in VS Code can be saved directly to Foundry, so you can work with your agent across platforms."

**Q31.** After installing the Microsoft Foundry extension, where does its icon appear in VS Code?
A. In the Settings menu only
B. In the VS Code activity bar
C. In the terminal panel
D. It does not appear anywhere visibly
**Answer:** B — The module states that after installation, the Microsoft Foundry icon appears in the VS Code activity bar on the left side of the window.

**Q32.** Which example models does the module mention when describing how to deploy a model from the VS Code extension's Resources > Model deployments section?
A. GPT-4o or GPT-4
B. Claude Opus or Claude Haiku only
C. Llama 3 or Mistral only
D. DALL-E 3 only
**Answer:** A — The module gives GPT-4o or GPT-4 as example models to choose from when creating a new deployment in the extension.

## Configure and manage agents in Visual Studio Code

**Q33.** A developer sets an agent's Temperature to 0.9 for a customer-facing structured business task that requires consistent, predictable responses. Is this configuration appropriate per the module's guidance?
A. Yes, higher temperature always improves customer satisfaction
B. No — for structured business tasks, values between 0.3 and 0.7 typically work well; 0.9 falls in the higher/more creative-and-varied range
C. Yes, because Top P should be adjusted instead of Temperature
D. No, because Temperature must always be set to exactly 1.0
**Answer:** B — The module recommends 0.3–0.7 for structured business agent tasks; values 0.7–1.0 generate more creative, varied (less consistent) responses, which is generally undesirable for structured tasks.

**Q34.** What is the default value for Top P mentioned in the module, and what does it control?
A. Default 0.5; controls temperature
B. Default 1.0; limits vocabulary choices during generation, controlling diversity
C. Default 0; disables all randomness
D. There is no default; it must always be manually set
**Answer:** B — Top P's default is 1.0, and it controls diversity by limiting vocabulary choices during generation. Most scenarios work well with the default.

**Q35.** In the agent YAML schema shown in the module, which field holds the auto-generated unique identifier used when calling the agent through APIs?
A. `metadata.tags`
B. `id`
C. `model.id`
D. `name`
**Answer:** B — The YAML example shows `id: 'agent-abc123xyz'` as the agent's unique identifier field, separate from `model.id` (which identifies the underlying deployed model, e.g. `'gpt-4.1'`).

**Q36.** Which YAML top-level keys appear in the module's complete agent YAML example? (Choose three.)
A. `instructions`
B. `endpoints`
C. `tools`
D. `metadata`
**Answer:** A, C, D — The example includes `version`, `name`, `description`, `id`, `metadata`, `model`, `instructions`, and `tools`. There is no `endpoints` top-level key in the declarative agent YAML schema shown.

**Q37.** According to the module's best practices, what should you do BEFORE adding complexity to an agent's instructions?
A. Deploy the agent to production immediately
B. Start simple, then iterate based on testing results
C. Add every available tool to maximize capability
D. Disable YAML validation to speed up editing
**Answer:** B — "Start simple, then iterate" is an explicit best practice: begin with basic instructions and add complexity based on testing results, since overly complex initial instructions are harder to debug.

**Q38.** True/false-style MC: The configuration workflow described in this unit (Agent Designer, YAML properties like `model`, `instructions`, `tools`) applies equally to hosted agents and workflow agents without modification.
A. True — all three agent types share one identical schema
B. False — this workflow applies to declarative prompt-based agents; hosted agents are configured through code, and workflow agents use a different YAML schema for multi-agent orchestration
C. True, but only for hosted agents
D. False — none of the three agent types can be configured via YAML
**Answer:** B — The module's explicit note states the configuration workflow described applies to declarative prompt-based agents specifically; hosted agents use code, and workflow agents use a different multi-agent YAML schema.

## Extend agent capabilities with tools

**Q39.** Which tool would you use to have an agent compute the exact compound interest on a $10,000 investment via executed code, rather than an approximated language-model answer?
A. File Search
B. Code Interpreter
C. Bing Web Search
D. OpenAPI tools
**Answer:** B — Code Interpreter writes and executes Python code in a sandboxed environment for tasks like mathematical calculations — the module gives this exact compound-interest example.

**Q40.** What is the key distinguishing factor between File Search and Azure AI Search as agent tools?
A. File Search supports images only; Azure AI Search supports text only
B. File Search works with documents uploaded directly to the agent (indexed into a Foundry-managed vector store); Azure AI Search connects to your existing enterprise-scale indexed data sources
C. Azure AI Search is deprecated in favor of File Search
D. There is no functional difference between them
**Answer:** B — This is the explicit distinguishing factor given in the module: File Search = documents uploaded directly to the agent and indexed in a vector store; Azure AI Search = connects to existing, already-indexed enterprise search sources.

**Q41.** Which file formats does the module explicitly say File Search supports? (Choose three.)
A. PDF
B. Word (.docx)
C. Markdown (.md)
D. Executable (.exe)
**Answer:** A, B, C — The module lists PDF, Word (.docx), plain text (.txt), Markdown (.md), and other formats. Executable files are not a supported/relevant format for RAG document search.

**Q42.** An agent needs to answer questions using information from a public API defined by an OpenAPI 3.0 specification. Which tool type should be configured?
A. Code Interpreter
B. OpenAPI tools
C. Bing Web Search
D. Agent-to-Agent
**Answer:** B — OpenAPI tools let agents interact with external APIs defined by OpenAPI 3.0 specs; you supply the spec and Foundry handles parameter mapping and response parsing.

**Q43.** Which built-in tool provides automatic citation generation when it retrieves information?
A. Code Interpreter
B. Bing Web Search
C. SharePoint
D. Microsoft Fabric
**Answer:** B — Bing Web Search connects the agent to real-time internet info and includes automatic citation generation so the agent can reference its sources.

**Q44.** In the YAML tool configuration example, what parameter is required under the `file_search` tool type to specify which indexed document collection the agent should query?
A. `connection_id`
B. `vector_store_ids`
C. `document_path`
D. `search_index_name`
**Answer:** B — The example shows `type: file_search` with a nested `file_search.vector_store_ids` list (e.g., `"vectorstore-123"`). `connection_id` is instead used under `bing_grounding`.

**Q45.** Which of the following are types of MCP servers described in the module? (Choose three.)
A. Remote MCP servers
B. Local MCP servers
C. Custom MCP servers
D. Federated MCP servers
**Answer:** A, B, C — The module describes exactly three types: Remote (hosted externally, most common for production), Local (run on your machine during development/testing), and Custom (your own implementations). "Federated" is not a term used in the module.

**Q46.** A developer wants to delegate a subtask from one agent to another agent automatically. Which built-in tool from the catalog table supports this?
A. Deep Research
B. Agent-to-Agent
C. Browser Automation
D. Computer Use
**Answer:** B — The Agent-to-Agent tool is listed in the catalog table as enabling delegation of tasks to other agents.

**Q47.** Per the module's tool configuration best practices, why should you avoid adding tools to an agent without a clear purpose?
A. Because the Foundry portal limits agents to exactly 3 tools
B. Because each tool adds latency
C. Because tools cannot be removed once added
D. Because unused tools automatically disable the agent
**Answer:** B — The module explicitly warns: "Don't add tools without clear purposes, as each tool adds latency."

## Test, deploy, and integrate agents

**Q48.** Which testing approach specifically verifies that an agent respects the boundaries defined in its instructions when given out-of-scope requests?
A. Happy path testing
B. Boundary testing
C. Multi-turn conversation testing
D. Tool invocation testing
**Answer:** B — Boundary testing confirms the agent respects instructed boundaries by testing out-of-scope requests, distinct from happy-path (expected requests) and multi-turn (context retention) testing.

**Q49.** What is the key distinction between "deploying" and "publishing" an agent in Microsoft Foundry?
A. They are the same operation with different names
B. Deploying keeps the agent within your project workspace; publishing creates a dedicated externally callable endpoint (Agent Application) that doesn't require access to your Foundry project
C. Publishing is only available in the Foundry portal, never in VS Code
D. Deploying requires an Entra identity; publishing does not
**Answer:** B — Deploying saves the agent configuration within the project for team testing/iteration. Publishing creates an Agent Application — a managed Azure resource with its own invocation URL — making the agent externally callable without requiring Foundry project access.

**Q50.** What two artifacts does Foundry create when you publish an agent version? (Choose two.)
A. An Agent Application (its own invocation URL, auth policy, and Entra agent identity)
B. A Deployment (a running instance of a specific agent version with start/stop lifecycle management)
C. A new Azure subscription
D. A dedicated virtual network
**Answer:** A, B — Publishing creates an Agent Application (Azure resource with URL/auth/identity) and a Deployment (running instance of a specific version with lifecycle management). No new subscription or VNet is created.

**Q51.** Which authentication mechanism is used for Agent Application endpoints, and which is explicitly NOT supported?
A. API keys are used; Entra ID is not supported
B. Microsoft Entra ID is used; API key authentication is NOT supported
C. Both API keys and Entra ID are equally supported
D. Anonymous access is allowed by default
**Answer:** B — The module states Agent Applications use Microsoft Entra ID for authentication, and explicitly notes "API key authentication isn't supported for Agent Applications."

**Q52.** Which RBAC role must a caller have on the Agent Application resource to successfully invoke the published endpoint?
A. Contributor
B. Azure AI User
C. Owner
D. Cognitive Services Contributor
**Answer:** B — The module specifies callers must have the Azure AI User role on the Agent Application resource; a 403 Forbidden response indicates this role is missing.

**Q53.** A team publishes an agent that previously worked fine in development, calling Azure AI Search and Azure Functions tools. After publishing, all tool calls fail with authorization errors. What is the MOST LIKELY cause, per the module's guidance?
A. The Responses API was deprecated
B. The published agent received its own dedicated Entra identity separate from the project's shared identity, and RBAC roles for accessed resources weren't reassigned to it
C. The agent's Temperature was set too high
D. The vector store was deleted during publishing
**Answer:** B — The module's "Important" callout warns that publishing gives the agent a new dedicated Entra identity; permissions don't transfer automatically, so you must reassign RBAC roles to the new identity or tool calls fail with authorization errors.

**Q54.** When you publish updates to an already-published agent, what traffic-routing behavior does the Agent Application exhibit?
A. It splits traffic 50/50 between old and new versions
B. It routes 100% of traffic to the new version automatically
C. It requires manual DNS changes to redirect traffic
D. It creates a brand-new endpoint URL for the updated version
**Answer:** B — Selecting "Publish Updates" causes the Agent Application to route 100% of traffic to the new version automatically, while the endpoint URL remains unchanged so existing integrations keep working.

**Q55.** Which API protocol do published Agent Application endpoints use, and what state-management limitation does this impose?
A. GraphQL; requires a persistent WebSocket connection
B. The Responses API; endpoints currently support only the stateless Responses API, so conversation history must be stored client-side for multi-turn experiences
C. SOAP; state is stored automatically server-side indefinitely
D. gRPC; no state management is possible at all
**Answer:** B — Published endpoints use the Responses API protocol but support only its stateless mode — conversation history must be stored in the client for multi-turn interactions, unlike the project-level playground where state is described as automatically managed.

**Q56.** Which Azure monitoring integration does the module cite for tracking response times, tool invocation success rates, and token consumption in production?
A. Azure Monitor Workbooks only
B. Application Insights integration
C. Log Analytics agent extension
D. Azure Advisor
**Answer:** B — The module specifies tracking these metrics "using Application Insights integration" under Production considerations.

## Exercise - Build and deploy an AI agent

**Q57.** Approximately how long is the "Build and deploy an AI agent" exercise estimated to take?
A. 5 minutes
B. 30 minutes
C. 3 hours
D. 1 minute
**Answer:** B — The exercise unit lists an estimated duration of 30 minutes.

**Q58.** Which of the following activities does the exercise unit describe you performing? (Choose three.)
A. Create an agent and configure its instructions and tools
B. Connect with the Visual Studio Code extension
C. Use your agent in an app
D. Manually train a new foundation model from scratch
**Answer:** A, B, C — The exercise has you create an agent, configure instructions and tools, connect via the VS Code extension, and use the agent in an app. Training a foundation model from scratch is outside the scope of Foundry agent development, which consumes already-deployed models rather than training new ones.

**Q59.** What resource does Microsoft offer to those without an existing Azure subscription who want to complete the exercise?
A. A permanent free-tier Foundry project with no expiration
B. A free account sign-up that includes credits for the first 30 days
C. A one-time voucher redeemable only for compute, not storage
D. No accommodation is offered — a paid subscription is mandatory
**Answer:** B — The exercise unit notes you can sign up for an Azure account, which includes credits for the first 30 days, if you don't already have a subscription.

**Q60.** What does the module recommend you do after finishing the exercise if you're done exploring Foundry Agents?
A. Leave resources running in case you return later
B. Delete the Azure resources created during the exercise
C. Export the agent to a different cloud provider
D. Convert the agent to a hosted agent before deleting anything
**Answer:** B — The module's tip explicitly recommends deleting the Azure resources you created during the exercise once you're finished, to avoid ongoing costs.

**Q61.** The exercise is launched via an external link rather than performed inline in the Learn module page. What is the practical implication of this for exam preparation? [general Azure knowledge]
A. The exercise content itself introduces new exam facts not covered elsewhere in the module
B. The exercise is a hands-on lab reinforcing units 2–8's concepts (agent creation, configuration, tools, testing, deployment) rather than introducing new testable facts
C. The exercise replaces the need to read any other unit
D. The exercise only covers Azure billing, unrelated to agents
**Answer:** B — The exercise applies the concepts already taught in prior units (create, configure, add tools, connect via VS Code, deploy/use in an app) hands-on; it doesn't introduce distinct new technical facts beyond what's in units 2–8.

**Q62.** Which Azure entry point does the exercise reference for signing up if you need a subscription to explore Microsoft Foundry?
A. portal.azure.com directly, with no separate signup flow
B. The Azure free account sign-up page (azure.microsoft.com pricing/purchase-options)
C. A GitHub Education pack
D. The Microsoft Learn sandbox only, no external signup needed
**Answer:** B — The exercise unit links to the Azure account sign-up page, noting it includes credits for the first 30 days, for users without an existing subscription.

## Knowledge check

**Q63.** Per the module's own knowledge check, what is the primary benefit of Microsoft Foundry Agent Service compared to building agents with standard APIs?
A. It provides access to more powerful AI models
B. It handles tool calling, state management, and infrastructure automatically
C. It requires no Azure subscription
D. It only works with the Azure portal
**Answer:** B — This is the module's stated correct answer: automatic handling of tool calling, state management, and infrastructure, versus the significant manual coding effort standard APIs require.

**Q64.** Per the module's knowledge check, which of the following is explicitly called out as NOT a recommended security practice for AI agents?
A. Using role-based access controls
B. Implementing prompt filtering and validation
C. Allowing agents unrestricted access to all enterprise data
D. Maintaining comprehensive logging and traceability
**Answer:** C — Unrestricted access directly contradicts the least-privilege and RBAC principles emphasized throughout the module; the other three options are all explicitly recommended practices.

**Q65.** Per the module's knowledge check, how does Microsoft Foundry Agent Service handle conversation state?
A. By requiring developers to manually manage conversation history
B. Through external database connections configured by the developer
C. Through the Responses API, which automatically manages conversation context
D. Using local file storage on the client device
**Answer:** C — The knowledge check confirms conversation state is handled through the Responses API, which automatically manages conversation context.

**Q66.** Per the module's knowledge check, what happens when an agent determines it needs a tool to respond to a user request?
A. The agent asks the user for permission to use the tool
B. The agent stops processing and waits for developer input
C. The agent automatically invokes the tool, processes results, and incorporates them into its response
D. The agent sends the request to a separate processing queue
**Answer:** C — The knowledge check confirms the tool-calling lifecycle is automatic: the agent invokes the tool, processes results, and incorporates them into its response without pausing for user or developer intervention.

**Q67.** Among the distractor options offered in the knowledge check's first question ("primary benefit of Foundry Agent Service"), which statements are factually incorrect? (Choose two.)
A. It requires no Azure subscription
B. It handles tool calling, state management, and infrastructure automatically
C. It only works with the Azure portal
D. It provides access to more powerful AI models
**Answer:** A, C — Foundry Agent Service does require an Azure subscription, and it supports both the Foundry portal and the VS Code extension (not portal-only), so both are incorrect distractors. B is the correct answer, and D is also incorrect since the benefit is about workflow simplification, not inherently "more powerful" models.

**Q68.** How many questions does the module's knowledge check unit contain, and what topic areas do they cover?
A. 10 questions covering pricing tiers
B. 4 questions covering Foundry Agent Service benefits, conversation state handling, security practices, and tool invocation behavior
C. 2 questions covering only YAML syntax
D. 6 questions covering deployment regions
**Answer:** B — The knowledge check unit contains exactly 4 questions: the primary benefit of Foundry Agent Service vs. standard APIs, how conversation state is handled, which security practice is NOT recommended, and what happens when an agent needs a tool.

## Summary

**Q69.** Which tool examples does the module summary highlight as transforming agents from simple chat interfaces into sophisticated automation systems? (Choose three.)
A. Code Interpreter
B. File Search
C. Bing Web Search
D. Azure Kubernetes Service
**Answer:** A, B, C — The summary explicitly names Code Interpreter, File Search, and Bing Web Search (along with Azure AI Search and "many more") as the built-in tools that transform chat interfaces into automation systems. Azure Kubernetes Service is unrelated infrastructure, not an agent tool.

**Q70.** Which capability does the module summary say allows connecting agents to applications after testing and deployment?
A. Manually rewriting the application from scratch
B. Generated integration code via the VS Code extension
C. Only the Foundry portal's built-in chatbot widget
D. A dedicated mobile app SDK
**Answer:** B — The summary states you "generated integration code to connect agents with your applications," referring to the VS Code extension's code-generation capability (View Code) covered in the "Test, deploy, and integrate agents" unit.

**Q71.** Per the module summary, what are the two primary agent types recapped?
A. Prompt-based and workflow agents only
B. Declarative agents (configured via visual designers and YAML) and hosted agents (created and deployed through code)
C. Public agents and private agents
D. Synchronous and asynchronous agents
**Answer:** B — The summary recaps the two primary agent types as declarative agents (configured through visual designers and YAML) and hosted agents (created and deployed through code); prompt-based and workflow are the two forms of declarative agents specifically, not the top-level split.

**Q72.** Which two development approaches does the summary recap as having been covered in the module?
A. Azure Data Factory and Azure Synapse
B. The visual Foundry portal and the developer-focused VS Code extension
C. Power Automate and Logic Apps
D. Bicep and Terraform
**Answer:** B — The summary recaps building agents using "both the visual Foundry portal and the developer-focused VS Code extension," understanding when each approach fits best.

**Q73.** Per the summary, what did you do immediately after configuring agents with clear instructions defining their behavior and personality?
A. Immediately deleted the agent
B. Extended agent capabilities using the tool catalog
C. Migrated the agent to a different subscription
D. Disabled all tools to reduce cost
**Answer:** B — The summary's narrative sequence is: configure instructions → extend capabilities using the tool catalog → test using integrated playgrounds → deploy to production → generate integration code.

**Q74.** According to the summary, besides Code Interpreter, File Search, and Bing Web Search, which other tool is explicitly named as part of the tool catalog that transforms chat interfaces into automation systems?
A. Azure AI Search
B. Azure Kubernetes Service
C. Azure DevOps
D. Azure Bastion
**Answer:** A — The summary explicitly lists Azure AI Search alongside Code Interpreter, File Search, and Bing Web Search ("and many more") as built-in tools available through the tool catalog.
