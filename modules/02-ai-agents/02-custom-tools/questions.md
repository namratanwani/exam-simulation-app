# Practice questions — Integrate custom tools into your agent

## Introduction

**Q1.** According to the module introduction, what capability does Microsoft Foundry Agent Service provide "out of the box" (built-in), separate from custom tools?
A. Built-in tools for gathering knowledge and generating code
B. Built-in tools for training new foundation models from scratch
C. Built-in tools for provisioning virtual networks
D. Built-in tools for compiling C++ agent binaries
**Answer:** A — The module states the "AI Agent Service provides built-in tools for gathering knowledge and generating code." B, C, and D are not agent tool capabilities described anywhere in the module.

**Q2.** Per the module's definition, a custom tool is based on which of the following?
A. Only Microsoft-certified partner connectors
B. Your own code or a third-party service/API
C. A retrained copy of the base LLM
D. A Logic Apps template marketplace listing only
**Answer:** B — The introduction defines a custom tool as being "based on your own code or a third-party service or API." Option D describes only one of several tool options (Logic Apps), not the general definition.

**Q3.** In the retail industry scenario used to motivate the module, what problem does the custom FAQ agent solve?
A. It replaces the CRM system entirely
B. It frees the support team from repetitive inquiries by handling common questions and looking up customer orders
C. It trains new support staff using synthetic data
D. It automatically negotiates refunds with third-party vendors without any tool integration
**Answer:** B — The scenario describes a company "struggling with managing customer inquiries efficiently" and building "a custom FAQ agent" with "a set of custom tools to look up customer orders" to free up the support team.

**Q4.** Which statement best reflects why an agent might need a custom tool rather than relying solely on the base model?
A. The AI model would struggle to complete specific tasks or actions on its own
B. Custom tools are required for the model to generate any text output
C. Custom tools reduce the token context window automatically
D. Custom tools are mandatory for all Foundry Agent Service deployments
**Answer:** A — The module explains custom tools exist because "sometimes your agent needs to be able to complete specific tasks or actions that an AI model would struggle to handle on its own."

**Q5.** True or false framed as MCQ: Building an agent with Microsoft Foundry Agent Service, per the introduction, requires extensive AI or machine learning expertise.
A. True — deep ML expertise is required
B. False — it offers a seamless way to build an agent without needing extensive AI or ML expertise
C. True, but only for custom tools specifically
D. False, but only when using Azure Functions
**Answer:** B — The module explicitly states Foundry Agent Service "offers a seamless way to build an agent without needing extensive AI or machine learning expertise."

**Q6.** [general Azure knowledge] Which Azure service is referenced as the platform underpinning the agent-building capability discussed throughout this module?
A. Microsoft Foundry Agent Service
B. Azure Machine Learning Designer
C. Azure Bot Framework Composer
D. Azure Cognitive Search
**Answer:** A — Microsoft Foundry Agent Service (formerly Azure AI Agent Service) is the named platform throughout the module; the other services are related but distinct Azure offerings not discussed in this module.

## Why use custom tools

**Q1.** Which THREE benefits does the module explicitly attribute to custom tools? (Choose three.)
A. Enhanced productivity
B. Improved accuracy
C. Tailored solutions
D. Reduced model token costs by 50%
E. Guaranteed zero hallucinations
**Answer:** A, B, C — The module lists exactly these three: "Enhanced productivity," "Improved accuracy," and "Tailored solutions." D and E are not claims made in the module.

**Q2.** In the ski-resort weather scenario, what is the correct sequence of events?
A. The tool calls the agent, then the agent asks the user a clarifying question
B. The user asks about weather; the agent determines it has a tool that can call a meteorological API and invokes it; the tool returns the report and the agent informs the user
C. The agent generates the weather answer directly from training data without any tool
D. The user directly calls the external meteorological API and the agent summarizes the raw JSON
**Answer:** B — This is the exact three-step flow described: the user asks, the agent decides to call the tool, and the tool result is relayed back to the user.

