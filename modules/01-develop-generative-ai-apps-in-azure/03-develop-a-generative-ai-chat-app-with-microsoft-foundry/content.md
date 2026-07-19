# Develop a generative AI chat app with Microsoft Foundry

Source: https://learn.microsoft.com/en-us/training/modules/foundry-sdk/

## Learning objectives

After completing this module, you'll be able to:

- Describe the process for creating a generative AI chat application with Microsoft Foundry.
- Use the Chat playground to explore models and generate code samples.
- Choose an endpoint, authentication method, and client SDK for your app development.
- Use the Responses API to generate AI responses in applications.
- Use the ChatCompletions API to generate AI responses in applications.

Module info: Beginner level, 8 units, tagged AI Engineer / Developer / Microsoft Foundry. Prerequisites: familiarity with Azure services/portal, generative AI concepts/use cases, and experience with Python or another language.

Caution (from module): Some Microsoft Foundry features are currently in preview and subject to change.

## Exam relevance

- **Build generative applications by using Foundry** → "Integrate generative workflows into applications by using Foundry SDKs and connectors" and "Configure an application to connect to a Foundry project" — the entire module (endpoint/SDK selection, AIProjectClient, get_openai_client()).
- **Build generative applications by using Foundry** → "Deploy and consume LLMs, small models, code models, and multimodal models" — Foundry direct models via Responses API.
- **Plan and manage an Azure AI solution** → "Configure security, including managed identity, private networking, keyless credentials, and role policies" — Microsoft Entra ID / DefaultAzureCredential authentication guidance.
- **Optimize and operationalize generative AI systems** → "Tune generation behavior, such as prompt engineering and adjusting model parameters" — temperature, max_output_tokens, top_p; streaming and async patterns.

## Introduction

Developers building AI solutions with Microsoft Foundry combine multiple services and frameworks. This module covers choosing the appropriate endpoint, SDK, authentication, and chat API options for a generative AI chat application.

## Explore with the model playground

The **Model playground** in the Foundry portal (left navigation → **Model playground**) is a no-code interactive environment for testing models before writing code. It lets you:
- Send prompts to deployed models and see responses in real time.
- Adjust settings like temperature and max tokens.
- Add system messages to customize model behavior.
- Experiment with different models/configurations.

### Generating code samples
The **Code** button in the chat pane generates code samples to reproduce the chat session in your app, with choices for:
- **API** — Responses API or another API like ChatCompletions.
- **Language** — your preferred programming language.
- **SDK** — which SDK to view a sample for.

Samples are pre-populated with your project endpoint, model deployment name, and current settings — copy directly into your dev environment.

### From playground to code (workflow)
1. **Explore in the playground** — test prompts, adjust settings.
2. **Generate code samples** — use the **Code** tab for SDK samples.
3. **Develop your application** — customize the generated code.
4. **Iterate and refine** — return to playground, then update code.

## Choose an endpoint and SDK

Key considerations for app development:

- **Endpoints**: every Foundry project provides two endpoints for client applications: the **Project endpoint** and the **Azure OpenAI endpoint**.
- **Client SDK**: depending on endpoint, use the **Microsoft Foundry SDK** or the **OpenAI SDK**. Both support an OpenAI-API-compatible client object for submitting prompts, but differ in available functionality.
- **Authentication**: production apps should use **Microsoft Entra ID** authentication (identity-based); some scenarios also support **key-based** or **token-based** authentication.
- **Chat API**: the OpenAI client API supports two chat APIs — **ChatCompletions** (well-established, broadly compatible) and **Responses** (recommended for most new development).

### Using the Foundry SDK with the project endpoint

The Microsoft Foundry SDK gives programmatic access to project resources via REST API and language-specific client libraries:
- **Azure AI Projects for Python** (PyPI)
- **Azure AI Projects for .NET** (NuGet)
- **Azure AI Projects for JavaScript** (npm)

Each SDK is developed/maintained independently — functionality may be at different implementation stages across languages.

**Install:**
```bash
pip install azure-ai-projects azure-identity openai
```
Note: the chat client functionality in the Foundry SDK derives from the OpenAI SDK, so the `openai` package must also be installed/imported.

