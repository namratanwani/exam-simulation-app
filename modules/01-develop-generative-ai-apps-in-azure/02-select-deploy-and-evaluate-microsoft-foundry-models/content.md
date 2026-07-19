# Select, deploy, and evaluate Microsoft Foundry models

Source: https://learn.microsoft.com/en-us/training/modules/model-catalog-evaluate/

## Learning objectives

By the end of this module, you'll be able to:

- Explore and filter models in the model catalog
- Compare models using benchmark metrics for quality, safety, cost, and performance
- Deploy a model to an endpoint and test it in the playground
- Evaluate model performance using manual and automated approaches
- Understand different evaluation metrics and when to use them

Module info: Intermediate level, 8 units, tagged Data Scientist / AI Engineer / Microsoft Foundry. Prerequisites: fundamental AI concepts and services in Azure.

## Exam relevance

- **Plan and manage an Azure AI solution** → "Choose an appropriate model for each task, including LLMs, small language models, multimodal models, and Foundry Tools" — Explore model catalog unit; Understand generative AI model types.
- **Plan and manage an Azure AI solution** → "Configure model and agent deployments" — Deploy models to endpoints unit (deployment types, PTUs, endpoints).
- **Build generative applications by using Foundry** → "Deploy and consume LLMs, small models, code models, and multimodal models" — Deploy models unit.
- **Build generative applications by using Foundry** → "Evaluate models and apps, including detecting fabrications, relevance, quality, and safety" — Evaluate model performance unit (groundedness, safety metrics, NLP metrics).
- **Implement responsible AI across generative AI and agentic systems** → "Apply responsible AI instrumentation, including evaluators, safety evaluations, and explanation tooling" — Evaluator library, risk/safety metrics.
- **Manage, monitor, and secure AI systems** → "Manage quotas, scaling, rate limits, and cost footprints for model and agent workloads" — Cost benchmarks, PTUs, deployment types.

## Introduction

Scenario used throughout: building an AI-powered customer support chatbot for a retail company — need to select a model that understands questions, provides accurate responses, and maintains tone/safety. The Foundry portal supports the full workflow: explore >1,900 models from providers like Microsoft, Anthropic, OpenAI, Meta, and Hugging Face; compare via industry-standard benchmarks (quality, safety, cost, performance); deploy to an endpoint; evaluate with automated metrics and manual testing.

## Explore the model catalog

The **Foundry Models catalog** is the central hub for discovering/comparing AI models — over **1,900 models** from various providers.

Two broad categories of models in the catalog:
- **Foundry Models sold directly by Azure** — billed directly through your Azure subscription; includes Azure OpenAI models and models from Microsoft and other providers.
- **Foundry Models from partners and community** — provided by trusted partners/community, each with own licensing and pricing.

### Finding models
Each model has a **model card** showing provider, capabilities, benchmark metrics, responsible AI considerations, and deployment options. You can search by keyword and filter by:
- **Collection** — e.g., models provided directly in Azure, or models in the Hugging Face repository.
- **Capabilities** — *reasoning* (complex problem-solving), *tool calling* (API/function integration), *multimodal processing* (text, images, audio).
- **Source** — provider: Azure OpenAI, Microsoft, Cohere, Mistral, Meta, Anthropic, others.
- **Inference tasks** — text generation, summarization, translation, image generation, speech synthesis, etc.
- **Fine-tuning methods** — supported fine-tuning techniques.
- **Industry** — models trained on industry-specific datasets (often outperform general-purpose models in their domain).

### Understand generative AI model types

- **Large Language Models (LLMs)** — e.g., GPT-5, Mistral Large, Llama 3 70B. Designed for deep reasoning, complex content generation, extensive context understanding. Excel at sophisticated apps but need more compute.
- **Small Language Models (SLMs)** — e.g., Phi-4, Mistral OSS models, Llama 3 8B. Efficient/cost-effective for common NLP tasks; ideal when speed/cost matter more than complex reasoning; can run on lower-end hardware or edge devices.

**Chat completion vs. reasoning models**:
- Most catalog models are **chat completion** models — generate coherent, contextually appropriate text responses; power conversational interfaces/content generation.
- **Reasoning models** (e.g., Claude Opus 4.6) — higher performance on complex tasks (math, coding, science, strategy, logistics); can break down problems and show their reasoning process.

