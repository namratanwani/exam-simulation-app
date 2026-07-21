# Practice questions — Optimize generative AI model performance with Microsoft Foundry

## Optimize model output with prompt engineering

**Q1.** You want a model's responses to be more creative and varied for a brainstorming feature, while keeping a separate summarization feature deterministic and focused. What is the recommended approach to adjusting model parameters?
A. Increase both `temperature` and `top_p` together for the brainstorming feature — the module recommends adjusting only one of the two at a time, not both together
B. Use a higher `temperature` (or `top_p`) for brainstorming and a lower value for summarization, adjusting only one of the two parameters at a time
C. Always set `temperature` to 1.0 for consistency across features — a fixed value ignores that brainstorming and summarization need different randomness levels entirely
D. Use `top_p` for creative tasks and `temperature` for factual tasks simultaneously in the same request — using different parameters per feature doesn't apply within one request the way this implies
**Answer:** B — Higher temperature/top_p increases randomness (creativity); lower decreases it (determinism). The general recommendation is to adjust only one of temperature or top_p at a time, not both.

**Q2.** A developer wants the model to explain its reasoning step by step before giving a final answer, to reduce inaccurate results. Which prompt pattern are they using, and does it apply to Azure OpenAI reasoning (o-series) models?
A. Few-shot learning; required for all models including o-series — few-shot is a separate technique from step-by-step reasoning, and nothing requires it specifically for o-series models
B. Chain-of-thought prompting; primarily useful for non-reasoning models, since o-series reasoning models handle step-by-step logic internally
C. Persona pattern; required for all models including o-series — the persona pattern changes tone/perspective, it doesn't produce step-by-step reasoning
D. Format template pattern; irrelevant to reasoning quality — format templates control output structure, they don't identify what pattern this scenario actually describes
**Answer:** B — Chain-of-thought is a prompting technique for non-reasoning models. Reasoning models (o-series) already perform step-by-step reasoning internally, so explicit CoT prompting is unnecessary for them.

**Q3.** Which of the following are valid components typically found in a prompt for a chat completion model? (Choose two.)
A. System message
B. Embedding index
C. User message
D. Vector store connection string
**Answer:** A, C — System message and user message (along with assistant message and examples) are prompt components. Embeddings/vector stores relate to RAG, not prompt structure itself.

**Q4.** A prompt includes lengthy instructions followed by source text and several examples, but the model keeps misinterpreting which part is an instruction versus which part is content. What should the developer do?
A. Remove all examples from the prompt — removing examples doesn't fix the model confusing instructions with content, it just removes helpful context
B. Increase the temperature to improve comprehension — temperature controls output randomness, it has no effect on how the model parses which section is which
C. Use clear delimiters (e.g., Markdown headings, `---`, or XML tags) to separate the prompt's sections
D. Switch to zero-shot prompting — removing examples via zero-shot doesn't solve section-boundary confusion, it just changes how many examples are given
**Answer:** C — Delimiters create clear boundaries between instructions, content, and examples, reducing misinterpretation.

**Q5.** Your model consistently fails to apply an instruction stated at the very beginning of a long prompt. What technique addresses recency bias in this scenario?
A. Remove the instruction entirely
B. Repeat the key instruction near the end of the prompt
C. Increase top_p to 1.0
D. Convert the instruction into a code block
**Answer:** B — Models can weight text near the end of a prompt more heavily (recency bias); repeating the key instruction at the end helps ensure it's followed.

**Q6.** What is the key limitation of prompt engineering that makes it insufficient on its own for scenarios requiring current, private, or domain-specific facts?
A. It cannot use system messages
B. It cannot give the model access to information the model wasn't trained on
C. It always increases token costs beyond acceptable limits
D. It requires model retraining before use
**Answer:** B — Prompt engineering only shapes behavior/output style; it cannot supply the model with knowledge outside its training data. That requires grounding (RAG).

**Q7.** Providing the model with one example of a customer message and its correct classification category, then asking it to classify a new message, is an example of which technique?
A. Zero-shot learning
B. One-shot learning (a form of few-shot learning)
C. Fine-tuning
D. Chain-of-thought prompting
**Answer:** B — A single example provided in the prompt is "one-shot," a specific case of the few-shot learning pattern. Zero-shot means no examples are given.

**Q27.** A developer is writing a system message and wants to follow the module's recommended design checklist. Which sequence of considerations does the checklist specify?

