# Generate images with AI

Source: https://learn.microsoft.com/en-us/training/modules/generate-images-azure-openai/

> Note on module naming: the module's URL slug is `generate-images-azure-openai` and it lives under Learning Path 4 ("Extract insights from visual data on Azure"), but Microsoft has since rebranded the page title to **"Generate images with AI"** and reworded the content to be Microsoft Foundry-first (rather than "Azure OpenAI Studio"-first). Both names refer to the same module. Last content update per the page metadata: 2026-05-15 (unit content), module index 2026-03-24.

Module facts: **Intermediate** level, **7 units**, tagged **AI Engineer** / **Developer**, products: **Microsoft Foundry**, **Azure OpenAI Service**.

## Learning objectives

After completing this module, you'll be able to:

- Describe the capabilities of image generation models
- Use the Images playground in Microsoft Foundry portal
- Integrate image generation models into your apps

**Prerequisites:** Familiarity with Microsoft Foundry; programming experience.

## Exam relevance

Maps to `EXAM_SKILLS.md` — **Implement computer vision solutions (10-15%)**:

- *Design and implement image- and video-generation solutions*
  - "implement a solution that generates images from text prompts and reference media" → Unit 3 (Images playground supports a reference image, subject to model support) and Unit 4 (`client.images.generate()` code sample).
  - "select and apply appropriate generation and editing controls provided by the platform" → Unit 3 (resolution/size control in the playground), Unit 4 (`size`, `n` parameters in the SDK call), Unit 2 (Model catalog filter by inference task = *text to image*).
  - **GAP:** "configure image-editing workflows, including inpainting, mask-based edits, and prompt-driven modifications" — **this module, as currently published, does not cover inpainting, masks, or an explicit image-edit API/endpoint.** It only demonstrates the *generate* call. See note at the end of this file.
  - **GAP:** "implement a solution that generates videos..." / "implement workflows to edit generated videos" — not covered by this module (video generation is out of scope here; likely covered elsewhere in the learning path, e.g., Sora-related modules).
- *Implement responsible AI for multimodal content* (filters for unsafe content, prompt-injection via embedded text, watermarks/policy rules) — **GAP: not mentioned anywhere in this module's unit content.** No discussion of content filtering, moderation, or responsible-AI controls for generated images appears in units 1–7.

Also touches `EXAM_SKILLS.md` — **Plan and manage an Azure AI solution (25-30%)**:

- "Choose an appropriate model for each task... multimodal models" → Unit 2's guidance to use the **Model catalog** and filter by inference task ("text to image") to find image-generation models.
- "Deploy and consume LLMs, small models, code models, and multimodal models" → Unit 5 exercise deploys an image-generation model in a Microsoft Foundry project and consumes it via SDK.

