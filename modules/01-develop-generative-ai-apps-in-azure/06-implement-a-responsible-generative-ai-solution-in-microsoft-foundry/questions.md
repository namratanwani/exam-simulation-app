# Practice questions — Implement a responsible generative AI solution in Microsoft Foundry

## Introduction & the four-stage process

**Q1.** What are the four stages of Microsoft's responsible generative AI process, in order?
A. Identify, Test, Deploy, Retire
B. Map, Measure, Mitigate, Manage
C. Plan, Build, Test, Release
D. Assess, Filter, Block, Report
**Answer:** B — Map, Measure, Mitigate, Manage — closely aligned with the NIST AI Risk Management Framework functions.

**Q2.** Which framework do the four stages of Microsoft's responsible generative AI guidance closely correspond to?
A. ISO 27001
B. The NIST AI Risk Management Framework
C. The OWASP Top 10
D. The Azure Well-Architected Framework
**Answer:** B — The module explicitly notes the four stages correspond closely to the NIST AI Risk Management Framework functions.

## Map potential harms

**Q3.** What are the four steps within the "Map potential harms" stage, in order?
A. Identify, Prioritize, Test and verify, Document and share
B. Identify, Mitigate, Measure, Release
C. Prioritize, Identify, Deploy, Monitor
D. Test, Mitigate, Document, Release
**Answer:** A — Identify potential harms → Prioritize identified harms → Test and verify the prioritized harms → Document and share the verified harms.

**Q4.** What testing strategy does the module recommend for verifying whether identified potential harms actually occur in a generative AI solution, and under what conditions?
A. Load testing
B. Red team testing — testers deliberately probe the solution to try to produce harmful results
C. Unit testing of the model's API client only
D. A/B testing of UI layouts
**Answer:** B — Red team testing (borrowed from security testing practice) is the recommended approach; it can also surface previously unidentified harms.

**Q5.** When prioritizing identified harms for a generative AI solution, what two factors should be assessed for each harm?
A. Development cost and time to fix
B. Likelihood of occurrence and resulting level of impact
C. Number of competitors offering similar features
D. Token cost per request
**Answer:** B — Harms are prioritized by assessing likelihood × impact, factoring in both intended use and potential misuse.

**Q6.** Which official Azure OpenAI Service document should you consult to understand known limitations and behavior of the models in your solution when identifying potential harms?
A. The Azure pricing calculator
B. The transparency note
C. The Azure Well-Architected review checklist
D. The SLA document
**Answer:** B — The Azure OpenAI Service transparency note documents known limitations/considerations, alongside model-developer documentation like system cards.

**Q24.** Which of the following is listed among the common harm types to consider when identifying potential harms for a generative AI solution?

A. Offensive, pejorative, or discriminatory content; factual inaccuracies; content that encourages/supports illegal or unethical behavior
B. Slow response times, high latency, poor UI design
C. High cloud costs, vendor lock-in, licensing complexity
D. Overfitting, underfitting, model drift
**Answer:** A — These are the three common harm types the module lists under "Identify potential harms." The other options describe engineering/cost/ML-training concerns, not responsible-AI harm categories.

**Q25.** Besides the Azure OpenAI Service transparency note and model-developer documentation (e.g., a system card), which Microsoft resource specifically provides a structured guide and accompanying template for evaluating potential harms of an AI solution?

A. The Azure Well-Architected Framework
B. The Microsoft Responsible AI Impact Assessment Guide, along with its accompanying Responsible AI Impact Assessment template
C. The Azure Pricing Calculator
D. The NIST Cybersecurity Framework
**Answer:** B — The module lists the Responsible AI Impact Assessment Guide and its accompanying template as resources to consult when identifying potential harms, alongside the transparency note and model-developer documentation.

**Q26.** In the module's smart-kitchen-copilot example, how does the team weigh "the assistant provides a recipe for a lethal poison" against "the assistant gives inaccurate cooking times" when prioritizing harms?

A. Both harms are always weighted identically since they are both "harms"
B. The poison-recipe harm is treated as higher-impact but lower-frequency, while inaccurate cooking times is higher-frequency but lower per-instance impact — the team weighs both dimensions to decide overall priority
C. Only frequency matters; impact is never considered in prioritization
D. The lethal-poison-recipe harm is ignored entirely since it's an edge case
**Answer:** B — This is the module's own illustrative example of the likelihood × impact prioritization trade-off: rare-but-severe harms must be weighed against common-but-minor ones, a deliberately subjective judgment the team must make.

## Measure potential harms