A. Pick a temperature value, choose a model, set max tokens, add examples — these are inference/API settings, not the role-boundaries-format-policy checklist the module actually describes
B. Start with the assistant's role, define boundaries (topics/actions/content to avoid), specify the output format, and add a "when unsure" policy
C. List every possible user question in advance, then ban all others — the checklist defines boundaries and an unsure-case policy, not an exhaustive question list
D. Only specify the output format; the other elements are optional — the checklist treats role, boundaries, and the unsure-case policy as equally necessary steps
**Answer:** B — The module's system message design checklist has exactly these four steps: start with the role, define boundaries, specify output format, and add a policy for ambiguous/out-of-scope/insufficient-information cases.

**Q28.** True or which statement about system messages is correct, per the module's caution?

A. A system message guarantees 100% compliant model behavior and requires no further testing — the module explicitly cautions that system messages influence but never guarantee compliance
B. A system message influences but does not guarantee compliance — it should be tested/iterated on and layered with content filtering and evaluation
C. System messages are ignored by chat completion models — system messages actively shape model behavior in chat completion models, they aren't ignored
D. System messages can only be used with fine-tuned models — system messages are a standard prompt component usable with any chat completion model
**Answer:** B — The module explicitly cautions: "A system message influences but does not guarantee compliance — test/iterate, and layer with content filtering + evaluation."

**Q29.** A prompt begins with "You're a seasoned marketing professional with 15 years of experience in digital campaigns..." to change the style and perspective of the model's responses. Which prompt pattern is this?

