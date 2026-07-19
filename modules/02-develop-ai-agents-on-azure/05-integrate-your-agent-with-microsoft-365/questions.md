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

**Q41.** How many units does this module contain, and at what level is it classified?
A. 5 units, Beginner level
B. 9 units, Intermediate level
C. 12 units, Advanced level
D. 7 units, Intermediate level
**Answer:** B — The module metadata states Intermediate level across 9 units, for roles AI Engineer, Developer, and Solution Architect.

## Understand Foundry agent publishing options

**Q3.** When you publish a Foundry agent, what resource does Microsoft Foundry create to give it a dedicated invocation URL, a distinct identity, and user data isolation?
A. A Foundry Hub resource
B. An Agent Application
C. A Foundry Connection
D. An Azure AI Search index
**Answer:** B — Publishing creates an "Agent Application" resource with a dedicated invocation URL, its own Entra identity, and per-user data isolation. A Foundry Hub and Connection are project-level constructs unrelated to publish-time identity.

**Q4.** What happens to the public invocation URL when you publish a new version of an already-published agent?
A. A new URL is generated and the old one is deprecated after 30 days
B. The URL stays the same; the Agent Application routes traffic to the updated deployment
C. The URL changes only if the publish scope is set to Organization
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
A. Azure AI Search indexes are automatically deleted whenever an agent is published
B. The published agent has a new distinct identity, and development-time permissions don't transfer automatically
C. Published agents cannot use custom tools at all once they go live in production Teams
D. The Azure Bot Service channel blocks outbound calls to Azure AI Search endpoints
**Answer:** B — Publishing creates a distinct agent identity; development-time permissions on the project identity don't transfer, so tools accessing Azure services need the new identity to be granted permissions.

**Q9.** Which two Azure/Entra roles does the module identify as prerequisites for publishing an agent to Microsoft 365? (Choose two.)
A. Azure AI Project Manager (on the Foundry project)
B. Azure AI User (on the agent application scope)
C. Global Administrator (on the Entra tenant)
D. Cognitive Services Contributor (on the resource group)
**Answer:** A, B — The module specifies Azure AI Project Manager role on the Foundry project and Azure AI User role on the agent application scope as prerequisites, plus permission to create Bot Service resources and register Entra ID apps. Global Administrator and Cognitive Services Contributor are not listed.

**Q42.** Why does the module explicitly warn against putting secrets or API keys in an agent's publishing metadata fields (name, description, publisher info)?
A. Metadata fields have a strict 32-character length limit that breaks secrets
B. Metadata fields are visible to users who discover the agent in the Teams agent store
C. Metadata is stored unencrypted in an unmonitored Cosmos DB container
D. Metadata fields are automatically indexed by Bing Web Search
**Answer:** B — The module's explicit warning states secrets/API keys should never be put in metadata fields because they're visible to users who discover the agent — metadata is public-facing listing information, not a secure configuration store.

## Publish an agent from Foundry portal to Teams

**Q10.** Before publishing, the module says you must ensure a specific Azure resource provider is registered on the subscription. Which one?
A. Microsoft.CognitiveServices
B. Microsoft.BotService
C. Microsoft.MachineLearningServices
D. Microsoft.Web resource provider
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
B. Teams > Settings > Integrations > Import agent package directly from disk
C. Foundry portal > Deploy > Push directly to the Teams client instance
D. Azure portal > Bot Service resource > Test in Web Chat pane directly
**Answer:** A — The module describes navigating to Apps > Manage your apps > Upload an app > Upload a custom app, then selecting the downloaded .zip file.

**Q15.** An agent was published with Organization scope. Where does a Microsoft 365 administrator go to approve it?
A. Azure portal > Bot Services > Approvals blade for the resource
B. Microsoft 365 admin center > Agents > All > Requested > Approve request and activate
C. Foundry portal > Governance > Pending Approvals dashboard view
D. Microsoft Entra admin center > Enterprise applications > Consent requests
**Answer:** B — The admin navigates to the Microsoft 365 admin center, then Agents > All > Requested, finds the agent, and selects "Approve request and activate."

