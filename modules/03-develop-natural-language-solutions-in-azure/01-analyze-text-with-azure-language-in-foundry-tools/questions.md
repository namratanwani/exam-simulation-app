# Practice questions — Analyze text with Azure Language in Foundry Tools

## Unit 1–2: Introduction / Azure Language in Microsoft Foundry Tools

**Q1.** Which Python package do you install to use the Azure Language client library for text analytics?
A. `azure-ai-language`
B. `azure-ai-textanalytics`
C. `azure-cognitiveservices-language`
D. `azure-text-analytics-sdk`
**Answer:** B — The module explicitly instructs `pip install azure-ai-textanalytics` and imports `from azure.ai.textanalytics import TextAnalyticsClient`. The other package names do not exist as documented in this module.

**Q2.** Which three capabilities does the module identify as the current (non-deprecated) focus of Azure Language in Foundry Tools?
A. Language detection
B. Named entity recognition
C. Sentiment analysis
D. PII extraction
E. Text summarization
**Answer:** A, B, D — The module states Azure Language "also provides functionality for sentiment analysis, summarization, key phrase extraction... these deprecated capabilities are provided to support existing applications," explicitly separating them from the three capabilities taught (language detection, NER, PII extraction).

**Q3.** You have a Foundry project endpoint of `https://contoso-foundry.services.ai.azure.com/api/projects/contoso-app`. What is the underlying Foundry resource endpoint?
A. `https://contoso-foundry.services.ai.azure.com`
B. `https://contoso-app.services.ai.azure.com`
C. `https://contoso-foundry.services.ai.azure.com/api/projects`
D. `https://contoso-foundry.services.ai.azure.com/resource`
**Answer:** A — The module states the project endpoint equals the resource endpoint with `/api/projects/{project_name}` appended, so stripping that suffix gives the resource endpoint.

**Q4.** Which authentication method does Microsoft recommend for production Azure Language solutions, per this module?
A. `AzureKeyCredential` with a static key stored in application settings
B. Shared Access Signature (SAS) tokens issued by the storage account
C. Microsoft Entra ID authentication using `DefaultAzureCredential`
D. Anonymous access secured only by network-level IP allow-listing rules
**Answer:** C — The module states "For greater security in production solutions, Microsoft recommends using Microsoft Entra ID authentication," demonstrated via `DefaultAzureCredential`.

**Q5.** Which class do you instantiate to submit requests to Azure Language APIs from Python code?
A. `LanguageServiceClient`
B. `TextAnalyticsClient`
C. `CognitiveServicesClient`
D. `AzureLanguageClient`
**Answer:** B — Both code examples create `client = TextAnalyticsClient(endpoint=..., credential=...)`.

**Q6.** True statement about the project vs. resource key in Microsoft Foundry, according to this module:
A. The project key and the parent resource key are different and must be rotated independently.
B. The project key and the parent Foundry resource key are the same value.
C. Only the resource has a key; projects use certificates only.
D. Keys are only visible via the Azure CLI, never in the portal.
**Answer:** B — The module explicitly says "The project and foundry resource keys are the same."

**Q21.** Which NuGet package provides the .NET client library for Azure Language text analytics?
A. Microsoft.Azure.TextAnalytics
B. Azure.AI.TextAnalytics
C. Azure.Language.Text
D. Microsoft.CognitiveServices.TextAnalytics
**Answer:** B — The module lists "Microsoft Azure Text Analytics Client Library for .NET — NuGet package `Azure.AI.TextAnalytics`."

**Q22.** Which npm package provides the JavaScript client library for Azure Language text analytics?
A. @azure/ai-language
B. @azure/text-analytics
C. @azure/ai-text-analytics
D. @azure/cognitiveservices-textanalytics
**Answer:** C — The module lists "Microsoft Azure Text Analytics Client Library for JavaScript — npm package `@azure/ai-text-analytics`."

**Q23.** In the Foundry portal, where do you go to view the endpoint and key for the parent Foundry *resource* (as opposed to the project)?
A. The Overview tab of the project home page
B. The Admin tab of the Operate page
C. Azure Portal > Access control (IAM)
D. The Deployments tab in the project pane
**Answer:** B — "To see the key/endpoint for the parent resource, view it under the Admin tab of the Operate page."

**Q24.** Per this module, which two mechanisms can you use to call Azure Language APIs?
A. JSON REST requests
B. A language-specific SDK
C. GraphQL queries
D. gRPC calls
**Answer:** A, B — "You can call the APIs either via JSON REST requests or via a language-specific SDK."

## Unit 3: Detect language

**Q7.** What is the maximum character size per document accepted by the Azure Language detect-language operation, per this module?
A. 1,024 characters
B. 5,120 characters
C. 10,000 characters
D. 50,000 characters
**Answer:** B — The module states "the document size must be under 5,120 characters."

