# Practice questions — Translate text and speech with Microsoft Foundry Tools

## Translation in Microsoft Foundry

**Q1.** Which two Foundry Tools does Microsoft Foundry provide for comprehensive multi-language translation, and what does each primarily handle?
A. Azure AI Search (text) and Azure Vision (speech) — neither is the Foundry Tool this module actually uses for translation
B. Azure Translator in Foundry Tools (text translation) and Azure Speech in Foundry Tools (speech-to-text and speech-to-speech translation)
C. Azure Content Understanding (text) and Azure Document Intelligence (speech) — both extract structured data rather than translate language
D. Azure OpenAI (text) and Azure Bot Service (speech) — neither is the dedicated translation-focused Foundry Tool this module describes
**Answer:** B — Azure Translator handles comprehensive text translation with custom model support; Azure Speech handles speech-to-text and simultaneous multi-language speech-to-speech translation.

**Q2.** Why does the module state that comprehensive multi-language translation solutions generally require specialized models, even though many LLMs can translate phrases or documents?
A. LLMs cannot process any non-English text at all — an overstatement, since many LLMs do support multiple languages to some extent
B. LLMs generally lack the depth needed for comprehensive, wide-language-range translation compared to purpose-built translation services
C. LLMs are more expensive than every translation-specific service in all cases — a cost claim the module never actually makes
D. Specialized models are required by law for any Azure deployment — there's no such legal requirement described anywhere in the module
**Answer:** B — The module notes that while LLMs can translate, comprehensive solutions generally require the specialized translation models that Foundry Tools like Azure Translator provide.

## Translate text (Azure Translator)

**Q3.** How many languages does Azure Translator in Foundry Tools support for text translation, per this module?
A. Over 20
B. Over 50
C. Over 90
D. Over 200
**Answer:** C — The module states Azure Translator supports translation between over 90 languages.

**Q4.** Which Azure Translator capability lets you translate domain-specific terminology accurately for a specialized industry vocabulary?
A. The default translation model only
B. Custom translation models
C. Transliteration
D. The `get_supported_languages` method
**Answer:** B — Custom translation models are specifically called out for translating domain-specific terms.

**Q5.** Which of the following are valid ways to connect a `TextTranslationClient` to Azure Translator, per the module's code examples? (Choose two.)
A. By specifying a Foundry resource `endpoint`
B. By specifying a `region`
C. By specifying only a username and password
D. By specifying a Kubernetes namespace
**Answer:** A, B — The `TextTranslationClient` constructor examples show connecting either via `endpoint=` or via `region=`, both with an `AzureKeyCredential`.

**Q6.** What is the global endpoint hostname for Azure Translator, per this module?
A. `api.cognitive.microsofttranslator.com`
B. `translator.azure.com`
C. `api.translator.azure.com`
D. `cognitiveservices.translator.com`
**Answer:** A — The module lists "Global endpoint: `api.cognitive.microsofttranslator.com`."

**Q7.** Which of the following are regional endpoints for Azure Translator mentioned in this module? (Choose three.)
A. `api-nam.cognitive.microsofttranslator.com`
B. `api-apc.cognitive.microsofttranslator.com`
C. `api-eur.cognitive.microsofttranslator.com`
D. `api-latam.cognitive.microsofttranslator.com`
**Answer:** A, B, C — The module lists exactly these three regional endpoints (nam, apc, eur); a `latam` regional endpoint is not mentioned.

**Q8.** Which PyPI package provides the Python SDK for Azure Translator text translation, per this module?
A. `azure-ai-translation-text`
B. `azure-cognitiveservices-translator`
C. `azure-translator-text`
D. `azure-ai-textanalytics`
**Answer:** A — The module states SDKs exist for "Python (`azure-ai-translation-text`), .NET, Java, JavaScript."

