# Develop a vision-enabled generative AI application

Source: https://learn.microsoft.com/en-us/training/modules/develop-generative-ai-vision-apps/

(Note: this module's on-page title is "Develop a vision-enabled generative AI application"; it is filed under Learning Path 4 "Extract insights from visual data on Azure" as Module 1, sometimes referenced by the shorter name "Develop generative AI vision apps". Level: Intermediate. Role: AI Engineer. Product: Microsoft Foundry. 6 units.)

## Learning objectives

After completing this module, you'll be able to:

- Deploy a vision-enabled generative AI model in Microsoft Foundry.
- Test an image-based prompt in the chat playground.
- Create a chat app that submits image-based prompts.

**Prerequisites:** Experience with deploying generative AI models in Microsoft Foundry; programming experience.

**Module description:** A picture says a thousand words, and multimodal generative AI models can interpret images to respond to visual prompts. Learn how to build vision-enabled chat apps.

## Exam relevance

Maps primarily to **Implement computer vision solutions (10-15%)** → "Design and implement multimodal understanding workflows":
- Build a solution that analyzes visual context by using multimodal models — this module's core topic (deploying multimodal models, submitting image + text prompts).
- Implement a solution that enables question-answering grounded in visual evidence — the multi-part user message pattern (text + image content items) shown here is exactly this.
- (Adjacent, not directly covered here but relevant context for the exam objective) Configure generation of alt-text/extended image descriptions, single-task vs pro-mode Content Understanding, video analysis, object/region identification — these are covered by *other* modules in this learning path (e.g., Azure AI Content Understanding), not this one. This module is scoped strictly to LLM/chat-based multimodal reasoning (the model "sees and reasons" in one call), which the exam contrasts against Content Understanding's structured-extraction approach.

Also touches **Plan and manage an Azure AI solution (25-30%)** → "Choose an appropriate model for each task, including LLMs, small language models, multimodal models" (model selection: Phi-4-multimodal-instruct vs gpt-4.1 vs gpt-4.1-mini) and "Configure model and agent deployments" (deploying a multimodal model in Foundry).

Also touches **Implement generative AI and agentic solutions (30-35%)** → "Deploy and consume LLMs, small models, code models, and multimodal models" and "Integrate generative workflows into applications by using Foundry SDKs and connectors" (Responses API / ChatCompletions API usage with the OpenAI Python SDK against Azure OpenAI/Foundry endpoints).

## Unit 1: Introduction

Generative AI models enable development of chat-based applications that reason over and respond to input. Input is often a text-based prompt, but increasingly **multimodal models** that respond to visual input are becoming available.

This module discusses vision-enabled generative AI and explores how to use **Microsoft Foundry** to create generative AI solutions that respond to prompts containing a mix of text and image data.

## Unit 2: Use a vision-capable model in the Microsoft Foundry portal

To handle prompts that include images, you need to deploy a **multimodal** generative AI model — a model that supports not only text-based input, but image-based input (and in some cases audio-based input) as well.

**Multimodal models available in Microsoft Foundry include (among others):**
- Microsoft **Phi-4-multimodal-instruct**
- OpenAI **gpt-4.1**
- OpenAI **gpt-4.1-mini**

For the full/current list of available models, see the Microsoft Foundry Models overview article in the Microsoft Foundry documentation (`/en-us/azure/foundry/concepts/foundry-models-overview`).

### Testing multimodal models with image-based prompts

After deploying a multimodal model, you can test it in the **chat playground** in the Microsoft Foundry portal. In the chat playground you can upload an image from a local file and add text to the message to elicit a response from a multimodal model.

## Unit 3: Develop a vision-based chat app

To develop a client app that engages in vision-based chats with a multimodal model, you use the same basic techniques used for text-based chats:
- You require a connection to the **endpoint** where the model is deployed.
- You use that endpoint to submit prompts consisting of **messages** to the model and process the responses.

**Key difference for vision-based chat:** prompts include **multi-part user messages** that contain both a *text* content item and an *image* content item (rather than a single plain-text message).

Two APIs are shown for submitting image-based prompts, corresponding to two different client/model combinations:

### Submit an image-based prompt using the Responses API

To include an image in a prompt using the **Responses API**, you either:
- specify a URL for a web-based image file, or
- load a local image and encode its data in **Base64** format and submit a URL in the format `data:image/jpeg;base64,{image_data}` (replacing "jpeg" with "png" or other formats as appropriate).

Python example (Responses API, model `gpt-4.1`):

```python
# Read the image data from a local file
image_path = Path("dragon-fruit.jpeg")
image_format = "jpeg"
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

data_url = f"data:image/{image_format};base64,{image_data}" # You can also use a web URL

# Send the image data in a prompt to the model
response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "developer", "content": "You are an AI assistant for chefs planning recipes."},
        {"role": "user", "content": [  
            { "type": "input_text", "text": "What desserts could I make with this?"},
            { "type": "input_image", "image_url": data_url}
        ] } 
    ]
)
print(response.output_text)
```

Notes on this pattern:
- The message roles used are `"developer"` (system-style instruction) and `"user"`.
- The user message `content` is a **list/array** of content-item dicts.
- Content item types for the Responses API are **`"input_text"`** (with a `"text"` key) and **`"input_image"`** (with an `"image_url"` key that holds the data URL or web URL directly, i.e. a plain string, not a nested object).
- The response text is read via `response.output_text`.

### Submit an image-based prompt using the ChatCompletions API

When using the Azure OpenAI endpoint to submit prompts to models that **don't support the Responses API**, you use the **ChatCompletions API** instead.

Python example (ChatCompletions API, model `Phi-4-multimodal-instruct`):

```python
# Read the image data from a local file
image_path = Path("orange.jpeg")
image_format = "jpeg"
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

data_url = f"data:image/{image_format};base64,{image_data}" # You can also use a web URL

# Send the image data in a prompt to the model
response = client.chat.completions.create(
    model="Phi-4-multimodal-instruct",
    messages=[
        {"role": "system", "content": "You are an AI assistant for chefs planning recipes."},
        { "role": "user", "content": [  
            { "type": "text", "text": "What can I make with this fruit?"},
            { "type": "image_url", "image_url": {"url": data_url}}
        ] }
    ]
)
print(response.choices[0].message.content)
```

Notes on this pattern:
- The message roles used are `"system"` and `"user"` (standard ChatCompletions roles, unlike the Responses API's `"developer"` role).
- The user message `content` is again a **list of content-item dicts**.
- Content item types for ChatCompletions are **`"text"`** (with a `"text"` key) and **`"image_url"`** (with an `"image_url"` key that holds a **nested object** `{"url": data_url}` — note the structural difference from the Responses API's `input_image`, where `image_url` is a plain string).
- The response text is read via `response.choices[0].message.content` (standard ChatCompletions response shape), as opposed to `response.output_text` for the Responses API.

### Explicit comparison: Responses API vs ChatCompletions API for vision prompts

| Aspect | Responses API | ChatCompletions API |
|---|---|---|
| Used when | Model supports the Responses API (e.g., `gpt-4.1`) | Model does **not** support the Responses API (e.g., `Phi-4-multimodal-instruct`) |
| Method | `client.responses.create(...)` | `client.chat.completions.create(...)` |
| Instruction role | `"developer"` | `"system"` |
| Text content type | `"input_text"` / `"text"` key | `"text"` / `"text"` key |
| Image content type | `"input_image"` / `"image_url"` key holds **string** (data URL) | `"image_url"` / `"image_url"` key holds **object** `{"url": ...}` |
| Output access | `response.output_text` | `response.choices[0].message.content` |
| Image input formats | Web URL, or local file Base64-encoded as `data:image/{format};base64,{data}` | Same: web URL, or local file Base64-encoded as `data:image/{format};base64,{data}` |

## Unit 4: Exercise — Develop a vision-enabled chat app

Hands-on exercise (requires an Azure subscription; free trial includes credits for the first 30 days). The exercise is launched via an external link (go.microsoft.com fwlink) and walks through building a vision-enabled chat app using Microsoft Foundry and the OpenAI APIs described in Unit 3. No additional technical/API detail beyond Unit 3 is given on the module page itself — the actual steps live in the external exercise instructions.

## Unit 5: Module assessment

A 3-question knowledge-check quiz (no new technical content; reproduced here for completeness since it reinforces the module's key exam-relevant facts):

1. "Which kind of model can you use to respond to visual input?" — options: Only OpenAI GPT models / Embedding models / **Multimodal models**.
2. "How can you submit a prompt that asks a model to analyze an image?" — options: Submit one prompt with an image-based message followed by another prompt with a text-based message / **Submit a prompt that contains a multi-part user message, containing both text content and image content** / Submit the image as the system message and the instruction or question as the user message.
3. "How can you include an image in a message?" — options: **As a URL or as binary data** / Only as a URL / Only as binary data.

(Correct answers are the bolded options, inferred from module content in Units 2–3; the source page does not visually mark answers in fetched text but they align directly with what Units 2 and 3 teach.)

## Unit 6: Summary

Vision-enabled models let you create AI solutions that can understand images and respond to related questions or instructions. Beyond just identifying objects in pictures, some models can also use **reasoning** based on what they see — for instance, interpreting a chart or assessing whether an object is damaged.

Further reading pointed to by the module: "Images and vision" in the OpenAI developer guide (`https://developers.openai.com/api/docs/guides/images-vision`) — for more information about analyzing images with the OpenAI Responses API.

## Cross-cutting exam notes (synthesized from this module's content)

- **This module = "LLM does the seeing and reasoning in one call."** A multimodal chat model (Phi-4-multimodal-instruct, gpt-4.1, gpt-4.1-mini) receives a multi-part message containing text + image content items and returns a free-form grounded answer/caption in a single completion. This is distinct from Content Understanding / Document Intelligence-style services (covered elsewhere in this learning path), which perform structured field/entity extraction rather than open-ended visual reasoning.
- **Two ways to supply an image to a multimodal model:** (1) a web URL pointing to the image, or (2) local binary image data Base64-encoded into a `data:image/{format};base64,{data}` URL string. Both APIs (Responses and ChatCompletions) accept either form.
- **Model choice determines which API to use:** models that support the newer Responses API (e.g., gpt-4.1) use `client.responses.create()`; models that don't (e.g., Phi-4-multimodal-instruct) require the ChatCompletions API via `client.chat.completions.create()`. Know this pairing — it is a natural distractor pattern (e.g., exam might ask which API to use with a Phi model).
- **Message shape is the crux of "grounded visual QA":** a user message's `content` becomes a list of typed content items instead of a plain string — mixing a text item and an image item is what lets the model reason over both simultaneously in one request/response turn.
- No explicit mention in this module of image token cost/limits, image resolution constraints, content-safety filtering for images, or accessibility alt-text prompt patterns — those are exam objectives from the same "computer vision" skill area but are evidently covered by other modules in this learning path, not this one. Treat this module strictly as covering: model deployment + testing in chat playground + client-side multi-part prompt code.
