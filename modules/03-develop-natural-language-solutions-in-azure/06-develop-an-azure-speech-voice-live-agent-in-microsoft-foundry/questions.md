# Practice questions — Develop an Azure Speech Voice Live Agent in Microsoft Foundry

## Introduction & Voice Live API overview

**Q1.** What core problem does the Voice Live API solve for developers building voice agents, compared to manually chaining speech-to-text, an LLM, and text-to-speech themselves?
A. It only provides text-to-speech and requires developers to build STT and orchestration separately by hand
B. It enables low-latency, high-quality speech-to-speech interactions and eliminates the need to manually orchestrate multiple separate components
C. It replaces the need for any Azure subscription or resource provisioning at all, using a free public tier
D. It only works with Azure custom voices, not OpenAI voices, contrary to what the module's voice options list actually shows
**Answer:** B — Voice Live is described as an integrated real-time pipeline for speech-to-speech interaction, removing the need to manually wire together separate STT/LLM/TTS components.

**Q2.** Which transport protocol does the Voice Live API use for real-time, bidirectional communication?
A. HTTP long polling
B. WebSocket connections
C. SMTP (used for message-queue-style delivery)
D. FTP (used for bulk file transfer)
**Answer:** B — The Voice Live API uses WebSocket connections with JSON-formatted client/server events.

**Q3.** Into which two categories does the module divide the Voice Live API's JSON-formatted events?
A. Sync events and async events, matching the SDK's dual programming model
B. Client events (client → server) and server events (server → client)
C. Session events and conversation events only, with no other grouping
D. Public events and private/internal events, exposed differently by the SDK
**Answer:** B — "Events are split into client events (client → server) and server events (server → client)."

**Q4.** Which event, per the module's server event examples, indicates that a new conversation item (e.g., a turn) has been added?
A. `response.done` (signals the full response finished, not item creation)
B. `conversation.item.created`
C. `session.updated` (confirms a session config change, not a new item)
D. `input_audio_buffer.append`
**Answer:** B — `conversation.item.created` is listed among the server event examples as signaling a new conversation item was added.

**Q5.** Which audio formats are explicitly mentioned as supported by the Voice Live API's real-time audio processing?
A. MP3 and FLAC (common file-based compressed formats)
B. PCM16 and G.711
C. WAV only, per the module's real-time audio format table
D. AAC and OGG (common streaming-media codecs)
**Answer:** B — PCM16 and G.711 are the audio formats explicitly named for Voice Live real-time audio processing.

**Q6.** Per the "Advanced voice options" key feature, which two categories of voices does the Voice Live API support?
A. OpenAI voices and Azure custom voices
B. Only Azure custom voices, since OpenAI voices require a separate resource
C. Only OpenAI voices, since custom voices aren't supported in real-time mode
D. Third-party voices via plugins only, not first-party voice catalogs
**Answer:** A — The module's key features list "Advanced voice options: OpenAI voices and Azure custom voices."

**Q7.** For production applications connecting to the Voice Live API, which authentication method is recommended, and what role must be assigned?
A. API key via query string; no role needed since resource keys bypass RBAC checks entirely
B. Microsoft Entra ID (keyless) authentication; the Cognitive Services User role must be assigned to the account or managed identity
C. Basic auth with username/password; Contributor role required on the whole resource group
D. Anonymous access; no authentication required for public preview endpoints in any region
**Answer:** B — Entra ID (keyless) is recommended, requiring the Cognitive Services User role, with a token generated using scope `https://ai.azure.com/.default` (or legacy `https://cognitiveservices.azure.com/.default`).

**Q8.** Which API key authentication option for the Voice Live API is explicitly stated as NOT available in a browser environment?
A. The `api-key` query string parameter, encrypted over the wss:// connection
B. The `api-key` connection header on the prehandshake connection
C. Microsoft Entra ID token authentication via a bearer token
D. All API key options are unavailable in browsers, including query string
**Answer:** B — The connection-header approach for API keys isn't available in browser environments; the query-string parameter option is available (and is encrypted over https/wss).

