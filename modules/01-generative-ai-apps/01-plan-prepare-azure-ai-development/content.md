# Plan and prepare to develop AI solutions on Azure

Source: https://learn.microsoft.com/en-us/training/modules/prepare-azure-ai-development/

## Learning objectives

By the end of this module, you'll be able to:

- Identify common AI capabilities that you can implement in applications
- Describe Microsoft Foundry and considerations for using it
- Describe Foundry Tools and considerations for using them
- Identify appropriate developer tools and SDKs for an AI project
- Describe considerations for responsible AI

Prerequisites: basic software development concepts, basic AI concepts, basic Azure concepts.

Module info: Beginner level, 9 units, tagged AI Engineer / Foundry Tools / Microsoft Foundry.

## Exam relevance

- **Plan and manage an Azure AI solution (25–30%)** → "Choose the appropriate Foundry services for generative AI and agents" — choosing an appropriate model/Foundry Tool for a task; choosing appropriate Foundry services for generative tasks, grounding, vector search, agent workflows, multimodal processing.
- **Plan and manage an Azure AI solution** → "Set up AI solutions in Foundry" — designing Azure infrastructure for AI apps/agents; developer tooling and SDK selection.
- **Plan and manage an Azure AI solution** → "Implement responsible AI across generative AI and agentic systems" — the Responsible AI principles unit directly underpins this skill area (fairness, reliability/safety, privacy/security, inclusiveness, transparency, accountability).

## Introduction

Growth in AI, and generative AI specifically, requires developers to build comprehensive AI solutions combining machine learning models, AI services, prompt engineering, and custom code. Azure offers multiple services for this. Before starting a project, it's important to consider available services, tools, frameworks, and responsible AI practices. This module introduces **Microsoft Foundry**, described as "a comprehensive platform for AI development on Microsoft Azure."

## What is AI?

"Artificial Intelligence" (AI) covers software capabilities that let applications exhibit human-like behavior. Modern AI solutions are built on machine learning **models** that encapsulate semantic relationships found in large quantities of data, enabling applications to interpret input, reason over it, and generate responses/predictions.

Common AI capabilities developers can integrate:

| Capability | Description |
|---|---|
| **Generative AI and agents** | Based on large language models (LLMs) able to generate original responses to natural-language **prompts** (e.g., chat apps, AI-assisted content creation). Generative AI increasingly underlies **agentic AI** solutions, where AI **agents** combine LLMs with focused **instructions** (task responsibilities) and **tools** (to find knowledge and automate tasks). |
| **Natural language processing (NLP)** | Modern LLMs evolved from NLP. NLP uses statistical and semantic models to interpret text in documents, emails, social media, etc. Many NLP tasks are now done by generative LLMs, but specialized **text analysis** still benefits from statistical NLP (term-frequency algorithms) and task-specific models for classification, sentiment analysis, and summarization. |
| **Computer Speech** | Recognize and synthesize speech for natural voice interaction; handles background noise, interruptions, multiple languages/accents. Also used for transcription/analysis of live or recorded speech and text-to-speech for translation/read-aloud. |
| **Computer vision** | Accept, interpret, and process visual input from images, video, live camera streams (e.g., automated checkout identifying products). Generative models are increasingly **multimodal** — can process visual input AND generate visual output (images/video). |
| **Information extraction** | Combines generative AI (language reasoning), NLP (document understanding), and computer vision/speech (media analysis) to extract key info from documents, forms, images, recordings (e.g., expense-claim processing extracting purchase date, line items, totals from a scanned receipt). |

Determining which AI capabilities an app needs helps identify which AI services to provision, configure, and use.

## Microsoft Foundry

Microsoft Foundry is **the** platform for AI development on Azure. You *can* provision individual AI resources and consume them without Foundry, but Foundry's project organization, resource management, and AI development capabilities make it the **recommended** way to build all but the simplest solutions.

Foundry provides two primary interfaces:
- **Microsoft Foundry portal** — web-based visual interface for AI projects.
- **Microsoft Foundry SDK** — build AI solutions programmatically (also used to automate project operations via scripts/CI/CD in DevOps pipelines).

### Microsoft Foundry projects

In Foundry you manage resource connections, data, code, and other elements of an AI solution in a **project**. Each project belongs to a single Foundry **resource** in Azure, which provides compute, data storage, AI tools, and other services. A Foundry resource can support one or more child projects, one of which is designated the **default** project.

Project assets developers manage:
- **Models**: LLM deployments from **Foundry Models** — a comprehensive catalog of models from Microsoft, OpenAI, and other providers. Connect via the project **endpoint** (Foundry-specific APIs/SDKs) or the **Azure OpenAI endpoint** (OpenAI APIs/SDKs).
- **Agents**: Named AI configurations encapsulating an LLM, instructions, and tools — defining an autonomous AI entity that automates tasks and collaborates with users/other agents. Developed/consumed via the **Microsoft Foundry Agent service** through the project endpoint.
- **Tools**: Built-in functionality (web search, code interpreter) or connections to custom/third-party tools via **Model Context Protocol (MCP)** connections. **Foundry Tools** = suite of AI services for common tasks (text analysis, speech recognition/synthesis, translation, content understanding). Foundry Tools are hosted in the Foundry resource associated with the project(s).
- **Knowledge**: Agents use tools to connect to knowledge stores to contextualize prompts. **Foundry IQ** lets you create a single, central MCP-based knowledge connection in a project to simplify integration with multiple knowledge sources.

### Microsoft Foundry portal

