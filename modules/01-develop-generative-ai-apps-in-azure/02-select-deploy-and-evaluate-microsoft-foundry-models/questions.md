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

**Q25.** Approximately how many models does the Foundry Models catalog provide access to, according to the module's introduction?

A. Over 100
B. Over 500
C. Over 1,900
D. Over 10,000

**Answer:** C — The module states the catalog lets you "explore over 1,900 models from providers like Microsoft, Anthropic, OpenAI, Meta, and Hugging Face."

**Q26.** What are the two broad categories of models in the Foundry Models catalog?

A. Free models available at no cost, and paid models billed per-token through your Azure subscription
B. Foundry Models sold directly by Azure, and Foundry Models from partners and community
C. Text-generation models for chat and completion tasks, and image models for generation and analysis
D. Certified models that passed Microsoft's compliance review, and experimental models still in preview

**Answer:** B — Models sold directly by Azure are billed through your Azure subscription (includes Azure OpenAI and Microsoft models); models from partners and community are provided by trusted third parties, each with their own licensing and pricing.

**Q27.** Which of the following is NOT something a Foundry model card displays, per the module?

A. Provider and capabilities, alongside supported context window and maximum output token limits
B. Benchmark metrics sourced from the Foundry leaderboard's quality, safety, cost, and performance tabs
C. Responsible AI considerations and deployment options
D. The exact source code used to train the model

**Answer:** D — Model cards show provider, capabilities, benchmark metrics, responsible AI considerations, and deployment options — not training source code, which is not mentioned as part of a model card.

**Q28.** A developer wants to filter the model catalog to see only models available in the Hugging Face repository. Which filter category should they use?

A. Collection
B. Capabilities
C. Fine-tuning methods
D. Industry

**Answer:** A — The Collection filter is described as letting you filter by, for example, "models provided directly in Azure, or models available in the Hugging Face repository."

**Q29.** Which filter lets a developer narrow the model catalog specifically by provider, such as Azure OpenAI, Cohere, Mistral, Meta, or Anthropic?

A. Source
B. Collection
C. Inference tasks
D. Industry

**Answer:** A — The Source filter is defined as filtering by provider: Azure OpenAI, Microsoft, Cohere, Mistral, Meta, Anthropic, and others.

**Q30.** How does the module distinguish reasoning models from standard chat completion models?

A. Reasoning models cannot generate conversational text at all, because their architecture relies exclusively on chain-of-thought token sequences rather than the standard transformer decoder layers used by chat completion models like GPT-4.1 for dialogue
B. Chat completion models generate coherent, contextually appropriate responses for conversational interfaces, while reasoning models show higher performance on complex tasks like math, coding, and strategy and can break down problems and show their reasoning process
C. Reasoning models are a subset of embedding models, sharing the same vector-representation architecture used for semantic search, and are simply embedding models fine-tuned with additional chain-of-thought training data
D. There is no meaningful distinction; the terms are interchangeable marketing labels applied inconsistently across providers like Azure OpenAI, Anthropic, and Meta depending on release timing rather than actual model architecture

**Answer:** B — Most catalog models are chat completion models suited to conversational interfaces/content generation; reasoning models (e.g., Claude Opus 4.6) show higher performance on complex tasks (math, coding, science, strategy, logistics) and can break problems down, exposing their reasoning process.

**Q31.** Which model type/example pairing is correct for generating brand-new images from text descriptions?

A. GPT-4.1 — image generation
B. GPT-image-1 — image generation
C. GPT-4o-tts — image generation
D. Sora 2 — image generation

**Answer:** B — The module's specialized-model table lists GPT-image-1 as the example image generation model, creating images from text descriptions. Sora 2 (D) is the video generation example, not image generation.

**Q32.** Which model is given as the example for creating video content from text descriptions?

A. GPT-4o-transcribe
B. GPT-image-1
C. Sora 2
D. GPT-4.1

**Answer:** C — Sora 2 is listed as the video generation model example in the module's specialized/task-specific models table.

**Q33.** GPT-4.1 is given as the example model for which specialized task in the module's table?

A. Text to speech, converting written input into synthesized audio output via the GPT-4o-tts model
B. Image analysis — multimodal input (text+images) producing natural language output
C. Speech to text transcription, converting spoken audio into written text via GPT-4o-transcribe
D. Video generation, producing short video clips directly from text descriptions via Sora 2

**Answer:** B — GPT-4.1 is listed under "Image analysis models," taking multimodal input (text+images) and producing natural language output.

**Q34.** Which pairing correctly matches example models to their text-to-speech and speech-to-text roles, respectively?

A. GPT-4o-tts (text to speech) and GPT-4o-transcribe (speech to text)
B. GPT-4o-transcribe (text to speech) and GPT-4o-tts (speech to text)
C. Sora 2 (text to speech) and GPT-image-1 (speech to text)
D. GPT-4.1 (text to speech) and GPT-image-1 (speech to text)

**Answer:** A — The module's table lists GPT-4o-tts as the text-to-speech example (converts text to synthesized speech) and GPT-4o-transcribe as the speech-to-text example (converts audio/speech to text transcriptions).

**Q35.** A developer wants to filter the model catalog to see which models support a particular custom fine-tuning technique they plan to use. Which filter should they apply?

