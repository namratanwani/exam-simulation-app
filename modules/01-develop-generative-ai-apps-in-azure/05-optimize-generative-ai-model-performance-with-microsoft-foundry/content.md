# Optimize generative AI model performance with Microsoft Foundry

Source: https://learn.microsoft.com/en-us/training/modules/optimize-generative-ai-model-performance/

## Learning objectives

By the end of this module, you'll be able to:

- Apply prompt engineering techniques including system messages, few-shot learning, and model parameters to optimize model output.
- Understand when and how to ground a language model using Retrieval Augmented Generation (RAG).
- Identify when fine-tuning a model improves behavioral consistency.
- Compare optimization strategies and determine when to combine them.

**Prerequisites**: Familiarity with fundamental AI concepts and services in Azure.

## Exam relevance

Maps to **Learning Path 1 — Develop generative AI apps on Microsoft Foundry**. Supports:
- **"Implement generative AI and agentic solutions" (30–35%)** → *"Optimize and operationalize generative AI systems"*: *"Tune generation behavior, such as prompt engineering and adjusting model parameters"*.
- Same domain → *"Build generative applications by using Foundry"*: *"Implement retrieval-augmented generation (RAG) in an application"*.
- **"Plan and manage an Azure AI solution" (25–30%)** → *"Choose the appropriate Foundry services for generative AI and agents"*: *"Choose an appropriate method for retrieval and indexing"*.

This module is the canonical source for the exam's core "when to use prompt engineering vs. RAG vs. fine-tuning" decision framework.

## Introduction

A base language model might not meet all requirements out of the box (tone, accuracy on private data, consistent format). There are three complementary strategies to optimize performance, ranging from quick/low-cost to more involved:
1. Prompt engineering
2. Retrieval Augmented Generation (RAG)
3. Fine-tuning

These are **complementary, not mutually exclusive** — a recurring exam theme.

## Optimize model output with prompt engineering

**Prompt engineering**: designing/refining prompts to improve quality, accuracy, relevance of responses. No additional infrastructure or training data required; can start immediately.

### Prompt components (chat completion models)
- **System message** — instructions defining the model's behavior, role, constraints. Appears first; highest-level instructions.
- **User message** — the question/input from the user.
- **Assistant message** — previous model responses (multi-turn conversations).
- **Examples** — sample input/output pairs demonstrating expected format.

### System message design checklist
1. Start with the assistant's role.
2. Define boundaries (topics/actions/content to avoid).
3. Specify the output format (state plainly, keep consistent).
4. Add a "when unsure" policy (what to do when ambiguous/out of scope/lacking info).

> A system message **influences** but does **not guarantee** compliance — test/iterate, and layer with content filtering + evaluation.

### Prompt patterns
- **Persona pattern** — instruct the model to adopt a specific role/perspective (e.g., "You're a seasoned marketing professional...") to change response style.
- **Format template pattern** — provide a template/structure in the prompt for structured, parseable output.
- **Chain-of-thought pattern** — ask the model to reason step-by-step; reduces inaccuracy, aids verification. **Note: this is a technique for non-reasoning models — reasoning models (o-series) handle step-by-step logic internally**, so applying explicit CoT prompting to them is unnecessary/redundant. A related technique: **decompose** a task into explicit sub-steps across separate prompts (e.g., extract facts first, then answer based on those facts) rather than asking the model to do it all in one shot — reduces errors on complex, multi-part tasks.
- **Few-shot learning pattern** — provide one or more input/output examples so the model infers the pattern. **One-shot** = single example. **Zero-shot** = no examples provided.
- **Clear syntax/delimiters** — use `---`, Markdown headings, or XML tags to separate prompt sections (instructions vs. source text vs. examples), reducing misinterpretation.
- **Recency bias** — models can weight text near the *end* of a prompt more heavily. If instructions aren't followed consistently, repeat the key instruction at the end.

### Model parameters
- **Temperature** — controls randomness. Higher (e.g., 0.7) = more creative/varied. Lower (e.g., 0.2) = more focused/deterministic. Use low for factual tasks, high for creative tasks.
- **Top_p** — also controls randomness, but by limiting the model to the subset of most-probable next tokens (e.g., `top_p=0.9` → considers only the top 90% probability mass of tokens).
- **General recommendation: adjust temperature OR top_p, not both at the same time.** (Common exam trap.)

