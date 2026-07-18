# Practice questions — Discover Azure AI Agents with A2A

## Introduction

**Q1.** According to the module introduction, what primary challenge does the Agent-to-Agent (A2A) protocol address?

A. Reducing the token cost of LLM calls
B. Coordinating discovery, communication, and task execution across remote/distributed agents
C. Improving the accuracy of retrieval-augmented generation
D. Encrypting data at rest in Azure Storage

**Answer:** B — The module states A2A "addresses this challenge by providing a standardized framework for agent discovery, communication, and coordinated task execution" for real-world tasks that require collaboration across multiple, often remote, agents. It has nothing to do with token cost, RAG accuracy, or storage encryption.

**Q2.** In the module's technical-writer example, which component coordinates the workflow between a title-generation agent and an outline-generation agent?

A. The Agent Executor
B. The Task Store
C. A routing agent
D. The Request Handler

**Answer:** C — A routing agent sends the user's request to the title agent, passes the generated title to the outline agent, and returns the final outline to the user. The Executor, Task Store, and Request Handler are server-side implementation components, not the orchestrating agent in this example.

**Q3.** Which of the following are stated benefits of implementing A2A, per the module introduction? (Choose two.)

A. Managing connections to remote agents
B. Automatically fine-tuning LLM weights
C. Delegating requests to the appropriate agent
D. Eliminating the need for authentication

**Answer:** A, C — The introduction states A2A lets you "manage connections to remote agents, delegate requests to the appropriate agent, and enable seamless, standardized, and secure communication." A2A does not fine-tune models, and it explicitly builds in (not eliminates) authentication.

**Q4.** True or false framed as MC: The module's text and video content cover identical levels of detail.

A. True — video and text are interchangeable
B. False — the text contains greater detail and should sometimes supplement the video
C. False — video contains more detail than text
D. True, but only for the exercise unit

**Answer:** B — The module note explicitly says "The text contains greater detail than the videos, so in some cases you might want to refer to it as supplemental material to the video presentation."

**Q5.** Why might a technical writing team choose an A2A-based multi-agent design over a single monolithic agent for headline and outline generation?

A. A2A requires fewer Azure resources overall
B. A2A allows each specialized agent (title, outline) to be developed, hosted, and discovered independently while a routing agent coordinates them
C. A2A agents cannot use different LLMs, simplifying governance
D. A2A removes the need for a routing/orchestration layer

**Answer:** B — This is the core motivation given: distributed collaboration among specialized agents coordinated by a routing agent. Option C is wrong — A2A explicitly allows different LLMs per agent. Option D is wrong — a routing agent is still required.

**Q6.** [General Azure knowledge] Within the broader AI-103 "Build agents by using Foundry" skill area, A2A-based orchestration is best classified as an example of which capability?

A. Retrieval-augmented generation (RAG)
B. Orchestrated multi-agent solutions
C. Content moderation and safety filtering
D. Model quota and rate-limit management

**Answer:** B — A2A is a protocol for coordinating multiple independent agents, which directly maps to "Implement orchestrated multi-agent solutions" in the exam skills outline.

## Define an A2A agent

**Q7.** What does the A2A protocol standardize between AI agents?

A. How agents are billed for compute usage
B. How agents share context, invoke each other's capabilities, and exchange information securely
C. How agents are deployed to Azure Kubernetes Service
D. How agents store embeddings in a vector index

**Answer:** B — Per the module: "It defines how agents can share context, invoke each other's capabilities, and exchange information securely." Billing, AKS deployment, and vector indexing are unrelated to A2A's purpose.

**Q8.** Which A2A protocol feature is explicitly called out as an advantage over "some MCP scenarios"?

A. A2A always uses a single shared LLM across all agents for consistency
B. A2A allows each agent to independently choose which LLM to use, unlike some MCP scenarios that rely on a single LLM connection
C. A2A does not require any authentication, simplifying setup
D. A2A only supports text input/output, unlike MCP

