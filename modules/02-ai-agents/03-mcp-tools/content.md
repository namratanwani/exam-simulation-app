# Integrate MCP Tools with Azure AI Agents

Source: https://learn.microsoft.com/en-us/training/modules/connect-agent-to-mcp-tools/

(Module also referenced/requested as "Connect an agent to Model Context Protocol (MCP) tools" — this is the current Microsoft Learn title for that module.)

## Learning objectives

After completing this module, you're able to:

- Explain the roles of the MCP server and client in tool discovery and invocation.
- Wrap MCP tools as asynchronous functions and register them with Azure AI agents.
- Build an Azure AI agent that dynamically accesses and calls MCP tools during runtime.

Prerequisites: experience deploying generative AI models in Microsoft Foundry; programming experience.

Module metadata: Intermediate level. Roles: AI Engineer, Developer, Solution Architect, Student. Products: Microsoft Foundry, Foundry Agent Service. 7 units.

## Exam relevance

This module maps to **"Implement generative AI and agentic solutions" (30–35%)**, specifically the **"Build agents by using Foundry"** subsection:

- **"Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions"** — MCP is a standardized way to integrate external APIs/tools as agent tools, as an alternative/complement to hand-written custom function tools.
- **"Build agents that integrate retrieval, function-calling, and conversation memory"** — MCP tool invocation is a form of dynamic function-calling.
- **"Build autonomous or semiautonomous workflows with safeguards and approval flow controls"** — directly covered by the `require_approval` parameter and the `mcp_approval_request` / `mcp_approval_response` human-in-the-loop pattern.

It also supports the **"Plan and manage an Azure AI solution" (25–30%)** domain:

- **"Choose appropriate memory, tool, and knowledge integration services for agent solutions"** (under "Choose the appropriate Foundry services for generative AI and agents") — this module directly teaches when/how to choose MCP-based tool integration vs. custom function tools.
- **"Configure security, including managed identity, private networking, keyless credentials, and role policies"** — relevant to MCP custom headers carrying API keys/OAuth tokens.
- **"Govern agent behavior with oversight modes, constraints, and tool-access controls"** — the `allowed_tools` and `require_approval` parameters are exactly this kind of tool-access governance.

## Introduction

AI agents often need to interact with tools outside the LLM itself — APIs, databases, internal services. Manually integrating and maintaining these tool connections becomes complex as a system grows or changes frequently.

**Model Context Protocol (MCP) servers** solve this by giving an agent a **catalog of tools accessible on demand**, rather than requiring hand-integrated, hardcoded tool logic. This makes the AI solution more robust, scalable, and easier to maintain.

Example scenario used throughout the module: a cosmetics retailer builds an AI assistant to check product stock levels and recent sales trends. An MCP server exposes tools for inventory assessment; the agent calls them dynamically.

The module teaches: setting up an MCP server and client, connecting tools to an Azure AI Agent dynamically, and building an MCP tool solution with **Microsoft Foundry Agent Service**.

## Understand MCP tool discovery

### Advantages of MCP for AI agents

- **Dynamic Tool Discovery** — AI agents automatically receive a list of available tools from a server, with descriptions of their functions. Unlike traditional APIs (which require manual coding per integration and updates whenever the API changes), MCP enables an **"integrate once"** approach that improves adaptability and reduces maintenance.
- **Interoperability Across LLMs** — MCP works seamlessly with different LLMs, letting developers switch or evaluate core models without reworking tool integrations.
- **Standardized Security** — MCP provides a **consistent authentication method**, simplifying secure access across multiple MCP servers, eliminating the need to manage separate keys/authentication protocols per API.

### What is dynamic tool discovery?

A mechanism that lets an AI agent discover available external tools **without hardcoded knowledge of each one**. Instead of manually adding/updating every tool, the agent queries a centralized **MCP server**, which acts as a live catalog exposing tools the agent can understand and call.

Implications:
- Tools can be added, updated, or removed centrally without modifying agent code.
- Agents always use the latest version of a tool.
- Tool-management complexity shifts from the agent into a dedicated service.

### How MCP enables dynamic tool discovery

- An **MCP server** hosts a set of functions exposed as **tools** using the `@mcp.tool` decorator.
- **Tools** are a **primitive type** in MCP that lets servers expose executable functionality to clients.
- A **client** connects to the server and fetches these tools dynamically, then generates **function wrappers** that are added to the Azure AI Agent's tool definitions.

Pipeline:
1. The MCP server hosts available tools.
2. The MCP client dynamically discovers the tools.
3. The Azure AI Agent uses the available tools to respond to user requests.

### Why use dynamic tool discovery with MCP?

