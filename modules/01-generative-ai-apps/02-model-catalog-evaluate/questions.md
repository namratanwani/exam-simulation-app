# Practice questions — Select, deploy, and evaluate Microsoft Foundry models

## Explore the model catalog

**Q1.** A developer needs a model to power semantic search over a document store for a RAG solution. Which category of model should they select from the Foundry Models catalog?

A. Reasoning model
B. Embedding model
C. Image generation model
D. Chat completion model

**Answer:** B — Embedding models (e.g., Ada, Cohere) convert text into numerical representations enabling semantic search, recommendation systems, and RAG scenarios based on meaning rather than exact keyword matches. Chat completion models (D) generate conversational text responses, not vector representations for retrieval.

**Q2.** Which TWO statements correctly distinguish Large Language Models (LLMs) from Small Language Models (SLMs) as described in the Foundry model catalog module? (Choose 2.)

A. LLMs are designed for deep reasoning and extensive context understanding but require more computational resources
B. SLMs can run on lower-end hardware or edge devices and are ideal when speed/cost matter more than complex reasoning
C. SLMs always outperform LLMs on coding benchmarks
D. LLMs cannot be deployed through Microsoft Foundry

**Answer:** A, B — These are the exact distinguishing characteristics given (LLM examples: GPT-5, Mistral Large, Llama 3 70B; SLM examples: Phi-4, Mistral OSS, Llama 3 8B). C is false — SLMs trade off complex reasoning capability for efficiency, they don't generally outperform LLMs on complex tasks. D is false — LLMs are standard catalog deployments.

**Q3.** A model card in the Foundry catalog lists "tool calling" as a capability. What does this capability specifically refer to?

A. The model's ability to be fine-tuned using custom training data
B. API and function integration
C. The model's support for multiple languages
D. The model's ability to process images alongside text

**Answer:** B — The module defines capabilities filters explicitly: reasoning = complex problem-solving, tool calling = API and function integration, multimodal processing = text/images/audio. D describes multimodal processing, a distinct filter category — a classic close-distractor pairing on this exam.

**Q4.** Which filter would you use in the Foundry model catalog to find models trained specifically on medical literature that outperform general-purpose models for healthcare use cases?

A. Collection
B. Source
C. Industry
D. Inference tasks

**Answer:** C — The Industry filter surfaces "models trained on industry-specific datasets," which the module states "often outperform general-purpose models in their respective domains." Source (B) filters by provider (Azure OpenAI, Cohere, Meta, etc.), not domain specialization.

## Select models using benchmarks

**Q5.** In the Foundry portal's safety benchmarks, a model scores a high value on the WMDP (Weapons of Mass Destruction Proxy) benchmark. What does this indicate?

A. The model is very safe and resistant to attacks
B. The model has more knowledge of potentially dangerous capabilities in biosecurity, cybersecurity, and chemical security
C. The model has a low Attack Success Rate
D. The model performs well on toxic content detection

**Answer:** B — Per the module: "Higher WMDP scores indicate more knowledge of potentially dangerous capabilities." This is an important exam nuance: unlike most benchmarks where higher = better/safer, a higher WMDP score is a risk signal, not a safety endorsement. A confuses this with ASR (which should be LOW for safety, from HarmBench).

**Q6.** Which benchmark and metric combination is used to measure a model's resistance to generating unsafe content, where LOWER values indicate a safer model?

A. WMDP score
B. ToxiGen F1 score
C. HarmBench Attack Success Rate (ASR)
D. Quality index

**Answer:** C — HarmBench calculates Attack Success Rate (ASR), where "lower values indicate safer, more robust models." ToxiGen F1 score (B) is the opposite direction — higher F1 indicates BETTER hate-speech detection performance, making it a plausible but incorrect distractor.

**Q7.** The Estimated cost benchmark in the Foundry portal combines input and output token costs using what ratio?

A. 1:1 (equal input and output tokens)
B. 1:3 (one input token for every three output tokens)
C. 3:1 (three input tokens for every one output token)
D. 5:1

**Answer:** C — The module states: "Estimated cost combines input and output costs using a typical 3:1 ratio (three input tokens for every output token)."

