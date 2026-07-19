# Practice questions — Develop an AI agent with Microsoft Agent Framework

## Introduction

**Q1.** According to the module introduction, the Microsoft Agent Framework is described as the next generation of which two prior frameworks/toolkits, built by the same engineering teams?

A. LangChain and Semantic Kernel
B. Semantic Kernel and AutoGen
C. AutoGen and LangGraph
D. Semantic Kernel and Bot Framework

**Answer:** B — The module states the Microsoft Agent Framework is "the next generation of both Semantic Kernel and AutoGen, built by the same teams." LangChain and Bot Framework are not mentioned in this module.

**Q2.** Which capability does the Microsoft Agent Framework add on top of what Semantic Kernel and AutoGen already provided?

A. Vector database indexing for long-term semantic memory storage
B. Graph-based workflows for explicit multi-agent orchestration
C. Built-in speech-to-text transcription for voice-driven agent inputs
D. Content moderation filters applied automatically to every model response

**Answer:** B — The introduction states the framework "adds graph-based workflows for explicit multi-agent orchestration" as the new element combining AutoGen's abstractions with Semantic Kernel's enterprise features.

**Q3.** In the module's running example scenario, what task does the AI agent perform?

A. Answers customer support tickets using RAG over a knowledge base
B. Extracts data from submitted expense reports, formats them, and emails them to recipients
C. Generates marketing images from text prompts using a diffusion model
D. Translates speech in real time during meetings using a speech SDK

**Answer:** B — The introduction and the hands-on exercise both use the expense-report-to-email scenario as the running example.

**Q4.** What two enterprise-grade features does Semantic Kernel contribute to the Microsoft Agent Framework, per the module?

A. Multimodal image generation and video editing pipelines for content creation
B. Session-based state management and type safety (along with middleware and telemetry)
C. Built-in OCR and layout analysis for scanned document processing
D. Content Understanding pipelines for extracting structured fields

**Answer:** B — The module states Semantic Kernel contributes "enterprise features—session-based state management, type safety, middleware, and telemetry" to the combined framework.

**Q5.** [general Azure knowledge] Which prerequisite knowledge does the module recommend before starting, beyond familiarity with the Azure portal?

A. Deep Kubernetes administration experience
B. An understanding of generative AI concepts
C. Certification in Azure networking
D. Prior experience with .NET MAUI

**Answer:** B — The module lists "familiarity with Azure and the Azure portal" and "an understanding of generative AI" as prerequisites, pointing to the "Fundamentals of Generative AI" module.

**Q6.** Every agent created with the Microsoft Agent Framework derives from which common construct, ensuring a consistent interface across providers?

A. A unified `Agent` base class
B. A shared `Plugin` interface
C. A `KernelFunction` wrapper
D. An `AgentThread` subclass

**Answer:** A — The introduction/Unit 2 states "Every agent is derived from a unified `Agent` base class, giving you a consistent interface regardless of which underlying model provider you use."

**Q40.** How many units does this module contain, and at what level is it classified?
A. 7 units, Intermediate level
B. 11 units, Beginner level
C. 5 units, Advanced level
D. 9 units, Intermediate level
**Answer:** A — The module metadata states Intermediate level across 7 units, for roles AI Engineer, Developer, Solution Architect, and Student.

## Understand Microsoft Agent Framework AI agents

**Q7.** Which Microsoft Agent Framework building block provides "a single, unified interface to connect with multiple AI providers"?

A. Context providers
B. Model clients
C. Middleware
D. Workflow orchestration

**Answer:** B — Per the architecture table, "Model clients" are defined exactly as "A single, unified interface to connect with multiple AI providers." Context providers instead supply memory; middleware intercepts/logs actions.

**Q8.** Which framework component is described as "plug-and-play memory components that surface relevant information to agents dynamically"?

A. Function tools
B. MCP clients themselves
C. Context providers
D. Agent session

**Answer:** C — This is the exact description of "Context providers" in the architecture table. "Agent session" instead handles native state management for persistent conversation context.

