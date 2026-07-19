# Create speech-enabled apps with Azure Speech in Microsoft Foundry Tools

Source: https://learn.microsoft.com/en-us/training/modules/create-speech-enabled-apps/

Module info: 9 Units, Intermediate level, roles: AI Engineer / Data Scientist / Developer / Solution Architect / Student, product: Microsoft Foundry.

## Learning objectives

- Use a Microsoft Foundry resource for Azure Speech in Foundry Tools.
- Implement speech recognition with the Azure Speech to text API.
- Use the Text to speech API to implement speech synthesis.
- Configure audio format and voices.
- Use Speech Synthesis Markup Language (SSML).

Prerequisites: familiarity with Azure services/portal; programming experience.

## Exam relevance

Maps to:
- **Implement text analysis solutions (10–15%)** → "Implement speech solutions" → "Implement workflows to convert speech to text and text to speech for agentic interactions" and "Integrate speech as an agent modality, including custom speech models" — this is THE core Speech SDK module.
- Also underlies "Enable multimodal reasoning from audio inputs" and "Translate speech into other languages" (later modules build on the `SpeechConfig`/`SpeechRecognizer`/`SpeechSynthesizer` pattern taught here).

**Key distinguishing factor (exam-critical):** This module uses the dedicated **Azure Speech SDK** (`azure-cognitiveservices-speech` package, classes `SpeechConfig`, `AudioConfig`, `SpeechRecognizer`, `SpeechSynthesizer`) — architecturally different from the **generative gpt-4o audio models** (module 3, `AzureOpenAI` client, `client.audio.transcriptions`/`client.audio.speech`). The Speech SDK is the classic/dedicated speech service approach; it supports SSML markup, granular audio format/voice configuration, and (per other Speech docs) custom speech models — capabilities the generative-model approach does not expose in the same way.

## Unit 1: Introduction

Azure Speech in Foundry Tools provides APIs to build speech-enabled applications:
- **Speech to text** — enables *speech recognition* (app accepts spoken input).
- **Text to speech** — enables *speech synthesis* (app provides spoken output).
- **Speech Translation** — translates spoken input into multiple languages.
- **Voice Live** — API for building AI agents capable of real-time conversations.

This module focuses on **speech recognition and speech synthesis** — core capabilities of any speech-enabled app. (Speech Translation and Voice Live are covered in later modules of this learning path — units 7 and 6 respectively.)

Code examples are in Python; equivalent SDK packages exist for other languages:
- **Azure Speech for Python** — PyPI `azure-cognitiveservices-speech`
- **Azure Speech for Microsoft .NET** — NuGet `Microsoft.CognitiveServices.Speech`
- **Azure Speech for JavaScript** — npm `microsoft-cognitiveservices-speech-sdk`
- **Azure Speech for Java** — Maven `com.microsoft.cognitiveservices.speech:client-sdk`

## Unit 2: Azure Speech in Foundry Tools

Azure Speech in Foundry Tools = a set of speech-related capabilities provided by a **Foundry resource**, usable to add speech support to apps/agents built in Microsoft Foundry projects. Example scenarios: transcribing recorded calls/meetings; an AI assistant reading text messages/emails aloud.

### Using Azure Speech in a Microsoft Foundry resource

Must provision a Microsoft Foundry resource in your Azure subscription. Use its **endpoint** to call APIs, authenticating with the **key** associated with the resource. Call via REST (JSON) or an SDK.

Same project-vs-resource endpoint relationship as module 1: project endpoint = resource endpoint + `/api/projects/{project_name}`. Project and Foundry resource keys are the same. View resource-level endpoint/key under **Admin** tab of the **Operate** page in the Foundry portal.

### Creating a SpeechConfig

The initial object needed: a **`SpeechConfig`** object — encapsulates connection details to the Speech service in your Foundry resource.