A. Fine-tuning methods
B. Inference tasks
C. Collection (by repository)
D. Capabilities (by feature)

**Answer:** A — The Fine-tuning methods filter narrows results to "supported fine-tuning techniques." Inference tasks (B) instead filters by task type such as text generation, summarization, translation, image generation, or speech synthesis.

## Select models using benchmarks

**Q5.** In the Foundry portal's safety benchmarks, a model scores a high value on the WMDP (Weapons of Mass Destruction Proxy) benchmark. What does this indicate?

A. The model is very safe and resistant to attacks, as confirmed by a low Attack Success Rate on the HarmBench adversarial jailbreak benchmark
B. The model has more knowledge of potentially dangerous capabilities in biosecurity, cybersecurity, and chemical security
C. The model has a low Attack Success Rate, meaning it successfully resists adversarial jailbreak prompts during HarmBench red-team testing
D. The model performs well on toxic content detection, scoring a high F1 value on the ToxiGen adversarial and implicit hate speech benchmark

**Answer:** B — Per the module: "Higher WMDP scores indicate more knowledge of potentially dangerous capabilities." This is an important exam nuance: unlike most benchmarks where higher = better/safer, a higher WMDP score is a risk signal, not a safety endorsement. A confuses this with ASR (which should be LOW for safety, from HarmBench).

**Q6.** Which benchmark and metric combination is used to measure a model's resistance to generating unsafe content, where LOWER values indicate a safer model?

A. WMDP score (biosecurity proxy)
B. ToxiGen F1 score (hate speech)
C. HarmBench Attack Success Rate (ASR)
D. Quality index (0 to 1 scale)

**Answer:** C — HarmBench calculates Attack Success Rate (ASR), where "lower values indicate safer, more robust models." ToxiGen F1 score (B) is the opposite direction — higher F1 indicates BETTER hate-speech detection performance, making it a plausible but incorrect distractor.

**Q7.** The Estimated cost benchmark in the Foundry portal combines input and output token costs using what ratio?

A. 1:1 (equal input and output token counts)
B. 1:3 (one input token for every three output tokens)
C. 3:1 (three input tokens for every one output token)
D. 5:1 (five input tokens for every one output token)

**Answer:** C — The module states: "Estimated cost combines input and output costs using a typical 3:1 ratio (three input tokens for every output token)."

**Q8.** A developer building a real-time streaming chat interface cares most about how quickly the first word of a response appears. Which performance metric should they prioritize?

A. Latency P99 (tail latency)
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

A. MMLU-Pro (knowledge)
B. GPQA (graduate QA)
C. HumanEval+ and MBPP+
D. IFEval (instructions)

**Answer:** C — HumanEval+ and MBPP+ are listed as code generation task datasets. MMLU-Pro assesses general knowledge, GPQA is graduate-level multi-discipline QA, and IFEval measures instruction following.

**Q36.** How can a developer access model quality/safety/cost/performance benchmarking tools in the Foundry portal? (Choose the pairing that is complete per the module.)

A. Only through the Model catalog → Model leaderboard, which the module describes as sufficient on its own without the model card's Benchmarks tab
B. Model catalog → Model leaderboard (comparative rankings across all models), and Model card → Benchmarks tab (detailed metrics for one model with comparisons)
C. Only through the Evaluator library, which the module describes as the sole location for reviewing quality, safety, and performance benchmark data
D. Only through the Azure Cost Management portal, which surfaces token pricing and estimated cost benchmarks alongside subscription billing history

**Answer:** B — The module explicitly states benchmarking tools are "accessed two ways": the Model leaderboard for comparative rankings, and a model card's Benchmarks tab for detailed metrics/datasets on a single model plus comparison charts vs. similar models.

**Q37.** The Quality index shown in the Foundry portal is normalized to what numeric range, and what does it represent?

A. 0 to 100; a raw token count summed across all benchmark datasets used during the model's quality evaluation run
B. 0 to 1; an average of accuracy scores across multiple benchmark datasets measuring reasoning, knowledge, QA, math, and coding
C. -1 to 1; a sentiment polarity score derived from the ToxiGen adversarial hate speech detection benchmark
D. 1 to 5; a human star rating collected from structured manual review by evaluators in the playground

**Answer:** B — The module states the Quality index "averages accuracy scores across multiple benchmark datasets... Scores are normalized indexes ranging from 0 to 1, where higher scores indicate better overall quality."

**Q38.** Which quality benchmark dataset is described as testing "adversarial question answering"?

A. Arena-Hard
B. MATH suite
C. IFEval set
D. MMLU-Pro

**Answer:** A — Arena-Hard is listed in the module as the adversarial question-answering dataset among the quality benchmarks.

**Q39.** Which quality benchmark dataset specifically measures reasoning capabilities (as opposed to knowledge recall)?

A. MMLU-Pro set
B. BIG-Bench Hard
C. HumanEval+
D. WMDP score

**Answer:** B — BIG-Bench Hard is listed as measuring reasoning capabilities. MMLU-Pro instead assesses general knowledge; HumanEval+ assesses code generation; WMDP is a safety (not quality) benchmark.

