# Generate videos with Microsoft Foundry

Source: https://learn.microsoft.com/en-us/training/modules/generate-video-with-foundry/

> Naming note: this module was recently rebranded by Microsoft from "Generate video with Azure AI Foundry" to "Generate videos with Microsoft Foundry" (the service/portal is being renamed "Microsoft Foundry", portal URL still `https://ai.azure.com`). The exam guide (AI-103) may still reference "Azure AI Foundry" — treat **Azure AI Foundry** and **Microsoft Foundry** as the same service/product for exam purposes. Module level: Intermediate. Role: AI Engineer. 7 units total.

## Learning objectives

After completing this module, you'll be able to:

- Deploy a video-generating AI model in Microsoft Foundry.
- Test a video-based prompt in the chat (video) playground.
- Use the Azure OpenAI SDK to generate and remix videos in Python.

Prerequisites: experience deploying generative AI models in Microsoft Foundry; programming experience.

## Exam relevance

Maps primarily to **Implement computer vision solutions (10–15%)** → "Design and implement image- and video-generation solutions":
- Implement a solution that generates videos from text prompts and reference media → Unit 3 (prompt-based generation, `input_reference`), Unit 4 (`client.videos.create`)
- Implement workflows to edit generated videos → Unit 3 & 4 (remix feature, `client.videos.remix`)
- Select and apply appropriate generation and editing controls provided by the platform → Unit 3 parameter table (`size`, `seconds`, `model`)

Also touches **Implement responsible AI for multimodal content**:
- Filters to classify unsafe/disallowed visual content → content moderation filter mentioned in Unit 3 & 4 (prompts rejected as harmful content; human-face reference images rejected)

Also touches **Plan and manage an Azure AI solution (25–30%)**:
- Choose appropriate deployment options / configure model deployments → Unit 2 (deploying Sora-2 via Foundry portal model catalog)
- Manage quotas, scaling, rate limits → Unit 4 (2 concurrent video jobs, 24-hour download expiration)

Also touches **Implement generative AI and agentic solutions**:
- Integrate generative workflows into applications by using Foundry SDKs and connectors → Unit 4 (OpenAI Python SDK `client.videos.*`)

## Unit 1: Introduction

Generative AI has expanded beyond text and images to video creation. **Sora 2** in Microsoft Foundry generates realistic and imaginative video scenes from:
- text prompts
- reference images
- remixing (editing) existing videos

The module teaches: deploying Sora 2, writing effective video prompts, and building a Python application that creates videos programmatically using the **OpenAI SDK**.

## Unit 2: Deploy a video generating model

**Sora 2** is an AI model **from OpenAI** that creates realistic and imaginative video scenes from text instructions, input images, or existing videos. It is available in Microsoft Foundry and is described as an "all-in-one creative platform with superior video quality and intuitive controls."

### Prerequisites to deploy Sora 2
- An Azure subscription
- Access to the Microsoft Foundry portal
- A Foundry project where you have permissions to deploy models

### Deployment steps (Foundry portal)
1. Go to the Microsoft Foundry portal (`https://ai.azure.com`) and sign in.
2. From the Foundry landing page, create or select a project.
3. Select **Build** from the navigation pane on the right.
4. Select **Models** from the left-hand menu to open the model catalog.
5. Use the search bar/filters to find the **Sora-2** video generation model.
6. Select the **Sora-2** model, select **Deploy**, and choose the appropriate deployment settings.

Reference doc mentioned: "Model catalog and collections in Microsoft Foundry portal" (`/en-us/azure/ai-foundry/how-to/model-catalog-overview`).

### Sora 2 capabilities (exact table from source)

| Feature | Description |
| --- | --- |
| Text to video | Generate videos from natural language text prompts |
| Image to video | Transform existing images into video content |
| Video remix | Make targeted adjustments to existing videos without regenerating from scratch |
| Audio generation | Supports audio generation in output videos |
| Multiple resolutions | Supports portrait (720×1280) and landscape (1280×720) formats |
| Variable duration | Generate videos of 4, 8, or 12 seconds |

Key exam facts: only two resolutions (1280x720 landscape, 720x1280 portrait); only three duration values (4, 8, 12 seconds); Sora 2 also generates **audio** in the output video (not silent/visual-only).

## Unit 3: Generate video from a prompt