```python
# run "pip install azure-cognitiveservices-speech" first to install the package 
import azure.cognitiveservices.speech as speech_sdk

# Create SpeechConfig using endpoint and key
speech_config = speech_sdk.SpeechConfig(subscription="YOUR_FOUNDRY_KEY",
                                        endpoint="YOUR_FOUNDRY_ENDPOINT")
```

> **Version note (exam-relevant detail):** Python SDK releases **prior to 1.48.2** required specifying the **region** where your resource is deployed instead of the endpoint. As of the latest release, you can use **either** the Foundry resource endpoint **or** the region.

## Unit 3: Use the Speech to Text API

Azure Speech supports speech recognition through the **Speech to text** API. Pattern (consistent across SDKs):

1. Use a **`SpeechConfig`** object to encapsulate connection info: **endpoint** (or **region**) and **key**.
2. Optionally use an **`AudioConfig`** to define the audio input source — defaults to the **system microphone**; can also specify an audio file.
3. Use `SpeechConfig` + `AudioConfig` to create a **`SpeechRecognizer`** object — the proxy client for the Speech to text API.
4. Call methods on `SpeechRecognizer`. E.g., **`RecognizeOnceAsync()`** (Python: `recognize_once_async()`) asynchronously transcribes a single spoken utterance.
5. Process the response — a **`SpeechRecognitionResult`** object with properties:
   - `Duration`
   - `OffsetInTicks`
   - `Properties`
   - `Reason`
   - `ResultId`
   - `Text`

If successful, `Reason` == **`RecognizedSpeech`** and `Text` contains the transcription. Other `Reason` values:
- **`NoMatch`** — audio was parsed successfully but no speech was recognized.
- **`Canceled`** — an error occurred; check `Properties` collection's **`CancellationReason`** property for details.

### Example — Transcribing an audio file

```python
import azure.cognitiveservices.speech as speech_sdk

# Speech config encapsulates the connection to the resource
speech_config = speech_sdk.SpeechConfig(subscription="YOUR_FOUNDRY_KEY",
                                       endpoint="YOUR_FOUNDRY_ENDPOINT")

# Audio config determines the audio stream source (defaults to system mic)
file_path = "audio.wav"
audio_config = speech_sdk.audio.AudioConfig(filename=file_path)

# Use a speech recognizer to transcribe the audio
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config,
                                               audio_config=audio_config)

result = speech_recognizer.recognize_once_async().get()

# Did it succeeed
if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
    # Yes!
    print(f"Transcription:\n{result.text}")
else:
    # No. Try to determine why.
    print("Error transcribing message: {}".format(result.reason))
```

## Unit 4: Use the Text to Speech API

The **Text to speech** API for speech synthesis. Pattern similar to speech recognition:

1. Use a **`SpeechConfig`** object to encapsulate connection info: **location** and **key**.
2. Optionally use an **`AudioConfig`** to define the output device — defaults to **system speaker**; can specify an audio file, or set it explicitly to a **null value** to process the returned audio stream object directly.
3. Use `SpeechConfig` + `AudioConfig` to create a **`SpeechSynthesizer`** object — proxy client for Text to speech.
4. Call methods on `SpeechSynthesizer`. E.g., **`SpeakTextAsync()`** (Python: `speak_text_async()`) converts text to spoken audio.
5. Process the response — a **`SpeechSynthesisResult`** object with properties:
   - `AudioData`
   - `Properties`
   - `Reason`
   - `ResultId`

When successful, `Reason` == **`SynthesizingAudioCompleted`** and `AudioData` contains the audio stream (auto-routed to speaker/file depending on `AudioConfig`).

### Example — synthesizing text as speech

```python
import azure.cognitiveservices.speech as speechsdk

# Speech config encapsulates the connection to the resource
speech_config = speechsdk.SpeechConfig(subscription=KEY, endpoint=ENDPOINT)

# Audio output config determines where to send the audio stream (defaults to speaker)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# Use speech synthesizer to synthesize text as speech
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                                 audio_config=audio_config)
text = "My voice is my password!"
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

# Did it succeeed?
if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    # Yes!
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    # No - Ty to find out why not
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
```

