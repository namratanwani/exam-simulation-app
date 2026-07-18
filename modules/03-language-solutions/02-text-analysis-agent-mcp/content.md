# Develop a text analysis agent with the Azure Language MCP server

Source: https://learn.microsoft.com/en-us/training/modules/develop-text-analysis-agent-language-mcp/

Module info: 6 Units, Intermediate level, roles: AI Engineer / Developer, products: Azure AI Language, Microsoft Foundry, Foundry Agent Service.

> The **Azure Language MCP server is in public preview** — details in this module are subject to change (explicitly noted).

## Learning objectives

- Describe the Azure Language MCP server and the text analysis capabilities it exposes.
- Explain how MCP enables dynamic tool discovery and selection by AI agents.
- Connect the Azure Language MCP server to an agent in Microsoft Foundry.
- Build a Python client application that invokes an agent to perform text analysis.

Prerequisites: familiarity with Azure services and the Foundry portal; experience deploying generative AI models in Foundry; some Python familiarity.

## Exam relevance

Maps primarily to:
- **Implement text analysis solutions (10–15%)** → "Implement solutions to extract entities, topics, summaries, and structured JSON outputs by using generative prompting and Foundry Tools" and "Configure detection of sentiment, tone, safety issues, and sensitive content" — the Language MCP server exposes NER, PII redaction, and language detection as agent-callable tools.
- **Implement generative AI and agentic solutions (30–35%)** → "Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions" and "Build agents that integrate retrieval, function-calling, and conversation memory" — this module is fundamentally about MCP tool integration and dynamic tool discovery/selection for agents.
- Also touches "Choose appropriate memory, tool, and knowledge integration services for agent solutions" (Plan and manage an Azure AI solution).

## Unit 1: Introduction

Azure Language in Foundry Tools provides NLP capabilities (language detection, NER, PII extraction) callable individually via REST/SDK. Alternatively, you can expose them to an AI agent through the **Azure Language Model Context Protocol (MCP) server**, letting the agent dynamically select/call the right language tool per user request — no per-capability routing code needed.

Example scenario: analyzing multilingual customer feedback — detect language, identify people/places mentioned, redact personal details — all through a single MCP tool connection instead of separate integrations.

Module covers: how the Azure Language MCP server works, connecting it to a Foundry agent, and building a client app that interacts with the agent programmatically.

## Unit 2: Understand the Azure Language MCP server

### What is the Model Context Protocol (MCP)?

MCP is an **open protocol** defining how AI agents interact with external tools, data sources, and services. Client-server architecture with three components:

- **Host** — the application running the agent (e.g., Microsoft Foundry or a custom app).
- **Client** — a component within the host that manages connections to MCP servers and handles communication.
- **Server** — a program that exposes tools, resources, and prompts an agent can discover and call.

When an agent connects to an MCP server, it receives a **catalog of available tools** with descriptions. The agent picks the right tool based on the user's request — this is **dynamic tool discovery**: no hardcoded tool knowledge; the agent queries the MCP server at runtime.

**Key advantage:** flexibility — tools can be added/updated/removed server-side without modifying the agent. The agent always has the latest tool definitions → easier maintenance/scaling.

> Cross-reference: for MCP architecture/custom tool integration generally, see the separate **"Integrate MCP Tools with Azure AI Agents"** module (`/en-us/training/modules/connect-agent-to-mcp-tools/`).

### Azure Language MCP server capabilities

| Capability | Description |
|---|---|
| **Language Detection** | Identifies the language in which text is written. |
| **Named Entity Recognition** | Identifies and categorizes entities in text (people, places, organizations, dates, quantities). |
| **PII Redaction** | Detects and redacts PII (names, addresses, phone numbers). |
| **Text Analytics for Health** | Extracts and labels medical entities (diagnoses, medications, symptoms) from clinical text. |

> Same deprecation note as module 1: sentiment analysis, summarization, key phrase extraction, and other "common language-related tasks" are called out as **deprecated capabilities**, kept only for existing applications — and notably **NOT** listed among the four current MCP server capabilities above. **Text Analytics for Health is new here** (not covered in module 1) — exam-relevant distinguishing capability specific to the MCP tool catalog.

### How the agent selects tools

1. User sends a prompt to the agent.
2. Agent analyzes the prompt, determines needed task(s).
3. Agent checks available MCP tools + descriptions for best match.
4. Agent calls the selected tool via the MCP server, passing relevant input text.
5. MCP server processes the request using the appropriate Azure Language capability, returns results.
6. Agent combines results into a natural-language response.

No routing logic needed in your app — the agent autonomously selects tools based on descriptions received from the MCP server. Example: prompt "Determine the language that this article is written in, and tell me what people are mentioned" → agent may call **both** the language detection tool and the NER tool in the same turn.

### MCP server endpoint

Remote endpoint URL format:
```
https://{foundry-resource-name}.cognitiveservices.azure.com/language/mcp?api-version=2025-11-15-preview
```
Replace `{foundry-resource-name}` with your Foundry (or Azure Language) resource name. This is what you configure when connecting the MCP server to an agent.

**API version:** `2025-11-15-preview`.

> Note: Azure Language also provides a **local MCP server** you can self-host — see the Azure Language MCP Server quickstart in the `Azure-Samples/ai-language-samples` GitHub repo. (Distinguishing factor: remote/hosted endpoint above vs. self-hosted local server option.)

## Unit 3: Connect and use the Language MCP server with an agent

### Create a Foundry project and agent

