# Practice questions — Develop an AI agent with Microsoft Agent Framework

## Introduction

**Q1.** According to the module introduction, the Microsoft Agent Framework is described as the next generation of which two prior frameworks/toolkits, built by the same engineering teams?

A. LangChain and Semantic Kernel
B. Semantic Kernel and AutoGen
C. AutoGen and LangGraph
D. Semantic Kernel and Bot Framework

**Answer:** B — The module states the Microsoft Agent Framework is "the next generation of both Semantic Kernel and AutoGen, built by the same teams." LangChain and Bot Framework are not mentioned in this module.

**Q2.** Which capability does the Microsoft Agent Framework add on top of what Semantic Kernel and AutoGen already provided?

A. Vector database indexing
B. Graph-based workflows for explicit multi-agent orchestration
C. Built-in speech-to-text
D. Content moderation filters

**Answer:** B — The introduction states the framework "adds graph-based workflows for explicit multi-agent orchestration" as the new element combining AutoGen's abstractions with Semantic Kernel's enterprise features.

**Q3.** In the module's running example scenario, what task does the AI agent perform?

A. Answers customer support tickets using RAG over a knowledge base
B. Extracts data from submitted expense reports, formats them, and emails them to recipients
C. Generates marketing images from text prompts
D. Translates speech in real time during meetings

**Answer:** B — The introduction and the hands-on exercise both use the expense-report-to-email scenario as the running example.

**Q4.** What two enterprise-grade features does Semantic Kernel contribute to the Microsoft Agent Framework, per the module?

A. Multimodal image generation and video editing
B. Session-based state management and type safety (along with middleware and telemetry)
C. Built-in OCR and layout analysis
D. Content Understanding pipelines

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

## Understand Microsoft Agent Framework AI agents

**Q7.** Which Microsoft Agent Framework building block provides "a single, unified interface to connect with multiple AI providers"?

A. Context providers
B. Model clients
C. Middleware
D. Workflow orchestration

**Answer:** B — Per the architecture table, "Model clients" are defined exactly as "A single, unified interface to connect with multiple AI providers." Context providers instead supply memory; middleware intercepts/logs actions.

**Q8.** Which framework component is described as "plug-and-play memory components that surface relevant information to agents dynamically"?

A. Function tools
B. MCP clients
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

A. It is the only provider that supports streaming responses
B. It supports service-side chat history, so the agent session persists across turns automatically without the application managing conversation state
C. It is the only provider compatible with Python
D. It offers the lowest per-token pricing of all listed providers

**Answer:** B — The module explicitly states this is "a key differentiator" and that "service-side history makes Foundry the recommended provider for production scenarios where maintaining context is critical." Pricing and language support are not discussed in this module.

**Q11.** Which of the following providers in the matrix does NOT support service-side chat history?

A. OpenAI Responses
B. Foundry Agent Service
C. Anthropic Claude
D. Azure OpenAI Responses

**Answer:** C — Anthropic Claude is listed as "No" for service chat history, along with Azure OpenAI Chat Completion, OpenAI Chat Completion, Amazon Bedrock, GitHub Copilot, and Ollama. The other three options are all listed "Yes."

**Q12.** Out of the box, which of the following is NOT listed as a capability every Microsoft Agent Framework agent supports regardless of provider?

A. Function calling
B. Structured outputs
C. Automatic fine-tuning of the underlying model
D. Streaming responses

**Answer:** C — The listed default capabilities are function calling, multi-turn conversations, structured outputs, streaming responses, and service-provided tools (where supported). Automatic model fine-tuning is not mentioned anywhere in the module.

**Q13.** What benefit does the framework's unified provider interface give developers when model requirements change?

A. Automatic model retraining on proprietary data
B. The ability to switch the underlying inference service without rewriting agent logic — only client configuration changes
C. Free migration credits from Microsoft
D. Guaranteed identical latency across all providers

**Answer:** B — The module states: "you can switch the underlying inference service without rewriting your agent logic—only the client configuration changes."

## Create an Azure AI agent with Microsoft Agent Framework

**Q14.** Which two pieces of information are needed to connect to a Foundry project before writing agent code?

A. Subscription ID and resource group name
B. Project endpoint and model deployment name
C. Tenant ID and client secret
D. API key and endpoint region

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
C. The JSON schema for the agent's tool outputs
D. The billing configuration for the agent's deployment

**Answer:** B — Unit 3 defines "Instructions—the system prompt that defines the agent's role, goals, and constraints" as one of the two inputs (with optional Tools) when creating the agent.

**Q17.** What SDK class is used as the Foundry chat client that bridges the application and the Foundry Agent Service (per the knowledge check)?

A. `AgentThread`
B. `ChatAgent`
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
C. Batch mode
D. Polling mode

**Answer:** B — "Streaming is better suited for user-facing interfaces where showing output progressively improves the experience," per Unit 3. Non-streaming waits for a complete response object before returning.

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
D. Web Search

**Answer:** C — This is the table's exact description of the Azure AI Search tool. Foundry Toolboxes are described instead as "Named, versioned bundles of hosted tool configurations."