In the Foundry portal you can:
- Find, compare, deploy, and test models.
- Create and test agents.
- Create MCP connections to tools and Foundry IQ knowledge sources.
- Explore and test Microsoft Foundry tools.
- Manage resource configuration and user access.
- Find endpoints and keys needed to access assets from client apps.

To automate project operations use the **Microsoft Foundry SDK** — create/manage assets via scripts or automated CI/CD actions in DevOps pipelines.

**Important architecture note**: This module covers the *latest* Foundry project architecture. Older (**classic**) Foundry projects use a **hub-based architecture**. The Foundry portal is also transitioning to a "new" interface — some tasks may not yet be supported there.

## Foundry Tools

While generative AI models/agents are the focus of most modern projects, "off-the-shelf" functionality for common AI tasks is often useful. **Foundry Tools** = a set of out-of-the-box prebuilt APIs and models you integrate into applications — more cost-effective and predictable than relying solely on generative-AI-based agents.

| Tool | Description |
|---|---|
| **Azure Language** | Analyze natural language text: entity extraction, sentiment analysis, summarization. Also supports building conversational language models and question-answering solutions. |
| **Azure Speech** | **Text to speech** and **speech to text** transformation, plus real-time live speech for conversational apps/agents. |
| **Azure Translator** | State-of-the-art language models to translate text between many languages. |
| **Azure Document Intelligence** | Pre-built or custom models to extract fields from complex documents (invoices, receipts, forms). |
| **Azure Content Understanding** | Multi-modal content analysis — extract data from forms/documents, images, videos, and audio streams. |

Usage: create client apps that connect to the tool-specific **endpoint** in your Foundry resource, using the **project authentication key** or **token-based authentication**, then use tool-specific APIs/SDKs. Some tools provide a UI for configuration/testing directly in the Foundry portal.

**Naming history / exam trap**: Azure tools were previously called **Azure AI Services**, and before that **Azure Cognitive Services**. These older names still appear in some APIs/SDKs, and you can still provision some tools as *individual* Azure resources outside a Foundry resource. **For new projects, use the tools provided in a Microsoft Foundry resource** (not standalone Cognitive Services resources).

## Developer tools and SDKs

You can do many tasks directly in the Foundry portal, but developers also need to write, test, and deploy code.

### Development tools and environments
Choose based on languages/SDKs/APIs needed:
- **Microsoft Visual Studio** — favored for Windows/.NET Framework development.
- **Visual Studio Code (VS Code)** — favored for open-source languages/libraries, web development.

Both are suitable for AI development on Azure.

### Foundry Toolkit extension for Visual Studio Code
Simplifies key workflow tasks:
- Browsing/managing project resources (deployed models, agents, connections, vector stores).
- Deploying models from the model catalog.
- Testing models and agents in integrated playgrounds.
- Configuring declarative and hosted agents via a **visual designer and YAML files**.
- Generating integration code to connect agents with applications.

### GitHub and GitHub Copilot
GitHub = source control/DevOps platform. Visual Studio and VS Code both natively integrate with GitHub and **GitHub Copilot** (AI coding assistant).

### Programming languages, APIs, and SDKs
Supported languages include C#, Python, Node, TypeScript, Java, and others. Key APIs/SDKs:
- **Microsoft Foundry SDK** — connect to Foundry projects, access Foundry-specific assets (agents, Foundry IQ knowledge stores).
- **The OpenAI API** — use OpenAI SDKs to build chat apps based on Foundry models that support OpenAI syntax.
- **Foundry Tools SDKs** — AI-service-specific libraries (multiple languages/frameworks) to consume Foundry Tools resources in your subscription. Foundry Tools can also be consumed via **REST APIs** directly.

## Responsible AI

Software engineers must consider the impact of AI-imbued software on users and society, since AI decisions are often based on probabilistic models dependent on training data. The human-like nature of AI builds user trust, which raises the stakes of incorrect predictions or misuse. Microsoft's core responsible AI principles:

1. **Fairness** — AI systems should treat all people fairly, without bias based on gender, ethnicity, etc. (example: a loan-approval model must not disadvantage groups unfairly). Requires reviewing training data representativeness and evaluating predictive performance across population subsections throughout the development lifecycle. Tooling alone is not sufficient.
2. **Reliability and safety** — AI systems must perform reliably and safely (examples: autonomous vehicles, diagnostic/prescription models — unreliability risks human life). Requires rigorous testing/deployment management and appropriate confidence-score thresholds given the probabilistic nature of ML.
3. **Privacy and security** — Models rely on large volumes of data that may include personal details requiring privacy protection; production systems using new data for predictions also need safeguards for data/customer content.
4. **Inclusiveness** — AI should empower and engage everyone, regardless of physical ability, gender, sexual orientation, ethnicity, etc. Optimize by including diverse people in design, development, and testing.
5. **Transparency** — AI systems should be understandable: users should know the system's purpose, how it works, and its limitations (e.g., training data size, influential features, confidence scores). For personal-data-driven systems (e.g., facial recognition), make clear how data is used, retained, and who has access.
6. **Accountability** — People must be accountable for AI systems. Developers who train/validate models and define decision logic are ultimately responsible; work within a governance/organizational framework ensuring responsible and legal standards.

Further reading pointer: microsoft.com/ai/responsible-ai.

## Exercise — Prepare for an AI development project

A hands-on lab (requires an Azure subscription, or a free 30-day-credit signup) that has learners explore the Microsoft Foundry portal directly. No additional conceptual content beyond linking out to the live exercise.

## Summary

The module covered key considerations for planning/preparing AI application development and introduced Microsoft Foundry as the preferred platform for developing AI solutions on Azure. Further reading: the Azure AI solutions page (azure.microsoft.com/solutions/ai).
