# Develop an Azure Speech Voice Live Agent in Microsoft Foundry

Source: https://learn.microsoft.com/en-us/training/modules/develop-voice-live-agent/

## Learning objectives

After completing this module, you'll be able to:
- Describe the core components and capabilities of the Azure Speech Voice Live platform.
- Use the Voice Live API to create conversational AI solutions.
- Use the Voice Live SDK to build and deploy conversational AI solutions.
- Integrate Microsoft Foundry agents with the Voice Live API to create voice agents.

**Prerequisites**: Programming experience (Python/JavaScript/C#); familiarity with RESTful APIs and webhooks; basic Azure/cloud concepts.

## Exam relevance

Maps to **Learning Path 3 — Develop natural language solutions in Azure**. Supports:
- **"Implement text analysis solutions" (10–15%)** → *"Implement speech solutions"*: *"Implement workflows to convert speech to text and text to speech for agentic interactions"*; *"Integrate speech as an agent modality"*; *"Enable multimodal reasoning from audio inputs"*.
- **"Implement generative AI and agentic solutions" (30–35%)** → *"Build agents by using Foundry"*: integrating agent tools/modalities.

Voice Live is the exam's canonical example of real-time, low-latency, bidirectional speech-to-speech agent interaction (as opposed to the turn-based speech-to-text → LLM → text-to-speech pattern covered elsewhere).

## Introduction

The **Voice Live API** (part of **Azure Speech in Foundry Tools**) enables **low-latency, high-quality speech-to-speech interactions** for voice agents. It's designed for scalable, efficient voice-driven experiences and **eliminates the need to manually orchestrate multiple separate components** (i.e., you don't have to hand-wire STT → LLM → TTS yourself — Voice Live handles this as an integrated real-time pipeline).

## Explore the Azure Voice Live API

### Key features
- Real-time, **bidirectional communication over WebSocket connections**.
- **JSON-formatted events** manage conversations, audio streams, responses.
- Events are split into **client events** (client → server) and **server events** (server → client).
- Real-time audio processing supporting multiple formats: **PCM16**, **G.711**.
- Advanced voice options: **OpenAI voices** and **Azure custom voices**.
- **Avatar integration** using **WebRTC** for video/animation.
- Built-in **noise reduction** and **echo cancellation**.

> Voice Live API is **optimized for Microsoft Foundry resources** — recommended for full feature availability and best integration.

### Authentication (two methods)
- **Microsoft Entra ID (keyless, recommended)** — token-based. Requires the **Cognitive Services User** role assigned to the user/managed identity. Token generated via Azure CLI/SDKs with scope `https://ai.azure.com/.default` (or legacy `https://cognitiveservices.azure.com/.default`). Used as `Bearer <token>` in the `Authorization` header.
- **API key** — either:
  - `api-key` **connection header** on the prehandshake connection (⚠️ **not available in a browser environment**).
  - `api-key` **query string parameter** on the request URI (encrypted when using https/wss).

### WebSocket endpoints
- **Project connection** (implementing an agent): `wss://<resource-name>.services.ai.azure.com/voice-live/realtime?api-version=2025-10-01`
- **Model connection** (direct model access): `wss://<resource-name>.cognitiveservices.azure.com/voice-live/realtime?api-version=2025-10-01`
- Endpoint format is the same for all models; only the query parameters differ: `model` (direct), or `agent_id` + `project_id` (Agent Service).

### Key events
**Client events** (examples):
- `session.update` — modify session configuration.
- `input_audio_buffer.append` — add audio data to the buffer.
- `response.create` — trigger response generation via model inference.

**Server events** (examples):
- `session.updated` — confirms session config change.
- `response.done` — response generation complete.
- `conversation.item.created` — new conversation item added.

### Session configuration (`session.update`)
Typically the **first event** sent on a new session. Controls modalities, voice, instructions, audio format/sampling rate, turn detection, temperature, `max_response_output_tokens`, etc. Example:
```json
{
  "type": "session.update",
  "session": {
    "modalities": ["text", "audio"],
    "voice": {"type": "openai", "name": "alloy"},
    "instructions": "You are a helpful assistant. Be concise and friendly.",
    "input_audio_format": "pcm16",
    "output_audio_format": "pcm16",
    "input_audio_sampling_rate": 24000,
    "turn_detection": {
      "type": "azure_semantic_vad",
      "threshold": 0.5,
      "prefix_padding_ms": 300,
      "silence_duration_ms": 500
    },
    "temperature": 0.8,
    "max_response_output_tokens": "inf"
  }
}
```
**Tip**: use **Azure semantic VAD** (voice activity detection) for intelligent turn detection and improved conversational flow.

### Real-time audio processing
Client events: **append** (add audio bytes to input buffer), **commit** (process buffer for transcription/response), **clear** (remove buffered audio).

Noise reduction / echo cancellation config example:
```json
{
  "type": "session.update",
  "session": {
    "input_audio_noise_reduction": {"type": "azure_deep_noise_suppression"},
    "input_audio_echo_cancellation": {"type": "server_echo_cancellation"}
  }
}
```
Noise reduction improves **VAD accuracy** and model performance by filtering input audio.