**Answer:** B — The module states flexible model selection lets "each A2A agent... choose which large language model (LLM) to use for handling requests, enabling optimized or fine-tuned models per agent, unlike some MCP scenarios that rely on a single LLM connection." This is the key A2A vs. MCP distinction. A is the opposite of the true statement; C is false since A2A has integrated authentication; D is not stated.

**Q9.** Which of the following are listed as key elements of an Agent Skill? (Choose three.)

A. ID
B. Endpoint URL
C. Description
D. Tags

**Answer:** A, C, D — Agent Skill elements are ID, Name, Description, Tags, Examples, and Input/Output Modes. Endpoint URL is a property of the Agent Card, not the Agent Skill — a classic exam distractor pairing the two related-but-distinct concepts.

**Q10.** What is the Agent Card most analogous to, according to the module?

A. A firewall rule set
B. A digital business card for the agent
C. A load balancer configuration
D. A vector database schema

**Answer:** B — The module explicitly describes it as "like a digital business card for your agent... a structured document that a routing agent or client can retrieve to discover your agent's capabilities and how to interact with it."

**Q11.** Which of the following are key elements of an Agent Card? (Choose three.)

A. Identity Information (name, description, version)
B. Endpoint URL
C. Examples (sample prompts)
D. Authentication Support

**Answer:** A, B, D — Agent Card elements: Identity Information, Endpoint URL, Capabilities, Default Input/Output Modes, Skills, and Authentication Support. "Examples" is a Skill-level element, not a Card-level element — this distinction is a likely exam trap.

**Q12.** A vendor's agent and a different vendor's agent need to collaborate on a task. What makes this possible under A2A?

A. Both agents must be deployed to the same Azure region
B. Both agents must use the identical LLM
C. Both agents adhere to the same standardized protocol for discovery and communication, regardless of vendor or platform
D. Both agents must share the same Task Store instance

**Answer:** C — "By adhering to the A2A protocol, agents from different vendors or platforms can work together seamlessly." Region, LLM choice, and shared Task Store are not requirements.

**Q13.** Which capability listed under an Agent Card's "Capabilities" field is explicitly mentioned as an example in the module?

A. Batch processing and cron scheduling
B. Streaming or push notifications
C. Role-based access control (RBAC) assignments
D. GPU vs. CPU compute preference

**Answer:** B — The module lists "Capabilities: Supported A2A features such as streaming or push notifications" as an Agent Card element.

**Q14.** In the "Putting it together" section, once an agent publishes its skills and Agent Card, what becomes possible? (Choose two.)

A. Other agents/clients can discover the agent automatically
B. The agent automatically retrains its underlying LLM
C. Requests can be routed to the agent's appropriate skill
D. The agent no longer requires a hosting server

**Answer:** A, C — The module states discovery becomes automatic and requests can be routed to the appropriate skill. Retraining and removing the need for hosting are not mentioned or implied — an agent still must be hosted (covered in the next unit).

## Implement an agent executor

**Q15.** What is described as "the bridge between the A2A protocol and your agent's specific business logic"?

A. The Task Store
B. The Agent Card
C. The Agent Executor
D. The ASGI server

**Answer:** C — The module states: "The Agent Executor... Think of it as the bridge between the A2A protocol and your agent's specific business logic."

**Q16.** Which interface handles all incoming requests sent to an A2A agent?

A. `RequestHandler`
B. `AgentExecutor`
C. `TaskStore`
D. `EventQueue`

**Answer:** B — "The `AgentExecutor` interface handles all incoming requests sent to your agent." `RequestHandler` (covered in the hosting unit) routes requests to the Executor's methods, but the Executor itself is the interface that processes them.

**Q17.** Which two primary operations does an Agent Executor typically define? (Choose two.)

A. Execute
B. Deploy
C. Cancel
D. Authenticate