### When prompt engineering is enough
Good for: guiding tone/format/behavior, giving task instructions, fast iteration, low cost (no training/storage). **Limits**: can't give the model information it doesn't have access to; can't reliably force behavior the model resists despite detailed instructions — in those cases, add RAG and/or fine-tuning.

## Ground your model with Retrieval Augmented Generation (RAG)

Prompt engineering can't give a model new knowledge. Models have a training-data cutoff and no access to private org data by default → risk of **fabrication** (plausible-sounding but factually wrong output).

**Grounding**: supplying relevant, factual data alongside the user's question so the model bases its answer on that data instead of (only) its training data.

### RAG pattern — 3 steps
1. **Retrieve** — search a data source for information relevant to the user's question.
2. **Augment** — add the retrieved information to the prompt as context.
3. **Generate** — send the augmented prompt to the model to produce a grounded response.

### Embeddings & vector search
- **Embedding**: a mathematical vector representation of text capturing semantic meaning. Created by sending content to an embedding model (e.g., an Azure OpenAI embedding model in Microsoft Foundry).
- Semantically similar text → vectors close together in multidimensional space, even with different wording.
- **Cosine similarity**: measures closeness between two vectors via the angle between them; value near 1 = very similar.

### Azure AI Search for retrieval
**Azure AI Search** is the retrieval component for RAG in Microsoft Foundry. Workflow:
1. **Add your data** to Foundry from Azure Blob Storage, Azure Data Lake Storage Gen2, Microsoft OneLake, or direct file upload.
2. **Create an index** using an embedding model to generate vector representations; index stored in Azure AI Search.
3. **Query the index** — user question is embedded, index is searched for similar content, relevant results returned.

**Azure AI Search techniques:**
- **Keyword search** — exact term matching.
- **Semantic search** — matches meaning via semantic models, not exact keywords.
- **Vector search** — uses embeddings to find semantically similar content.
- **Hybrid search** — combines keyword + semantic + vector. **Recommended for generative AI applications** (exam-relevant recommendation).

### Implementing RAG with the Microsoft Foundry SDK
Use the `azure-ai-projects` SDK to get an authenticated OpenAI client via `AIProjectClient`, then call the **Responses API** (`client.responses.create(...)`), injecting `retrieved_context` (from the Azure AI Search index) into the system message.

```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

client = project.get_openai_client()

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "You are a helpful travel advisor. "
         "Use the following hotel data to answer: " + retrieved_context},
        {"role": "user", "content": "Which hotels do you offer in Paris?"},
    ],
)

print(response.output_text)
```

### When to use RAG
- Model needs domain-specific/private knowledge (product catalog, policy docs, internal KB).
- Information changes frequently (inventory, pricing, news) — RAG retrieves current data at query time without retraining.
- Factual accuracy is critical.
- Data postdates the model's training cutoff.

> **Tip / cross-reference**: If building agents that need grounded knowledge without managing your own search infrastructure, consider **Foundry IQ** — a managed knowledge store that simplifies grounding for AI agents (see the "Build knowledge-enhanced AI agents with Foundry IQ" module notes). This is a key exam distinction: **Azure AI Search = you manage the index/infra yourself; Foundry IQ = managed knowledge platform for agents.**

## Fine-tune a model for consistent behavior

Use when the model **ignores or inconsistently follows instructions** even with detailed system messages/few-shot examples, despite prompt engineering and RAG.

**Fine-tuning**: taking a pretrained model and further training it on a smaller, task-specific dataset, adjusting internal weights so output matches the training data's patterns.

- Uses **LoRA (Low-Rank Adaptation)** — approximates weight changes with a lower-rank representation; updates only a smaller subset of parameters instead of retraining everything → faster, more cost-effective, quality maintained.
- Key benefit over training from scratch: efficiency (less time, compute, data).

### When to fine-tune
- Consistent brand style/tone across all interactions.
- Specific structured output formats (e.g., JSON schema) that few-shot alone can't reliably enforce.
- Reducing prompt length/token cost — fine-tuning embeds patterns into the model so long system messages/examples aren't needed each request.
- **Distillation** — transfer capability from a large/expensive model to a smaller/cheaper one by fine-tuning the smaller model on the larger model's outputs.
- Enhancing tool-calling accuracy (tool selection + parameter generation) via fine-tuning with tool-call examples.