**Q7.** What is the purpose of the initial "baseline" created during the Measure stage?
A. To set the model's default temperature parameter
B. To quantify the harms produced by the solution in given usage scenarios, so improvements can be tracked against it as mitigations are applied
C. To determine the Azure subscription's spending limit
D. To calculate the number of tokens consumed per request
**Answer:** B — The baseline quantifies current harm levels; subsequent iterative changes are measured for improvement against this baseline.

**Q8.** What are the three generalized steps for measuring potential harms in a generative AI solution?
A. Deploy, monitor, alert
B. Prepare diverse input prompts likely to elicit each harm, submit them and retrieve output, apply pre-defined criteria to categorize the output's harm level
C. Fine-tune, evaluate, redeploy
D. Identify, prioritize, document
**Answer:** B — Prepare prompts targeting each documented harm → submit and retrieve output → apply strict, pre-defined criteria to categorize harm level.

**Q9.** What is the recommended sequencing of manual vs. automated testing when measuring harms, and why should manual testing continue even after automation is implemented?
A. Automate first at full scale, then manually test only if automation fails; manual testing is otherwise unnecessary
B. Start with manual testing on a small set to validate consistent results and well-defined criteria, then automate at scale; continue periodic manual testing to validate new scenarios and confirm the automated solution still performs as expected
C. Only manual testing is recommended; automation is discouraged for responsible AI evaluation
D. Automated and manual testing are mutually exclusive approaches that should never be combined
**Answer:** B — Manual testing first validates the approach; automation scales it; periodic manual testing continues afterward as a check on the automated system.

**Q27.** When applying pre-defined criteria to categorize an output's harm level during the Measure stage, what quality must those criteria have, per the module?

A. They can vary from prompt to prompt for flexibility
B. They must be strict and consistent — whether a simple harmful/not-harmful judgment or a defined range of harm levels
C. They should be determined solely by the model being tested, without human input
D. They are optional if automated testing is used
**Answer:** B — The module states the pre-defined criteria used to categorize output "must be strict/consistent," regardless of whether the scale is binary (harmful/not-harmful) or a defined range of harm levels.

## Mitigate potential harms

**Q10.** What are the four layers of the layered mitigation approach for a generative AI solution, in order from the model outward?
A. Model, Safety system, System message and grounding, User experience
B. User experience, System message, Safety system, Model
C. Safety system, Model, User experience, Grounding
D. Model, User experience, System message, Safety system
**Answer:** A — Model → Safety system → System message and grounding → User experience.

**Q11.** In Microsoft Foundry guardrails' content filters, what are the four severity levels used to classify content?
A. Low, medium, high, critical
B. Safe, low, medium, high
C. Pass, warn, block, escalate
D. Green, yellow, orange, red
**Answer:** B — Content filters classify content into four severity levels: safe, low, medium, and high.

**Q12.** In Microsoft Foundry guardrails' content filters, which five categories of potential harm are classified by severity level?
A. Hate and fairness, sexual, violence, self-harm, task-adherence
B. Hate speech, spam, malware, phishing, piracy
C. Bias, toxicity, profanity, misinformation, plagiarism
D. Violence, self-harm, sexual, fraud, copyright infringement
**Answer:** A — The five categories are hate and fairness, sexual, violence, self-harm, and task-adherence.

**Q13.** A user is attempting to systematically subvert an AI application's system prompt to bypass its intended behavior (a jailbreak attempt). Which Microsoft Foundry guardrails capability is specifically designed to detect this kind of abuse?
A. Content filters
B. Prompt shields — use abuse-detection algorithms to determine if the solution is being systematically abused
C. Fine-tuning with DPO
D. Red team testing
**Answer:** B — Prompt shields specifically target abuse/subversion attempts (e.g., prompt injection or jailbreak attempts), distinct from content filters which classify generated content severity.

**Q14.** At the "model layer" of the mitigation approach, what are two valid mitigation techniques?
A. Selecting an appropriately-scoped model for the task, and fine-tuning a foundational model on your own training data
B. Adding a rollback plan and an incident response plan
C. Constraining UI inputs and adding output validation
D. Using RAG to retrieve grounding data
**Answer:** A — Model layer mitigations include choosing a model appropriate to the task's risk/complexity and fine-tuning to scope responses to your scenario. (RAG and grounding belong to the "system message and grounding" layer; rollback/incident plans belong to the "manage" stage; UI constraints belong to the "user experience" layer.)

**Q15.** Which mitigation layer is responsible for techniques like using RAG to retrieve contextual data from trusted sources and including it in prompts?
A. Model layer
B. Safety system layer
C. System message and grounding layer
D. User experience layer
**Answer:** C — The system message and grounding layer covers prompt construction techniques, including applying RAG to ground prompts with trusted contextual data.