**Q3.** A manufacturing company wants its agent to check stock levels, predict restocking needs from historical data, and place supplier orders automatically. Which scenario from the module does this match?
A. Customer support automation
B. Inventory management
C. IT Helpdesk support
D. E-learning and training
**Answer:** B — This is the "Inventory management" scenario verbatim: "check stock levels, predict restocking needs using historical data, and place orders with suppliers automatically."

**Q4.** Which scenario in the module involves connecting an AI agent to a learning management system (LMS) to recommend courses and track student progress?
A. Healthcare appointment scheduling
B. IT Helpdesk support
C. E-learning and training
D. Customer support automation
**Answer:** C — "E-learning and training" scenario: "connect the AI agent with their learning management system (LMS)... recommend courses, track student progress, and answer questions about course content."

**Q5.** In the Customer support automation scenario, what system does the custom tool connect the Azure AI Agent to?
A. An inventory management system
B. A customer relationship management (CRM) system
C. A learning management system (LMS)
D. A ticketing and knowledge base system
**Answer:** B — The scenario states "a custom tool that connects the Azure AI Agent to their customer relationship management (CRM) system," enabling order history retrieval, refund processing, and shipping updates.

**Q6.** Which outcome is associated with the IT Helpdesk support scenario in the module?
A. Streamlined inventory processes and optimized supply chain operations
B. Faster issue resolution, reduced downtime, and improved employee productivity
C. Enhanced learning experiences and increased student engagement
D. Reduced administrative burden and better resource utilization
**Answer:** B — IT Helpdesk support outcome: "Faster issue resolution, reduced downtime, and improved employee productivity." A is inventory management's outcome, C is e-learning's, D is healthcare scheduling's.

**Q7.** Why does adding tools to an agent make functionality "available" rather than guaranteed to run on every prompt?
A. Because tools run on a fixed schedule regardless of the prompt
B. Because the agent decides how to use tools depending on how it interprets the user prompt
C. Because tools must be manually triggered by the developer for each request
D. Because Foundry Agent Service requires a human approval step before every tool call by default
**Answer:** B — "Adding tools makes custom functionality available for the agent to use, depending on how it decides to respond to the user prompt" — tool invocation is model-driven, not fixed or manually triggered per this module.

## Options for implementing custom tools

**Q1.** Which FOUR custom tool options does Foundry Agent Service provide according to this module? (Choose four.)
A. Custom function (function calling)
B. Azure Functions
C. OpenAPI specification tools
D. Azure Logic Apps
E. Azure Data Factory pipelines
**Answer:** A, B, C, D — The module names exactly four options: custom function/function calling, Azure Functions, OpenAPI specification tools, and Azure Logic Apps. Azure Data Factory is not mentioned as a custom tool option in this module.

**Q2.** Which custom tool option is described as a "low-code/no-code solution to add workflows and connect apps, data, and services"?
A. Custom function
B. Azure Functions
C. OpenAPI specification tools
D. Azure Logic Apps
**Answer:** D — Azure Logic Apps is explicitly described this way. The other three all involve code or a technical specification (function code, serverless code, or an API spec).

**Q3.** In Azure Functions terminology as used in this module, what determines WHEN a function executes, versus what facilitates its connection to input/output data sources?
A. Bindings determine when it executes; triggers facilitate data source connections
B. Triggers determine when it executes; bindings facilitate data source connections
C. Both triggers and bindings determine execution timing only
D. Neither triggers nor bindings relate to execution — only HTTP endpoints do
**Answer:** B — "Triggers determine when a function executes, while bindings facilitate streamlined connections to input or output data sources." This is a classic exam distinction to memorize precisely.

**Q4.** What specification version does the module state OpenAPI specification tools use to connect an Azure AI Agent to an external API?
A. OpenAPI 2.0
B. OpenAPI 3.0
C. GraphQL schema definition language
D. WSDL 1.1
**Answer:** B — "These tools allow you to connect your Azure AI Agent to an external API using an OpenAPI 3.0 specification." Note the sample JSON in the "How to integrate" unit shows `"openapi": "3.1.0"`, but the module text consistently states 3.0 as the supported/documented version.