Once Sora 2 is deployed, video generation is an **asynchronous process**: you submit a request with prompt + video settings, then retrieve the completed video when ready. (Contrast with image generation, which the module positions as more immediate/synchronous — video generation explicitly requires submit-then-retrieve due to longer processing time.)

### Video generation parameters (exact table from source)

| Parameter | Description | Supported values |
| --- | --- | --- |
| `prompt` | Natural language description of your video | Text string (required) |
| `model` | The model to use | `sora-2` or `sora-2-pro` |
| `size` | Output resolution | `1280x720` (landscape), `720x1280` (portrait) |
| `seconds` | Video duration | `4`, `8`, or `12` (default: `4`) |
| `input_reference` | Reference image for the first frame | JPEG, PNG, or WebP file |
| `remix_video_id` | ID of a previous video to remix | Video ID string |

Note the two named model variants: **`sora-2`** and **`sora-2-pro`**.

Tip from Microsoft: the model follows instructions more reliably in shorter clips. For best results, consider generating two 4-second clips and stitching them together rather than a single 8-second clip.

### Test video generation in the playground

Steps (Foundry portal Video playground):
1. Navigate to your deployed Sora 2 model in the Foundry portal.
2. Select the **Playground** tab to access the video generation interface.
3. Enter your prompt describing the desired video.
4. Configure video settings (resolution and duration).
5. Select **Generate** to start video creation.

Video generation typically takes **1 to 5 minutes** depending on settings. The generated video appears on the page when ready.

Content moderation note: "The content generation APIs include a content moderation filter. If Azure OpenAI recognizes your prompt as harmful content, it won't return a generated video." Referenced doc: [Content filtering](/en-us/azure/ai-services/openai/concepts/content-filter).

The playground also offers **cURL code samples** prefilled per your settings, accessible via the **View code** button.

### Writing effective prompts

Think of prompting like briefing a cinematographer. Prompt anatomy:
- **Camera framing**: shot type (wide, medium, close-up) and angle
- **Subject description**: anchor the subject with distinctive details
- **Action**: describe movement in beats (small steps, gestures, pauses)
- **Lighting and palette**: mood via lighting direction and color anchors
- **Style**: establish aesthetic early (e.g., "1970s film" or "handheld documentary")

#### Weak vs. strong prompts (exact table from source)

| Weak prompt | Strong prompt |
| --- | --- |
| "A beautiful street at night" | "Wet asphalt, zebra crosswalk, neon signs reflecting in puddles" |
| "Person moves quickly" | "Cyclist pedals three times, brakes, and stops at crosswalk" |
| "Cinematic look" | "Anamorphic 2.0x lens, shallow DOF, volumetric light" |

#### Example prompt (verbatim from source)

```text
In a 90s documentary-style interview, an old Swedish man sits in a study 
and says, "I still remember when I was young."
```

Why it works: "90s documentary" sets style (camera/lighting/color choices follow); "old Swedish man sits in a study" gives subject/setting while allowing creative interpretation; dialogue gives the model specific words to sync with the character.

### Using reference images

Use `input_reference` to supply a visual reference. The model anchors the **first frame** on the image; the prompt defines what happens next.

Requirements:
- Image resolution **must match** the target video `size` (`1280x720` or `720x1280`)
- Supported formats: **JPEG, PNG, WebP**

### Remixing existing videos

The **remix** feature modifies specific aspects of an existing video while **preserving its core elements** — scene transitions, visual layout, overall structure. Useful for targeted adjustments without regenerating from scratch.

Steps:
1. Generate a video and note its **video ID** from the completed job.
2. Call the remix endpoint with the original video ID and an updated prompt.
3. Describe only the changes you want — keep modifications focused.

Best practices:
- Limit changes to **one clearly articulated adjustment**.
- Be specific: "same shot, switch to 85mm lens" or "same lighting, new palette: teal, sand, rust."
- Narrow, precise edits retain greater fidelity to the source material.

### Tips for better results
- **Keep it simple**: one clear camera move + one clear subject action per shot.
- **Use beats for timing**: e.g., "actor takes four steps to the window, pauses, and pulls the curtain" instead of "actor walks across the room."
- **Be consistent**: reuse phrasing for characters across shots for continuity.
- **Iterate**: small changes to camera, lighting, or action can shift outcomes dramatically; treat each generation as a creative variation — the second or third generation may be the best.

## Unit 4: Generate video in Python

