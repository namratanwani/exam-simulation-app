# Build agent-driven workflows using Microsoft Foundry

Source: https://learn.microsoft.com/en-us/training/modules/build-agent-workflows-microsoft-foundry/

## Learning objectives

By the end of this module, you learn to:

- Explain how nodes, variables, and agent outputs control workflow execution
- Route requests using structured outputs and conditional logic
- Loop over multiple inputs with For-Each nodes
- Use human-in-the-loop and escalation patterns for low-confidence items
- Utilize Power Fx expressions to manipulate data and control flow

Prerequisites: familiarity with deploying and managing AI agents using Microsoft Foundry.

Module facts: 11 units, Beginner level, roles: AI Engineer, Data Scientist, Developer, Solution Architect, Student. Product: Microsoft Foundry.

## Exam relevance

This module maps to **"Implement generative AI and agentic solutions" (30–35%)** in EXAM_SKILLS.md, specifically:

- **Build generative applications by using Foundry** → "Design workflows, tool-augmented flows, and multistep reasoning pipelines" — this entire module is about the Foundry visual workflow designer (nodes, control flow, data transformation) used to build these pipelines.
- **Build agents by using Foundry** → "Implement orchestrated multi-agent solutions" — covered via the group chat workflow pattern and the Invoke agent node, which lets multiple specialized agents collaborate.
- **Build agents by using Foundry** → "Build autonomous or semiautonomous workflows with safeguards and approval flow controls" — covered directly by the human-in-the-loop workflow pattern, escalation on low-confidence agent output, and Basic chat nodes that pause execution for user input.
- **Optimize and operationalize generative AI systems** → "Orchestrate multiple models, flows, or hybrid LLM and rules engines" — Power Fx conditional/loop logic combined with agent nodes is exactly this kind of hybrid LLM + rules-engine orchestration.
- **Build generative applications by using Foundry** → "Integrate generative workflows into applications by using Foundry SDKs and connectors" — covered by the "Use workflows in code" unit (Azure AI Projects SDK / `AIProjectClient`, OpenAI-compatible `responses.create` with `agent_reference`).

It also touches **"Plan and manage an Azure AI solution"** → "Choose the appropriate Foundry services for generative tasks, grounding, vector search, agent workflows, or multimodal processing" (this module is literally about the "agent workflows" Foundry service/capability) and **"Implement responsible AI..."** → "Implement auditing through trace logging, provenance metadata, and approval workflows" / "Govern agent behavior with oversight modes, constraints, and tool-access controls" via workflow versioning and human-in-the-loop escalation.

**Distinguishing note for the exam:** This module covers orchestration using Microsoft Foundry's native, low-code **visual workflow builder** (nodes + Power Fx + YAML), which is distinct from code-first orchestration frameworks covered elsewhere in Learning Path 2:
- **Foundry Agent Service** = the managed runtime that hosts individual agents (model, instructions, tools, threads).
- **Foundry agent *workflows*** (this module) = a declarative, node-based orchestration layer on top of Foundry Agent Service agents — built in the Foundry portal designer, represented as YAML, invoked via the Azure AI Projects SDK / OpenAI-compatible `responses` API using an `agent_reference` of type `"agent_reference"`.
- **Microsoft Agent Framework** and **Semantic Kernel** = code-first orchestration SDKs (Python/.NET) where you write orchestration logic (sequential, concurrent, group chat, handoff patterns) directly in code rather than a visual canvas. Foundry workflows achieve similar patterns (sequential, group chat, human-in-the-loop) but through low-code nodes and Power Fx expressions instead of SDK orchestration classes.
- If an exam question describes a **visual canvas, drag-and-drop nodes, YAML export, or Power Fx formulas**, it is describing **Foundry workflows**. If it describes writing Python/C# orchestration code directly against agent classes, it's Microsoft Agent Framework or Semantic Kernel.

## Introduction

Modern AI solutions often rely on multiple agents working together to analyze inputs, make decisions, and take action. In **Microsoft Foundry**, **agent workflows** orchestrate these interactions using a combination of agents, control flow, and runtime safeguards.

Foundry includes a **visual workflow builder** (canvas) that lets you design and test these systems without writing extensive code. On the canvas you define how agents are invoked, how data moves between steps, and how decisions are made based on agent outputs. You can observe execution paths and inspect intermediate results at runtime.

Example scenario used throughout the module: a developer automating customer support triage at a SaaS company — tickets range from billing disputes to API errors to how-to questions. Manual review doesn't scale; full automation isn't always safe. Workflows combine multiple AI agents, conditional logic, and human-in-the-loop escalation to triage tickets efficiently while maintaining reliability and control.

