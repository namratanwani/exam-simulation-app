# Practice questions — Integrate MCP Tools with Azure AI Agents

## Introduction

**Q1.** A retail company wants its AI agent to access an evolving catalog of inventory-related tools without redeploying the agent every time a tool changes. Which capability of a Model Context Protocol (MCP) server directly addresses this requirement?

A. A catalog of tools accessible on demand, hosted independently of the agent
B. A built-in vector index that stores inventory records inside the agent
C. A conversation memory store that retains prior chat turns
D. A prompt-flow orchestrator that chains multiple LLM calls

**Answer:** A — MCP servers provide a catalog of tools accessible on demand, so tools can change without touching the agent. B and C describe unrelated Foundry capabilities (retrieval/memory), and D describes prompt orchestration, not tool integration.

**Q2.** According to the module introduction, what problem does manually integrating and maintaining agent tools create as a system grows?

A. It has no effect on system complexity
B. It becomes complex and hard to maintain, especially as the system grows or changes frequently
C. It automatically scales without additional engineering effort
D. It eliminates the need for authentication

**Answer:** B — The module explicitly states manual tool integration "can quickly become complex, especially as your system grows, or changes frequently."

**Q3.** Which Azure/Microsoft service is used in this module's exercise to host the agent that consumes MCP tools?

A. Azure Logic Apps
B. Microsoft Foundry Agent Service
C. Azure Functions Premium plan
D. Azure Bot Service

**Answer:** B — The module builds an MCP client-server application that registers tools to an agent hosted in Microsoft Foundry Agent Service. [general Azure knowledge for distractor plausibility]

## Understand MCP tool discovery

**Q4.** Which term does Microsoft Learn use to describe the MCP approach where a tool integration is coded once and then automatically adapts as the underlying API changes?

A. "Zero-trust" approach
B. "Integrate once" approach
C. "Serverless-first" approach
D. "Single sign-on" approach

**Answer:** B — The module explicitly names this the "integrate once" approach, contrasted with traditional APIs that require manual coding per integration and updates whenever the API changes.

**Q5.** Which TWO benefits does the module attribute specifically to MCP's standardized approach? (Choose two.)

A. Interoperability across different LLMs without reworking integrations
B. Automatic translation of agent responses into 40+ languages
C. A consistent/standardized authentication method across MCP servers
D. Guaranteed sub-100ms latency for all tool calls

**Answer:** A, C — The module lists "Interoperability Across LLMs" (switch/evaluate models without reworking integrations) and "Standardized Security" (consistent authentication method) as core MCP advantages. B and D are not mentioned and are implausible guarantees.

**Q6.** In MCP terminology, what is a "tool"?

A. A UI component used to configure the Foundry portal
B. A primitive type in MCP that enables servers to expose executable functionality to clients
C. A synonym for the MCP server itself
D. A container image that hosts the agent runtime

**Answer:** B — The module states: "Tools are a primitive type in the MCP that enables servers to expose executable functionality to clients."

**Q7.** What decorator is used on an MCP server to expose a function as a discoverable tool?

A. `@mcp.expose`
B. `@mcp.tool`
C. `@fastmcp.register`
D. `@agent.function`

**Answer:** B — Tools are hosted as functions exposed using the `@mcp.tool` decorator, per Units 2 and 3.

**Q8.** Which sequence correctly reflects the dynamic tool discovery pipeline described in the module?

A. Agent hosts tools → client discovers agent → server responds to user
B. MCP server hosts available tools → MCP client dynamically discovers the tools → Azure AI Agent uses the available tools to respond to user requests
C. MCP client hosts tools → MCP server discovers tools → agent ignores discovery
D. Azure AI Agent hosts tools → MCP server wraps them → MCP client executes them

**Answer:** B — This is the exact three-step pipeline given in the module: server hosts, client discovers, agent uses the tools.

**Q9.** Which of the following is NOT listed in the module as a benefit of using dynamic tool discovery with MCP?

A. Scalability
B. Modularity
C. Maintainability
D. Guaranteed model fine-tuning acceleration

**Answer:** D — The module lists Scalability, Modularity, Maintainability, and Flexibility as benefits. Fine-tuning acceleration is unrelated and not mentioned.

## Integrate agent tools using an MCP server and client

**Q10.** Which class/function initializes an MCP server in the pattern shown in this module?

A. `MCPServer("server-name")`
B. `FastMCP("server-name")`
C. `AgentServer.create("server-name")`
D. `ToolRegistry("server-name")`

**Answer:** B — The module states: "You can initialize your MCP server using `FastMCP(\"server-name\")`."

**Q11.** How does the `FastMCP` class automatically generate tool definitions?

A. By parsing YAML configuration files uploaded separately
B. By using Python type hints and docstrings
C. By requiring a manually authored OpenAPI spec
D. By scanning compiled bytecode for annotations

**Answer:** B — "The FastMCP class uses Python type hints and document strings to automatically generate tool definitions."

