# Practice questions — Plan and prepare to develop AI solutions on Azure

## What is AI?

**Q1.** A retail company wants an application that automatically identifies which products a customer places in a shopping basket using a live camera feed, without barcode scanning. Which AI capability does this scenario primarily require?

A. Natural language processing
B. Computer vision
C. Information extraction
D. Computer speech

**Answer:** B — Identifying objects from images/video/live camera streams is the definition of computer vision given in the module. Information extraction (C) is a distractor because it combines multiple capabilities (language + vision + speech) to pull structured data out of content like documents, which isn't what's described here.

**Q2.** Which statement correctly distinguishes generative AI from traditional natural language processing (NLP), as described in Microsoft Learn?

A. NLP can only process speech, relying on acoustic models such as Azure Speech's phoneme recognizer for transcription, while generative AI is limited to processing plain text prompts and cannot handle any audio or spoken-language input whatsoever
B. Generative AI is based on LLMs that generate original responses to prompts, while NLP uses statistical/semantic models and is still preferred for tasks like classification, sentiment analysis, and summarization built on term-frequency techniques
C. NLP and generative AI are the same technology, just rebranded under different marketing names by vendors like Azure Cognitive Services and Azure OpenAI, with no meaningful architectural difference between statistical pipelines and transformer-based LLMs
D. Generative AI cannot perform sentiment analysis under any circumstances, because transformer-based LLMs like those deployed through Azure OpenAI lack the statistical term-frequency scoring mechanisms required to classify emotional tone in text

**Answer:** B — The module explicitly states LLMs evolved from NLP, and while generative LLMs can now do many NLP tasks, specialized statistical NLP techniques (term-frequency algorithms, task-specific classification/sentiment/summarization models) remain useful for text analysis. A and C are factually wrong claims about NLP and generative AI being mutually exclusive or identical; D is too absolute — generative AI CAN do sentiment analysis, it's just not the only approach.

**Q3.** An AI agent is described as combining an LLM with "focused instructions" and something else that lets it "find relevant knowledge and automate tasks." What is this third component called?

A. Connectors
B. Tools
C. Endpoints
D. Evaluators

**Answer:** B — The module defines agentic AI as LLMs + instructions (task responsibilities) + tools (used to find relevant knowledge and automate tasks). Connectors and endpoints are Azure/Foundry infrastructure terms, not the agent-composition term used here; evaluators relate to responsible AI/testing, not agent composition.

**Q21.** A customer service system needs to recognize spoken language in a noisy call center environment, handle interruptions from callers, support multiple languages and accents, and also convert written responses into natural-sounding speech. Which AI capability is this?

A. Natural language processing
B. Computer vision
C. Computer Speech
D. Information extraction

**Answer:** C — Computer Speech is described as recognizing and synthesizing speech for natural voice interaction, handling background noise, interruptions, and multiple languages/accents, plus text-to-speech and transcription/analysis of speech.

**Q22.** A finance team wants a solution that scans submitted expense claims (scanned receipts) and automatically extracts the purchase date, line items, and total amount — combining document understanding, language reasoning, and image analysis. Which AI capability best describes this scenario?

A. Computer vision only
B. Information extraction
C. Natural language processing only
D. Computer Speech only

**Answer:** B — Information extraction combines generative AI (language reasoning), NLP (document understanding), and computer vision/speech (media analysis). The module uses this exact expense-claim/scanned-receipt example.

## Microsoft Foundry

**Q4.** In the current (non-classic) Microsoft Foundry project architecture, which statement is correct?

A. A Foundry resource can support only exactly one project, and creating a second project via the portal returns a quota error
B. A Foundry resource can support one or more child projects, one of which is designated the default project
C. Projects exist independently of any Foundry resource and can be provisioned directly via the Azure Resource Manager API
D. Only the Foundry SDK can create projects via the ProjectClient class; the portal only supports viewing existing ones

**Answer:** B — Per the module, "A Foundry resource can support one or more child projects, with one of them being designated the default project." A is wrong (one or more, not exactly one, and no such quota error is described); C is wrong because every project belongs to a single Foundry resource; D is wrong because both the portal and SDK can manage projects.

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

A. To provide a code interpreter tool for agents, implemented as a sandboxed Python execution environment within the Foundry Tools category
B. To create a single, central MCP-based knowledge connection that simplifies integration with multiple knowledge sources
C. To evaluate model fairness and bias using the Foundry Responsible AI dashboard and automated fairness metrics across demographic subgroups
D. To manage user role-based access control across Foundry projects using Microsoft Entra ID role assignments and custom permission scopes

**Answer:** B — Per the module: "you can use Foundry IQ in a project to create a single, central MCP-based knowledge connection" to simplify integration with multiple sources of knowledge. The other options describe unrelated Foundry capabilities (built-in tools, responsible AI evaluation, and access management, respectively).

