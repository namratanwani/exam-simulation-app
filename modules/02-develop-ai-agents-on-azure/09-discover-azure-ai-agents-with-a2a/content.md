# Discover Azure AI Agents with A2A

Source: https://learn.microsoft.com/en-us/training/modules/discover-agents-with-a2a/

## Learning objectives

After completing this module, you're able to:

- Understand the A2A protocol and its role in multi-agent orchestration.
- Design discoverable agents for modular, collaborative problem-solving.
- Implement A2A strategies to discover and invoke remote agents.

**Prerequisites:** Experience with deploying generative AI models in Microsoft Foundry; programming experience.

**Module facts:** 8 units, Intermediate level. Roles: AI Engineer, Developer, Solution Architect, Student. Product: Foundry Tools.

Module description: "Learn how to implement the A2A protocol to enable agent discovery, direct communication, and coordinated task execution across remote agents."

## Exam relevance

This module maps to the **Implement generative AI and agentic solutions (30–35%)** domain, specifically the **"Build agents by using Foundry"** skill group:

- **"Implement orchestrated multi-agent solutions"** — A2A is a standardized protocol specifically for coordinating and orchestrating independent, potentially remote agents (e.g., a routing agent delegating to a title-generation agent and an outline-generation agent).
- **"Define agent roles, goals, conversation-tracking approach, and tool schemas"** — Agent Skills and Agent Cards are the mechanism by which an A2A agent declares its role/capabilities to other agents.
- **"Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions"** — relevant for distinguishing A2A (agent-to-agent communication) from tool/data integration patterns like MCP.

It also touches the **"Choose the appropriate Foundry services for generative AI and agents"** skill group under **Plan and manage an Azure AI solution**, specifically **"Choose appropriate memory, tool, and knowledge integration services for agent solutions"** — because A2A is one of the key protocol choices (alongside MCP) when designing how agents interconnect.

**Critical distinction for the exam: A2A vs. MCP**
- **A2A (Agent-to-Agent) protocol** = agent-to-**agent** interoperability. It standardizes how independent agents (potentially from different vendors/platforms) **discover** each other (via an Agent Card), **communicate**, and **coordinate task execution**. Each A2A agent can use its own LLM.
- **MCP (Model Context Protocol)** = agent-to-**tool/data** integration. It connects a single agent to external tools, APIs, and knowledge stores, typically relying on a single LLM connection to interpret and call those tools.
- Per the module: A2A's flexible model selection lets "each A2A agent choose which large language model (LLM) to use for handling requests... unlike some MCP scenarios that rely on a single LLM connection."

## Introduction

AI agents are powerful individually, but many real-world tasks require **collaboration across multiple agents**. Coordinating these interactions manually is complex, especially when agents are remote or distributed.

The **Agent-to-Agent (A2A) protocol** addresses this by providing a **standardized framework for agent discovery, communication, and coordinated task execution**. Implementing A2A lets you:
- Manage connections to remote agents.
- Delegate requests to the appropriate agent.
- Enable seamless, standardized, and secure communication between agents.

**Example scenario used throughout the module:** A technical writer wants to create blog content. One agent generates compelling article headlines; another creates detailed outlines. Using A2A, a **routing agent** coordinates the workflow:
1. Sends the user's request to the title agent.
2. Passes the generated title to the outline agent.
3. Returns the final outline to the user — all automatically.

The module teaches implementing A2A with Azure AI Agents, including configuring a routing agent, registering remote agents, and building a coordinated multi-agent workflow.

Note: the module offers both video and text formats; text contains more detail.

## Define an A2A agent

The **Agent-to-Agent (A2A) protocol** is a standardized way for AI agents to communicate and collaborate with each other. It defines how agents can **share context, invoke each other's capabilities, and exchange information securely**. Agents from different vendors or platforms can interoperate because they adhere to the same protocol.

Before an A2A agent can participate in multi-agent workflows, it must explain what it can do. This is done via:
- **Agent Skills** — the specific capabilities the agent exposes.
- **Agent Card** — the discovery document listing those capabilities (and how to invoke them) for other agents/clients.

### Advantages of the A2A protocol

- **Enhanced Collaboration:** Agents from different vendors/platforms can share context and work together, enabling automation across systems that are traditionally disconnected.
- **Flexible Model Selection:** Each A2A agent independently chooses which LLM to use for handling requests — enabling optimized or fine-tuned models per agent — **unlike some MCP scenarios that rely on a single LLM connection**. (This is the key A2A-vs-MCP distinguishing point called out explicitly in the source material.)
- **Integrated Authentication:** Authentication is built into the A2A protocol itself, providing a robust security framework for secure agent-to-agent communication.