**Q12.** In the manual MCP client/server pattern, which method call does the client use to discover available tools from the server?

A. `session.discover_tools()`
B. `session.list_tools()`
C. `session.get_catalog()`
D. `session.fetch_tools()`

**Answer:** B — "Discovers available tools from the MCP server using `session.list_tools()`."

**Q13.** Which method is used to actually invoke a discovered MCP tool once the client has it wrapped?

A. `session.run_tool(tool_name)`
B. `session.call_tool(tool_name, tool_args)`
C. `session.execute(tool_name, tool_args)`
D. `session.invoke_function(tool_name)`

**Answer:** B — "An MCP tool can be invoked using `session.call_tool(tool_name, tool_args)`."

**Q14.** Why must each MCP tool wrapper on the client side be an async function, per this module?

A. So the agent can wait for user input before proceeding
B. So the agent is able to invoke the tool without blocking other operations
C. So the function is automatically converted into a REST endpoint
D. Async is required only for tools that write to a database

**Answer:** B — Per the module and the official knowledge check: wrapping in async functions "enables asynchronous invocation so the agent can call tools without blocking."

**Q15.** After tool functions are wrapped and bundled in the manual client/server integration pattern, what object is registered to the agent's toolset?

A. `ToolBundle`
B. `MCPRegistry`
C. `FunctionTool`
D. `AgentToolkit`

**Answer:** C — "The tool functions are bundled into `FunctionTool` that makes them usable by the agent. The `FunctionTool` is registered to the agent's toolset."

**Q16.** Which TWO of the following are responsibilities explicitly assigned to the MCP server (not the client) in this module? (Choose two.)

A. Hosting tool definitions decorated with `@mcp.tool`
B. Generating Python function stubs that wrap tools
C. Serving tool definitions over HTTP when requested
D. Registering wrapped functions with the Azure AI Agent

**Answer:** A, C — The server hosts tool definitions and serves them over HTTP. B and D ("generates function stubs," "registers functions with the agent") are explicitly client-side responsibilities.

## Use Azure AI agents with MCP servers

**Q17.** When using Microsoft Foundry Agent Service's native support for remote MCP servers, what must a developer do differently compared to the manual client/server pattern?

A. Manually create an MCP client session and add function tools to the agent, exactly as before
B. Create an `MCPTool` object that connects to the MCP server and add server info to the agent thread — no manual client session or function tools needed
C. Deploy a separate Azure Function for every MCP tool
D. Disable dynamic discovery and hardcode each tool name in the agent definition

**Answer:** B — The module states you "don't need to manually create an MCP client session or add any function tools to your agent. Instead, you create an MCP tool object... add information about the MCP server to the agent thread."

**Q18.** Which parameter of `MCPTool` uniquely identifies a specific MCP server when an agent is connected to multiple servers?

A. `server_url`
B. `server_label`
C. `server_id`
D. `connection_name`

**Answer:** B — "`server_label`: A unique identifier for the MCP server (e.g., GitHub)." `server_url` (A) is the server's address, not its identifying label — a common close-distractor pairing.

**Q19.** Which optional `MCPTool` parameter restricts which specific tools on an MCP server the agent is permitted to access?

A. `require_approval`
B. `allowed_tools`
C. `tool_scope`
D. `permitted_functions`

**Answer:** B — "`allowed_tools` (optional): A list of specific tools the agent is allowed to access."

**Q20.** If the `require_approval` parameter on an `MCPTool` is left unspecified, what is the default behavior?

A. No approval is required for any tool call (equivalent to `never`)
B. Every tool call requires developer approval (equivalent to `always`)
C. The agent randomly selects whether approval is required per call
D. The MCP server rejects all connections until a value is set

**Answer:** B — "`always`: ... If you don't provide a value, this one is the default." This is a key distinction from the `never` mode, which must be explicitly set.

**Q21.** An agent using an `MCPTool` with `require_approval` set to `always` attempts to invoke a tool. What does the agent's response contain, and what must the developer send to proceed?

A. An `mcp_approval_request`; the developer replies with an `mcp_approval_response` containing `approval_request_id` and `approve`
B. An `mcp_error`; the developer replies by restarting the agent thread
C. A `tool_blocked_event`; the developer replies with a new `server_label`
D. Nothing — the call proceeds automatically after a timeout

**Answer:** A — "you get an `mcp_approval_request` in the agent response... send a follow-up message with the `mcp_approval_response` object, which includes an `approval_request_id` value and an `approve` boolean."

**Q22.** Which method is used on an `MCPTool` object to supply authentication headers (e.g., API keys or OAuth tokens) required by the MCP server?

A. `set_auth()`
B. `update_headers`
C. `add_credentials()`
D. `configure_security()`

**Answer:** B — "Use `update_headers` to apply any headers required by the server." The MCP tool "supports custom headers, which let you pass: Authentication keys (API keys, OAuth tokens)."

**Q23.** Which statement correctly distinguishes the manual MCP client/server integration (Unit 3) from Azure AI Agent Service's remote `MCPTool` integration (Unit 4)?

