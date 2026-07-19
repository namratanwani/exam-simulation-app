# Translate text and speech with Microsoft Foundry Tools

Source: https://learn.microsoft.com/en-us/training/modules/translate-text-speech/

## Learning objectives

After completing this module, you'll be able to:
- Identify options for translating text and speech in Microsoft Foundry Tools
- Use Azure Translator in Foundry Tools to translate text
- Use Azure Speech in Foundry Tools to translate speech

**Prerequisites**: Familiarity with Microsoft Foundry and Azure; programming experience.

## Exam relevance

Maps to **Learning Path 3 — Develop natural language solutions in Azure**. Supports:
- **"Implement text analysis solutions" (10–15%)** → *"Apply language model text analysis"*: *"Build solutions that translate text by using Azure Translator in Foundry Tools or LLM-powered translation flows"*.
- Same domain → *"Implement speech solutions"*: *"Translate speech into other languages by using language models and Foundry Tools"*.

Key exam distinction: **Azure Translator (text)** vs. **Azure Speech Translation API (spoken)** — different client objects, different config classes, different synthesis approaches (manual vs. event-based).

## Introduction

Automated ("machine") translation reduces the time/cost of manual translation but requires complex software understanding linguistic rules/idioms of both source and target languages. AI models are commonly at the core of both text-document and spoken-language translation solutions.

## Translation in Microsoft Foundry

While many LLMs can translate phrases/documents natively, **comprehensive** multi-language translation generally needs **specialized models**. Microsoft Foundry provides two dedicated Foundry Tools for this:

- **Azure Translator in Foundry Tools**: comprehensive text translation service; wide language support; supports **custom translation models**.
- **Azure Speech in Foundry Tools**: suite of speech tools including **speech-to-text** and **speech-to-speech translation in multiple languages simultaneously**.

Both are accessible through a Microsoft Foundry resource endpoint and provide REST APIs + language-specific SDKs.

## Translate text (Azure Translator)

Azure Translator provides an API for translating text across **90+ supported languages**. Capabilities:
- Translate **or transliterate** text using the **default translation model** or an **LLM**.
- Translate **documents** (sync or async) while **preserving document structure**.
- Use **custom translation models** for domain-specific terminology.

This module focuses on the **text translation** API specifically (not document translation).

### Foundry portal
Text translation and document translation **playgrounds** let you compare the default model vs. LLM results and view sample client code.

### SDKs
REST API, plus SDKs for **Python** (`azure-ai-translation-text`), **.NET**, **Java**, **JavaScript**.

### Connecting to Azure Translator
Endpoint options:
- **Global endpoint**: `api.cognitive.microsofttranslator.com`
- **Regional endpoints**: `api-nam.cognitive.microsofttranslator.com`, `api-apc.cognitive.microsofttranslator.com`, `api-eur.cognitive.microsofttranslator.com`
- **Foundry resource endpoint**: `{foundry-resource-name}.cognitiveservices.azure.com/`

Connect by endpoint OR by region:
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import *

key_credential = AzureKeyCredential("FOUNDRY_KEY")

# By Foundry resource endpoint
client = TextTranslationClient(credential=key_credential, endpoint="FOUNDRY_ENDPOINT")
# Or by region
client = TextTranslationClient(credential=key_credential, region="FOUNDRY_REGION")
```

### Determine available languages
`client.get_supported_languages(scope="translation")` returns a dict of language **name + ISO code** pairs.
```python
languages = client.get_supported_languages(scope="translation")
for language in languages.translation.keys():
    print(languages.translation[language].name + " (" + language + ")")
```

### Translate text
Use the **`translate`** method:
- Source text passed as a list of **`InputTextItem`** objects.
- Optional **`from_language`** (ISO code) — if omitted, Azure Translator **auto-detects** the source language.
- **`to_language`** — list of target language codes; a translation is returned for each valid code.

```python
input_text_elements = [InputTextItem(text="Hola"), InputTextItem(text="こんにちは")]
translation_results = client.translate(body=input_text_elements, to_language=["fr", "en"])
for translation in translation_results:
    sourceLanguage = translation.detected_language
    for translated_text in translation.translations:
        print(f"... translated from {sourceLanguage.language} to {translated_text.to} as '{translated_text.text}'.")
```
Detected sources in the example: Spanish (`es`) for "Hola", Japanese (`ja`) for "こんにちは" — each translated to both `fr` and `en`.

### Transliterate text
**Transliteration** = rendering text in a **different script**, not a different language (e.g., Japanese Hiragana → Latin script). Use the **`transliterate`** method with **`from_script`** and **`to_script`** parameters:
```python
transliteration_results = client.transliterate(
    body=input_text_elements, language="ja", from_script="Jpan", to_script="Latn")
