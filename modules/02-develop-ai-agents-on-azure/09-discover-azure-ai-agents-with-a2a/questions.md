# Practice questions — Discover Azure AI Agents with A2A

## Introduction

**Q1.** According to the module introduction, what primary challenge does the Agent-to-Agent (A2A) protocol address?

A. Reducing the token cost of LLM calls across every deployed agent
B. Coordinating discovery, communication, and task execution across remote/distributed agents
C. Improving the accuracy of retrieval-augmented generation over enterprise data
D. Encrypting data at rest in Azure Storage for compliance purposes

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

A. True — video and text are fully interchangeable in every unit
B. False — the text contains greater detail and should sometimes supplement the video
C. False — video contains more detail than the accompanying text
D. True, but only for the exercise unit specifically covered later

**Answer:** B — The module note explicitly says "The text contains greater detail than the videos, so in some cases you might want to refer to it as supplemental material to the video presentation."

**Q5.** Why might a technical writing team choose an A2A-based multi-agent design over a single monolithic agent for headline and outline generation?

A. A2A requires fewer Azure resources overall compared to a single monolithic agent design handling everything
B. A2A allows each specialized agent (title, outline) to be developed, hosted, and discovered independently while a routing agent coordinates them
C. A2A agents cannot use different LLMs from each other, which is claimed to simplify governance overhead
D. A2A removes the need for a routing/orchestration layer entirely between specialist agents in the workflow

**Answer:** B — This is the core motivation given: distributed collaboration among specialized agents coordinated by a routing agent. Option C is wrong — A2A explicitly allows different LLMs per agent. Option D is wrong — a routing agent is still required.

**Q6.** [General Azure knowledge] Within the broader AI-103 "Build agents by using Foundry" skill area, A2A-based orchestration is best classified as an example of which capability?

A. Retrieval-augmented generation (RAG)
B. Orchestrated multi-agent solutions
C. Content moderation and safety filtering
D. Model quota and rate-limit management

**Answer:** B — A2A is a protocol for coordinating multiple independent agents, which directly maps to "Implement orchestrated multi-agent solutions" in the exam skills outline.

**Q53.** How many units does this module contain, and at what level is it classified?
A. 8 units, Intermediate level
B. 5 units, Beginner level
C. 11 units, Advanced level
D. 6 units, Intermediate level
**Answer:** A — The module facts state 8 units at Intermediate level, for roles AI Engineer, Developer, Solution Architect, and Student, tagged under product "Foundry Tools."

## Define an A2A agent

**Q7.** What does the A2A protocol standardize between AI agents?

A. How agents are billed for compute usage across a shared Foundry project subscription
B. How agents share context, invoke each other's capabilities, and exchange information securely
C. How agents are deployed to Azure Kubernetes Service clusters for scaling purposes
D. How agents store embeddings in a vector index for later semantic retrieval

**Answer:** B — Per the module: "It defines how agents can share context, invoke each other's capabilities, and exchange information securely." Billing, AKS deployment, and vector indexing are unrelated to A2A's purpose.

**Q8.** Which A2A protocol feature is explicitly called out as an advantage over "some MCP scenarios"?

A. A2A always uses a single shared LLM across all agents for consistency and centralized governance
B. A2A allows each agent to independently choose which LLM to use, unlike some MCP scenarios that rely on a single LLM connection
C. A2A does not require any authentication at all between agents, simplifying initial setup work
D. A2A only supports text input/output modes between agents, unlike MCP's richer format support

**Answer:** B — The module states flexible model selection lets "each A2A agent... choose which large language model (LLM) to use for handling requests, enabling optimized or fine-tuned models per agent, unlike some MCP scenarios that rely on a single LLM connection." This is the key A2A vs. MCP distinction. A is the opposite of the true statement; C is false since A2A has integrated authentication; D is not stated.

**Q9.** Which of the following are listed as key elements of an Agent Skill? (Choose three.)

A. ID
B. Endpoint URL
C. Description
D. Tags

**Answer:** A, C, D — Agent Skill elements are ID, Name, Description, Tags, Examples, and Input/Output Modes. Endpoint URL is a property of the Agent Card, not the Agent Skill — a classic exam distractor pairing the two related-but-distinct concepts.

**Q10.** What is the Agent Card most analogous to, according to the module?

