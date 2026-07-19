# Practice questions — Develop a speech-capable generative AI application

## Unit 1–2: Introduction / Choose a speech-capable model

**Q1.** Where do you go in Microsoft Foundry to find and filter speech-capable generative AI models?
A. The Azure AI Speech resource blade in the Azure portal
B. The Microsoft Foundry Models catalog, using its filter and search features
C. The Azure Marketplace listing for third-party AI add-ons
D. The Cognitive Services multi-service resource page in the classic Azure portal blade
**Answer:** B — The module states: "Microsoft Foundry Models is a model catalog... To find a suitable model, you can use the filter and search features in the Microsoft Foundry Portal."

**Q2.** Which family of OpenAI models does this module identify as providing specialized speech-capable (transcription and synthesis) models in Microsoft Foundry?
A. gpt-3.5-turbo family
B. gpt-4o family
C. text-embedding family
D. whisper-standalone family
**Answer:** B — "Microsoft Foundry provides models that support both of these use-cases, including specialized speech-capable models from the gpt-4o family of OpenAI models."

**Q3.** Which two generative AI use cases does this module identify for speech-capable models?
A. Transcribing speech to text
B. Translating text between languages
C. Synthesizing text to speech
D. Detecting spoken language sentiment
**Answer:** A, C — The module explicitly lists two common use cases: generative models that transcribe speech to text and generative models that synthesize text to speech.

**Q4.** Which of the following are explicitly listed in this module's introduction as usage scenarios for speech transcription/synthesis? (Choose three.)
A. Documenting spoken conversations in calls and meetings
B. Generating captions for videos or presentations
C. Real-time language translation during video calls
D. Developing hands-free AI assistants that read text messages or emails aloud
E. Automatically generating video content from text prompts
**Answer:** A, B, D — The module lists: documenting spoken conversations, generating captions, creating audible/accessible UIs, and developing hands-free AI assistants that read messages or emails aloud. Real-time translation and video generation are not mentioned.

**Q5.** Which capabilities does this module identify as unique to the classic Azure AI Speech SDK (covered in a different module of this learning path), rather than to the generative gpt-4o audio models covered here?
A. Custom speech models, continuous recognition, real-time microphone streaming, and pronunciation assessment
B. The ability to transcribe an audio file at all, regardless of resource type
C. Support for connecting via the `AzureOpenAI` client and its bearer-token authentication
D. Deployment through the Microsoft Foundry model catalog alongside other chat models
**Answer:** A — The module's exam-relevance note states the Speech SDK/Speech resource "supports custom speech models, continuous recognition, real-time streaming via microphone, pronunciation assessment, etc.," distinguishing it from the generative audio models in this module.

## Unit 3: Transcribe speech

**Q6.** Which model is specifically designed to include speaker diarization when transcribing audio, per this module?
A. gpt-4o-transcribe (standard)
B. gpt-4o-mini-transcribe
C. gpt-4o-transcribe-diarize
D. gpt-4o-tts (text-to-speech model)
**Answer:** C — The module lists `gpt-4o-transcribe-diarize` as one of three speech-to-text models, distinguished by name from the plain `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`.

**Q7.** Which of the following are listed in this module as speech-to-text capable models? (Choose two.)
A. gpt-4o-transcribe
B. gpt-4o-mini-transcribe
C. gpt-4o-tts
D. gpt-4o-mini-tts
**Answer:** A, B — gpt-4o-transcribe, gpt-4o-mini-transcribe, and gpt-4o-transcribe-diarize are the speech-to-text models; gpt-4o-tts and gpt-4o-mini-tts are text-to-speech models instead.

**Q8.** Which client class from the OpenAI SDK is used to connect to a Microsoft Foundry resource endpoint for speech transcription?
A. `SpeechClient`
B. `AzureOpenAI`
C. `FoundryAudioClient`
D. `TextAnalyticsClient`
**Answer:** B — Code sample: `from openai import AzureOpenAI` and `client = AzureOpenAI(azure_endpoint=..., api_key=..., api_version=...)`.

