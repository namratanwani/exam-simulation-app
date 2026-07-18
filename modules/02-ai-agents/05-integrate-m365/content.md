# Integrate your agent with Microsoft 365

Source: https://learn.microsoft.com/en-us/training/modules/integrate-foundry-agent-with-m365/

## Learning objectives
By the end of this module, you'll be able to:
- Explain the options for publishing Foundry agents to Microsoft 365
- Publish an agent from the Foundry portal to Teams and Microsoft 365 Copilot
- Use Work IQ to access Microsoft 365 data in your agents
- Test and troubleshoot agents integrated with Microsoft 365

**Prerequisites:** Familiarity with Azure and the Azure portal; experience building agents in Microsoft Foundry (recommended prior module: "Develop AI agents with Microsoft Foundry and Visual Studio Code"); a Microsoft 365 subscription with access to Teams.

**Module metadata:** Intermediate level. Roles: AI Engineer, Developer, Solution Architect. Products: Microsoft Foundry, Foundry Agent Service, Microsoft 365 Copilot. 9 units.

## Exam relevance
This module maps to **Learning Path 2 — "Develop AI agents on Azure"**, and supports the following EXAM_SKILLS.md bullets under **Implement generative AI and agentic solutions (30–35%)**:

- **Build agents by using Foundry** → "Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions" — Work IQ is presented as an MCP server exposing Microsoft 365 data as tools/resources to an agent.
- **Build generative applications by using Foundry** → "Integrate generative workflows into applications by using Foundry SDKs and connectors" — the Microsoft 365 Agents Toolkit / Agents SDK proxy pattern is a connector-style integration between a custom app and a Foundry agent endpoint.
- **Plan and manage an Azure AI solution → Set up AI solutions in Foundry** → "Choose appropriate deployment options" — this module is specifically about the deployment/publish option of exposing a Foundry agent through Microsoft 365 (Teams, M365 Copilot) versus web app preview, stable API endpoint, or Azure Bot Service channels.
- **Plan and manage an Azure AI solution → Manage, monitor, and secure AI systems** → "Configure security, including managed identity, private networking, keyless credentials, and role policies" — the module's agent identity/RBAC reassignment guidance (Azure AI Project Manager, Azure AI User roles; RBAC on published agent identity) and "Monitor model performance..." maps to the Foundry metrics/Application Insights monitoring content in Unit 6.

## Introduction
Scenario framing: an agent built in Microsoft Foundry works in the Foundry playground, but users live in Microsoft Teams / Microsoft 365 Copilot. Microsoft Foundry provides **built-in capabilities to publish agents directly to Microsoft Teams and Microsoft 365 Copilot**, so users interact with custom agents inside their existing collaboration tools rather than a separate app.

The module explores:
1. The publishing workflow from the Foundry portal.
2. When advanced integration options (Agents Toolkit) are needed.
3. How to use **Work IQ** to give agents access to Microsoft 365 data (emails, meetings, documents).

## Understand Foundry agent publishing options

**Core concept:** An agent built in Microsoft Foundry runs within the **Foundry Agent Service** infrastructure. *Publishing* promotes the agent from a development asset into a managed Azure resource — an **Agent Application** — with a dedicated endpoint, independent identity, and governance capabilities.

### Agent Application resource
When you publish an agent, Microsoft Foundry creates an **Agent Application** resource with:
- **Dedicated invocation URL** — a stable endpoint that stays consistent across agent version updates.
- **Agent identity** — a distinct Microsoft Entra identity, separate from your development project's identity.
- **User data isolation** — one user's inputs/interactions aren't available to other users.

The Agent Application acts as a **routing layer**: publishing a new agent version routes traffic to the updated deployment automatically without changing the public endpoint.