**Q5.** Function calling, as described in "Options for implementing custom tools," allows you to do what with respect to an agent?
A. Directly modify the underlying LLM's weights at inference time
B. Describe the structure of custom functions to an agent, which then dynamically identifies and returns the functions to call along with their arguments
C. Bypass the agent entirely and call your function from the client application
D. Automatically generate an OpenAPI spec from your Python function signature
**Answer:** B — "Function calling allows you to describe the structure of custom functions to an agent and return the functions that need to be called along with their arguments. The agent can dynamically identify appropriate functions based on their definitions."

**Q6.** What benefit do OpenAPI specifications provide, according to the module, beyond enabling API calls?
A. They enable people to understand how an API works, generate client code, create tests, and apply design standards
B. They automatically deploy the API to Azure App Service
C. They eliminate the need for authentication on any endpoint
D. They convert REST APIs into gRPC services automatically
**Answer:** A — This is stated directly: OpenAPI specs "describe HTTP APIs, enabling people to understand how an API works, generate client code, create tests, and apply design standards."

**Q7.** A company wants event-driven, serverless compute with minimal overhead to react to triggers such as HTTP requests or queue messages within its agent solution. Which custom tool option best fits, per the module?
A. OpenAPI specification tools
B. Azure Functions
C. Azure Logic Apps
D. Custom function (in-agent code)
**Answer:** B — Azure Functions "enables you to create intelligent, event-driven applications with minimal overhead" and "support triggers and bindings." Logic Apps is low-code/no-code workflow-oriented rather than serverless-code-oriented, making B the more precise match to "serverless... triggers such as HTTP requests or queue messages."

## How to integrate custom tools

**Q1.** In the Python function-calling example, what does the `recent_snowfall` function return?
A. A Python dictionary object
B. Snowfall details as a JSON string (via `json.dumps`)
C. An XML document
D. A pandas DataFrame
**Answer:** B — The function signature is `def recent_snowfall(location: str) -> str` and it returns `json.dumps({"location": location, "snowfall": snow})` — a JSON string.

**Q2.** When registering a function tool with the Azure AI SDK as shown in the module, which class is used to define the function tool's name, parameters, description, and strictness?
A. `AzureFunctionTool`
B. `OpenApiTool`
C. `FunctionTool`
D. `PromptAgentDefinition`
**Answer:** C — `FunctionTool(name=..., parameters={...}, description=..., strict=True)` is the class shown. `PromptAgentDefinition` is used afterward to define the agent itself (model, instructions, tools), not the individual tool.

**Q3.** In the `FunctionTool` parameters JSON schema example, what does setting `"additionalProperties": False` combined with `"required": ["location"]` enforce?
A. That `location` is optional but other properties are allowed
B. That only the `location` property is allowed and it must always be supplied
C. That the schema accepts any number of undefined properties as long as `location` is present
D. That the function returns only string types
**Answer:** B — `"required": ["location"]` makes `location` mandatory, and `"additionalProperties": False` disallows any properties not defined in the schema — together restricting input to exactly the `location` field.

**Q4.** Which model name is used in the code examples for both the function-calling agent and the Azure Function agent in this module?
A. `gpt-4o-mini`
B. `gpt-4.1`
C. `gpt-35-turbo`
D. `o1-preview`
**Answer:** B — Both `PromptAgentDefinition` examples in the module specify `model="gpt-4.1"`.

**Q5.** How does the agent in the Azure Functions example actually communicate with the deployed Azure Function?
A. Via a direct synchronous HTTP POST request
B. Via a storage queue — an input binding queue for requests and an output binding queue for results
C. Via a gRPC streaming channel
D. Via Azure Service Bus topics exclusively
**Answer:** B — The example configures `AzureFunctionDefinition` with `input_binding` and `output_binding`, both using `AzureFunctionStorageQueue` with `queue_name` and `queue_service_endpoint` — i.e., communication happens through storage queues, not direct HTTP.