**Answer:** A, C — "An Agent Executor typically defines two primary operations: Execute... Cancel." Deploy and Authenticate are not Executor operations per the module.

**Q18.** What does the `Execute` operation use to send results back to the client?

A. A `Task Store`
B. An `EventQueue`
C. A `RequestContext`
D. A well-known endpoint

**Answer:** B — "Sends results back via an event queue, which may include messages, task updates, or artifacts." `RequestContext` is used to understand the incoming request, not to send results out — a key distinction between the two objects the executor uses.

**Q19.** What does the executor use `RequestContext` for?

A. To store the task lifecycle persistently across server restarts
B. To understand the incoming request
C. To authenticate the calling client
D. To route the request to another agent server

**Answer:** B — "The executor uses the RequestContext to understand the incoming request and an EventQueue to communicate results or events back to the client."

**Q20.** In the "Hello World" agent request-handling flow, what is the correct order of steps?

A. Executor wraps result as event → agent's logic runs → routing mechanism responds → executor receives request
B. Executor receives request → calls agent's logic → wraps result as event on the event queue → routing mechanism sends event back to requester
C. Routing mechanism sends request → agent logic executes → Task Store persists result → client polls for result
D. Client authenticates → Agent Card is fetched → executor cancels task → result returned

**Answer:** B — This matches the four-step flow given in the module verbatim (helper class with core logic → executor receives request and calls the logic → wraps as event on event queue → routing mechanism sends event to requester).

**Q21.** For a basic/simple A2A agent, what is the typical behavior for the `Cancel` operation?

A. It always successfully cancels any in-flight task within 5 seconds
B. It may not be supported at all
C. It automatically restarts the Execute operation
D. It deletes the Agent Card from the well-known endpoint

**Answer:** B — "May not be supported for simple agents." A basic agent might simply indicate cancellation isn't supported, per the module.

**Q22.** Which statement best summarizes the role of the Agent Executor per the module's closing remarks on this unit?

A. It is optional and can be omitted for production agents
B. It is central to making the A2A agent functional, defining how it executes tasks and communicates results via a standardized interface
C. It replaces the need for an Agent Card
D. It only applies to streaming responses, not direct messages

**Answer:** B — "The Agent Executor is central to making your A2A agent functional... providing a standardized interface for clients and other agents." It does not replace the Agent Card and applies to both streaming and non-streaming interactions.

## Host an A2A server

**Q23.** At what standard/well-known endpoint is an Agent Card typically exposed?

A. `/api/v1/agent-card`
B. `/.well-known/agent-card.json`
C. `/agents/discover`
D. `/a2a/manifest.json`

**Answer:** B — The module states the Agent Card is "exposed at a standard endpoint (typically `/.well-known/agent-card.json`) so clients and other agents can discover your agent." This exact path is a high-value exam fact.

**Q24.** Which three components together form the core of an A2A agent server? (Choose three.)

A. Agent Card
B. Request Handler
C. Server Application
D. Vector Index

**Answer:** A, B, C — "To host an agent, you need three essential components working together: Agent Card, Request Handler, Server Application." A Vector Index is unrelated to A2A hosting.

**Q25.** In the Python implementation described by the module, which web framework and ASGI server are used to build and run the agent server?

A. Flask and Gunicorn
B. FastAPI and Hypercorn
C. Starlette and Uvicorn
D. Django and Daphne

**Answer:** C — "Built using a web framework (Starlette in Python)... Combined with an ASGI server (like Uvicorn) to start listening on a network interface and port." This exact pairing is explicit exam-testable detail.

**Q26.** What is the role of the Request Handler in an A2A server?

A. It stores the agent's LLM weights
B. It routes incoming requests to the appropriate methods on the Agent Executor (e.g., `execute` or `cancel`) and manages the task lifecycle via a Task Store
C. It generates the Agent Card dynamically from the LLM's system prompt
D. It replaces the ASGI server for handling HTTP traffic