**Q40.** Which quality benchmark dataset is used specifically for mathematical reasoning, and which for graduate-level, multi-discipline questions? (Choose the correct pairing.)

A. MATH — mathematical reasoning; GPQA — graduate-level multi-discipline questions
B. GPQA — mathematical reasoning; MATH — graduate-level multi-discipline questions
C. IFEval — mathematical reasoning; Arena-Hard — graduate-level multi-discipline questions
D. MMLU-Pro — mathematical reasoning; BIG-Bench Hard — graduate-level multi-discipline questions

**Answer:** A — Per the module's quality benchmark dataset list: MATH tests mathematical reasoning, and GPQA tests graduate-level, multi-discipline questions.

**Q41.** HarmBench's harmful-behavior detection tests THREE functional areas. Which set correctly lists them?

A. Standard harmful behaviors (cybercrime, illegal activity, general harm); contextually harmful behaviors (misinformation, harassment, bullying); copyright violations
B. Toxic language, sentiment bias, and factual hallucination, all measured using the ToxiGen F1 detection score across minority group references
C. Data leakage, prompt injection, and model theft, three security risks typically mitigated through Azure AI Content Safety filters rather than HarmBench testing
D. Fairness, reliability, and transparency, three of the module's core responsible AI principles rather than HarmBench's functional harm-testing categories

**Answer:** A — The module states HarmBench tests three functional areas: standard harmful behaviors, contextually harmful behaviors, and copyright violations, using these exact examples.

**Q42.** The ToxiGen safety benchmark measures a model's ability to avoid generating adversarial and implicit hate speech. How is performance scored, and in which direction is "better"?

A. Attack Success Rate from HarmBench; lower is better
B. F1 scores across references to minority groups; higher is better
C. WMDP score from the biosecurity proxy benchmark; lower is better
D. Quality index averaged across benchmarks; higher is better

**Answer:** B — The module states ToxiGen "measures adversarial and implicit hate speech detection... higher F1 scores indicate better detection performance" across references to minority groups.

**Q43.** How are "Cost per input tokens" and "Cost per output tokens" expressed in the Foundry cost benchmarks?

A. Price per single token processed, billed individually rather than in batches of a million tokens
B. Price per 1 million input tokens and price per 1 million output tokens, respectively
C. A flat monthly subscription fee, similar to Azure Marketplace licensing for partner catalog models
D. Price per API call, regardless of token count, as some third-party embedding services structure billing

**Answer:** B — The module defines these as "the price per 1 million input tokens (text you send to the model)" and "the price per 1 million output tokens (text the model produces)."

**Q44.** A developer wants to know the response time within which 95% of requests to a model complete. Which performance metric should they look at?

A. Latency mean
B. Latency P50
C. Latency P95
D. Time to first token

**Answer:** C — Latency P95 is defined as the time within which 95% of requests complete. P50 (median) is where 50% complete faster, and Latency mean is simply the average processing time — both distinct from the 95th-percentile figure requested.

**Q45.** Which throughput metric measures the COMBINED input and output tokens processed per second, as distinct from the metric measuring only output tokens per second?

A. Total tokens per second (TTPS) is combined input+output; Generated tokens per second (GTPS) is output-only
B. GTPS is combined input+output; TTPS is output-only, reversing the module's actual metric naming convention
C. Both measure only input tokens processed per second, ignoring output generation entirely during benchmarking
D. Time between tokens measures combined input+output throughput, rather than the interval between generated tokens

**Answer:** A — The module defines GTPS as "output tokens processed per second" and TTPS as "combined input and output tokens processed per second." Time between tokens instead measures the interval between consecutive tokens, not a throughput rate.

**Q46.** What are "Scenario leaderboards" in the Foundry portal used for, and when does the module recommend starting with them instead of the overall quality index?

A. They rank models by Azure subscription cost only, ignoring quality, safety, and performance benchmarks entirely; use them when budget is the sole concern
B. They rank models optimized for specific use cases like reasoning, coding, math, QA, and groundedness; use them when your application maps to one of these specific scenarios
C. They exist only for safety benchmarking, aggregating HarmBench ASR and ToxiGen F1 scores rather than quality or cost metrics across scenarios
D. They replace the need for the Evaluator library entirely, since scenario leaderboards already compute custom evaluator scores automatically for any agent

**Answer:** B — The module states scenario leaderboards show "models optimized for specific use cases: reasoning, coding, math, QA, groundedness," and recommends starting there "if your app maps to a specific scenario, rather than relying solely on the overall quality index."

**Q47.** When using the Foundry side-by-side model comparison feature, how many models can be selected for comparison, and what categories of information does the comparison include?

A. Exactly 5 models; only pricing information is shown, omitting performance benchmarks, model details, endpoints, and feature support entirely
B. 2 or 3 models; performance benchmarks, model details (context window, training data, supported languages), supported endpoints, and feature support (function calling, structured output, vision)
C. Only 1 model at a time; safety benchmarks only are displayed, without any side-by-side performance, endpoint, or feature-support comparison
D. Unlimited models; only the quality index is shown, without performance benchmarks, model details, endpoints, or feature support columns

**Answer:** B — The module states you "select 2 or 3 models from the leaderboard" via checkboxes and select Compare, viewing performance benchmarks, model details, supported endpoints, and feature support.