**Q6.** Which THREE authentication types does the module state are supported with OpenAPI 3.0 tools in Foundry Agent Service? (Choose three.)
A. Anonymous
B. API key
C. Managed identity
D. OAuth 2.0 client credentials
E. Shared access signature (SAS) token
**Answer:** A, B, C — The module's tip states: "Currently, three authentication types are supported with OpenAPI 3.0 tools: anonymous, API key, and managed identity." OAuth 2.0 and SAS tokens are not listed as supported types in this module.

**Q7.** In the OpenAPI tool registration code, which class represents the "anonymous" authentication option passed to `OpenApiFunctionDefinition`'s `auth` parameter?
A. `OpenApiApiKeyAuthDetails`
B. `OpenApiManagedIdentityAuthDetails`
C. `OpenApiAnonymousAuthDetails`
D. `OpenApiNoAuthRequired`
**Answer:** C — The code imports and uses `OpenApiAnonymousAuthDetails()` as the `auth` argument to `OpenApiFunctionDefinition`. The other class names are plausible but not the one shown in the module's code sample.

**Q8.** What is the key conceptual point the module makes about how an agent decides to invoke a registered custom tool (function, Azure Function, or OpenAPI tool)?
A. The developer's application code must explicitly call the tool function at the appropriate point in the conversation
B. Tool use is declarative — the agent itself decides to call tool functions based on messages in prompts, without the developer writing explicit call logic
C. Tools are invoked on a round-robin schedule regardless of the conversation
D. Tool invocation requires the user to type an exact command like `/callTool`
**Answer:** B — The module's callout states: "You don't need to write code that explicitly calls your custom tool functions - the agent itself decides to call tool functions based on messages in prompts." This declarative nature applies across all three tool integration types covered.

**Q9.** In the OpenAPI spec JSON example (`weather_openapi.json`), what does the `format` query parameter's schema specify as its default value?
A. `"xml"`
B. `"j1"`
C. `"json"`
D. No default is specified
**Answer:** B — The spec shows `"name": "format", "in": "query", ..., "schema": {"type": "string", "default": "j1"}`, with the description noting to "Always use j1 value for this parameter."

**Q10.** Which SDK import is shown for constructing the OpenAPI tool's authentication and tool objects in the module's Python example?
A. `from azure.ai.projects.models import OpenApiTool, OpenApiAnonymousAuthDetails`
B. `from azure.ai.agents import OpenApiTool, ApiKeyAuth`
C. `from azure.functions import OpenApiTool`
D. `from openapi_spec_validator import OpenApiTool`
**Answer:** A — The module's code explicitly shows `from azure.ai.projects.models import OpenApiTool, OpenApiAnonymousAuthDetails`.

## Exercise - Build an agent with custom tools

**Q1.** What is the primary hands-on objective of the exercise unit?
A. Deploy a Logic App workflow visually with no code
B. Create an agent in code and connect the tool definition to a custom tool function
C. Fine-tune a GPT model on customer support transcripts
D. Configure Azure Content Understanding analyzers
**Answer:** B — The unit states: "In this exercise, you create an agent in code and connect the tool definition to a custom tool function."

**Q2.** Approximately how long is the exercise unit estimated to take?
A. 10 minutes
B. 30 minutes
C. 60 minutes
D. 2 hours
**Answer:** B — The unit header lists "30 minutes."

**Q3.** What does the module recommend if you don't already have an Azure subscription but want to complete the exercise?
A. Skip the exercise entirely — it cannot be completed without a paid subscription
B. Sign up for an Azure account, which includes credits for the first 30 days
C. Use a local emulator instead of Azure resources
D. Request a Microsoft Learn sandbox extension via support ticket
**Answer:** B — The module states you can "sign up for an account, which includes credits for the first 30 days" if you don't have an Azure subscription.

**Q4.** What best-practice tip does the module give for after completing the exercise?
A. Leave all resources running in case you want to repeat the exercise
B. Delete the Azure resources you created during the exercise once you're finished exploring
C. Export the agent definition to GitHub for version control
D. Downgrade the resources to a free tier automatically
**Answer:** B — "After completing the exercise, if you're finished exploring Azure AI Agents, delete the Azure resources that you created during the exercise."