1. In the Foundry portal (ai.azure.com), create a new project (or use existing).
2. Deploy a model (example given: **gpt-4.1**) for the agent's reasoning/response generation.
3. Create an agent with instructions describing its purpose, e.g.:
   ```
   You are an AI agent that assists users by helping them analyze and summarize text.
   ```

### Connect the Azure Language MCP server (via Foundry portal)

Via the **Tools** page in the Foundry portal:
1. Select **Tools** in the navigation pane.
2. Select **Connect a tool** → choose **Azure Language in Foundry Tools** from the catalog.
3. Configure connection settings:
   - **Foundry resource name** — e.g., `myproject-resource`.
   - **Authentication** — Key-based.
   - **Credential** (`Ocp-Apim-Subscription-Key`) — the key for your Foundry project.
4. Wait for the connection, then select **Use in an agent** and choose your agent.

Tip: find the project key on the project home page in the Foundry portal.

### Update agent instructions

After connecting, update instructions to direct tool use, e.g.:
```
You are an AI agent that assists users by helping them analyze text. Use the Azure Language tool to perform text analysis tasks.
```

### Test in the agent playground

When you send a prompt requiring text analysis, the agent:
1. Identifies needed tasks (e.g., language detection + entity recognition).
2. Calls the appropriate Azure Language MCP tool(s).
3. Returns a combined response.

**First-use approval**: The first time the agent uses an MCP tool, you're prompted to **approve** tool usage. Options: approve for a single use, or select **"Always approve all Azure Language in Foundry Tools tools"** to skip future prompts.

**Logs pane**: After the agent responds, review the Logs pane to verify which tools were used — shows each MCP tool call, the input sent, and the result returned.

### Build a client application

The Foundry SDK supports programmatic agent invocation via the **OpenAI Responses API**. Packages: `azure-ai-projects` and `azure-identity`.

Pattern:
1. Create an **`AIProjectClient`** using your Foundry project endpoint and **`DefaultAzureCredential`** (uses Azure CLI credentials in dev).
2. Get an OpenAI client from the project client via **`get_openai_client()`**.
3. Call **`responses.create()`** to send a user prompt to the agent.

Reference the agent **by name** via the `extra_body` parameter:

```python
response = openai_client.responses.create(
    input=[{"role": "user", "content": user_prompt}],
    extra_body={
        "agent_reference": {
            "name": "Text-Analysis-Agent",
            "type": "agent_reference"
        }
    },
)

print(response.output_text)
```

Result text is in **`response.output_text`**. Full response JSON (via **`response.model_dump_json()`**) reveals which tools were called — e.g., **`extract_named_entities_from_text`** or **`detect_language_from_text`** — with arguments and per-call results.

### Connect the MCP server in code (alternative to portal configuration)

Use the **`MCPTool`** class from the `azure-ai-projects` SDK to define the server connection directly in code:

```python
from azure.ai.projects.models import MCPTool

mcp_tool = MCPTool(
    server_label="azure-language",
    server_url="https://{foundry-resource-name}.cognitiveservices.azure.com/language/mcp?api-version=2025-11-15-preview",
    require_approval="always",
)
```

Pass `mcp_tool` when creating the agent through the SDK. Useful for managing tool connections as application code rather than manual portal configuration. Use the **`allowed_tools`** property on `MCPTool` to restrict which specific Language tools the agent can call.

Parameters seen on `MCPTool`: `server_label`, `server_url`, `require_approval` (e.g., `"always"`), `allowed_tools`.

### Tool selection with multi-task prompts

When a prompt spans multiple tasks, the agent can call multiple tools in one turn. Example prompt: *"Tell me what entities and dates are mentioned in this review, and whether it is positive or negative."* — this needs both entity recognition and sentiment analysis. Per the module text, the agent "identifies both tasks, calls the appropriate tools (`extract_named_entities_from_text` and `detect_language_from_text`), and combines the results into a single response."

> Note: this example text names `detect_language_from_text` as the second tool called for a sentiment-analysis-flavored request — worth flagging as a module inconsistency (sentiment analysis is listed elsewhere as deprecated / not one of the 4 current MCP capabilities), but reproduced verbatim since it's the literal exam-source text.

Each tool call goes through the MCP server independently; the agent synthesizes outputs into one coherent answer.

## Unit 4: Exercise — Develop a text analysis agent

Hands-on exercise (~30 minutes): create an AI agent in Microsoft Foundry, connect it to the Azure Language MCP server, test in the agent playground, and build a Python client application using the agent for tasks like entity recognition and PII redaction. Requires an Azure subscription with administrative access. Delivered via external lab launch link.

## Unit 5: Knowledge check

Standard graded quiz — interactive only, no extractable content.

## Unit 6: Summary

Recap — you learned how to:
- Describe the Azure Language MCP server and the text analysis capabilities it exposes.
- Explain how MCP enables dynamic tool discovery and selection by AI agents.
- Connect the Azure Language MCP server to an agent in Microsoft Foundry.
- Test language tool integration in the agent playground.
- Build a Python client application that invokes an agent with language tools using the Foundry SDK.

### Learn more links
- Azure Language tools and agents (`/en-us/azure/ai-services/language-service/concepts/foundry-tools-agents`)
- Azure Language MCP server capabilities (same page, `#azure-language-mcp-server-preview` anchor)
- Connect to Model Context Protocol servers (`/en-us/azure/foundry/agents/how-to/tools/model-context-protocol`)
- Azure AI Projects SDK for Python (`/en-us/python/api/overview/azure/ai-projects-readme`)
- Build agents using Model Context Protocol on Azure (`/en-us/azure/developer/ai/intro-agents-mcp`)