Use the **OpenAI Python SDK** with your Sora 2 deployment in Microsoft Foundry. Video generation is asynchronous: **submit a job → poll for status → download the result**.

### Generate a video (three-step pattern: create, poll, download)

```python
import time

# Create the video generation job
video = client.videos.create(
    model="sora-2",
    prompt="A robot walks through a rainy city street at dusk, neon signs reflecting in puddles",
    size="1280x720",
    seconds="4",
)

print(f"Video creation started. ID: {video.id}")

# Poll for completion
while video.status not in ["completed", "failed", "cancelled"]:
    print(f"Status: {video.status}. Waiting...")
    time.sleep(20)
    video = client.videos.retrieve(video.id)

# Download when complete
if video.status == "completed":
    content = client.videos.download_content(video.id, variant="video")
    content.write_to_file("output.mp4")
    print("Video saved to output.mp4")
```

Key SDK methods/attributes:
- `client.videos.create(model=, prompt=, size=, seconds=, input_reference=)` — creates the async job, returns a video object with `.id` and `.status`
- `client.videos.retrieve(video.id)` — polls current job status
- `client.videos.download_content(video.id, variant="video")` — downloads the completed asset; `.write_to_file("output.mp4")` saves it
- `video.status` — one of `queued`, `in_progress`, `completed`, `failed`, `cancelled`
- `video.error` — inspect for details when a job's status is `failed`
- `client.videos.remix(video_id=, prompt=)` — creates a remix job from an existing video ID

### Generate video from a reference image

```python
video = client.videos.create(
    model="sora-2",
    prompt="The camera slowly pans across the landscape as clouds drift overhead",
    size="1280x720",
    seconds="4",
    input_reference=open("landscape.png", "rb"),
)
```

Important restriction (exam-relevant): **reference images containing human faces are currently rejected**. Use images of landscapes, objects, or animated characters instead.

### Remix an existing video

```python
video = client.videos.remix(
    video_id="video_abc123",
    prompt="Change the color palette to warm sunset tones",
)
```

### Job status values (exact table from source)

| Status | Description |
| --- | --- |
| `queued` | Job is waiting to be processed |
| `in_progress` | Video is being generated |
| `completed` | Video is ready for download |
| `failed` | Generation failed (check error details) |
| `cancelled` | Job was canceled |

When a job fails, check `video.error` for details about what went wrong.

### Key considerations (exam-relevant limits)
- **Rate limits**: you can run **up to two video creation jobs simultaneously**.
- **Job expiration**: completed videos are available for download for **24 hours**.
- **Resolution requirements**: reference images must match the target video resolution **exactly**.
- **Content filtering**: prompts are subject to content moderation; harmful content won't generate a video.

## Unit 5: Exercise — Generate video with Sora 2 in Microsoft Foundry

Hands-on lab (30 minutes, requires an Azure subscription — free trial includes credits for the first 30 days). The exercise guides you through: deploying the Sora 2 model, generating videos from text prompts, and using reference images for more control over video content. Launched via an external exercise link (go.microsoft.com fwlink); no additional technical content on the page itself beyond what's covered in Units 2–4.

## Unit 6: Module assessment (knowledge check)

The official knowledge-check unit poses these questions (topic areas only — used here to confirm which facts Microsoft considers most exam-critical; do not treat the option ordering below as the answer key):
1. What video durations does Sora 2 support? (Tests knowledge of the `seconds` parameter: `4`, `8`, or `12`.)
2. What is required when using a reference image with Sora 2? (Tests the `input_reference` resolution-match requirement.)
3. What is the remix feature used for in Sora 2? (Tests understanding of targeted edits vs. full regeneration.)

## Unit 7: Summary

Recap of what the module covered:
- Deploy a Sora 2 video generation model in Microsoft Foundry
- Write effective prompts describing camera framing, subject details, action, and lighting
- Use the Video playground to test video generation with different settings
- Generate videos from reference images and remix existing videos
- Build a Python application that creates videos programmatically using the OpenAI SDK

Core takeaway emphasized by Microsoft: "The asynchronous API pattern—submit a job, poll for status, download the result—enables you to integrate video generation into your applications." This is the single most exam-relevant architectural distinction versus (typically synchronous) image generation workflows covered in the prior module.

Further reading referenced: [Video generation with Sora](/en-us/azure/ai-services/openai/concepts/video-generation) in the Azure OpenAI documentation.