**Q9.** Which method call submits an audio file for transcription using the `AzureOpenAI` client?
A. `client.audio.transcribe(file=audio_file)`, a shorthand added in later SDK versions
B. `client.audio.transcriptions.create(model=..., file=audio_file, response_format="text")`
C. `client.speech.recognize(audio=audio_file)`, mirroring the classic Speech SDK's method name
D. `client.transcriptions.upload(audio_file)`, used for asynchronous batch jobs
**Answer:** B — Shown verbatim in the module's code sample.

**Q10.** In the transcription code sample, what value is passed for `api_version` when constructing the `AzureOpenAI` client?
A. `"2024-02-01"` (an earlier stable API version)
B. `"2025-03-01-preview"`
C. `"2023-12-01-preview"`
D. `"v1"` (the OpenAI public API version string)
**Answer:** B — `api_version="2025-03-01-preview"` appears in both the transcription and synthesis code samples.

**Q11.** True or False (single-answer): model availability for gpt-4o audio models is consistent across every Azure region.
A. True — all Foundry regions support all audio models identically, since they share one global backend
B. False — the module notes model availability varies by region and directs you to the regional availability table
C. True, but only for the transcription models, not TTS, which is region-locked separately
D. False, availability depends solely on subscription tier, not region, unlike other Foundry models
**Answer:** B — The module explicitly notes: "Model availability varies by region. Review the model regional availability table in the Microsoft Foundry documentation" (stated for both transcription and synthesis models).

**Q12.** What value is passed for the `response_format` parameter in the module's transcription code sample?
A. `"json"`
B. `"text"`
C. `"srt"`
D. `"verbose_json"`
**Answer:** B — `transcription = client.audio.transcriptions.create(model=..., file=audio_file, response_format="text")`.

## Unit 4: Synthesize speech

**Q13.** Which two models does this module list as supporting text-to-speech?
A. gpt-4o-tts
B. gpt-4o-mini-tts
C. gpt-4o-transcribe
D. gpt-4o-realtime
**Answer:** A, B — "Models that support text-to-speech operations include: gpt-4o-tts, gpt-4o-mini-tts."

**Q14.** Which method is used to generate and stream synthesized speech to a file using the `AzureOpenAI` client?
A. `client.audio.speech.create()`, directly writing the returned bytes to disk without streaming
B. `client.audio.speech.with_streaming_response.create(...)` used as a context manager, then `response.stream_to_file(path)`
C. `client.tts.synthesize(text=...).save(path)`, a shorthand method from an older, now-retired SDK preview release
D. `client.audio.synthesize_speech(text=..., output=path)`, mirroring the classic Speech SDK signature
**Answer:** B — Shown verbatim: `with client.audio.speech.with_streaming_response.create(...) as response: response.stream_to_file(speech_file_path)`.

**Q15.** In the text-to-speech code sample, which parameter lets you steer the delivery style/tone using natural language (e.g., "Speak in an upbeat, excited tone")?
A. `voice` (selects the speaker identity)
B. `style` (a preset delivery category)
C. `instructions`
D. `prosody` (an SSML-style rate/pitch control)
**Answer:** C — The `instructions` parameter is passed directly in the sample: `instructions="Speak in an upbeat, excited tone."`.

**Q16.** What voice name is used as an example value for the `voice` parameter in the text-to-speech code sample?
A. `"nova"`
B. `"alloy"`
C. `"shimmer"`
D. `"echo"`
**Answer:** B — `voice="alloy"` appears in the code sample.

**Q17.** What audio file format is used for the output file in the text-to-speech example?
A. `.mp3`
B. `.ogg`
C. `.wav`
D. `.flac`
**Answer:** C — `speech_file_path = Path("output_speech.wav")`.