**Q8.** How many documents (IDs) can a single collection/batch contain when calling the language detection API, per this module?
A. Up to 100
B. Up to 500
C. 1,000
D. 5,120
**Answer:** C — "each collection is restricted to 1,000 items (IDs)."

**Q9.** You submit the multilingual sentence "I know a cool AI developer. He has a certain je ne sais quoi!" to `detect_language`. What behavior should you expect?
A. The call fails with a 400 Bad Request because mixed-language input isn't supported.
B. It returns the language with the largest representation in the content, with a lower confidence score.
C. It returns two separate primary_language results, one per detected language.
D. It always returns `(unknown)` with a score of 0, regardless of how many recognizable languages are present.
**Answer:** B — The module states mixed-language content "returns the language with the largest representation in the content, but with a lower positive rating, reflecting the marginal strength of that assessment."

**Q10.** If text submitted to `detect_language` can't be parsed (e.g., due to character-encoding issues), what does the API return for the primary language name/ISO code and confidence score?
A. The name/code default to "en" and score of 0.5
B. The response silently omits the document entirely from the returned collection
C. Name and ISO code are returned as `(unknown)` and score is `0`
D. It throws an unrecoverable exception that terminates the batch request
**Answer:** C — The module explicitly documents this exact fallback behavior.

**Q11.** Which method on `TextAnalyticsClient` is used to detect the language of submitted documents?
A. `client.analyze_language(documents=documents)`
B. `client.detect_language(documents=documents)`
C. `client.identify_language(documents=documents)`
D. `client.language_detect(text=documents)`
**Answer:** B — Shown verbatim in the code sample.

**Q25.** The confidence score returned by the language detection API falls within which range?
A. 0–1
B. 0–100
C. -1 to 1
D. 1–10
**Answer:** A — Example scores shown are 0.9 and 0.98, and the module describes it as a confidence score between 0 and 1.

**Q26.** Which use cases does the module cite for the language detection API? (Choose two.)
A. Determining the language of arbitrary text in a content store where the language is unknown
B. Detecting a chat user's language at session start to configure responses appropriately
C. Translating text between languages
D. Generating summaries of foreign-language documents
**Answer:** A, B — The module lists exactly these two use cases for language detection.

## Unit 4: Extract entities

**Q12.** Which method is used to perform Named Entity Recognition against a batch of documents?
A. `client.extract_entities(documents=documents)`
B. `client.get_entities(documents=documents)`
C. `client.recognize_entities(documents=documents)`
D. `client.analyze_entities(documents=documents)`
**Answer:** C — Shown in the code sample: `response = client.recognize_entities(documents=documents)`.

**Q13.** In the sample output, "CEO" is categorized under which entity category?
A. PersonName
B. Organization
C. PersonType
D. JobTitle
**Answer:** C — Output shows `- CEO (PersonType)`.

**Q14.** Given the entity recognition response object `doc`, which attributes let you print each entity's text and category?
A. `doc.text` and `doc.type` (iterating the response object directly)
B. `entity.value` and `entity.label` (iterating `doc.results`)
C. `entity.text` and `entity.category` (iterating `doc.entities`)
D. `doc.entity_text` and `doc.entity_category` attributes
**Answer:** C — The sample loops `for entity in doc.entities: print(f" - {entity.text} ({entity.category})")`.

**Q15.** Which of the following are entity categories explicitly shown in this module's NER example output? (Choose three.)
A. Organization
B. Location
C. DateTime
D. Product
E. Currency
**Answer:** A, B, C — The output lists Organization, DateTime, Person, Location, and PersonType; Product and Currency are not shown in this module's examples.

**Q27.** Beyond what appears in the sample output, which entity categories does the module explicitly name as examples of NER categories? (Choose three.)
A. Address
B. Email
C. URL
D. Currency
E. Product
**Answer:** A, B, C — The module's bulleted list of NER categories includes Person, Location, DateTime, Organization, Address, Email, and URL; Currency and Product are not mentioned.

## Unit 5: Extract PII

**Q16.** Which method call both extracts PII entities AND makes the redacted text available in the same response, per this module?
A. `client.redact_pii_entities(documents=documents)` then a separate `recognize_pii_entities` call
B. `client.recognize_pii_entities(documents=documents, language="en")` — response includes both `.entities` and `.redacted_text`
C. `client.mask_entities(documents=documents)`, which returns only masked text with no entity metadata
D. `client.recognize_entities(documents=documents, redact=True)` for combined extraction and redaction
**Answer:** B — The same `recognize_pii_entities` response object exposes both `doc.entities` (for extraction/analysis) and `doc.redacted_text` (the masked text) — no separate redaction call is shown or needed.

**Q17.** In the PII example, what category is assigned to `123-45-6789`?
A. `PhoneNumber` (US format)
B. `CreditCardNumber`
C. `USSocialSecurityNumber`
D. `NationalID` (generic)
**Answer:** C — Output: `- 123-45-6789: USSocialSecurityNumber (confidence: 0.99)`.

