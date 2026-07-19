# Practice questions — Generate images with AI

Grounded in `content.md` (module: *Generate images with AI*, slug `generate-images-azure-openai`). Where a question draws on general Azure knowledge beyond the module content, it is flagged inline with **[general knowledge]**.

## Learning objectives / Exam relevance

**Q21.** Which of the following is one of the three stated learning objectives for this module?

A. Fine-tune `gpt-image-1` on a proprietary logo dataset
B. Use the Images playground in Microsoft Foundry portal
C. Configure mask-based inpainting workflows
D. Deploy a Content Understanding analyzer

**Answer:** B — The three objectives are: describe the capabilities of image-generation models, use the Images playground in Microsoft Foundry portal, and integrate image-generation models into your apps.

---

**Q22.** What prerequisites does the module state a learner should already have?

A. No prerequisites at all; this module is intended for absolute beginners
B. Familiarity with Microsoft Foundry and programming experience
C. Prior experience with Azure AI Search indexing
D. A completed certification in Azure Data Engineering

**Answer:** B — Prerequisites listed are familiarity with Microsoft Foundry and programming experience.

---

**Q23.** Within the "Plan and manage an Azure AI solution" exam skill area, which module content maps to "choose an appropriate model for each task"?

A. The Images playground's resolution control for setting output image size and aspect ratio
B. Using the Model catalog and filtering by inference task ("text to image") to find image-generation models
C. The `n` parameter in `client.images.generate()`, which sets the number of variations
D. Deleting Azure resources after the exercise to avoid ongoing charges once testing is complete

**Answer:** B — Filtering the Model catalog by inference task is how the module ties into the "choose an appropriate model for each task" guidance under "Plan and manage an Azure AI solution."

---

## Introduction

**Q1.** According to the module, which OpenAI model is given as the example that "can create original graphical content based on a description of a desired image"?

A. `dall-e-3`
B. `gpt-image-1`
C. `gpt-4-vision`
D. `text-embedding-3-large`

**Answer:** B — The introduction unit names `gpt-image-1` as the example image-generation model.

**Q2.** Which of the following applications are explicitly called out in the module's introduction as use cases for AI image generation? (Choose two.)

A. Generating unique product or company logos
B. Generating photorealistic images for articles or marketing collateral
C. Translating scanned documents into structured JSON
D. Detecting objects within an existing photograph

**Answer:** A, B — The introduction lists illustrations/photorealistic images for articles or marketing collateral, and generation of unique product or company logos, as example applications.

**Q3.** The module offers its content in two formats. What are they?

A. PDF and interactive notebook
B. Video and text
C. Slides and audio
D. Text and a live sandbox only

**Answer:** B — The module explicitly supports a video pivot and a text pivot, noting the text contains more detail.

## What are image-generation models?

**Q4.** Which two model families does the module name as being supported for image generation in Microsoft Foundry? (Choose two.)

A. OpenAI `gpt-image-1` series
B. Black Forest Labs `FLUX` series
C. Meta `Llama Vision` series
D. Stability AI `SDXL` series

**Answer:** A, B — The module explicitly names the OpenAI `gpt-image-1` series and the Black Forest Labs `FLUX` series (stating "including but not limited to").

**Q5.** You are browsing the Microsoft Foundry Model catalog and want to narrow the list down to models that can generate images from text. Which inference task should you filter by?

A. Image to text
B. Text to image
C. Embeddings
D. Chat completion