**Answer:** B — "Routes incoming requests to the appropriate methods on your Agent Executor (for example, execute or cancel). Manages the task lifecycle using a Task Store."

**Q27.** What does the Task Store track?

A. Only completed tasks, for audit/compliance purposes
B. Tasks, streaming data, and resubscriptions
C. The Agent Card's version history
D. Billing and quota consumption per agent

**Answer:** B — "Manages the task lifecycle using a Task Store, which tracks tasks, streaming data, and resubscriptions. Even simple agents require a task store to handle interactions reliably."

**Q28.** True/false-style MC: Simple "Hello World" A2A agents can skip using a Task Store since they don't have complex task lifecycles.

A. True — Task Stores are only needed for streaming agents
B. False — even simple agents require a task store to handle interactions reliably
C. True — Task Stores are only required when authentication is enabled
D. False — Task Stores are only required in production, not in "Hello World" examples

**Answer:** B — The module explicitly states: "Even simple agents require a task store to handle interactions reliably."

**Q29.** Put the A2A server setup steps in the correct order: (1) Start the server with Uvicorn, (2) Define skills and Agent Card, (3) Initialize a request handler linking the Executor and Task Store, (4) Set up the server application with the Agent Card and request handler.

A. 2, 3, 4, 1
B. 1, 2, 3, 4
C. 2, 4, 3, 1
D. 3, 2, 4, 1

**Answer:** A — Module order: "1. Define your agent's skills and Agent Card. 2. Initialize a request handler that links your Agent Executor with a Task Store. 3. Set up the server application, providing the Agent Card and request handler. 4. Start the server using an ASGI server (Uvicorn)."

**Q30.** What can an Agent Card include for authenticated users, per the hosting unit?

A. A second, "extended" card
B. An encrypted binary payload
C. A duplicate Task Store
D. A separate ASGI server instance

**Answer:** A — "Can include multiple versions or an 'extended' card for authenticated users."

## Connect to your A2A agent

**Q31.** What must a client know before it can connect to an A2A agent server?

A. The agent's LLM provider API key only
B. The base URL of the server
C. The full source code of the Agent Executor
D. The Task Store's internal schema

**Answer:** B — "The client must know the base URL of the server." It then retrieves the Agent Card from a well-known endpoint on that server.

**Q32.** How does a client typically obtain metadata about an A2A agent before interacting with it?

A. By querying the agent's underlying LLM directly
B. By retrieving the Agent Card from a well-known endpoint on the server
C. By requesting the Task Store's contents
D. By inspecting the server's TLS certificate

**Answer:** B — "The client typically retrieves the Agent Card from a well-known endpoint on the server. Once the Agent Card is obtained, the client can be initialized with it."

**Q33.** What is the key difference between Non-Streaming and Streaming requests in A2A?

A. Non-Streaming requests are only used for authentication handshakes
B. Non-Streaming: client sends a message and waits for a complete response; Streaming: client receives responses incrementally as the agent processes the request
C. Streaming requests never use an event queue
D. Non-Streaming requests cannot include a `role` field

**Answer:** B — This matches the module's definitions exactly: non-streaming is suitable for simple/single-response interactions, streaming is useful for long-running tasks or real-time updates.

**Q34.** What field do A2A requests usually include to indicate who is sending the message (e.g., "user")?

A. `sender`
B. `role`
C. `origin`
D. `principal`

**Answer:** B — "In both cases, requests usually include a role (for example, user) and the message content."

**Q35.** What may more complex A2A agents return instead of an immediate message?

A. A raw HTTP 202 with no body
B. A task object, allowing for task tracking or cancellation
C. A signed JWT only
D. A redirect to a different Agent Card

**Answer:** B — "More complex agents may return task objects instead of immediate messages, allowing for task tracking or cancellation."

**Q36.** An A2A client receives a task-based response rather than a direct message. What should the client be prepared to do?

