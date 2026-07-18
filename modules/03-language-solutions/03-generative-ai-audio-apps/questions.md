# Practice questions — Develop a speech-capable generative AI application

## Unit 1–2: Introduction / Choose a speech-capable model

**Q1.** Where do you go in Microsoft Foundry to find and filter speech-capable generative AI models?
A. The Azure AI Speech resource blade in the Azure portal
B. The Microsoft Foundry Models catalog, using its filter and search features
C. The Azure Marketplace
D. The Cognitive Services multi-service resource page
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

## Unit 3: Transcribe speech

**Q4.** Which model is specifically designed to include speaker diarization when transcribing audio, per this module?
A. gpt-4o-transcribe
B. gpt-4o-mini-transcribe
C. gpt-4o-transcribe-diarize
D. gpt-4o-tts
**Answer:** C — The module lists `gpt-4o-transcribe-diarize` as one of three speech-to-text models, distinguished by name from the plain `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`.

**Q5.** Which of the following are listed in this module as speech-to-text capable models? (Choose two.)
A. gpt-4o-transcribe
B. gpt-4o-mini-transcribe
C. gpt-4o-tts
D. gpt-4o-mini-tts
**Answer:** A, B — gpt-4o-transcribe, gpt-4o-mini-transcribe, and gpt-4o-transcribe-diarize are the speech-to-text models; gpt-4o-tts and gpt-4o-mini-tts are text-to-speech models instead.

**Q6.** Which client class from the OpenAI SDK is used to connect to a Microsoft Foundry resource endpoint for speech transcription?
A. `SpeechClient`
B. `AzureOpenAI`
C. `FoundryAudioClient`
D. `TextAnalyticsClient`
**Answer:** B — Code sample: `from openai import AzureOpenAI` and `client = AzureOpenAI(azure_endpoint=..., api_key=..., api_version=...)`.

**Q7.** Which method call submits an audio file for transcription using the `AzureOpenAI` client?
A. `client.audio.transcribe(file=audio_file)`
B. `client.audio.transcriptions.create(model=..., file=audio_file, response_format="text")`
C. `client.speech.recognize(audio=audio_file)`
D. `client.transcriptions.upload(audio_file)`
**Answer:** B — Shown verbatim in the module's code sample.

**Q8.** In the transcription code sample, what value is passed for `api_version` when constructing the `AzureOpenAI` client?
A. `"2024-02-01"`
B. `"2025-03-01-preview"`
C. `"2023-12-01-preview"`
D. `"v1"`
**Answer:** B — `api_version="2025-03-01-preview"` appears in both the transcription and synthesis code samples.

**Q9.** True or False (single-answer): model availability for gpt-4o audio models is consistent across every Azure region.
A. True — all Foundry regions support all audio models identically
B. False — the module notes model availability varies by region and directs you to the regional availability table
C. True, but only for the transcription models, not TTS
D. False, availability depends solely on subscription tier, not region
**Answer:** B — The module explicitly notes: "Model availability varies by region. Review the model regional availability table in the Microsoft Foundry documentation" (stated for both transcription and synthesis models).

## Unit 4: Synthesize speech

**Q10.** Which two models does this module list as supporting text-to-speech?
A. gpt-4o-tts
B. gpt-4o-mini-tts
C. gpt-4o-transcribe
D. gpt-4o-realtime
**Answer:** A, B — "Models that support text-to-speech operations include: gpt-4o-tts, gpt-4o-mini-tts."

**Q11.** Which method is used to generate and stream synthesized speech to a file using the `AzureOpenAI` client?
A. `client.audio.speech.create()` directly writing bytes
B. `client.audio.speech.with_streaming_response.create(...)` used as a context manager, then `response.stream_to_file(path)`
C. `client.tts.synthesize(text=...).save(path)`
D. `client.audio.synthesize_speech(text=..., output=path)`
**Answer:** B — Shown verbatim: `with client.audio.speech.with_streaming_response.create(...) as response: response.stream_to_file(speech_file_path)`.

**Q12.** In the text-to-speech code sample, which parameter lets you steer the delivery style/tone using natural language (e.g., "Speak in an upbeat, excited tone")?
A. `voice`
B. `style`
C. `instructions`
D. `prosody`
**Answer:** C — The `instructions` parameter is passed directly in the sample: `instructions="Speak in an upbeat, excited tone."`.

**Q13.** What voice name is used as an example value for the `voice` parameter in the text-to-speech code sample?
A. `"nova"`
B. `"alloy"`
C. `"shimmer"`
D. `"echo"`
**Answer:** B — `voice="alloy"` appears in the code sample.

**Q14.** What audio file format is used for the output file in the text-to-speech example?
A. `.mp3`
B. `.ogg`
C. `.wav`
D. `.flac`
**Answer:** C — `speech_file_path = Path("output_speech.wav")`.

**Q15.** Which statement correctly distinguishes the generative AI TTS approach shown in this module from the classic Azure AI Speech SDK's `SpeechSynthesizer`?
A. The generative TTS approach uses SSML tags exclusively for tone control, identical to the Speech SDK.
B. The generative TTS approach steers tone/style via a natural-language `instructions` parameter passed to an OpenAI-style API, rather than SSML prosody markup via a dedicated Speech resource.
C. There is no difference; both are the same underlying service.
D. The generative TTS approach cannot output audio files, only real-time streams.
**Answer:** B — This module's TTS model is accessed via the OpenAI-compatible `AzureOpenAI` client with a natural-language `instructions` parameter for tone, which is architecturally distinct from the Speech SDK's SSML-based synthesis (covered in a separate module in this learning path).

## Unit 5: Exercise

**Q16.** What is required to complete the hands-on exercise for this module?
A. A GitHub Copilot subscription
B. An Azure subscription (new accounts get free credits for the first 30 days)
C. A pre-existing Azure AI Speech resource only
D. Local GPU hardware for on-device transcription
**Answer:** B — The module states you need an Azure subscription and notes new sign-ups include credits for the first 30 days.

## Unit 6–7: Module assessment / Summary

**Q17.** According to the module summary, what two generative AI solution capabilities did you learn to build using Microsoft Foundry?
A. Transcribe speech to text and synthesize speech from text
B. Translate speech and detect PII in speech
C. Perform sentiment analysis on transcribed calls and generate video captions
D. Train custom acoustic models and deploy them to edge devices
**Answer:** A — The summary states: "you learned... how you can use Microsoft Foundry to create generative AI solutions that: Transcribe speech to text. Synthesize speech from text."
