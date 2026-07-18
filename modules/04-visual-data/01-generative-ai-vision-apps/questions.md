# Practice questions — Develop a vision-enabled generative AI application

## Unit 1: Introduction

**Q1.** What type of generative AI model must you deploy to build an app that can respond to prompts containing both text and images?

A. An embedding model
B. A multimodal model
C. A fine-tuned text-completion model
D. A speech-to-text model

**Answer:** B — Multimodal models support image-based (and sometimes audio-based) input in addition to text, which is required to respond to visual prompts.

---

**Q2.** According to the module, generative AI chat applications traditionally reason over which type of input, with multimodal support being an emerging extension?

A. Audio-only input
B. Text-based prompts
C. Video streams only
D. Structured JSON only

**Answer:** B — The module states that generative AI input "often takes the form of a text-based prompt," with multimodal (visual) input becoming increasingly available as an extension.

---

**Q3.** Which Azure product does this module use to create and test generative AI solutions that respond to combined text-and-image prompts?

A. Azure Cognitive Search
B. Microsoft Foundry
C. Azure Data Factory
D. Azure Logic Apps

**Answer:** B — The module explicitly uses Microsoft Foundry to deploy and test vision-enabled generative AI models.

---

## Unit 2: Use a vision-capable model in the Microsoft Foundry portal

**Q4.** Which of the following are multimodal models explicitly listed in this module as available in Microsoft Foundry? (Choose two.)

A. Phi-4-multimodal-instruct
B. text-embedding-ada-002
C. gpt-4.1
D. gpt-35-turbo-instruct

**Answer:** A, C — The module lists Microsoft Phi-4-multimodal-instruct, OpenAI gpt-4.1, and OpenAI gpt-4.1-mini as example multimodal models available in Microsoft Foundry. text-embedding-ada-002 is an embedding model (not multimodal/generative chat), and gpt-35-turbo-instruct is a text-only completion model.

---

**Q5.** Where in the Microsoft Foundry portal can you interactively test an image-based prompt against a deployed multimodal model before writing any client code?

A. The Deployments quota blade
B. The chat playground
C. The Azure Monitor workbook
D. The model catalog filter panel

**Answer:** B — After deploying a multimodal model, you can test it in the chat playground in the Microsoft Foundry portal, uploading a local image and adding text to the message.

---

**Q6.** A developer needs to confirm the complete, current list of multimodal models supported in Microsoft Foundry beyond the three named in this module. Which resource does the module point to?

A. The Azure Pricing Calculator
B. The Microsoft Foundry Models overview article
C. The OpenAI API changelog
D. The Azure Well-Architected Framework

**Answer:** B — The module's tip references the "Microsoft Foundry Models overview" documentation article for the full/current list of available models.

---

**Q7.** True or false framed as MCQ: In the Microsoft Foundry chat playground, which action lets you elicit a vision-grounded response from a deployed multimodal model?

A. Upload an image from a local file and add accompanying text to the message
B. Submit only an image with no text
C. Submit only text describing the image verbally, without uploading a file
D. Configure a separate vision endpoint outside the playground

**Answer:** A — The chat playground allows uploading a local image file plus adding text to the message to elicit a response from the multimodal model.

---

## Unit 3: Develop a vision-based chat app

**Q8.** What is the key structural difference between a vision-based chat prompt and a standard text-only chat prompt when calling a multimodal model's API?

A. Vision-based prompts require a separate authentication token
B. Vision-based prompts use multi-part user messages containing both a text content item and an image content item
C. Vision-based prompts must omit the system/developer message
D. Vision-based prompts can only be sent as HTTP GET requests

**Answer:** B — The module states the key difference is that vision-based chat prompts include multi-part user messages containing both a text content item and an image content item.

---

**Q9.** When encoding a local image file for submission in a prompt, which format is used to construct the image URL string?

A. `file://{image_path}`
B. `data:image/{format};base64,{image_data}`
C. `image-blob:{image_data}`
D. `azureblob://{container}/{image_data}`

**Answer:** B — The module shows Base64-encoding the image bytes and constructing a data URL in the format `data:image/{format};base64,{image_data}` (e.g., substituting "jpeg" or "png").

---

**Q10.** You are calling the OpenAI **Responses API** (`client.responses.create`) with a model that supports it (e.g., `gpt-4.1`) to ask a question about an uploaded image. Which content item `"type"` values should appear in the user message's content list? (Choose two.)

A. `input_text`
B. `input_image`
C. `text`
D. `image_url`

**Answer:** A, B — In the Responses API example, the user message content list uses `{"type": "input_text", "text": ...}` and `{"type": "input_image", "image_url": ...}`. `text` and `image_url` as type values belong to the ChatCompletions API pattern instead.

---

**Q11.** In the module's ChatCompletions API example for `Phi-4-multimodal-instruct`, how is the image URL represented within the content item?

A. As a plain string value directly under the key `image_url`
B. As a nested object `{"url": data_url}` under the key `image_url`
C. As a separate top-level parameter called `image`
D. As a file attachment parameter called `attachments`

**Answer:** B — The ChatCompletions example uses `{ "type": "image_url", "image_url": {"url": data_url}}`, i.e., a nested object with a `url` key, unlike the Responses API where `input_image`'s `image_url` value is the data URL string directly.

---

**Q12.** A developer is submitting an image-based prompt to a model that does NOT support the Responses API. Which API and role name combination should they use, based on the module's example?

A. `client.responses.create()` with role `"developer"`
B. `client.chat.completions.create()` with role `"system"`
C. `client.chat.completions.create()` with role `"developer"`
D. `client.responses.create()` with role `"system"`