A. Format template pattern
B. Persona pattern
C. Chain-of-thought pattern
D. Few-shot learning pattern
**Answer:** B — The persona pattern instructs the model to adopt a specific role/perspective (the module's own example: "You're a seasoned marketing professional...") to change response style.

**Q30.** A developer includes a specific structural template in their prompt (e.g., "Respond using this format: Title: ... / Summary: ... / Key Points: ...") to ensure the output is structured and easily parseable by downstream code. Which prompt pattern is this?

A. Persona pattern
B. Format template pattern
C. Recency bias mitigation
D. Chain-of-thought pattern
**Answer:** B — The format template pattern provides a template/structure in the prompt for structured, parseable output.

**Q31.** Rather than asking the model to "extract the key facts from this document and then answer the question" in a single prompt, a developer splits this into two separate prompts — one that extracts facts, and a second that answers the question based on those facts. What is this technique called, and why is it used?

A. Few-shot learning; to provide more examples — splitting a task across separate prompts isn't about adding examples, it's about breaking down the task itself
B. Decomposing a task into explicit sub-steps across separate prompts; reduces errors on complex, multi-part tasks
C. Recency bias mitigation; to repeat instructions — recency bias mitigation is about instruction placement within one prompt, not splitting a task across prompts
D. Persona pattern; to change response tone — the persona pattern changes tone/perspective, it has nothing to do with splitting a task into sub-steps
**Answer:** B — The module describes this decompose technique as splitting a task into explicit sub-steps (e.g., extract facts first, then answer) rather than one-shot handling, reducing errors on complex, multi-part tasks — a technique related to chain-of-thought.

**Q32.** Besides the system message and user message, which TWO other components does the module list as typically found in a chat completion model prompt? (Choose 2.)

A. Assistant message — previous model responses in multi-turn conversations
B. Examples — sample input/output pairs demonstrating expected format
C. Vector store ID
D. API version header
**Answer:** A, B — The module's four prompt components are system message, user message, assistant message, and examples. Vector store IDs and API version headers are not prompt components.

**Q33.** How do `temperature` and `top_p` differ in HOW they control randomness, per the module?

A. `temperature` limits the model to the top X% probability mass of tokens; `top_p` scales overall randomness directly — this swaps the two mechanisms exactly backwards from how the module describes them
B. `temperature` scales overall randomness directly (e.g., 0.7 = more creative, 0.2 = more focused); `top_p` limits the model to the subset of most-probable next tokens by cumulative probability mass (e.g., `top_p=0.9` considers the top 90% probability mass)
C. Both parameters are functionally identical and always produce the same output — they're two distinct mechanisms with different effects on the output distribution, not interchangeable
D. `temperature` only affects the first token generated; `top_p` affects all subsequent tokens — both parameters apply to every token generated, not just the first one
**Answer:** B — This is the module's exact distinction between the two randomness-control mechanisms: temperature directly scales randomness, while top_p performs nucleus sampling over the most-probable token mass.

## Ground your model with Retrieval Augmented Generation

**Q8.** A company wants their generative AI app to answer questions using their private, frequently-updated product catalog without retraining the model every time the catalog changes. Which approach best fits this requirement?
A. Fine-tuning with DPO
B. Retrieval Augmented Generation (RAG) using Azure AI Search
C. Increasing the temperature parameter
D. Using only the persona prompt pattern
**Answer:** B — RAG retrieves current data at query time from an external index, avoiding the need to retrain the model whenever the underlying data changes.

**Q9.** What are the three steps of the RAG pattern, in order?
A. Generate, Augment, Retrieve
B. Retrieve, Augment, Generate
C. Embed, Index, Query
D. Fine-tune, Retrieve, Respond
**Answer:** B — Retrieve relevant data, Augment the prompt with it, then Generate the grounded response.

**Q10.** Which Azure AI Search technique is recommended for generative AI applications because it combines keyword, semantic, and vector search for the most accurate results?
A. Keyword search
B. Semantic search only
C. Vector search only
D. Hybrid search
**Answer:** D — Hybrid search combines keyword + semantic + vector search and is the recommended technique for generative AI applications.

**Q11.** Two sentences use different wording but convey the same meaning. In an embedding-based vector search, what does this imply about their vector representations, and what metric is commonly used to measure this?
A. Their vectors will be far apart; measured using Euclidean distance only — semantically similar text produces vectors close together, not far apart, and cosine similarity is the standard metric, not only Euclidean distance
B. Their vectors will be close together in multidimensional space; commonly measured using cosine similarity, where a value near 1 indicates high similarity
C. Their vectors will be identical; measured using temperature — similar meaning doesn't make vectors identical, and temperature is an inference-randomness parameter with no role in similarity measurement
D. Embeddings cannot capture semantic similarity, only exact keyword matches — this is the opposite of embeddings' purpose, which is capturing meaning beyond exact keywords
**Answer:** B — Semantically similar text produces vectors close together in vector space; cosine similarity (angle between vectors, near 1 = very similar) is the standard measure.

**Q12.** In the Microsoft Foundry Python SDK RAG example, which SDK/class is used to obtain an authenticated OpenAI client from a Foundry project, and which API is then used to generate a grounded response?
A. `AIProjectClient` from `azure-ai-projects`, then the Responses API (`client.responses.create(...)`)
B. `SearchClient` from `azure-search-documents`, then the Chat Completions API only
C. `DefaultAzureCredential` alone, with no project client needed
D. `AIProjectClient`, then a direct call to the embedding model with no chat API
**Answer:** A — `AIProjectClient` (from `azure.ai.projects`) with `DefaultAzureCredential` provides `get_openai_client()`, and grounded responses are generated via `client.responses.create(...)`, injecting retrieved context into the system message.

**Q13.** Which data sources can you add to Microsoft Foundry to build a searchable index for RAG? (Choose two.)
A. Azure Blob Storage
B. Microsoft OneLake
C. A fine-tuned model checkpoint
D. A system message template
**Answer:** A, B — Along with Azure Data Lake Storage Gen2 and direct file upload, Blob Storage and OneLake are valid data sources for building a RAG index.

**Q14.** A team wants grounded knowledge for their AI agents without building or managing their own Azure AI Search index and infrastructure. Which Microsoft Foundry capability is designed for this managed scenario?
A. Fine-tuning with LoRA
B. Foundry IQ — a managed knowledge store simplifying grounding for AI agents
C. Prompt engineering with the persona pattern
D. Direct Preference Optimization
**Answer:** B — Foundry IQ is the managed knowledge platform alternative to self-managed Azure AI Search indexing, purpose-built for agent grounding.

**Q34.** What is "grounding" in the context of generative AI, and what risk does it mitigate?

A. Grounding means lowering the temperature parameter; it mitigates excessive creativity — lowering temperature only reduces output randomness, it doesn't supply the model with any factual data
B. Grounding means supplying relevant, factual data alongside the user's question so the model bases its answer on that data instead of only its training data; it mitigates fabrication (plausible-sounding but factually wrong output)
C. Grounding means fine-tuning the model on labeled data; it mitigates high latency — that describes fine-tuning, a separate technique that adjusts model weights rather than supplying data at query time, and it doesn't specifically target latency
D. Grounding means caching previous responses; it mitigates token cost — caching avoids recomputation, it doesn't give the model access to facts outside its training data
**Answer:** B — The module defines grounding exactly this way and states models risk "fabrication" — plausible-sounding but factually wrong output — without it, since models have a training-data cutoff and no default access to private org data.

**Q35.** The module describes a THREE-step workflow for using Azure AI Search to build retrieval for RAG in Microsoft Foundry — distinct from the "Retrieve, Augment, Generate" RAG pattern itself. What are those three steps?

A. Retrieve, Augment, Generate — that's the general RAG pattern itself, not the module's distinct three-step workflow for building the retrieval layer
B. Add your data (from Blob Storage/Data Lake/OneLake/file upload), create an index (using an embedding model), and query the index (embed the user question and search for similar content)
C. Fine-tune, evaluate, deploy — that's a fine-tuning lifecycle, an entirely separate workflow from building a search index for retrieval
D. Train, validate, test — that's a generic ML training lifecycle, not the module's specific add-data/create-index/query-index workflow
**Answer:** B — This is the module's Azure AI Search workflow specifically: add data, create an index using an embedding model, then query the index by embedding the user's question and searching for similar content — distinct from (but feeding into) the general Retrieve/Augment/Generate RAG pattern.

**Q36.** Which pairing correctly distinguishes Azure AI Search's keyword search from its semantic search technique?

A. Keyword search matches exact terms; semantic search matches meaning via semantic models rather than exact keywords
B. Keyword search matches meaning; semantic search matches exact terms only — this reverses the module's actual definitions of the two techniques
C. Both keyword and semantic search require embeddings — only vector search (and hybrid search, which incorporates it) uses embeddings
D. Keyword search and vector search are the same technique under different names — the module treats them as two of four distinct techniques, not the same one renamed
**Answer:** A — The module defines keyword search as exact term matching and semantic search as matching meaning via semantic models, distinct from vector search (which uses embeddings for semantic similarity) and hybrid search (which combines all three).

**Q37.** What is an "embedding," and how is it created, per the module?

A. A cached copy of a previous model response; created by the Responses API automatically — caching stores past outputs verbatim, it doesn't produce a semantic vector representation of text
B. A mathematical vector representation of text capturing semantic meaning; created by sending content to an embedding model (e.g., an Azure OpenAI embedding model in Microsoft Foundry)
C. A compressed version of the fine-tuning training dataset; created by LoRA — LoRA is a fine-tuning technique for updating model weights efficiently, unrelated to producing vector representations
D. A system message template; created by the persona pattern — the persona pattern shapes prompt wording and tone, it doesn't generate any vector representation
**Answer:** B — This is the module's exact definition of an embedding and how it's produced.

## Fine-tune a model for consistent behavior

**Q15.** A model reliably follows a detailed system message about brand tone in most cases but occasionally drifts, and the team wants to shorten their very long system messages to reduce per-request token cost while keeping consistent behavior. What technique directly addresses both goals?
A. Increasing temperature
B. Fine-tuning the model on representative examples of the desired style
C. Adding more few-shot examples to every request
D. Switching to zero-shot prompting
**Answer:** B — Fine-tuning embeds the desired behavior into the model's weights, improving consistency while allowing shorter prompts (since instructions/examples no longer need to be repeated every request).

**Q16.** What technique does Microsoft Foundry fine-tuning use to make training faster and more cost-effective by updating only a smaller subset of important parameters instead of retraining the whole model?
A. Cosine similarity
B. LoRA (Low-Rank Adaptation)
C. Hybrid search
D. Chain-of-thought decomposition
**Answer:** B — LoRA approximates weight changes with a lower-rank representation, updating a smaller parameter subset rather than the full model.

**Q17.** Which fine-tuning technique trains on a labeled dataset of prompt-and-response pairs and works best for tasks with clear, well-defined approaches?
A. Reinforcement fine-tuning (RFT)
B. Direct Preference Optimization (DPO)
C. Supervised fine-tuning (SFT)
D. Retrieval Augmented Generation
**Answer:** C — SFT trains on labeled prompt/response pairs and suits clearly-defined tasks. RFT uses iterative grader-based feedback for complex/dynamic tasks; DPO aligns using preferred vs. non-preferred pairs.

**Q18.** Which fine-tuning technique optimizes model behavior through a grader that rewards better responses incrementally, and is best suited for complex or dynamic tasks with many possible valid solutions?
A. Supervised fine-tuning (SFT)
B. Reinforcement fine-tuning (RFT)
C. Direct Preference Optimization (DPO)
D. Zero-shot prompting
**Answer:** B — RFT uses iterative, grader-based feedback and is best for complex/dynamic tasks requiring improved reasoning quality, unlike SFT's fixed labeled pairs.

**Q19.** Which fine-tuning technique aligns a model to human preferences using pairs of preferred and non-preferred responses, and is described as computationally lighter than traditional reinforcement learning while equally effective for alignment?
A. Supervised fine-tuning (SFT)
B. Reinforcement fine-tuning (RFT)
C. Direct Preference Optimization (DPO)
D. Prompt engineering
**Answer:** C — DPO uses preferred/non-preferred response pairs and is lighter-weight than traditional RL approaches while achieving similar alignment quality.

**Q20.** What format is required for fine-tuning training data for chat completion models in Microsoft Foundry, and what is a key requirement about the system message within that data?
A. CSV format; the system message should be omitted to reduce file size — the required format is JSONL, not CSV, and omitting the system message tends to lower model accuracy rather than help
B. JSONL format (one JSON object with role/content messages per line); a consistent system message should be included, matching the one used at inference time
C. Plain text transcripts; system messages are optional and don't affect accuracy — plain text isn't the required format, and the module states the system message does affect accuracy
D. YAML format; only user and assistant messages are needed — YAML isn't the required format, and the system message is explicitly required, not omittable
**Answer:** B — Training data must be JSONL with system/user/assistant messages per example. Omitting the system message during training tends to produce lower-accuracy models, and the same system message should be used at inference time.

**Q21.** A team wants to transfer the capability of a large, expensive model into a smaller, cheaper model that achieves similar quality at lower cost and latency. What is this technique called, and how is it achieved?
A. Retrieval Augmented Generation; done by indexing the large model's documentation
B. Distillation; achieved by fine-tuning a smaller model on outputs collected from the larger, high-performing model
C. Chain-of-thought prompting; achieved by asking the small model to imitate the large model's reasoning steps at inference time
D. Hybrid search; achieved by combining two models' outputs at query time
**Answer:** B — Distillation is a fine-tuning use case: collect outputs from a larger model and fine-tune a smaller model on them to approximate its quality at lower cost/latency.

**Q22.** Before committing to fine-tuning, what does the module recommend as an essential first step, and why?
A. Immediately fine-tune with DPO, since it's the lightest-weight technique — the module recommends baselining first, regardless of which fine-tuning technique is eventually chosen
B. Evaluate the baseline performance of a standard (non-fine-tuned) model first, so you can tell whether fine-tuning actually improved or degraded performance
C. Skip prompt engineering and RAG entirely, since fine-tuning supersedes both — fine-tuning is described as an advanced step considered after simpler strategies, not a replacement for them
D. Prepare fewer than 10 training examples to keep costs low — the module recommends at least hundreds of training examples, not fewer than 10
**Answer:** B — Without a baseline, it's impossible to determine whether fine-tuning helped or hurt performance. Fine-tuning is described as an advanced capability to consider only after simpler strategies.

**Q38.** How does the module define "fine-tuning" itself, distinct from training a model from scratch?

A. Taking a pretrained model and further training it on a smaller, task-specific dataset, adjusting internal weights so output matches the training data's patterns
B. Creating an entirely new model architecture trained from random initialization — that describes training from scratch, which fine-tuning is explicitly distinguished from by starting from a pretrained model instead
C. Adjusting only the `temperature` and `top_p` inference parameters — these are inference-time sampling parameters, they don't adjust the model's weights the way fine-tuning does
D. Building a vector index over the training data without altering the model — that describes RAG's retrieval setup, not fine-tuning, which does alter the model's internal weights
**Answer:** A — This is the module's exact definition of fine-tuning, contrasted with training from scratch (fine-tuning's key benefit being efficiency: less time, compute, and data).