**Specialized/task-specific models**:
| Type | Example | Purpose |
|---|---|---|
| Embedding models | Ada, Cohere | Convert text to numerical representations for semantic search, recommendation systems, RAG |
| Image generation models | GPT-image-1 | Create images from text descriptions |
| Video generation models | Sora 2 | Create video content from text descriptions |
| Image analysis models | GPT-4.1 | Multimodal input (text+images) → natural language output |
| Text to speech models | GPT-4o-tts | Convert text to synthesized speech |
| Speech to text models | GPT-4o-transcribe | Convert audio/speech to text transcriptions |

**Regional and domain-specific models**: optimized for specific languages/regions/industries (e.g., medical literature, legal documents, specific language corpora) — often outperform general-purpose models in their niche.

## Select models using benchmarks

Foundry portal provides quality, safety, cost, and performance benchmarking tools, accessed two ways:
- **Model catalog → Model leaderboard**: comparative rankings across all models, ranked by quality, safety, estimated cost, and throughput.
- **Model card → Benchmarks tab**: detailed metrics/datasets for one model, with comparison charts vs. similar models.

### Quality benchmarks
The **Quality index** averages accuracy scores across multiple benchmark datasets measuring reasoning, knowledge, QA, math, and coding. Higher = better. Scores are normalized indexes **0 to 1**.

Datasets used:
- **Arena-Hard** — adversarial question answering
- **BIG-Bench Hard** — reasoning capabilities
- **GPQA** — graduate-level multi-discipline questions
- **HumanEval+** and **MBPP+** — code generation
- **MATH** — mathematical reasoning
- **MMLU-Pro** — general knowledge assessment
- **IFEval** — instruction following

### Safety benchmarks
Ensure models don't generate harmful/biased/inappropriate content. Crucial for customer-facing/regulated scenarios.

- **Harmful behavior detection**: uses **HarmBench** → calculates **Attack Success Rate (ASR)** (lower = safer). Tests 3 functional areas: standard harmful behaviors (cybercrime, illegal activity, general harm), contextually harmful behaviors (misinformation, harassment, bullying), copyright violations.
- **Toxic content detection**: uses **ToxiGen** dataset → measures adversarial/implicit hate speech detection. Higher **F1 scores** = better detection (across references to minority groups).
- **Sensitive domain knowledge**: uses **WMDP** (Weapons of Mass Destruction Proxy) benchmark → measures model knowledge in biosecurity, cybersecurity, chemical security. Higher WMDP score = MORE knowledge of dangerous capabilities (i.e., higher is a risk indicator, not a "goodness" indicator like other benchmarks — exam nuance).

### Cost benchmarks
Displays pricing for serverless API deployments and Azure OpenAI models:
- **Cost per input tokens** — price per 1 million input tokens (text sent to model).
- **Cost per output tokens** — price per 1 million output tokens (text model produces).
- **Estimated cost** — combines input+output cost using a typical **3:1 ratio** (3 input tokens per 1 output token) into a single comparable number. Lower = more cost-effective.

### Performance benchmarks
**Latency measurements**:
- **Latency mean** — average time (seconds) to process a request
- **Latency P50** (median) — 50% of requests complete faster
- **Latency P90** — 90% of requests complete faster
- **Latency P95** — 95% of requests complete faster
- **Latency P99** — 99% of requests complete faster
- **Time to first token (TTFT)** — time until first token arrives (streaming)

**Throughput measurements**:
- **Generated tokens per second (GTPS)** — output tokens/sec
- **Total tokens per second (TTPS)** — combined input+output tokens processed/sec
- **Time between tokens** — interval between consecutive tokens

Leaderboard summarizes performance via mean TTFT (lower better) and mean GTPS (higher better).

### Leaderboards and comparison features
- **Model leaderboard** — sort by quality, safety, estimated cost, throughput.
- **Scenario leaderboards** — models optimized for specific use cases: reasoning, coding, math, QA, groundedness. Start here if your app maps to a specific scenario, rather than relying solely on overall quality index.
- **Trade-off charts** — plot two metrics at once (e.g., quality vs. cost, quality vs. throughput). Models near top-right corner perform well on both axes.
- **Side-by-side comparison** — select 2 or 3 models from leaderboard, compare: performance benchmarks (quality, safety, throughput), model details (context window, training data, supported languages), supported endpoints (deployment options), feature support (function calling, structured output, vision). Select via checkboxes, then **Compare**.