**Answer:** B — For models that don't support the Responses API (e.g., Phi-4-multimodal-instruct), the module uses `client.chat.completions.create()` with a `"system"` role message, contrasted with the Responses API's `"developer"` role.

---

**Q13.** How does a developer read the model's textual answer from each of the two APIs shown in the module? (Choose two.)

A. `response.output_text` for the Responses API
B. `response.choices[0].message.content` for the ChatCompletions API
C. `response.result.text` for the Responses API
D. `response.data[0].content` for the ChatCompletions API

**Answer:** A, B — The Responses API example prints `response.output_text`; the ChatCompletions example prints `response.choices[0].message.content`.

---

**Q14.** Besides a Base64-encoded local file, what other way can an image be supplied in an image-based prompt, per the module?

A. As an Azure Blob Storage SAS token only
B. As a web URL pointing to the image file
C. As a Base64 string embedded directly in the system message
D. Images cannot be supplied any other way

**Answer:** B — The module explicitly states you can specify a URL for a web-based image file as an alternative to Base64-encoding a local file.

---

## Unit 4: Exercise — Develop a vision-enabled chat app

**Q15.** What is required to complete the hands-on exercise in this module?

A. A local GPU-enabled workstation
B. An Azure subscription
C. A Microsoft 365 E5 license
D. A GitHub Copilot subscription

**Answer:** B — The exercise instructions state that an Azure subscription is required to complete the exercise (a free trial with 30-day credits is offered if the learner doesn't already have one).

---

**Q16.** The hands-on exercise in Unit 4 primarily gives practical experience with which task?

A. Fine-tuning an embedding model on custom image data
B. Building a vision-enabled chat app using Microsoft Foundry and OpenAI-style APIs
C. Configuring Azure Content Understanding pro-mode pipelines
D. Setting up network isolation for a Foundry hub

**Answer:** B — The exercise is titled "Develop a vision-enabled chat app" and applies the concepts from Units 2–3 (deploying a multimodal model, submitting multi-part image+text prompts).

---

## Unit 5: Module assessment

**Q17.** Per the module's own knowledge check, which kind of model can you use to respond to visual input?

A. Only OpenAI GPT models
B. Embedding models
C. Multimodal models
D. Speech recognition models

**Answer:** C — Multimodal models are the correct answer given in the module assessment; note that "only OpenAI GPT models" is a plausible-looking distractor since the module itself also lists a non-OpenAI multimodal model (Phi-4-multimodal-instruct).

---

**Q18.** Per the module's knowledge check, how can you submit a prompt that asks a model to analyze an image?

A. Submit one prompt with an image-based message, then a separate prompt with a text-based message
B. Submit a prompt containing a multi-part user message with both text content and image content
C. Submit the image as the system message and the question as the user message
D. Submit the image as an HTTP header on the request

**Answer:** B — This matches the module's core teaching in Unit 3: a single multi-part user message combining text and image content items, not separate prompts or misplaced roles.

---

**Q19.** Per the module's knowledge check, how can you include an image in a message?

A. Only as a URL
B. Only as binary data
C. As a URL or as binary (Base64-encoded) data
D. Only as a file path string

**Answer:** C — The module supports both a web URL and Base64-encoded local binary data (wrapped in a `data:image/{format};base64,...` URL).

---

## Unit 6: Summary

**Q20.** Beyond simply identifying objects in an image, what additional capability does the module attribute to some vision-enabled multimodal models?

A. Automatically retraining themselves on new images
B. Reasoning based on what they see, such as interpreting a chart or assessing whether an object is damaged
C. Generating new images from the input image
D. Automatically translating the image's embedded text into other languages

**Answer:** B — The summary states that some models can use reasoning based on what they see, giving examples of interpreting a chart or assessing whether an object is damaged — this goes beyond basic object identification.

---

**Q21.** Where does the module direct learners for further information about analyzing images with the OpenAI Responses API?

A. The Azure Well-Architected Framework documentation
B. The "Images and vision" guide in the OpenAI developer documentation
C. The Microsoft Foundry pricing page
D. The Azure AI Content Understanding overview

**Answer:** B — The Summary unit links to "Images and vision" in the OpenAI developer guide for more information on analyzing images with the Responses API.

---

## Cross-cutting / synthesis (general Azure knowledge flagged where used)

**Q22.** *(General Azure/AI-103 knowledge beyond this module's page content, flagged as such)* A team wants an application that extracts structured invoice fields (vendor name, totals, line items) into a fixed JSON schema, rather than answering open-ended questions about an image. Based on the distinction this module draws between multimodal LLM chat and structured extraction approaches, which approach is more appropriate?

A. A multimodal chat model called via the Responses/ChatCompletions API with a free-form user question
B. A structured-extraction service such as Azure AI Content Understanding, designed for field/entity extraction
C. An embedding model used purely for similarity search
D. A speech-to-text model

**Answer:** B — This module positions multimodal chat models as suited to open-ended, grounded visual reasoning/QA (single call, free-form answer), whereas fixed-schema structured extraction is the domain of Content Understanding-style services covered elsewhere in the learning path. This question draws the contrast explicitly called out in this module's "Cross-cutting exam notes."

---

**Q23.** A developer building a vision-enabled chat app needs to decide between the Responses API and the ChatCompletions API for a given deployed model. What should primarily drive this decision, per the module?

A. The size of the image file being submitted
B. Whether the specific deployed model supports the Responses API
C. The Azure region where the model is hosted
D. Whether the prompt is in English or another language

**Answer:** B — The module states you use the ChatCompletions API specifically "when using the Azure OpenAI endpoint to submit prompts to models that don't support the Responses API" — model capability, not file size/region/language, is the deciding factor.