**Generation vs. understanding distinction** (per the task's cross-module note): this module is squarely on the **text → image (generation)** side of computer vision — it never touches image *understanding* (image → text captioning, VQA, OCR, Content Understanding), which is the subject of the sibling module(s) in this learning path. The generation direction here uses the OpenAI-style `images.generate` API surface; there is no `images.edit` or `images.createEdit`-style call shown or described in this module's content, unlike the general Azure OpenAI/OpenAI product documentation which does expose a separate image-edit endpoint for mask-based inpainting. Exam-takers should be aware the broader product does support editing, but **this specific training module doesn't teach it** — treat that as a documented content gap, not a statement that Azure OpenAI/Foundry lacks the capability.

---

## Introduction

With Microsoft Foundry, you can use language models to generate content based on natural language prompts. Often the generated content is natural-language text, but increasingly, models can generate other kinds of content.

- Example: the OpenAI **`gpt-image-1`** model can create original graphical content based on a description of a desired image.
- Applications called out: illustrations or photorealistic images for articles/marketing collateral, generation of unique product or company logos, or any scenario where a desired image can be described.

The module teaches how to develop an application that uses generative AI to generate original images. (Content is offered in both video and text form; the text form is stated to contain more detail than the video.)

## What are image-generation models?

**Microsoft Foundry supports multiple models capable of generating images**, including (but not limited to):

- The OpenAI **`gpt-image-1`** series of models.
- The Black Forest Labs **`FLUX`** series of models.

> Tip called out on the page: use the **Model catalog** (`https://ai.azure.com/catalog/models`) to see the full set of models available in Microsoft Foundry. In the Foundry portal, you can **filter by inference task** to find **text to image** models. (This is the exact filter terminology used — relevant for exam questions phrased as "which inference task should you filter by?": answer is **Text to image**, not "Image to text" or "Embeddings".)

**Definition given:** Image generation models are generative AI models that can create graphical data from natural-language input — you provide the model with a description and it generates an appropriate image.

Example prompt given: *"A robot eating spaghetti"* → results in a generated illustration of a robot eating spaghetti.

**Key conceptual point (exam-relevant):** the images generated are **original** — they are **not retrieved from a curated image catalog**. The model is not a search system for *finding* appropriate images; it is an AI model that **generates new images** based on the data it was trained on. (Good distractor material: exam may ask you to distinguish "image generation" from "image search/retrieval".)

## Explore image-generation models in Microsoft Foundry portal

To experiment with image generation models:

1. Create a **Microsoft Foundry project**.
2. Use the **model playground** ("Images playground") in the **Microsoft Foundry portal** to submit prompts and view the resulting generated images.

Capabilities of the Images playground called out explicitly (subject to model support):

- You can specify the **resolution (size)** of the generated images.
- You can **include a reference image** for the model to base its output on.

(No further UI-configuration steps, parameter names, or numeric size limits are given in this unit — it stays at a conceptual/portal-tour level. The screenshot referenced is captioned "Images playground in Azure AI Studio", showing the module's content predates full renaming to "Foundry" in places.)

## Create a client application that uses an image generation model

You can use a **language-specific SDK** to build client apps that call image-generation models. Named examples:

- The **OpenAI Python SDK**
- The **Azure OpenAI .NET SDK**

The unit demonstrates the **OpenAI *Images* API** via the Python SDK, calling `client.images.generate(...)`. Exact code sample from the module:

```python
# Generate an image
img_results = client.images.generate(
    model="FLUX.1-Kontext-pro",
    prompt="A robot eating a cheeseburger.",
    n=1,
    size="1024x1024",
)

# Save the generated image
image_data = base64.b64decode(img_results.data[0].b64_json)
with open("image.png", "wb") as image_file:
    image_file.write(image_data)
```

Notes on this exact snippet (parameter-level detail, since exam questions hinge on precise names):

- Method: **`client.images.generate()`** — this is the *generation-only* call; the module shows no `images.edit`/`images.createEdit`/mask parameter anywhere.
- `model="FLUX.1-Kontext-pro"` — the **deployment/model name** passed as a string (a Black Forest Labs FLUX model deployed in Foundry, not `gpt-image-1` in this particular sample — showing the API surface is model-agnostic across the supported image models).
- `prompt="A robot eating a cheeseburger."` — the natural-language description, a required string parameter.
- `n=1` — number of images to generate (integer).
- `size="1024x1024"` — resolution string, `"<width>x<height>"` format.
- The result (`img_results`) contains a `.data` list; each element has a **`.b64_json`** attribute — a base64-encoded string of the generated image, which the sample decodes with `base64.b64decode()` and writes to disk as `image.png`.
- The unit states the API call's result is conceptually "a binary stream containing the requested image."

No `quality`, `style`, or `response_format` parameters are shown or discussed in this unit — only `model`, `prompt`, `n`, and `size` appear in the module's own code sample. (The broader Azure OpenAI/OpenAI Images API does support additional parameters like `quality`, `style`, and `response_format`, but they are **not part of this module's documented content** — treat any exam answer requiring those as general product knowledge, not something taught here.)

## Exercise - Generate images with AI

Hands-on exercise (external, launched via a link to a separate lab environment: `https://go.microsoft.com/fwlink/?linkid=2356876`). Stated flow:

1. Provision a **Microsoft Foundry project**.
2. **Deploy an image generation model**.
3. Explore image generation in the **Microsoft Foundry portal** (Images playground).
4. Use **Python** to consume the image generation model from a custom application.

Reminder given: after completing the exercise, delete the Azure resources you created.

(No further technical detail is available for this unit beyond the above — it's a pointer to an external interactive lab, not inline content.)

## Module assessment

The official knowledge-check unit presents (at minimum) these two questions, captured verbatim as they appear on the page (answer options shown are exactly as listed; the page did not expose which option is marked correct in the fetched content):

1. "You want to find a model in Microsoft Foundry to generate images. Which inference task should you filter by?"
   Options: **Text to image** / Image to text / Embeddings
   (Correct answer per Unit 2's explicit guidance: **Text to image**.)

2. "Which OpenAI API can you use with image-generation models?"
   Options: Video / **Image** / Graphics
   (Correct answer per Unit 4's explicit demonstration of the OpenAI **Images** API: **Image**.)

## Summary

This module described image generation models, and how you can use them in Microsoft Foundry to generate images based on natural language prompts. You can explore image generation models using the **Images** playground in Microsoft Foundry portal, and you can use **REST APIs or SDKs** to build applications that generate new images.

(The summary is the only place the module mentions "REST APIs" by name for this capability — no specific REST endpoint path, HTTP verb, header, or JSON request/response schema is ever shown anywhere in the module; the only concrete code shown is the Python SDK `images.generate()` call in Unit 4.)

---

## Content gaps vs. the expected exam-skill mapping

The task brief for this module anticipated coverage of: exact model/deployment names (DALL-E 3 vs. GPT-Image), REST API endpoint paths, request body params (`prompt`, `size`, `quality`, `style`, `n`, `response_format`), image editing/inpainting workflows (mask-based edits), which model versions support edits vs. generation-only, and content filtering on generated images. After fetching all 7 units verbatim, **the currently published module content does not include most of this**:

- No mention of **DALL-E 3** anywhere (the module has been updated to reference **`gpt-image-1`** and **FLUX** models instead — useful to note as this module clearly superseded an older DALL-E-3-centric version).
- No REST endpoint paths (e.g., no `POST /openai/deployments/{deployment-id}/images/generations` shown), no HTTP headers, no JSON request/response body shown — only a Python SDK call.
- No `quality`, `style`, or `response_format` parameters mentioned.
- **No image-editing/inpainting/mask-based-edit content at all** — no `images.edit` call, no mask parameter, no discussion of which models support edits vs. generation-only.
- **No content-filtering / responsible-AI content for generated images** in this module (contrast with the exam skill "Implement filters to classify unsafe or disallowed visual content").

These gaps are called out explicitly in `## Exam relevance` above and should be flagged to the orchestrator as things likely covered in a *different* module (e.g., a Responsible AI module, or the general Azure OpenAI REST API reference docs) rather than here.
