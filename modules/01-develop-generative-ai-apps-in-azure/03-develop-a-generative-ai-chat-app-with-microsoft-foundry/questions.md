# Practice questions — Develop a generative AI chat app with Microsoft Foundry

## Explore with the model playground

**Q1.** In the Foundry portal's Model playground, what does selecting the "Code" button in the chat pane provide?

A. A downloadable ARM template for the whole project, including resource definitions, role assignments, and network configuration
B. Code samples pre-populated with your project endpoint, model deployment name, and current settings, with choices for API, language, and SDK
C. A CI/CD pipeline YAML file preconfigured for Azure DevOps or GitHub Actions to automate model deployment
D. A cost estimate for the current session broken down by input tokens, output tokens, and the selected deployment tier

**Answer:** B — The module states the Code button provides samples "pre-populated with your project endpoint, model deployment name, and current settings," with choices for API (Responses/ChatCompletions), Language, and SDK.

**Q2.** What is the recommended workflow order for building an AI application with Microsoft Foundry, per this module?

A. Develop application → explore in playground → generate code → iterate
B. Explore in the playground → generate code samples → develop your application → iterate and refine
C. Generate code samples → deploy to production → explore in the playground
D. Iterate and refine → explore in playground → generate code → develop

**Answer:** B — This is the exact four-step workflow given: explore, generate code, develop, iterate/refine (returning to the playground as needed).

**Q21.** Where in the Foundry portal do you access the Model playground, and which actions can you perform there before writing any code?

A. Build → Evaluation; you can only view past evaluation runs and their aggregate quality, safety, and performance scores, without adjusting any model settings interactively
B. Left navigation → Model playground; you can send prompts to deployed models and see responses in real time, adjust settings like temperature/max tokens, add system messages, and experiment with different models/configurations
C. Settings → Billing; you can only view cost estimates broken down by input/output token pricing for each deployment, without any interactive prompt testing capability
D. Discover → Models; you can only read model cards, benchmark metrics, and responsible AI considerations, not send prompts or adjust generation settings

**Answer:** B — The module describes the Model playground (accessed via the left navigation) as a no-code interactive environment that lets you send prompts and see real-time responses, adjust settings like temperature and max tokens, add system messages, and experiment with different models/configurations.

**Q22.** What caution does the module explicitly give regarding Microsoft Foundry features covered in this module?

A. They are deprecated and will be removed within a year, per a Learn retirement notice
B. Some Microsoft Foundry features are currently in preview and subject to change
C. They require a paid enterprise agreement to access, unlike free-tier Foundry features
D. They are only available in the Azure US Government cloud

**Answer:** B — The module includes an explicit caution: "Some Microsoft Foundry features are currently in preview and subject to change."

## Choose an endpoint and SDK

**Q3.** Which TWO endpoints does every Microsoft Foundry project provide for client applications? (Choose 2.)

A. Project endpoint
B. Azure OpenAI endpoint
C. Azure Cognitive Search endpoint
D. Azure Key Vault endpoint

**Answer:** A, B — "Each project has both a Project endpoint and an Azure OpenAI endpoint." C and D are unrelated Azure services, not Foundry project client endpoints.

**Q4.** A developer needs to build an agent that uses tool invocation/approval workflows, cloud evaluations, and tracing. Which SDK does Microsoft recommend?

A. OpenAI SDK exclusively
B. Microsoft Foundry SDK
C. Azure Cognitive Services SDK
D. Azure Functions SDK

**Answer:** B — The module explicitly lists Foundry Agent Service, tool invocation/approval workflows, cloud evaluations, and tracing/observability as reasons to use the Foundry SDK, and states "Microsoft recommends the Foundry SDK when building apps with agents, evaluations, or Foundry-specific features."

**Q5.** What object do you obtain by calling `project_client.get_openai_client(api_version="2024-10-21")` on an `AIProjectClient`?

A. An Azure Machine Learning workspace client used for training and compute management
B. An OpenAI-compatible client object for submitting prompts to models
C. A Foundry IQ knowledge connection linking the project to external document repositories
D. A vector store client used for embedding storage and semantic retrieval operations