**Q9. (Choose two)** According to the provider matrix in this module, which of the following providers DO support service-side chat history?

A. Foundry Agent Service
B. Azure OpenAI Chat Completion
C. Azure OpenAI Responses
D. Amazon Bedrock

**Answer:** A, C — The provider matrix lists "Yes" for service chat history only for Foundry Agent Service, Azure OpenAI Responses, and OpenAI Responses. Azure OpenAI Chat Completion and Amazon Bedrock are both listed as "No."

**Q10.** Why does the module recommend Foundry Agent Service as the primary provider for production scenarios?

A. It is the only provider among those listed that supports streaming responses back to the client application
B. It supports service-side chat history, so the agent session persists across turns automatically without the application managing conversation state
C. It is the only provider that is fully compatible with the Python SDK specifically, per the provider matrix
D. It offers the lowest per-token pricing of all the providers listed in the module's comparison matrix table

**Answer:** B — The module explicitly states this is "a key differentiator" and that "service-side history makes Foundry the recommended provider for production scenarios where maintaining context is critical." Pricing and language support are not discussed in this module.

**Q11.** Which of the following providers in the matrix does NOT support service-side chat history?

A. OpenAI Responses
B. Foundry Agent Service
C. Anthropic Claude
D. Azure OpenAI Responses

**Answer:** C — Anthropic Claude is listed as "No" for service chat history, along with Azure OpenAI Chat Completion, OpenAI Chat Completion, Amazon Bedrock, GitHub Copilot, and Ollama. The other three options are all listed "Yes."

**Q12.** Out of the box, which of the following is NOT listed as a capability every Microsoft Agent Framework agent supports regardless of provider?

A. Function calling across registered tools
B. Structured outputs matching a schema
C. Automatic fine-tuning of the underlying model
D. Streaming responses to the client

**Answer:** C — The listed default capabilities are function calling, multi-turn conversations, structured outputs, streaming responses, and service-provided tools (where supported). Automatic model fine-tuning is not mentioned anywhere in the module.

**Q13.** What benefit does the framework's unified provider interface give developers when model requirements change?

A. Automatic model retraining on the organization's own proprietary data whenever requirements change
B. The ability to switch the underlying inference service without rewriting agent logic — only client configuration changes
C. Free migration credits from Microsoft toward adopting the new provider's inference service
D. Guaranteed identical latency across all providers regardless of region or underlying model choice

**Answer:** B — The module states: "you can switch the underlying inference service without rewriting your agent logic—only the client configuration changes."

**Q41.** Which Microsoft Agent Framework building block is described as "Hooks to intercept, log, or modify agent actions before and after execution"?
A. Middleware
B. Context providers
C. MCP clients
D. Agent session
**Answer:** A — This is the architecture table's exact description of Middleware. Context providers instead supply dynamic memory; MCP clients provide runtime tool discovery via the Model Context Protocol.

**Q42.** Which building block provides "built-in support for the Model Context Protocol, enabling dynamic tool discovery at runtime"?
A. Function tools
B. MCP clients
C. Model clients
D. Workflow orchestration
**Answer:** B — This is the exact description of "MCP clients" in the architecture table. "Model clients" is a different building block providing a unified interface across AI providers, not MCP tool discovery.

**Q43.** Which building block is described as providing "graph-based workflows for managing sequential, concurrent, group chat, and agent handoff patterns"?
A. Agent session tracking
B. Function tools registry
C. Workflow orchestration
D. Middleware interception hooks
**Answer:** C — "Workflow orchestration" is the architecture table entry covering graph-based workflows for sequential, concurrent, group chat, and handoff multi-agent patterns — the foundation extended further in the multi-agent orchestration module.

## Create an Azure AI agent with Microsoft Agent Framework

**Q14.** Which two pieces of information are needed to connect to a Foundry project before writing agent code?

A. Subscription ID and resource group name
B. Project endpoint and model deployment name
C. Tenant ID and client secret pair
D. API key and endpoint region value