**Q39.** A team needs the model to reliably return output matching a specific JSON schema on every response, and few-shot examples alone haven't achieved fully reliable compliance. Which "when to fine-tune" scenario does this match?

A. Reducing prompt length only — shortening prompts is a side benefit of some fine-tuning use cases, not the scenario about enforcing a structured JSON output format
B. Specific structured output formats (e.g., JSON schema) that few-shot alone can't reliably enforce
C. Enhancing tool-calling accuracy — that's a distinct fine-tuning use case about function-call selection and parameters, not output-schema compliance
D. Distillation from a larger model — distillation transfers a larger model's quality into a smaller model, unrelated to enforcing a specific output schema
**Answer:** B — The module lists "specific structured output formats (e.g., JSON schema) that few-shot alone can't reliably enforce" as one of the explicit reasons to fine-tune.

**Q40.** An agent frequently selects the wrong tool or generates malformed parameters when invoking function calls. Which fine-tuning use case directly targets this problem?

A. Distillation — distillation transfers a larger model's quality into a smaller one, it isn't the use case targeting tool selection or parameter accuracy
B. Enhancing tool-calling accuracy (tool selection + parameter generation) via fine-tuning with tool-call examples
C. Reducing prompt length/token cost — shortening prompts addresses token cost, not the accuracy of which tool is chosen or how its parameters are generated
D. Consistent brand style/tone — brand style consistency is a separate fine-tuning use case, unrelated to fixing tool selection or malformed parameters
**Answer:** B — The module explicitly lists "enhancing tool-calling accuracy (tool selection + parameter generation) via fine-tuning with tool-call examples" as a fine-tuning use case.