**Answer:** B — The module states: "To chat with a model in your Foundry project, you need an OpenAI-compatible client object. You can use the get_openai_client() method of the project client to get one."

**Q6.** Which authentication method does Microsoft recommend for PRODUCTION applications connecting to Foundry/Azure OpenAI endpoints?

A. API key stored in source code
B. Anonymous access with no credentials
C. Microsoft Entra ID authentication
D. Shared access signature (SAS) tokens

**Answer:** C — "In general, production applications should use Microsoft Entra ID authentication, which requires the application to be running in the context of a specific identity." The module also cautions that API keys should be used carefully and stored in Key Vault, never hardcoded — implying they are not the production-recommended default.

**Q7.** Which class provides Foundry-native operations that have NO OpenAI equivalent, such as retrieving resource connections, accessing project configuration, enabling tracing, and managing datasets/indexes?

A. OpenAI client
B. AzureOpenAI
C. AIProjectClient
D. AsyncOpenAI

**Answer:** C — The module states: "The project client (AIProjectClient) provides access to Foundry-native operations that don't have OpenAI equivalents," listing exactly these four capabilities.

**Q8.** A developer needs to use a specific, pinned version of the Azure OpenAI API rather than the general v1 endpoint behavior. Which client object should they instantiate, and what two parameters must they specify?

A. `OpenAI`, specifying `base_url` and `api_key`
B. `AzureOpenAI`, specifying `azure_endpoint` and `api_version`
C. `AIProjectClient`, specifying `credential` and `endpoint`
D. `AsyncOpenAI`, specifying `stream` and `model`

**Answer:** B — "you also have the option to create an AzureOpenAI client object if you need to use functionality from a specific version of the Azure OpenAI API. To create an AzureOpenAI client object, you must specify the API version and the Azure endpoint."

**Q9.** True or false: The Foundry SDK and OpenAI SDK are mutually exclusive — an application must choose exactly one and cannot use both.

A. True — mixing SDKs is unsupported, since the Foundry SDK and OpenAI SDK use incompatible authentication formats
B. False — both SDKs work with your Foundry project endpoint and can be combined in the same application
C. True, but only if using the Responses API, which the module says cannot share a client with the Foundry SDK
D. False, but only for non-production applications, since production deployments require picking exactly one SDK

**Answer:** B — The module explicitly states: "You can also use both SDKs together in the same application—the Foundry SDK for project features and the OpenAI SDK for model inference."

**Q23.** The Foundry SDK's client libraries for accessing project resources are distributed across three language ecosystems. Which pairing is correct, per the module?

A. Python via PyPI (Azure AI Projects), .NET via NuGet, JavaScript via npm
B. Python via npm, .NET via PyPI, JavaScript via NuGet
C. All three languages share a single unified package published only on npm
D. Only Python is supported; .NET and JavaScript are not available

**Answer:** A — The module lists "Azure AI Projects for Python (PyPI)," "Azure AI Projects for .NET (NuGet)," and "Azure AI Projects for JavaScript (npm)," each developed/maintained independently.

**Q24.** When installing the Microsoft Foundry SDK for Python chat app development (`pip install azure-ai-projects azure-identity openai`), why must the `openai` package also be installed?

A. Because the chat client functionality in the Foundry SDK derives from the OpenAI SDK
B. Because `azure-identity` requires `openai` as a dependency for token caching
C. It is not actually required at all, just optional and recommended for convenience
D. Because Foundry direct models can only be called via raw HTTP requests otherwise

**Answer:** A — The module notes: "the chat client functionality in the Foundry SDK derives from the OpenAI SDK, so the openai package must also be installed/imported."

**Q25.** Which of the following is the correct format for a Microsoft Foundry project endpoint, as found on the project's Overview page?

A. `https://{resource-name}.openai.azure.com/openai/v1?api-version=2024-10-21`
B. `https://{resource-name}.services.ai.azure.com/api/projects/<project-name>`
C. `https://api.openai.com/v1/projects/<project-name>?api-version=2024-10-21`
D. `https://{resource-name}.cognitiveservices.azure.com/projects/<project-name>`