A. Discard the response, since only direct messages are valid
B. Make follow-up calls to check status or retrieve results
C. Immediately terminate the connection
D. Re-send the original request with a new role

**Answer:** B — "Task-based responses: Objects representing ongoing tasks, which may require follow-up calls to check status or retrieve results. Clients should be prepared to handle both response types."

**Q37.** Which two statements about interacting with an A2A agent are accurate per the module? (Choose two.)

A. Each request should be uniquely identifiable, often using a generated ID
B. Streaming responses are synchronous and always return the full result at once
C. Streaming responses are asynchronous and may provide partial results before the final output
D. Simple agents always manage multiple tasks simultaneously

**Answer:** A, C — Both are stated directly. B contradicts the module (streaming is asynchronous with partial results, not synchronous/full-at-once). D is backwards — simple agents "may return messages directly," while advanced agents manage multiple tasks.

## Exercise - Connect to remote Azure AI Agents with the A2A protocol

**Q38.** What does the hands-on exercise in this module ask learners to build?

A. A speech-to-text pipeline using Azure AI Speech
B. An A2A client-server application that interacts with remote Azure AI Agents
C. A Content Understanding analyzer for documents
D. A RAG pipeline using Azure AI Search

**Answer:** B — Per the exercise unit: "you can complete this exercise to develop an A2A client-server application that interacts with remote agents."

**Q39.** What is required to complete this exercise?

A. A GitHub Copilot license
B. An Azure subscription
C. A Microsoft 365 E5 license
D. A pre-existing Foundry Agent Service deployment with GPT-4

**Answer:** B — "If you have an Azure subscription, you can complete this exercise..." The unit also notes a free account with 30-day credits is available if the learner doesn't already have a subscription.

**Q40.** [General Azure knowledge] What benefit does a free Azure account referenced in the exercise unit provide to new users?

A. Unlimited free compute forever
B. Credits for the first 30 days
C. A permanent free Foundry Agent Service tier
D. Free GPU quota with no expiration

**Answer:** B — The module links to signing up for an account "which includes credits for the first 30 days," consistent with general Azure free-account knowledge.

**Q41.** Approximately how long does the module estimate this exercise will take?

A. 5 minutes
B. 15 minutes
C. 30 minutes
D. 60 minutes

**Answer:** C — The unit page lists a duration of 30 minutes.

**Q42.** Conceptually, which units' content does the exercise most directly apply hands-on? (Choose two.)

A. "Host an A2A server"
B. "Implement responsible AI" (a different exam domain entirely)
C. "Connect to your A2A agent"
D. "Implement computer vision solutions" (a different exam domain entirely)

**Answer:** A, C — The exercise has learners build and connect to an A2A client-server application, directly applying the hosting (server, Agent Card, Request Handler) and client-connection (Agent Card discovery, sending requests) concepts from those two units. B and D belong to unrelated AI-103 domains.

## Module assessment (Knowledge check)

**Q43.** Per the module's own knowledge check, what is the primary role of an A2A server?

A. It executes business logic for the agent directly
B. It routes requests between clients and connected agents
C. It stores static agent responses for reuse
D. It generates the agent's Agent Skills automatically

**Answer:** B — This is the module's own stated correct answer, consistent with the Request Handler's job of routing requests to the Executor's `execute`/`cancel` methods.

**Q44.** Per the module's knowledge check, what does the Agent Executor do?

A. Manages network connections between clients and servers
B. Processes incoming requests and generates responses or events
C. Provides a GUI for monitoring agent activity
D. Persists the Task Store to disk

**Answer:** B — Matches the module's stated correct answer and the Unit 3 definition verbatim.

**Q45.** Per the module's knowledge check, what is an Agent Card used for?

A. It stores the agent's API key for authentication
B. It provides metadata about the agent, such as its capabilities and available functions
C. It visualizes the agent's workflow in a GUI dashboard
D. It defines the ASGI server's port configuration