Module outcomes:
- Explain how workflow nodes, variables, and agent outputs work together to control execution paths.
- Use structured agent outputs and conditional logic to route requests to the appropriate workflow steps.
- Implement loops (For-Each) to process multiple inputs efficiently within a single workflow.
- Apply human-in-the-loop and escalation patterns to manage uncertainty and low-confidence agent responses.
- Utilize Power Fx expressions to manipulate data, evaluate conditions, and control flow within workflows.

## Understand Workflows

Workflows in Microsoft Foundry provide a way to orchestrate AI-driven actions using a **visual, declarative approach**. Instead of writing code, you define a sequence of steps describing what should happen and when; the platform manages execution and state. This suits business processes combining AI reasoning, logic, and user interaction.

A workflow consists of **connected nodes**, where each node performs a specific function:
- Some nodes **invoke agents**.
- Others **evaluate conditions**, **manage data**, or **communicate with users**.

Together these nodes form an execution path determining how requests move through the system.

Key advantages:
- **Coordinate multiple agents.** Single-agent solutions often struggle with complex/ambiguous tasks. Workflows let you combine agents with different responsibilities (classification, decision-making, resolution) into a cohesive process — more robust, scalable automation.
- **Balance automation with oversight.** When confidence is low or more context is needed, workflows can **pause execution, request human input, or escalate decisions**.

(Referenced screenshot: a "group chat workflow" example in the Foundry UI.)

## Identify Workflow Patterns

Microsoft Foundry provides several **predefined workflow patterns**:

1. **Sequential workflow** — a fixed, step-by-step path. Each node executes in order, passing its output to the next step. Good for pipelines/multi-stage processes (e.g., validate input → enrich data → generate final response). Predictable and easy to reason about; a good starting point.

2. **Human-in-the-loop workflow** — introduces pauses where user input or approval is required before the workflow can continue. The workflow explicitly asks a question, waits for a response, then resumes based on that input. Useful for approvals, confirmations, or supplying missing context — balancing automation with oversight.

3. **Group chat workflow** — enables dynamic orchestration across multiple agents. Instead of a fixed path, control shifts between agents based on context, rules, or intermediate results. Useful when multiple specialized agents collaborate on complex requests (e.g., customer support, multi-domain Q&A). Agents can build on each other's outputs and adapt to changing inputs.

**Exam distinction:** Sequential = fixed order/predictable; Human-in-the-loop = pauses for approval/input; Group chat = dynamic control transfer between multiple agents (not a fixed path).

## Create workflows in Microsoft Foundry

Microsoft Foundry provides a **visual designer** to build workflows as a sequence of connected nodes. Each node represents an action (invoke an agent, evaluate logic, transform data); connections define execution flow.

You can start from a **blank canvas** or a **predefined pattern** (e.g., sequential workflow). The designer shows nodes in execution order; you can move nodes, insert steps, and inspect configuration inline.

**Important operational detail:** Workflows are **NOT saved automatically** — you must save changes regularly to preserve each version of your design.

### Main node types

- **Invoke** — Invokes an AI agent from your project, or creates a new one. Agent nodes can return free-text responses or **structured outputs (e.g., JSON)** usable by other nodes. Used for classification, reasoning, recommendations, or any AI-driven task.
- **Flow** — Controls the workflow's execution path, letting it adapt dynamically. Includes:
  - **If/Else** — Branches execution based on conditions.
  - **Go To** — Jumps to another node in the workflow.
  - **For Each** — Loops over a list of items, performing the same actions for each.
- **Data transformation** — Manipulates data and manages variables, ensuring information is correctly passed to subsequent steps. Includes:
  - **Set Variable** — Assigns a value to a variable for later use.
  - **Reset Variable** — Clears or reinitializes a variable.
  - **Parse value** — Extracts specific data from structured outputs or converts values to different formats.
- **Basic chat** — Sends messages to the user or asks questions to collect input. Often paired with variables to capture responses that influence logic or agent decisions later.
- **End** — Marks the conclusion of a workflow. Can optionally return a final result or status.

**Variables** provide shared state across nodes — outputs from one step (agent results, user input) can inform decisions or trigger further actions in later steps.

Workflows execute within a **conversational context**, letting you interact with them through the chat window — useful for observing how inputs move through nodes and validating step behavior before adding complexity.

## Add Agents to a Workflow

Agents are the **core reasoning components** within a Foundry workflow. Adding agents enables AI-driven decision-making, classification, and response generation as part of a larger orchestration. Each agent is configured with a purpose, model, prompt, and set of tools.

You add agents via an **Invoke agent** node, which can:
- Reference an **existing agent** from your Foundry project, OR
- **Create a new agent** directly within the workflow designer.

The **Invoke agent editor** lets you configure: **tools, knowledge bases, memory, and guardrails** for the agent. When invoked, the workflow passes context (user input or previously set variables) to the agent and receives a response usable in subsequent steps.