**Answer:** B — Unit 3 states you connect using "Project endpoint—the URL of your Foundry project" and "Model deployment name—the name of the model deployment you want to use for your agent."

**Q15.** Which credential mechanism does the Agent Framework use to authenticate to a Foundry project without hardcoding connection strings or API keys?

A. `ManagedIdentityCredential` only
B. `DefaultAzureCredential`
C. `InteractiveBrowserCredential`
D. A stored client secret in environment variables

**Answer:** B — The module states "`DefaultAzureCredential` resolves the right credential automatically based on your environment—Azure CLI during development, managed identity in production." No connection strings or API keys need to be hardcoded.

**Q16.** In the agent creation step, what do the "Instructions" provided to the agent represent?

A. The list of Azure resources the agent is permitted to access
B. The system prompt that defines the agent's role, goals, and constraints
C. The JSON schema describing the shape of the agent's tool call outputs specifically
D. The billing configuration for the agent's deployment

**Answer:** B — Unit 3 defines "Instructions—the system prompt that defines the agent's role, goals, and constraints" as one of the two inputs (with optional Tools) when creating the agent.

**Q17.** What SDK class is used as the Foundry chat client that bridges the application and the Foundry Agent Service (per the knowledge check)?

A. `AgentThread` class instance
B. `ChatAgent` class instance
C. `AzureAIAgentClient`
D. `KernelFunction`

**Answer:** C — The knowledge check confirms the correct sequence: "Create an `AzureAIAgentClient`, define a `ChatAgent` with instructions and tools, and create an `AgentThread` for conversations." `AzureAIAgentClient` is the chat client; `ChatAgent` is the agent itself; `AgentThread` manages conversation state.

**Q18.** Which component manages conversation state and stores messages across turns, per the knowledge check?

A. `ChatAgent`
B. `AzureAIAgentClient`
C. `AgentThread`
D. `Model client`

**Answer:** C — The knowledge check explicitly confirms `AgentThread` is the component that "manages conversation state and stores messages," matching the "session" concept described in Unit 3.

**Q19. (Choose two)** For which providers does the Microsoft Agent Framework maintain conversation state locally, in memory, within the session object, rather than server-side?

A. Foundry Agent Service
B. Azure OpenAI Chat Completion
C. Anthropic Claude
D. OpenAI Responses

**Answer:** B, C — Providers without service-side history support (per the provider matrix: Azure OpenAI Chat Completion and Anthropic Claude both listed "No") use local, in-memory history instead. Foundry Agent Service and OpenAI Responses both support service-side history ("Yes").

**Q20.** What is a limitation of "local history" as described in the module?

A. It cannot be used with custom function tools
B. It does not persist across process restarts
C. It requires a separate Cosmos DB account
D. It is only available in the .NET SDK

**Answer:** B — The module states local history "is suitable for short-lived or stateless applications, but it doesn't persist across process restarts," unlike Foundry's persistent, service-side history.

**Q21.** In both streaming and non-streaming response modes, which property on the response object aggregates all text content from the agent's output?

A. `.content`
B. `.text`
C. `.output_text`
D. `.message`

**Answer:** B — The module states: "the response exposes a `text` property that aggregates all text content from the agent's output, making it straightforward to extract the final answer regardless of which mode you use."

**Q22.** Which response mode is described as better suited for user-facing interfaces where showing output progressively improves the experience?

A. Non-streaming (synchronous)
B. Streaming (asynchronous)
C. Batch mode processing
D. Polling mode requests

**Answer:** B — "Streaming is better suited for user-facing interfaces where showing output progressively improves the experience," per Unit 3. Non-streaming waits for a complete response object before returning.