**Answer:** B — This is the exact project endpoint format shown in the module. Option A is a close distractor — it's actually the Azure OpenAI endpoint format, not the project endpoint format.

**Q26.** Before running Python code that instantiates `AIProjectClient(credential=DefaultAzureCredential(), endpoint=project_endpoint)`, what must be true of the execution environment?

A. Nothing; `DefaultAzureCredential` works without any prior authentication
B. The code must run in an authenticated Azure session, e.g. after running `az login` via the Azure CLI
C. An API key must be hardcoded into the script before `AIProjectClient` will accept any requests
D. The environment must have SSH keys configured and registered with the project's access control settings

**Answer:** B — The module states the code "must run in an authenticated Azure session (for example, after running az login via the Azure CLI)," since `DefaultAzureCredential` relies on ambient credentials.

**Q27.** When installing the OpenAI SDK (`pip install openai azure-identity`) for use against an Azure OpenAI endpoint, when is the `azure-identity` package actually needed?

A. Always, for every possible authentication method
B. Only for token-based Microsoft Entra ID authentication
C. Only for API-key authentication against the Azure OpenAI endpoint
D. It is never needed with the OpenAI SDK

**Answer:** B — The module notes `azure-identity` is "needed only for token-based Microsoft Entra ID auth," not for the simpler API-key connection method.

**Q28.** Which is the correct Azure OpenAI endpoint format used with the OpenAI SDK's `base_url` parameter?

A. `https://{resource-name}.services.ai.azure.com/api/projects/<project-name>`
B. `https://{resource-name}.openai.azure.com/openai/v1`
C. `https://openai.azure.com/{resource-name}/v1`
D. `https://{resource-name}.ai.azure.com/openai`

**Answer:** B — This is the exact Azure OpenAI endpoint format given in the module (contrast with the project endpoint format in option A, which is a deliberate close distractor).

**Q29.** When connecting the OpenAI SDK client to Azure OpenAI using Microsoft Entra ID (the recommended approach), which function supplies the `api_key` parameter with a refreshable token instead of a static string?

A. `get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")`
B. `get_api_key_from_vault()`
C. `AIProjectClient.get_token()`
D. `os.getenv("AZURE_OPENAI_API_KEY")`

**Answer:** A — The module's Entra ID connection example passes `token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")` as the `api_key` argument to the `OpenAI` client.

**Q30.** Which environment variables does the OpenAI SDK automatically pick up when you instantiate `OpenAI()` with no explicit arguments?

A. `AZURE_ENDPOINT` and `AZURE_KEY`
B. `OPENAI_BASE_URL` and `OPENAI_API_KEY`
C. `FOUNDRY_PROJECT_ENDPOINT` and `FOUNDRY_API_KEY`
D. `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT` only

**Answer:** B — The module shows `openai_client = OpenAI()  # Uses environment variables`, noting `OPENAI_BASE_URL` and `OPENAI_API_KEY` are picked up automatically.

**Q31.** Besides chat completions and the Responses API, what else does the module say the `OpenAI` client handles?

A. Image generation and accessing Foundry direct models
B. Virtual network configuration
C. Billing and quota management
D. Role-based access control assignment

**Answer:** A — "The OpenAI client handles model inference operations: generating responses (Responses API), chat completions, image generation, and accessing Foundry direct models (non-Azure OpenAI models)."

**Q32.** Per the module, which scenario is the OpenAI SDK ideal for, and which capability does it explicitly NOT provide?

A. Agent-heavy apps; it lacks Responses API support
B. Model-inference-only workloads wanting full OpenAI-API compatibility and portability; it does not provide Foundry-specific features like agents or evaluations
C. Cloud-evaluation workloads; it lacks chat completions support
D. Tracing/observability workloads; it lacks image generation support

**Answer:** B — "The OpenAI SDK is ideal for model-inference-only workloads wanting existing OpenAI code with minimal changes—but it does NOT provide Foundry-specific features like agents or evaluations."

## Generate responses with the Responses API