**Reusability:** Agents can be reused across multiple workflows (modular design) — e.g., one categorization agent invoked by many workflows to classify requests, while different resolution agents handle follow-up actions.

**Structured output:** Agents can be configured to return structured output via a **response format such as a JSON schema**, ensuring predictable output shape — especially useful when agent responses drive control flow (routing logic, variable assignment). You define an agent's **output schema** in the parameters of the **Details tab** of the Invoke agent editor.

**Variable storage:** Once an agent is added, its output can be stored in a variable and referenced throughout the workflow (drives conditional branches, feeds other agents). Configure variable storage in the **Action settings** of the Invoke agent node.

## Apply Power Fx in Workflows

**Power Fx** is the **low-code, Excel-like language** that acts as the "glue" of a workflow. It manipulates data, evaluates conditions, and controls execution flow without complex code. Used wherever decisions are made, variables are set, or loops are applied.

### How formulas work

A Power Fx formula is an expression that evaluates to a value. Formulas reference two variable scopes:
- **System variables** — contextual info about the workflow/conversation (e.g., current activity, last message, user info).
- **Local variables** — data captured/created during workflow execution, usable in subsequent nodes.

Example formulas:
- Convert input to uppercase: `Upper(Local.Input)`
- Check confidence threshold: `Local.Confidence > 0.8`
- Sum a list/column: `Sum(Local.ItemList, Amount)`

### Conditions as decision points

Power Fx expressions are used in **If/Else nodes** to evaluate conditions and branch execution — e.g., checking an agent's confidence score to decide whether to continue automatically or escalate to a human.

### Loops for processing multiple items

**For-each nodes** use Power Fx to iterate over collections, applying the same actions to each item — handles lists of inputs (e.g., multiple support tickets) without duplicating nodes/logic.

### Power Fx formula reference table (verbatim from module)

| Purpose | Formula Example | Notes |
| --- | --- | --- |
| Convert text to uppercase | `Upper(Local.Input)` | Transforms a string to all caps |
| Convert text to lowercase | `Lower(Local.Input)` | Transforms a string to all lowercase |
| Get string length | `Len(Local.Input)` | Returns the number of characters in a string |
| Conditional check | `Local.Confidence > 0.8` | Returns true/false; used in If/Else nodes |
| If/Else logic | `If(Local.Confidence > 0.8, "Proceed", "Escalate")` | Returns one of two values depending on a condition |
| Sum a list of numbers | `Sum([10, 20, 30])` | Adds up numbers in a simple list |
| Sum a column in a table | `Sum(Local.ItemList, Amount)` | Adds up the `Amount` property of each record in a table |
| Count items in a table or list | `Count(Local.ItemList)` | Returns the number of items |
| Check if blank | `IsBlank(Local.Input)` | Returns true if variable or input is empty |
| Check if empty table | `IsEmpty(Local.ItemList)` | Returns true if a table has no records |
| Loop over items | `ForAll(Local.ItemList, Upper(Name))` | Applies a formula to each item in a list or table |
| Concatenate text | `Concatenate(Local.FirstName, " ", Local.LastName)` | Joins multiple strings into one |

