# Practice questions — Create speech-enabled apps with Azure Speech in Microsoft Foundry Tools

## Unit 1: Introduction

**Q1.** Which four API categories does this module identify as being offered by Azure Speech in Foundry Tools?
A. Speech to text, Text to speech, Speech Translation, Voice Live
B. Speech to text, Text to speech, Sentiment Analysis, Language Detection
C. Speech Translation, Voice Live, Named Entity Recognition, PII Redaction
D. Text to speech, Voice Live, Custom Vision, Document Intelligence
**Answer:** A — The module lists exactly these four: Speech to text, Text to speech, Speech Translation, and Voice Live.

**Q2.** Which PyPI package provides the Azure Speech SDK for Python?
A. `azure-ai-speech`
B. `azure-cognitiveservices-speech`
C. `azure-speech-sdk`
D. `microsoft-speech-python`
**Answer:** B — The module lists "Azure Speech for Python" as PyPI package `azure-cognitiveservices-speech`, and the code imports `azure.cognitiveservices.speech as speech_sdk`.

## Unit 2: Azure Speech in Foundry Tools

**Q3.** Which object must you create first to encapsulate the connection details (endpoint/region and key) to Azure Speech in a Foundry resource?
A. `SpeechClient`
B. `SpeechConfig`
C. `AudioConfig`
D. `FoundryConnection`
**Answer:** B — "The initial object you need to create... is a SpeechConfig object; which encapsulates the connection details for the service."

**Q4.** Prior to which Python Speech SDK version did you have to specify a region instead of being able to use a Foundry resource endpoint?
A. 1.30.0
B. 1.40.1
C. 1.48.2
D. 2.0.0
**Answer:** C — "Releases of the Python SDK prior to 1.48.2 required that you specify the region... With the latest release, you can use either the Foundry resource endpoint or the region."

**Q5.** Given a Foundry project endpoint `https://my-ai-app-foundry.services.ai.azure.com/api/projects/my-ai-app`, what is the underlying resource endpoint?
A. `https://my-ai-app-foundry.services.ai.azure.com/api/projects`
B. `https://my-ai-app.services.ai.azure.com`
C. `https://my-ai-app-foundry.services.ai.azure.com`
D. `https://my-ai-app-foundry.services.ai.azure.com/resource/my-ai-app`
**Answer:** C — Same pattern as module 1: strip `/api/projects/{project_name}` to get the resource endpoint.

## Unit 3: Use the Speech to Text API

**Q6.** Which sequence correctly describes the object creation pattern for speech recognition?
A. AudioConfig → SpeechRecognizer → SpeechConfig
B. SpeechConfig (+ optional AudioConfig) → SpeechRecognizer → call RecognizeOnceAsync()
C. SpeechClient → SpeechConfig → AudioConfig
D. SpeechRecognizer → SpeechConfig → AudioConfig
**Answer:** B — The documented pattern: create SpeechConfig, optionally an AudioConfig, use both to create a SpeechRecognizer, then call its methods (e.g., RecognizeOnceAsync()).

**Q7.** By default, if no `AudioConfig` is supplied, what audio input source does `SpeechRecognizer` use?
A. A specified WAV file
B. The default system microphone
C. A blob storage container
D. Standard input (stdin) only
**Answer:** B — "By default, this is the default system microphone, but you can also specify an audio file."

**Q8.** After a successful call to `recognize_once_async().get()`, which property indicates the outcome, and what enumerated value confirms success?
A. `result.status` == `"OK"`
B. `result.reason` == `ResultReason.RecognizedSpeech`
C. `result.state` == `"Completed"`
D. `result.success` == `True`
**Answer:** B — "If the operation was successful, the Reason property has the enumerated value RecognizedSpeech."

**Q9.** What does a `Reason` value of `NoMatch` indicate after a speech-to-text call?
A. An unrecoverable network error occurred.
B. The audio was parsed successfully, but no speech was recognized.
C. The audio file format was unsupported.
D. The subscription key is invalid.
**Answer:** B — Explicitly defined in the module: "NoMatch (indicating that the audio was successfully parsed but no speech was recognized)."

**Q10.** If `result.reason` is `Canceled`, where should you look to determine the root cause?
A. The `Text` property
B. The `Properties` collection's `CancellationReason` property
C. The `Duration` property
D. There's no way to diagnose a Canceled result
**Answer:** B — "Canceled, indicating that an error occurred (in which case, you can check the Properties collection for the CancellationReason property to determine what went wrong)."

**Q11.** Which properties are part of the `SpeechRecognitionResult` object, per this module? (Choose three.)
A. `Text`
B. `Reason`
C. `Duration`
D. `Confidence`
E. `Locale`
**Answer:** A, B, C — The module lists: Duration, OffsetInTicks, Properties, Reason, ResultId, Text. Confidence and Locale are not listed as properties in this module's content.

## Unit 4: Use the Text to Speech API

**Q12.** Which object serves as the proxy client for the Text to speech API?
A. `SpeechRecognizer`
B. `AudioOutputConfig`
C. `SpeechSynthesizer`
D. `TextToSpeechClient`
**Answer:** C — "Use the SpeechConfig and AudioConfig to create a SpeechSynthesizer object. This object is a proxy client for the Text to speech API."