## Deploy models to endpoints

**Q11.** A company needs guaranteed predictable high throughput for a production workload and is willing to reserve capacity in advance, with no requirement to stay within a specific data zone. Which deployment type should they choose?

A. Global Standard
B. Global Provisioned
C. Data Zone Provisioned
D. Developer tier

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
D. Standard tier

**Answer:** A — Data Zone Standard ensures data stays within a specific data zone on a pay-per-token basis, ideal for EU/US data zone compliance without committing to reserved PTUs. Data Zone Provisioned (B) requires reserved throughput commitment, inappropriate for low/unpredictable volume; Standard (D) restricts to a single region rather than a data zone.

**Q14.** During model deployment configuration, what is the purpose of the "Deployment name" field?

A. It sets the Azure resource group name used for billing and role-based access control across all project deployments
B. It is used in the `model` parameter of API requests at inference time to route requests to that specific deployment
C. It configures the virtual machine SKU used for managed-compute deployments requiring reserved compute quota
D. It determines which Azure region the model is deployed to, independent of the deployment type's data-residency scope

**Answer:** B — The module states: "During inference, your code uses this deployment name in the `model` parameter to route requests," and later reiterates it under "Access models programmatically."

**Q15.** Which TWO authentication methods can an application use to call a deployed Foundry model endpoint, with one being recommended for production? (Choose 2.)

A. An authentication key/token
B. Microsoft Entra ID authentication (recommended for production)
C. SSH key-based authentication
D. Anonymous public access

**Answer:** A, B — The module states you can use an authentication key/token, "Alternatively, you can use Microsoft Entra ID authentication... Entra ID authentication is recommended for production scenarios." SSH keys and anonymous access are not mentioned as valid options.

**Q16.** A model from a partner in the Foundry catalog (not sold directly by Azure) requires an additional step before deployment that Azure OpenAI models like GPT-4o-mini do NOT require. What is this step?

A. Configuring a virtual network for private endpoint connectivity
B. Accepting an Azure Marketplace subscription's terms of use
C. Requesting Azure Machine Learning compute quota
D. Enabling Microsoft Entra ID authentication tenant-wide

**Answer:** B — The module notes that models requiring an Azure Marketplace subscription (common for partner/community models) show terms of use requiring "Agree and Proceed," while models sold directly by Azure, like GPT-4o-mini, don't require marketplace subscriptions.

**Q48.** Which deployment type does the module explicitly recommend using "whenever possible for maximum capabilities"?

A. Developer tier
B. Regional Provisioned
C. Global Standard
D. Data Zone Batch

**Answer:** C — The module states: "Global Standard deployments in Foundry resources should be used whenever possible for maximum capabilities."

**Q49.** A team has a large volume of non-urgent inference requests that can tolerate up to a 24-hour turnaround and wants the lowest possible cost. Which deployment type is designed for this?

A. Global Standard, billed per-token in real time with no batch discount or asynchronous processing delay
B. Global Batch — offering a 50% discount for asynchronous processing completed within 24 hours
C. Global Provisioned, using reserved PTU capacity billed continuously regardless of request volume or urgency
D. Standard, restricted to a single Azure region with pay-per-token billing and no batch-processing discount

**Answer:** B — Global Batch is described as offering a 50% discount, processed asynchronously, within 24 hours, and is best suited for large asynchronous batch jobs.

**Q50.** An organization needs large asynchronous batch job processing at a discount, while also keeping all data within a specific EU/US data zone for compliance. Which deployment type matches both requirements?

A. Global Batch
B. Data Zone Batch
C. Data Zone Standard
D. Regional Provisioned

**Answer:** B — Data Zone Batch provides discounted asynchronous processing for large batch jobs while keeping processing within a specific data zone, combining the compliance need with batch-discount economics.

**Q51.** Which deployment type provides reserved PTU-based predictable throughput while restricting deployment to a single Azure region (rather than any region or a data zone)?

A. Global Provisioned
B. Regional Provisioned
C. Data Zone Provisioned
D. Standard deployment

**Answer:** B — Regional Provisioned uses reserved PTUs for predictable throughput but is scoped to a single region, unlike Global Provisioned (any region) or Data Zone Provisioned (a specific data zone).

**Q52.** From the Foundry portal homepage, which navigation path does the module describe for beginning a model deployment?

A. Build → Evaluation → New Evaluation, the path for automated quality and safety scoring
B. Discover → Models (left pane), then open the model card and select Deploy
C. Settings → Billing → Add Model, the path for configuring Azure Marketplace subscription billing
D. Manage → Access Control → Deploy, the path for configuring Entra ID role assignments

**Answer:** B — Step 1 of the deployment walkthrough: "From the Foundry portal homepage, select Discover, then Models from the left pane."

**Q53.** When deploying a model, what is the difference between choosing "Default settings" versus "Custom settings"?

A. Default settings deploys to a random Azure region chosen automatically by the platform; Custom settings lets you pick a specific model and provider manually
B. Default settings applies a quick, recommended configuration; Custom settings lets you adjust configuration options like deployment type and compute in detail
C. Default settings is only available for partner and community models; Custom settings is restricted exclusively to Azure OpenAI models sold directly by Azure
D. There is no functional difference — both produce identical deployments regardless of which configuration options or deployment type you select