### Agent Skills

An **Agent Skill** describes a specific capability or function the agent can perform — a building block that tells clients/other agents what tasks the agent can handle.

Key elements of an Agent Skill:
- **ID** — unique identifier for the skill.
- **Name** — human-readable name describing the skill.
- **Description** — detailed explanation of what the skill does.
- **Tags** — keywords for categorization and discovery.
- **Examples** — sample prompts or use cases illustrating the skill.
- **Input/Output Modes** — supported data formats or media types (e.g., text, JSON).

Example: a simple "Hello World" skill returns a basic greeting in text format; a blog-writing skill might accept a topic and return a suggested title or outline.

### Agent Card

The **Agent Card** is described as "a digital business card for your agent" — a structured document a routing agent or client retrieves to discover the agent's capabilities and how to interact with it.

Key elements of an Agent Card:
- **Identity Information** — name, description, version of the agent.
- **Endpoint URL** — where the agent's A2A service can be accessed.
- **Capabilities** — supported A2A features such as streaming or push notifications.
- **Default Input/Output Modes** — the primary media types the agent can handle.
- **Skills** — a list of the agent's skills that other agents can invoke.
- **Authentication Support** — indicates if the agent requires credentials for access.

An accurate Agent Card lets clients/routing agents discover the agent, understand its capabilities, and interact with it appropriately.

### Putting it together

Once an agent defines skills and publishes an Agent Card:
- Other agents/clients can discover the agent automatically.
- Requests can be routed to the agent's appropriate skill.
- Responses return in supported formats, enabling smooth multi-agent collaboration.

In the technical-writer example: one agent defines skills for generating article titles, another for creating outlines. The routing agent retrieves each agent's Agent Card to discover these capabilities and orchestrates the workflow — a title from one agent feeds into the outline agent, producing the final response.

## Implement an agent executor

The **Agent Executor** is a core component of an A2A agent. It defines how the agent **processes incoming requests, generates responses, and communicates with clients or other agents** — the bridge between the A2A protocol and the agent's specific business logic.

### Understand the Agent Executor

The **`AgentExecutor`** interface handles all incoming requests sent to the agent. It receives request information, processes it per the agent's capabilities, and sends responses/events back through a communication channel.

**Key responsibilities:**
- Execute tasks requested by users or other agents.
- Stream responses or send individual messages back to the client.
- Handle task cancellation if supported.

### Implement the interface

An Agent Executor typically defines two primary operations:

**`Execute`**
- Processes incoming requests and generates responses.
- Accesses request details (e.g., user input, task context).
- Sends results back via an **event queue**, which may include messages, task updates, or artifacts.

**`Cancel`**
- Handles requests to cancel an ongoing task.
- May not be supported for simple agents.

The executor uses:
- **`RequestContext`** — to understand the incoming request.
- **`EventQueue`** — to communicate results or events back to the client.

### Request handling flow ("Hello World" example)

1. The agent has a small helper class implementing its core logic (e.g., returning a string).
2. The executor receives a request and calls the agent's logic.
3. The executor wraps the result as an event and places it on the event queue.
4. The routing mechanism sends the event back to the requester.

For cancellation, a basic agent might simply indicate that cancellation isn't supported.

**Summary point:** The Agent Executor is central to making an A2A agent functional — it defines how the agent executes tasks and communicates results via a standardized interface, enabling seamless integration in multi-agent workflows.

## Host an A2A server

Once an agent defines its skills and Agent Card, it must be **hosted on a server** to be accessible to clients and other agents over HTTP, enabling real-time interactions and multi-agent workflows.

Hosting an agent allows it to:
- Expose its capabilities through its **Agent Card**, discoverable by clients/other agents.
- Receive incoming A2A requests and forward them to the **Agent Executor** for processing.
- Manage **task lifecycles**, including streaming responses and stateful interactions.

The server acts as the bridge between the agent's logic and the external world.

### Core components of the agent server

**Agent Card**
- Describes the agent's capabilities, skills, and input/output modes.
- Exposed at a **standard/well-known endpoint**, typically **`/.well-known/agent-card.json`**, so clients and other agents can discover the agent.
- Can include multiple versions or an **"extended" card** for authenticated users.

**Request Handler**
- Routes incoming requests to the appropriate methods on the **Agent Executor** (e.g., **`execute`** or **`cancel`**).
- Manages the task lifecycle using a **Task Store**, which tracks tasks, streaming data, and resubscriptions.
- Even simple agents require a task store to handle interactions reliably.