## Deploy models to endpoints

### Deployment types
| Deployment type | Region scope | Billing | Best for |
|---|---|---|---|
| **Global Standard** | Any Azure region | Pay-per-token | General workloads; highest quota |
| **Global Provisioned** | Any Azure region | Reserved **provisioned throughput units (PTU)** | Predictable high-throughput |
| **Global Batch** | Any Azure region | 50% discount, async, within 24 hours | Large asynchronous batch jobs |
| **Data Zone Standard** | Specific data zone (EU/US) | Pay-per-token | Data zone compliance |
| **Data Zone Provisioned** | Specific data zone | Reserved PTUs | Predictable throughput w/ data zone compliance |
| **Data Zone Batch** | Specific data zone | Discounted async | Large batch jobs w/ data zone compliance |
| **Standard** | Single region | Pay-per-token | Regional data residency compliance, low-volume scenarios |
| **Regional Provisioned** | Single region | Reserved PTUs | Predictable throughput, single region |
| **Developer** | Any Azure region | Pay-per-token | Fine-tuned model evaluation ONLY |

Each model indicates which deployment types it supports; the portal auto-selects the best option. **Global Standard deployments in Foundry resources should be used whenever possible for maximum capabilities.**

### Deploy a model (portal steps)
1. From Foundry portal homepage, select **Discover** → **Models** (left pane).
2. Open the model card, review specs/supported deployment types.
3. Select **Deploy**. Choose **Default settings** (quick, recommended config) or **Custom settings**.
4. If model requires Azure Marketplace subscription (common for partner/community models) — review terms, select **Agree and Proceed**. Models sold directly by Azure (e.g., GPT-4o-mini) don't require marketplace subscriptions.
5. Configure:
   - **Deployment name** — defaults to model name; customizable for multiple deployments of same model; used in the `model` parameter at inference time to route requests.
   - **Deployment type** — auto-selected but can be adjusted.
   - (Managed compute only) **Virtual machine SKU** — requires Azure Machine Learning compute quota for the SKU in your subscription.
   - (Managed compute only) **Instance count** — number of instances for load distribution/redundancy.
6. Select **Deploy**. On completion, lands in the **Foundry Playground**. Verify deployment status shows **Succeeded**.

### Manage deployed models
Foundry portal → **Build** → **Models** (left pane) shows deployment list. Selecting a deployment shows: configuration/status, **endpoint URL**, authentication keys/tokens, monitoring/usage metrics, options to adjust settings or delete.