Reference: [Power Fx documentation](https://learn.microsoft.com/en-us/power-platform/power-fx/overview).

## Maintain Workflows in Microsoft Foundry

Real-world automation evolves over time; Foundry provides built-in features to manage workflow versions, document changes, and keep visual/YAML representations in sync.

### YAML and visual representations

Foundry workflows can be represented in both a **visual canvas** and **YAML**. The canvas suits conceptual understanding, tracing execution paths, and collaboration. **YAML** provides a textual representation editable for advanced configuration, version tracking, or **source control integration**. Changes in either view are reflected in the other.

### Versioning

Every time a workflow is saved, Foundry **automatically creates a new, immutable version**. This lets you review prior versions, compare changes, or roll back to an earlier workflow if a modification introduces errors. Also supports collaboration by tracking who made changes and why.

### Adding notes for maintainers

The workflow visualizer allows attaching **notes** to nodes or sections — explaining design decisions or variable usage, helping future maintainers understand purpose/logic and reducing errors.

### Best practices for refinement

- Regularly review workflows for unused or redundant nodes.
- Ensure structured agent outputs are consistently handled.
- Document decisions and logic with notes.
- Leverage version history to track changes and validate updates.

## Use workflows in code

After designing/testing a workflow in the Foundry visual designer, you integrate it into applications using the **Azure AI Projects SDK**.

Workflows are created in the **Foundry portal** using the visual designer, which generates the underlying **YAML definition**. Once saved in your project, you invoke a workflow programmatically **by referencing its name**. You can also download the workflow's YAML definition from the portal for inclusion in your codebase.

### Invoke a workflow

Establish a connection to your Foundry project using **`AIProjectClient`**, which handles authentication and provides access to the **OpenAI-compatible API** for executing conversations and invoking workflows. To run an existing workflow: create a conversation, then invoke the workflow by name.

```python
# Reference a workflow created in the Foundry portal
workflow_name = "triage-workflow"

# Create a conversation context for the workflow
conversation = openai_client.conversations.create()

# Execute the workflow, passing input to drive the workflow logic
stream = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent": {"name": workflow_name, "type": "agent_reference"}},
    input="Users can't reset their password from the mobile app.",
    stream=True,
)
```

Key details:
- `input` parameter passes a prompt/message that drives workflow logic. It might be: a user question, a support ticket description, a data payload, or an empty string (just starts the workflow with no specific input).
- The workflow reference is passed via `extra_body={"agent": {"name": workflow_name, "type": "agent_reference"}}` on `openai_client.responses.create(...)` — note the type value is the literal string `"agent_reference"`.
- `stream=True` enables streaming of events.

### Process workflow events

```python
for event in stream:
    if event.type == "response.completed":
        print("Workflow completed:")
        for message in event.response.output:
            if message.content:
                for content_item in message.content:
                    if content_item.type == 'output_text':
                        print(content_item.text)
    if (event.type == "response.output_item.done") and event.item.type == ItemType.WORKFLOW_ACTION:
        print(f"Action '{event.item.action_id}' completed with status: {event.item.status}")
```

Common event types:

| Event Type | Description |
| --- | --- |
| `response.completed` | The workflow finished executing and returned a final response |
| `response.output_item.done` | An individual output item (such as a workflow action) completed |

Notes:
- Monitoring events lets you show real-time progress, capture agent outputs, or trigger external actions based on workflow state.
- Alternatively, you can wait for the entire workflow to complete and process the final response without streaming.
- For workflows with **human-in-the-loop** patterns, your application may need to handle **pauses** where the workflow waits for user input — send additional messages to the conversation to provide the requested input and resume execution.
- `event.item.type == ItemType.WORKFLOW_ACTION` — a specific item type identifying a workflow action event; each has an `action_id` and a `status`.

### Benefits of code integration

| Scenario | Benefit |
| --- | --- |
| Web applications | Embed AI-driven workflows directly in user-facing apps |
| APIs and microservices | Expose workflow capabilities through REST endpoints |
| Batch processing | Invoke workflows programmatically for bulk operations |
| Testing and validation | Automate workflow testing as part of CI/CD pipelines |
| Custom interfaces | Build specialized UIs tailored to specific workflow use cases |

## Exercise - Create an Agent-driven Workflow

Hands-on lab (30 minutes) completed in the Microsoft Foundry portal — practice building an agent-driven workflow. Requires an Azure subscription (free trial with 30-day credits available if you don't have one). Exercise is launched via an external link and is not further described in text content (no additional technical facts beyond what's covered in prior units).

## Module Assessment (Knowledge check)

The official module assessment includes (questions and options, verbatim; correct answers were not shown on the page and are inferred from module content in the Answer lines within questions.md):

1. "Which type of node in a Foundry workflow is used to invoke an AI agent?" — Options: Logic node / **Agent node** (labeled "Invoke" node type in the module content — the module assessment's phrasing uses "Agent node" as the answer choice referring to this) / Data transformation node.
2. "Which node type would you use to handle multiple tickets in a workflow without duplicating nodes?" — Options: If/Else node / **For-Each node** / Send message node.
3. "Which of the following best describes how structured agent outputs are used in workflows?" — Options: "They are ignored once generated, since agents always handle routing automatically" / **"They provide predictable data that can be stored in variables, evaluated with conditions, and trigger workflow steps"** / "They replace the need for loops and If/Else nodes".

## Summary

Key takeaways restated by the module:

- Workflows provide a structured way to orchestrate AI reasoning, logic, and user interaction in Microsoft Foundry.
- Workflows are composed by combining **nodes** — agents, logic (flow), data transformation, and chat — into sequences defining both actions and control flow.
- Agents generate **structured outputs**, captured in **variables**, which drive workflow decisions such as routing, escalation, or continuation.
- **Power Fx** acts as a low-code "glue" language enabling data transformation, condition evaluation, and iteration (loops) over multiple items.
- Variables, conditions, and loops move data through a workflow, creating adaptive, intelligent behavior.
- Workflows are maintained/refined using **versioning**, **notes**, and dual **visual/YAML** representations to remain reliable, understandable, and scalable for enterprise use.

Further reading referenced: Microsoft Foundry ["Create a workflow" documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/workflow).