**Q10.** Which parameter of the Responses API's `responses.create()` method is used to link a new call to a prior turn's response, enabling stateful multi-turn conversation without manually resending history?

A. `conversation_id`
B. `previous_response_id`
C. `thread_id`
D. `session_token`

**Answer:** B — "The previous_response_id parameter links responses together, maintaining conversation context across multiple API calls." This is a core Responses-API-specific feature not present in ChatCompletions.

**Q11.** What is the valid range for the `temperature` parameter in the Responses API, and what does a HIGHER value produce?

A. 0.0–1.0; lower creativity
B. 0.0–2.0; more creative and varied output
C. 1–100; more deterministic output
D. -1.0–1.0; no effect on creativity

**Answer:** B — "temperature: Controls randomness (0.0-2.0). Higher values make output more creative and varied."

**Q12.** Which property of a Responses API response object contains the generated text?

A. `response.choices[0].message.content`
B. `response.output_text`
C. `response.text`
D. `response.completion`

**Answer:** B — The module repeatedly uses `response.output_text` for the Responses API. Option A (`choices[0].message.content`) is actually the ChatCompletions API's accessor — a deliberate close distractor testing whether the candidate confuses the two APIs.

**Q13.** A conversational app connects to a Foundry project endpoint using the Responses API and sets `model="microsoft-phi-4"`. What does this demonstrate?

A. This is invalid; the Responses API only works with Azure OpenAI models
B. The Responses API can work with Foundry direct models — models hosted directly in Microsoft Foundry, not just Azure OpenAI models
C. Phi-4 requires the ChatCompletions API instead
D. This requires a separate Phi-specific SDK

**Answer:** B — The module explicitly demonstrates calling `responses.create()` with `model="microsoft-phi-4"` as "an example Foundry direct model," and states the Responses API "works with models hosted directly in Microsoft Foundry, not just Azure OpenAI models" (also naming DeepSeek as another example).

**Q14.** When streaming a Responses API call (`stream=True`) and iterating over events, which event type signals that the full response has finished, letting you capture the final response ID?

A. `response.output_text.delta`
B. `response.completed`
C. `response.chunk.end`
D. `stream.close`

**Answer:** B — The example code checks `elif event.type == "response.completed": response_id = event.response.id`, while `response.output_text.delta` (A) is the event type used for incremental text chunks, not completion.

**Q15.** Which of the following are explicitly listed as components of the active context window sent to the model on EVERY request in a Responses API conversation? (Choose THREE.)

A. System instructions
B. Tool schemas (functions, OpenAPI specs, MCP tools)
C. The Azure subscription ID
D. Conversation history (previous user + assistant messages)

**Answer:** A, B, D — The module lists: system instructions, current prompt, conversation history, tool schemas, tool outputs, and retrieved memory/documents as concatenated and sent on every request. The Azure subscription ID (C) is not part of the model's context window.

**Q16.** To make non-blocking, concurrent API calls to the Responses API for a high-performance application, which client class should be imported instead of `OpenAI`?

A. `AzureOpenAI`
B. `AIProjectClient`
C. `AsyncOpenAI`
D. `ConcurrentOpenAI`

**Answer:** C — "To use it, import AsyncOpenAI instead of OpenAI and use await with each API call." This supports async/concurrent, non-blocking usage.

**Q33.** Which two previously separate OpenAI APIs does the Responses API unify into a single interface?

A. ChatCompletions and Assistants API
B. Embeddings and Images API
C. Foundry SDK and OpenAI SDK
D. Completions and Fine-tuning API

**Answer:** A — "The OpenAI Responses API unifies capabilities previously split across two APIs: ChatCompletions and Assistants," providing stateful, multi-turn response generation.

**Q34.** Which set of advantages does the module explicitly list for the Responses API?

A. Stateful conversations, unified experience, support for Foundry direct models, simple integration
B. Lower cost, faster latency, smaller payloads, no authentication required
C. Multi-region replication, autoscaling, encryption at rest, DDoS protection
D. Built-in RAG, built-in fine-tuning, built-in evaluation, built-in translation

**Answer:** A — The module lists exactly these four advantages under "Advantages of the Responses API."