```
Example: "こんにちは" (Jpan) → "Kon'nichiwa" (Latn). **Exam distinction: translate() changes language; transliterate() changes script/writing system while keeping the same language.**

## Translate speech (Azure Speech Translation API)

Azure Speech's **Speech Translation API** builds solutions that translate spoken input and return the translation as **text or speech**.

### Core objects
- **`TranslationRecognizer`** — performs the speech translation.
- **`SpeechTranslationConfig`** — connects to the Azure Speech resource (via `subscription` + `endpoint`, or `subscription` + `region`).
- **`AudioConfig`** — specifies the source audio stream (e.g., default microphone).

```python
import azure.cognitiveservices.speech as speech_sdk

translation_cfg = speech_sdk.translation.SpeechTranslationConfig(
    subscription="FOUNDRY_KEY", endpoint="FOUNDRY_ENDPOINT")
# or: subscription="FOUNDRY_KEY", region="FOUNDRY_REGION"
```

### Configure languages and input
```python
translation_cfg.speech_recognition_language = 'en-US'
translation_cfg.add_target_language('fr')
translation_cfg.add_target_language('ja')

audio_cfg = speech_sdk.AudioConfig(use_default_microphone=True)
```
Note: Speech Translation supports **multiple simultaneous target languages** via repeated `add_target_language()` calls — a key distinction from event-based synthesis (see below), which supports only one target language.

### Translate speech to text
```python
translator = speech_sdk.translation.TranslationRecognizer(
    translation_config=translation_cfg, audio_config=audio_cfg)
translation_results = translator.recognize_once_async().get()
translations = translation_results.translations
for translation_language in translations:
    print(f"{translation_language}: '{translations[translation_language]}'")
```

## Synthesize translations as speech (two approaches)

### 1. Manual synthesis
Combination of **two separate operations**: (1) `TranslationRecognizer` translates spoken input into text transcriptions for one or more target languages; (2) iterate the `Translations` results, using a **`SpeechSynthesizer`** (with its own `SpeechConfig` + `AudioOutputConfig`) to synthesize audio **per language**. Supports **multi-language** output — you can specify language-specific voices (e.g., `fr-FR-HenriNeural`, `ja-JP-NanamiNeural`) for correct pronunciation per target language.

```python
speech_cfg = speech_sdk.SpeechConfig(subscription="FOUNDRY_KEY", endpoint="FOUNDRY_ENDPOINT")
audio_out_cfg = speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
voices = {"fr": "fr-FR-HenriNeural", "ja": "ja-JP-NanamiNeural"}

for translation_language in translations:
    speech_cfg.speech_synthesis_voice_name = voices.get(translation_language)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_cfg, audio_out_cfg)
    speak = speech_synthesizer.speak_text_async(translations[translation_language]).get()
```

### 2. Event-based synthesis
For **1:1 translation only** (one source → one target language — **cannot** be used for multi-language translation, unlike manual synthesis). Steps:
- Specify the desired voice in the `TranslationConfig` (via `voice_name`).
- Register an event handler on the `TranslationRecognizer`'s **`synthesizing`** event.
- In the handler, use **`evt.result.audio`** to retrieve the byte stream of translated audio.

```python
translation_cfg.voice_name = "fr-FR-HenriNeural"
translator = speech_sdk.translation.TranslationRecognizer(translation_config=translation_cfg, audio_config=audio_cfg)

def synthesis_callback(evt):
    size = len(evt.result.audio)
    if size > 0:
        with open(output_file, 'wb+') as file:
            file.write(evt.result.audio)

translator.synthesizing.connect(synthesis_callback)
translation_results = translator.recognize_once()
```

**Exam-relevant comparison table:**

| Approach | Target languages | How it works |
|---|---|---|
| Manual synthesis | Multiple simultaneous | `TranslationRecognizer` (text) + separate `SpeechSynthesizer` per language |
| Event-based synthesis | Single (1:1) only | `synthesizing` event handler on `TranslationRecognizer`, reads `evt.result.audio` |

## Exercise (lab, hands-on)
30-minute lab building apps that use Microsoft Foundry tools to translate text and speech. Requires an Azure subscription.

## Summary
Covered how to use **Azure Translator in Foundry Tools** for text translation (including transliteration and multi-target-language translate calls) and **Azure Speech in Foundry Tools** for speech translation (speech-to-text translation plus manual vs. event-based speech synthesis of translations).

### Further reading
- Azure Translator in Foundry Tools documentation
- Azure Speech in Foundry Tools translation documentation
