# Practice questions — Create speech-enabled apps with Azure Speech in Microsoft Foundry Tools

## Unit 1: Introduction

**Q1.** Which four API categories does this module identify as being offered by Azure Speech in Foundry Tools?
A. Speech to text, Text to speech, Speech Translation, Voice Live
B. Speech to text, Text to speech, Sentiment Analysis, Language Detection
C. Speech Translation, Voice Live, Named Entity Recognition, PII Redaction
D. Text to speech, Voice Live, Custom Vision, Document Intelligence
**Answer:** A — The module lists exactly these four: Speech to text, Text to speech, Speech Translation, and Voice Live.

**Q2.** Which PyPI package provides the Azure Speech SDK for Python?
A. `azure-ai-speech` (a newer, unified package name)
B. `azure-cognitiveservices-speech`
C. `azure-speech-sdk` (the shorthand alias)
D. `microsoft-speech-python`
**Answer:** B — The module lists "Azure Speech for Python" as PyPI package `azure-cognitiveservices-speech`, and the code imports `azure.cognitiveservices.speech as speech_sdk`.

**Q3.** Which NuGet package provides the Azure Speech SDK for .NET, per this module?
A. Azure.AI.Speech (the newer unified naming scheme)
B. Microsoft.CognitiveServices.Speech
C. Azure.CognitiveServices.Speech.SDK
D. Microsoft.Azure.Speech (a legacy-sounding package name)
**Answer:** B — The module lists "Azure Speech for Microsoft .NET — NuGet Microsoft.CognitiveServices.Speech."

**Q4.** Which npm package provides the Azure Speech SDK for JavaScript, per this module?
A. @azure/cognitiveservices-speech-sdk
B. azure-speech-sdk (an unscoped, shorter alias)
C. microsoft-cognitiveservices-speech-sdk
D. @microsoft/speech-sdk (a scoped, shorter alias)
**Answer:** C — The module lists "Azure Speech for JavaScript — npm microsoft-cognitiveservices-speech-sdk."

**Q5.** Which example scenarios does the module cite for using Azure Speech in Foundry Tools? (Choose two.)
A. Transcribing recorded calls or meetings
B. An AI assistant reading text messages or emails aloud
C. Real-time video captioning during livestreams
D. Detecting sentiment in written product reviews
**Answer:** A, B — The module's example scenarios are "transcribing recorded calls/meetings" and "an AI assistant reading text messages/emails aloud."

## Unit 2: Azure Speech in Foundry Tools

**Q6.** Which object must you create first to encapsulate the connection details (endpoint/region and key) to Azure Speech in a Foundry resource?
A. `SpeechClient`
B. `SpeechConfig`
C. `AudioConfig`
D. `FoundryConnection`
**Answer:** B — "The initial object you need to create... is a SpeechConfig object; which encapsulates the connection details for the service."

**Q7.** Prior to which Python Speech SDK version did you have to specify a region instead of being able to use a Foundry resource endpoint?
A. 1.30.0
B. 1.40.1
C. 1.48.2
D. 2.0.0
**Answer:** C — "Releases of the Python SDK prior to 1.48.2 required that you specify the region... With the latest release, you can use either the Foundry resource endpoint or the region."

**Q8.** Given a Foundry project endpoint `https://my-ai-app-foundry.services.ai.azure.com/api/projects/my-ai-app`, what is the underlying resource endpoint?
A. `https://my-ai-app-foundry.services.ai.azure.com/api/projects`
B. `https://my-ai-app.services.ai.azure.com`
C. `https://my-ai-app-foundry.services.ai.azure.com`
D. `https://my-ai-app-foundry.services.ai.azure.com/resource/my-ai-app`
**Answer:** C — Same pattern as module 1: strip `/api/projects/{project_name}` to get the resource endpoint.

## Unit 3: Use the Speech to Text API

**Q9.** Which sequence correctly describes the object creation pattern for speech recognition?
A. AudioConfig → SpeechRecognizer → SpeechConfig, then call StartAsync()
B. SpeechConfig (+ optional AudioConfig) → SpeechRecognizer → call RecognizeOnceAsync()
C. SpeechClient → SpeechConfig → AudioConfig, then call TranscribeAsync()
D. SpeechRecognizer → SpeechConfig → AudioConfig, then call RecognizeOnceAsync()
**Answer:** B — The documented pattern: create SpeechConfig, optionally an AudioConfig, use both to create a SpeechRecognizer, then call its methods (e.g., RecognizeOnceAsync()).