**Q35.** Besides `output_text`, which set of properties does a Responses API response object expose, per the module?

A. `id`, `status`, `usage`, `model`
B. `choices`, `index`, `finish_reason`
C. `embedding`, `dimensions`
D. `thread_id`, `run_id`

**Answer:** A — The module lists `id` (unique identifier), `status` (e.g., "completed"), `usage` (token usage — input/output/total), and `model` (model used), alongside `output_text`.

**Q36.** Which parameter of `responses.create()` sets the system-prompt-like guidance for the assistant's behavior across the call?

A. `system`
B. `instructions`
C. `role`
D. `context`

**Answer:** B — The module's example passes `instructions="You are a helpful AI assistant that answers questions clearly and concisely."` as a dedicated parameter, distinct from `input`.

**Q37.** Besides `temperature`, which Responses API parameter is described as "an alternative to temperature for controlling randomness"?

A. `max_output_tokens`
B. `top_p`
C. `previous_response_id`
D. `stream`

**Answer:** B — The module lists `top_p` as an alternative to `temperature` for controlling randomness, alongside `max_output_tokens` (which instead limits response length, not randomness).

**Q38.** A developer wants full manual control over exactly which messages are included in each request — e.g., to prune older turns for token limits or restore history from a database — rather than relying on `previous_response_id`. Which approach does the module describe for this?

A. Setting `stream=True`
B. Manual conversation chaining — building a `conversation_history` list of message objects yourself and passing it as `input`
C. Using the ChatCompletions API's `previous_response_id`
D. Calling `responses.retrieve()` repeatedly

**Answer:** B — The module's "Alternative: manual conversation chaining" section describes exactly this, noting it's useful to "customize which messages are included, implement conversation pruning for token limits, or store/restore history from a database."

**Q39.** Which method call retrieves a previously generated Responses API response by its ID?

A. `openai_client.responses.create(id=response_id)`
B. `openai_client.responses.retrieve(response_id)`
C. `openai_client.responses.get_history(response_id)`
D. `openai_client.responses.fetch(id=response_id)`

**Answer:** B — The module's example: `previous_response = openai_client.responses.retrieve(response_id)`.

**Q40.** Which statement about the Responses API's context window is correct, per the module's explicit caution?

A. Using `previous_response_id` reduces token usage because Azure caches prior turns server-side for free
B. The SDK manages conversation state for you, but does NOT make token usage cheaper — all context (instructions, prompt, history, tool schemas/outputs, retrieved documents) is concatenated, tokenized, and sent on every request
C. Context window size is unlimited when using the Responses API
D. Token usage only applies to the ChatCompletions API, not the Responses API

**Answer:** B — The module states plainly: "the SDK manages state but does NOT make token usage cheaper," since the full active context is concatenated, tokenized, and sent together with every request.

**Q41.** To enable streaming output from `responses.create()`, which parameter is set, and how is the result typically consumed?

A. `async=True`; consumed with `await`
B. `stream=True`; consumed by iterating over the returned object with a `for` loop over events
C. `mode="stream"`; consumed by calling `.read()` once
D. `output_format="stream"`; parsed as JSON afterward

**Answer:** B — The module's example sets `stream=True` and then does `for event in stream: print(event, end="", flush=True)`.

**Q42.** For a long-running or high-concurrency application using async streaming with the Responses API, which looping construct is used to consume stream events?

A. A standard `for` loop
B. `async for`
C. `while True` with manual polling
D. `Promise.all()`

**Answer:** B — "Async streaming uses async for," as shown in the module's `async def stream_response()` example.

## Generate responses with the ChatCompletions API

**Q17.** What data structure does the ChatCompletions API use to encapsulate a prompt and conversation, and what is one required field per entry?

A. A single string containing the full conversation; no fields required
B. A collection of message objects in JSON, each with a `role` (e.g., system/user/assistant) and `content` field
C. A `previous_response_id` reference chain
D. A binary-encoded protobuf message

**Answer:** B — "The ChatCompletions API uses collections of message objects in JSON format to encapsulate prompts," shown with `{"role": "system", "content": "..."}` style entries.