A. A firewall rule set governing network access
B. A digital business card for the agent
C. A load balancer configuration
D. A vector database schema for embeddings

**Answer:** B — The module explicitly describes it as "like a digital business card for your agent... a structured document that a routing agent or client can retrieve to discover your agent's capabilities and how to interact with it."

**Q11.** Which of the following are key elements of an Agent Card? (Choose three.)

A. Identity Information (name, description, version)
B. Endpoint URL
C. Examples (sample prompts)
D. Authentication Support

**Answer:** A, B, D — Agent Card elements: Identity Information, Endpoint URL, Capabilities, Default Input/Output Modes, Skills, and Authentication Support. "Examples" is a Skill-level element, not a Card-level element — this distinction is a likely exam trap.

**Q12.** A vendor's agent and a different vendor's agent need to collaborate on a task. What makes this possible under A2A?

A. Both agents must be deployed to the exact same Azure region and Azure subscription to interoperate
B. Both agents must use the identical underlying LLM and model deployment configuration to interoperate
C. Both agents adhere to the same standardized protocol for discovery and communication, regardless of vendor or platform
D. Both agents must share the exact same Task Store instance across both independent servers to interoperate

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

**Q54.** Which A2A advantage does the module describe as providing "a robust security framework for secure agent-to-agent communication" built directly into the protocol itself, rather than bolted on separately?
A. Enhanced Collaboration
B. Flexible Model Selection
C. Integrated Authentication
D. Task Store persistence
**Answer:** C — "Integrated Authentication: Authentication is built into the A2A protocol itself, providing a robust security framework for secure agent-to-agent communication." Enhanced Collaboration is about cross-vendor interoperability, and Flexible Model Selection is about per-agent LLM choice — distinct advantages.

**Q55.** What is the distinction between the "Input/Output Modes" listed as an Agent Skill element and the "Default Input/Output Modes" listed as an Agent Card element?
A. There is no distinction at all between the two fields; they are simply the same field duplicated for redundancy across both the Skill and Card levels
B. Skill-level Input/Output Modes describe the data formats supported by that specific capability; Card-level Default Input/Output Modes describe the agent's primary media types overall
C. Skill-level modes are assumed to apply only to streaming interactions; Card-level modes are assumed to apply only to non-streaming ones
D. Only the Card-level field is ever actually populated in practice by implementers; the Skill-level field is assumed deprecated and effectively unused
**Answer:** B — Each Agent Skill lists its own supported Input/Output Modes (formats/media types for that capability), while the Agent Card's Default Input/Output Modes describe the agent's primary media types at the whole-agent level — a skill-specific vs. agent-wide distinction worth not confusing on the exam.

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
D. Client authenticates first → Agent Card is fetched → executor cancels the task → result is returned

**Answer:** B — This matches the four-step flow given in the module verbatim (helper class with core logic → executor receives request and calls the logic → wraps as event on event queue → routing mechanism sends event to requester).

**Q21.** For a basic/simple A2A agent, what is the typical behavior for the `Cancel` operation?

A. It always successfully cancels any in-flight task within 5 seconds
B. It may not be supported at all
C. It automatically restarts the Execute operation
D. It deletes the Agent Card from the well-known endpoint

**Answer:** B — "May not be supported for simple agents." A basic agent might simply indicate cancellation isn't supported, per the module.

**Q22.** Which statement best summarizes the role of the Agent Executor per the module's closing remarks on this unit?

A. It is entirely optional and can be safely omitted for production-grade, customer-facing agents
B. It is central to making the A2A agent functional, defining how it executes tasks and communicates results via a standardized interface
C. It replaces the need for an Agent Card entirely once it has been implemented and deployed on the server
D. It only applies to streaming responses and never applies to direct, non-streaming message responses

**Answer:** B — "The Agent Executor is central to making your A2A agent functional... providing a standardized interface for clients and other agents." It does not replace the Agent Card and applies to both streaming and non-streaming interactions.

## Host an A2A server

**Q23.** At what standard/well-known endpoint is an Agent Card typically exposed?

A. `/api/v1/agent-card` endpoint path
B. `/.well-known/agent-card.json`
C. `/agents/discover` endpoint path
D. `/a2a/manifest.json` endpoint path

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