Note: error handling here uses `speech_synthesis_result.cancellation_details.reason`, then checks for `CancellationReason.Error` and reads `.error_details` — a two-level cancellation diagnostic pattern distinct from the speech-to-text example's simpler `else` branch.

## Unit 5: Configure audio format and voices

Use `SpeechConfig` to customize synthesized audio.

### Audio format

Azure Speech supports multiple output formats for the synthesized audio stream, selectable by:
- Audio file type
- Sample-rate
- Bit-depth

```python
speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
```

Method: **`speech_config.set_speech_synthesis_output_format(...)`**, taking a **`SpeechSynthesisOutputFormat`** enum value (example shown: `Riff24Khz16BitMonoPcm`).

### Voices

Azure Speech provides multiple voices for personalizing speech-enabled apps. Voice names encode locale, person's name, and other details — example: **`en-US-Brian:DragonHDLatestNeural`**.

```python
speech_config.speech_synthesis_voice_name='en-US-Brian:DragonHDLatestNeural'
```

Property: **`speech_config.speech_synthesis_voice_name`**.

## Unit 6: Use Speech Synthesis Markup Language (SSML)

Beyond submitting plain text, the Speech SDK supports **SSML** — an XML-based syntax for describing speech characteristics, giving finer control over synthesized output:

- Specify a **speaking style** (e.g., "excited," "cheerful") with a neural voice.
- Insert **pauses/silence**.
- Specify **phonemes** (phonetic pronunciations) — e.g., pronounce "SQL" as "sequel."
- Adjust **prosody** (pitch, timbre, speaking rate).
- Use **"say-as"** rules — express a string as a date, time, telephone number, etc.
- Insert **recorded speech or audio** — e.g., standard recorded messages or simulated background noise.

### Example SSML

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" 
                     xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US"> 
    <voice name="en-US-AriaNeural"> 
        <mstts:express-as style="cheerful"> 
          I say tomato 
        </mstts:express-as> 
    </voice> 
    <voice name="en-US-GuyNeural"> 
        I say <phoneme alphabet="sapi" ph="t ao m ae t ow"> tomato </phoneme>. 
        <break strength="weak"/>Lets call the whole thing off! 
    </voice> 
</speak>
```

This produces a dialog between two neural voices:
- **Aria** (*cheerfully*): "I say tomato"
- **Guy**: "I say tomato (pronounced *tom-ah-toe*) ... Let's call the whole thing off!"

Key SSML elements shown: `<speak>` (root, with `version`, default xmlns, `xmlns:mstts` for Microsoft TTS extensions, `xml:lang`), `<voice name="...">`, `<mstts:express-as style="...">`, `<phoneme alphabet="sapi" ph="...">`, `<break strength="weak"/>`.

### Submitting SSML

```python
speech_synthesis_result = speech_synthesizer.speak_ssml_async('<speak>...').get()
```

Method: **`speech_synthesizer.speak_ssml_async(ssml_string)`** — distinct from `speak_text_async()` used for plain text.

## Unit 7: Exercise — Create a speech-enabled app

Hands-on exercise (~30 minutes): build a speech-enabled app implementing both speech recognition and synthesis. Requires an Azure subscription. Delivered via external lab launch link. Tip: delete resources after completing exploration.

## Unit 8: Module assessment

Standard graded quiz — interactive only, no extractable content.

## Unit 9: Summary

Recap — you learned how to:
- Connect to Azure Speech in Foundry Tools in a Foundry resource.
- Use the Speech to text API to implement speech recognition.
- Use the Text to speech API to implement speech synthesis.
- Configure audio format and voices.
- Use Speech Synthesis Markup Language (SSML).

Further reading: Azure Speech in Foundry Tools documentation (`/en-us/azure/ai-services/speech-service/`).