**Q16.** What determines which users can actually access an organization-scope agent once it's approved and appears under "Built by your org"?
A. The agent's publish scope alone
B. App policies configured in the organization
C. The Foundry project's RBAC role assignments
D. The Azure Bot Service pricing tier
**Answer:** B — Once approved, the agent is visible tenant-wide under "Built by your org," but app policies in the organization control which users can actually access it.

**Q43.** After you've iterated on an agent published with Organization scope and repeated the publishing process to create a new package, what should you check before assuming the update ships immediately?
A. Whether the update requires re-approval depending on tenant policy
B. Whether the Azure Bot Service SKU needs to be upgraded
C. Whether the small icon still meets the 32x32 px requirement
D. Whether the agent needs to be renamed before republishing it
**Answer:** A — The module notes that for Organization-scope deployments, updates might require re-approval depending on tenant policy — you shouldn't assume the update ships immediately without checking this, unlike Shared scope where you simply upload the new package to Teams manually.

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
A. Foundry Playground inside the portal itself
B. Microsoft 365 Agents Playground
C. Bot Framework Emulator Cloud
D. Teams Developer Sandbox
**Answer:** B — The Agents Toolkit includes the Microsoft 365 Agents Playground, a local testing environment that simulates Teams, launched by running the project in debug mode.

**Q20.** According to the module's comparison table, which statement correctly contrasts direct Foundry publishing with the Agents Toolkit proxy approach?
A. Direct publishing requires writing a proxy application from scratch; the Toolkit requires no code
B. Direct publishing setup takes minutes with no code required; the Toolkit takes hours to days and requires a proxy application
C. Both approaches offer identical customization options and debugging capabilities per the table
D. The Toolkit is faster to set up but offers noticeably less customization than direct publishing
**Answer:** B — Per the comparison table, direct publishing is minutes/no code/limited customization/Foundry portal debugging, while the Toolkit is hours-to-days/requires a proxy app/extensive customization/full IDE debugging.

**Q21.** Which project type do you select in the Microsoft 365 Agents Toolkit VS Code extension to connect to an existing Foundry agent?
A. Basic Bot project template
B. Custom Engine Agent
C. Declarative Agent
D. Message Extension
**Answer:** B — The module states you choose "Custom Engine Agent" as the project type after selecting "Create a New Agent/App" in the extension panel.

## Access Microsoft 365 data with Work IQ

**Q22.** What is Microsoft Work IQ, precisely?
A. A machine learning model that scores individual employee productivity metrics
B. A CLI and MCP server that connects AI agents/assistants to Microsoft 365 Copilot data
C. A no-code replacement for Microsoft Teams meetings and calling entirely
D. A Visual Studio Code extension exclusively for building agents
**Answer:** B — Work IQ is defined as a command-line interface and server that connects AI assistants to Microsoft 365 Copilot data, enabling natural-language queries over workplace information.

**Q23.** Work IQ is built on which open protocol?
A. Agent-to-Agent (A2A) protocol
B. Model Context Protocol (MCP)
C. OpenAPI 3.0 specification
D. gRPC streaming protocol
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
A. Because it modifies Teams app policies tenant-wide
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
A. CLI mode run manually
B. MCP server mode
C. Batch export mode
D. Webhook mode
**Answer:** B — In MCP server mode, Work IQ integrates with AI assistants like GitHub Copilot in VS Code, which automatically calls Work IQ's MCP tools when relevant, without explicit CLI commands.

**Q44.** Which Work IQ data type category enables an agent to "find files in SharePoint and OneDrive" and "search content," and which category enables it to "identify team members" and "find collaborators on projects"?
A. Emails (files); Meetings (collaborators)
B. Documents (files); People (collaborators)
C. Teams messages (files); Documents (collaborators)
D. Meetings (files); Emails (collaborators)
**Answer:** B — Per the module's data types table: Documents covers finding files in SharePoint/OneDrive and searching content; People covers identifying team members and finding collaborators on projects.