**Q9.** Which WebSocket endpoint pattern should you use when connecting to Voice Live through a Microsoft Foundry project to implement an agent (as opposed to connecting directly to a model)?
A. `wss://<resource-name>.cognitiveservices.azure.com/voice-live/realtime?api-version=2025-10-01`
B. `wss://<resource-name>.services.ai.azure.com/voice-live/realtime?api-version=2025-10-01`
C. `https://<resource-name>.openai.azure.com/voice-live` (the model-direct OpenAI endpoint)
D. `wss://<resource-name>.search.windows.net/voice-live` (an Azure Cognitive Search endpoint)
**Answer:** B — The project connection endpoint (`services.ai.azure.com`) is used for agent implementations, distinguishing it from the model connection endpoint (`cognitiveservices.azure.com`).

**Q10.** Which WebSocket endpoint pattern is used for a **model connection** (direct model access, bypassing the Foundry Agent Service)?
A. `wss://<resource-name>.services.ai.azure.com/voice-live/realtime?api-version=2025-10-01`
B. `wss://<resource-name>.cognitiveservices.azure.com/voice-live/realtime?api-version=2025-10-01`
C. `https://<resource-name>.openai.azure.com/voice-live/realtime` (a plain HTTPS, non-WebSocket URL)
D. `wss://<resource-name>.foundry.azure.com/voice-live` (a fabricated-looking Foundry-branded domain)
**Answer:** B — The model connection endpoint uses `cognitiveservices.azure.com`, distinguished from the project connection's `services.ai.azure.com`; only the query parameters differ (`model` for direct access vs. `agent_id` + `project_id` for the Agent Service).

**Q11.** Which event is typically the FIRST one sent by the caller on a newly established Voice Live session, and what does it control?
A. `response.create` — triggers response generation immediately for the session
B. `session.update` — controls voice type, modalities, turn detection, and audio formats
C. `conversation.item.created` — creates the first conversation turn
D. `input_audio_buffer.append` — starts streaming audio immediately
**Answer:** B — `session.update` is typically the first event, configuring session-wide settings like modalities, voice, turn detection, and audio formats.

**Q12.** In the module's `session.update` example, what values are set for `turn_detection`'s `threshold`, `prefix_padding_ms`, and `silence_duration_ms`?
A. `0.5`, `300`, `500`
B. `0.8`, `500`, `300`
C. `1.0`, `100`, `1000`
D. `0.3`, `200`, `400`
**Answer:** A — The sample `azure_semantic_vad` config shows `"threshold": 0.5, "prefix_padding_ms": 300, "silence_duration_ms": 500`.

**Q13.** What values does the module's `session.update` example use for `temperature` and `max_response_output_tokens`?
A. `temperature: 0.8`, `max_response_output_tokens: "inf"`
B. `temperature: 1.0`, `max_response_output_tokens: 4096`
C. `temperature: 0.2`, `max_response_output_tokens: "auto"`
D. `temperature: 0.8`, `max_response_output_tokens: 2048`
**Answer:** A — The sample shows `"temperature": 0.8, "max_response_output_tokens": "inf"`.

**Q14.** What sampling rate is specified for `input_audio_sampling_rate` in the module's `session.update` example?
A. 16000
B. 24000
C. 44100
D. 8000
**Answer:** B — The sample sets `"input_audio_sampling_rate": 24000`.

**Q15.** Which turn-detection setting type does the module recommend for intelligent turn detection and improved conversational flow?
A. `fixed_silence_timer`
B. `manual_push_to_talk`
C. `azure_semantic_vad`
D. `client_side_polling`
**Answer:** C — Azure semantic VAD (voice activity detection) is recommended for intelligent turn detection.