**Q10.** By default, if no `AudioConfig` is supplied, what audio input source does `SpeechRecognizer` use?
A. A specified WAV file on local disk
B. The default system microphone
C. A blob storage container
D. Standard input (stdin) only
**Answer:** B — "By default, this is the default system microphone, but you can also specify an audio file."

**Q11.** After a successful call to `recognize_once_async().get()`, which property indicates the outcome, and what enumerated value confirms success?
A. `result.status` == `"OK"` (a REST-style status string)
B. `result.reason` == `ResultReason.RecognizedSpeech`
C. `result.state` == `"Completed"` (a job-state style string)
D. `result.success` == `True` (a simple boolean flag)
**Answer:** B — "If the operation was successful, the Reason property has the enumerated value RecognizedSpeech."

**Q12.** What does a `Reason` value of `NoMatch` indicate after a speech-to-text call?
A. An unrecoverable network error occurred during the recognition call.
B. The audio was parsed successfully, but no speech was recognized.
C. The audio file format was unsupported by the recognizer.
D. The subscription key is invalid or has expired.
**Answer:** B — Explicitly defined in the module: "NoMatch (indicating that the audio was successfully parsed but no speech was recognized)."

**Q13.** If `result.reason` is `Canceled`, where should you look to determine the root cause?
A. The `Text` property, which contains an error message in this case
B. The `Properties` collection's `CancellationReason` property
C. The `Duration` property, which reports zero on cancellation
D. There's no way to diagnose a Canceled result programmatically
**Answer:** B — "Canceled, indicating that an error occurred (in which case, you can check the Properties collection for the CancellationReason property to determine what went wrong)."

**Q14.** Which properties are part of the `SpeechRecognitionResult` object, per this module? (Choose three.)
A. `Text`
B. `Reason`
C. `Duration`
D. `Confidence`
E. `Locale`
**Answer:** A, B, C — The module lists: Duration, OffsetInTicks, Properties, Reason, ResultId, Text. Confidence and Locale are not listed as properties in this module's content.

## Unit 4: Use the Text to Speech API

**Q15.** Which object serves as the proxy client for the Text to speech API?
A. `SpeechRecognizer`
B. `AudioOutputConfig`
C. `SpeechSynthesizer`
D. `TextToSpeechClient`
**Answer:** C — "Use the SpeechConfig and AudioConfig to create a SpeechSynthesizer object. This object is a proxy client for the Text to speech API."

**Q16.** By default, if no `AudioConfig` is supplied, where does synthesized audio output go?
A. Nowhere — an AudioConfig is mandatory
B. The default system speaker
C. A temporary blob in Azure Storage
D. Standard output as raw bytes
**Answer:** B — "By default, this is the default system speaker."

**Q17.** How can you configure a `SpeechSynthesizer` to let you process the returned audio stream object directly, instead of auto-routing it to a speaker or file?
A. Set `AudioConfig` to a null value.
B. Omit `SpeechConfig` entirely.
C. Call `speak_text_async()` with `stream=True`.
D. This isn't possible with the Speech SDK.
**Answer:** A — "by explicitly setting this value to a null value, you can process the audio stream object that is returned directly."

**Q18.** Which `Reason` enumeration value on `SpeechSynthesisResult` confirms successful speech synthesis?
A. `RecognizedSpeech` (used for speech-to-text results)
B. `SynthesizingAudioCompleted`
C. `AudioGenerated` (a plausible-sounding but unused name)
D. `SpeechSynthesized` (a plausible-sounding but unused name)
**Answer:** B — "the Reason property is set to the SynthesizingAudioCompleted enumeration."

**Q19.** In the text-to-speech error-handling code sample, after detecting `ResultReason.Canceled`, how do you get further error detail when the cancellation reason is `CancellationReason.Error`?
A. `cancellation_details.error_details`
B. `speech_synthesis_result.error_message`
C. `speech_config.get_error()`
D. Errors cannot be inspected further in this SDK
**Answer:** A — Shown in the code: `if cancellation_details.reason == speechsdk.CancellationReason.Error: if cancellation_details.error_details: print(...)`.