**Q25.** Per the module's note, which of these service-provided tools are explicitly flagged as being in preview/experimental status with limited support across non-Foundry providers?

A. Code Interpreter, Web Search
B. Azure AI Search, Bing Grounding, SharePoint
C. Hosted MCP Tools, Foundry Toolboxes
D. File Search, Code Interpreter

**Answer:** B — The exact note reads: "Some tools—including Azure AI Search, Bing Grounding, SharePoint, and others—are in preview or experimental. They're available for Foundry agents but may have limited support across other providers."

**Q26.** What two approaches does the Agent Framework support for describing custom function tools to the model?

A. XML schema files and OpenAPI specs
B. Type annotations with `Annotated` descriptions, and the `@tool` decorator
C. YAML manifest files and JSON Schema drafts
D. Docstrings only, with no other option

**Answer:** B — The module states the two approaches are "Type annotations with descriptions—use Python's `Annotated` type" and "The `@tool` decorator—explicitly specify the tool's name and description as decorator arguments."

**Q27.** When using the `@tool` decorator approach and precise control over input structure is required, what can be supplied to define an explicit schema?

A. A Pydantic model
B. An XML Schema Definition (XSD)
C. A GraphQL schema
D. A .proto file

**Answer:** A — The module states: "You can also provide an explicit schema using a Pydantic model if you need precise control over the input structure."

**Q28.** How does the model choose which of several registered tools to invoke when multiple tools are passed to an agent?

A. The developer must write explicit routing/if-else logic to select the tool
B. The model automatically selects the most appropriate tool based on conversation context and the tool descriptions provided
C. Tools are invoked strictly in the order they were registered
D. Only one tool may be registered per agent; multiple tools are not supported

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
C. Registering the inner agent as an MCP server
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
D. Export the agent definition to GitHub

**Answer:** B — The tip at the end of the exercise unit explicitly says to "delete the Azure resources that you created during the exercise" once finished, a standard cost-hygiene practice.

**Q34.** [general Azure knowledge] What is required before a learner can complete this exercise?

A. A Microsoft Azure subscription
B. An on-premises Semantic Kernel installation
C. A GitHub Copilot Enterprise license
D. A pre-existing Bing Search resource

**Answer:** A — The exercise unit states: "To complete this exercise, you will need a Microsoft Azure subscription."

## Knowledge check

**Q35.** Per the module's knowledge check, what are the key steps to create a Microsoft Foundry Agent using the Microsoft Agent Framework?

A. Deploy a custom AI model, then create an agent definition directly in the Azure portal
B. Initialize the agent by defining a model in the `AgentThread` constructor
C. Create an `AzureAIAgentClient`, define a `ChatAgent` with instructions and tools, and create an `AgentThread` for conversations
D. Register the agent as an MCP server before assigning it any tools

**Answer:** C — This is the correct sequence confirmed by the knowledge check and consistent with the 5-step flow in the "Create an Azure AI agent" unit (project setup, authentication, chat client, agent creation, session/thread for conversation).

**Q36.** Per the knowledge check, how do you add custom functionality to a Microsoft Foundry Agent?

A. Configure custom functions in the Azure portal and link them via connection strings
B. Create Python functions with proper type annotations and descriptions, then pass them to the `ChatAgent`'s tools parameter
C. Modify the underlying AI model's architecture directly
D. Submit a support ticket to Microsoft to enable custom functions

**Answer:** B — The knowledge check confirms this is the correct approach, matching the custom function tool registration process described in the "Add tools" unit.

## Summary

**Q37.** According to the module summary, what is the overall value of using the Microsoft Agent Framework?

A. It replaces the need for any Azure subscription
B. It enables developers to create dynamic, adaptable AI solutions that enhance user interactions and automate complex tasks
C. It eliminates the need to define agent instructions
D. It is exclusively for computer vision workloads

**Answer:** B — The summary states: "you can use the Microsoft Agent Framework to create dynamic, adaptable AI solutions that enhance user interactions and automate complex tasks."

**Q38.** Which two categories of knowledge does the module summary say were covered?

A. Computer vision pipelines and speech translation
B. The components/core concepts of the Microsoft Agent Framework, and how to create custom tools to extend agent capabilities
C. Content Understanding analyzers and OCR extraction
D. Responsible AI evaluators and safety filters

**Answer:** B — The summary states: "You learned about the components and core concepts of the Microsoft Agent Framework. You also learned how to create custom tools to extend your agent's capabilities." The other options are not covered by this module.

**Q39.** Which SDK/framework name should NOT be used interchangeably with "Microsoft Agent Framework" on the exam, despite the module's shared lineage explanation?

A. Foundry Agent Service — the managed service Microsoft Agent Framework connects to, not the SDK itself
B. Azure Functions
C. Azure Logic Apps
D. Azure Data Factory

**Answer:** A — Per this module, Microsoft Agent Framework is the open SDK (successor to Semantic Kernel/AutoGen) used to build agents; Foundry Agent Service is the separate managed backend/provider it connects to for features like service-side chat history. Confusing "the SDK you code against" with "the managed service it talks to" is a common exam distractor; Azure Functions, Logic Apps, and Data Factory are unrelated services not discussed in this module.