**Q45.** Do the CLI mode and MCP server mode of Work IQ differ in which Microsoft 365 data they can access?
A. Yes — MCP server mode can access organization-wide data while CLI mode is limited only to the user's own personal mailbox contents
B. No — both modes access the same underlying data with the same permissions; they differ only in interface (scripting/quick queries vs. an integrated AI assistant experience)
C. Yes — CLI mode requires purchasing a separate, additional Copilot license that MCP server mode simply doesn't need at all
D. No — but only because both modes require administrative tenant consent to run absolutely any query whatsoever, always, per tenant-wide policy
**Answer:** B — The module explicitly states both modes access the same underlying data with the same permissions; the difference is purely the interface — CLI for scripting/quick terminal queries, MCP server for automatic integration with an AI assistant like Copilot in VS Code.

## Test and iterate your integrated agent

**Q31.** Why does the module recommend testing a published agent in Microsoft Teams even after thorough testing in the Foundry playground?
A. The Foundry playground charges a per-message metering fee for every single test interaction run
B. The playground doesn't simulate the full published experience, including Teams UI rendering, auth flows, and production response times
C. The Foundry playground cannot invoke any registered tools at all during a live testing session
D. Teams testing is required by an explicit Microsoft 365 compliance and data-residency policy document
**Answer:** B — The module explicitly states the Foundry playground is valuable for development but doesn't simulate the full published experience, so post-publish Teams testing verifies UI rendering, authentication, response times, and identity permissions.

**Q32.** A published agent doesn't respond at all in Teams. Which of the following are listed as possible causes? (Choose two.)
A. Azure Bot Service isn't running
B. Bot Service configuration is incorrect
C. The agent's system prompt exceeds the token limit
D. The user's Teams license expired
**Answer:** A, B — The module lists Azure Bot Service not running, incorrect Bot Service configuration, and network issues between Teams and the agent as the possible causes for a non-responsive agent.

**Q33.** Tools that worked correctly in Foundry fail once the agent is published to Teams. What is the module's recommended resolution?
A. Redeploy the Azure Bot Service resource entirely from scratch to fix the failing tool calls
B. Find the published agent's identity in Foundry portal, then assign appropriate RBAC roles to it on the resources the tools access
C. Switch the publish scope from Organization to Shared entirely to resolve the underlying tool failure
D. Increase the agent's response timeout setting in the Foundry portal's runtime configuration
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

**Q46.** Users report slow response times from a published agent in Teams. Which of the following are listed by the module as possible causes? (Choose two.)
A. Complex agent instructions requiring extended processing
B. Tools querying large data sets
C. The Teams client being set to dark mode
D. The published agent's icon exceeding the 192x192 px size limit
**Answer:** A, B — The module lists complex agent instructions requiring extended processing, tools querying large data sets, and network latency as possible causes of slow response times, with resolutions being to simplify instructions, optimize tool configurations, and test from different network locations to isolate latency.

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
A. A shared access signature (SAS) token embedded directly in the agent's plain-text instructions field
B. Role-based access control (RBAC) granting the agent's Entra identity a role such as Search Index Data Reader on the Azure AI Search resource
C. A hardcoded admin-level API key stored inside the agent's public metadata description field, visible to all users
D. Anonymous access enabled globally on the Azure AI Search resource's public network settings and firewall rules
**Answer:** B — This follows both the module's guidance (assign RBAC roles to the published agent identity) and general Azure security best practice of using managed identity + RBAC over embedded keys or anonymous access; the module explicitly warns against putting secrets in metadata fields.

## Scenario-based questions