**Q8.** A developer building a real-time streaming chat interface cares most about how quickly the first word of a response appears. Which performance metric should they prioritize?

A. Latency P99
B. Time to first token (TTFT)
C. Generated tokens per second (GTPS)
D. Total tokens per second (TTPS)

**Answer:** B — TTFT is explicitly defined as "time until the first token arrives when using streaming," directly matching the scenario. GTPS/TTPS measure ongoing throughput rate, not initial responsiveness.

**Q9.** Which Foundry leaderboard feature would BEST help a developer choose between two models where one is slightly less accurate but significantly faster and cheaper?

A. Scenario leaderboard
B. Trade-off chart
C. Model card Benchmarks tab alone
D. Evaluator library

**Answer:** B — Trade-off charts plot two metrics simultaneously (e.g., quality vs. cost, quality vs. throughput) to visualize this exact kind of balance, noting "A model that's slightly less accurate but significantly faster or cheaper might better serve your needs." Scenario leaderboards (A) rank models for a use case but don't visualize two-metric trade-offs directly.

**Q10.** In quality benchmarks, which dataset is specifically used to evaluate code generation capability?

A. MMLU-Pro
B. GPQA
C. HumanEval+ and MBPP+
D. IFEval

**Answer:** C — HumanEval+ and MBPP+ are listed as code generation task datasets. MMLU-Pro assesses general knowledge, GPQA is graduate-level multi-discipline QA, and IFEval measures instruction following.

## Deploy models to endpoints

**Q11.** A company needs guaranteed predictable high throughput for a production workload and is willing to reserve capacity in advance, with no requirement to stay within a specific data zone. Which deployment type should they choose?

A. Global Standard
B. Global Provisioned
C. Data Zone Provisioned
D. Developer

**Answer:** B — Global Provisioned deployments use any Azure region and are based on reserved provisioned throughput units (PTU) to provide predictable high-throughput. Data Zone Provisioned (C) adds a data-residency constraint not required here; Global Standard (A) is pay-per-token, not reserved/predictable.

**Q12.** Which deployment type is explicitly restricted to fine-tuned model evaluation only?

A. Standard
B. Regional Provisioned
C. Global Batch
D. Developer

**Answer:** D — The module states Developer deployments "use any Azure region on a pay-per-token basis and are for fine-tuned model evaluation only."

**Q13.** A healthcare organization in the EU must ensure inference data never leaves the EU data zone, but only has low, unpredictable request volume and prefers pay-as-you-go billing. Which deployment type fits best?

A. Data Zone Standard
B. Data Zone Provisioned
C. Global Standard
D. Standard

**Answer:** A — Data Zone Standard ensures data stays within a specific data zone on a pay-per-token basis, ideal for EU/US data zone compliance without committing to reserved PTUs. Data Zone Provisioned (B) requires reserved throughput commitment, inappropriate for low/unpredictable volume; Standard (D) restricts to a single region rather than a data zone.

**Q14.** During model deployment configuration, what is the purpose of the "Deployment name" field?

A. It sets the Azure resource group name
B. It is used in the `model` parameter of API requests at inference time to route requests to that specific deployment
C. It configures the virtual machine SKU
D. It determines which Azure region the model is deployed to

**Answer:** B — The module states: "During inference, your code uses this deployment name in the `model` parameter to route requests," and later reiterates it under "Access models programmatically."

**Q15.** Which TWO authentication methods can an application use to call a deployed Foundry model endpoint, with one being recommended for production? (Choose 2.)

A. An authentication key/token
B. Microsoft Entra ID authentication (recommended for production)
C. SSH key-based authentication
D. Anonymous public access

**Answer:** A, B — The module states you can use an authentication key/token, "Alternatively, you can use Microsoft Entra ID authentication... Entra ID authentication is recommended for production scenarios." SSH keys and anonymous access are not mentioned as valid options.

**Q16.** A model from a partner in the Foundry catalog (not sold directly by Azure) requires an additional step before deployment that Azure OpenAI models like GPT-4o-mini do NOT require. What is this step?

A. Configuring a virtual network
B. Accepting an Azure Marketplace subscription's terms of use
C. Requesting Azure Machine Learning compute quota
D. Enabling Microsoft Entra ID