**Q41.** Roughly how many training examples does the module recommend as a minimum when preparing a fine-tuning dataset?

A. At least 5
B. At least hundreds of examples, with more generally being better
C. Exactly 50, no more and no less
D. At least 1 million
**Answer:** B — The module states: "Aim for at least hundreds of examples; more is generally better."

**Q42.** Which of the following is explicitly listed among the module's fine-tuning challenges/costs?

A. Model drift — over-specializing the model can degrade its general-purpose performance
B. Inability to use JSONL training data
C. Complete elimination of hosting costs after training
D. No need to ever retrain, regardless of data or base-model changes
**Answer:** A — The module lists training costs (upfront + ongoing hosting), data quality risks (overfitting/underfitting/bias), maintenance (retraining when data/base models change), hyperparameter experimentation, and model drift (over-specialization degrading general-purpose performance) as fine-tuning challenges.

## Compare and combine optimization strategies

**Q23.** Which optimization strategy is generally described as having the lowest implementation time, lowest complexity, and lowest cost (per-token only)?
A. Fine-tuning
B. RAG
C. Prompt engineering
D. Distillation
**Answer:** C — Prompt engineering requires no additional infrastructure/training and incurs only per-token cost, making it the lowest across all three dimensions compared to RAG and fine-tuning.