- **Scalability** — add/update tools without redeploying agents.
- **Modularity** — agents stay simple, focused on delegation rather than tool-detail management.
- **Maintainability** — centralized tool management reduces duplication and errors.
- **Flexibility** — supports diverse tool types and complex workflows by aggregating capabilities.

Especially useful where tools evolve rapidly or many teams manage different APIs/services.

## Integrate agent tools using an MCP server and client

To dynamically connect tools to an Azure AI Agent you need a functioning MCP setup: an **MCP server** (hosts the tool catalog) and an **MCP client** (fetches those tools and makes them usable by the agent).

### What is the MCP Server?

- Acts as a **registry** for tools the agent can use.
- Initialized with **`FastMCP("server-name")`**.
- The `FastMCP` class uses **Python type hints and docstrings** to automatically generate tool definitions.
- Tool definitions are served over **HTTP** when requested by the client.
- Because tool definitions live on the server, you can update/add tools at any time **without modifying or redeploying the agent**.

```python
# Conceptual pattern from the unit
from fastmcp import FastMCP

mcp = FastMCP("server-name")

@mcp.tool
def some_tool_function(...):
    """Docstring used to auto-generate the tool definition."""
    ...
```

### What is the MCP Client?

A standard MCP client is a **bridge** between the MCP server and the Azure AI Agent Service. It:

1. Initializes an MCP client **session** and connects to the server.
2. **Discovers available tools** from the MCP server using **`session.list_tools()`**.
3. **Generates Python function stubs** that wrap the tools.
4. **Registers those functions** with the agent.

This lets the agent call any tool in the MCP catalog as if it were a native function, with no hardcoded logic.

### Register tools with an Azure AI Agent

- Once an MCP client session is initialized, the client pulls tools from the MCP server.
- An MCP tool is invoked using **`session.call_tool(tool_name, tool_args)`**.
- Each tool should be wrapped in an **async function** so the agent can invoke it.
- These wrapped functions are bundled together and become part of the agent's toolset, available at runtime for any user request.

### Overview of MCP agent tool integration (end-to-end flow)

1. The **MCP server** hosts tool definitions decorated with `@mcp.tool`.
2. The **MCP client** initializes an MCP client connection to the server.
3. The **MCP client** fetches available tool definitions with `session.list_tools()`.
4. Each tool is wrapped in an async function that invokes `session.call_tool`.
5. The tool functions are bundled into a **`FunctionTool`** that makes them usable by the agent.
6. The `FunctionTool` is registered to the agent's toolset.

This creates a clean separation between tool management and agent logic, so the system adapts quickly as new tools become available.

**Key distinction to remember:** In this manual client/server pattern, YOU write the MCP client code (session init, `list_tools()`, `call_tool()`, async wrapping, bundling into `FunctionTool`). This differs from the next unit's approach, where Azure AI Agent Service handles the client-side plumbing for you via a remote **`MCPTool`** object.

## Use Azure AI agents with MCP servers

You can enhance a Microsoft Foundry agent by connecting it to MCP servers, extending capabilities beyond built-in functions. **Azure AI Agent Service includes native support for remote MCP servers**, letting the agent connect to a server and access tools without you building the client yourself.

**Key distinction:** When using Microsoft Foundry Agent Service to connect to a remote MCP server, you do **NOT** need to manually create an MCP client session or add function tools to the agent. Instead:

- You create an **MCP tool object** (`MCPTool`) that connects to your MCP server.
- You add information about the MCP server to the **agent thread** when invoking a prompt.
- You can connect to and use tools from **multiple MCP servers simultaneously**, each added as a separate tool.

### Requirements to connect to an MCP server

- A remote MCP server endpoint (example given: `https://api.githubcopilot.com/mcp/`).
- A Microsoft Foundry agent configured to use the MCP tool.

### `MCPTool` parameters

- **`server_label`** — a unique identifier for the MCP server (e.g., "GitHub").
- **`server_url`** — the MCP server's URL.
- **`allowed_tools`** (optional) — a list of specific tools the agent is allowed to access.
- **`require_approval`** (optional) — boolean/mode determining whether tool invocations require human approval. If `true`/set, the agent pauses and waits for approval before invoking any tools on the MCP server.

The MCP tool also supports **custom headers**, used to pass:
- Authentication keys (API keys, OAuth tokens).
- Other headers required by the MCP server.

### Invoking tools automatically

With the Azure `MCPTool` object, you do **not** need to wrap function tools or call `session.call_tool` yourself — tools are automatically invoked when necessary during an agent run.