**Q9.** When calling the `translate` method without specifying the `from_language` parameter, what happens?
A. The call fails with an error
B. Azure Translator automatically detects the source language
C. The source language defaults to English regardless of actual input
D. Only transliteration is performed instead of translation
**Answer:** B — Omitting `from_language` causes Azure Translator to auto-detect the source language, as shown in the module's example with unspecified-language inputs.

**Q10.** Which method call returns a dictionary of supported language name/ISO-code pairs for Azure Translator?
A. `client.list_languages()`
B. `client.get_supported_languages(scope="translation")`
C. `client.languages()`
D. `client.supported_languages`
**Answer:** B — Shown in the module: `languages = client.get_supported_languages(scope="translation")`.

**Q11.** In the Foundry portal, what do the text translation and document translation playgrounds let you do?
A. Compare results from the default translation model vs. an LLM, and view sample client code
B. Train a custom translation model from scratch entirely within the portal
C. Deploy a new Azure Speech resource
D. Configure Voice Live avatar sessions
**Answer:** A — "Text translation and document translation playgrounds let you compare the default model vs. LLM results and view sample client code."

**Q12.** In the module's `translate` example, which source languages were auto-detected for the inputs "Hola" and "こんにちは" respectively?
A. Spanish (`es`) and Japanese (`ja`)
B. Portuguese (`pt`) and Chinese (`zh`)
C. Italian (`it`) and Korean (`ko`)
D. French (`fr`) and Japanese (`ja`)
**Answer:** A — "Detected sources in the example: Spanish (es) for 'Hola', Japanese (ja) for 'こんにちは' — each translated to both fr and en."