**Q24.** A generative AI application needs to (1) always respond in the company's exact brand voice, and (2) answer questions using the company's constantly-changing hotel pricing and availability data. Which combination of strategies best addresses both requirements simultaneously?
A. Prompt engineering alone — prompt engineering alone can't reliably keep pace with constantly-changing pricing/availability data
B. RAG alone — RAG handles the changing data but doesn't reliably enforce a consistent brand voice across responses
C. Fine-tuning for consistent brand voice/style, combined with RAG for current, domain-specific pricing/availability data
D. Increasing temperature to 1.0 — higher temperature increases randomness in wording, it doesn't enforce brand voice or supply current pricing data
**Answer:** C — Fine-tuning addresses consistent style/format (requirement 1); RAG addresses accurate, frequently-changing domain data (requirement 2). This is the documented "RAG + fine-tuning" combination pattern.

**Q25.** According to the module's decision framework, what is the recommended order of adding optimization strategies to a generative AI application?
A. Start with fine-tuning, then add RAG, then prompt engineering — this reverses the module's recommended order, starting with the most complex/costly strategy first
B. Start with RAG, then fine-tuning, then prompt engineering — this also starts with a more complex strategy before the lowest-cost one, contrary to the module's guidance
C. Start with prompt engineering, add RAG if factual/domain accuracy is needed, then add fine-tuning if consistency still isn't achieved
D. Always implement all three simultaneously from the start — the module recommends adding strategies incrementally as needed, not implementing all three unconditionally
**Answer:** C — The recommended incremental approach starts with the lowest-cost/complexity strategy (prompt engineering) and layers in RAG and then fine-tuning only as needed, avoiding unnecessary cost/complexity.