**Q13.** By default, if no `AudioConfig` is supplied, where does synthesized audio output go?
A. Nowhere — an AudioConfig is mandatory
B. The default system speaker
C. A temporary blob in Azure Storage
D. Standard output as raw bytes
**Answer:** B — "By default, this is the default system speaker."

**Q14.** How can you configure a `SpeechSynthesizer` to let you process the returned audio stream object directly, instead of auto-routing it to a speaker or file?
A. Set `AudioConfig` to a null value.
B. Omit `SpeechConfig` entirely.
C. Call `speak_text_async()` with `stream=True`.
D. This isn't possible with the Speech SDK.
**Answer:** A — "by explicitly setting this value to a null value, you can process the audio stream object that is returned directly."

**Q15.** Which `Reason` enumeration value on `SpeechSynthesisResult` confirms successful speech synthesis?
A. `RecognizedSpeech`
B. `SynthesizingAudioCompleted`
C. `AudioGenerated`
D. `SpeechSynthesized`
**Answer:** B — "the Reason property is set to the SynthesizingAudioCompleted enumeration."

**Q16.** In the text-to-speech error-handling code sample, after detecting `ResultReason.Canceled`, how do you get further error detail when the cancellation reason is `CancellationReason.Error`?
A. `cancellation_details.error_details`
B. `speech_synthesis_result.error_message`
C. `speech_config.get_error()`
D. Errors cannot be inspected further in this SDK
**Answer:** A — Shown in the code: `if cancellation_details.reason == speechsdk.CancellationReason.Error: if cancellation_details.error_details: print(...)`.

## Unit 5: Configure audio format and voices

**Q17.** Which method sets the output audio format (file type, sample rate, bit depth) for speech synthesis?
A. `speech_config.set_audio_format()`
B. `speech_config.set_speech_synthesis_output_format()`
C. `speech_synthesizer.set_output_format()`
D. `audio_config.set_format()`
**Answer:** B — `speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)`.

**Q18.** Which property sets which voice `SpeechSynthesizer` should use, and what is an example valid value shown in the module?
A. `speech_config.voice_name = "aria"`
B. `speech_config.speech_synthesis_voice_name = 'en-US-Brian:DragonHDLatestNeural'`
C. `speech_synthesizer.voice = "en-US-Brian"`
D. `audio_config.voice_name = 'en-US-Brian'`
**Answer:** B — Shown verbatim in the module's code example.

## Unit 6: Use Speech Synthesis Markup Language

**Q19.** What is SSML, per this module?
A. A binary protocol for streaming audio
B. An XML-based syntax for describing characteristics of speech to be synthesized, offering finer control than plain text
C. A JSON schema for configuring SpeechConfig objects
D. A Python-only DSL specific to the `speechsdk` package
**Answer:** B — "the service also supports an XML-based syntax for describing characteristics of the speech you want to generate. This Speech Synthesis Markup Language (SSML) syntax offers greater control over how the spoken output sounds."

**Q20.** Which SSML feature would you use to make the text "SQL" pronounced as "sequel"?
A. `<break strength="weak"/>`
B. `<mstts:express-as style="cheerful">`
C. `<phoneme alphabet="sapi" ph="...">` (specifying phonemes / phonetic pronunciation)
D. `<prosody rate="slow">`
**Answer:** C — The module explicitly gives this exact example: "Specify phonemes (phonetic pronunciations), for example to pronounce the text 'SQL' as 'sequel'," demonstrated via the `<phoneme>` element in the sample SSML.

**Q21.** Which SSML element/attribute in the module's example is used to set a neural voice's speaking style (e.g., "cheerful")?
A. `<voice name="...">`
B. `<mstts:express-as style="cheerful">`
C. `<prosody style="cheerful">`
D. `<say-as interpret-as="style">`
**Answer:** B — Shown in the sample SSML: `<mstts:express-as style="cheerful"> I say tomato </mstts:express-as>`.

**Q22.** Which method do you call on a `SpeechSynthesizer` to submit SSML (rather than plain text) for synthesis?
A. `speak_text_async()`
B. `speak_markup_async()`
C. `speak_ssml_async()`
D. `synthesize_xml_async()`
**Answer:** C — `speech_synthesis_result = speech_synthesizer.speak_ssml_async('<speak>...').get()`.

**Q23.** SSML's "say-as" rules are used for which purpose?
A. Inserting recorded background noise
B. Expressing a string according to a specific form, such as a date, time, or telephone number
C. Adjusting pitch and timbre
D. Switching between two different voices mid-utterance
**Answer:** B — "Use common 'say-as' rules, for example to specify that a given string should be expressed as a date, time, telephone number, or other form."

## Unit 7–9: Exercise / Assessment / Summary

**Q24.** Which two Speech SDK capabilities does the exercise in this module ask you to implement in a single app?
A. Speech recognition and speech synthesis
B. Speech translation and Voice Live
C. Custom speech model training and deployment
D. SSML validation and audio format benchmarking
**Answer:** A — "In this exercise, build a speech enabled app for both speech recognition and synthesis."