**Server Application**
- Built using a web framework — **Starlette** in Python.
- Combined with an **ASGI server** — **Uvicorn** — to listen on a network interface and port.
- Exposes the agent card and request handler endpoints for client interaction.

### Set up the A2A agent server (steps)

1. Define your agent's skills and Agent Card.
2. Initialize a **request handler** that links your Agent Executor with a **Task Store**.
3. Set up the **server application**, providing the Agent Card and request handler.
4. Start the server using an **ASGI server (Uvicorn)** to make it network-accessible.
5. Once running, the agent listens for incoming requests and responds according to its defined skills.

Example: a "Hello World" agent exposes a basic greeting skill; once hosted, it responds to requests sent to its endpoint. More complex agents can serve multiple skills or an extended Agent Card for authenticated users.

**Summary point:** Hosting an A2A agent combines the Agent Card, request handler, and agent executor to make it available for client/agent interactions, ensuring tasks are managed correctly and responses delivered reliably.

## Connect to your A2A agent

Once an A2A agent server is running, a **client** acts as the bridge between an application and the agent server.

Client responsibilities:
- Discovering the **Agent Card**, which contains metadata about the agent and its endpoints.
- Sending requests to the agent for processing.
- Receiving and interpreting the agent's responses (direct messages or task-based results).

### Connect to your agent server

- The client must know the **base URL** of the server.
- The client typically retrieves the **Agent Card from a well-known endpoint** on the server.
- Once the Agent Card is obtained, the client is initialized with it, establishing a connection ready to send messages.

### Send requests to the agent

Two main request types:
- **Non-Streaming Requests:** the client sends a message and waits for a complete response — suitable for simple interactions or when a single response is expected.
- **Streaming Requests:** the client sends a message and receives responses incrementally as the agent processes it — useful for long-running tasks or real-time updates.

In both cases, requests usually include a **`role`** (e.g., `user`) and the message content. More complex agents may return **task objects** instead of immediate messages, allowing task tracking or cancellation.

### Handle the agent response

Agent responses may include:
- **Direct messages:** immediate outputs (text or structured content).
- **Task-based responses:** objects representing ongoing tasks, which may require follow-up calls to check status or retrieve results.

Clients must handle both response types and interpret returned data appropriately.

### Interacting with the agent

- Each request should be uniquely identifiable, often using a generated ID.
- Streaming responses are asynchronous and may provide partial results before the final output.
- Simple agents may return messages directly; advanced agents may manage multiple tasks simultaneously.

**Summary point:** Connecting a client to an agent server involves fetching the Agent Card, establishing a connection, sending requests, and handling responses — enabling interaction with remote agents for both simple messages and complex task management.

## Exercise - Connect to remote Azure AI Agents with the A2A protocol

Hands-on exercise (requires Azure subscription; free trial includes credits for first 30 days) to build an **A2A client-server application** that interacts with remote agents. Learners launch the exercise via a linked lab environment (external Microsoft Learn sandbox link) and follow guided instructions to implement what was covered in units 2–5: defining an agent, implementing an executor, hosting the A2A server, and connecting a client.

Duration: 30 minutes.

## Module assessment (Knowledge check)

The module's built-in assessment posed these three questions (options as listed on the page; correct answers per module content are noted based on unit definitions):

1. **What is the primary role of an A2A server?**
   - It executes business logic for the agent directly.
   - **It routes requests between clients and connected agents.** *(matches "Request Handler routes incoming requests to the appropriate methods on your Agent Executor")*
   - It stores static agent responses for reuse.

2. **What does the Agent Executor do in an A2A agent?**
   - Manages network connections between clients and servers.
   - **Processes incoming requests and generates responses or events.** *(matches Unit 3 definition verbatim)*
   - Provides a GUI for monitoring agent activity.

3. **What is an agent card used for in A2A?**
   - It stores the agent's API key for authentication.
   - **It provides metadata about the agent, such as its capabilities and available functions.** *(matches Unit 2 "digital business card" definition)*
   - It visualizes the agent's workflow in a GUI dashboard.

## Summary

This module covered connecting Python clients to Azure AI Agents using the **Agent-to-Agent (A2A) protocol**. Key takeaways:

- Agents are **discovered and communicated with dynamically using the Agent Card**.
- **Executors** handle agent requests (via `Execute`/`Cancel` and `RequestContext`/`EventQueue`).
- Messages flow between clients and agents in **streaming** and **non-streaming** modes.
- These concepts enable building **flexible, discoverable agent networks** that can delegate tasks and respond to requests across distributed environments — i.e., true multi-agent orchestration across independent agents, as opposed to a single agent calling tools.