**Answer:** B — Matches the module's stated correct answer and the "digital business card" definition from Unit 2.

**Q46.** Why is "It executes business logic for the agent directly" an incorrect answer for the role of an A2A server?

A. Because business logic execution is the responsibility of the Agent Executor, not the server/Request Handler itself
B. Because A2A servers never execute any code
C. Because business logic is handled exclusively by the Task Store
D. Because only the Agent Card can execute logic

**Answer:** A — The server (via the Request Handler) routes requests to the Agent Executor, which is the component that actually implements business logic — a subtle but exam-relevant separation of concerns.

**Q47.** Why is "It stores the agent's API key for authentication" an incorrect description of the Agent Card?

A. Because the Agent Card only contains metadata/capabilities information (identity, endpoint, capabilities, skills, auth support flag) — not raw credentials
B. Because Agent Cards are never used with authenticated agents
C. Because API keys are stored in the Task Store instead
D. Because the Agent Card is encrypted and thus cannot store any authentication-related info

**Answer:** A — The Agent Card indicates *whether* authentication is required ("Authentication Support") but is a discovery/metadata document, not a credential store.

## Summary

**Q48.** According to the module summary, how are agents discovered and communicated with dynamically?

A. Using the Agent Card
B. Using a shared central LLM registry
C. Using DNS TXT records
D. Using the Task Store's public API

**Answer:** A — "you explored how agents are discovered and communicated with dynamically using the Agent Card."

**Q49.** Which two message-flow modes between clients and agents are highlighted in the summary? (Choose two.)

A. Streaming
B. Non-streaming
C. Batch-only
D. Polling-only

**Answer:** A, B — "how messages—both streaming and non-streaming—flow between clients and agents." Batch-only and polling-only are not terms used in the module.

**Q50.** What capability does the summary say these A2A concepts (Agent Card, executors, streaming/non-streaming messaging) ultimately enable?

A. Building flexible, discoverable agent networks that can delegate tasks and respond to requests across distributed environments
B. Eliminating the need for any server hosting
C. Automatically merging multiple agents into a single monolithic model
D. Replacing the need for Foundry Agent Service entirely

**Answer:** A — This is the module's closing statement verbatim. It does not claim to eliminate hosting or replace Foundry Agent Service — A2A is a communication/discovery layer, not a replacement for the underlying agent hosting platform.

**Q51.** Based on the whole module, which statement most precisely distinguishes A2A's purpose from MCP's purpose? [general Azure knowledge reinforced by module's explicit MCP comparison]

A. A2A connects an agent to external tools and data sources; MCP connects independent agents to each other
B. A2A connects independent agents to each other for discovery, communication, and coordinated task execution; MCP connects an agent to external tools/data sources
C. A2A and MCP are two names for the same protocol
D. A2A is only used within a single Azure subscription, while MCP works across subscriptions

**Answer:** B — The module frames A2A entirely around agent-to-agent discovery (Agent Card), communication, and coordinated task execution among independent/remote agents, explicitly contrasting it with "some MCP scenarios that rely on a single LLM connection" (MCP's typical role is tool/data integration for a single agent). A reverses the definitions; C and D are false.

**Q52.** Which of the following would most likely appear as an AI-103 exam scenario testing this module's content?

A. Configuring Azure Content Understanding to extract layout from a PDF
B. Designing a solution where a "coordinator" agent must discover and invoke two independently hosted specialist agents built by different teams, each exposing its own Agent Card at `/.well-known/agent-card.json`
C. Tuning temperature and top-p parameters for a single chat completion call
D. Configuring semantic search ranking in Azure AI Search

**Answer:** B — This scenario directly requires knowledge of Agent Cards, the well-known discovery endpoint, and multi-agent orchestration via A2A — the core subject of this module. A, C, and D belong to other AI-103 domains (Content Understanding/information extraction, prompt/parameter tuning, and RAG/search respectively).