**Q47.** A solution architect publishes a Foundry agent directly from the portal to Teams with Organization scope. The agent uses an Azure AI Search tool and a Work IQ MCP server for M365 document search. After admin approval, users report the agent responds but Azure AI Search-backed answers fail while Work IQ-backed answers succeed. What's the most likely explanation, combining the identity model and Work IQ's security model covered in this module?
A. Work IQ doesn't require any identity, so it always works; Azure AI Search fails because the published agent's new distinct Entra identity wasn't granted RBAC roles on the Search resource, unlike development time
B. Both should fail identically since both integrations depend on the exact same underlying agent Entra identity and RBAC assignment process
C. Work IQ succeeded only because the publish scope was configured as Shared, not Organization, in this specific deployment scenario overall
D. Azure AI Search always fails after publishing regardless of any RBAC configuration applied to the agent's new identity afterward, per the module
**Answer:** A — Publishing gives the agent a new, distinct Entra identity separate from the dev-time project identity; permissions on resources like Azure AI Search must be explicitly reassigned (RBAC) to that new identity, or tool calls fail with authorization errors. Work IQ instead operates under a permission-based model tied to the querying user's own Microsoft Graph identity/permissions (inherited from M365 Copilot's security model), which is a different access path not gated by the agent's own Entra identity/RBAC assignments.

**Q48.** A company needs an agent integration with: (1) custom single sign-on beyond default Entra ID, (2) separate dev/staging/production pipelines, and (3) the ability to inject custom logging middleware between Teams and the agent. Which integration path fits, and what is the tradeoff versus direct Foundry publishing per the module's comparison table?
A. Direct Foundry publishing — it already supports custom SSO and custom middleware injection out of the box with zero extra setup required whatsoever
B. Microsoft 365 Agents Toolkit proxy pattern — setup takes hours to days and requires building/maintaining a proxy application, versus direct publishing's minutes-and-no-code tradeoff, but it provides extensive customization and full IDE debugging
C. Work IQ — it entirely replaces the need for both direct publishing and the Microsoft 365 Agents Toolkit in every deployment scenario the company might face
D. Azure Bot Service Twilio channel — it's the only publishing channel documented as supporting injected custom middleware logic between Teams and the agent
**Answer:** B — All three requirements (custom SSO, multi-environment pipelines, middleware logic) are the exact triggers the module lists for choosing the Microsoft 365 Agents Toolkit's proxy pattern over direct publishing. Per the comparison table, this trades direct publishing's "minutes, no code, limited customization, Foundry portal debugging" for "hours to days, proxy application required, extensive customization, full IDE debugging."

**Q49.** During testing, an agent works perfectly in the Foundry playground but two issues appear after publishing to Teams with Shared scope: (1) a colleague on a different phrasing style gets no tool results back from an Azure AI Search tool, and (2) another colleague can't find the agent at all in Teams. Diagnose each issue using the module's troubleshooting guidance.
A. Both issues share one single root cause: the Microsoft.BotService resource provider simply isn't registered on the Azure subscription being used for this deployment, per the module's registration checklist
B. Issue 1 is likely the published agent's identity lacking RBAC permissions on the Azure AI Search resource (reassign roles); Issue 2 — since scope is Shared (immediate, no approval needed), it's more likely the second colleague simply doesn't have the direct share link, or a tenant policy issue, rather than a pending admin approval (which only applies to Organization scope)
C. Issue 1 means the agent must be republished with Organization scope instead of Shared scope entirely; Issue 2 means the small 32x32 pixel icon is missing entirely from the uploaded package
D. Both issues indicate the Foundry playground must be used instead of Teams for all future testing sessions going forward, per the module's stated guidance on published-agent troubleshooting
**Answer:** B — The module's troubleshooting table attributes "tools work in Foundry but fail in Teams" to the published agent identity lacking required permissions (fix: assign RBAC roles). "Users can't find the agent" possible causes include wrong publish scope, pending admin approval (Organization scope only), or tenant policies — since this agent is Shared scope (no approval required), a missing share link or tenant policy is the more relevant cause than pending approval.