**Q26.** Which statement correctly distinguishes what RAG optimizes for versus what fine-tuning optimizes for?
A. RAG optimizes model style/tone; fine-tuning optimizes for context/accuracy — this swaps the module's actual pairing; RAG addresses context/accuracy, fine-tuning addresses style/consistency
B. RAG optimizes for context (accuracy, via retrieved data); fine-tuning optimizes the model itself (behavioral consistency, style, format)
C. Both RAG and fine-tuning optimize exclusively for token cost reduction — token cost is a side effect, not the stated purpose of either strategy's core focus
D. RAG and fine-tuning both require retraining the base model — RAG requires no retraining at all, since it retrieves external data at query time instead
**Answer:** B — RAG addresses the "optimize for context" dimension (accuracy via retrieval); fine-tuning addresses the "optimize the model" dimension (consistency of style/format). Prompt engineering underlies both.

**Q43.** Which combination of strategies does the module describe as the "most common combo," where prompt engineering defines *how* the model acts and the other strategy supplies *what* it needs to know?

A. Fine-tuning + RAG
B. Prompt engineering + RAG
C. Prompt engineering + fine-tuning only
D. Fine-tuning alone
**Answer:** B — The module states: "Prompt engineering + RAG — most common combo: PE defines how the model acts, RAG supplies what it needs to know."

**Q44.** A mature enterprise application uses all three optimization strategies together. Per the module, what role does each strategy play in this "all three together" combination?

A. Fine-tuning handles style/format, RAG supplies accurate domain knowledge, and prompt engineering adds conversation-specific instructions/guardrails
B. Fine-tuning handles domain knowledge, RAG handles style, and prompt engineering handles cost reduction — this swaps fine-tuning's and RAG's actual roles; fine-tuning handles style, RAG supplies domain knowledge
C. All three strategies perform the identical function of reducing token cost — token cost is a side effect, not the primary function of any of the three; each targets a different concern
D. Prompt engineering replaces the need for RAG and fine-tuning once implemented — in the all-three-together pattern, prompt engineering layers guardrails on top, it doesn't replace the other two
**Answer:** A — The module describes the "all three together" pattern exactly this way: fine-tuning for style/format consistency, RAG for accurate domain knowledge, and prompt engineering for conversation-specific instructions/guardrails layered on top.

## Scenario-based questions

**Q45.** A legal-research assistant must (1) break a complex multi-part question into an extraction step followed by an answer step, and (2) ground each answer in the firm's private case-law database, which is updated weekly. Which combination of techniques from across the module addresses both needs?

A. Persona pattern alone for both needs — the persona pattern only changes tone/perspective, it addresses neither task decomposition nor grounding in private, updated data
B. Decomposing the task into separate extract-then-answer prompts (a prompt engineering technique) combined with RAG (using Azure AI Search hybrid search) to ground answers in the frequently-updated private case-law data
C. Fine-tuning alone, since it can encode both the decomposition logic and the case-law data into model weights — fine-tuning would require constant retraining to keep pace with weekly data changes, which RAG avoids
D. Zero-shot prompting combined with a higher temperature — higher temperature increases output randomness, it doesn't decompose a task or ground answers in private case-law data
**Answer:** B — Decomposition is a prompt engineering pattern for breaking down complex tasks, while RAG is specifically recommended when data is private and changes frequently — fine-tuning would require constant retraining to keep pace with weekly data changes, which RAG avoids.

**Q46.** A brand wants every response to consistently sound like their mascot character, regardless of topic, and also wants to avoid resending a 2,000-token persona description with every single API call. Which strategy, and which specific benefit of that strategy, addresses both concerns together?

A. RAG; because it retrieves the persona description at query time — RAG is designed for retrieving factual/domain data, not for embedding a persona into every response without repeating it
B. Fine-tuning; because embedding the desired behavior into model weights improves consistency AND allows shorter prompts since the persona description no longer needs to be repeated every request
C. Increasing `top_p` to reduce token usage — top_p controls nucleus sampling for randomness, it has no effect on how many tokens a persona description costs per request
D. The format template pattern; because templates are shorter than personas — format templates control output structure, they don't address consistency or the repeated persona-description cost
**Answer:** B — This maps directly to the module's fine-tuning benefits: consistent behavioral style plus the token-cost benefit of not needing to repeat long instructions/examples on every request.