**Q5.** How is the exercise launched from the Microsoft Learn module page?
A. Through an embedded Jupyter notebook directly on the page
B. Via an external link/button that opens the interactive exercise sandbox
C. By downloading a ZIP file of exercise instructions
D. Through the Azure CLI using a provided script only
**Answer:** B — The unit provides a "Launch exercise" button/link ("Launch the exercise and follow the instructions") pointing to an external fwlink.

**Q6.** [general Azure knowledge] Which of the following is generally true about Microsoft Learn sandbox/exercise environments for Foundry Agent Service exercises like this one?
A. They always run entirely offline with no real Azure resource provisioning
B. They typically provision real Azure resources under your subscription, which can incur cost if not cleaned up
C. They are limited strictly to read-only demonstrations
D. They require no Azure subscription under any circumstances
**Answer:** B — Consistent with the module's own tip to delete resources afterward, Learn exercises for services like this typically provision real resources in your subscription that should be cleaned up to avoid ongoing charges.

## Module assessment

**Q1.** Per the module assessment, what best answers: "What are custom tools, and how can they help you develop effective agents with Microsoft Foundry Agent Service?"
A. Extensions for Visual Studio Code that make it easier to create and deploy agents
B. Callable functions that an agent can use to extend its capabilities
C. Fine-tuned models that the agent can use to generate custom output
D. Prebuilt UI components for the Foundry portal chat window
**Answer:** B — This matches the module's own conceptual framing of custom tools as functionality (callable functions) the agent can invoke to extend what it can do. A and C describe unrelated concepts (IDE tooling, fine-tuning) not covered as "custom tools" in this module.

**Q2.** The module assessment asks: "You need to integrate functionality from an OpenAPI 3.0-based web service into an agent solution. What should you do?" What is the correct choice?
A. Add the JSON schema of the web service to the agent's instructions
B. Rewrite the web service as a Python function and hard-code it in your agent app
C. Add the web service as an OpenAPI specification tool to the agent definition
D. Convert the OpenAPI spec into an Azure Function app before registering it
**Answer:** C — This directly matches the "OpenAPI specification tools" mechanism taught in the module: connect the agent to an external API using its OpenAPI 3.0 spec, registered as a tool in the agent definition (via `OpenApiTool`/`OpenApiFunctionDefinition`).

**Q3.** The module assessment asks: "Your agent application code includes a local function that you want the agent to call. What kind of tool should you add to the agent's definition?" What is the correct choice?
A. Code interpreter
B. Azure Functions
C. Function calling
D. Azure Logic Apps
**Answer:** C — Function calling is specifically for functions defined within your own agent application code that the agent can call dynamically, as shown by the `recent_snowfall` example. Azure Functions is for externally deployed serverless functions (via storage queue), and Code interpreter is a distractor never covered as a custom tool in this module (it is a separate built-in tool).

**Q4.** Why is "Code interpreter" an incorrect answer for a scenario needing to call a local in-app function?
A. Because Code interpreter is a built-in Foundry Agent Service tool for running/generating code, not a mechanism for wiring in your own predefined local functions
B. Because Code interpreter only works with Azure Logic Apps
C. Because Code interpreter requires an OpenAPI 3.0 specification
D. Because Code interpreter is deprecated in favor of function calling
**Answer:** A — The module's introduction notes built-in tools exist "for gathering knowledge and generating code," distinct from custom tools like function calling that let the agent call your own predefined local functions.

**Q5.** Why would "Rewrite the web service as a Python function and hard-code it in your agent app" be a poor approach for integrating an OpenAPI 3.0-based web service?
A. Because Python does not support calling web services
B. Because it discards the standardized, automated, scalable integration that OpenAPI specification tools already provide, requiring unnecessary duplicate engineering effort
C. Because OpenAPI specs cannot be parsed by Python at all
D. Because Foundry Agent Service blocks all custom Python functions
**Answer:** B — The module states OpenAPI tools provide "standardized, automated, and scalable API integrations" — hard-coding a rewrite forfeits this and duplicates work the OpenAPI tool option already handles declaratively.