A. It stores the agent's LLM weights and fine-tuning checkpoints directly on the server's local disk storage volume
B. It routes incoming requests to the appropriate methods on the Agent Executor (e.g., `execute` or `cancel`) and manages the task lifecycle via a Task Store
C. It generates the Agent Card dynamically from the underlying LLM's system prompt at each incoming request time
D. It replaces the ASGI server entirely, handling all raw HTTP traffic on its own without needing Uvicorn at all

**Answer:** B — "Routes incoming requests to the appropriate methods on your Agent Executor (for example, execute or cancel). Manages the task lifecycle using a Task Store."

**Q27.** What does the Task Store track?

A. Only completed tasks, for audit/compliance purposes
B. Tasks, streaming data, and resubscriptions
C. The Agent Card's version history
D. Billing and quota consumption per agent

**Answer:** B — "Manages the task lifecycle using a Task Store, which tracks tasks, streaming data, and resubscriptions. Even simple agents require a task store to handle interactions reliably."

**Q28.** True/false-style MC: Simple "Hello World" A2A agents can skip using a Task Store since they don't have complex task lifecycles.

A. True — Task Stores are only needed for streaming agents, not simple ones
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

A. By querying the agent's underlying LLM directly for its own metadata
B. By retrieving the Agent Card from a well-known endpoint on the server
C. By requesting the Task Store's contents over an unauthenticated endpoint
D. By inspecting the server's TLS certificate for embedded metadata

**Answer:** B — "The client typically retrieves the Agent Card from a well-known endpoint on the server. Once the Agent Card is obtained, the client can be initialized with it."

**Q33.** What is the key difference between Non-Streaming and Streaming requests in A2A?

A. Non-Streaming requests are only ever used for the initial authentication handshake between the client and server
B. Non-Streaming: client sends a message and waits for a complete response; Streaming: client receives responses incrementally as the agent processes the request
C. Streaming requests never use an event queue at all to deliver incremental results back to the requesting client
D. Non-Streaming requests cannot include a `role` field identifying the sender of the message at all, per this claim

**Answer:** B — This matches the module's definitions exactly: non-streaming is suitable for simple/single-response interactions, streaming is useful for long-running tasks or real-time updates.

**Q34.** What field do A2A requests usually include to indicate who is sending the message (e.g., "user")?

A. `sender`
B. `role`
C. `origin`
D. `principal`

**Answer:** B — "In both cases, requests usually include a role (for example, user) and the message content."

**Q35.** What may more complex A2A agents return instead of an immediate message?

A. A raw HTTP 202 status code with an entirely empty response body
B. A task object, allowing for task tracking or cancellation
C. A signed JWT only, with no other accompanying data
D. A redirect pointing to a completely different Agent Card endpoint

**Answer:** B — "More complex agents may return task objects instead of immediate messages, allowing for task tracking or cancellation."

**Q36.** An A2A client receives a task-based response rather than a direct message. What should the client be prepared to do?

A. Discard the response, since only direct messages are valid
B. Make follow-up calls to check status or retrieve results
C. Immediately terminate the connection without any follow-up
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

A. A speech-to-text pipeline built using Azure AI Speech services
B. An A2A client-server application that interacts with remote Azure AI Agents
C. A Content Understanding analyzer for extracting fields from documents
D. A RAG pipeline built using Azure AI Search for retrieval

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
D. Persists the Task Store's contents to disk for durability

**Answer:** B — Matches the module's stated correct answer and the Unit 3 definition verbatim.

**Q45.** Per the module's knowledge check, what is an Agent Card used for?

A. It stores the agent's API key directly for authentication purposes
B. It provides metadata about the agent, such as its capabilities and available functions
C. It visualizes the agent's internal workflow in a GUI dashboard
D. It defines the ASGI server's port configuration for deployment

**Answer:** B — Matches the module's stated correct answer and the "digital business card" definition from Unit 2.

**Q46.** Why is "It executes business logic for the agent directly" an incorrect answer for the role of an A2A server?

A. Because business logic execution is the responsibility of the Agent Executor, not the server/Request Handler itself
B. Because A2A servers are assumed to never execute any code at all under any circumstances
C. Because business logic is assumed to be handled exclusively by the Task Store instead
D. Because only the Agent Card is assumed to be able to execute logic in this architecture