**Q44.** How many exchanges (user message + response) does a single call to the agent's run method handle, and what mechanism is needed to remember prior turns across multiple calls?
A. A single call handles one full multi-turn conversation automatically; no additional mechanism is needed
B. A single call handles exactly one exchange (one message, one response); a session (`AgentThread`) is needed to remember prior turns
C. A single call handles unlimited exchanges automatically, as long as streaming mode is enabled on the client
D. Multi-turn memory is handled entirely by the `@tool` decorator's `approval_mode` parameter internally
**Answer:** B — The module states: "A single call to the agent's run method handles one exchange—one user message, one response. For a real conversation, the agent needs to remember what happened in prior turns. That's where a session comes in," referring to `AgentThread`.

**Q45.** How does the module describe the non-streaming (synchronous) response mode, in contrast to streaming?
A. It returns partial updates as the model generates them, iterated over asynchronously as each chunk arrives
B. The run method waits for the agent to finish and returns a complete response object — the simplest pattern, good when incremental display isn't needed
C. It is only available for providers without service-side chat history support enabled on their account settings
D. It requires the `@tool` decorator to be explicitly applied to every registered function beforehand always
**Answer:** B — Non-streaming is described as the simplest pattern: the run method waits for the agent to finish processing and returns a complete response object, suited to cases where incremental/progressive display isn't required — unlike streaming, which returns a response stream of partial updates.

## Add tools to Azure AI agent

**Q23. (Choose two)** Which of the following are listed as service-provided (hosted) tools available through the Foundry provider?

A. Code Interpreter
B. `@tool` decorator
C. File Search
D. `Annotated` type hints

**Answer:** A, C — Code Interpreter and File Search are both service-provided tools in the table (along with Web Search, Hosted MCP Tools, Azure AI Search, and Foundry Toolboxes). The `@tool` decorator and `Annotated` type hints are mechanisms for defining custom function tools, not service-provided tools.

**Q24.** Which service-provided tool "Queries an Azure AI Search index through a Foundry connection"?

A. Foundry Toolboxes
B. Hosted MCP Tools
C. Azure AI Search
D. Web Search results

**Answer:** C — This is the table's exact description of the Azure AI Search tool. Foundry Toolboxes are described instead as "Named, versioned bundles of hosted tool configurations."

**Q25.** Per the module's note, which of these service-provided tools are explicitly flagged as being in preview/experimental status with limited support across non-Foundry providers?

A. Code Interpreter, Web Search preview
B. Azure AI Search, Bing Grounding, SharePoint
C. Hosted MCP Tools, Foundry Toolboxes
D. File Search, Code Interpreter preview

**Answer:** B — The exact note reads: "Some tools—including Azure AI Search, Bing Grounding, SharePoint, and others—are in preview or experimental. They're available for Foundry agents but may have limited support across other providers."

**Q26.** What two approaches does the Agent Framework support for describing custom function tools to the model?

A. XML schema files and OpenAPI spec definitions uploaded separately to the project
B. Type annotations with `Annotated` descriptions, and the `@tool` decorator
C. YAML manifest files and JSON Schema draft documents authored outside the codebase
D. Docstrings only, with absolutely no other supported option

**Answer:** B — The module states the two approaches are "Type annotations with descriptions—use Python's `Annotated` type" and "The `@tool` decorator—explicitly specify the tool's name and description as decorator arguments."

**Q27.** When using the `@tool` decorator approach and precise control over input structure is required, what can be supplied to define an explicit schema?

A. A Pydantic model
B. An XML Schema Definition (XSD)
C. A GraphQL schema
D. A .proto file

**Answer:** A — The module states: "You can also provide an explicit schema using a Pydantic model if you need precise control over the input structure."

**Q28.** How does the model choose which of several registered tools to invoke when multiple tools are passed to an agent?

A. The developer must write explicit routing/if-else logic to select the correct tool manually
B. The model automatically selects the most appropriate tool based on conversation context and the tool descriptions provided
C. Tools are invoked strictly in the exact order in which they were registered with the agent object
D. Only one tool may be registered per agent; multiple simultaneous tools are not supported

**Answer:** B — The module states: "the model automatically selects the most appropriate tool for each part of the conversation. You don't need to write any routing logic—the framework handles tool orchestration."