**Q18.** How is the assistant's generated text retrieved from a ChatCompletions API response object?

A. `response.output_text`
B. `completion.choices[0].message.content`
C. `completion.result.text`
D. `completion.output[0].content`

**Answer:** B — The module's code consistently uses `completion.choices[0].message.content`. This is the key structural difference from the Responses API's `response.output_text` — a likely point of exam confusion between the two APIs.

**Q19.** Which statement correctly describes how conversational context is retained when using the ChatCompletions API, in contrast to the Responses API?

A. ChatCompletions automatically tracks context using a `previous_response_id`-equivalent parameter
B. ChatCompletions has no stateful tracking feature; the developer must manually append each user/assistant message to a running `messages` list and resend the full history each call
C. ChatCompletions context is retained server-side indefinitely with no client action needed
D. ChatCompletions cannot support multi-turn conversations at all

**Answer:** B — "Unlike the Responses API, the ChatCompletions API doesn't provide a stateful response tracking feature. To retain conversational context, you must write code to manually track previous prompts and responses," appending user and assistant messages to a `conversation_messages` list that's resent every call.

**Q20.** Given that the Responses API is recommended for new projects, in which scenario does the module suggest the ChatCompletions API is still useful?

A. Never — it should not be used in any new or existing code
B. For code maintenance or cross-platform compatibility, since it's well-established across many generative AI models and platforms
C. Only when using Foundry direct models
D. Only for image generation tasks

**Answer:** B — "Although the Responses API is recommended for new project development, it's likely that you'll encounter scenarios where the ChatCompletions API is useful for code maintenance or cross-platform compatibility... it's well established in the generative AI model ecosystem."

**Q43.** Which three role values appear in ChatCompletions `messages` entries across the module's examples?

A. system, user, assistant
B. sender, receiver, bot
C. input, output, context
D. prompt, completion, model

**Answer:** A — The module's examples use `role: "system"` for behavior-setting instructions, `role: "user"` for the human's input, and `role: "assistant"` for the model's prior responses appended back into history.

**Q44.** In the ChatCompletions interactive loop pattern described by the module, what must happen after each API call to preserve context for the next turn?

A. Nothing; the API tracks it automatically
B. The assistant's response must be manually appended to the `conversation_messages` list (along with the next user message) before the next call
C. You must call `responses.retrieve()`
D. You must restart the client object

**Answer:** B — The module's loop pattern: "append each user input, call the API, append the assistant response, repeat. The entire conversation history is resubmitted every turn."

**Q45.** Which model deployment name is used in the module's ChatCompletions code examples, as opposed to the `gpt-4.1` used in the Responses API examples?

A. gpt-4o
B. gpt-3.5-turbo
C. microsoft-phi-4
D. text-davinci-003

**Answer:** A — The module's ChatCompletions examples consistently use `model="gpt-4o"`.

## Scenario-based questions

**Q46.** A developer wants to build an agent-based application that also needs maximum OpenAI-code portability for a subset of simple chat features shared with a non-Azure OpenAI product. Which SDK strategy best fits, per the module's guidance?

A. Use only the OpenAI SDK for everything, since the Foundry SDK cannot be combined with it
B. Use the Foundry SDK (`AIProjectClient`) for agent/evaluation/tracing features, and the OpenAI SDK for the portable chat-inference code, combined in the same application
C. Use only the Foundry SDK, since it fully replaces the OpenAI SDK for chat completions
D. Rewrite the shared chat code twice, once per cloud provider, since SDKs cannot share an endpoint

**Answer:** B — The module explicitly supports combining both SDKs in the same application: Foundry SDK for project features (agents, evaluations, tracing, connections), OpenAI SDK for model inference/portability.

**Q47.** A team is migrating a legacy ChatCompletions-based application to take advantage of stateful multi-turn conversations without manually resending full message history, while also wanting the option to call newer Foundry direct models like DeepSeek. Which API should they migrate to, and which parameter enables the stateful behavior?

A. Stay on ChatCompletions; use `role: assistant`
B. Migrate to the Responses API; use `previous_response_id`
C. Migrate to the Assistants API; use `thread_id`
D. Migrate to the Embeddings API; use `dimensions`