Steps to automatically invoke MCP tools:
1. Create the `MCPTool` object with the server label and URL.
2. Use **`update_headers`** to apply any headers required by the server.
3. Use the **`require_approval`** parameter to determine whether approval is required. Supported values:
   - **`always`** — a developer must approve every call. This is the **default** if you don't provide a value.
   - **`never`** — no approval required.
4. Create an agent and add the `MCPTool` object to its tools list.
5. Invoke a prompt on the agent — tool invocation results appear in the response.

### Human-in-the-loop approval flow

- If the model tries to invoke a tool requiring approval, the agent response includes an **`mcp_approval_request`** — containing information about which tool is being invoked.
- To approve, send a follow-up message containing an **`mcp_approval_response`** object, which includes:
  - **`approval_request_id`** value.
  - **`approve`** boolean.

MCP integration is described as a key step toward richer, more context-aware AI agents, with growing opportunities to bring specialized tools into agent workflows.

## Exercise - Connect MCP tools to Azure AI Agents

A hands-on Microsoft Learn sandbox exercise (~30 minutes, requires an Azure subscription — free trial includes credits for the first 30 days). Task: build an MCP client-server application that dynamically registers tools to an Azure AI Agent. Launched via an external fwlink to the Learn sandbox; no additional technical content is present on the page itself beyond the launch link.

## Module assessment (knowledge check)

Official knowledge-check questions (answer options as listed on the page; correct answers not marked inline on the source page, but are directly derivable from unit content above):

1. **What role does the MCP server play in the MCP agent tool integration?**
   - Runs the AI agent and processes user prompts directly.
   - Manages network connections between multiple agents.
   - Hosts tool definitions and makes them available for discovery by the client. *(correct, per Unit 3: "The MCP server hosts tool definitions decorated with @mcp.tool.")*

2. **How does an MCP client retrieve available tools from the MCP server?**
   - By calling `session.list_tools()` to get the current tool catalog. *(correct, per Unit 3.)*
   - By reading a static JSON file from the server directory.
   - By subscribing to server events via a WebSocket connection.

3. **Why should MCP tools be wrapped in async functions on the client-side?**
   - To allow the agent to wait for user input.
   - To enable asynchronous invocation so the agent can call tools without blocking. *(correct, per Unit 3: "wrapped in an async function so that the agent is able to invoke them.")*
   - To convert the functions into REST API endpoints automatically.

## Summary

This module covered integrating external tools with **Microsoft Foundry Agent Service** using the **Model Context Protocol (MCP)**.

Key takeaways:
- Connecting an agent to an MCP server enables **dynamic discovery and registration of tools at runtime**, without hardcoding APIs or redeploying the agent.
- Using an MCP client, you generate **function wrappers** from discovered tools and connect them directly to the agent.
- This lets the agent **adapt to evolving toolsets**, producing more flexible AI solutions that grow alongside applications.

Further reading referenced by the module:
- Model Context Protocol User Guide: https://modelcontextprotocol.io/introduction
- Microsoft Foundry Agent Service — Connect to Model Context Protocol servers: `/en-us/azure/ai-foundry/agents/how-to/tools/model-context-protocol` (Python pivot)

## Consolidated distinctions (exam-critical)

- **MCP server vs. MCP client**: The **server** hosts/exposes tools (via `FastMCP`, `@mcp.tool` decorator, served over HTTP). The **client** discovers (`session.list_tools()`) and invokes (`session.call_tool()`) those tools, then wraps them for the agent.
- **Manual MCP client/server setup (Unit 3) vs. Azure AI Agent Service native `MCPTool` (Unit 4)**: In the manual pattern, the developer writes client-session code, tool discovery, async wrapping, and bundles a `FunctionTool`. With Azure AI Agent Service's built-in `MCPTool` object, none of that client code is needed — you just supply `server_label`, `server_url`, optional `allowed_tools`, and `require_approval`, and Foundry handles discovery/invocation automatically at runtime, referencing the MCP server info on the agent thread per prompt.
- **MCP tools vs. custom function tools**: Custom function tools are hardcoded into the agent and require redeployment to add/change. MCP tools are discovered dynamically from a live catalog — "integrate once," update centrally without touching agent code.
- **`require_approval` values**: `always` (default if unspecified — every tool call needs developer approval) vs. `never` (no approval needed). Approval handshake uses `mcp_approval_request` (from agent) and `mcp_approval_response` with `approval_request_id` + `approve` (developer's reply).
- **`allowed_tools`** restricts which tools on a connected MCP server the agent may use — a tool-access governance control, distinct from `require_approval` (which governs whether/how each call is authorized at runtime).
- Multiple MCP servers can be attached to one agent simultaneously, each as its own `MCPTool` with its own `server_label`/`server_url`/headers.
