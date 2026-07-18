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
A. `AzureKeyCredential` with a static key
B. Shared Access Signature (SAS) tokens
C. Microsoft Entra ID authentication using `DefaultAzureCredential`
D. Anonymous access with IP allow-listing
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

## Unit 3: Detect language

**Q7.** What is the maximum character size per document accepted by the Azure Language detect-language operation, per this module?
A. 1,024 characters
B. 5,120 characters
C. 10,000 characters
D. 50,000 characters
**Answer:** B — The module states "the document size must be under 5,120 characters."

**Q8.** How many documents (IDs) can a single collection/batch contain when calling the language detection API, per this module?
A. 100
B. 500
C. 1,000
D. 5,120
**Answer:** C — "each collection is restricted to 1,000 items (IDs)."

**Q9.** You submit the multilingual sentence "I know a cool AI developer. He has a certain je ne sais quoi!" to `detect_language`. What behavior should you expect?
A. The call fails with a 400 Bad Request because mixed-language input isn't supported.
B. It returns the language with the largest representation in the content, with a lower confidence score.
C. It returns two separate primary_language results, one per detected language.
D. It always returns `(unknown)` with a score of 0.
**Answer:** B — The module states mixed-language content "returns the language with the largest representation in the content, but with a lower positive rating, reflecting the marginal strength of that assessment."

**Q10.** If text submitted to `detect_language` can't be parsed (e.g., due to character-encoding issues), what does the API return for the primary language name/ISO code and confidence score?
A. The name/code default to "en" and score of 0.5
B. The response omits the document entirely
C. Name and ISO code are returned as `(unknown)` and score is `0`
D. It throws an unrecoverable exception
**Answer:** C — The module explicitly documents this exact fallback behavior.

**Q11.** Which method on `TextAnalyticsClient` is used to detect the language of submitted documents?
A. `client.analyze_language()`
B. `client.detect_language(documents=documents)`
C. `client.identify_language(documents=documents)`
D. `client.language_detect(text=documents)`
**Answer:** B — Shown verbatim in the code sample.

## Unit 4: Extract entities

**Q12.** Which method is used to perform Named Entity Recognition against a batch of documents?
A. `client.extract_entities()`
B. `client.get_entities()`
C. `client.recognize_entities(documents=documents)`
D. `client.analyze_entities(documents=documents)`
**Answer:** C — Shown in the code sample: `response = client.recognize_entities(documents=documents)`.

**Q13.** In the sample output, "CEO" is categorized under which entity category?
A. Person
B. Organization
C. PersonType
D. Title
**Answer:** C — Output shows `- CEO (PersonType)`.

**Q14.** Given the entity recognition response object `doc`, which attributes let you print each entity's text and category?
A. `doc.text` and `doc.type`
B. `entity.value` and `entity.label`
C. `entity.text` and `entity.category` (iterating `doc.entities`)
D. `doc.entity_text` and `doc.entity_category`
**Answer:** C — The sample loops `for entity in doc.entities: print(f" - {entity.text} ({entity.category})")`.

**Q15.** Which of the following are entity categories explicitly shown in this module's NER example output? (Choose three.)
A. Organization
B. Location
C. DateTime
D. Product
E. Currency
**Answer:** A, B, C — The output lists Organization, DateTime, Person, Location, and PersonType; Product and Currency are not shown in this module's examples.

## Unit 5: Extract PII

**Q16.** Which method call both extracts PII entities AND makes the redacted text available in the same response, per this module?
A. `client.redact_pii_entities(documents=documents)` then a separate `recognize_pii_entities` call
B. `client.recognize_pii_entities(documents=documents, language="en")` — response includes both `.entities` and `.redacted_text`
C. `client.mask_entities(documents=documents)`
D. `client.recognize_entities(documents=documents, redact=True)`
**Answer:** B — The same `recognize_pii_entities` response object exposes both `doc.entities` (for extraction/analysis) and `doc.redacted_text` (the masked text) — no separate redaction call is shown or needed.

**Q17.** In the PII example, what category is assigned to `123-45-6789`?
A. `PhoneNumber`
B. `CreditCardNumber`
C. `USSocialSecurityNumber`
D. `NationalID`
**Answer:** C — Output: `- 123-45-6789: USSocialSecurityNumber (confidence: 0.99)`.

**Q18.** What parameter, explicitly passed in the PII code sample (but not shown in the earlier NER example), specifies the document language for PII recognition?
A. `locale="en-US"`
B. `language="en"`
C. `lang_code="en"`
D. `iso6391_name="en"`
**Answer:** B — `client.recognize_pii_entities(documents=documents, language="en")`.

**Q19.** Which attribute on a returned entity gives the model's certainty for a detected PII item?
A. `entity.score`
B. `entity.confidence_score`
C. `entity.probability`
D. `entity.certainty`
**Answer:** B — Shown as `entity.confidence_score:.2f` in the code and output (e.g., "confidence: 0.99").

**Q20.** A compliance application must both flag sensitive fields for a review queue AND produce a safely shareable version of a support ticket. Which single Azure Language operation satisfies both needs without additional API calls?
A. `recognize_entities` followed by manual regex masking
B. `recognize_pii_entities`, using `.entities` for the review queue and `.redacted_text` for the shareable version
C. `detect_language` combined with `recognize_entities`
D. Two separate calls: `extract_pii()` and `redact_text()`
**Answer:** B — As documented, a single `recognize_pii_entities` call returns both the categorized entity list (for review) and the redacted text (for safe sharing).