**Q29.** Which parameter, configured on the `@tool` decorator, enables the tool approval pattern requiring human review before a tool executes?

A. `require_confirmation`
B. `human_in_loop`
C. `approval_mode`
D. `pending_review`

**Answer:** C — The module states: "Approval behavior can be configured per tool using the `approval_mode` parameter on the `@tool` decorator."

**Q30.** What pattern allows a specialized "inner" agent to be delegated tasks by a coordinating "outer" agent in the Microsoft Agent Framework?

A. Converting the inner agent into a function tool and passing it to the outer agent
B. Merging both agents' instructions into a single `ChatAgent`
C. Registering the inner agent as an MCP server on the network
D. Using two separate `AzureAIAgentClient` instances that automatically synchronize

**Answer:** A — The module states: "You convert an inner agent into a function tool and pass it to an outer agent, which can then delegate specific tasks to it," noting this pattern is explored further in a separate multi-agent module.

**Q31. (Choose three)** Which of the following are listed among the module's "best practices for custom tools"?

A. Write clear descriptions
B. Keep tools focused on a single responsibility
C. Return meaningful, structured data
D. Maximize the number of parameters per tool for flexibility

**Answer:** A, B, C — The module lists "Write clear descriptions," "Keep tools focused," and "Return meaningful data" among its five best practices (along with annotating every parameter and handling errors gracefully). Maximizing parameters per tool is the opposite of the guidance given, which favors focused, single-purpose tools.

## Exercise - Develop an Azure AI agent with the Microsoft Agent Framework SDK

**Q32.** What does the hands-on exercise in this module ask learners to build?

A. A multi-agent customer support chatbot
B. An AI agent that creates an expense claim email
C. A RAG pipeline over PDF documents
D. A speech-to-text transcription agent

**Answer:** B — The exercise unit states: "you use the Microsoft Agent Framework SDK to create an AI agent that creates an expense claim email," consistent with the scenario introduced earlier in the module.

**Q33.** What is recommended after completing the exercise, once you're done exploring Azure AI Agents?

A. Leave the resources running for future reference
B. Delete the Azure resources created during the exercise
C. Downgrade the Foundry project to a free tier
D. Export the agent definition to GitHub for archiving

**Answer:** B — The tip at the end of the exercise unit explicitly says to "delete the Azure resources that you created during the exercise" once finished, a standard cost-hygiene practice.

**Q34.** [general Azure knowledge] What is required before a learner can complete this exercise?

A. A Microsoft Azure subscription
B. An on-premises Semantic Kernel installation
C. A GitHub Copilot Enterprise license
D. A pre-existing Bing Search resource

**Answer:** A — The exercise unit states: "To complete this exercise, you will need a Microsoft Azure subscription."

## Knowledge check

**Q35.** Per the module's knowledge check, what are the key steps to create a Microsoft Foundry Agent using the Microsoft Agent Framework?

A. Deploy a custom AI model, then create an agent definition directly in the Azure portal manually
B. Initialize the agent by defining a model directly inside the `AgentThread` constructor call itself
C. Create an `AzureAIAgentClient`, define a `ChatAgent` with instructions and tools, and create an `AgentThread` for conversations
D. Register the agent as an MCP server before assigning it any tools whatsoever in the configuration

**Answer:** C — This is the correct sequence confirmed by the knowledge check and consistent with the 5-step flow in the "Create an Azure AI agent" unit (project setup, authentication, chat client, agent creation, session/thread for conversation).

**Q36.** Per the knowledge check, how do you add custom functionality to a Microsoft Foundry Agent?

A. Configure custom functions in the Azure portal and link them via connection strings manually
B. Create Python functions with proper type annotations and descriptions, then pass them to the `ChatAgent`'s tools parameter
C. Modify the underlying AI model's architecture directly in order to add new functionality
D. Submit a support ticket to Microsoft to have custom functions enabled for the project manually