**Q16.** What benefit does enabling `input_audio_noise_reduction` provide, beyond simply making audio sound cleaner to the end user?
A. It reduces the WebSocket connection's cost per token by compressing frames
B. It improves VAD accuracy and model performance by filtering the input audio
C. It automatically translates speech into other languages
D. It disables echo cancellation to reduce processing overhead
**Answer:** B — The module explicitly notes noise reduction improves VAD accuracy and model performance, not just perceived audio quality.

**Q17.** Which three client-side operations manage the input audio buffer during Voice Live's real-time audio processing?
A. append, commit, clear
B. push, pop, flush
C. open, stream, close
D. buffer, send, ack
**Answer:** A — The module states: "Client events: append (add audio bytes to input buffer), commit (process buffer for transcription/response), clear (remove buffered audio)."

**Q18.** Which technology is used for avatar streaming integration in the Voice Live API, and which event initiates the avatar connection?
A. gRPC; `avatar.start` (a streaming-RPC-based initiation event)
B. WebRTC; `session.avatar.connect` (providing the client's SDP offer)
C. WebSocket only; `session.update` (reusing the general session config event)
D. RTMP; `avatar.stream.begin` (a media-streaming-protocol event name)
**Answer:** B — Avatar streaming uses WebRTC, initiated via the `session.avatar.connect` event with the client's SDP offer.

**Q19.** Besides video resolution, bitrate, and codec, what animation outputs does the module mention for avatar streaming configuration?
A. Blendshapes and visemes
B. Skeletal rigs and morph targets
C. Subtitles and closed captions
D. Lip-sync waveforms only
**Answer:** A — The module lists "animation outputs (blendshapes, visemes)" as part of avatar streaming configuration.

## Voice Live Python SDK

**Q20.** As of version 1.0.0 of the Azure AI Voice Live client library for Python, what is true about its API style?
A. It supports both sync and async patterns equally, chosen at connection time
B. It is async-only; the synchronous API is deprecated
C. It is sync-only; async support was removed in this release
D. It requires callback-based (non-async, non-sync) programming exclusively
**Answer:** B — The SDK is async-only as of v1.0.0, with the synchronous API deprecated in favor of async/await exclusively.

**Q21.** Why is proper event handling — specifically responding to a "user started speaking" event — critical in a Voice Live client application?
A. It has no functional impact on the session at all, only cosmetic logging value useful for debugging
B. If the client doesn't stop/cancel agent audio playback on user interruption, the client continues playing the agent's last response, causing the agent to "talk over" the user
C. It's required only for text modality sessions, and can safely be skipped for audio modality sessions
D. It only affects avatar video rendering quality, not the underlying audio playback behavior at all
**Answer:** B — Without immediately cancelling playback on detecting user speech (interruption), stale agent audio keeps playing, creating a "talking over" experience until the interrupt is processed server-side.

**Q22.** In the Voice Live Python SDK, which server event type indicates that a new chunk of the agent's spoken audio response has arrived and should be played?
A. `SESSION_UPDATED`
B. `RESPONSE_AUDIO_DELTA`
C. `INPUT_AUDIO_BUFFER_SPEECH_STOPPED`
D. `ERROR` (reports failures, not audio chunks)
**Answer:** B — `RESPONSE_AUDIO_DELTA` events deliver incremental audio chunks (`event.delta`) for playback as the response streams in.

**Q23.** In the module's minimal session example, which classes from `azure.ai.voicelive.models` are used to build and update a session?
A. `RequestSession`, `Modality`, `InputAudioFormat`/`OutputAudioFormat`, `ServerVad`
B. `SessionConfig`, `AudioFormat`, `VoiceType`, `TurnDetector`
C. `LiveSession`, `Modalities`, `AudioCodec`, `VADConfig` (plausible-sounding but unused names)
D. `VoiceSession`, `Format`, `Voice`, `Detection` (also plausible-sounding but unused names)
**Answer:** A — The module states the minimal session example uses `RequestSession`, `Modality`, `InputAudioFormat`/`OutputAudioFormat`, and `ServerVad` from `azure.ai.voicelive.models`, applied via `conn.session.update(session=session)`.

**Q24.** In the Voice Live Python SDK's `connect()` code sample (both API key and Entra ID versions), what value is passed for the `model` parameter?
A. `"gpt-4o"`
B. `"gpt-4o-realtime-preview"`
C. `"whisper-1"`
D. `"voice-live-1"`
**Answer:** A — Both code samples call `connect(endpoint=..., credential=..., model="gpt-4o")`.

## Create a Voice Live agent

**Q25.** What is a key advantage of connecting Voice Live to a Microsoft Foundry **agent** rather than connecting directly to a bare model?
A. Agents are always cheaper to run than direct model connections, since billing is agent-scoped
B. Agent instructions/configuration are encapsulated within the agent itself, so conversational flows can be updated without changing client code, and connecting only requires the agent ID
C. Agents cannot support avatar streaming at all; only direct model connections can enable avatars
D. Agents remove the need for any authentication, since the agent ID itself acts as a credential
**Answer:** B — Encapsulating logic in the agent (rather than session code) allows updating behavior server-side without client code changes, and the agent ID alone drives the connection with settings handled internally.

**Q26.** In the Foundry portal's agent playground, which of the following are configurable "voice mode" settings? (Choose two.)
A. Language, and VAD/audio enhancement settings under Advanced settings
B. Voice (with tone/speaking-rate controls), and Interim response (speak while waiting for the model)
C. The agent's underlying Azure subscription ID
D. The Azure region's default currency
**Answer:** A, B — Language, Advanced settings (VAD, audio enhancement), Voice (with tone/rate), Interim response, and Avatar are all configurable in the playground's voice mode.

**Q27.** When creating a Voice Live-enabled agent via code using the Foundry SDK, where is the Voice Live session configuration (voice, turn detection, noise reduction, etc.) attached?
A. As a separate session object created at runtime, entirely unrelated to the persisted agent definition
B. As metadata on the agent version, using keys such as `microsoft.voice-live.configuration`
C. As an environment variable read only by the client application at process startup
D. It cannot be configured via code at all — only through the portal playground's voice mode UI
**Answer:** B — The Voice Live config is serialized to JSON and attached as agent metadata (e.g., `microsoft.voice-live.configuration`), not passed as a separate runtime session object.

**Q28.** Agent metadata values are limited to 512 characters. What technique does the module's example use to store a larger Voice Live JSON configuration as agent metadata?
A. Compressing the JSON with gzip before storing it, then decompressing it client-side on read
B. Splitting the configuration into multiple metadata keys (e.g., `microsoft.voice-live.configuration`, `.configuration.1`, `.configuration.2`, ...), each holding up to 512 characters, and reassembling them
C. Storing the configuration in Azure Blob Storage and referencing it by URL in a single metadata key instead
D. Truncating the configuration to fit the 512-character limit and accepting the resulting data loss
**Answer:** B — The `chunk_config()` helper splits the JSON string into ≤512-character chunks across multiple metadata keys, working around the per-value metadata size limit.

**Q29.** According to the recommended client application pattern, which two custom classes are suggested to structure a Voice Live client application in Python?
A. `SessionManager` and `TokenProvider` (a credential-focused split, per this pattern)
B. `VoiceAssistant` (agent config, session setup, event processing) and `AudioProcessor` (mic/speaker I/O)
C. `WebSocketClient` and `JSONParser` (a transport-focused split, per this pattern)
D. `ModelClient` and `PromptBuilder` (a model-configuration-focused split, per this pattern)
**Answer:** B — The recommended pattern encapsulates agent/session/event logic in a `VoiceAssistant` class and audio I/O in a separate `AudioProcessor` class.

**Q30.** In the reference client implementation, what action does the code take upon receiving an `INPUT_AUDIO_BUFFER_SPEECH_STARTED` event?
A. It ignores the event entirely and continues audio playback uninterrupted throughout
B. It clears the playback queue (to stop any currently playing agent audio) since the user has started speaking
C. It immediately disconnects the WebSocket session and requires the client to reconnect
D. It switches the session from audio modality to text-only modality for the remainder of the turn
**Answer:** B — This event signals the user has started talking; the client clears its playback queue to prevent the agent from talking over the user (interrupt handling).

**Q31.** Which authentication approach does the recommended Voice Live client application pattern use to connect to an agent in a Microsoft Foundry project?
A. Anonymous/no authentication
B. Microsoft Entra ID authentication
C. Basic authentication with a shared password
D. SAS tokens generated by Azure Blob Storage
**Answer:** B — The recommended pattern uses Microsoft Entra ID authentication (e.g., via `AzureCliCredential` in the sample) to connect to the agent in a Foundry project.

**Q32.** Besides the Python SDK demonstrated in this module's exercise, which other language-specific client library is mentioned as available for building similar Voice Live applications?
A. Azure VoiceLive client library for .NET
B. Azure VoiceLive client library for Go
C. Azure VoiceLive client library for Rust
D. Azure VoiceLive client library for PHP
**Answer:** A — The module explicitly mentions the Azure VoiceLive client library for .NET as an alternative to the Python-based exercise.

## Scenario questions

**Q33.** You're building a production voice agent client as a server-side Python application and want to avoid embedding a static API key. Which authentication approach and `connect()` pattern should you use?
A. `AzureKeyCredential` with the `api-key` connection header, since it's the simplest option to wire up
B. `DefaultAzureCredential` from `azure.identity.aio`, passed as the `credential` to `connect()`, requiring the Cognitive Services User role
C. The `api-key` query string parameter, hardcoded directly into source control for convenience
D. No authentication is needed for server-side apps behind a corporate firewall or VPN
**Answer:** B — Microsoft Entra ID authentication via `DefaultAzureCredential` is the module's recommended approach for production, requiring the Cognitive Services User role rather than a static key.

**Q34.** A user interrupts the agent mid-response. Which server event should trigger the client to stop audio playback, and what must the client do in response, per this module's reference implementation?
A. `RESPONSE_AUDIO_DELTA`; append more audio to the queue
B. `INPUT_AUDIO_BUFFER_SPEECH_STARTED`; clear the playback queue immediately
C. `SESSION_UPDATED`; restart the WebSocket connection and re-send `session.update`
D. `ERROR`; log the error and continue playback unchanged
**Answer:** B — `INPUT_AUDIO_BUFFER_SPEECH_STARTED` signals the user has started talking; the reference implementation clears the playback queue immediately to stop the agent from talking over the user.

**Q35.** You want a voice agent whose conversational behavior can be updated by another team without redeploying the client application, using a Foundry agent plus Voice Live. Given the 512-character metadata value limit, how should you store a large Voice Live configuration?
A. Store it in a single metadata key and truncate the content to fit within the 512-character limit
B. Split it across multiple metadata keys (`microsoft.voice-live.configuration`, `.configuration.1`, `.configuration.2`, ...), each ≤512 characters, and reassemble them
C. Store it in the agent's `instructions` field instead of metadata, since instructions have no size limit
D. Voice Live configuration can't be attached to an agent at all; it must live entirely in client code
**Answer:** B — The `chunk_config()` helper works around the 512-character metadata value limit by splitting the JSON config across multiple sequentially-numbered metadata keys.

**Q36.** You need to enable an avatar and ensure the model receives clean audio despite mobile background noise. Which two `session.update` configuration blocks from this module would you combine?
A. `input_audio_noise_reduction` (`azure_deep_noise_suppression`) + `session.avatar.connect` (with the client's SDP offer)
B. `turn_detection` (`azure_semantic_vad`) alone, since it also filters and handles background noise
C. The avatar block alone; noise reduction is automatic and entirely unconfigurable in this SDK
D. `output_audio_format` alone, since output bitrate settings control input noise levels
**Answer:** A — Noise reduction is configured via `input_audio_noise_reduction` in a `session.update` event, while the avatar connection is a separate `session.avatar.connect` event carrying the client's SDP offer — both are needed together for this scenario.