**Answer:** B — The Responses API provides built-in statefulness via `previous_response_id` and explicitly supports Foundry direct models (e.g., Microsoft Phi, DeepSeek), unlike ChatCompletions.

**Q48.** A production application must authenticate to the Azure OpenAI endpoint without ever storing a static secret in code, using an identity-based token that is automatically refreshed. Which combination satisfies this, per the module?

A. `openai` package only, using `api_key=os.getenv("AZURE_OPENAI_API_KEY")`
B. `azure-identity`'s `get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")` supplied as the `api_key` parameter of the `OpenAI` client
C. Hardcoding the key directly for simplicity, then rotating it manually every 90 days
D. SSH key-based authentication via `azure-identity`

**Answer:** B — This is the module's recommended production connection pattern: Entra ID authentication via a bearer token provider, avoiding any static secret in source code.

**Q49.** A developer building a streaming chat UI wants to know the response ID as soon as generation completes, and separately wants to render partial text as it streams. Which two event types/techniques from the Responses API streaming example should they use together?

A. `response.output_text.delta` for partial text chunks, and `response.completed` (via `event.response.id`) to capture the final response ID
B. `stream.chunk` for partial text, and `stream.end` for the ID
C. `completion.choices[0].message.content` for partial text, and `completion.id` for the final ID
D. `previous_response_id` for partial text, and `output_text` for the ID

**Answer:** A — The module's streaming example checks `event.type == "response.output_text.delta"` for incremental text and `event.type == "response.completed"` to capture `event.response.id`.

**Q50.** A developer needs to explain why increasing `temperature` to 1.8 and setting `max_output_tokens=50` together produced a truncated but highly varied story. Which pairing of parameter effects explains this?

A. `temperature` controls response length; `max_output_tokens` controls randomness
B. `temperature` (0.0–2.0) controls randomness/creativity — higher is more varied; `max_output_tokens` caps the number of tokens in the response, which can truncate longer creative output
C. Both parameters control only the model's context window size
D. `max_output_tokens` controls creativity; `temperature` controls token limits

**Answer:** B — `temperature` and `max_output_tokens` are independent controls: one governs randomness/creativity, the other caps output length, and a high-creativity, low-token-limit combination naturally produces varied but truncated text.

**Q51.** A team wants to test a model's behavior interactively before writing any code, adjusting temperature and system messages, and then generate a starter code sample already wired to their exact project endpoint and deployment name. Which Foundry portal workflow accomplishes this without manual endpoint copying?

A. Manually write boilerplate code from scratch by reading values off the Azure Portal
B. Use the Model playground to test prompts/settings, then use the Code button to generate samples pre-populated with the project endpoint, model deployment name, and current settings
C. Use the Evaluator library exclusively
D. Use `AIProjectClient.get_openai_client()` without ever opening the portal

**Answer:** B — This is exactly the "Explore in the playground" → "Generate code samples" workflow described in the module, with the Code button auto-populating endpoint/deployment/settings.

**Q52.** An application currently uses the ChatCompletions API and manually resends the full `conversation_messages` list on every call. The team is concerned about growing token costs as conversations lengthen, regardless of which API they use. Which statement correctly combines both API sections' guidance on this?

A. Switching to the Responses API's `previous_response_id` eliminates token costs entirely since Azure caches history for free
B. Whether using ChatCompletions (manual history) or the Responses API (`previous_response_id` / manual chaining), the full active context is tokenized and billed on every request; the Responses API only manages state bookkeeping for you, it doesn't make tokens cheaper — pruning strategies (e.g., manual conversation chaining) help control cost either way
C. Only ChatCompletions incurs token costs for history; the Responses API is entirely free for conversation context
D. Neither API charges for conversation history, only for the current turn's input

**Answer:** B — Both APIs resend/reconstruct full context on each call (explicitly or via state linkage), and the module explicitly warns the Responses API's statefulness is a bookkeeping convenience, not a cost reduction — manual conversation chaining/pruning is the documented lever for controlling token growth.