**Answer:** B — Text to image is the exact inference-task filter named in the module (and repeated as the answer to the module's own knowledge check).

**Q6.** A colleague claims that Azure image-generation models work by searching a large curated library of stock photos for the closest match to a prompt. Is this an accurate description of how the models described in this module work?

A. Yes, image generation models retrieve the nearest matching image from a curated catalog.
B. No, the models generate original images based on patterns learned during training; they are not a retrieval/search system.
C. Yes, but only for the FLUX model family, which retrieves near-matches from Black Forest Labs' training corpus.
D. No, they only work when a reference image is supplied to ground the generation in an existing photo.

**Answer:** B — The module explicitly states the generated images are original and not retrieved from a curated image catalog — the model generates new images rather than searching for existing ones.

**Q7.** Where can you view the full set of image-generation models available in Microsoft Foundry?

A. The Azure Portal "Cognitive Services" blade
B. The Microsoft Foundry Model catalog
C. The Azure OpenAI Studio "Deployments" tab only
D. The Azure AI Search index list

**Answer:** B — The module points to the Model catalog (`ai.azure.com/catalog/models`) as the place to view the full set of available models, filterable by inference task.

## Explore image-generation models in Microsoft Foundry portal

**Q8.** Which Microsoft Foundry feature lets you interactively submit prompts and preview generated images without writing code?

A. The Prompt flow designer for orchestration workflows
B. The Images playground (model playground)
C. The Evaluation pipeline for model scoring
D. The Content Understanding analyzer

**Answer:** B — The module describes using the "model playground" (Images playground) in Microsoft Foundry portal to submit prompts and view resulting images.

**Q9.** Before you can use the Images playground, what must you first create?

A. An Azure Storage account with a blob container
B. A Microsoft Foundry project
C. An Azure Kubernetes Service cluster
D. A Log Analytics workspace

**Answer:** B — The module states you create a Microsoft Foundry project, then use the model playground to experiment with image generation models.

**Q10.** In the Images playground, which two generation controls does the module say you can configure (subject to model support)? (Choose two.)

A. The resolution (size) of generated images
B. A reference image for the model to base its output on
C. The temperature/randomness parameter
D. A vector index to ground the output

**Answer:** A, B — The module explicitly says you can specify the resolution (size) and include a reference image, subject to model support.

## Create a client application that uses an image generation model

**Q11.** Which two SDKs does the module name as options for building a client application that generates images?

A. The OpenAI Python SDK
B. The Azure OpenAI .NET SDK
C. The Azure Cognitive Services Java SDK
D. The Microsoft Bot Framework SDK

**Answer:** A, B — The module names the OpenAI Python SDK and the Azure OpenAI .NET SDK as example language-specific SDKs.

**Q12.** Given the module's Python code sample:
```python
img_results = client.images.generate(
    model="FLUX.1-Kontext-pro",
    prompt="A robot eating a cheeseburger.",
    n=1,
    size="1024x1024",
)
```
Which method call is used to request the image, and which OpenAI API family does it belong to?

A. `client.images.edit()` — the Edits API
B. `client.images.generate()` — the Images API
C. `client.completions.create()` — the Completions API
D. `client.responses.create()` — the Responses API

**Answer:** B — The sample calls `client.images.generate()`, which is part of the OpenAI Images API (this is also the answer to the module's own knowledge-check question "Which OpenAI API can you use with image-generation models?" → Image).

**Q13.** In the module's code sample, how is the generated image data returned and saved to disk?

A. As a public URL in `img_results.data[0].url`, downloaded with `requests.get()` before saving
B. As a base64-encoded string in `img_results.data[0].b64_json`, decoded with `base64.b64decode()` and written to a file
C. As a raw PNG byte stream returned directly by `client.images.generate()`, with no decoding step needed
D. As a SAS-token-protected blob reference that must be fetched via the Azure Storage SDK

**Answer:** B — The sample decodes `img_results.data[0].b64_json` using `base64.b64decode()` and writes the bytes to `image.png`.

**Q14.** Which parameters appear in the module's `client.images.generate()` sample? (Choose three.)

A. `model`
B. `prompt`
C. `size`
D. `quality`

**Answer:** A, B, C — The sample uses `model`, `prompt`, `n`, and `size`. `quality` is not present in this module's sample (it is a parameter documented elsewhere in the broader OpenAI/Azure OpenAI Images API but not shown in this module's content — flagged as a content gap in content.md).

**Q15.** A developer wants to *edit* an existing image by masking out a region and asking the model to fill it in with new content based on a prompt (inpainting). Based strictly on what this module teaches, which SDK call demonstrates this workflow?

A. `client.images.edit()` with a `mask` parameter pointing to the region to fill
B. `client.images.generate()` with an `inpaint=True` flag enabling region-based editing
C. `client.images.variations()` with a `region` parameter restricting the edit area
D. None — this module does not demonstrate any image-editing or mask-based inpainting call

**Answer:** D — The module's only demonstrated call is `client.images.generate()`; it contains no image-editing, mask, or inpainting example or discussion. **[Note: mask-based inpainting is a real capability of the broader Azure OpenAI/OpenAI image APIs — this question tests recognition that it is absent from this specific module's content, per the gap noted in content.md.]**

## Exercise - Generate images with AI

**Q16.** What are the ordered high-level steps of the hands-on exercise in this module? (Choose three.)

A. Provision a Microsoft Foundry project
B. Deploy an image generation model
C. Use Python to consume the model from a custom application
D. Configure a Custom Vision classifier and train it on labeled images

**Answer:** A, B, C — The exercise: provision a Microsoft Foundry project, deploy an image generation model, explore it in the portal Images playground, then use Python to consume it from a custom application. Custom Vision classifier training is unrelated and not part of this exercise.

**Q17.** What does the module recommend you do after completing the exercise, if you're finished exploring Microsoft Foundry?

A. Leave the resources running for future exercises
B. Delete the Azure resources you created during the exercise
C. Export the deployed model to an on-premises container
D. Downgrade the Foundry project's pricing tier

**Answer:** B — The module explicitly tips readers to delete the Azure resources created during the exercise once finished exploring.

## Module assessment