**Answer:** B — The module presents "Default settings (quick, recommended configuration)" as the alternative to "Custom settings" when deploying a model.

**Q54.** For a managed-compute deployment, what prerequisite must exist in your subscription before you can select a particular Virtual machine SKU?

A. An active Azure Marketplace subscription, required only for partner and community catalog models
B. Sufficient Azure Machine Learning compute quota for that SKU in your subscription
C. A configured Microsoft Entra ID tenant with production authentication enabled for the deployment
D. A pre-existing PTU reservation covering the throughput units needed for provisioned-type deployments

**Answer:** B — The module notes that Virtual machine SKU selection (managed compute only) "requires sufficient Azure Machine Learning compute quota for the SKU in your subscription."

**Q55.** In a managed-compute model deployment, what does the "Instance count" setting control?

A. The number of API keys generated for the deployment
B. The number of instances used for load distribution and redundancy
C. The number of tokens allowed per request before the API returns a truncation error
D. The number of days the deployment stays active

**Answer:** B — Instance count (managed compute only) is described as "the number of instances for load distribution and redundancy."

**Q56.** After deploying a model, where in the Foundry portal can a developer view the deployment's endpoint URL, authentication keys/tokens, and monitoring/usage metrics, or delete the deployment?

A. Discover → Models, used for browsing the catalog rather than managing deployments
B. Build → Models (left pane), by selecting the specific deployment
C. Exercise → Lab environment, a Learn sandbox unrelated to the portal's deployment view
D. Learning objectives page, a module summary unrelated to the Foundry portal itself

**Answer:** B — Under "Manage deployed models," the module states: "In the Foundry portal, select Build, then Models from the left pane to see your deployment list. Selecting a deployment shows configuration and status, the endpoint URL, authentication keys/tokens, monitoring/usage metrics, and options to adjust settings or delete."

**Q57.** In the Foundry playground, what is the purpose of a "system message"?

A. It logs errors encountered during testing sessions so developers can review them later in the monitoring tab
B. It sets context, tone, and instructions that are applied to all user inputs, e.g. "respond as a customer service representative"
C. It configures the virtual machine SKU for the deployment, applicable only to managed-compute deployment types
D. It defines the deployment's billing plan, choosing between pay-per-token Standard billing and reserved PTU billing

**Answer:** B — The module describes system messages as setting "the context, tone, and instructions" applied across all user inputs, giving the customer-service-representative example.

**Q58.** In the Foundry playground, which THREE parameters are described as adjustable when testing a model, and what does the "Code tab" provide?