**Q18.** Which statement correctly distinguishes the generative AI TTS approach shown in this module from the classic Azure AI Speech SDK's `SpeechSynthesizer`?
A. The generative TTS approach uses SSML tags exclusively for tone control, identical to the classic Speech SDK's `SpeechSynthesizer` class.
B. The generative TTS approach steers tone/style via a natural-language `instructions` parameter passed to an OpenAI-style API, rather than SSML prosody markup via a dedicated Speech resource.
C. There is no difference; both are the same underlying service exposed through two differently branded client libraries and SDK packages.
D. The generative TTS approach cannot output audio files at all, only real-time streams played directly through locally connected speakers.
**Answer:** B — This module's TTS model is accessed via the OpenAI-compatible `AzureOpenAI` client with a natural-language `instructions` parameter for tone, which is architecturally distinct from the Speech SDK's SSML-based synthesis (covered in a separate module in this learning path).

## Unit 5: Exercise

**Q19.** What is required to complete the hands-on exercise for this module?
A. A GitHub Copilot subscription with the Azure extension enabled
B. An Azure subscription (new accounts get free credits for the first 30 days)
C. A pre-existing Azure AI Speech resource only, with no other Foundry setup needed
D. Local GPU hardware for on-device transcription and synthesis
**Answer:** B — The module states you need an Azure subscription and notes new sign-ups include credits for the first 30 days.

## Unit 6–7: Module assessment / Summary

**Q20.** According to the module summary, what two generative AI solution capabilities did you learn to build using Microsoft Foundry?
A. Transcribe speech to text and synthesize speech from text
B. Translate speech and detect PII in speech
C. Perform sentiment analysis on transcribed calls and generate video captions
D. Train custom acoustic models and deploy them to edge devices
**Answer:** A — The summary states: "you learned... how you can use Microsoft Foundry to create generative AI solutions that: Transcribe speech to text. Synthesize speech from text."

## Scenario questions

**Q21.** You want to build a hands-free assistant that reads a user's incoming emails aloud in an upbeat tone, and also transcribes the user's spoken replies into text. Which combination of calls from this module fits, and which parameter controls the tone?
A. `client.audio.transcriptions.create` to read emails aloud and `client.audio.speech...create` to transcribe replies; tone via `voice`
B. `client.audio.speech.with_streaming_response.create` (with the `instructions` parameter for tone) to read emails aloud, and `client.audio.transcriptions.create` to transcribe replies
C. A single unified call handles both directions automatically; no separate methods are needed for reading emails or transcribing replies
D. Use the classic `SpeechSynthesizer` class for reading emails aloud and a separate standalone Whisper API for transcribing replies
**Answer:** B — Text-to-speech uses `client.audio.speech.with_streaming_response.create(...)` with the `instructions` parameter for delivery tone/style, while speech-to-text uses the separate `client.audio.transcriptions.create(...)` call.

**Q22.** You're building a meeting-transcription app that requires real-time streaming from a live microphone feed with continuous recognition. Based on this module's distinctions, which approach is more appropriate, and why?
A. The gpt-4o generative audio models, because they support the `instructions` parameter for controlling delivery tone and pacing
B. The Azure AI Speech SDK, because it supports continuous recognition and real-time microphone streaming, unlike the file-based generative audio flow shown in this module
C. Either approach works identically for this use case; there's no meaningful architectural distinction between them at all
D. Neither approach supports meeting transcription at all without installing a separate third-party diarization add-on package
**Answer:** B — This module's generative audio flow works on uploaded audio files via `client.audio.transcriptions.create`; the module's exam-relevance note attributes continuous recognition and real-time microphone streaming to the classic Speech SDK instead.

**Q23.** Your app needs to transcribe a recorded meeting and differentiate between speakers, using the same `AzureOpenAI`-based flow shown in this module. Which model should you deploy, and which method do you call?
A. Deploy `gpt-4o-transcribe-diarize`, then call `client.audio.transcriptions.create(model=..., file=..., response_format="text")`
B. Deploy `gpt-4o-tts`, then call `client.audio.speech.with_streaming_response.create` on the recording
C. Deploy `gpt-4o-mini-tts` with a `diarization=True` parameter passed at transcription request time
D. Diarization isn't supported by any model in this module; a third-party service is required
**Answer:** A — `gpt-4o-transcribe-diarize` is the diarization-capable speech-to-text model, and transcription (of any speech-to-text model) still goes through `client.audio.transcriptions.create`.
