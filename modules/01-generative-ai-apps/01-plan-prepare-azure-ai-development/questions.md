# Practice questions — Plan and prepare to develop AI solutions on Azure

## What is AI?

**Q1.** A retail company wants an application that automatically identifies which products a customer places in a shopping basket using a live camera feed, without barcode scanning. Which AI capability does this scenario primarily require?

A. Natural language processing
B. Computer vision
C. Information extraction
D. Computer speech

**Answer:** B — Identifying objects from images/video/live camera streams is the definition of computer vision given in the module. Information extraction (C) is a distractor because it combines multiple capabilities (language + vision + speech) to pull structured data out of content like documents, which isn't what's described here.

**Q2.** Which statement correctly distinguishes generative AI from traditional natural language processing (NLP), as described in Microsoft Learn?

A. NLP can only process speech, while generative AI only processes text
B. Generative AI is based on LLMs that generate original responses to prompts, while NLP uses statistical/semantic models and is still preferred for tasks like classification, sentiment analysis, and summarization built on term-frequency techniques
C. NLP and generative AI are the same technology with different marketing names
D. Generative AI cannot perform sentiment analysis under any circumstances

**Answer:** B — The module explicitly states LLMs evolved from NLP, and while generative LLMs can now do many NLP tasks, specialized statistical NLP techniques (term-frequency algorithms, task-specific classification/sentiment/summarization models) remain useful for text analysis. A and C are factually wrong; D is too absolute — generative AI CAN do sentiment analysis, it's just not the only approach.

**Q3.** An AI agent is described as combining an LLM with "focused instructions" and something else that lets it "find relevant knowledge and automate tasks." What is this third component called?

A. Connectors
B. Tools
C. Endpoints
D. Evaluators

**Answer:** B — The module defines agentic AI as LLMs + instructions (task responsibilities) + tools (used to find relevant knowledge and automate tasks). Connectors and endpoints are Azure/Foundry infrastructure terms, not the agent-composition term used here; evaluators relate to responsible AI/testing, not agent composition.

## Microsoft Foundry

**Q4.** In the current (non-classic) Microsoft Foundry project architecture, which statement is correct?

A. A Foundry resource can support only exactly one project
B. A Foundry resource can support one or more child projects, one of which is designated the default project
C. Projects exist independently of any Foundry resource
D. Only the Foundry SDK can create projects; the portal cannot

**Answer:** B — Per the module, "A Foundry resource can support one or more child projects, with one of them being designated the default project." A is wrong (one or more, not exactly one); C is wrong because every project belongs to a single Foundry resource; D is wrong because both the portal and SDK can manage projects.

**Q5.** Which TWO of the following are listed as assets that developers manage within a Microsoft Foundry project? (Choose 2.)

A. Agents
B. Virtual networks
C. Models
D. Storage accounts

**Answer:** A, C — The module lists four categories of project assets: Models, Agents, Tools, and Knowledge. Virtual networks and storage accounts are underlying Azure infrastructure concerns, not Foundry project-level assets described in this unit.

**Q6.** A developer wants to interact with a deployed LLM using standard OpenAI SDK syntax rather than Foundry-specific SDKs. Which endpoint should they connect to?

A. The Foundry IQ endpoint
B. The Azure OpenAI endpoint
C. The Foundry Agent service endpoint
D. The Model Context Protocol endpoint

**Answer:** B — The module states models can be reached "through the project endpoint (using Foundry-specific APIs and SDKs) and the Azure OpenAI endpoint (using OpenAI APIs and SDKs)." Foundry IQ is for knowledge connections, the Agent service is for agents specifically, and MCP is a tool-connection protocol, not an OpenAI-compatible endpoint.

**Q7.** What is the purpose of Foundry IQ within a Microsoft Foundry project?

A. To provide a code interpreter tool for agents
B. To create a single, central MCP-based knowledge connection that simplifies integration with multiple knowledge sources
C. To evaluate model fairness and bias
D. To manage user role-based access control

**Answer:** B — Per the module: "you can use Foundry IQ in a project to create a single, central MCP-based knowledge connection" to simplify integration with multiple sources of knowledge. The other options describe unrelated Foundry capabilities (built-in tools, responsible AI evaluation, and access management, respectively).

**Q8.** Which architecture term does Microsoft Learn use to describe OLDER Microsoft Foundry projects, as opposed to the current project architecture covered in this module?

A. Serverless architecture
B. Hub-based architecture
C. Multi-tenant architecture
D. Federated architecture

**Answer:** B — The module's note explicitly says "Older (classic) Foundry projects may use a hub-based architecture," directing readers to separate documentation for Foundry *classic*. This is a common exam trap distinguishing current vs. classic Foundry project structures.

## Foundry Tools

**Q9.** A developer needs to extract structured fields (line items, totals, vendor name) from scanned invoices and receipts. Which Foundry Tool is the best fit?

A. Azure Language
B. Azure Document Intelligence
C. Azure Translator
D. Azure Speech

**Answer:** B — Azure Document Intelligence is described as using pre-built or custom models "to extract fields from complex documents such as invoices, receipts, and forms." Azure Language handles free text (entities, sentiment, summarization) rather than structured document field extraction; Translator and Speech are unrelated to document field extraction.

**Q10.** What were "Foundry Tools" (formerly known by an older name) previously called BEFORE that, according to the module's naming-history note? (Choose the correct chronological pair.)

