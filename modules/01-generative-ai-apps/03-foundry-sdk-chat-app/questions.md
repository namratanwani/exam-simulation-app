# Practice questions — Develop a generative AI chat app with Microsoft Foundry

## Explore with the model playground

**Q1.** In the Foundry portal's Model playground, what does selecting the "Code" button in the chat pane provide?

A. A downloadable ARM template for the whole project
B. Code samples pre-populated with your project endpoint, model deployment name, and current settings, with choices for API, language, and SDK
C. A CI/CD pipeline YAML file
D. A cost estimate for the current session

**Answer:** B — The module states the Code button provides samples "pre-populated with your project endpoint, model deployment name, and current settings," with choices for API (Responses/ChatCompletions), Language, and SDK.

**Q2.** What is the recommended workflow order for building an AI application with Microsoft Foundry, per this module?

A. Develop application → explore in playground → generate code → iterate
B. Explore in the playground → generate code samples → develop your application → iterate and refine
C. Generate code samples → deploy to production → explore in the playground
D. Iterate and refine → explore in playground → generate code → develop

**Answer:** B — This is the exact four-step workflow given: explore, generate code, develop, iterate/refine (returning to the playground as needed).

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

A. An Azure Machine Learning workspace client
B. An OpenAI-compatible client object for submitting prompts to models
C. A Foundry IQ knowledge connection
D. A vector store client

**Answer:** B — The module states: "To chat with a model in your Foundry project, you need an OpenAI-compatible client object. You can use the get_openai_client() method of the project client to get one."

**Q6.** Which authentication method does Microsoft recommend for PRODUCTION applications connecting to Foundry/Azure OpenAI endpoints?

A. API key stored in source code
B. Anonymous access
C. Microsoft Entra ID authentication
D. Shared access signature (SAS) tokens

**Answer:** C — "In general, production applications should use Microsoft Entra ID authentication, which requires the application to be running in the context of a specific identity." The module also cautions that API keys should be used carefully and stored in Key Vault, never hardcoded — implying they are not the production-recommended default.

**Q7.** Which class provides Foundry-native operations that have NO OpenAI equivalent, such as retrieving resource connections, accessing project configuration, enabling tracing, and managing datasets/indexes?

A. OpenAI
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

A. True — mixing SDKs is unsupported
B. False — both SDKs work with your Foundry project endpoint and can be combined in the same application
C. True, but only if using the Responses API
D. False, but only for non-production applications

**Answer:** B — The module explicitly states: "You can also use both SDKs together in the same application—the Foundry SDK for project features and the OpenAI SDK for model inference."

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