**Answer:** B — The module notes that models requiring an Azure Marketplace subscription (common for partner/community models) show terms of use requiring "Agree and Proceed," while models sold directly by Azure, like GPT-4o-mini, don't require marketplace subscriptions.

## Evaluate model performance

**Q17.** Which automated evaluation metric provides a BINARY (grounded / not grounded) assessment, useful specifically when factual accuracy requirements demand a clear-cut answer?

A. Coherence
B. Fluency
C. Groundedness Pro
D. Relevance

**Answer:** C — The module states: "Groundedness Pro offers binary assessment (grounded or not grounded) useful for factual accuracy requirements." Coherence, Fluency, and Relevance are scored on a scale/other criteria, not binary.

**Q18.** For content-harm risk and safety metrics (e.g., violent content, hateful content), how does Microsoft Foundry aggregate results?

A. As a normalized 0–1 quality index
B. As a "defect rate" — the percentage of responses exceeding a severity threshold (typically Medium)
C. As an F1-score comparing to ground truth
D. As an Attack Success Rate

**Answer:** B — The module states: "For content harm metrics, results aggregate as defect rate—the percentage of responses exceeding a severity threshold (typically Medium)." Attack Success Rate (D) is specific to HarmBench in the model-catalog benchmarking unit, not the general Evaluation feature's content-harm aggregation.

**Q19.** A team wants to evaluate summarization quality where covering key points matters more than avoiding extra generated words, and they have reference summaries available. Which NLP metric is BEST suited?

A. BLEU
B. ROUGE
C. F1-score
D. WMDP

**Answer:** B — ROUGE "emphasizes recall over precision, making it particularly useful for summarization tasks where covering key points matters more than avoiding extra words" — this is verbatim from the module. BLEU is more associated with machine translation (n-gram precision-oriented); WMDP is a safety benchmark, not an NLP quality metric.

**Q20.** Which metric extends BLEU by additionally accounting for synonyms, stemming, and paraphrasing?

A. GLEU
B. METEOR
C. ROUGE
D. F1-score

**Answer:** B — METEOR (Metric for Evaluation of Translation with Explicit ORdering) "extends BLEU by accounting for synonyms, stemming, and paraphrasing, providing more flexible comparison."

**Q21.** A developer lacks a labeled test dataset for evaluating a newly deployed agent. Within the Foundry Evaluation feature, what option lets them proceed without manually curating test data first?

A. Use existing dataset
B. Generate synthetic dataset
C. Dataset-based evaluation
D. Groundedness Pro

**Answer:** B — "Generate synthetic dataset: If you lack test data, the system can generate sample data based on a topic description you provide," specifying the generating resource, number of rows, and a descriptive prompt (optionally uploading files to improve relevance).

**Q22.** When AI-assisted (generation quality) evaluation metrics are used in Foundry, what must the developer specify to perform the assessment?

A. A ground truth reference dataset only
B. A GPT model to act as the evaluator
C. An Azure Content Safety filter policy
D. A vector index for retrieval grounding

**Answer:** B — "When using AI-assisted evaluation, you specify a GPT model to perform the assessment. This evaluator model analyzes your deployed model's responses and assigns scores based on the selected criteria." NLP metrics (not AI-assisted) are the ones that instead typically require ground truth data (A).

**Q23.** Evaluation results show elevated safety-metric defect rates for a deployed chatbot. Which of the following is explicitly recommended as a mitigation in the module?

A. Increasing the temperature parameter
B. Implementing Azure AI Content Safety services as content filters
C. Switching to the Developer deployment type
D. Increasing the max tokens parameter

**Answer:** B — Under "When safety metrics show concerns," the module lists content filters (implementing Azure AI Content Safety services), prompt hardening, and output validation. None of the other options address safety concerns as documented.

**Q24.** In the Evaluator library within a Foundry project, which capability is explicitly supported for custom evaluators?

A. Automatic deployment to production without review
B. Version management — comparing versions, restoring previous versions, and collaborating with others
C. Direct billing integration with Azure Cost Management
D. Automatic translation of evaluator prompts into multiple languages

**Answer:** B — "The library supports version management, letting you compare different versions, restore previous versions if needed, and collaborate with others on custom evaluators."