### Test in the playground
- Auto-opens after deployment, or select a deployment to open it.
- Enter prompts, view input/output side by side.
- Test types: simple questions, complex multi-step reasoning, specific format/style requests, edge cases.
- **System messages** set context/tone/instructions applied to all user inputs (e.g., "respond as a customer service representative").
- Adjustable parameters: **temperature** (creativity vs. consistency), **max tokens** (response length limit), **top-p** (nucleus sampling).
- **Code tab** — shows sample code (Python, C#, JavaScript) for authentication, endpoint config, request formatting — copyable into your app.

### Access models programmatically
Three key pieces needed from deployment details:
- **Endpoint URL** — Foundry supports **project endpoints** (Foundry-specific functionality) and **OpenAI v1 endpoints** (broad OpenAI API compatibility).
- **Authentication key** — secret key/token, OR **Microsoft Entra ID authentication** (token based on app identity) — **Entra ID is recommended for production scenarios**.
- **Deployment name** — used in the `model` parameter of API requests to route to your specific deployment.

## Evaluate model performance

### Why evaluate
- **Quality assurance** — catch issues before production.
- **User satisfaction** — understand real user experience.
- **Continuous improvement** — track enhancement opportunities as prompts/features/models change.
- **Compliance and safety** — verify adherence to policy, avoidance of harmful content, privacy/data protection.

### Manual evaluation approaches
- **Interactive testing** in the playground — qualitative exploration; can test models **side by side**, synchronizing system instructions/prompts to compare.
- **Structured review** — test-case sets; human evaluators rate on: **Relevance**, **Informativeness**, **Engagement**, **Accuracy**, **Safety** — typically on a rating scale (e.g., 1–5), aggregated across test cases.
- **User studies** — feedback from real/representative users; surfaces issues (confusing phrasing, missing context, unmet expectations) that controlled testing misses.

Manual evaluation captures subjective aspects (user satisfaction, contextual appropriateness, brand alignment) automated metrics can't.

### Automated evaluation metrics

**Generation quality metrics**:
- **Groundedness** — whether responses are based on provided context vs. speculation. **Groundedness Pro** offers binary assessment (grounded / not grounded) — useful for factual accuracy requirements.
- **Relevance** — whether responses appropriately address the user's question/request.
- **Coherence** — logical flow, consistent ideas.
- **Fluency** — linguistic correctness, natural language quality.

**Risk and safety metrics**:
- **Self-harm content**
- **Hateful and unfair content**
- **Violent content**
- **Sexual content**
- **Protected material** — potential copyright/proprietary content reproduction
- **Indirect attack (jailbreak)** — vulnerability to manipulation

For content harm metrics, results aggregate as **defect rate** — % of responses exceeding a severity threshold (typically **Medium**). For protected material and indirect attack, defect rate = `(true instances / total instances) × 100`.

AI-assisted evaluation requires specifying a **GPT model as the evaluator** that analyzes the deployed model's responses and assigns scores.

### Natural language processing (NLP) metrics
Mathematical evaluation, no evaluator model needed — but usually require **ground truth data** (expected/correct responses):

- **F1-score** — ratio of shared words between generated and ground truth answers (balances precision/recall). Good for text classification, information retrieval.
- **BLEU** (Bilingual Evaluation Understudy) — compares n-grams between generated and reference texts; common for machine translation.
- **METEOR** (Metric for Evaluation of Translation with Explicit ORdering) — extends BLEU with synonyms, stemming, paraphrasing — more flexible.
- **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) — emphasizes recall over precision; useful for summarization (covering key points matters more than avoiding extra words).
- **GLEU** (Google-BLEU) — variant of BLEU for sentence-level evaluation.

NLP metrics work well with definitive correct answers/reference texts; less suitable for open-ended generation with many valid responses.

### Create comprehensive evaluations
Foundry portal's **Evaluation** feature runs systematic evaluations using test datasets + multiple metrics simultaneously. Evaluation basis options:
- **Model** — evaluate a deployed model with prompts you specify (system generates outputs during evaluation).
- **Agent** — evaluate an agent's responses with user-defined prompts.
- **Dataset** — evaluate pre-generated outputs already in a test dataset.

Dataset options (for Model/Agent evaluation):
- **Upload new dataset** — CSV or JSONL file from local storage.
- **Use existing dataset** — previously uploaded to your project.
- **Generate synthetic dataset** — system generates sample data from a topic description; you specify the generating resource, number of rows, and a descriptive prompt; can upload files to improve task relevance.

Configure metrics, field mappings, and system prompt, then start the evaluation job (runs asynchronously, processes each dataset row against selected metrics).

### Evaluator library
Centralized location (Project → **Evaluation** page → **Evaluator library** tab) to:
- View Microsoft-curated evaluators for quality, safety, performance.
- Examine evaluator details (name, description, parameters, associated files).
- Review annotation prompts for quality evaluators.
- Check definitions/severity levels for safety evaluators.
- Manage custom evaluators.
- Supports **version management** — compare versions, restore previous versions, collaborate on custom evaluators.

### Iterate based on evaluation
If quality scores are low, consider (increasing complexity/cost):
- **Prompt engineering** — refine instructions/system messages.
- **Different models** — try models optimized for the use case.
- **RAG integration** — add retrieval to ground responses in your data.
- **Fine-tuning** — train on domain-specific data (if supported).

If safety metrics show concerns:
- **Content filters** — implement **Azure AI Content Safety** services.
- **Prompt hardening** — add safety instructions to system messages.
- **Output validation** — check responses before displaying to users.

Establish evaluation benchmarks early; re-run after modifications to measure impact and prevent regression.

## Exercise — Select, deploy, and evaluate models

Hands-on lab (20 minutes, requires Azure subscription with administrative access) practicing the full select → deploy → test → evaluate workflow in the Foundry portal.
