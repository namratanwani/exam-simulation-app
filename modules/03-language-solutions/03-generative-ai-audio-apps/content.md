# Develop a speech-capable generative AI application

Source: https://learn.microsoft.com/en-us/training/modules/develop-generative-ai-audio-apps/

Module info: 7 Units, Intermediate level, roles: AI Engineer, product: Microsoft Foundry.

## Learning objectives

- Deploy speech-capable generative AI models in Microsoft Foundry.
- Use a generative AI model to transcribe speech.
- Use a generative AI model to synthesize speech.

Prerequisites: experience deploying generative AI models in Microsoft Foundry; programming experience.

## Exam relevance

Maps to:
- **Implement text analysis solutions (10–15%)** → "Implement speech solutions" → "Implement workflows to convert speech to text and text to speech for agentic interactions" and "Enable multimodal reasoning from audio inputs" — this module is specifically about using **generative (LLM-family) models**, not the classic Speech SDK, for speech-to-text and text-to-speech.
- **Implement generative AI and agentic solutions (30–35%)** → "Deploy and consume LLMs, small models, code models, and multimodal models" — covers deploying multimodal/audio-capable models from the Foundry model catalog.

**Key distinguishing factor (exam-critical):** This module uses **generative AI audio models (gpt-4o family via `AzureOpenAI` client / `client.audio.*`)**, which is architecturally different from the **Azure AI Speech SDK** (`SpeechConfig`, `SpeechRecognizer`, `SpeechSynthesizer`) covered in module 4 of this learning path. Both achieve speech-to-text/text-to-speech, but:
- Generative audio models (this module) are accessed through the **OpenAI-compatible `AzureOpenAI` client**, deployed like any other Foundry model, and are part of the **gpt-4o model family**.
- The Speech SDK/Speech resource (module 4) is a dedicated **Azure AI Speech** service with its own SDK, supports **custom speech models**, continuous recognition, real-time streaming via microphone, pronunciation assessment, etc.

## Unit 1: Introduction

Speech transcription and synthesis are useful in scenarios such as:
- Documenting spoken conversations in calls and meetings.
- Generating captions for videos or presentations.
- Creating audible user interfaces to improve application accessibility.
- Developing hands-free AI assistants that read text messages or emails aloud.

Module explores using **speech-capable generative AI models in Microsoft Foundry** to convert speech to text and text to speech.

## Unit 2: Choose a speech-capable model

**Microsoft Foundry Models** is a model catalog including generative AI models from multiple providers, with different capabilities optimized for different use cases. Use the **filter and search features in the Microsoft Foundry Portal** to find a suitable model.

Two common speech-capable use cases:
1. Generative AI models that **transcribe speech to text**.
2. Generative AI models that **synthesize text to speech**.

Microsoft Foundry provides models for both, including specialized speech-capable models from the **gpt-4o family** of OpenAI models.

Reference: Microsoft Foundry Models overview doc (`/en-us/azure/foundry/concepts/foundry-models-overview`).

## Unit 3: Transcribe speech (speech-to-text)

**Speech transcription (speech-to-text)**: submit audio content to a model → model responds with a text transcript.

**Models that support speech-to-text:**
- **gpt-4o-transcribe**
- **gpt-4o-mini-transcribe**
- **gpt-4o-transcribe-diarize** (implies speaker diarization capability — distinguishing this variant from the other two)

> Note: model availability varies by region — check the model regional availability table in Foundry docs.

### Using a speech-to-text model

Use the **`AzureOpenAI`** client (from the `openai` SDK) to connect to your Microsoft Foundry resource endpoint, then upload an audio file for transcription.

```python
from openai import AzureOpenAI
from pathlib import Path

# Create an AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=YOUR_FOUNDRY_ENDPOINT,
    api_key=YOUR_FOUNDRY_KEY,
    api_version="2025-03-01-preview"
)

# Get the audio file
file_path = Path("speech.mp3")
audio_file = open(file_path, "rb")

# Use the model to transcribe the audio file
transcription = client.audio.transcriptions.create(
    model=YOUR_MODEL_DEPLOYMENT,
    file=audio_file,
    response_format="text"
)

print(transcription)
```

Key API: **`client.audio.transcriptions.create(model=..., file=..., response_format="text")`**. `api_version` used: `"2025-03-01-preview"`.

## Unit 4: Synthesize speech (text-to-speech)

**Speech synthesis (text-to-speech)**: the reverse of speech-to-text — submit text to a model → model returns an audio stream of vocalized text.

**Models that support text-to-speech:**
- **gpt-4o-tts**
- **gpt-4o-mini-tts**

> Note: model availability varies by region (same regional-availability table reference as speech-to-text).

### Using a text-to-speech model

Also uses the **`AzureOpenAI`** client, but calls `client.audio.speech.with_streaming_response.create(...)`.

```python
from openai import AzureOpenAI
from pathlib import Path

# Create an AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=YOUR_FOUNDRY_ENDPOINT,
    api_key=YOUR_FOUNDRY_KEY,
    api_version="2025-03-01-preview"
)

# Path for audio output file
speech_file_path = Path("output_speech.wav")

# Generate speech and save to file
with client.audio.speech.with_streaming_response.create(
            model=YOUR_MODEL_DEPLOYMENT,
            voice="alloy",
            input="This speech was AI-generated!",
            instructions="Speak in an upbeat, excited tone.",
    ) as response:
    response.stream_to_file(speech_file_path)

print(f"Speech generated and saved to {speech_file_path}")
```

Key API: **`client.audio.speech.with_streaming_response.create(model=..., voice=..., input=..., instructions=...)`** used as a context manager, then **`response.stream_to_file(speech_file_path)`**.

Parameters: `model` (deployment name), `voice` (example: `"alloy"`), `input` (text to speak), `instructions` (natural-language tone/style directive, e.g., `"Speak in an upbeat, excited tone."`). Output saved as a `.wav` file in the example.

**Exam-relevant distinguishing detail:** the `instructions` parameter is unique to the generative TTS model approach — it lets you steer delivery style/tone via natural language, which is not how the classic Azure AI Speech SDK's `SpeechSynthesizer` (SSML-based prosody control) works.

## Unit 5: Exercise — Use speech-capable generative AI models

Hands-on exercise (~30 minutes): implement speech transcription and synthesis using generative AI models in Microsoft Foundry. Requires an Azure subscription (new accounts get free credits for the first 30 days). Delivered via external lab launch link.

## Unit 6: Module assessment

Standard graded quiz — interactive only, no extractable content.

## Unit 7: Summary

Recap: you learned about speech-capable AI models and how to use Microsoft Foundry to create generative AI solutions that:
- Transcribe speech to text.
- Synthesize speech from text.

Further reading: **Audio models** section of the Foundry "models sold directly by Azure" doc (`/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai#audio-models`).