**Q20.** Which properties are part of the `SpeechSynthesisResult` object, per this module? (Choose two.)
A. `AudioData`
B. `Reason`
C. `Text`
D. `Duration`
**Answer:** A, B — The module lists `AudioData`, `Properties`, `Reason`, and `ResultId` as `SpeechSynthesisResult` properties. `Text` and `Duration` belong to `SpeechRecognitionResult` instead.

## Unit 5: Configure audio format and voices

**Q21.** Which method sets the output audio format (file type, sample rate, bit depth) for speech synthesis?
A. `speech_config.set_audio_format()` (a shortened, non-existent name)
B. `speech_config.set_speech_synthesis_output_format()`
C. `speech_synthesizer.set_output_format()`
D. `audio_config.set_format()` (on the wrong object entirely)
**Answer:** B — `speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)`.

**Q22.** Which property sets which voice `SpeechSynthesizer` should use, and what is an example valid value shown in the module?
A. `speech_config.voice_name = "aria"` (a shortened, non-existent property)
B. `speech_config.speech_synthesis_voice_name = 'en-US-Brian:DragonHDLatestNeural'`
C. `speech_synthesizer.voice = "en-US-Brian"` (set on the wrong object)
D. `audio_config.voice_name = 'en-US-Brian'` (also on the wrong object)
**Answer:** B — Shown verbatim in the module's code example.

## Unit 6: Use Speech Synthesis Markup Language

**Q23.** What is SSML, per this module?
A. A binary protocol for streaming raw audio bytes between the client and the Speech service endpoint
B. An XML-based syntax for describing characteristics of speech to be synthesized, offering finer control than plain text
C. A JSON schema for configuring SpeechConfig objects at synthesis request time via the REST API
D. A Python-only DSL specific to the `speechsdk` package, unavailable in other languages
**Answer:** B — "the service also supports an XML-based syntax for describing characteristics of the speech you want to generate. This Speech Synthesis Markup Language (SSML) syntax offers greater control over how the spoken output sounds."

**Q24.** Which SSML feature would you use to make the text "SQL" pronounced as "sequel"?
A. `<break strength="weak"/>` (inserts a pause, not a pronunciation change)
B. `<mstts:express-as style="cheerful">` (controls speaking style, not pronunciation)
C. `<phoneme alphabet="sapi" ph="...">` (specifying phonemes / phonetic pronunciation)
D. `<prosody rate="slow">` (controls speaking rate, not pronunciation)
**Answer:** C — The module explicitly gives this exact example: "Specify phonemes (phonetic pronunciations), for example to pronounce the text 'SQL' as 'sequel'," demonstrated via the `<phoneme>` element in the sample SSML.

**Q25.** Which SSML element/attribute in the module's example is used to set a neural voice's speaking style (e.g., "cheerful")?
A. `<voice name="...">` (selects the speaker, not the style)
B. `<mstts:express-as style="cheerful">`
C. `<prosody style="cheerful">`
D. `<say-as interpret-as="style">`
**Answer:** B — Shown in the sample SSML: `<mstts:express-as style="cheerful"> I say tomato </mstts:express-as>`.

**Q26.** Which method do you call on a `SpeechSynthesizer` to submit SSML (rather than plain text) for synthesis?
A. `speak_text_async()`
B. `speak_markup_async()`
C. `speak_ssml_async()`
D. `synthesize_xml_async()`
**Answer:** C — `speech_synthesis_result = speech_synthesizer.speak_ssml_async('<speak>...').get()`.

**Q27.** SSML's "say-as" rules are used for which purpose?
A. Inserting recorded background noise behind the spoken audio track
B. Expressing a string according to a specific form, such as a date, time, or telephone number
C. Adjusting the pitch and timbre of the synthesized voice output directly
D. Switching between two different voices mid-utterance for a dialog
**Answer:** B — "Use common 'say-as' rules, for example to specify that a given string should be expressed as a date, time, telephone number, or other form."

**Q28.** Which SSML element is used in the module's example to insert a pause/silence between phrases?
A. `<mstts:express-as>`
B. `<break strength="weak"/>`
C. `<prosody rate="slow"/>`
D. `<say-as interpret-as="pause"/>`
**Answer:** B — The sample SSML includes `<break strength="weak"/>Lets call the whole thing off!`, and the module lists "insert pauses/silence" as an SSML capability.