**Q16.** Constraining an application's UI to only accept specific subjects/input types, and applying input/output validation, are mitigation techniques at which layer?
A. Model layer
B. Safety system layer
C. System message and grounding layer
D. User experience layer
**Answer:** D — These are user experience layer mitigations, which also include transparent documentation of capabilities/limitations/potential harms.

**Q28.** Per the module, what should an application's documentation be transparent about at the user experience mitigation layer?

A. Only the Azure subscription cost associated with the deployment
B. The system's capabilities, limitations, base models used, and potential harms not fully addressed by other mitigations
C. The internal source code of the underlying model
D. The exact training dataset used to pretrain the base model
**Answer:** B — The module states user experience layer documentation "should be transparent about capabilities, limitations, base models, and potential harms not fully addressed by mitigations."

## Manage a responsible generative AI solution

**Q17.** Before releasing a generative AI solution, which compliance review areas does the module list as common prerelease reviews?
A. Legal, Privacy, Security, Accessibility
B. Marketing, Sales, Finance, HR
C. Performance, Scalability, Cost, Latency
D. UX, QA, DevOps, SRE
**Answer:** A — Legal, Privacy, Security, and Accessibility are the common compliance review areas listed for prerelease review.

**Q18.** What release strategy does the module recommend to gather feedback and identify problems before releasing a generative AI solution to a wide audience?
A. A phased delivery plan — release initially to a restricted group of users
B. A single "big bang" release to all users simultaneously
C. Releasing only after 100% automated test coverage is achieved
D. Releasing with no monitoring, relying solely on user complaints
**Answer:** A — A phased delivery plan allows initial release to a restricted user group, enabling feedback collection and problem identification before wider release.

**Q19.** Which of the following are elements of a responsible operational readiness plan described in the "Manage" stage? (Choose two.)
A. An incident response plan with estimated response times
B. A rollback plan defining steps to revert to a previous state
C. A model temperature tuning schedule
D. A fixed, unchangeable system prompt that is never updated
**Answer:** A, B — The Manage stage calls for an incident response plan and a rollback plan, plus capabilities to block harmful responses/abusive users and telemetry tracking — not temperature tuning schedules or frozen prompts.

**Q20.** When collecting telemetry data to track user satisfaction and identify functional gaps in a deployed generative AI solution, what constraint does the module emphasize?
A. Telemetry should be collected without any restriction to maximize insight
B. Telemetry collected should comply with privacy laws and the organization's own privacy policies/commitments
C. Telemetry is not needed once content filters are configured
D. Telemetry should only be collected from internal employees, never external users
**Answer:** B — The module explicitly notes telemetry collection must comply with privacy laws and organizational privacy commitments.

**Q21.** Users should be able to report generated content using which categories, according to the module's guidance on release/operation feedback mechanisms?
A. Slow, fast, average
B. Inaccurate, incomplete, harmful, offensive, or otherwise problematic
C. Expensive, cheap, free
D. Approved, rejected, pending
**Answer:** B — The module specifically lists these categories for user-reported content issues, enabling ongoing harm identification post-release.

**Q29.** Beyond having a rollback plan and an incident response plan, which TWO operational capabilities does the module list as necessary for responsibly releasing and operating a generative AI solution? (Choose 2.)

A. Capability to immediately block harmful system responses when discovered
B. Capability to block specific users, applications, or client IP addresses in case of misuse
C. Capability to automatically increase temperature during peak load to improve creativity
D. Capability to disable all content filters temporarily to reduce latency
**Answer:** A, B — The module explicitly lists the capability to immediately block harmful system responses when discovered, and the capability to block specific users, applications, or client IP addresses in case of misuse, as part of responsible release/operation. C and D are not mentioned and contradict responsible-AI practice.

## Scenario / synthesis

**Q22.** A developer wants to reduce the risk of a generative AI travel assistant giving unsafe or off-brand answers. They configure Microsoft Foundry content filters to block "high" and "medium" severity content in the "violence" and "self-harm" categories, and separately enable prompt shields. Which mitigation layer(s) are these two actions part of?
A. Model layer
B. Safety system layer (both content filters and prompt shields are Foundry guardrails capabilities at this layer)
C. User experience layer
D. Manage stage
**Answer:** B — Content filters and prompt shields are both part of Microsoft Foundry's guardrails, which operate at the safety system layer.

