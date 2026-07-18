# Practice questions — Integrate your agent with Microsoft 365

## Introduction

**Q1.** According to the module introduction, which Microsoft Foundry capability allows users to interact with a custom agent directly inside Microsoft Teams and Microsoft 365 Copilot without switching applications?
A. A built-in publishing capability that deploys the agent to those surfaces
B. A manual export of the agent's system prompt into a Teams bot template
C. A Power Automate flow that polls the Foundry API on a schedule
D. A Logic App connector that screen-scrapes the Foundry playground
**Answer:** A — Microsoft Foundry provides built-in capabilities to publish agents directly to Microsoft Teams and Microsoft 365 Copilot; the other options describe workarounds not mentioned in the module.

**Q2.** Per the module prerequisites, which of the following is explicitly required before starting this module? (Choose two.)
A. Experience building agents in Microsoft Foundry
B. A Microsoft 365 subscription with access to Teams
C. An active Power BI Premium capacity
D. A Microsoft Copilot Studio license
**Answer:** A, B — The module lists familiarity with Azure, experience building Foundry agents, and an M365 subscription with Teams access as prerequisites. Power BI Premium and Copilot Studio licenses are not mentioned.

## Understand Foundry agent publishing options

**Q3.** When you publish a Foundry agent, what resource does Microsoft Foundry create to give it a dedicated invocation URL, a distinct identity, and user data isolation?
A. A Foundry Hub
B. An Agent Application
C. A Foundry Connection
D. An Azure AI Search index
**Answer:** B — Publishing creates an "Agent Application" resource with a dedicated invocation URL, its own Entra identity, and per-user data isolation. A Foundry Hub and Connection are project-level constructs unrelated to publish-time identity.

**Q4.** What happens to the public invocation URL when you publish a new version of an already-published agent?
A. A new URL is generated and the old one is deprecated after 30 days
B. The URL stays the same; the Agent Application routes traffic to the updated deployment
C. The URL changes only if the publish scope is Organization
D. The URL is regenerated but the old one keeps working indefinitely
**Answer:** B — The Agent Application acts as a routing layer, so publishing a new version routes traffic to the updated deployment without changing the public endpoint.

**Q5.** Which THREE actions occur specifically when you publish a Foundry agent to Microsoft 365? (Choose three.)
A. Creates an Azure Bot Service resource that routes messages between Microsoft 365 and the agent
B. Registers a Microsoft Entra ID application for authentication
C. Generates a Microsoft 365 publishing package for distribution
D. Automatically provisions an Azure Cosmos DB account for conversation history
**Answer:** A, B, C — Publishing to Microsoft 365 creates an Azure Bot Service resource, registers an Entra ID app, and generates a publishing package, and also makes the agent discoverable in the Teams agent store. Cosmos DB provisioning is not part of this workflow per the module.

**Q6.** A team wants to expose a Foundry agent to users outside Microsoft 365, embedded in a custom web application via REST calls. Which publishing option should they use?
A. Web application preview only
B. Stable API endpoint
C. Organization-scope Teams publish
D. Microsoft 365 Agents Toolkit proxy only
**Answer:** B — The module lists "Stable API endpoint" as the channel specifically described as a REST API for embedding in custom applications, distinct from the demo-oriented web application preview.

**Q7.** Which of the following are listed as "Other publishing channels" available via Azure Bot Service, besides Microsoft 365? (Choose two.)
A. Slack
B. Twilio (SMS)
C. WhatsApp Business Platform
D. Salesforce Chat
**Answer:** A, B — The module explicitly lists Slack, Telegram, Twilio (SMS), Facebook, and others as Azure Bot Service channels. WhatsApp Business Platform and Salesforce Chat are not mentioned.