### Avatar streaming
WebRTC-based; configure via `session.avatar.connect` event (providing the client's SDP offer), plus video resolution/bitrate/codec and animation outputs (blendshapes, visemes).
```json
{"type": "session.avatar.connect", "client_sdp": "<client_sdp>"}
```

## Explore the AI Voice Live client library for Python

The **Azure AI Voice Live client library for Python** (`azure-ai-voicelive`) is a real-time speech-to-speech client: opens a WebSocket session to stream mic audio and receive server events.

> **As of v1.0.0, the SDK is async-only** — the synchronous API is deprecated. All examples use async/await.

### Authentication in code
API key:
```python
import asyncio
from azure.core.credentials import AzureKeyCredential
from azure.ai.voicelive import connect

async def main():
    async with connect(
        endpoint="your-endpoint",
        credential=AzureKeyCredential("your-api-key"),
        model="gpt-4o"
    ) as connection:
        pass

asyncio.run(main())
```
Microsoft Entra (recommended for production):
```python
from azure.identity.aio import DefaultAzureCredential
from azure.ai.voicelive import connect

credential = DefaultAzureCredential()
async with connect(endpoint="your-endpoint", credential=credential, model="gpt-4o") as connection:
    ...
```

### Handling events
Proper event handling is critical — e.g., when a user interrupts the agent, the client must **immediately cancel agent audio playback**, or the agent keeps "talking over" the user until the interrupt is processed server-side.
```python
async for event in connection:
    if event.type == ServerEventType.SESSION_UPDATED:
        ...  # Start audio capture
    elif event.type == ServerEventType.INPUT_AUDIO_BUFFER_SPEECH_STARTED:
        ...  # Stop playback / cancel current response
    elif event.type == ServerEventType.RESPONSE_AUDIO_DELTA:
        audio_bytes = event.delta  # Play chunk
    elif event.type == ServerEventType.ERROR:
        print(f"Error: {event.error.message}")
```

### Minimal session example
Uses `RequestSession`, `Modality`, `InputAudioFormat`/`OutputAudioFormat`, `ServerVad` from `azure.ai.voicelive.models`, and `conn.session.update(session=session)`.

## Create a Voice Live agent

Connecting Voice Live to a **Microsoft Foundry agent** (rather than a bare model) has advantages:
- Instructions/config are **encapsulated in the agent itself**, not the session code.
- Agents support **complex logic/behaviors** — update conversational flows without changing client code.
- Streamlined integration: **agent ID** used to connect; settings handled internally.
- Separating agent logic from voice implementation improves maintainability/scalability across multiple conversational experiences.

### No-code path: agent playground
Enable **voice mode** on an agent in the Microsoft Foundry portal; configure via the Configuration pane:
- **Language**
- **Advanced settings**: VAD settings (interruption/end-of-speech detection), audio enhancement (background noise/quality)
- **Voice**: specific voice + tone/speaking-rate controls
- **Interim response**: agent can speak while waiting for the model's full response
- **Avatar**: optional visual avatar

### Code path
Create the agent via the Foundry SDK (`AIProjectClient`, `PromptAgentDefinition`) and attach **Voice Live configuration as agent metadata** (not session code):
```python
agent = project_client.agents.create_version(
    agent_name="AGENT_NAME",
    definition=PromptAgentDefinition(model="MODEL_DEPLOYMENT_NAME", instructions="..."),
    metadata=chunk_config(json.dumps(voice_live_config))
)
```
> **Metadata values have a 512-character limit** — the module's `chunk_config()` helper splits a larger Voice Live JSON config across multiple metadata keys (`microsoft.voice-live.configuration`, `.configuration.1`, `.configuration.2`, ...) to work around this. **This 512-char metadata chunking limit is a specific, exam-testable detail.**

### Client application pattern (recommended)
1. Connect to the agent (Microsoft Entra ID auth to the Foundry project).
2. Configure audio hardware input/output.
3. Establish the Voice Live session.
4. Monitor audio systems for activity.
5. Process events (user speech input, agent responses).

Recommended code structure: a custom **`VoiceAssistant`** class (agent config, session setup, event processing) + a custom **`AudioProcessor`** class (mic/speaker I/O, e.g. via **PyAudio**). Key behaviors demonstrated in the reference implementation:
- On `SESSION_UPDATED` → start audio capture.
- On `INPUT_AUDIO_BUFFER_SPEECH_STARTED` (user starts talking) → **clear the playback queue** to stop the agent "talking over" the user (interrupt handling).
- On `RESPONSE_AUDIO_DELTA` → queue audio chunk for playback.
- On `ERROR` → surface `event.error.message`.

## Exercise (lab, hands-on)
30-minute lab: create a voice agent using the Voice Live tool in Azure Speech in Foundry Tools, test it in the agent playground, then implement a Python client application for a voice-based conversation. Note: an equivalent **Azure VoiceLive client library for .NET** also exists for non-Python implementations. Requires an Azure subscription and a microphone/speaker-capable audio device.

## Summary
Covered: Voice Live API features (WebSocket connections, speech recognition, TTS, avatar streaming); the Azure AI Voice Live Python SDK for real-time speech-to-speech apps (client library setup, session management); implementing event handlers for dynamic responses/real-time audio; building and testing a Python (Flask-based, per the lab) voice application integrated with Azure resources.

### Further reading
- What is the Speech service?
- How to customize Voice Live input and output