**Q23.** A team has deployed a generative AI feature and now wants to detect if the model's live performance is drifting toward more harmful outputs than what was measured pre-launch. Which combination of practices from this module supports that ongoing detection?
A. One-time red team testing during initial development only, with no further action needed
B. Establishing a harm-measurement baseline pre-launch, then continuing periodic (manual and automated) measurement plus telemetry/user feedback reporting post-launch to detect drift
C. Relying solely on the model's built-in temperature parameter to prevent drift
D. Skipping the Measure stage entirely since Mitigate stage guardrails are sufficient on their own
**Answer:** B — The Measure stage establishes a baseline for comparison, and the Manage stage's telemetry and user-feedback mechanisms provide ongoing signals post-release — together enabling drift detection over time.

**Q30.** A team is choosing a model for a narrow, low-risk classification feature (categorizing support tickets by department) versus a general-purpose creative-writing assistant. Per the model-layer mitigation guidance, which approach best reduces harm risk for the classification feature?

A. Use the largest general-purpose model available for both features, since bigger is always safer
B. Select a simpler/smaller model scoped to the narrow classification task, since it may carry lower risk of harmful generation than a large general-purpose model, and reserve broader risk controls for the creative-writing assistant
C. Apply prompt shields only, since model choice doesn't affect harm risk
D. Fine-tune the general-purpose model to write poetry, since fine-tuning always eliminates harm risk
**Answer:** B — The module's model-layer guidance states a simpler/smaller model for narrow tasks may carry lower risk of harmful generation than a large general-purpose model like GPT-4, making model selection itself a risk-reduction lever distinct from safety-system controls like prompt shields.

**Q31.** During red-team testing, testers discover a previously undocumented jailbreak technique that bypasses the system prompt. Which sequence of module-defined actions should follow, spanning multiple stages?

A. Ignore it since it wasn't part of the original harm list
B. Document and share the newly found harm (Map stage), measure its occurrence against defined criteria (Measure stage), enable/tune prompt shields and content filters to mitigate it (Mitigate stage, safety system layer), and update the prioritized harm list plus operational plans (Manage stage)
C. Immediately and permanently shut down the entire application with no further analysis
D. Increase the temperature parameter, since higher randomness prevents jailbreaks
**Answer:** B — This traces the newly discovered harm across all four stages: Map explicitly notes red teaming "may reveal new, previously unidentified harms" that must then be documented/shared; Measure quantifies it; Mitigate applies safety-system-layer controls (prompt shields, content filters); Manage keeps the harm list and readiness plans current.

**Q32.** A company is preparing to launch a new generative AI feature. They plan a restricted-audience rollout first, have defined how quickly they'll respond to incidents, and have a way to revert to the previous version if something goes wrong. Which Manage-stage elements does this describe, respectively?

A. Prerelease legal review, content filter configuration, red team testing
B. Phased delivery plan, incident response plan (with estimated response times), rollback plan
C. Telemetry collection, user feedback reporting, prompt shields
D. Map stage prioritization, Measure stage baseline, Mitigate stage grounding
**Answer:** B — These map directly to the three named Manage-stage release/operate elements: a phased delivery plan (restricted initial audience), an incident response plan (with estimated response times), and a rollback plan (steps to revert).

**Q33.** A generative AI assistant passed manual harm testing on a small prompt set during development. Six months post-launch, the team wants ongoing assurance that harmful-output rates haven't crept up as usage patterns evolved. Which combination of this module's practices addresses this?

A. Nothing further is needed once manual testing passes once
B. Continue automated measurement at scale against the original baseline, periodically supplement with manual testing on new scenarios, and use post-launch telemetry/user feedback reporting to catch issues the original test set didn't anticipate
C. Rely exclusively on prompt shields, since they replace the need for ongoing measurement
D. Re-run only the original Map stage harm list without ever re-measuring
**Answer:** B — This combines the Measure stage's guidance (automate at scale against the baseline, but keep performing periodic manual testing to validate new scenarios) with the Manage stage's telemetry and user-feedback reporting mechanisms for post-launch signal.

**Q34.** An application's content filters are configured to flag "medium" and "high" severity content in the "self-harm" category, but a reviewer notes the filters alone won't stop a user who has learned to phrase harmful requests in a way that evades the system prompt's original intent. Which additional Foundry guardrails capability should be layered on, and at which mitigation layer does it operate?

A. Red team testing; Map stage
B. Prompt shields — abuse-detection algorithms that detect systematic attempts to subvert the system prompt; operates at the safety system layer alongside content filters
C. Telemetry; Manage stage
D. RAG; system message and grounding layer
**Answer:** B — Prompt shields are the Foundry guardrails capability specifically designed to detect systematic abuse/subversion of the system prompt (jailbreak-style attacks), and — like content filters — they operate at the safety system layer, the second of the four mitigation layers.