> **Important**: always evaluate baseline performance of the standard model first — without a baseline you can't tell if fine-tuning helped or hurt.

### Types of fine-tuning in Microsoft Foundry
- **Supervised fine-tuning (SFT)** — train on a labeled dataset of prompt/response pairs; best for clear, well-defined tasks.
- **Reinforcement fine-tuning (RFT)** — iterative feedback via a grader that rewards better responses; best for complex/dynamic tasks with many valid solutions, improving reasoning quality.
- **Direct Preference Optimization (DPO)** — aligns the model using preferred vs. non-preferred response pairs; computationally lighter than traditional RL, equally effective for alignment.
- Techniques can be **combined** (e.g., SFT first, then DPO to further align).

### Training data format
JSONL, one JSON object per line, each a chat conversation with `role`/`content` messages (system/user/assistant):
```json
{"messages": [{"role": "system", "content": "You are a friendly travel advisor for Margie's Travel."}, {"role": "user", "content": "What's a good beach destination in Europe?"}, {"role": "assistant", "content": "..."}]}
```
- Include a **consistent system message** across all examples.
- Use the **same system message at inference time** as used in training — omitting it in training data tends to produce lower-accuracy models.
- Aim for **at least hundreds of examples**; more is generally better.

### Fine-tuning challenges/costs
- Training costs: upfront training cost + ongoing hourly hosting cost for the custom model.
- Data quality: poor/unrepresentative data → overfitting, underfitting, bias.
- Maintenance: retraining needed when data or base models change.
- Hyperparameter experimentation (epochs, batch size, learning rate).
- Model drift: over-specializing can degrade general-purpose performance.

## Compare and combine optimization strategies

| Strategy | Time to implement | Complexity | Cost | Best for |
|---|---|---|---|---|
| Prompt engineering | Low | Low | Low (per-token only) | Tone/format/behavior guidance, quick iteration, instructions+examples |
| RAG | Medium | Medium | Medium (search infra + storage + per-token) | Factual accuracy, domain-specific knowledge, frequently-changing data |
| Fine-tuning | High | High | High (training compute + model hosting + per-token) | Behavioral consistency, style enforcement, shorter prompts, distillation |

**Two optimization dimensions:**
- **Optimize for context** (accuracy) → RAG.
- **Optimize the model** (consistency of style/format) → Fine-tuning.
- Prompt engineering is the foundation supporting both.

### Common combinations
- **Prompt engineering + RAG** — most common combo: PE defines *how* the model acts, RAG supplies *what* it needs to know.
- **Prompt engineering + fine-tuning** — fine-tuned model handles baseline style; system message adds per-conversation/session-specific context (e.g., a seasonal promotion).
- **RAG + fine-tuning** — fine-tuned model = consistent style; RAG = current domain data.
- **All three together** — fine-tuning (style/format) + RAG (accurate domain knowledge) + prompt engineering (conversation-specific instructions/guardrails).

### Decision framework (exam-relevant sequence)
1. Start with prompt engineering (system messages, few-shot, parameter tuning) — evaluate against requirements.
2. Add RAG if accuracy/domain-specific/current data matters.
3. Add fine-tuning if consistency of style/tone/format still isn't met after prompting.
4. Combine as needed — not every app needs all three.

## Exercise (lab, hands-on)
90-minute hands-on lab: fine-tune a language model in Microsoft Foundry. Requires an Azure subscription with administrative access. (Content is an external interactive lab, not further extractable text — the key exam-relevant material is the conceptual units above.)

## Summary
Prompt engineering, RAG, and fine-tuning are **complementary, not competing** strategies addressing different dimensions of model performance:
- Start with prompt engineering to guide behavior.
- Add RAG when factual accuracy needs domain-specific data.
- Add fine-tuning when consistent style/format is required beyond what prompting achieves.

### Further reading (official docs referenced)
- Getting started with customizing an LLM
- Prompt engineering techniques / System message design (advanced prompt engineering)
- Retrieval Augmented Generation in Microsoft Foundry
- Customize a model with fine-tuning / Fine-tuning considerations
- Augment LLMs with RAG or fine-tuning