### Publishing to Microsoft 365
Publishing to Microsoft 365 (the module's primary focus):
- Creates an **Azure Bot Service** resource that routes messages between Microsoft 365 and your agent.
- Generates a **Microsoft 365 publishing package** for distribution.
- Registers a **Microsoft Entra ID application** for authentication.
- Makes the agent discoverable in the **Teams agent store**.

### Two integration approaches — exact distinction
| Approach | What it is | When to use |
|---|---|---|
| **Direct publishing from Foundry portal** | Publishing wizard creates the Azure Bot Service resource, registers the Entra ID app, generates the M365 publishing package, and prepares the agent for distribution — all from the Foundry portal, no code | Fast deployment; agent logic stays entirely in Foundry |
| **Microsoft 365 Agents Toolkit** | You build a **proxy application** (VS Code/Visual Studio extension-based) that sits between Microsoft 365 and the Foundry agent | Custom SSO beyond default Entra ID setup, advanced middleware logic, multi-environment (dev/staging/prod) deployment pipelines |

### Publish scopes — exact distinction (exam-relevant)
| Scope | Description | Best for |
|---|---|---|
| **Shared** | Available immediately, no admin approval. Appears under **"Your agents"** in Teams. | Personal testing, small team pilots |
| **Organization** | Available to everyone in the tenant under **"Built by your org."** Requires admin approval. | Production deployments |

### Other publishing channels (non-M365)
Foundry agents can also publish to:
- **Web application preview** — browser-based UI for demos/stakeholder testing.
- **Stable API endpoint** — REST API for embedding in custom applications.
- **Azure Bot Service channels** — Slack, Telegram, Twilio (SMS), Facebook, and others.

### Agent identity and permissions
Publishing creates a **distinct agent identity**. Key exam point:
- The agent authenticates to Azure resources using **its own identity**, not the developer's project identity.
- Development-time permissions on the project identity **do not transfer automatically**.
- Any tool that accesses Azure services (e.g., Azure AI Search) needs permissions **reconfigured** for the new published-agent identity after publishing.

### Prerequisites for publishing
- **Azure AI Project Manager** role on the Foundry project.
- **Azure AI User** role on the agent application scope.
- Azure subscription permission to create Azure Bot Service resources.
- Permission to register applications in Microsoft Entra ID.
- A Microsoft 365 tenant that allows custom apps and bots.

## Publish an agent from Foundry portal to Teams

### Before you begin
- **Test thoroughly** in the Foundry playground first (inputs, tools, response appropriateness).
- **Verify permissions:** Azure AI Project Manager role (to publish), Azure AI User role (to invoke/chat), resource-creation permission in the Azure subscription, and Entra ID app-registration permission.
- **Register the Bot Service provider:** the publishing process creates an Azure Bot Service resource, so the **`Microsoft.BotService`** resource provider must be registered on the Azure subscription (check under subscription → **Resource providers**).
- **Prepare metadata:** display name, brief description, icons — **small 32x32 px** and **large 192x192 px**, PNG format — organization name/contact details, privacy policy URL, terms of use URL.
- **Warning:** never put secrets/API keys in metadata fields — they're visible to users who discover the agent.

### Step-by-step publishing process
1. **Select your agent version** — open the [Microsoft Foundry portal](https://ai.azure.com), navigate to the project, select the agent, confirm configuration.
2. **Start publishing** — select **Publish** → **Publish** again → **Publish to Teams and Microsoft 365 Copilot**. Opens the Microsoft 365 publishing configuration window.
3. **Configure Azure Bot Service** — portal auto-generates an **application ID** and **tenant ID** (note for troubleshooting). In the **Azure Bot Service** dropdown, select **Create an Azure Bot Service** to provision a new bot resource; wait for creation.
4. **Complete the metadata** — Name, Description, Icons (small/large PNG), Publisher information, Privacy policy URL, Terms of use URL.
5. **Choose publish scope** — Shared (immediate, "Your agents") vs. Organization (admin approval, "Built by your org").
6. **Prepare and optionally download the package** — select **Prepare Agent**; packaging typically takes **1–2 minutes**. Then either **Download the package** (test locally first) or **continue the in-product publishing flow** (direct distribution).

### Test the publishing package in Teams
1. Open Microsoft Teams.
2. **Apps** → **Manage your apps** → **Upload an app**.
3. **Upload a custom app**, choose the downloaded `.zip` file.
4. Teams installs the app, shows it in the apps list.
5. Open the agent, send a test message.

Checklist: agent responds; response content accurate/appropriate; response times acceptable; configured tools work correctly.

### Request admin approval (organization scope)
1. Admin goes to [Microsoft 365 admin center](https://admin.cloud.microsoft).
2. **Agents** → **All** → **Requested**.
3. Find the pending agent.
4. Admin selects **Approve request and activate**.

Once approved, the agent appears in **"Built by your org"** in the Teams agent store for the whole tenant; org **app policies** control which users can actually access it.

### Reassign permissions after publishing
Because publishing creates a distinct agent identity:
1. In Foundry portal, note the published agent application's identity information.
2. In Azure portal, go to the resources the agent's tools access (e.g., Azure AI Search, storage accounts, Cosmos DB).
3. Assign appropriate **RBAC roles** to the published agent identity.

Skipping this step is the #1 cause of "tools worked in dev, broke after publish."

### Update a published agent
1. Make changes in Foundry portal.
2. Test in Foundry playground.
3. Repeat the publishing process to create a new package.
4. Shared scope: upload the new package to Teams manually.
5. Organization scope: update might require re-approval depending on tenant policy.

## Advanced - Use Microsoft 365 Agents Toolkit

**When to consider it (exact triggers):** custom SSO configuration beyond default Entra ID setup; middleware logic (custom processing/logging/transformation between Teams and the Foundry agent); multi-environment deployment (separate dev/staging/production configs); advanced debugging/tracing beyond the Foundry portal; CI/CD integration via GitHub Actions or Azure DevOps.

**What it is:** a suite of development tools available as **Visual Studio Code** and **Visual Studio** extensions.

### Architecture — proxy pattern
```
Teams/Copilot → Proxy App (Agents Toolkit) → Foundry Agent
```
The proxy app receives messages from Teams/Copilot via **Azure Bot Service**, runs them through custom middleware, forwards the request to the Foundry agent, and returns the response along the same path. Gives full control over the message flow but adds deployment complexity — contrast with direct publishing, where Foundry itself is the endpoint.

### Getting started
1. Install the **Microsoft 365 Agents Toolkit** extension from the VS Code marketplace.
2. Open the extension panel → **Create a New Agent/App** → choose **Custom Engine Agent** as the project type.
3. Wizard configures options including the AI model source.
4. Connect the scaffolded proxy to an existing Foundry agent: configure the project to call the Foundry agent's endpoint, set up authentication using the agent's credentials, implement any needed middleware.
5. Use the **Microsoft 365 Agents Playground** (a local testing environment simulating Teams) — run the project in debug mode to open the playground in a browser and send test messages.
6. Once tested, use the toolkit to provision Azure resources, deploy the proxy app, and register it in Teams.

### Comparison summary (verbatim table — high exam value)
| Aspect | Direct Foundry publishing | Agents Toolkit proxy |
|---|---|---|
| Setup time | Minutes | Hours to days |
| Code required | None | Proxy application |
| Customization | Limited | Extensive |
| Debugging | Foundry portal | Full IDE debugging |
| Best for | Standard deployments | Complex enterprise needs |

**Further reading referenced:** Microsoft 365 Agents Toolkit documentation; "Create custom engine agents with the Agents Toolkit"; Microsoft 365 Agents SDK overview.

## Access Microsoft 365 data with Work IQ

### What is Work IQ?
**Microsoft Work IQ** is a **command-line interface (CLI) and server** that connects AI assistants/agents to **Microsoft 365 Copilot data** — enabling natural-language queries over workplace information (emails, meetings, documents, Teams messages, people). Status: **currently in preview** — features/APIs may change.

Example natural-language queries it supports:
- "What did my manager say about the project deadline?"
- "Find my recent documents about Q4 planning"
- "Summarize today's messages in the Engineering channel"
- "Who is working on Project Alpha?"

Data types and capabilities table:
| Data type | Example capabilities |
|---|---|
| Emails | Search messages, find communications from specific people |
| Meetings | Check calendar, retrieve meeting notes and decisions |
| Documents | Find files in SharePoint and OneDrive, search content |
| Teams messages | Summarize channel discussions, find specific conversations |
| People | Identify team members, find collaborators on projects |

### Understanding MCP servers (key distinguishing concept)
Work IQ is built on the **Model Context Protocol (MCP)** — an open protocol enabling AI assistants to connect to external data sources and tools. An **MCP server** exposes capabilities an agent can use:
- **Tools** — actions the agent can take (e.g., search documents, send messages).
- **Resources** — data sources the agent can query.
- **Prompts** — predefined templates for common queries.

When an MCP server is configured for an agent, the agent **discovers** available tools/resources and uses them to fulfill requests. **Work IQ is an MCP server purpose-built for Microsoft 365 data** — this is the exam-relevant distinction: Work IQ is not itself a generic MCP framework, it's a specific MCP server implementation scoped to M365 data.

### Operating modes
**CLI mode** — run queries directly from terminal:
```bash
workiq ask -q "What requirements did Sarah share about the authentication feature?"
```
Useful for quick dev-time queries or scripts.

**MCP server mode** — integrates with AI assistants like **GitHub Copilot in Visual Studio Code**; the assistant automatically accesses workplace context when relevant (e.g., meeting context surfaced while implementing a related feature).

### Installing Work IQ
**Via npm:**
```bash
# Global installation
npm install -g @microsoft/workiq

# Or run directly without installation
npx -y @microsoft/workiq mcp
```

**Via GitHub Copilot CLI (as a plugin):**
1. Open GitHub Copilot CLI: `copilot`
2. Add plugins marketplace (one-time): `/plugin marketplace add github/copilot-plugins`
3. Install Work IQ: `/plugin install workiq@copilot-plugins`
4. Restart Copilot CLI, start querying.

**Configure for VS Code (MCP server config JSON):**
```json
{
  "workiq": {
    "command": "npx",
    "args": [
      "-y",
      "@microsoft/workiq",
      "mcp"
    ],
    "tools": [
      "*"
    ]
  }
}
```

**Accept EULA before first use:**
```bash
workiq accept-eula
```

### Prerequisites for Work IQ
- Node.js installed (for local CLI use).
- A Microsoft 365 subscription with a **Copilot license**.
- **Administrative consent** for the Work IQ application in the Microsoft Entra tenant (required because it accesses **organization-wide** M365 data — non-admins must request access from IT).

### Security and data access model
Work IQ inherits the security model of Microsoft 365 Copilot:
- **Permission-based access** — can only access data the querying user already has permission to view.
- **No data storage** — retrieves information on-demand, doesn't persist M365 data.
- **Enterprise security** — all access follows org security policies.
- **Admin visibility** — admins can monitor/control Work IQ usage.

Queries go through **Microsoft Graph** using the caller's authenticated identity: you can't access documents you lack permission for; queries are auditable; data protection policies apply.

### Using Work IQ in agent development
- **CLI approach** example queries:
```bash
# Find project context
workiq ask -q "What were the key decisions in last week's architecture review meeting?"

# Understand requirements from documents
workiq ask -q "Summarize the requirements in the user portal spec document"

# Check team communications
workiq ask -q "What has the engineering team discussed about the API changes?"
```
Good for scripts, one-off queries, quick terminal answers.

- **MCP server approach** — AI assistant (e.g., Copilot in VS Code) calls Work IQ's MCP tools behind the scenes automatically; no explicit CLI commands needed; assistant decides when to query based on context.

Both modes access the **same underlying data with the same permissions** — the choice is CLI (scripting/quick queries) vs. MCP server (integrated AI assistant experience), not a difference in access scope.

## Test and iterate your integrated agent

### Testing beyond the Foundry playground
The Foundry playground doesn't simulate the full published experience. After publishing, test in Microsoft Teams to verify: Teams UI renders responses correctly; authentication flows work; response times acceptable in production; published agent identity has necessary permissions.

**Multi-user / multi-client testing:** have colleagues test (different phrasing surfaces different issues); test across Teams desktop, web, and mobile clients to catch platform-specific issues.

### Troubleshooting scenarios (table form — exam-relevant cause/resolution pairs)

**Agent doesn't respond in Teams**
- Possible causes: Azure Bot Service isn't running; Bot Service configuration incorrect; network issues between Teams and the agent.
- Resolution: verify Bot Service resource exists in Azure portal; check Bot Service logs; confirm agent published and package uploaded correctly.

**Tools work in Foundry but fail in Teams**
- Possible cause: the **published agent identity lacks required permissions** (same root cause as the "reassign permissions" step in unit 3).
- Resolution: find published agent's identity in Foundry portal; locate the resources tools access in Azure portal; assign appropriate RBAC roles.

**Users can't find the agent**
- Possible causes: wrong publish scope selected; admin approval pending (organization scope); tenant policies block custom apps.
- Resolution: shared scope → share direct link; organization scope → verify admin approval in M365 admin center; check tenant custom-app permission settings.

**Slow response times**
- Possible causes: complex agent instructions requiring extended processing; tools querying large data sets; network latency.
- Resolution: simplify agent instructions; optimize tool configurations; test from different network locations to isolate network issues.

### Monitoring published agents
- **Foundry metrics** (in the Foundry portal): request volume/patterns, response times, error rates, tool invocation statistics.
- **Application Insights** (if configured): trace individual conversations, analyze error patterns, measure end-to-end latency, set up alerts for anomalies.
- **User feedback channels:** dedicated Teams channel or email for agent feedback; periodic review to spot common problems; use feedback to prioritize improvements.

### Iterating
When testing/feedback reveals issues: update the agent in Foundry portal and republish using the same process as the publishing unit. Organization-scope deployments may require re-approval per tenant policy on update — check before assuming an update ships immediately.

## Exercise - Publish a Foundry agent to Teams
Hands-on lab (30 minutes): publish a Foundry agent to Microsoft Teams using an Azure subscription (free trial with 30-day credits available if none exists). A second, optional exercise covers building an app that connects to Work IQ for workplace insight (requires Work IQ access). Both exercises are launched via external fwlink URLs from the Learn module page — no additional technical content beyond what earlier units cover.

## Knowledge check
Five questions covering the module's core facts (correct answers per module content, verified against units 2–5):

1. **What Azure resource does the Foundry portal automatically create when you publish an agent to Microsoft Teams?** → **Azure Bot Service** (not Azure Functions, Cosmos DB, or Logic Apps).
2. **Main difference between shared scope and organization scope?** → **Organization scope requires admin approval before the agent is available to all users.**
3. **What happens to tool permissions when you publish an agent from Foundry to Teams?** → **The published agent gets a new identity and needs permissions reassigned** (not automatically transferred, not disabled, not scope-dependent).
4. **What is Microsoft Work IQ?** → **A CLI and MCP server that connects AI agents to Microsoft 365 data** (not an ML model, not a Teams replacement, not merely a VS Code extension).
5. **When should you consider the Microsoft 365 Agents Toolkit instead of direct publishing?** → **When you need custom SSO, middleware logic, or multi-environment deployment** (not for all production deployments, not tied to shared scope, not about tool usage).

## Summary
Recap: direct publishing from the Foundry portal auto-provisions **Azure Bot Service** and creates the necessary **Microsoft Entra ID** registrations. The **Microsoft 365 Agents Toolkit** is the alternative for complex enterprise scenarios (proxy app pattern). Publish scopes: **shared** (testing) vs. **organization** (broad distribution, admin-approved). **Agent identity** considerations drive RBAC permission reassignment after publishing. **Work IQ** connects agents to Microsoft 365 data through the **Model Context Protocol (MCP)**.

**Learn more links referenced:**
- Publish agents to Microsoft 365 Copilot and Microsoft Teams (`/azure/ai-foundry/agents/how-to/publish-copilot`)
- Microsoft Work IQ documentation (`/microsoft-365-copilot/extensibility/workiq-overview`)
- Microsoft 365 Agents Toolkit overview (`/microsoftteams/platform/toolkit/overview-agents-toolkit`)
- Agent identity concepts in Microsoft Foundry (`/azure/ai-foundry/agents/concepts/agent-identity`)