**Q13.** In the `translate` method, what type of object represents each piece of source text to be translated, and what parameter specifies the target language(s)?
A. `TextBlock` objects; `target_lang` parameter (not the names used in this module's actual code)
B. `InputTextItem` objects; `to_language` parameter (a list of language codes)
C. `TranslationRequest` objects; `destination` parameter (not the parameter names shown in the module's example)
D. Raw strings only; no target-language parameter needed (the example always passes `to_language` explicitly)
**Answer:** B — Source text is passed as a list of `InputTextItem` objects, and `to_language` takes a list of target language codes, returning one translation per valid code.

**Q14.** What is the key conceptual difference between the `translate` method and the `transliterate` method in Azure Translator?
A. They are functionally identical; `transliterate` is just a deprecated alias for `translate` with no distinct behavior of its own
B. `translate` converts text to a different language; `transliterate` renders text in a different script/writing system while keeping the same language
C. `translate` only works for speech, while `transliterate` only works for text — reversed from how the module actually describes each method's scope
D. `transliterate` requires an LLM, while `translate` never uses one — neither method in this module involves calling an LLM at all
**Answer:** B — Transliteration changes the writing script (e.g., Japanese Hiragana to Latin script) without changing the language, distinct from translation which changes the language itself.

**Q15.** In the `transliterate` method example converting Japanese Hiragana text to Latin script, which parameters specify the source and target scripts?
A. `source_lang` and `target_lang`
B. `from_script="Jpan"` and `to_script="Latn"`
C. `input_script` and `output_script`
D. `encoding_from` and `encoding_to`
**Answer:** B — The example uses `from_script="Jpan"` and `to_script="Latn"` alongside a `language="ja"` parameter.

**Q16.** Which Azure Translator capability allows translating entire documents (synchronously or asynchronously) while maintaining the original document structure?
A. The `transliterate` method
B. Document translation
C. The `get_supported_languages` method
D. Event-based synthesis
**Answer:** B — Document translation is explicitly listed as a distinct capability from text translation, supporting both sync and async modes while preserving structure. (Note: this module's hands-on focus is the text translation API specifically, but document translation is mentioned as part of Azure Translator's broader capability set.)

## Translate speech (Azure Speech Translation API)

**Q17.** Which three core objects work together to perform speech translation using the Azure Speech Translation API?
A. `SpeechConfig`, `SpeechRecognizer`, `SpeechSynthesizer`
B. `SpeechTranslationConfig`, `AudioConfig`, `TranslationRecognizer`
C. `TextTranslationClient`, `InputTextItem`, `AzureKeyCredential`
D. `AIProjectClient`, `PromptAgentDefinition`, `DefaultAzureCredential`
**Answer:** B — `SpeechTranslationConfig` connects to the Azure Speech resource, `AudioConfig` specifies the audio source, and `TranslationRecognizer` performs the actual translation.

**Q18.** How many target languages can a single `SpeechTranslationConfig` be configured to translate speech into simultaneously, based on the module's example using `add_target_language`?
A. Exactly one, always
B. Multiple — the example adds both 'fr' and 'ja' as target languages simultaneously
C. Zero — target languages must be configured separately per request
D. Only languages that share the same script as the source
**Answer:** B — `add_target_language()` can be called multiple times to configure multiple simultaneous target languages, as shown translating English speech into both French and Japanese at once.

**Q19.** What are the two valid ways shown to connect a `SpeechTranslationConfig` to an Azure Speech resource?
A. Only via a `region` parameter
B. Via `subscription` + `endpoint`, or via `subscription` + `region`
C. Via a REST API key embedded directly in the audio stream
D. Via Microsoft Entra ID only; API keys are not supported
**Answer:** B — The module shows both an endpoint-based and a region-based constructor pattern for `SpeechTranslationConfig`, both using a `subscription` key.

## Synthesize translations as speech

**Q20.** What are the two approaches described for synthesizing spoken translations from an Azure Speech translation result?
A. Manual synthesis and event-based synthesis
B. Batch synthesis and streaming synthesis
C. Local synthesis and cloud synthesis
D. Synchronous synthesis and asynchronous synthesis
**Answer:** A — Manual synthesis (recognize text, then synthesize each language's text separately) and event-based synthesis (capture audio via a `synthesizing` event handler) are the two approaches covered.

**Q21.** Which speech-synthesis approach can handle MULTIPLE target languages, and which is restricted to a single (1:1) target language only?
A. Both approaches support multiple languages equally — the module doesn't describe any such symmetry between manual and event-based synthesis
B. Manual synthesis supports multiple languages (via a separate `SpeechSynthesizer` per language); event-based synthesis supports only one target language
C. Event-based synthesis supports multiple languages; manual synthesis supports only one — this reverses the module's actual 1:1 vs. multi-language distinction
D. Neither approach supports more than one language — but manual synthesis explicitly loops over multiple target-language translations in the example
**Answer:** B — Manual synthesis iterates all target-language translations and synthesizes each separately, while event-based synthesis is explicitly stated as usable only for 1:1 translation.

**Q22.** In manual synthesis, what is used to ensure correct pronunciation for each target language's synthesized speech output?
A. A single default voice applied to all languages, regardless of which target language is being synthesized
B. Language-specific voice names (e.g., `fr-FR-HenriNeural`, `ja-JP-NanamiNeural`) mapped per target language
C. Automatic voice detection with no configuration needed — the example always sets voice names explicitly, never automatically
D. The same voice used for speech recognition input, reused unchanged for every target-language synthesis output
**Answer:** B — The module's example maps target-language codes to specific neural voice names to optimize pronunciation per language.

**Q23.** In event-based synthesis, which event on the `TranslationRecognizer` object must you handle to capture the synthesized translated audio, and what property provides the audio byte stream?
A. The `recognized` event; `evt.result.text`
B. The `synthesizing` event; `evt.result.audio`
C. The `session_started` event; `evt.audio_config`
D. The `canceled` event; `evt.error_details`
**Answer:** B — You connect a handler to the `synthesizing` event, and within it, `evt.result.audio` (via `GetAudio()`/`.audio`) provides the byte stream of translated audio.

**Q24.** Where must the target voice be specified when using event-based synthesis for speech-to-speech translation?
A. It cannot be specified — a default voice is always used
B. In the `TranslationConfig`, via its `voice_name` property
C. As a parameter passed directly to the `synthesizing` event handler
D. In a separate `SpeechSynthesizer` object, just like manual synthesis
**Answer:** B — Event-based synthesis requires setting `voice_name` on the `TranslationConfig` itself (e.g., `translation_cfg.voice_name = "fr-FR-HenriNeural"`), unlike manual synthesis which uses a separate `SpeechSynthesizer`/`SpeechConfig`.

## Scenario / synthesis

**Q25.** A developer needs to translate a live English phone call into both French and Spanish text simultaneously for two different support agents to read, with no audio output required. Which combination of Azure Speech objects should they use, and do they need `SpeechSynthesizer` at all?
A. `SpeechTranslationConfig` (with two `add_target_language` calls) + `AudioConfig` + `TranslationRecognizer`; no `SpeechSynthesizer` needed since only text output is required
B. Only a `SpeechSynthesizer`, since translation always requires synthesis — but `SpeechSynthesizer` alone can't recognize or translate speech, and no audio output is needed here
C. `TextTranslationClient` with `InputTextItem`, since this is a text-only translation problem — but the source here is live spoken audio, not text, so a speech-capable client is required
D. Event-based synthesis with two `TranslationConfig.voice_name` values set simultaneously — but event-based synthesis only supports one target language and one voice_name value
**Answer:** A — Since only translated text output is needed (not audio), `TranslationRecognizer` with multiple target languages configured is sufficient; synthesis (manual or event-based) is only needed when spoken audio output is required. Option D is also invalid because event-based synthesis supports only one target language, and voice_name isn't a multi-value property.

**Q26.** A developer wants real-time spoken audio output translated from English into French only, choosing between manual and event-based synthesis. Which approach is more appropriate given the single-language, audio-focused requirement, and why?
A. Manual synthesis, because it's the only approach that produces any audio at all — untrue, since event-based synthesis also produces an audio stream via its synthesizing event
B. Event-based synthesis, because it's designed for 1:1 (single target language) translation and directly captures the synthesized audio stream via the `synthesizing` event
C. Neither approach works for single-language speech-to-speech translation — both approaches actually support this exact single-target-language case
D. Manual synthesis is required because event-based synthesis only works with text output — but event-based synthesis specifically produces audio, not text
**Answer:** B — Event-based synthesis is specifically suited to 1:1 translation scenarios and directly provides the audio stream through its event handler, making it a more targeted fit than the more general manual synthesis approach (which is required only when multiple target languages need separate synthesis).

**Q27.** You need to both translate a Japanese customer review into English text AND provide the original-language review rendered in Latin script for a team that reads Romanized Japanese but doesn't read Japanese script. Which two Azure Translator methods would you call?
A. `translate()` only, since it also transliterates as a side effect — but `translate()` changes language, it never renders text in a different script
B. `translate()` to get the English text, and `transliterate()` (`from_script="Jpan"`, `to_script="Latn"`) to get the Romanized original-language text
C. `transliterate()` only, since it also changes language — but `transliterate()` explicitly keeps the same language and only changes the writing script
D. `get_supported_languages()` to auto-produce a transliteration — that method only lists supported language codes, it performs no translation or transliteration
**Answer:** B — `translate()` changes language (Japanese → English); `transliterate()` changes script while keeping the same language (Japanese in Hiragana/Kanji → Japanese in Latin script) — these are the two distinct, non-overlapping operations this module describes.

**Q28.** Your app must connect to Azure Translator without embedding an endpoint URL, using only the resource's region. Which constructor call is correct, per this module's code sample?
A. `TextTranslationClient(credential=key_credential, endpoint="FOUNDRY_ENDPOINT")`
B. `TextTranslationClient(credential=key_credential, region="FOUNDRY_REGION")`
C. `TextTranslationClient(credential=key_credential, global_endpoint=True)`
D. `TextTranslationClient(region="FOUNDRY_REGION")` with no credential argument
**Answer:** B — The module's alternate constructor pattern is `client = TextTranslationClient(credential=key_credential, region="FOUNDRY_REGION")`, still requiring the `AzureKeyCredential`.