**Q18.** What parameter, explicitly passed in the PII code sample (but not shown in the earlier NER example), specifies the document language for PII recognition?
A. `locale="en-US"`
B. `language="en"`
C. `lang_code="en"`
D. `iso6391_name="en"`
**Answer:** B — `client.recognize_pii_entities(documents=documents, language="en")`.

**Q19.** Which attribute on a returned entity gives the model's certainty for a detected PII item?
A. `entity.score` (legacy alias)
B. `entity.confidence_score`
C. `entity.probability`
D. `entity.certainty`
**Answer:** B — Shown as `entity.confidence_score:.2f` in the code and output (e.g., "confidence: 0.99").

**Q20.** A compliance application must both flag sensitive fields for a review queue AND produce a safely shareable version of a support ticket. Which single Azure Language operation satisfies both needs without additional API calls?
A. `recognize_entities` followed by a custom regex-based masking pass over the entity text
B. `recognize_pii_entities`, using `.entities` for the review queue and `.redacted_text` for the shareable version
C. `detect_language` combined with `recognize_entities`, then manually filtering by category
D. Two separate calls: `extract_pii()` for detection and `redact_text()` for masking
**Answer:** B — As documented, a single `recognize_pii_entities` call returns both the categorized entity list (for review) and the redacted text (for safe sharing).

**Q28.** Which categories of sensitive information does the module state Azure Language PII detection can identify? (Choose three.)
A. Names
B. Credit card numbers
C. Social security numbers
D. IP addresses
E. Passwords
**Answer:** A, B, C — The module states PII detection identifies "names, addresses, phone numbers, email addresses, social security numbers, and credit card numbers." IP addresses and passwords are not mentioned.

**Q29.** By default, how does `recognize_pii_entities` represent redacted PII in `doc.redacted_text`?
A. Replaced with the entity category name in brackets, e.g. `[Person]`
B. Replaced with asterisks (or a specified character)
C. Removed entirely with no placeholder
D. Replaced with the literal string "REDACTED"
**Answer:** B — The module states "The service can return a redacted version of the text with PII replaced by asterisks (or a specified character)," and the sample output shows runs of `*` characters.

## Scenario questions

**Q30.** You're building a customer-support intake pipeline. Incoming tickets arrive in an unknown language, need entities extracted for routing, and must have PII stripped before long-term storage. Which sequence of `TextAnalyticsClient` calls best fits this requirement?
A. Call `recognize_pii_entities` only — it also detects language automatically and extracts entities
B. Call `detect_language`, then `recognize_entities` for routing, then `recognize_pii_entities` and store `doc.redacted_text`
C. Call `recognize_entities` followed by a manual, regex-based PII scrubbing pass before storage
D. Call `detect_language` only, since its response object includes entities and redacted text fields
**Answer:** B — Each Azure Language operation covered in this module is a distinct call with a distinct purpose; language detection, entity recognition, and PII extraction/redaction are three separate API calls, chained here to satisfy all three requirements.

**Q31.** Your production application runs under a system-assigned managed identity in Azure and must avoid storing static secrets in configuration. How should you construct the `TextAnalyticsClient`?
A. `AzureKeyCredential` with the key stored in an environment variable on the host
B. `DefaultAzureCredential()` from `azure-identity`, passed as the `credential` to `TextAnalyticsClient`
C. An anonymous credential relying solely on network-level IP address restrictions
D. A SAS token generated from an Azure Storage account and rotated manually
**Answer:** B — The module recommends Microsoft Entra ID authentication via `DefaultAzureCredential` for production for greater security, avoiding static keys entirely.

**Q32.** You submit two documents to `detect_language`: one mixing roughly equal French and English text, and one that is garbled due to a character-encoding bug. What should you expect for each, per this module?
A. Both documents return `(unknown)` for the name and ISO code, each with a confidence score of exactly 0, regardless of content
B. The mixed-language document returns its dominant language with a lower confidence score; the garbled document returns `(unknown)` name/ISO code with a score of `0`
C. Both calls throw an unrecoverable exception that immediately terminates the entire batch request without returning partial results
D. The mixed-language document returns two separate `primary_language` results; the garbled one defaults to English with a score of 1.0
**Answer:** B — These are the two distinct edge-case behaviors the module documents separately for language detection.

**Q33.** You need a list of flagged sensitive terms for a manual-review dashboard AND a scrubbed version of the same ticket text for a public-facing chatbot transcript log, while minimizing API calls. What is the most efficient approach using this module's APIs?
A. Call `recognize_entities` for the dashboard and a separate `recognize_pii_entities` call for redaction
B. Call `recognize_pii_entities` once; use `doc.entities` for the dashboard and `doc.redacted_text` for the chatbot log
C. Call `detect_language`, then `recognize_pii_entities` twice — once for entities, once for redacted text
D. This isn't possible with the Azure Language SDK; it requires a separate generative model integration
**Answer:** B — A single `recognize_pii_entities` response provides both the entity list and the redacted text simultaneously, so one call satisfies both needs.