**Q18.** [As presented in the module's own knowledge check] Which OpenAI API can you use with image-generation models?

A. Video
B. Image
C. Graphics
D. Embeddings

**Answer:** B — Confirmed both by the knowledge-check unit and by Unit 4's demonstration of the `images.generate()` call as part of the OpenAI **Images** API.

## Summary

**Q19.** Per the module's summary, which two methods does it say you can use to build applications that generate new images with Microsoft Foundry image-generation models? (Choose two.)

A. REST APIs
B. SDKs
C. Azure Data Factory pipelines
D. Logic Apps connectors only

**Answer:** A, B — The summary states you can use REST APIs or SDKs to build applications that generate new images (though note: the module's own content only ever shows a concrete SDK example — no REST endpoint detail is given, per the gap noted in content.md).

**Q20.** [general knowledge] The module distinguishes image *generation* (text → image) from image *understanding* (image → text, e.g., captioning/VQA), which is covered in a separate sibling module of the same learning path. Which of the following best characterizes that distinction as drawn across the two modules?

A. Generation and understanding use the same API surface and are interchangeable, since both call `images.generate()` under the hood with different parameter names
B. Generation takes a text prompt and produces an image (e.g., `images.generate()`), while understanding takes an image as input and produces text (e.g., a caption or answer) using a multimodal/vision-capable chat model
C. Understanding is only possible with the FLUX model family, since only FLUX exposes a vision-capable inference task in the Model catalog filter used for model selection
D. Generation always requires a reference image as input, since `images.generate()` cannot run from a text prompt alone without one attached to ground the composition

**Answer:** B — This module (generation) is entirely about producing images from text prompts via `images.generate()`; the companion visual-understanding module deals with the reverse direction, feeding images into a multimodal model to produce descriptive or analytical text. **[Flagged general knowledge: the precise sibling-module comparison is inferred/contextual, not verbatim text within this module's own units.]**

---

## Scenario-based questions

**Q24.** *(Scenario)* You need to stand up an image-generation feature end to end: find a suitable model, try it out with a reference image, then wire it into a Python app. Put these module-taught steps in the correct order.

A. Write `client.images.generate()` code first, then browse the Model catalog, then test in the playground before deploying to production without further validation or review
B. Filter the Model catalog by inference task "Text to image" to find a model, try it in the Images playground (optionally with a reference image), then call `client.images.generate()` from a Python app using that model's deployment name
C. Deploy directly from the Images playground with no catalog step, then skip straight to production without any validation testing or output review by a moderator
D. Use `client.images.edit()` with a mask, then filter the catalog afterward to pick a matching deployment name and its supported parameters

**Answer:** B — The module's flow is: use the Model catalog filtered to "Text to image" models to identify a suitable model, validate interactively in the Images playground (which supports resolution control and an optional reference image), then integrate via the SDK's `client.images.generate()` call using the deployed model's name as the `model` parameter.

---

**Q25.** *(Scenario)* A developer wants to take an existing product photo and inpaint just the background using a text prompt, keeping the product itself unchanged. They plan to use only what's demonstrated in this module. What should they conclude?

A. Call `client.images.generate()` with `size` set to match the original image and a `mask` parameter pointing to the background region, since `generate()` accepts inpainting parameters identical to `edit()`
B. This module does not demonstrate any editing/inpainting/mask workflow — only whole-image generation via `client.images.generate()` is shown, so they'd need to look beyond this module's content for an edit-capable call
C. Use the Images playground's "reference image" feature, which performs true mask-based inpainting by automatically detecting the product boundary using edge-detection heuristics
D. Use FLUX.1-Kontext-pro's `n` parameter to blend the new background in automatically across all generated variations returned by a single request

**Answer:** B — The module explicitly contains no `images.edit`, mask parameter, or inpainting workflow — its only demonstrated call is generation-only `client.images.generate()`. The Images playground's reference image feature lets a model "base its output on" a reference, but the module never describes this as mask-based inpainting.

---

**Q26.** *(Scenario)* Your architecture review needs to state, for the exam objective "Implement responsible AI for multimodal content" (filters for unsafe generated visual content), what this module contributes. What is the accurate statement?

A. The module provides a detailed walkthrough of content-filtering configuration for generated images, including step-by-step moderation threshold tuning instructions
B. The module does not mention content filtering, moderation, or responsible-AI controls for generated images anywhere in its units — this is a documented content gap, not evidence the underlying service lacks the capability
C. The module states that FLUX models are exempt from content filtering because Black Forest Labs applies filtering upstream, per its published model card
D. The module implements responsible AI via the `quality` parameter, which it claims also screens generated output for unsafe or policy-violating content before delivery

**Answer:** B — content.md explicitly flags that no discussion of content filtering, moderation, or responsible-AI controls for generated images appears anywhere in units 1-7 of this module, even though the broader Azure OpenAI/Foundry platform does provide such controls.
