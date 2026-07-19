# Practice questions — Generate videos with Microsoft Foundry

Grounded in `content.md` (source: https://learn.microsoft.com/en-us/training/modules/generate-video-with-foundry/). Questions flagged **[general knowledge]** draw on well-established Azure knowledge beyond the module text.

## Learning objectives / Exam relevance

**Q37.** Which of the following is one of the three stated learning objectives for this module?

A. Deploy a video-generating AI model in Microsoft Foundry
B. Train a custom video classification model
C. Configure Azure AI Search vector indexes for video
D. Fine-tune Sora 2 on proprietary footage

**Answer:** A — The three objectives are: deploy a video-generating AI model in Microsoft Foundry, test a video-based prompt in the chat (video) playground, and use the Azure OpenAI SDK to generate and remix videos in Python.

---

**Q38.** Under the "Implement responsible AI for multimodal content" exam skill, which module content is the relevant mapping?

A. The `seconds` parameter default value, which governs how long generated clips run
B. The content moderation filter that rejects prompts recognized as harmful content, returning no generated video
C. The `remix_video_id` parameter, used to identify a prior video for targeted editing
D. The two supported output resolutions, landscape and portrait aspect ratios at 720p

**Answer:** B — The exam-relevance mapping ties "filters to classify unsafe/disallowed visual content" to the content moderation filter mentioned in Units 3 and 4, which rejects prompts recognized as harmful content.

---

## Unit 1: Introduction

**Q1.** Which company originally developed the Sora 2 model that is available for deployment in Microsoft Foundry?

A. Microsoft
B. OpenAI
C. Meta, known for its Llama model family
D. Stability AI

**Answer:** B — The module states Sora 2 "is an AI model from OpenAI that creates realistic and imaginative video scenes from text instructions, input images, or existing videos."

**Q2.** According to the module introduction, which SDK is used to build a Python application that creates videos programmatically with Sora 2?

A. Azure AI Vision SDK
B. Azure AI Content Understanding SDK
C. OpenAI SDK
D. Azure Cognitive Services Media SDK

**Answer:** C — Unit 1 states you'll "build a Python application that creates videos programmatically using the OpenAI SDK."

**Q3.** From which three input types can Sora 2 generate video content, per the module introduction?

A. Text prompts, reference images, and remixing existing videos
B. Text prompts, audio clips, and 3D models generated from a shared latent space
C. Reference images, spreadsheets, and audio clips
D. Text prompts, PDF documents, and remixing existing videos

**Answer:** A — "you can generate realistic and imaginative video scenes from text prompts, reference images, or by remixing existing videos."

**Q4.** True/False style — Which statement best describes the relationship between "Azure AI Foundry" and "Microsoft Foundry" as used in current Microsoft documentation and the AI-103 exam context?

A. They are unrelated, separate Azure services with different pricing and portals
B. Microsoft Foundry is a rebranded name for the same portal/product previously called Azure AI Foundry
C. Microsoft Foundry is the enterprise SKU and Azure AI Foundry is the free tier
D. Azure AI Foundry was deprecated and replaced entirely by a different product with no portal continuity

**Answer:** B — Microsoft has rebranded "Azure AI Foundry" to "Microsoft Foundry"; the portal remains at ai.azure.com and both names refer to the same service for exam purposes.

## Unit 2: Deploy a video generating model

**Q5.** In the Microsoft Foundry portal, which navigation path is used to locate and deploy the Sora-2 model?

A. Build → Models → search for Sora-2 → Deploy
B. Manage → Deployments → Add new resource → Sora-2
C. Playground → Video → Import model
D. Settings → Model catalog → Sora-2 → Publish

**Answer:** A — Steps given: select **Build** from the navigation pane, select **Models** to view the catalog, search for **Sora-2**, then select **Deploy**.

**Q6.** Which TWO resolutions does Sora 2 support for generated video output? (Choose two.)

A. 1280×720 (landscape)
B. 1920×1080 (landscape)
C. 720×1280 (portrait)
D. 1080×1080 (square)

**Answer:** A, C — The capabilities table lists "portrait (720×1280) and landscape (1280×720) formats" only.

**Q7.** Which THREE video durations can Sora 2 generate? (Choose three.)

A. 4 seconds
B. 6 seconds
C. 8 seconds
D. 12 seconds

**Answer:** A, C, D — "Generate videos of 4, 8, or 12 seconds."

**Q8.** Which of the following is listed as a Sora 2 capability alongside text-to-video and image-to-video?

A. Automatic subtitle translation
B. Audio generation in output videos
C. Real-time live streaming
D. 3D model export in glTF format

**Answer:** B — The capabilities table includes "Audio generation — Supports audio generation in output videos."

**Q9.** Before you can deploy Sora 2 in Microsoft Foundry, which of the following is NOT listed as a prerequisite in the module?

A. An Azure subscription with Cognitive Services enabled
B. Access to the Microsoft Foundry portal with contributor role assigned
C. A Foundry project where you have permissions to deploy models
D. A pre-approved content moderation exemption certificate

**Answer:** D — Listed prerequisites are only: Azure subscription, Foundry portal access, and a Foundry project with deploy permissions. No such exemption certificate is mentioned.

**Q10.** [general knowledge] Which Microsoft Foundry portal URL is used to sign in and deploy models such as Sora-2?

A. https://portal.azure.com
B. https://ai.azure.com
C. https://studio.azure.com
D. https://foundry.microsoft.com

**Answer:** B — The module directs users to "the Microsoft Foundry portal (https://ai.azure.com)."

## Unit 3: Generate video from a prompt

**Q11.** Why does the Sora 2 video generation API in Microsoft Foundry follow a submit-then-retrieve pattern rather than returning a result immediately?

A. Because video generation is an asynchronous process
B. Because the API requires manual admin approval for every request
C. Because video files must be uploaded to Azure Blob Storage first
D. Because Sora 2 only supports batch processing, not single requests

**Answer:** A — "Video generation is an asynchronous process—you submit a request with your prompt and video settings, then retrieve the completed video when it's ready."

**Q12.** A developer wants to submit a video generation request using the highest-quality/pro variant of the model. Which value should they pass for the `model` parameter?

A. `sora-2-hd`
B. `sora-2-pro`
C. `sora-2-plus`
D. `sora-video-pro`

**Answer:** B — Supported model values are `sora-2` or `sora-2-pro`.

**Q13.** What is the default value of the `seconds` parameter if not explicitly specified in a video generation request?

A. 4
B. 8
C. 12
D. There is no default; it is required

**Answer:** A — The parameter table states seconds supports `4`, `8`, or `12` (default: `4`).

**Q14.** Which parameter would you set to generate a new video by making targeted edits to a previously generated video?

A. `input_reference`
B. `remix_video_id`
C. `seed_video`
D. `source_id` referencing the origin clip

**Answer:** B — "remix_video_id — ID of a previous video to remix."

**Q15.** Which TWO of the following are valid file formats for an `input_reference` image supplied to Sora 2? (Choose two.)

A. JPEG
B. GIF
C. WebP
D. BMP

**Answer:** A, C — "Requirements for reference images: ... Supported formats: JPEG, PNG, WebP." (PNG is also valid but not offered as an option here; JPEG and WebP are the correct picks among the choices given.)

**Q16.** According to the module's prompting guidance, what is a key requirement for an `input_reference` image before submitting a generation request?

A. It must be uploaded to Azure Blob Storage with a SAS token
B. Its resolution must match the target video's `size` parameter
C. It must contain a clear image of a human face for continuity
D. It must be exactly the same aspect ratio regardless of `size`

**Answer:** B — "The image resolution must match the target video size (1280x720 or 720x1280)."

**Q17.** A prompt engineer wants better adherence to instructions from Sora 2. Per the module's tip, what should they do?

A. Always request the maximum 12-second duration for richer detail
B. Generate two 4-second clips and stitch them together rather than one 8-second clip
C. Avoid specifying camera framing so the model has creative freedom
D. Submit the same prompt multiple times in parallel and average the results

**Answer:** B — "The model follows instructions more reliably in shorter clips. For best results, consider generating two 4-second clips and stitching them together rather than a single 8-second clip."

**Q18.** What happens if Azure OpenAI's content moderation filter recognizes a video generation prompt as harmful content?

A. It generates a blurred/censored version of the video
B. It won't return a generated video
C. It generates the video but flags it for manual admin review before download
D. It automatically rewrites the prompt to a safe alternative and proceeds

**Answer:** B — "If Azure OpenAI recognizes your prompt as harmful content, it won't return a generated video."

**Q19.** In the Foundry Video playground, which button provides prefilled cURL code samples matching your current generation settings?

A. Export to a shareable link
B. View code
C. Copy request
D. Show API

**Answer:** B — "Select the View code button at the top of the playground to access sample code you can use in your applications."

**Q39.** In the Foundry Video playground, roughly how long does video generation typically take, depending on settings?

A. A few seconds
B. 1 to 5 minutes
C. 15 to 20 minutes
D. Over an hour

**Answer:** B — "Video generation typically takes 1 to 5 minutes depending on settings."

---

**Q40.** Put the Video playground testing steps in the correct order: (1) Configure video settings, (2) Select Generate, (3) Navigate to your deployed Sora 2 model, (4) Enter your prompt, (5) Select the Playground tab.

A. 5, 3, 4, 1, 2
B. 3, 5, 4, 1, 2
C. 3, 4, 5, 1, 2
D. 5, 4, 3, 1, 2

**Answer:** B — The steps are: navigate to your deployed Sora 2 model, select the Playground tab, enter your prompt, configure video settings, then select Generate.

---

**Q41.** Per the module's prompt-writing guidance ("think of prompting like briefing a cinematographer"), which FIVE elements make up effective prompt anatomy? (Choose five.)

A. Camera framing
B. Subject description
C. Action (described in beats)
D. Lighting and palette
E. Style
F. Frame-rate specification

**Answer:** A, B, C, D, E — The module lists camera framing, subject description, action, lighting and palette, and style as the five elements of prompt anatomy. Frame-rate specification is not mentioned.

---

**Q42.** Which of the following is given as an example of a "strong" prompt (as opposed to its weak counterpart) in the module's weak-vs-strong prompt table?

A. "A beautiful street at night, warmly lit and picturesque"
B. "Person moves quickly through the busy evening scene"
C. "Wet asphalt, zebra crosswalk, neon signs reflecting in puddles"
D. "Cinematic look, moody atmosphere, dramatic shadows"

**Answer:** C — This is the strong-prompt counterpart to the weak prompt "A beautiful street at night" in the module's table; A, B, and D are all listed as the weak versions.

---

**Q43.** According to the module's remix best practices, how many distinct adjustments should a single remix request focus on?

A. As many as needed to fully re-imagine the video
B. Exactly one clearly articulated adjustment
C. At least three, to make the remix worthwhile
D. Remix requests cannot specify adjustments — they only re-render with a new seed

**Answer:** B — Best practice: "Limit changes to one clearly articulated adjustment" and "narrow, precise edits retain greater fidelity to the source material."

---

**Q44.** Which of the following is listed among the module's general "Tips for better results" when generating video?

A. Always maximize duration to 12 seconds for richer scenes, since longer clips give the model more room to develop the story
B. Use beats for timing, e.g., "actor takes four steps to the window, pauses, and pulls the curtain," instead of vague phrasing like "actor walks across the room"
C. Avoid iterating — the first generation is always optimal, so re-running the same prompt wastes rate-limited job slots
D. Vary character phrasing across shots to keep things creative, rather than reusing consistent descriptive language

**Answer:** B — The tips explicitly recommend using beats for timing with that exact example, keeping prompts simple, staying consistent (reusing phrasing for characters across shots), and iterating since later generations may be better — the opposite of options A, C, and D.

---

## Unit 4: Generate video in Python

**Q20.** Using the OpenAI Python SDK against a Sora 2 deployment, which method call creates a new asynchronous video generation job?

A. `client.videos.generate()`
B. `client.videos.create()`
C. `client.video_jobs.submit()`
D. `client.media.videos.new()`

**Answer:** B — Example: `video = client.videos.create(model="sora-2", prompt=..., size=..., seconds=...)`.

**Q21.** After creating a video job, which method is used inside a polling loop to check the latest job status?

A. `client.videos.status()`
B. `client.videos.poll()` inside a retry-backoff loop
C. `client.videos.retrieve(video.id)`
D. `client.videos.refresh(video.id)`

**Answer:** C — The polling loop calls `video = client.videos.retrieve(video.id)`.

**Q22.** Which TWO of the following are valid values that a video job's `status` attribute can hold, per the module? (Choose two.)

A. `queued`
B. `pending_review`
C. `in_progress`
D. `rendering`

**Answer:** A, C — Valid statuses listed are: `queued`, `in_progress`, `completed`, `failed`, `cancelled`.

**Q23.** When a video job's status is `failed`, where should a developer look to diagnose what went wrong?

A. `video.status_reason`
B. `video.error`
C. `video.diagnostics`
D. `video.exception`

**Answer:** B — "When a job fails, check video.error for details about what went wrong."

**Q24.** Which method downloads the completed video content once a job's status is `completed`?

A. `client.videos.fetch_result(video.id, format="mp4")`
B. `client.videos.download_content(video.id, variant="video")`
C. `client.videos.export(video.id, variant="video")`
D. `client.videos.get_file(video.id, variant="video")`

**Answer:** B — `content = client.videos.download_content(video.id, variant="video")` followed by `content.write_to_file("output.mp4")`.

**Q25.** A developer passes an `input_reference` image of a person's face to `client.videos.create()`. What will happen?

A. The image will be accepted and used to anchor the first frame normally
B. The image will be rejected — reference images containing human faces are currently rejected
C. The face will automatically be blurred and the rest of the image processed
D. The request succeeds but the video is generated without audio, since faces disable audio synthesis

**Answer:** B — "Reference images containing human faces are currently rejected. Use images of landscapes, objects, or animated characters instead."

**Q26.** Which SDK call is used to create a remix of an existing video, and what parameter identifies the source video?

A. `client.videos.edit(source=..., mode="remix")`
B. `client.videos.remix(video_id=..., prompt=...)`
C. `client.videos.modify(target_id=..., prompt=...)`
D. `client.videos.create(remix=True, video_id=...)`

**Answer:** B — `video = client.videos.remix(video_id="video_abc123", prompt="Change the color palette to warm sunset tones")`.

**Q27.** Per the "Key considerations" in the Python unit, how many video creation jobs can a user run simultaneously, and how long are completed videos available for download?

A. 1 job simultaneously; 12 hours
B. 2 jobs simultaneously; 24 hours
C. 5 jobs simultaneously; 48 hours
D. Unlimited jobs; 7 days

**Answer:** B — "Rate limits: You can run up to two video creation jobs simultaneously. Job expiration: Completed videos are available for download for 24 hours."

**Q28.** A developer notices that requests with `input_reference` set to an image with a different resolution than the requested `size` fail validation. What does the module say about this requirement?

A. Resolution can differ; the API automatically resizes the reference image
B. Reference images must match the target video resolution exactly
C. Only the aspect ratio needs to match, not the exact pixel resolution
D. Resolution mismatches are allowed but reduce output quality

**Answer:** B — "Resolution requirements: Reference images must match the target video resolution exactly."

## Unit 5: Exercise

**Q29.** What is the approximate estimated time to complete the hands-on exercise "Generate video with Sora 2 in Microsoft Foundry"?

A. 5 minutes
B. 15 minutes
C. 30 minutes
D. 60 minutes

**Answer:** C — The exercise unit lists a duration of 30 minutes.

**Q30.** What does the hands-on exercise guide the learner through?

A. Configuring Azure Content Understanding pipelines for extracting structured video metadata
B. Deploying the Sora 2 model, generating videos from text prompts, and using reference images for more control
C. Setting up Azure Cognitive Search vector indexes for video metadata to enable semantic search
D. Training a custom video classification model from scratch using labeled frame annotations

**Answer:** B — "This exercise will guide you through deploying the Sora 2 model, generating videos from text prompts, and using reference images for more control over your video content."

## Unit 6: Module assessment (knowledge check topics)

**Q31.** Based on the module's own assessment focus, which statement correctly describes Sora 2's supported video durations?

A. 1 to 20 seconds in 1-second increments
B. 4, 8, or 12 seconds
C. Any duration up to 60 seconds
D. Fixed at exactly 10 seconds

**Answer:** B — Consistent with the parameter table: `seconds` supports `4`, `8`, or `12`.

**Q32.** What does the official module assessment identify as required when using a reference image with Sora 2?

A. The image must be smaller than 1 MB to avoid upload timeouts
B. The image resolution must match the target video size
C. The image must contain at least one human face
D. The image must be uploaded in TIFF format

**Answer:** B — Matches Unit 3/4 guidance on `input_reference` resolution matching (and note option C is actually the opposite of the truth — face images are rejected).

**Q33.** What is the remix feature used for in Sora 2, per the module's own assessment framing?

A. Combining multiple videos into one continuous rendered sequence
B. Making targeted adjustments to an existing video without regenerating from scratch
C. Adding background music to generated videos using a licensed audio track library
D. Converting a video from portrait to landscape orientation via an automatic reframing pass

**Answer:** B — Matches the definition given in Units 3 and 4: remix "modifies specific aspects of an existing video while preserving its core elements."

## Unit 7: Summary

**Q34.** Which single architectural pattern does the module summary emphasize as the key enabler for integrating video generation into applications?

A. Synchronous request/response calls with immediate results
B. The asynchronous pattern: submit a job, poll for status, download the result
C. Webhooks that push completed videos to a configured endpoint
D. A batch-only nightly processing pipeline triggered by a scheduled job

**Answer:** B — "The asynchronous API pattern—submit a job, poll for status, download the result—enables you to integrate video generation into your applications."

**Q35.** Which Microsoft Learn article is referenced in the summary for further reading on video generation with Sora?

A. Content filtering concepts for generative AI outputs
B. Video generation with Sora (Azure OpenAI documentation)
C. Model catalog and collections in Microsoft Foundry portal
D. Responsible AI overview for generative models

**Answer:** B — "For more information about video generation with Sora 2, see Video generation with Sora in the Azure OpenAI documentation."

**Q36.** Which of the following capabilities were explicitly covered across this module, per the summary recap? (Choose three.)

A. Deploying a Sora 2 video generation model in Microsoft Foundry
B. Writing effective prompts describing camera framing, subject details, action, and lighting
C. Training a custom Sora 2 model on proprietary video datasets
D. Building a Python application that creates videos programmatically using the OpenAI SDK

**Answer:** A, B, D — The summary explicitly lists deployment, prompt writing, playground testing, reference-image/remix generation, and the Python application — it does NOT mention custom model training/fine-tuning (option C is not supported anywhere in the module).

---

## Scenario-based questions

**Q45.** *(Scenario)* You deploy `sora-2` in Foundry, submit `client.videos.create(model="sora-2", prompt="...", size="1280x720", seconds="8", input_reference=open("ceo_headshot.jpg","rb"))`, and the job comes back with `status == "failed"`. What are the two most likely causes to check first, based on this module's content?

A. The `seconds` value of 8 is invalid for Sora 2, which only accepts values of 4 or 12
B. `ceo_headshot.jpg` likely contains a human face (rejected), or its resolution doesn't exactly match `1280x720`
C. The `model` name is case-sensitive and must be `Sora-2` with a capital S, not lowercase
D. `input_reference` doesn't accept JPEG files, only PNG and WebP are supported formats

**Answer:** B — Two documented failure causes are: reference images containing human faces are currently rejected, and reference images must match the target video resolution exactly. `seconds="8"` is valid (4, 8, or 12), `model="sora-2"` is correct, and JPEG is a supported format — so A, C, D are not the issue.

---

**Q46.** *(Scenario)* You generated a 4-second video (`video_id="video_abc123"`) and now want only the lighting and color palette changed, keeping the same shot and structure, without regenerating from scratch and without running more than one other job concurrently (you already have one job in progress). What is the correct approach?

A. Call `client.videos.create()` again with the same prompt plus new lighting details — remix is not needed since create() always incorporates prior context automatically
B. Call `client.videos.remix(video_id="video_abc123", prompt="same shot, new lighting: teal, sand, rust")`, noting this counts toward the 2-concurrent-job limit alongside your existing job
C. Call `client.videos.remix()` without a `video_id`, since it operates on the most recent job tracked in the current session's local job cache
D. Wait until the first job's 24-hour download window expires before starting a remix, since remix requires the source job to be fully expired

**Answer:** B — `client.videos.remix(video_id=..., prompt=...)` is the documented way to make a targeted, focused edit (here, lighting/palette) while preserving core structure; remix jobs are still video creation jobs subject to the "up to two simultaneous" rate limit, so running it alongside the one in-progress job is allowed (2 total) but a third would not be.

---

**Q47.** *(Scenario)* Comparing this module's video-generation workflow to the sibling image-generation module's workflow, what is the single biggest architectural difference an app developer must design for?

A. Video generation requires no authentication while image generation does, since video endpoints are exempt from the Foundry API-key requirement
B. Video generation is asynchronous (submit job → poll status → download result) due to longer processing time, whereas the image-generation module treats generation as effectively immediate/synchronous
C. Video generation only works via REST, never via SDK, unlike image generation, since the OpenAI Python SDK's `videos` namespace does not exist for this model family
D. Video generation does not support content moderation filters while image generation does, so harmful video prompts are never rejected before rendering

**Answer:** B — This module explicitly contrasts its asynchronous submit-then-retrieve pattern (driven by longer video processing time) with image generation's more immediate, synchronous-style workflow — this is called out as "the single most exam-relevant architectural distinction" in the Unit 7 summary.