**Project endpoint format** (found on the project's Overview page at https://ai.azure.com):
```
https://{resource-name}.services.ai.azure.com/api/projects/<project-name>
```

**Create an AIProjectClient:**
```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)
```
Requires the `azure-identity` package for `DefaultAzureCredential`. The code must run in an authenticated Azure session (e.g., `az login` via Azure CLI beforehand).

The **AIProjectClient** provides access to Foundry-native operations with no OpenAI equivalent:
- Retrieve resource connections
- Access project configuration
- Enable tracing
- Manage datasets and indexes

**Get an OpenAI-compatible chat client from the project client:**
```python
openai_client = project_client.get_openai_client(api_version="2024-10-21")
```

### Using the OpenAI SDK with the Azure OpenAI endpoint

The OpenAI SDK is the official client library for the OpenAI API — handles HTTP requests, auth, retries, response parsing. Works uniformly with OpenAI-hosted models, Azure OpenAI deployments, and Foundry models.

**Install:**
```bash
pip install openai azure-identity
```
(`azure-identity` needed only for token-based Microsoft Entra ID auth.)

**Azure OpenAI endpoint format** (from project Overview page):
```
https://{resource-name}.openai.azure.com/openai/v1
```

**Connect with Entra ID (recommended):**
```python
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(  
  base_url = "https://{resource-name}.openai.azure.com/openai/v1/",  
  api_key=token_provider,
)
```

**Connect with API key:**
```python
import os
from openai import OpenAI

openai_client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url="https://{resource-name}.openai.azure.com/openai/v1/"
)
```
Caution: store API keys securely (e.g., Azure Key Vault) — never hardcode in source.

**Connect via environment variables** (`OPENAI_BASE_URL`, `OPENAI_API_KEY` — picked up automatically):
```python
from openai import OpenAI
openai_client = OpenAI()  # Uses environment variables
```

The **OpenAI** client handles model inference operations: generating responses (Responses API), chat completions, image generation, and accessing **Foundry direct models** (non-Azure OpenAI models).

**AzureOpenAI client (alternative)**: Generally prefer the plain `OpenAI` client for the Azure OpenAI v1 endpoint, but use `AzureOpenAI` when you need a *specific* Azure OpenAI API version. Requires specifying `azure_endpoint` and `api_version`:
```python
import os
from openai import AzureOpenAI

openai_client = AzureOpenAI(
    azure_endpoint = "https://{resource-name}.openai.azure.com"
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2024-10-21",
)
```

### Choosing between the Foundry SDK and OpenAI SDK

**Use the Foundry SDK when the app needs Foundry-specific capabilities:**
- Foundry Agent Service (building/managing AI agents)
- Tool invocation and approval workflows
- Cloud evaluations for testing/validating AI responses
- Tracing and observability
- Foundry direct models (non-Azure OpenAI models from the catalog)
- Project metadata, connections, and governance features

Microsoft recommends the Foundry SDK for apps with agents, evaluations, or Foundry-specific features.

**Use the OpenAI SDK when maximum OpenAI-API compatibility matters:**
- Full OpenAI API compatibility for existing code/tooling
- Portability between OpenAI and Azure OpenAI deployments
- Chat Completions, Responses, and Images APIs
- Minimal dependency on Foundry-specific concepts

The OpenAI SDK is ideal for model-inference-only workloads wanting existing OpenAI code with minimal changes — but it does NOT provide Foundry-specific features like agents or evaluations.

**Both SDKs work with your Foundry project endpoint and CAN be combined in the same application** — Foundry SDK for project features (agents, evaluations, tracing, connections via `AIProjectClient`), OpenAI SDK for model inference.

## Generate responses with the Responses API

The OpenAI **Responses** API unifies capabilities previously split across two APIs: **ChatCompletions** and **Assistants**. It provides **stateful, multi-turn** response generation — ideal for conversational AI. Accessible through an OpenAI-compatible client via either the Foundry SDK or OpenAI SDK.

### Advantages of the Responses API
- **Stateful conversations** — maintains context across turns.
- **Unified experience** — combines chat completions + Assistants API patterns.
- **Foundry direct models** — works with models hosted directly in Foundry (not just Azure OpenAI models).
- **Simple integration** — via the OpenAI-compatible client.

Note: The Responses API is **the recommended approach** for generating AI responses in Foundry apps; it **replaces the older ChatCompletions API for most scenarios**.

### Simple response
```python
response = openai_client.responses.create(
    model="gpt-4.1",  # Your model deployment name
    input="What is Microsoft Foundry?"
)
print(response.output_text)
```
`input` accepts a text string prompt.

### Response object properties
- `output_text` — generated text
- `id` — unique identifier
- `status` — e.g., "completed"
- `usage` — token usage (input, output, total tokens)
- `model` — model used

```python
response = openai_client.responses.create(model="gpt-4.1", input="Explain machine learning in simple terms.")
print(f"Response: {response.output_text}")
print(f"Response ID: {response.id}")
print(f"Tokens used: {response.usage.total_tokens}")
print(f"Status: {response.status}")
```

### Instructions (system prompt)
```python
response = client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Explain neural networks."
)
```

### Controlling generation
```python
response = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Write a creative story about AI.",
    temperature=0.8,  # Higher temperature for more creativity
    max_output_tokens=200  # Limit response length
)
```
- **temperature**: controls randomness, range **0.0–2.0**. Higher = more creative/varied.
- **max_output_tokens**: max tokens in the response.
- **top_p**: alternative to temperature for controlling randomness.

### Foundry direct models
When connected to a **project** endpoint (Foundry SDK or AzureOpenAI client), Responses API works with both Azure OpenAI models AND **Foundry direct models** (e.g., Microsoft Phi, DeepSeek):
```python
response = openai_client.responses.create(
    model="microsoft-phi-4",  # Example Foundry direct model
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What are the benefits of small language models?"
)
```

### Multi-turn conversations via previous_response_id
```python
response1 = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="What is machine learning?"
)
response2 = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="Can you give me an example?",
    previous_response_id=response1.id
)
```
Interactive loop pattern tracks `last_response_id` and passes it as `previous_response_id` on each new call. Each turn's payload includes the *instructions* system message, the current *input*, and the *previous* response — grounding the new turn in prior context.

### Alternative: manual conversation chaining
Build message history yourself for finer control:
```python
conversation_history = [
    {"type": "message", "role": "user", "content": "What is machine learning?"}
]
response1 = openai_client.responses.create(model="gpt-4.1", input=conversation_history)
conversation_history += response1.output
conversation_history.append({"type": "message", "role": "user", "content": "Can you give me an example?"})
response2 = openai_client.responses.create(model="gpt-4.1", input=conversation_history)
```
Useful when you need to: customize which messages are included, implement conversation pruning for token limits, or store/restore history from a database.

### Retrieving previous responses
```python
response_id = "resp_67cb61fa3a448190bcf2c42d96f0d1a8"  # Example ID
previous_response = openai_client.responses.retrieve(response_id)
print(f"Previous response: {previous_response.output_text}")
```

### Context window considerations
`previous_response_id` links responses to maintain context, but conversation history increases token usage. Per-request active context window can include: system instructions, current prompt, conversation history, **tool schemas** (functions, OpenAPI specs, MCP tools), **tool outputs** (search results, code interpreter output, files), and **retrieved memory/documents** (memory stores, RAG, file search). All of this is concatenated, tokenized, and sent together on every request — the SDK manages state but does NOT make token usage cheaper.

### Streaming responses
```python
stream = openai_client.responses.create(
    model="gpt-4.1",
    input="Write a short story about a robot learning to paint.",
    stream=True
)
for event in stream:
    print(event, end="", flush=True)
```
To capture the response ID at stream completion, check event types:
```python
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="")
    elif event.type == "response.completed":
        response_id = event.response.id
```

### Async usage
Use `AsyncOpenAI` instead of `OpenAI`, with `await`:
```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url="https://<resource-name>.openai.azure.com/openai/v1/",
    api_key=token_provider,
)

async def main():
    response = await client.responses.create(
        model="gpt-4.1",
        input="Explain quantum computing briefly."
    )
    print(response.output_text)

asyncio.run(main())
```
Async streaming uses `async for`:
```python
async def stream_response():
    stream = await client.responses.create(
        model="gpt-4.1", input="Write a haiku about coding.", stream=True
    )
    async for event in stream:
        print(event, end="", flush=True)
```
Ideal for long-running requests or handling multiple concurrent requests without blocking.

## Generate responses with the ChatCompletions API

The OpenAI **ChatCompletions** API is well-established/commonly used across many models and platforms. While **Responses is recommended for new projects**, ChatCompletions remains useful for code maintenance or cross-platform compatibility.

### Submitting a prompt
Uses a collection of **message** objects in JSON with `role`/`content`:
```python
completion = openai_client.chat.completions.create(
    model="gpt-4o",  # Your model deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "When was Microsoft founded?"}
    ]
)
print(completion.choices[0].message.content)
```
Response text is accessed via `completion.choices[0].message.content` — NOT `response.output_text` as in the Responses API (exam-relevant distinction).

### Retaining conversational context
**Key difference from Responses API**: ChatCompletions has **no stateful tracking feature** — you must manually track and resend the full message history (`role: system/user/assistant`) on every call.

```python
conversation_messages=[
    {"role": "system", "content": "You are a helpful AI assistant that answers questions and provides information."}
]
conversation_messages.append({"role": "user", "content": "When was Microsoft founded?"})
completion = openai_client.chat.completions.create(model="gpt-4o", messages=conversation_messages)
assistant_message = completion.choices[0].message.content
conversation_messages.append({"role": "assistant", "content": assistant_message})
conversation_messages.append({"role": "user", "content": "Who founded it?"})
completion = openai_client.chat.completions.create(model="gpt-4o", messages=conversation_messages)
```
Interactive loop pattern: append each user input, call the API, append the assistant response, repeat. The entire conversation history is resubmitted every turn.

## Exercise — Create a generative AI chat app

10-minute hands-on lab (requires Azure subscription with admin access): deploy a generative model in Microsoft Foundry and build an application that chats with it using the SDKs covered in this module.

## Comparison summary (exam-critical distinctions)

| Aspect | Responses API | ChatCompletions API |
|---|---|---|
| State management | Stateful — built-in via `previous_response_id` | Stateless — manual history tracking required |
| Output access | `response.output_text` | `completion.choices[0].message.content` |
| Recommended for | New development | Legacy/cross-platform compatibility |
| Works with Foundry direct models | Yes | Yes (via OpenAI-compatible client) |
| Origin | Unifies ChatCompletions + Assistants API | Long-established, widely compatible |

| Aspect | Foundry SDK (AIProjectClient) | OpenAI SDK |
|---|---|---|
| Endpoint | Project endpoint | Azure OpenAI endpoint (or project endpoint via `get_openai_client()`) |
| Best for | Agents, evaluations, tracing, connections, governance, Foundry direct models | Model inference only, max OpenAI compatibility, portability |
| Chat client | Obtained via `project_client.get_openai_client()` | `OpenAI` / `AzureOpenAI` client classes |