**Q6.** Which pairing of module-assessment question and correct custom-tool option is accurate?
A. Local in-app function → OpenAPI specification tool
B. External OpenAPI 3.0 web service → Function calling
C. Local in-app function → Function calling
D. External OpenAPI 3.0 web service → Azure Logic Apps
**Answer:** C — Local/in-app functions map to function calling; external OpenAPI 3.0 services map to OpenAPI specification tools (not Logic Apps, which is a separate low-code/no-code option not mentioned in the assessment's correct answers).

## Summary

**Q1.** According to the summary, what is the overall effect of integrating custom tools into Foundry Agent Service?
A. It boosts productivity and provides tailored business solutions, optimizing processes for specific needs
B. It removes the need for any agent instructions
C. It automatically migrates agents to a different Azure region
D. It disables built-in tools to reduce cost
**Answer:** A — The summary states custom tools "boost productivity and provide tailored business solutions" and help "optimize processes to meet specific needs, resulting in better responses from your agent."

**Q2.** The summary states the techniques learned enable businesses to do which of the following?
A. Generate marketing materials, improve communications, and analyze market trends more effectively
B. Automatically comply with GDPR without configuration
C. Replace their CRM and ERP systems entirely
D. Eliminate the need for Azure subscriptions
**Answer:** A — Verbatim from the summary: "The techniques learned in this module enable businesses to generate marketing materials, improve communications, and analyze market trends more effectively."

**Q3.** Which two tool categories does the summary explicitly call out as enabling "intelligent, event-driven applications" built on well-established patterns?
A. Code interpreter and File search
B. Azure Functions and OpenAPI specifications
C. Azure Logic Apps and Azure Data Factory
D. Bing grounding and Azure AI Search
**Answer:** B — "The integration of various tool options in the AI Agent Service, from Azure Functions to OpenAPI specifications, allows for the creation of intelligent, event-driven applications."

**Q4.** Which of the following is listed as further reading in the module summary?
A. Microsoft Foundry Agent Service function calling documentation
B. Azure OpenAI Service pricing calculator
C. Azure DevOps pipeline YAML reference
D. Microsoft Purview compliance documentation
**Answer:** A — The further reading list includes "Microsoft Foundry Agent Service function calling" (linking to the how-to/tools/function-calling docs). The other options are not listed.

**Q5.** The "Introduction to Azure Functions" link in the further reading section supports which topic area from earlier in the module?
A. The OpenAPI specification tool option
B. The Azure Logic Apps option
C. The Azure Functions custom tool option (triggers, bindings, serverless compute)
D. The Module assessment scoring rubric
**Answer:** C — This further-reading link directly extends the "Azure Functions" custom tool option covered in the "Options for implementing custom tools" and "How to integrate custom tools" units.

**Q6.** Which external (non-Microsoft-Learn) resource is listed in the further reading section, and what does it define?
A. swagger.io — the OpenAPI Specification
B. github.com/microsoft — the Azure SDK reference
C. python.org — the `json` module documentation
D. cncf.io — the Kubernetes API specification
**Answer:** A — "OpenAPI Specification" links to swagger.io/specification, which defines the OpenAPI Specification standard referenced throughout the "OpenAPI Specification" sections of the module.

**Q7.** [general Azure knowledge] Beyond this module's scope, which Microsoft Learn module is recommended as a prerequisite for deeper familiarity with Foundry Agent Service before taking this one?
A. Fundamentals of Generative AI
B. Develop an AI agent with Microsoft Foundry Agent Service
C. Implement Content Understanding solutions in Foundry
D. Build a RAG solution with Azure AI Search
**Answer:** B — Listed under Prerequisites: "It's highly recommended you have experience with the Microsoft Foundry Agent Service. You can learn more with Develop an AI agent with Microsoft Foundry Agent Service." (Fundamentals of Generative AI is also a prerequisite but addresses generative AI fundamentals, not agent-service-specific experience.)