A. They are identical; `MCPTool` is just a renamed `FunctionTool`
B. Unit 3's pattern requires the developer to write client-session/discovery/invocation code and bundle a `FunctionTool`; Unit 4's `MCPTool` lets Foundry handle discovery and invocation automatically once given `server_label`/`server_url`
C. Unit 4's `MCPTool` only works with local, non-remote MCP servers
D. Unit 3's pattern does not support the `@mcp.tool` decorator

**Answer:** B — This is the core architectural distinction: manual session/`list_tools`/`call_tool`/`FunctionTool` bundling vs. a declarative `MCPTool` object that Foundry invokes automatically at runtime.

**Q24.** Can a single Azure AI Agent connect to more than one MCP server at a time?

A. No, an agent may only be linked to exactly one MCP server
B. Yes, by adding each MCP server as a separate tool (each its own `MCPTool` with its own `server_label`/`server_url`)
C. Yes, but only if both servers share the same `server_label`
D. No, unless the servers are merged into a single FastMCP instance first

**Answer:** B — "You can connect to multiple MCP servers by adding them to your agent as separate tools." Each server gets its own `MCPTool`.

## Exercise, Module assessment, and Summary

**Q25.** Approximately how long is the "Connect MCP tools to Azure AI Agents" hands-on exercise designed to take, and what does it require?

A. 5 minutes; no Azure subscription needed
B. 30 minutes; requires an Azure subscription (free trial available with 30-day credits)
C. 2 hours; requires a paid Azure Foundry enterprise tier
D. 15 minutes; requires only a local Python installation, no cloud resources

**Answer:** B — The exercise unit states "30 minutes" and that a subscription is required, with a free-trial signup link offering "credits for the first 30 days."

**Q26.** Per the module's official knowledge check, what role does the MCP server play in MCP agent tool integration?

A. Runs the AI agent and processes user prompts directly
B. Manages network connections between multiple agents
C. Hosts tool definitions and makes them available for discovery by the client
D. Stores the agent's conversation history for long-term memory

**Answer:** C — This is the exact correct option from the module assessment; the server hosts and exposes tool definitions, it does not run the agent or manage inter-agent networking.

**Q27.** Per the module summary, what does connecting an agent to an MCP server allow you to avoid?

A. Avoid using Python for agent development
B. Avoid hardcoding APIs and redeploying the agent when tools change
C. Avoid using Microsoft Foundry entirely
D. Avoid implementing any authentication for tool access

**Answer:** B — "you can dynamically discover and register tools at runtime without hardcoding APIs or redeploying your agent."

**Q28.** Where does the module direct readers for deeper Foundry-specific documentation on MCP integration?

A. The Azure Well-Architected Framework
B. "Connect to Model Context Protocol servers" in the Microsoft Foundry Agent Service documentation
C. The Semantic Kernel GitHub wiki
D. The Azure API Management developer portal

**Answer:** B — The Summary unit links to "Connect to Model Context Protocol servers" (`/azure/ai-foundry/agents/how-to/tools/model-context-protocol`) as the Foundry-specific follow-up reading, alongside the general modelcontextprotocol.io guide.

## Cross-cutting distinctions

**Q29.** Which statement best distinguishes MCP tools from traditional custom function tools, as characterized in this module?

A. Custom function tools are discovered dynamically at runtime; MCP tools must be hardcoded into the agent
B. MCP tools are discovered dynamically from a live server catalog and can change without redeploying the agent; traditional/custom integrations require manual coding per tool and updates whenever the API changes
C. There is no meaningful difference — both require identical developer effort
D. MCP tools can only be used with Semantic Kernel, never with Foundry Agent Service

**Answer:** B — This is the central "integrate once" value proposition of MCP versus traditional/custom API integration described across Units 1–2, and Unit 4 shows Foundry Agent Service has native MCP support.

**Q30.** A developer wants an MCP-connected agent to invoke certain low-risk tools automatically, while still requiring approval for a specific set of sensitive tools on the same server. Based on the parameters described in this module, which statement is most accurate?

A. This is possible directly: set `require_approval` per-tool and use `allowed_tools` to scope the sensitive subset
B. The module only describes a server-wide `require_approval` mode (`always`/`never`) and a server-wide `allowed_tools` filter; it does not describe a documented per-tool mixed-approval mechanism, so this would require workarounds beyond what's shown (e.g., splitting tools across separate `MCPTool`/server configurations)
C. `require_approval` cannot be used at all with `allowed_tools` simultaneously
D. MCP does not support any approval workflow — approval is only available for custom function tools

**Answer:** B — As documented in this module, `require_approval` takes `always`/`never` and `allowed_tools` is a list restricting accessible tools; the module does not present a per-tool granular approval mode, so a candidate should recognize the limits of what's explicitly documented rather than assume unstated fine-grained control. [reasoning beyond a single verbatim fact, grounded in the parameters as described]
