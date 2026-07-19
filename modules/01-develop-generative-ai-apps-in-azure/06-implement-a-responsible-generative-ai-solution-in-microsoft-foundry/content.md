# Implement a responsible generative AI solution in Microsoft Foundry

Source: https://learn.microsoft.com/en-us/training/modules/responsible-ai-studio/

## Learning objectives

By the end of this module, you'll be able to:
- Describe an overall process for responsible generative AI solution development
- Identify and prioritize potential harms relevant to a generative AI solution
- Measure the presence of harms in a generative AI solution
- Mitigate harms in a generative AI solution
- Prepare to deploy and operate a generative AI solution responsibly

## Exam relevance

Maps to **Learning Path 1 — Develop generative AI apps on Microsoft Foundry**. This is the primary source module for:
- **"Plan and manage an Azure AI solution" (25–30%)** → *"Implement responsible AI across generative AI and agentic systems"*: configure safety filters/guardrails/risk detection/content moderation; apply RAI instrumentation (evaluators, safety evaluations); implement auditing; govern agent behavior.

Content filter categories, severity levels, prompt shields, and the Map/Measure/Mitigate/Manage framework are all high-probability exam topics.

## Introduction

Generative AI models are trained on huge internet-scale datasets and can produce content indistinguishable from human-created content — this power brings risk. Microsoft's guidance for responsible generative AI builds on **Microsoft's Responsible AI standard**, adapted for generative-AI-specific considerations.

## The four-stage responsible AI process

Microsoft's practical, actionable process has **four stages**, closely corresponding to the functions in the **NIST AI Risk Management Framework**:

1. **Map** — identify potential harms relevant to your planned solution.
2. **Measure** — measure the presence of these harms in the solution's outputs.
3. **Mitigate** — mitigate harms at multiple layers of the solution, and communicate risks transparently to users.
4. **Manage** — operate the solution responsibly via a defined deployment/operational readiness plan.

(Mnemonic for the exam: **Map → Measure → Mitigate → Manage**.)

## Stage 1: Map potential harms

Four steps:
1. **Identify potential harms**
2. **Prioritize identified harms**
3. **Test and verify** the prioritized harms
4. **Document and share** the verified harms

### 1. Identify potential harms
Depends on the specific services/models used and any fine-tuning/grounding data. Common harm types:
- Offensive, pejorative, or discriminatory content
- Factual inaccuracies
- Content that encourages/supports illegal or unethical behavior

Resources to consult: the **Azure OpenAI Service transparency note**; model-developer documentation (e.g., the OpenAI GPT-4 system card); the **Microsoft Responsible AI Impact Assessment Guide** and its accompanying **Responsible AI Impact Assessment template**.

### 2. Prioritize the harms
Assess **likelihood** × **impact** for each harm, then prioritize the most likely/impactful first. Must factor in intended use *and* potential misuse; inherently somewhat subjective (may involve policy/legal experts). Example: a smart-kitchen copilot might weigh "provides a lethal poison recipe" as higher-impact but lower-frequency than "gives inaccurate cooking times" (higher-frequency, lower per-instance impact) — the team decides overall priority.

### 3. Test and verify
Use **red team testing**: a team of testers deliberately probes the solution to try to produce harmful output, testing under what conditions harms occur (may reveal new, previously unidentified harms). Red teaming is a strategy borrowed from security testing, extended here to responsible AI — it complements existing cybersecurity practices.

### 4. Document and share
Document evidence of harms and share with stakeholders; maintain and update the prioritized harm list as new harms are found.

## Stage 2: Measure potential harms

Goal: create an **initial baseline** quantifying harms produced in given usage scenarios, then track improvement against that baseline as mitigations are applied.

Three-step generalized measurement approach:
1. **Prepare a diverse selection of input prompts** likely to elicit each documented potential harm (e.g., prompts likely to elicit dangerous instructions).
2. **Submit the prompts** to the system and retrieve generated output.
3. **Apply pre-defined criteria** to evaluate/categorize the output by harm level (as simple as harmful/not-harmful, or a defined range of harm levels) — criteria must be strict/consistent.

Document and share measurement results with stakeholders.

### Manual vs. automatic testing
- Start with **manual testing** on a small input set to validate that results are consistent and evaluation criteria are well-defined.
- Then **automate** testing/measurement at larger volume (e.g., using a classification model to auto-evaluate output).
- Even after automating, **periodically perform manual testing** to validate new scenarios and confirm the automated solution still performs as expected.

## Stage 3: Mitigate potential harms

Mitigation uses a **layered approach across four layers**:

1. **Model layer**
2. **Safety system layer**
3. **System message and grounding layer**
4. **User experience layer**

### 1. Model layer
- Select a model appropriate for the intended use — e.g., a simpler/smaller model for narrow classification tasks may carry lower risk of harmful generation than a large general-purpose model like GPT-4.
- **Fine-tune** a foundational model with your own training data so outputs are more relevant/scoped to your scenario (reduces off-topic/harmful drift).

### 2. Safety system layer
Platform-level configurations/capabilities. **Microsoft Foundry guardrails** include:
- **Content filters** — classify content into **four severity levels**: **safe, low, medium, high**, across **five categories of potential harm**: **hate and fairness, sexual, violence, self-harm, and task-adherence**. (Exam-critical: know both the 4 severity levels and the 5 harm categories by name.)
- **Prompt shields** — use abuse-detection algorithms to determine whether the solution is being systematically abused (e.g., a user attempting to subvert/jailbreak the system prompt).

### 3. System message and grounding layer
Focuses on prompt construction submitted to the model:
- System inputs defining behavioral parameters for the model.
- Prompt engineering to add grounding data to inputs, maximizing likelihood of relevant, non-harmful output.
- **RAG** to retrieve contextual data from trusted sources and include it in prompts.

### 4. User experience layer
The application UI/UX and documentation:
- Constrain inputs to specific subjects/types via UI design; apply input/output validation.
- Documentation should be **transparent** about capabilities, limitations, base models, and potential harms not fully addressed by mitigations.

## Stage 4: Manage a responsible generative AI solution

### Complete prerelease reviews
Identify org/industry compliance requirements and ensure relevant teams review the system and documentation. Common review areas:
- Legal
- Privacy
- Security
- Accessibility

### Release and operate
- **Phased delivery plan** — release initially to a restricted user group to gather feedback/identify problems before wider release.
- **Incident response plan** — including estimated response times for unanticipated incidents.
- **Rollback plan** — steps to revert to a previous state if an incident occurs.
- Capability to **immediately block harmful system responses** when discovered.
- Capability to **block specific users, applications, or client IP addresses** in case of misuse.
- User feedback/reporting mechanism — let users flag generated content as **inaccurate, incomplete, harmful, offensive**, or otherwise problematic.
- **Telemetry** tracking for user satisfaction / functional gaps / usability issues — must comply with privacy laws and organizational privacy commitments.

## Exercise (lab, hands-on)
20-minute hands-on lab: deploy an AI model in Microsoft Foundry and observe the effect of **guardrail controls** on responses. Requires an Azure subscription.

## Summary
Practical responsible-AI process for generative AI:
1. Identify potential harms relevant to your solution.
2. Measure the presence of harms in use.
3. Mitigate harmful content generation at multiple levels.
4. Deploy with adequate plans/preparation for responsible operation.

### Further reading
- Overview of Responsible AI practices for Azure OpenAI models
- Microsoft Foundry Discord / Developer Forum