**Q8.** Which architecture term does Microsoft Learn use to describe OLDER Microsoft Foundry projects, as opposed to the current project architecture covered in this module?

A. Serverless architecture
B. Hub-based architecture
C. Multi-tenant architecture
D. Federated architecture

**Answer:** B — The module's note explicitly says "Older (classic) Foundry projects may use a hub-based architecture," directing readers to separate documentation for Foundry *classic*. This is a common exam trap distinguishing current vs. classic Foundry project structures.

**Q23.** Microsoft Foundry provides two primary interfaces for interacting with AI projects. What are they?

A. The Azure Portal and the Azure CLI with the az ai extension installed
B. The Microsoft Foundry portal and the Microsoft Foundry SDK
C. The Foundry Toolkit extension and GitHub Copilot
D. The Azure OpenAI endpoint and the Foundry Agent service endpoint

**Answer:** B — The module states Foundry provides a web-based visual interface (the Microsoft Foundry portal) and a way to build solutions programmatically (the Microsoft Foundry SDK), the latter also used to automate project operations via scripts or CI/CD.

**Q24.** Within a Foundry project, what does the "Tools" asset category include, according to the module?

A. Only Azure virtual machines used for training
B. Built-in functionality such as web search and code interpreter, plus connections to custom or third-party tools via Model Context Protocol (MCP)
C. Only Foundry IQ knowledge connections
D. Only Azure Kubernetes Service clusters

**Answer:** B — The module describes Tools as "built-in functionality, such as web search and code interpreter, or you can connect to custom or third-party tools by using Model Context Protocol (MCP) connections."

**Q25.** Which of the following tasks can be performed directly in the Microsoft Foundry portal, per the module?

A. Automating asset creation via CI/CD pipelines in Azure DevOps
B. Finding, comparing, deploying, and testing models, plus creating/testing agents and managing user access
C. Writing and compiling C++ device drivers
D. Configuring on-premises Active Directory federation

**Answer:** B — The module lists exactly these portal capabilities (find/compare/deploy/test models; create/test agents; create MCP/Foundry IQ connections; explore/test Foundry Tools; manage configuration/access; find endpoints/keys). Automating operations via CI/CD is specifically attributed to the Foundry SDK, not the portal.

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

**Q26.** A developer needs to extract named entities, perform sentiment analysis, and summarize free-text customer reviews, and also wants to build a question-answering solution. Which Foundry Tool should they use?

A. Azure Translator
B. Azure Language
C. Azure Document Intelligence
D. Azure Content Understanding

**Answer:** B — Azure Language is described as analyzing natural language text (entity extraction, sentiment analysis, summarization) and supporting conversational language models and question-answering solutions.

**Q27.** Which Foundry Tool provides text-to-speech and speech-to-text transformation, including real-time live speech capability for conversational apps and agents?

A. Azure Language
B. Azure Speech
C. Azure Translator
D. Azure Content Understanding

**Answer:** B — Azure Speech is described exactly this way in the module's Foundry Tools table.

**Q28.** Which Foundry Tool is described as using state-of-the-art language models to translate text between many languages?

A. Azure Document Intelligence
B. Azure Language
C. Azure Translator
D. Azure Speech

**Answer:** C — Azure Translator's description in the module.

**Q29.** A media company wants a single Foundry Tool capable of multi-modal content analysis — extracting data from documents, images, video, AND audio streams. Which tool best fits?

A. Azure Document Intelligence
B. Azure Content Understanding
C. Azure Language
D. Azure Speech

**Answer:** B — Azure Content Understanding is described as multi-modal content analysis that extracts data from forms/documents, images, videos, and audio streams — the only tool in the table spanning all these modalities.

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

**Q30.** Which development tool is favored for Windows/.NET Framework development, versus the one favored for open-source languages/libraries and web development?

A. Visual Studio is favored for Windows/.NET; VS Code is favored for open-source/web development
B. VS Code is favored for Windows/.NET; Visual Studio is favored for open-source/web development
C. Both are exclusively for .NET development
D. Neither is suitable for AI development on Azure

**Answer:** A — The module states Visual Studio is "favored for Windows/.NET Framework development" while VS Code is "favored for open-source languages/libraries and web development," and both are noted as suitable for AI development on Azure.

**Q31.** What role does GitHub Copilot play in the AI development workflow described in the module?

A. It is a Foundry Tool for text analysis
B. It is an AI coding assistant that integrates natively with Visual Studio and VS Code
C. It replaces the need for the Foundry SDK
D. It is a responsible AI evaluation framework

**Answer:** B — The module describes GitHub as a source control/DevOps platform and notes both Visual Studio and VS Code natively integrate with GitHub and GitHub Copilot, the AI coding assistant.

**Q32.** Which of the following is explicitly listed among the programming languages supported for AI development on Azure in this module?

