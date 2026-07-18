# Develop an AI agent with Microsoft Agent Framework

Source: https://learn.microsoft.com/en-us/training/modules/develop-ai-agent-with-semantic-kernel/

> **IMPORTANT — module content has changed from its folder/URL name.** The module URL slug (`develop-ai-agent-with-semantic-kernel`) and this repo folder name still reference "Semantic Kernel," but Microsoft Learn has replaced the module's actual content. As of the fetch date (2026-07-18, content dated `ms.date: 2026-07-14`), the module title, learning objectives, and all seven units are entirely about the **Microsoft Agent Framework** — not the Semantic Kernel SDK. Semantic Kernel is mentioned exactly once, as historical context (see Unit 2). There is **no** Semantic Kernel-specific content (no `Kernel`, `ChatCompletionAgent`, `KernelFunction`, or plugin/skill class names appear anywhere in this module) — do not confuse this module's actual content with a Semantic Kernel walkthrough. If your study plan specifically needs Semantic Kernel SDK class-level detail (`Kernel`, `KernelPlugin`, `ChatCompletionAgent`, etc.), that content is not in this Microsoft Learn module as currently published and would need to be sourced from the standalone Semantic Kernel SDK docs.

## Learning objectives

By the end of this module, you're able to:

- Use the Microsoft Agent Framework to connect to a Microsoft Foundry project.
- Create Microsoft Foundry Agent Service agents using the Microsoft Agent Framework SDK.
- Integrate plugin/tool functions with your AI agent.

Prerequisites: familiarity with Azure and the Azure portal; an understanding of generative AI (suggested prerequisite module: "Fundamentals of Generative AI").

Module metadata: Intermediate level; roles — AI Engineer, Developer, Solution Architect, Student; products tagged — Microsoft Foundry, Foundry Agent Service; 7 units.

## Exam relevance

This module maps to **AI-103 "Implement generative AI and agentic solutions" (30–35%)**, specifically the **"Build agents by using Foundry"** skill group:
- *"Define agent roles, goals, conversation-tracking approach, and tool schemas"* — covered by the agent creation steps (instructions = system prompt defining role/goals; `AgentThread` for conversation tracking; automatic tool-schema generation from function signatures).
- *"Build agents that integrate retrieval, function-calling, and conversation memory"* — covered by File Search / Azure AI Search tools (retrieval), custom function tools and service-provided tools (function-calling), and `AgentThread` + service-side history (conversation memory).
- *"Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions"* — covered directly by Unit 4 (Code Interpreter, File Search, Web Search, Hosted MCP Tools, Azure AI Search, Foundry Toolboxes, and custom Python function tools).
- *"Implement orchestrated multi-agent solutions"* — touched on lightly via the "using an agent as a tool" composition pattern (Unit 4), which the module explicitly says is explored further in a separate multi-agent module.
- *"Build autonomous or semiautonomous workflows with safeguards and approval flow controls"* — covered by the **tool approval** pattern (`approval_mode` parameter) in Unit 4.

It also supports **"Plan and manage an Azure AI solution" (25–30%)**:
- *"Choose appropriate memory, tool, and knowledge integration services for agent solutions"* and *"Choose the appropriate Foundry services for generative AI and agents"* — covered by the **provider matrix** in Unit 2 comparing Foundry Agent Service, Azure OpenAI Responses/Chat Completion, OpenAI, Anthropic Claude, Amazon Bedrock, GitHub Copilot, and Ollama on service-side chat history support.
- *"Configure security, including managed identity, private networking, keyless credentials, and role policies"* — covered by `DefaultAzureCredential` authentication in Unit 3 (no hardcoded connection strings/API keys).

## Introduction

AI agents use generative AI to interpret data, make decisions, and complete tasks with minimal human intervention, making them well suited for automating complex workflows.

**Microsoft Agent Framework** is described as **the next generation of both Semantic Kernel and AutoGen, built by the same teams**. It combines:
- AutoGen's straightforward agent abstractions
- Semantic Kernel's enterprise features: session-based state management, type safety, middleware, and telemetry
- New: graph-based workflows for explicit multi-agent orchestration

Result: a flexible, production-ready SDK for building both single-agent and multi-agent solutions.