A. Azure Cognitive Services → Azure AI Services → Foundry Tools
B. Azure AI Services → Azure Cognitive Services → Foundry Tools
C. Foundry Tools → Azure AI Services → Azure Cognitive Services
D. Azure Machine Learning → Azure AI Services → Foundry Tools

**Answer:** A — The module states: "Azure tools were previously called Azure AI Services, and prior to that Azure Cognitive Services." So the chronological order (oldest → newest) is Cognitive Services → AI Services → Foundry Tools. This naming lineage is a classic exam trap since all three names may appear in SDK/API artifacts.

**Q11.** Which TWO authentication approaches does the module describe for connecting a client application to a Foundry Tools endpoint? (Choose 2.)

A. Project authentication key
B. Anonymous access
C. Token-based authentication
D. SSH key pairs

**Answer:** A, C — The module states you connect specifying "the project authentication key or using token-based authentication." Anonymous access and SSH keys are not mentioned as valid options for Foundry Tools endpoints.

**Q12.** True or which statement is correct: can individual Foundry Tools (e.g., Azure Language, Azure Speech) still be provisioned as standalone Azure resources outside of a Foundry resource?

A. No, Foundry Tools can only ever be accessed through a Foundry resource
B. Yes, but Microsoft recommends using the tools provided within a Microsoft Foundry resource for new projects
C. No, standalone provisioning was deprecated and removed entirely
D. Yes, but only for Azure Document Intelligence

**Answer:** B — The module notes you "can still provision some tools as individual Azure resources outside of a Foundry resource," but "For new projects, you should use the tools provided in a Microsoft Foundry resource." A and C overstate the restriction; D incorrectly limits it to one tool.

## Developer tools and SDKs

**Q13.** A team wants to use a visual designer and YAML files to configure declarative and hosted agents directly from their code editor, plus browse deployed models, agents, connections, and vector stores. Which tool should they install?

A. GitHub Copilot
B. The Foundry Toolkit extension for Visual Studio Code
C. Azure CLI
D. The Foundry Tools SDK

**Answer:** B — The Foundry Toolkit extension for VS Code is described as supporting exactly these tasks: browsing/managing project resources, deploying models, testing in playgrounds, and "configuring declarative and hosted agents using a visual designer and YAML files." GitHub Copilot is a general AI coding assistant, not a Foundry-specific resource browser.

**Q14.** Which THREE of the following are named in the module as key APIs/SDKs to plan for when building AI solutions on Azure? (Choose 3.)

A. Microsoft Foundry SDK
B. The OpenAI API
C. Foundry Tools SDKs
D. Azure Kubernetes Service SDK

**Answer:** A, B, C — The module lists exactly these three: the Microsoft Foundry SDK (Foundry projects/assets), the OpenAI API (OpenAI-syntax chat apps against Foundry models), and Foundry Tools SDKs (service-specific libraries, also available via REST APIs). AKS SDK is unrelated to this AI development context.

**Q15.** Besides using SDKs, how else can developers programmatically consume Foundry Tools according to the module?

A. Only through the Foundry portal UI
B. Through their REST APIs
C. Only through Azure CLI
D. Foundry Tools cannot be consumed without an SDK

**Answer:** B — The module states "You can also use Foundry Tools through their REST APIs," in addition to tool-specific SDKs.

## Responsible AI

**Q16.** A bank's loan-approval model is found to systematically disadvantage applicants of a certain ethnicity, even though ethnicity was not an explicit input feature. Which responsible AI principle is most directly violated?

A. Transparency
B. Fairness
C. Accountability
D. Inclusiveness

**Answer:** B — Fairness is defined using exactly this loan-approval example: predictions should not incorporate bias based on gender, ethnicity, or other factors causing unfair advantage/disadvantage. Inclusiveness (D) is about empowering all of society in the system's design/benefit, a related but distinct concept from biased predictions.

**Q17.** For an AI system that diagnoses patient symptoms and recommends prescriptions, which responsible AI principle is most emphasized regarding rigorous testing, deployment management, and appropriate confidence-score thresholds?

A. Privacy and security
B. Reliability and safety
C. Fairness
D. Transparency

**Answer:** B — The module uses this exact example (autonomous vehicles, diagnostic/prescription models) under "Reliability and safety," emphasizing rigorous testing/deployment processes and appropriate thresholds for probabilistic confidence scores.

**Q18.** Which responsible AI principle specifically requires that users be told how their personal data (e.g., images used for facial recognition) is used, retained, and who has access to it?

A. Accountability
B. Transparency
C. Privacy and security
D. Inclusiveness

**Answer:** B — This is explicitly the facial-recognition example under "Transparency," which requires users understand a system's purpose, workings, limitations, and how personal data is used/retained/accessed. Privacy and security (C) is a plausible distractor but the module places the "make it clear to the user" disclosure requirement specifically under Transparency, not Privacy and security.

**Q19.** Under which responsible AI principle does the module state that "tooling alone isn't sufficient" and that developers should carefully review training data representativeness and evaluate predictive performance across subsections of the user population?

A. Fairness
B. Reliability and safety
C. Accountability
D. Privacy and security

**Answer:** A — This statement appears verbatim under the Fairness principle in the module.

**Q20.** Which responsible AI principle places ultimate responsibility on the developers who trained/validated models and defined the decision logic, even though the AI system may appear to operate autonomously?

A. Inclusiveness
B. Transparency
C. Accountability
D. Reliability and safety

**Answer:** C — The module states under Accountability: "Although many AI systems seem to operate autonomously, ultimately it's the responsibility of the developers who trained and validated the models... and defined the logic."