**Answer:** A — The server (via the Request Handler) routes requests to the Agent Executor, which is the component that actually implements business logic — a subtle but exam-relevant separation of concerns.

**Q47.** Why is "It stores the agent's API key for authentication" an incorrect description of the Agent Card?

A. Because the Agent Card only contains metadata/capabilities information (identity, endpoint, capabilities, skills, auth support flag) — not raw credentials
B. Because Agent Cards are assumed to never be used with authenticated agents at all in this hosting architecture
C. Because API keys are assumed to be stored inside the Task Store instead of inside the Agent Card itself, per this claim
D. Because the Agent Card is assumed to be fully encrypted and thus cannot store any authentication-related metadata

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
B. Eliminating the need for any server hosting of the agent whatsoever, per this option's claim
C. Automatically merging multiple independent agents into a single monolithic model at runtime
D. Replacing the need for Foundry Agent Service entirely as the underlying hosting platform for every agent

**Answer:** A — This is the module's closing statement verbatim. It does not claim to eliminate hosting or replace Foundry Agent Service — A2A is a communication/discovery layer, not a replacement for the underlying agent hosting platform.

**Q51.** Based on the whole module, which statement most precisely distinguishes A2A's purpose from MCP's purpose? [general Azure knowledge reinforced by module's explicit MCP comparison]

A. A2A connects a single agent to external tools and data sources; MCP connects independent agents to each other instead
B. A2A connects independent agents to each other for discovery, communication, and coordinated task execution; MCP connects an agent to external tools/data sources
C. A2A and MCP are simply two different marketing names describing the exact same underlying protocol specification
D. A2A is only ever usable within a single Azure subscription, while MCP is assumed to work seamlessly across subscriptions

**Answer:** B — The module frames A2A entirely around agent-to-agent discovery (Agent Card), communication, and coordinated task execution among independent/remote agents, explicitly contrasting it with "some MCP scenarios that rely on a single LLM connection" (MCP's typical role is tool/data integration for a single agent). A reverses the definitions; C and D are false.

**Q52.** Which of the following would most likely appear as an AI-103 exam scenario testing this module's content?

A. Configuring Azure Content Understanding to extract layout information from a scanned PDF document uploaded to blob storage first
B. Designing a solution where a "coordinator" agent must discover and invoke two independently hosted specialist agents built by different teams, each exposing its own Agent Card at `/.well-known/agent-card.json`
C. Tuning temperature and top-p sampling parameters for a single chat completion API call made to one deployed model instance
D. Configuring semantic search ranking and scoring profiles within an Azure AI Search index deployment's configuration settings

**Answer:** B — This scenario directly requires knowledge of Agent Cards, the well-known discovery endpoint, and multi-agent orchestration via A2A — the core subject of this module. A, C, and D belong to other AI-103 domains (Content Understanding/information extraction, prompt/parameter tuning, and RAG/search respectively).

## Scenario-based questions

**Q56.** An architecture has a "research coordinator" agent that must (1) discover and delegate subtasks to two independently hosted, third-party specialist agents built by different teams on different LLMs, and (2) give its own specialist agents access to an internal document search index and a code execution sandbox. Which protocol should be used for part 1, which for part 2, and why?
A. Both parts should use MCP exclusively, since MCP is assumed to handle all external connections regardless of whether they're to independent third-party agents or to internal tools and data sources, per this option's flawed premise
B. Part 1: A2A — because it standardizes agent-to-agent discovery (Agent Card), communication, and coordinated task execution across independently hosted agents that may each use a different LLM; Part 2: MCP (or Foundry service-provided tools) — because it connects a single agent to external tools/data sources like a search index or code execution sandbox
C. Both parts should use A2A exclusively, since A2A is assumed to also connect agents directly to tools and data stores, in addition to connecting agents to other independent agents, per this option's flawed premise
D. Part 1: MCP; Part 2: A2A — the exact reverse assignment of option B, incorrectly swapping which protocol handles agent-to-agent discovery versus agent-to-tool and data-source access
**Answer:** B — This module's explicit A2A-vs-MCP distinction: A2A is for agent-to-**agent** interoperability (discovery via Agent Card, communication, coordination, with each agent free to choose its own LLM), while MCP (or Foundry's built-in tools) is for agent-to-**tool/data** integration — exactly the document search and code execution needs in part 2.

**Q57.** A team is deciding whether to implement cross-team agent coordination using this module's A2A protocol or the Microsoft Agent Framework's handoff orchestration pattern (`WorkflowBuilder` with switch-case routing) from the multi-agent orchestration module. The specialist agents are built and hosted independently by separate teams, potentially outside the team's own Microsoft Agent Framework runtime, each needing to advertise its own capabilities for discovery. Which approach fits better, and why?
A. Handoff orchestration — because `WorkflowBuilder` is assumed to be required for any dynamic routing scenario at all, regardless of whether the specialist agents are hosted inside or entirely outside the team's own Microsoft Agent Framework runtime environment
B. A2A — because it's specifically designed for standardized discovery (Agent Card at `/.well-known/agent-card.json`) and communication between independently hosted, potentially cross-vendor/cross-platform agents, whereas Microsoft Agent Framework's handoff orchestration coordinates agents that are defined and run together within the same framework/runtime
C. Neither approach supports agents built by separate teams according to this option's flawed reasoning about cross-team ownership and independent hosting boundaries between organizations
D. A2A and handoff orchestration are assumed to be the exact same underlying coordination mechanism, just given two different marketing names by Microsoft's separate product teams
**Answer:** B — A2A's core purpose is standardized discovery and coordination across independently hosted, potentially cross-vendor agents (each exposing an Agent Card). Handoff orchestration, in contrast, is a Microsoft Agent Framework SDK pattern for dynamically routing between agents that are typically defined together within one orchestration/runtime — a different architectural scope than independently-hosted, separately-discoverable agents.

**Q58.** The technical-writer routing agent example needs a title-generation agent and an outline-generation agent, each hosted as separate A2A servers. For each specialist agent, walk through what must exist before the routing agent can successfully discover and invoke it.
A. Only an `AgentExecutor` class is needed for this scenario; hosting infrastructure, a Server Application, a Request Handler, and a Task Store are all assumed to be optional extras not strictly required
B. Each specialist agent needs: defined Agent Skills and an Agent Card (exposed at `/.well-known/agent-card.json`), an `AgentExecutor` implementing `Execute`/`Cancel`, a Request Handler linking the executor to a Task Store, and a Server Application (e.g., Starlette + Uvicorn) making it network-accessible — only then can the routing agent's client fetch the Agent Card and send requests
C. Only the Agent Card is required for discovery to succeed in this scenario; the executor and Server Application are assumed optional for purely read-only skills with no state
D. A single shared Task Store instance across both independently hosted specialist agents is assumed mandatory for this two-agent architecture to function correctly at all, per this option
**Answer:** B — This synthesizes the full module: Agent Skills/Agent Card (discovery), Agent Executor (business logic bridge via `Execute`/`Cancel`, using `RequestContext`/`EventQueue`), a Request Handler + Task Store (task lifecycle management, required "even for simple agents"), and a Server Application (Starlette/Uvicorn) to expose it over HTTP — all of which the routing agent's client depends on to discover (via the well-known endpoint) and invoke each specialist.

**Q59.** The outline-generation agent in the routing-agent scenario can take a long time to produce a detailed, multi-section outline, and the technical writer wants to see partial progress rather than waiting for the entire result. Additionally, the client needs to be able to check on or cancel the task later. Which A2A request type and executor operation combination addresses this, and how should the client interpret the response?
A. A Non-Streaming request using only the `Execute` operation with no `Cancel` support implemented at all; the client should discard any partial data received and simply wait for one single final message
B. A Streaming request, with the executor supporting both `Execute` (sending incremental results via the event queue) and `Cancel`; the client should expect asynchronous, incremental results and be prepared to handle a task-based response requiring follow-up calls rather than assuming a single direct message
C. A Non-Streaming request is assumed mandatory by this option for any task exceeding 30 minutes of estimated processing time, per an invented rule not actually found anywhere in the module
D. Streaming requests are assumed by this option to never return task objects at all, only ever returning direct messages instead of any task-based response type whatsoever
**Answer:** B — Streaming requests deliver responses incrementally and asynchronously, appropriate for long-running tasks. For cancellation/status tracking support, the executor should implement `Cancel` (unlike a minimal "Hello World" agent, which may skip it) alongside `Execute`. The client must be prepared to handle task-based responses (not just direct messages), potentially making follow-up calls to check status or retrieve final results.