This module focuses on using the **Microsoft Agent Framework with Microsoft Foundry Agent Service** to build AI agents. Example scenario used throughout: an agent that extracts data from submitted expense reports, formats them, and emails them to the appropriate recipients (this scenario is also the basis of the module's hands-on exercise).

After completing the module you can:
- Use the Microsoft Agent Framework to connect to a Microsoft Foundry project.
- Create Microsoft Foundry agents using the Microsoft Agent Framework.
- Integrate tool functions with your AI agent.

The module offers both video and text formats; the text version is noted to contain greater detail than the videos.

## Understand Microsoft Agent Framework AI agents

**Microsoft Agent Framework** = next generation of Semantic Kernel + AutoGen, built by the same engineering teams. Combines AutoGen's intuitive agent abstractions with Semantic Kernel's enterprise-grade features (session-based state management, type safety, execution filters, telemetry). Adds **graph-based workflows** for explicit control over multi-agent execution paths.

Every agent derives from a unified **`Agent` base class**, giving a consistent interface regardless of the underlying model provider.

### Architecture and key features

Composable building blocks bundled by the framework (usable individually or combined):

| Feature | Description |
| --- | --- |
| **Model clients** | A single, unified interface to connect with multiple AI providers |
| **Agent session** | Native state management for persistent conversation context across multi-turn interactions |
| **Context providers** | Plug-and-play memory components that surface relevant information to agents dynamically |
| **Function tools** | Custom functions automatically registered with agents, with schema generation handled by the framework |
| **MCP clients** | Built-in support for the Model Context Protocol, enabling dynamic tool discovery at runtime |
| **Middleware** | Hooks to intercept, log, or modify agent actions before and after execution |
| **Workflow orchestration** | Graph-based workflows for managing sequential, concurrent, group chat, and agent handoff patterns |

### What agents can do

Because all agents share the same `Agent` base class, capabilities are consistent regardless of provider. Every agent supports, out of the box:
- **Function calling** — automatically invoke registered tools to interact with external APIs/services
- **Multi-turn conversations** — maintain chat history locally or via service-provided history management
- **Structured outputs** — generate type-safe, schema-validated responses
- **Streaming responses** — receive results incrementally
- **Service-provided tools** — built-in capabilities such as code execution, file search, and web search where supported by the provider

### Using the Microsoft Agent Framework with AI Foundry

Designed to work seamlessly with Azure AI Foundry projects: consistent interface for connecting to Foundry, managing agent sessions, and integrating with tools/services. Authenticate with Azure credentials to connect to a Foundry project and create agents using **Foundry Agent Service** capabilities: persistent chat history, dynamic tool discovery, integration with Azure services.

**Why Foundry is the recommended provider:** Foundry Agent Service supports **service-side chat history** — the agent session persists across turns automatically, no need to manage conversation state yourself. This makes it the recommended provider for production scenarios where maintaining context is critical.

### Provider matrix (exact table from the unit)

| Provider | Service chat history |
| --- | --- |
| Foundry Agent Service | Yes |
| Azure OpenAI Responses | Yes |
| OpenAI Responses | Yes |
| Azure OpenAI Chat Completion | No |
| OpenAI Chat Completion | No |
| Anthropic Claude | No |
| Amazon Bedrock | No |
| GitHub Copilot | No |
| Ollama (OpenAI-compatible) | No |

Key distinction to memorize: only the **Responses**-style APIs (Foundry Agent Service, Azure OpenAI Responses, OpenAI Responses) provide service-side chat history — the older **Chat Completion**-style APIs (Azure OpenAI Chat Completion, OpenAI Chat Completion) do NOT, nor do third-party/self-hosted providers (Anthropic Claude, Amazon Bedrock, GitHub Copilot, Ollama).

This module focuses specifically on the **Foundry Agent Service** provider, citing enterprise-grade capabilities: persistent chat history, Model Context Protocol (MCP) tool support, and integration with Azure services.

## Create an Azure AI agent with Microsoft Agent Framework

The **Foundry Agent Service** is the recommended provider for production environments built with the Microsoft Agent Framework. It handles persistent conversation history server-side, supports built-in tools (code execution, file search), and integrates with Azure identity management.

### Configuring a Foundry agent — 5-step sequence

**1. Set up your Foundry project.** You need a Microsoft Foundry project with a deployed model, and connect using two pieces of information:
- **Project endpoint** — URL of the Foundry project
- **Model deployment name** — name of the model deployment to use for the agent

**2. Configure authentication.** The Agent Framework connects using Azure credentials. `DefaultAzureCredential` resolves the right credential automatically based on environment (Azure CLI during development, managed identity in production). No connection strings or API keys need to be hardcoded.

**3. Initialize the Foundry chat client.** Create a Foundry chat client by providing credentials, project endpoint, and model name. This client bridges the application and the Foundry Agent Service — it handles authentication, request routing, and service-side session management.

**4. Create the agent.** Using the chat client, create an agent by providing:
- **Instructions** — the system prompt defining the agent's role, goals, and constraints
- **Tools** *(optional)* — custom functions the agent can call to take actions or retrieve information

The framework registers any tools provided and automatically generates their schemas so the model knows when/how to invoke them.

**5. Establish a session and run the agent.** Open a **session** via the agent instance — the session is the container for conversation state. Send user messages to the session's execution method, which processes the prompt, coordinates any necessary tool calls, and returns the model's response.

(Note: the module's Knowledge Check unit confirms the exact class names used in this flow: **`AzureAIAgentClient`**, **`ChatAgent`** — created with instructions and tools — and **`AgentThread`**, created for conversations/state management. These are the terms to know precisely for exam purposes even though the main unit text used generic terms like "chat client," "agent," and "session.")

### Multi-turn conversations

A single call to the agent's run method handles one exchange (one user message, one response). For a real conversation, the agent needs to remember prior turns — that's what a **session** (`AgentThread`) is for.

- For the **Foundry provider**, sessions are backed by **service-side storage** — conversation history lives in the Foundry Agent Service, not in the application's memory.
  - **Persistent history**: because state lives server-side, a user's conversation can continue across multiple requests even if the application restarts or scales to multiple instances.
- For providers **without** service-side history support, the framework maintains conversation state **in memory within the session object** ("local history"). Local history is suitable for short-lived/stateless applications but does **not** persist across process restarts.

### Nonstreaming vs. streaming responses

Two response modes:
- **Non-streaming (synchronous)** — the run method waits for the agent to finish and returns a complete response object. Simplest pattern; good when incremental display isn't needed.
- **Streaming (asynchronous)** — the run method returns a response stream iterated over asynchronously, receiving partial updates as the model generates them. Better for user-facing interfaces where progressive output improves experience.

In both modes, the response exposes a **`text`** property that aggregates all text content from the agent's output, so extracting the final answer is straightforward regardless of mode.

## Add tools to Azure AI agent

Tools let an agent take action — call APIs, execute code, search files, interact with external services. Without tools, an agent can only generate text from what it already knows.

The Microsoft Agent Framework supports two broad tool categories:
1. **Service-provided tools** — hosted and managed by the provider
2. **Custom function tools** — written by the developer and registered with the agent

### Service-provided tools (Foundry provider)

Enabled by including them in the agent configuration; the provider executes them.

| Tool | What it does |
| --- | --- |
| **Code Interpreter** | Executes Python code in a sandboxed environment for calculations and data analysis |
| **File Search** | Searches through and retrieves information from uploaded documents |
| **Web Search** | Retrieves up-to-date information from the internet |
| **Hosted MCP Tools** | MCP (Model Context Protocol) servers invoked directly by the provider runtime |
| **Azure AI Search** | Queries an Azure AI Search index through a Foundry connection |
| **Foundry Toolboxes** | Named, versioned bundles of hosted tool configurations managed in a Foundry project |

Note (exact from source): Some tools — including **Azure AI Search, Bing Grounding, SharePoint**, and others — are in **preview or experimental** status. Available for Foundry agents but may have limited support across other providers.

### Custom function tools

Let you extend the agent with any logic: calling internal APIs, querying databases, performing calculations, or any Python function's logic. Register a function as a tool by passing it directly to the agent during creation — the framework inspects the function's signature and generates a schema describing what the function does, its parameters, and its return value.

Two approaches for describing tools to the model:
- **Type annotations with descriptions** — use Python's **`Annotated`** type with a field description on each parameter; the function's docstring serves as the tool description.
- **The `@tool` decorator** — explicitly specify the tool's name and description as decorator arguments for full control over what the model sees. You can also supply an explicit schema using a **Pydantic model** for precise control over input structure.

In either approach, the framework handles schema generation and tool invocation automatically. When the model decides a tool should be called, the framework executes the function and returns the result to the model before the final response is generated.

### Adding multiple tools

Register multiple tools with a single agent by passing a list of functions at agent creation. The model automatically selects the most appropriate tool per part of the conversation — no manual routing logic needed; the framework handles tool orchestration based on conversation context and the tool descriptions provided.

### Tool approval

For scenarios requiring human review before execution, the Agent Framework supports a **tool approval** pattern: when approval mode is enabled on a tool, the agent pauses before calling that function and requests confirmation. Useful for actions that are irreversible, expensive, or involve sensitive data. Configured **per tool** via the **`approval_mode`** parameter on the **`@tool`** decorator.

### Using an agent as a tool

Agents can be composed: convert an inner agent into a function tool and pass it to an outer (coordinating) agent, which delegates specific tasks to it. Enables modular designs where specialized agents handle particular domains and a coordinating agent routes requests between them. The module notes this pattern is explored in more depth in a separate **multi-agent module**.

### Best practices for custom tools (verbatim list)

- **Write clear descriptions** — the model's ability to choose the right tool depends entirely on the descriptions provided. Be specific about what the function does and when to use it.
- **Annotate every parameter** — describe each input so the model can construct valid calls, especially when parameter names alone aren't self-explanatory.
- **Return meaningful data** — tools should return structured, interpretable output; the model uses the return value directly when forming its response.
- **Keep tools focused** — each tool should do one thing well; combining multiple responsibilities into a single function makes it harder for the model to invoke it correctly.
- **Handle errors gracefully** — if a tool encounters unexpected input or an external service fails, return an informative error message rather than raising an exception, so the model can respond helpfully.

## Exercise - Develop an Azure AI agent with the Microsoft Agent Framework SDK

Hands-on exercise (30 minutes): use the Microsoft Agent Framework SDK to create an AI agent that **creates an expense claim email** (matches the scenario introduced in the Introduction unit).

Requirements: a Microsoft Azure subscription. A general environment setup guide is linked (shared across multiple exercises in the learning path; may include extra software not required for this specific exercise). The exercise itself is launched via an external link (`https://go.microsoft.com/fwlink/?linkid=2353605`) and is not reproduced as inline text/code on the Learn page — no code snippets are present on this unit page itself.

Tip given: after completing the exercise, if finished exploring Azure AI Agents, delete the Azure resources created during the exercise (cost-hygiene reminder).

## Knowledge check

Three multiple-choice questions appear on this unit (correct answer bolded/implied by content; module does not literally mark the answer text distinctly, but content elsewhere confirms these):

1. **What are the key steps to create a Microsoft Foundry Agent using the Microsoft Agent Framework?**
   - Deploy a custom AI model before creating an agent definition in the Azure portal.
   - Initialize the agent by defining a model in the `AgentThread` constructor.
   - **Create an `AzureAIAgentClient`, define a `ChatAgent` with instructions and tools, and create an `AgentThread` for conversations.** (correct, consistent with Unit 3's 5-step flow)

2. **Which component in the Microsoft Agent Framework manages conversation state and stores messages?**
   - **`AgentThread`** (correct — matches "session" described in Unit 3 as the container for conversation state)
   - `ChatAgent`
   - `AzureAIAgentClient`

3. **How do you add custom functionality to a Microsoft Foundry Agent in the Microsoft Agent Framework?**
   - Configure custom functions in the Azure portal and link them to the agent through connection strings.
   - **Create Python functions with proper type annotations and descriptions, then pass them to the `ChatAgent`'s tools parameter.** (correct, consistent with Unit 4's custom function tool description)
   - Modify the AI model's architecture to integrate the custom functionality directly.

These three questions confirm the exact class names used by the SDK: **`AzureAIAgentClient`** (the Foundry chat client), **`ChatAgent`** (the agent, created with instructions + tools), and **`AgentThread`** (the session/conversation-state container).

## Summary

The Microsoft Agent Framework enables developers to build AI agents. Key module takeaways:
- Learned the components and core concepts of the Microsoft Agent Framework.
- Learned how to create custom tools to extend an agent's capabilities.
- Overall goal: use the Microsoft Agent Framework to create dynamic, adaptable AI solutions that enhance user interactions and automate complex tasks.