**Q47.** A developer is implementing RAG end-to-end in Microsoft Foundry: they add hotel data from Blob Storage, build an index with an embedding model, and want the final chat call to inject retrieved context. Which code pattern correctly reflects the module's guidance for the final generation step?

A. Call `client.chat.completions.create()` with a `previous_response_id` referencing the index — `previous_response_id` tracks conversation state, it isn't how retrieved context gets injected into a chat call
B. Obtain an OpenAI-compatible client via `AIProjectClient.get_openai_client()`, then call `client.responses.create(...)`, injecting the retrieved context into the system message alongside the user's question
C. Call the embedding model directly and return its raw vector as the final answer — an embedding is a numeric vector, not a natural-language answer, so returning it directly isn't a usable response
D. Skip the `responses.create()` call entirely; Azure AI Search returns chat-ready text automatically — Azure AI Search returns matched documents/passages, not a finished chat response
**Answer:** B — This is exactly the module's RAG implementation pattern: get the OpenAI-compatible client from the project client, then call the Responses API with retrieved_context concatenated into the system message.

**Q48.** A team follows the module's decision framework: they start with prompt engineering, add RAG for accuracy, and are now considering fine-tuning because responses still don't consistently follow a required tone despite good system messages and grounded data. What should they do BEFORE starting fine-tuning, and which technique should they consider using to keep the fine-tuning process cost-effective?

A. Skip evaluation and go straight to Reinforcement fine-tuning, since it's always cheapest — the module recommends baselining before any fine-tuning technique, and RFT isn't described as universally cheapest
B. Evaluate the standard model's baseline performance first (to measure fine-tuning's actual impact), and use LoRA to update only a smaller subset of parameters rather than the whole model
C. Discard the RAG implementation before fine-tuning, since the two are incompatible — RAG and fine-tuning are explicitly combinable in the module's "all three together" pattern
D. Increase `temperature` instead of fine-tuning, since it's cheaper — temperature only adjusts output randomness, it can't enforce a required tone the way fine-tuning can
**Answer:** B — The module stresses baselining before fine-tuning to measure impact, and highlights LoRA as the mechanism that makes Foundry fine-tuning faster/more cost-effective by updating a smaller parameter subset instead of the whole model.

**Q49.** An agent-building team debates between standing up their own Azure AI Search index versus using Foundry IQ for knowledge grounding. Which factor, per the module, should most influence this decision?

A. Azure AI Search is always cheaper regardless of scale or management overhead — cost depends on scale and management overhead, which is the actual factor the module highlights, not a blanket cost claim
B. Azure AI Search means you manage the index/infrastructure yourself, while Foundry IQ is a managed knowledge platform that simplifies grounding specifically for AI agents without that infrastructure burden
C. Foundry IQ cannot be used with the Responses API — nothing in the module states Foundry IQ is incompatible with the Responses API
D. Azure AI Search only supports keyword search, so it should never be used for agents — Azure AI Search also supports semantic, vector, and hybrid search, not only keyword search
**Answer:** B — This is the module's explicit exam-relevant distinction: self-managed Azure AI Search infrastructure versus the managed Foundry IQ knowledge platform designed for agent grounding.

**Q50.** A company wants a smaller, cheaper model to match the quality of their larger flagship model on a narrow customer-support task, and separately wants that smaller model's alignment further refined using pairs of preferred/non-preferred responses after initial training. Which sequence of fine-tuning techniques matches this plan?

A. Use RFT only, since it's required for all alignment work — RFT is one of several fine-tuning techniques, not a universally required step for every alignment scenario
B. First perform distillation (fine-tune the smaller model on the larger model's outputs), then apply DPO (align using preferred vs. non-preferred response pairs) as a combined technique
C. Use only prompt engineering, since fine-tuning techniques cannot be combined — prompt engineering alone can't perform distillation or preference alignment, and fine-tuning techniques can in fact be combined
D. Use SFT exclusively and skip DPO, since combining techniques is unsupported — the module explicitly describes combining techniques, contrary to this claim
**Answer:** B — Distillation fine-tunes a smaller model on a larger model's outputs to approximate its quality; the module also notes fine-tuning techniques can be combined (e.g., SFT first, then DPO to further align), matching a distillation-then-DPO sequence for this scenario.