**Answer:** B — The knowledge check confirms this is the correct approach, matching the custom function tool registration process described in the "Add tools" unit.

## Summary

**Q37.** According to the module summary, what is the overall value of using the Microsoft Agent Framework?

A. It replaces the need for any Azure subscription or resource provisioning entirely for the developer
B. It enables developers to create dynamic, adaptable AI solutions that enhance user interactions and automate complex tasks
C. It eliminates the need to define agent instructions or any system prompt at all for the agent
D. It is exclusively designed for computer vision workloads and image generation pipelines only

**Answer:** B — The summary states: "you can use the Microsoft Agent Framework to create dynamic, adaptable AI solutions that enhance user interactions and automate complex tasks."

**Q38.** Which two categories of knowledge does the module summary say were covered?

A. Computer vision pipelines and real-time speech translation techniques covered in earlier modules
B. The components/core concepts of the Microsoft Agent Framework, and how to create custom tools to extend agent capabilities
C. Content Understanding analyzers and OCR-based extraction pipelines covered in a different module
D. Responsible AI evaluators and content safety filter configuration covered in a different module

**Answer:** B — The summary states: "You learned about the components and core concepts of the Microsoft Agent Framework. You also learned how to create custom tools to extend your agent's capabilities." The other options are not covered by this module.

**Q39.** Which SDK/framework name should NOT be used interchangeably with "Microsoft Agent Framework" on the exam, despite the module's shared lineage explanation?

A. Foundry Agent Service — the managed service Microsoft Agent Framework connects to, not the SDK itself
B. Azure Functions serverless compute platform used for event-driven code execution
C. Azure Logic Apps workflow automation platform used for low-code connector wiring
D. Azure Data Factory data integration pipeline service used for ETL workloads

**Answer:** A — Per this module, Microsoft Agent Framework is the open SDK (successor to Semantic Kernel/AutoGen) used to build agents; Foundry Agent Service is the separate managed backend/provider it connects to for features like service-side chat history. Confusing "the SDK you code against" with "the managed service it talks to" is a common exam distractor; Azure Functions, Logic Apps, and Data Factory are unrelated services not discussed in this module.

## Scenario-based questions

**Q46.** A team is deciding between Foundry Agent Service and Anthropic Claude as the model provider for a production agent that must reliably resume long-running, multi-day conversations even if the application restarts or scales across multiple instances. Using the provider matrix and the module's discussion of local vs. persistent history, which provider should they choose and why?
A. Anthropic Claude, because all providers are assumed to handle history identically once wrapped in an `AgentThread` session object, regardless of what the provider matrix actually states
B. Foundry Agent Service, because it supports service-side chat history — conversation state persists server-side and survives application restarts/scaling, unlike Anthropic Claude, which the matrix marks "No" for service chat history and would fall back to in-memory local history that doesn't survive restarts
C. Anthropic Claude, because it is assumed to be the only provider supporting streaming responses anywhere in the entire provider comparison matrix, per this option
D. Neither — persistent multi-day conversations are assumed not to be supported by the Microsoft Agent Framework at all, per this option's reasoning
**Answer:** B — The provider matrix marks Foundry Agent Service "Yes" and Anthropic Claude "No" for service chat history. Per the module, providers without service-side history support fall back to local, in-memory history within the session object, which does not persist across process restarts — making Foundry the correct choice for the stated durability requirement.

**Q47.** A developer registers a `send_refund` custom function tool that processes financial refunds, and a `lookup_order_status` read-only tool, both passed to the same `ChatAgent`. Management requires that refunds always get a human review before executing, but order lookups should run immediately without friction. How should this be configured, combining the module's tool-approval and multi-tool-orchestration guidance?
A. Set `approval_mode` on the `@tool` decorator for `send_refund` only; leave `lookup_order_status` without approval — the model will automatically route each request to the correct tool based on conversation context, and the agent will pause for confirmation only before calling `send_refund`
B. Set `approval_mode` on both tools together, since approval is assumed to be a global, agent-level setting rather than a configurable per-tool option
C. Write manual if/else routing logic directly in the application code itself to decide which tool needs approval before calling it each time
D. Combine both functions into a single tool so that one shared `approval_mode` setting covers both actions at once, per this option's suggested approach
**Answer:** A — `approval_mode` is configured per tool via the `@tool` decorator, not globally, so it can be applied only to `send_refund`. The model automatically selects the appropriate tool per conversation turn based on context and descriptions (no manual routing needed) — meaning `lookup_order_status` calls proceed without pausing, while `send_refund` calls trigger the approval pause. Combining both into one tool would violate the "keep tools focused" best practice.