**Q29.** What is the purpose of the `xmlns:mstts` namespace declaration on the `<speak>` root element in the module's SSML example?
A. It's a mandatory namespace attribute required on all valid XML documents everywhere
B. It enables Microsoft Text-to-Speech (mstts) extension elements, such as `<mstts:express-as>`
C. It specifies the target audio codec and bit rate used for synthesis output
D. It declares the SSML schema version number that the document targets
**Answer:** B — The `xmlns:mstts="https://www.w3.org/2001/mstts"` declaration is what allows the `<mstts:express-as style="cheerful">` extension element to be used in the sample.

**Q30.** In the module's example SSML, two `<voice>` elements are used within a single `<speak>` document. What does this demonstrate?
A. SSML only supports a single voice per request; the second `<voice>` element makes the example invalid
B. SSML supports combining multiple distinct voices in one synthesis request, producing a dialog (Aria and Guy each speak a line)
C. The second `<voice>` element is silently ignored by the synthesizer at runtime without error
D. Voice must always be set via `speech_config.speech_synthesis_voice_name`, never inline in SSML
**Answer:** B — The example SSML nests separate `<voice name="en-US-AriaNeural">` and `<voice name="en-US-GuyNeural">` elements to produce "a dialog between two neural voices."

## Unit 7–9: Exercise / Assessment / Summary

**Q31.** Which two Speech SDK capabilities does the exercise in this module ask you to implement in a single app?
A. Speech recognition and speech synthesis
B. Speech translation and Voice Live
C. Custom speech model training and deployment
D. SSML validation and audio format benchmarking
**Answer:** A — "In this exercise, build a speech enabled app for both speech recognition and synthesis."

## Scenario questions

**Q32.** You need an app that transcribes a customer's spoken support call to text for logging, and also plays back a cheerful synthesized confirmation message that correctly pronounces "SQL" as "sequel." Which combination of objects/methods fits?
A. `SpeechRecognizer` with `recognize_once_async()` for transcription; `SpeechSynthesizer` with `speak_ssml_async()` using `<mstts:express-as style="cheerful">` and `<phoneme>` for the confirmation
B. `AzureOpenAI` client's `client.audio.transcriptions.create` for transcription; `SpeechSynthesizer.speak_text_async()` for playback of a plain confirmation
C. A single `SpeechConfig` object handles both transcription and styled/phonetic playback automatically without a Recognizer or Synthesizer
D. `SpeechTranslationConfig` is required for any pronunciation control, even when no translation target language is ever configured
**Answer:** A — Transcription uses `SpeechRecognizer.recognize_once_async()`; a cheerful, correctly-pronounced confirmation requires SSML submitted via `speak_ssml_async()` with `<mstts:express-as>` for style and `<phoneme>` for pronunciation — both covered in this module.

**Q33.** Your team is choosing between the classic Azure Speech SDK (this module) and generative gpt-4o audio models (covered elsewhere) for a project that requires SSML-based prosody control and custom speech models. Which should you choose, and why?
A. The gpt-4o generative audio models, because they use a simpler natural-language `instructions` parameter for tone control instead
B. The classic Azure Speech SDK, because it supports SSML markup and (per Speech docs) custom speech models — capabilities the generative-model approach doesn't expose the same way
C. Either approach is identical for SSML support, since both ultimately wrap the exact same underlying Azure service
D. Neither approach supports custom pronunciation control without integrating a separate, dedicated third-party phoneme library
**Answer:** B — This module's exam-relevance note states the Speech SDK "supports SSML markup, granular audio format/voice configuration, and... custom speech models — capabilities the generative-model approach does not expose in the same way."

**Q34.** A developer creates both a `SpeechRecognizer` and a `SpeechSynthesizer` without passing an `AudioConfig` to either. What happens by default in each case?
A. Both throw a `MissingAudioConfigException` immediately at object construction time in the constructor
B. `SpeechRecognizer` defaults to the system microphone for input; `SpeechSynthesizer` defaults to the system speaker for output
C. Both default to silently writing their audio to a temporary WAV file located on local disk
D. `SpeechRecognizer` requires an explicit `AudioConfig` to function, but `SpeechSynthesizer` does not
**Answer:** B — The module states both default behaviors independently: "By default, this is the default system microphone" (recognition) and "By default, this is the default system speaker" (synthesis).