A. COBOL
B. Python
C. Fortran
D. Assembly

**Answer:** B — The module lists supported languages including C#, Python, Node, TypeScript, Java, and others.

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

**Q33.** Which responsible AI principle addresses the need for safeguards around personal data used to train models, and around new data used for predictions in production systems?

A. Privacy and security
B. Fairness
C. Inclusiveness
D. Accountability

**Answer:** A — The module states models rely on large volumes of data that may include personal details requiring privacy protection, and production systems using new data for predictions need safeguards for data/customer content — this is the Privacy and security principle.

**Q34.** A design team makes a point of including people with diverse physical abilities, genders, and ethnic backgrounds throughout the design, development, and testing of an AI system, to ensure it empowers and engages everyone. Which principle does this exemplify?

A. Transparency
B. Reliability and safety
C. Inclusiveness
D. Privacy and security

**Answer:** C — Inclusiveness is defined as AI empowering and engaging everyone regardless of physical ability, gender, sexual orientation, ethnicity, etc., optimized by including diverse people in design, development, and testing.

## Scenario-based questions

**Q35.** A team is planning a new generative-AI customer support agent on Azure. They want to (1) use the current, non-classic Foundry project architecture, (2) connect the agent to a knowledge base spanning multiple document repositories through a single MCP-based connection, and (3) allow the agent to run a code interpreter tool. Which combination of Foundry concepts addresses all three requirements?

A. Hub-based project + Foundry IQ + Azure OpenAI endpoint
B. Standard (non-classic) Foundry project + Foundry IQ for knowledge + built-in Tools for code interpreter
C. Classic Foundry project + Azure Cognitive Services + GitHub Copilot
D. Standard Foundry project + Azure Document Intelligence + SSH authentication

**Answer:** B — The current (non-classic) project architecture is required; Foundry IQ provides the single, central MCP-based knowledge connection across sources; built-in Tools include the code interpreter.

**Q36.** A developer is building an invoice-processing pipeline. They need to (a) extract structured fields from scanned invoices, (b) translate extracted text into three languages, and (c) ensure the system is auditable so any incorrect extraction can be traced back to a responsible engineer, per Microsoft's responsible AI principles. Which combination correctly matches tools/principles to needs?

A. Azure Language for extraction, Azure Speech for translation, Fairness for auditability
B. Azure Document Intelligence for extraction, Azure Translator for translation, Accountability for auditability
C. Azure Content Understanding for extraction, Azure Document Intelligence for translation, Transparency for auditability
D. Azure Translator for extraction, Azure Document Intelligence for translation, Inclusiveness for auditability

**Answer:** B — Document Intelligence extracts structured fields from documents; Translator handles multi-language translation; Accountability is the principle assigning responsibility for AI system outcomes to the developers/organization.

**Q37.** A solo developer wants to prototype quickly using VS Code, browse deployed models and vector stores without leaving the editor, use OpenAI-syntax SDK calls for chat completions, and use the Foundry SDK for agent management. Which set of tools should they combine?

A. Visual Studio + Azure CLI only
B. Foundry Toolkit extension for VS Code + OpenAI API (for chat) + Microsoft Foundry SDK (for agents)
C. GitHub Copilot alone
D. Foundry Tools SDK only, with no Foundry SDK

**Answer:** B — The Foundry Toolkit extension provides in-editor resource browsing; the OpenAI API is used for OpenAI-syntax chat calls against Foundry models; the Foundry SDK manages Foundry-specific assets like agents.

**Q38.** An organization migrating from a legacy hub-based Foundry deployment wants to confirm authentication options available to client apps calling Foundry Tools endpoints, and also wants confirmation that standalone Cognitive Services-style resources are still technically possible but discouraged. Which statement is accurate?

A. Only anonymous access is supported now; standalone provisioning was removed
B. Project authentication key or token-based authentication are supported; standalone Azure resource provisioning still works but Microsoft recommends Foundry-resource-hosted tools for new projects
C. Only SSH keys are supported; standalone provisioning is mandatory
D. Authentication is not required for Foundry Tools endpoints

**Answer:** B — Combines the module's two statements: authentication is via project key or token-based auth, and standalone provisioning of individual tools is still possible but not recommended for new projects.

**Q39.** A healthcare startup is building a diagnostic-assistance agent using a Foundry Model. To align with responsible AI, they set confidence-score thresholds and rigorous testing gates before deployment (principle X), and they also conduct bias audits across demographic subgroups in training data (principle Y). Which principles are X and Y respectively?

A. X = Fairness, Y = Reliability and safety
B. X = Reliability and safety, Y = Fairness
C. X = Transparency, Y = Accountability
D. X = Privacy and security, Y = Inclusiveness

**Answer:** B — Confidence-score thresholds and rigorous testing/deployment management map to Reliability and safety; auditing training data and predictive performance across population subsections maps to Fairness.