**Q48.** An architecture calls for a coordinating "triage" agent that routes requests to either a "billing specialist" agent or a "technical specialist" agent depending on the user's issue, with each specialist agent having its own distinct instructions and tools. How does the module say this composition should be built using the Microsoft Agent Framework, and what future module extends this pattern?
A. Merge all three agents' instructions into one giant `ChatAgent` with a very long combined system prompt covering every specialty area at once
B. Convert each specialist agent into a function tool and pass them to the coordinating (outer) agent, which delegates specific tasks to them — the module notes this "agent as a tool" pattern is explored further in a separate multi-agent orchestration module
C. Register each specialist agent as a separate MCP server and have the triage agent discover them dynamically at runtime — assumed to be the only supported composition method
D. This scenario isn't supported at all without first purchasing and separately configuring Foundry Toolboxes for each individual specialist agent
**Answer:** B — The module explicitly describes the "using an agent as a tool" pattern: converting an inner (specialist) agent into a function tool passed to an outer (coordinating) agent, which delegates tasks to it — and notes this composition pattern is explored in more depth in a separate multi-agent module (covered later in this learning path).

**Q49.** Walking through the full 5-step configuration flow from this module: a developer wants to stand up a Foundry-backed agent in a way that works identically when run locally (via `az login`) and when deployed to an Azure-hosted production environment with a managed identity, with zero code changes to the authentication logic. Which class enables this, and where does it fit in the 5-step sequence (project setup → authentication → chat client init → agent creation → session/thread)?
A. `AgentThread`, assumed to be used in step 1 of the flow to resolve credentials automatically before any authentication step ever occurs
B. `DefaultAzureCredential`, used in step 2 ("Configure authentication") — it resolves the right credential automatically based on environment (Azure CLI locally, managed identity in production), avoiding hardcoded connection strings or API keys
C. `ChatAgent`, assumed to be used in step 4 of the flow to authenticate the developer before the instructions are even configured
D. `AzureAIAgentClient`, assumed to be used in step 5 of the flow solely to establish the conversation session object afterward
**Answer:** B — `DefaultAzureCredential` is the authentication mechanism (step 2 of the 5-step flow) that automatically resolves the correct credential per environment — Azure CLI credential during local development, managed identity in Azure-hosted production — with no hardcoded secrets, exactly matching the described requirement.

**Q50.** A developer wants an agent that can execute Python calculations, search through uploaded PDFs, and query a live Azure AI Search index — all without the developer hosting any of that logic themselves — but is warned that one of these three service-provided tools may have preview-status limitations outside the Foundry provider. Which tool is that, and which two are not flagged that way?
A. Code Interpreter is assumed to be the preview-flagged tool in this scenario; File Search and Azure AI Search are assumed fully stable
B. Azure AI Search is explicitly flagged as preview/experimental with limited support across non-Foundry providers; Code Interpreter and File Search are not called out with that caveat
C. File Search is assumed to be preview-flagged in this scenario; Code Interpreter and Azure AI Search are assumed stable across providers
D. All three tools are assumed equally stable across every provider with no preview caveats mentioned at all
**Answer:** B — The module's note explicitly lists "Azure AI Search, Bing Grounding, SharePoint, and others" as being in preview or experimental status, available for Foundry agents but with potentially limited support across other providers — Code Interpreter and File Search are not called out with this caveat in the module.