**Q8.** After publishing an agent that uses a tool connecting to Azure AI Search, the tool stops working. What is the most likely cause, per the module?
A. Azure AI Search indexes are automatically deleted on publish
B. The published agent has a new distinct identity, and development-time permissions don't transfer automatically
C. Published agents cannot use custom tools at all
D. The Azure Bot Service channel blocks outbound calls to Azure AI Search
**Answer:** B — Publishing creates a distinct agent identity; development-time permissions on the project identity don't transfer, so tools accessing Azure services need the new identity to be granted permissions.

**Q9.** Which two Azure/Entra roles does the module identify as prerequisites for publishing an agent to Microsoft 365? (Choose two.)
A. Azure AI Project Manager (on the Foundry project)
B. Azure AI User (on the agent application scope)
C. Global Administrator (on the Entra tenant)
D. Cognitive Services Contributor (on the resource group)
**Answer:** A, B — The module specifies Azure AI Project Manager role on the Foundry project and Azure AI User role on the agent application scope as prerequisites, plus permission to create Bot Service resources and register Entra ID apps. Global Administrator and Cognitive Services Contributor are not listed.

## Publish an agent from Foundry portal to Teams

**Q10.** Before publishing, the module says you must ensure a specific Azure resource provider is registered on the subscription. Which one?
A. Microsoft.CognitiveServices
B. Microsoft.BotService
C. Microsoft.MachineLearningServices
D. Microsoft.Web
**Answer:** B — The publishing process creates an Azure Bot Service resource, so the Microsoft.BotService provider must be registered (checked under the subscription's Resource providers section).

**Q11.** What are the required icon sizes for the Teams agent store listing, per the module's metadata preparation guidance?
A. 16x16 and 128x128 pixels
B. 32x32 and 192x192 pixels
C. 64x64 and 256x256 pixels
D. 48x48 and 144x144 pixels
**Answer:** B — The module specifies small (32x32 pixels) and large (192x192 pixels) icons in PNG format.

**Q12.** During the publishing wizard's "Configure Azure Bot Service" step, what does the portal automatically generate that you should note for troubleshooting?
A. A storage account connection string
B. An application ID and tenant ID
C. A Cosmos DB primary key
D. A managed identity client secret
**Answer:** B — The portal automatically generates an application ID and tenant ID during this step, which should be noted for later troubleshooting.

**Q13.** Approximately how long does the "Prepare Agent" packaging step typically take, according to the module?
A. 1–2 minutes
B. 10–15 minutes
C. Instantaneous, less than 5 seconds
D. 1–2 hours
**Answer:** A — The module states the packaging process typically takes 1–2 minutes to complete.

**Q14.** To test a downloaded agent package locally in Teams before broad distribution, what is the correct sequence of actions?
A. Teams > Apps > Manage your apps > Upload an app > Upload a custom app > select the .zip file
B. Teams > Settings > Integrations > Import agent package
C. Foundry portal > Deploy > Push directly to Teams client
D. Azure portal > Bot Service resource > Test in Web Chat
**Answer:** A — The module describes navigating to Apps > Manage your apps > Upload an app > Upload a custom app, then selecting the downloaded .zip file.

**Q15.** An agent was published with Organization scope. Where does a Microsoft 365 administrator go to approve it?
A. Azure portal > Bot Services > Approvals
B. Microsoft 365 admin center > Agents > All > Requested > Approve request and activate
C. Foundry portal > Governance > Pending Approvals
D. Microsoft Entra admin center > Enterprise applications > Consent requests
**Answer:** B — The admin navigates to the Microsoft 365 admin center, then Agents > All > Requested, finds the agent, and selects "Approve request and activate."

**Q16.** What determines which users can actually access an organization-scope agent once it's approved and appears under "Built by your org"?
A. The agent's publish scope alone
B. App policies configured in the organization
C. The Foundry project's RBAC role assignments
D. The Azure Bot Service pricing tier
**Answer:** B — Once approved, the agent is visible tenant-wide under "Built by your org," but app policies in the organization control which users can actually access it.

## Advanced - Use Microsoft 365 Agents Toolkit

**Q17.** A solution architect needs a Foundry agent integration with custom single sign-on beyond default Entra ID setup, plus separate dev/staging/production deployment pipelines. Which approach fits best?
A. Direct publishing from the Foundry portal with Organization scope
B. Direct publishing from the Foundry portal with Shared scope
C. Microsoft 365 Agents Toolkit proxy application
D. Azure Bot Service Twilio channel configuration
**Answer:** C — Custom SSO beyond default setup and multi-environment deployment pipelines are exactly the scenarios the module identifies as reasons to use the Microsoft 365 Agents Toolkit instead of direct publishing.

**Q18.** In the Agents Toolkit proxy architecture, what is the correct message flow?
A. Teams/Copilot → Foundry Agent → Proxy App
B. Teams/Copilot → Proxy App (Agents Toolkit) → Foundry Agent
C. Proxy App → Teams/Copilot → Foundry Agent
D. Foundry Agent → Azure Bot Service → Teams/Copilot → Proxy App
**Answer:** B — The module diagrams the flow as Teams/Copilot → Proxy App (Agents Toolkit) → Foundry Agent, with responses returning along the same path.

**Q19.** What local testing environment does the Microsoft 365 Agents Toolkit provide to simulate Teams during development?
A. Foundry Playground
B. Microsoft 365 Agents Playground
C. Bot Framework Emulator Cloud
D. Teams Developer Sandbox
**Answer:** B — The Agents Toolkit includes the Microsoft 365 Agents Playground, a local testing environment that simulates Teams, launched by running the project in debug mode.

**Q20.** According to the module's comparison table, which statement correctly contrasts direct Foundry publishing with the Agents Toolkit proxy approach?
A. Direct publishing requires writing a proxy application; the Toolkit requires no code
B. Direct publishing setup takes minutes with no code required; the Toolkit takes hours to days and requires a proxy application
C. Both approaches offer identical customization and debugging capabilities
D. The Toolkit is faster to set up but offers less customization than direct publishing
**Answer:** B — Per the comparison table, direct publishing is minutes/no code/limited customization/Foundry portal debugging, while the Toolkit is hours-to-days/requires a proxy app/extensive customization/full IDE debugging.

**Q21.** Which project type do you select in the Microsoft 365 Agents Toolkit VS Code extension to connect to an existing Foundry agent?
A. Basic Bot
B. Custom Engine Agent
C. Declarative Agent
D. Message Extension
**Answer:** B — The module states you choose "Custom Engine Agent" as the project type after selecting "Create a New Agent/App" in the extension panel.

## Access Microsoft 365 data with Work IQ

**Q22.** What is Microsoft Work IQ, precisely?
A. A machine learning model that scores employee productivity
B. A CLI and MCP server that connects AI agents/assistants to Microsoft 365 Copilot data
C. A no-code replacement for Microsoft Teams
D. A Visual Studio Code extension exclusively for building agents
**Answer:** B — Work IQ is defined as a command-line interface and server that connects AI assistants to Microsoft 365 Copilot data, enabling natural-language queries over workplace information.

**Q23.** Work IQ is built on which open protocol?
A. Agent-to-Agent (A2A) protocol
B. Model Context Protocol (MCP)
C. OpenAPI 3.0 specification
D. gRPC
**Answer:** B — The module explicitly states Work IQ is built on the Model Context Protocol (MCP), an open protocol that enables AI assistants to connect to external data sources and tools.

**Q24.** Per the module's definition of MCP concepts, which THREE capability types can an MCP server expose to an agent? (Choose three.)
A. Tools — actions the agent can take
B. Resources — data sources the agent can query
C. Prompts — predefined templates for common queries
D. Embeddings — precomputed vector representations of documents
**Answer:** A, B, C — The module defines exactly these three MCP server capability types: Tools, Resources, and Prompts. Embeddings are not mentioned as an MCP server capability category in this module.

**Q25.** Which command runs a one-off Work IQ query directly from the terminal in CLI mode?
A. `workiq query --json "..."`
B. `workiq ask -q "..."`
C. `workiq mcp start "..."`
D. `npx workiq search "..."`
**Answer:** B — The module's examples all use the form `workiq ask -q "<question>"` for CLI-mode queries.

**Q26.** Which command installs Work IQ globally via npm?
A. `npm install -g @microsoft/workiq`
B. `npm add microsoft-workiq --global`
C. `npx install @azure/workiq`
D. `npm install @microsoft/workiq-cli`
**Answer:** A — The module gives `npm install -g @microsoft/workiq` for global installation, and `npx -y @microsoft/workiq mcp` to run it without installing.

**Q27.** What must a user run before first using Work IQ, per the module?
A. `workiq init --tenant`
B. `workiq accept-eula`
C. `workiq login --consent`
D. `workiq configure --admin`
**Answer:** B — The module states you must accept the End User License Agreement before first use by running `workiq accept-eula`.

**Q28.** Why does Work IQ require administrative consent in the Microsoft Entra tenant?
A. Because it modifies Teams app policies
B. Because it accesses organization-wide Microsoft 365 data
C. Because it deploys Azure Bot Service resources
D. Because it requires a Global Administrator to run any query
**Answer:** B — Work IQ requires admin consent specifically because it accesses organization-wide Microsoft 365 data; non-admin users must request access from IT.

**Q29.** Which statement correctly describes Work IQ's data handling and security model? (Choose two.)
A. Work IQ can only access data the querying user already has permission to view
B. Work IQ stores a persistent cache of retrieved Microsoft 365 data for faster future queries
C. Queries go through Microsoft Graph using the caller's authenticated identity
D. Work IQ bypasses organizational data protection policies for efficiency
**Answer:** A, C — The module states Work IQ is permission-based (only accesses data the user can already view), doesn't store data, and queries go through Microsoft Graph with the caller's identity — all access is auditable and subject to org policies.

**Q30.** A developer wants their AI assistant in VS Code to automatically pull in relevant meeting context from Microsoft 365 without running manual commands. Which Work IQ operating mode enables this?
A. CLI mode
B. MCP server mode
C. Batch export mode
D. Webhook mode
**Answer:** B — In MCP server mode, Work IQ integrates with AI assistants like GitHub Copilot in VS Code, which automatically calls Work IQ's MCP tools when relevant, without explicit CLI commands.

## Test and iterate your integrated agent

**Q31.** Why does the module recommend testing a published agent in Microsoft Teams even after thorough testing in the Foundry playground?
A. The Foundry playground charges per test message
B. The playground doesn't simulate the full published experience, including Teams UI rendering, auth flows, and production response times
C. The Foundry playground cannot invoke tools at all
D. Teams testing is required by Microsoft 365 compliance policy
**Answer:** B — The module explicitly states the Foundry playground is valuable for development but doesn't simulate the full published experience, so post-publish Teams testing verifies UI rendering, authentication, response times, and identity permissions.

**Q32.** A published agent doesn't respond at all in Teams. Which of the following are listed as possible causes? (Choose two.)
A. Azure Bot Service isn't running
B. Bot Service configuration is incorrect
C. The agent's system prompt exceeds the token limit
D. The user's Teams license expired
**Answer:** A, B — The module lists Azure Bot Service not running, incorrect Bot Service configuration, and network issues between Teams and the agent as the possible causes for a non-responsive agent.

**Q33.** Tools that worked correctly in Foundry fail once the agent is published to Teams. What is the module's recommended resolution?
A. Redeploy the Azure Bot Service resource from scratch
B. Find the published agent's identity in Foundry portal, then assign appropriate RBAC roles to it on the resources the tools access
C. Switch the publish scope from Organization to Shared
D. Increase the agent's timeout setting in the Foundry portal
**Answer:** B — This mirrors the identity/permissions issue from earlier units: the resolution is to locate the published agent's identity and assign RBAC roles on the Azure resources (e.g., Azure AI Search, storage, Cosmos DB) that the tools access.

**Q34.** Users report they cannot find a newly published agent that was published with Organization scope. What should be checked first?
A. Whether the Azure Bot Service SKU supports organization scope
B. Whether admin approval is pending in the Microsoft 365 admin center
C. Whether the agent's Cosmos DB throughput is provisioned correctly
D. Whether the Foundry project has a valid Azure AI Search connection
**Answer:** B — For organization scope, the module identifies pending admin approval as a key possible cause of users not finding the agent, along with wrong publish scope and tenant policies blocking custom apps.

**Q35.** Where in the Foundry portal can you review request volume, response times, error rates, and tool invocation statistics for a published agent?
A. Foundry metrics
B. Azure Monitor Workbooks (Foundry does not expose its own metrics view)
C. Microsoft 365 admin center usage reports
D. Azure Bot Service channel logs only
**Answer:** A — The module states the Foundry portal provides metrics for published agents covering request volume/patterns, response times, error rates, and tool invocation statistics.

**Q36.** If Application Insights integration is configured for a published agent, which capabilities does it add per the module? (Choose two.)
A. Tracing individual conversations
B. Automatically reassigning RBAC roles on tool resources
C. Measuring end-to-end latency and setting up anomaly alerts
D. Approving organization-scope publish requests
**Answer:** A, C — The module lists tracing individual conversations, analyzing error patterns, measuring end-to-end latency, and setting up alerts for anomalies as Application Insights capabilities. RBAC reassignment and approval workflows are separate, unrelated processes.

## Knowledge check

**Q37.** (Restating the module's own knowledge check in exam format.) What Azure resource does the Foundry portal automatically create when you publish an agent to Microsoft Teams?
A. Azure Functions
B. Azure Bot Service
C. Azure Cosmos DB
D. Azure Logic Apps
**Answer:** B — Confirmed directly by the module: publishing to Teams provisions an Azure Bot Service resource, not Functions, Cosmos DB, or Logic Apps.

**Q38.** What is the main difference between shared scope and organization scope when publishing an agent?
A. Shared scope requires more Azure resources than organization scope
B. Organization scope requires admin approval before the agent is available to all users
C. Shared scope only works in the Foundry playground, not in Teams
D. Organization scope provides better agent runtime performance
**Answer:** B — Per the module's own knowledge check, the defining difference is that organization scope requires admin approval for tenant-wide availability; shared scope is immediately available without approval.

## Summary

**Q39.** Which combination correctly matches each publishing/integration concept from this module to its purpose?
A. Azure Bot Service = message routing between M365 and the agent; Agents Toolkit = proxy app for advanced customization; Work IQ = MCP server for M365 data access
B. Azure Bot Service = agent identity provider; Agents Toolkit = built-in Foundry publishing wizard; Work IQ = replacement for Microsoft Teams
C. Azure Bot Service = MCP server for M365 data; Agents Toolkit = agent identity provider; Work IQ = proxy app for SSO
D. Azure Bot Service = Work IQ's backing data store; Agents Toolkit = Microsoft Entra ID app registration tool; Work IQ = Teams agent store
**Answer:** A — This matches the module's summary precisely: Azure Bot Service routes messages, the Agents Toolkit provides the proxy-app path for complex/custom scenarios, and Work IQ is the MCP server connecting agents to Microsoft 365 data.

**Q40.** [General Azure knowledge] A Foundry agent published to Microsoft 365 needs to call Azure AI Search using its own managed identity rather than a stored API key, in line with Azure security best practices. Which authentication approach should be configured on the published agent's identity?
A. A shared access signature (SAS) token embedded in the agent's instructions
B. Role-based access control (RBAC) granting the agent's Entra identity a role such as Search Index Data Reader on the Azure AI Search resource
C. A hardcoded admin API key stored in the agent's metadata description field
D. Anonymous access enabled on the Azure AI Search resource
**Answer:** B — This follows both the module's guidance (assign RBAC roles to the published agent identity) and general Azure security best practice of using managed identity + RBAC over embedded keys or anonymous access; the module explicitly warns against putting secrets in metadata fields.