A. Temperature, max tokens, and top-p control response creativity/length/sampling; the Code tab shows sample code (Python, C#, JavaScript) for authentication, endpoint configuration, and request formatting
B. Only temperature is adjustable; the Code tab shows billing information summarizing per-token cost estimates for the current Standard pricing tier
C. Region, SKU, and instance count are adjustable; the Code tab shows deployment logs capturing request/response history and error traces from managed compute
D. Only max tokens is adjustable; there is no Code tab, since sample code snippets are instead generated separately through the Foundry SDK documentation

**Answer:** A — The module lists temperature (creativity vs. consistency), max tokens (response length limit), and top-p (nucleus sampling) as adjustable parameters, and describes the Code tab as showing copyable sample code for authentication, endpoint config, and request formatting in Python, C#, and JavaScript.

**Q59.** When accessing a deployed model programmatically, the module describes two types of endpoint URLs. What are they?

A. REST endpoints and SOAP endpoints, an older enterprise messaging distinction not used for Foundry model access
B. Project endpoints (Foundry-specific functionality) and OpenAI v1 endpoints (broad OpenAI API compatibility)
C. Public endpoints and private endpoints, a network-exposure distinction configured via virtual network settings
D. Batch endpoints and streaming endpoints, a distinction based on synchronous versus asynchronous response delivery

**Answer:** B — The module states Foundry "supports project endpoints (Foundry-specific functionality) and OpenAI v1 endpoints (broad OpenAI API compatibility)" as the two endpoint URL types needed to call a deployment.

## Evaluate model performance

**Q17.** Which automated evaluation metric provides a BINARY (grounded / not grounded) assessment, useful specifically when factual accuracy requirements demand a clear-cut answer?

A. Coherence score
B. Fluency rating
C. Groundedness Pro
D. Relevance score

**Answer:** C — The module states: "Groundedness Pro offers binary assessment (grounded or not grounded) useful for factual accuracy requirements." Coherence, Fluency, and Relevance are scored on a scale/other criteria, not binary.

**Q18.** For content-harm risk and safety metrics (e.g., violent content, hateful content), how does Microsoft Foundry aggregate results?

A. As a normalized 0–1 quality index averaged across coherence, fluency, relevance, and groundedness scores
B. As a "defect rate" — the percentage of responses exceeding a severity threshold (typically Medium)
C. As an F1-score comparing generated content-harm labels to ground truth annotations from human reviewers
D. As an Attack Success Rate, the same metric HarmBench uses to measure adversarial jailbreak resistance

**Answer:** B — The module states: "For content harm metrics, results aggregate as defect rate—the percentage of responses exceeding a severity threshold (typically Medium)." Attack Success Rate (D) is specific to HarmBench in the model-catalog benchmarking unit, not the general Evaluation feature's content-harm aggregation.

**Q19.** A team wants to evaluate summarization quality where covering key points matters more than avoiding extra generated words, and they have reference summaries available. Which NLP metric is BEST suited?

A. BLEU
B. ROUGE
C. F1-score
D. WMDP

**Answer:** B — ROUGE "emphasizes recall over precision, making it particularly useful for summarization tasks where covering key points matters more than avoiding extra words" — this is verbatim from the module. BLEU is more associated with machine translation (n-gram precision-oriented); WMDP is a safety benchmark, not an NLP quality metric.

**Q20.** Which metric extends BLEU by additionally accounting for synonyms, stemming, and paraphrasing?

A. GLEU score
B. METEOR
C. ROUGE
D. F1-score

**Answer:** B — METEOR (Metric for Evaluation of Translation with Explicit ORdering) "extends BLEU by accounting for synonyms, stemming, and paraphrasing, providing more flexible comparison."

**Q21.** A developer lacks a labeled test dataset for evaluating a newly deployed agent. Within the Foundry Evaluation feature, what option lets them proceed without manually curating test data first?

A. Use existing dataset
B. Generate synthetic dataset
C. Dataset-based evaluation
D. Groundedness Pro metric

**Answer:** B — "Generate synthetic dataset: If you lack test data, the system can generate sample data based on a topic description you provide," specifying the generating resource, number of rows, and a descriptive prompt (optionally uploading files to improve relevance).

**Q22.** When AI-assisted (generation quality) evaluation metrics are used in Foundry, what must the developer specify to perform the assessment?

A. A ground truth reference dataset only
B. A GPT model to act as the evaluator
C. An Azure Content Safety filter policy
D. A vector index for retrieval grounding

**Answer:** B — "When using AI-assisted evaluation, you specify a GPT model to perform the assessment. This evaluator model analyzes your deployed model's responses and assigns scores based on the selected criteria." NLP metrics (not AI-assisted) are the ones that instead typically require ground truth data (A).

**Q23.** Evaluation results show elevated safety-metric defect rates for a deployed chatbot. Which of the following is explicitly recommended as a mitigation in the module?

A. Increasing the temperature parameter to produce more varied and creative chatbot responses
B. Implementing Azure AI Content Safety services as content filters
C. Switching to the Developer deployment type, restricted to fine-tuned evaluation only
D. Increasing the max tokens parameter to allow longer chatbot responses per request

**Answer:** B — Under "When safety metrics show concerns," the module lists content filters (implementing Azure AI Content Safety services), prompt hardening, and output validation. None of the other options address safety concerns as documented.

**Q24.** In the Evaluator library within a Foundry project, which capability is explicitly supported for custom evaluators?

A. Automatic deployment to production without review, bypassing the staged evaluation approval workflow
B. Version management — comparing versions, restoring previous versions, and collaborating with others
C. Direct billing integration with Azure Cost Management, surfacing per-evaluator token spend in real time
D. Automatic translation of evaluator prompts into multiple languages using the Azure Translator service

**Answer:** B — "The library supports version management, letting you compare different versions, restore previous versions if needed, and collaborate with others on custom evaluators."

**Q60.** Which FOUR reasons does the module give for evaluating model performance?

A. Quality assurance, user satisfaction, continuous improvement, compliance and safety
B. Marketing differentiation, investor reporting, headcount planning, vendor negotiation
C. Reduced cloud spend, faster deployment, smaller model size, fewer parameters
D. SEO ranking, brand awareness, social media reach, customer acquisition cost

**Answer:** A — The module lists exactly these four reasons: quality assurance (catch issues before production), user satisfaction (understand real user experience), continuous improvement (track enhancement opportunities), and compliance and safety (verify adherence to policy, avoidance of harmful content, privacy/data protection).

**Q61.** What is the benefit of testing models "side by side" during interactive playground testing, as described under manual evaluation?

A. It doubles the token quota for the session, allowing longer conversations across both compared models
B. It lets you synchronize system instructions/prompts across two models to directly compare their responses
C. It automatically calculates BLEU and ROUGE scores for each response without requiring a reference dataset
D. It is required before any deployment can go live, per the module's mandatory pre-production testing gate

**Answer:** B — Interactive testing in the playground is described as qualitative exploration that "can test models side by side, synchronizing system instructions/prompts to compare" them directly.

**Q62.** In structured manual review, human evaluators typically rate model responses against which FIVE criteria, usually on a rating scale?

A. Relevance, Informativeness, Engagement, Accuracy, Safety
B. Latency, Throughput, Cost, Quality, Security
C. Precision, Recall, F1-score, BLEU, and ROUGE
D. Fairness, Reliability, Privacy, Inclusiveness, Transparency

**Answer:** A — The module states structured review uses test-case sets where human evaluators rate on Relevance, Informativeness, Engagement, Accuracy, and Safety, typically on a scale (e.g., 1–5), aggregated across test cases.

**Q63.** What unique value do "user studies" add to manual evaluation, beyond what controlled/structured testing provides?

A. They eliminate the need for any automated metrics entirely, replacing BLEU, ROUGE, F1-score, and AI-assisted evaluation with purely qualitative feedback
B. They surface issues like confusing phrasing, missing context, or unmet expectations that controlled testing misses, by gathering feedback from real/representative users
C. They calculate the Quality index automatically by averaging accuracy scores across reasoning, knowledge, QA, math, and coding benchmark datasets
D. They replace the need for an evaluator GPT model entirely, since user studies score responses using the same AI-assisted criteria automatically

**Answer:** B — The module states user studies gather "feedback from real or representative users," surfacing issues such as confusing phrasing, missing context, or unmet expectations that controlled testing might miss.

**Q64.** Among the automated "generation quality" metrics, which one specifically measures whether a response's logical flow and ideas are consistent, as distinct from whether the response addresses the user's request or is based on provided context?

A. Relevance
B. Groundedness
C. Coherence
D. Fluency

**Answer:** C — Coherence specifically measures logical flow and consistent ideas. Relevance measures whether the response appropriately addresses the user's request; Groundedness measures whether the response is based on provided context vs. speculation; Fluency measures linguistic correctness/natural language quality.

**Q65.** Which of the following is NOT one of the risk and safety metrics listed in the module's automated evaluation section?

A. Self-harm content
B. Protected material
C. Indirect attack (jailbreak)
D. Latency P99

**Answer:** D — The listed risk and safety metrics are self-harm content, hateful and unfair content, violent content, sexual content, protected material, and indirect attack (jailbreak). Latency P99 is a performance benchmark metric from a different section, not a risk/safety metric.

**Q66.** For the "protected material" and "indirect attack" risk/safety metrics specifically, how is the defect rate calculated?

A. (true instances / total instances) × 100
B. A normalized 0–1 index averaged across datasets
C. Attack Success Rate from HarmBench
D. F1-score against ground truth

**Answer:** A — The module states: "For protected material and indirect attack, defect rate = (true instances / total instances) × 100," distinct from the general severity-threshold-based defect rate used for other content harm metrics.

**Q67.** When creating a comprehensive evaluation in the Foundry portal's Evaluation feature, which THREE "evaluation basis" options are available?

A. Model, Agent, Dataset
B. Endpoint, Region, SKU
C. Fast, Balanced, Thorough
D. Manual, Automated, Hybrid

**Answer:** A — The module lists exactly these three evaluation basis options: Model (evaluate a deployed model with prompts you specify), Agent (evaluate an agent's responses with user-defined prompts), and Dataset (evaluate pre-generated outputs already in a test dataset).

**Q68.** When evaluating a Model or Agent in the Foundry Evaluation feature, which dataset option lets you reuse data that was previously uploaded to your project, as opposed to bringing in a brand-new CSV/JSONL file?

A. Generate synthetic dataset
B. Use existing dataset
C. Upload new dataset
D. Groundedness Pro dataset

**Answer:** B — "Use existing dataset" reuses data previously uploaded to your project, while "Upload new dataset" brings in a CSV or JSONL file from local storage, and "Generate synthetic dataset" creates sample data from a topic description.

**Q69.** In the Evaluator library (Project → Evaluation page → Evaluator library tab), what can a developer review specifically for safety evaluators?

A. Their Azure billing history
B. Definitions and severity levels
C. Their virtual machine SKU requirements
D. Their PTU reservation status

**Answer:** B — The module states the Evaluator library lets you "check definitions and severity levels for safety evaluators," alongside reviewing annotation prompts for quality evaluators and viewing Microsoft-curated evaluators for quality, safety, and performance.

**Q70.** If evaluation results show low quality scores, the module lists a set of iteration options in increasing order of complexity/cost. What is that order?

A. Fine-tuning → RAG integration → different models → prompt engineering
B. Prompt engineering → different models → RAG integration → fine-tuning
C. Different models → fine-tuning → prompt engineering → RAG integration
D. RAG integration → prompt engineering → fine-tuning → different models

**Answer:** B — The module lists, in increasing complexity/cost order: prompt engineering (refine instructions/system messages), different models (try models optimized for the use case), RAG integration (add retrieval to ground responses), and fine-tuning (train on domain-specific data if supported).

**Q71.** Which NLP evaluation metric is described as the "ratio of shared words between generated and ground truth answers, balancing precision and recall," and is well suited to text classification and information retrieval?

A. BLEU score
B. F1-score
C. METEOR
D. GLEU score

**Answer:** B — The module defines F1-score exactly this way, contrasting it with BLEU (n-gram comparison, common for machine translation), METEOR (BLEU extended with synonyms/stemming/paraphrasing), and GLEU (a BLEU variant for sentence-level evaluation).

## Scenario-based questions

**Q72.** A startup needs a cost-efficient model for a high-volume, latency-sensitive mobile app FAQ feature, deployed with pay-per-token billing and no data-residency constraint, prioritizing the lowest possible Estimated cost (3:1 input:output ratio) among candidates. Which combination best satisfies this?

A. An LLM like GPT-5, deployed as Regional Provisioned
B. A Small Language Model like Phi-4, deployed as Global Standard
C. A reasoning model like Claude Opus 4.6, deployed as Developer
D. An embedding model, deployed as Data Zone Batch

**Answer:** B — SLMs (e.g., Phi-4) are efficient/cost-effective for common NLP tasks and can run on lower-end hardware, fitting a cost-sensitive FAQ scenario; Global Standard offers pay-per-token billing in any region with no data-zone constraint and is the module's recommended default "whenever possible."

**Q73.** A model scores high on WMDP and high (unsafe) on HarmBench ASR during pre-deployment benchmarking. After deployment, automated evaluation also shows an elevated defect rate for "hateful and unfair content." Which set of actions addresses these findings, per the module?

A. Increase max tokens and switch to Global Batch billing, since discounted asynchronous processing reduces both cost and defect rates
B. Choose a different, safer model at the benchmarking stage, and post-deployment implement Azure AI Content Safety content filters and prompt hardening
C. Ignore WMDP since higher is always better, and rely solely on ROUGE scores to measure summarization quality instead of safety
D. Switch to Developer deployment type, since it is restricted to safer fine-tuned models only and therefore cannot generate unsafe content

**Answer:** B — High WMDP (more dangerous-capability knowledge) and high ASR (easily jailbroken) both signal an unsafe model choice at selection time; post-deployment, the module's recommended mitigations for safety-metric concerns are content filters (Azure AI Content Safety), prompt hardening, and output validation.

**Q74.** A regulated EU financial services company needs predictable, reserved high-throughput capacity, must keep data within the EU data zone, and requires production-grade authentication. Which combination of deployment type and authentication method satisfies all requirements?

A. Global Standard with an authentication key only
B. Data Zone Provisioned with Microsoft Entra ID authentication
C. Standard with SSH key-based authentication
D. Developer with anonymous access, needing no authentication at all

**Answer:** B — Data Zone Provisioned offers reserved PTU-based predictable throughput while keeping data within a specific data zone; Microsoft Entra ID authentication is explicitly recommended for production scenarios (versus a simple key/token).

**Q75.** A team has no existing test dataset for a new summarization agent. They want to (1) generate test data automatically, and (2) score the agent's summaries against reference summaries emphasizing recall of key points over precision. Which combination of Foundry Evaluation features should they use?

A. Upload new dataset + BLEU
B. Generate synthetic dataset + ROUGE
C. Use existing dataset + WMDP
D. Groundedness Pro + GTPS throughput

**Answer:** B — With no test data available, "Generate synthetic dataset" creates sample data from a topic description; ROUGE emphasizes recall over precision, making it best suited for summarization tasks where covering key points matters more than avoiding extra words.

**Q76.** A developer has narrowed a shortlist to three coding-assistant candidate models. They want to (1) see how each ranks specifically for coding use cases rather than general quality, and (2) visualize the trade-off between quality and cost for the finalists before deciding. Which two Foundry portal features should they use, in order?

A. Model leaderboard sorted by safety, then the Evaluator library
B. Scenario leaderboard (coding), then a trade-off chart plotting quality vs. cost
C. Model card Benchmarks tab only, ignoring leaderboards and scenario-specific rankings entirely
D. Side-by-side comparison of feature support only, ignoring benchmarks

**Answer:** B — The module recommends starting with a scenario leaderboard when your app maps to a specific use case like coding, then using a trade-off chart to visualize two metrics (e.g., quality vs. cost) at once to spot models that are slightly less accurate but significantly cheaper or faster.

**Q77.** During playground testing, a developer lowers the temperature parameter to reduce randomness and sets a system message defining a formal support-agent tone. After deployment, they configure an AI-assisted evaluation. What must they additionally specify to run that AI-assisted evaluation, and what is that component's role?

A. A VM SKU; it hosts the evaluation compute needed for managed-compute deployments running the scoring job
B. A GPT model as the evaluator; it analyzes the deployed model's responses and assigns scores based on selected criteria
C. A PTU reservation; it guarantees evaluation throughput by reserving provisioned capacity ahead of the scoring run
D. An Azure Marketplace subscription; it licenses the evaluation feature for partner and community catalog models

**Answer:** B — AI-assisted (generation quality) evaluation requires specifying a GPT model to act as the evaluator, which analyzes the deployed model's responses and assigns scores — separate from playground parameters like temperature and system messages, which shape generation, not evaluation.

**Q78.** An end-to-end pipeline: a developer filters the catalog by Industry to find a legal-domain model, deploys it as Data Zone Standard for EU compliance, tests it in the playground with a system message and top-p adjustment, then runs a comprehensive evaluation using the "Agent" basis with a synthetic dataset, and finally acts on low groundedness scores. Which action correctly addresses low groundedness per the module's iteration guidance?

A. Increase the Instance count to add more managed-compute replicas for load distribution and redundancy
B. Add RAG integration to ground responses in retrieved data (or, if still insufficient, consider fine-tuning)
C. Switch the deployment type to Developer, since it is restricted to fine-tuned evaluation scenarios only
D. Lower the Quality index threshold in the leaderboard so the model appears to score better on benchmarks

**Answer:** B — Groundedness issues are a quality concern; the module's iteration guidance for low quality scores includes prompt engineering, trying different models, RAG integration (to ground responses in your data), and fine-tuning — RAG integration directly targets groundedness by retrieving relevant context.
