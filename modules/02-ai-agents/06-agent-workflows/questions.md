# Practice questions — Build agent-driven workflows using Microsoft Foundry

## Introduction

**Q1.** According to the module introduction, what does Microsoft Foundry's visual workflow builder let you do without writing extensive code?

A. Deploy a new Azure OpenAI resource
B. Define how agents are invoked, how data moves between steps, and how decisions are made based on agent outputs
C. Train a custom small language model from scratch
D. Configure network isolation for a Foundry hub

**Answer:** B — The introduction explicitly states the canvas lets you define agent invocation, data movement, and decision-making without extensive code. A, C, and D are unrelated Foundry infrastructure/model tasks not described in this module.

**Q2.** In the customer support triage scenario used throughout the module, why is workflows-based automation preferred over either fully manual review or full automation?

A. Fully automating responses isn't always safe, and manual review doesn't scale, so workflows combine agents, conditional logic, and human-in-the-loop escalation
B. Manual review is always more accurate than any AI agent
C. Full automation is required by Azure compliance policy for support tickets
D. Workflows eliminate the need for any human oversight entirely

**Answer:** A — The module explicitly frames workflows as balancing scale (vs. manual review) and safety/control (vs. full automation) through human-in-the-loop escalation. D contradicts the stated purpose of human-in-the-loop patterns.

**Q3.** Which of the following are learning objectives explicitly stated for this module? (Choose two.)

A. Use structured agent outputs and conditional logic to route requests
B. Apply human-in-the-loop and escalation patterns to manage low-confidence agent responses
C. Configure Azure Content Understanding analyzers for document extraction
D. Fine-tune a custom model using Azure Machine Learning

**Answer:** A, B — Both are directly listed as learning objectives. C and D belong to other exam domains (information extraction, model training) not covered in this workflows module.

## Understand Workflows

**Q4.** What best describes a Microsoft Foundry workflow?

A. A single agent configured with multiple tools
B. A sequence of connected nodes, where each node performs a specific function such as invoking an agent, evaluating conditions, or managing data
C. A YAML file that defines only the model deployment parameters
D. A Semantic Kernel plugin registered with a kernel instance

**Answer:** B — Workflows are explicitly defined as consisting of connected nodes performing distinct functions (agent invocation, condition evaluation, data management, user communication). A describes a single agent, not a workflow; D describes a Semantic Kernel concept, not a Foundry workflow construct.

**Q5.** According to the module, why do workflows provide an advantage over single-agent solutions for complex or ambiguous tasks?

A. Workflows automatically reduce token costs by 50%
B. Workflows let you combine agents with different responsibilities (classification, decision-making, resolution) into a cohesive, more robust and scalable process
C. Workflows remove the need for any agent to be defined
D. Workflows bypass Foundry's content safety filters for faster responses

**Answer:** B — This is stated verbatim as the key advantage of workflows: coordinating multiple agents with different responsibilities. A, C, and D are not supported by the module content.

**Q6.** What capability allows Foundry workflows to balance automation with oversight when confidence is low or more context is required?

A. Automatic model retraining
B. The ability to pause execution, request human input, or escalate decisions
C. Mandatory manager sign-off configured at the Azure subscription level
D. Switching to a larger foundation model automatically

**Answer:** B — The module states workflows "can pause execution, request human input, or escalate decisions" when confidence is low. This is the human-in-the-loop capability, not automatic model changes.

## Identify Workflow Patterns

**Q7.** A workflow needs to validate input, enrich data, and generate a final response, always executing in the same fixed order. Which workflow pattern best fits this scenario?

A. Group chat workflow
B. Human-in-the-loop workflow
C. Sequential workflow
D. For-each workflow

**Answer:** C — A sequential workflow follows a fixed, step-by-step path where each node passes output to the next, exactly matching the described pipeline. "For-each" is a node type used within a workflow, not a workflow pattern itself.

**Q8.** Which workflow pattern explicitly pauses execution to wait for user approval or input before continuing?

A. Sequential workflow
B. Human-in-the-loop workflow
C. Group chat workflow
D. Invoke agent workflow

**Answer:** B — The human-in-the-loop pattern explicitly asks a question, waits for a response, and resumes based on that input. "Invoke agent workflow" is not one of the three named patterns (Invoke is a node type).

**Q9.** In a group chat workflow, how does control flow differ from a sequential workflow?

A. Control always passes to the End node first
B. Control shifts dynamically between agents based on context, rules, or intermediate results, rather than following a fixed path
C. Control is entirely determined by Power Fx loop counters
D. Control chat workflows do not support multiple agents

**Answer:** B — Group chat workflows enable dynamic orchestration where control shifts between agents based on context/rules/results, contrasted explicitly with the fixed path of sequential workflows.

**Q10.** Which two of the following are named predefined workflow patterns in Microsoft Foundry? (Choose two.)

A. Sequential workflow
B. Group chat workflow
C. Retrieval-augmented workflow
D. Batch inference workflow

**Answer:** A, B — Only "sequential," "human-in-the-loop," and "group chat" are named as predefined patterns in the module. C and D are not workflow pattern names used in this module.

## Create workflows in Microsoft Foundry

**Q11.** In the Microsoft Foundry workflow designer, which node type is used to invoke an AI agent from your project or create a new one?

A. Flow node
B. Invoke node
C. Data transformation node
D. Basic chat node

**Answer:** B — The Invoke node type invokes an AI agent (existing or new) and can return free-text or structured (JSON) output. Flow nodes control execution path; Data transformation nodes manage variables; Basic chat nodes message the user.

**Q12.** Which Flow node type would you use to jump execution to another specific node in the workflow?

A. If/Else
B. For Each
C. Go To
D. Set Variable

**Answer:** C — Go To jumps to another node in the workflow. If/Else branches based on conditions, For Each loops over items, and Set Variable is a Data transformation node, not a Flow node.

**Q13.** Which of the following are Data transformation node types in the Foundry workflow designer? (Choose three.)

A. Set Variable
B. Reset Variable
C. Parse value
D. Go To

**Answer:** A, B, C — Set Variable, Reset Variable, and Parse value are all listed as Data transformation nodes. Go To is a Flow node, not a Data transformation node.

**Q14.** A workflow developer builds several nodes but closes the designer without explicitly saving. What happens to the changes?

A. Foundry automatically saves the workflow every 60 seconds
B. Changes are lost because workflows are not saved automatically — you must save regularly to preserve each version
C. Changes are saved automatically to source control
D. Changes are cached locally and restored on next login

**Answer:** B — The module explicitly warns that "workflows aren't saved automatically" and it's important to save changes regularly. This is a key operational detail likely to appear on the exam.

**Q15.** What is the purpose of the End node in a Foundry workflow?

A. It deletes all variables created during execution
B. It marks the conclusion of a workflow and can optionally return a final result or status
C. It forces the workflow to restart from the Introduction node
D. It triggers a knowledge check for the end user

**Answer:** B — The End node marks the workflow's conclusion and can optionally return a final result or status, per the module content.

## Add Agents to a Workflow

**Q16.** Which node is used to add an agent to a Foundry workflow, and what two options does it provide for selecting the agent?

A. The Flow node; select a model deployment or a fine-tuned checkpoint
B. The Invoke agent node; reference an existing agent from your Foundry project, or create a new agent directly within the workflow designer
C. The Basic chat node; select a language or a locale
D. The Data transformation node; select JSON or XML output

**Answer:** B — The Invoke agent node lets you reference an existing project agent or create a new one directly in the designer, per the module.

**Q17.** Where in the Invoke agent node do you define an agent's structured output schema (e.g., a JSON schema)?

A. In the parameters of the Details tab of the Invoke agent editor
B. In the workflow's global YAML header
C. In the Action settings of the End node
D. In the Power Fx formula bar

**Answer:** A — The module states you define an agent's output schema "in the parameters of the Details tab of the Invoke agent editor."

**Q18.** Where do you configure storing an invoked agent's output into a variable for later use in the workflow?

A. In the Details tab of the Invoke agent editor
B. In the Action settings of the Invoke agent node
C. In the workflow's End node configuration
D. In the module assessment settings

**Answer:** B — Variable storage for agent output is configured in the Action settings of the Invoke agent node, distinct from the Details tab (which is where the response schema is defined).

**Q19.** Why does the module recommend reusing a single categorization agent across multiple workflows rather than duplicating it?

A. Foundry limits projects to one agent total
B. It encourages modular design, making workflows easier to maintain and evolve over time
C. Reused agents automatically gain higher rate limits
D. Only one agent per project can return structured output

**Answer:** B — Agent reuse across workflows is described as encouraging modular design and easier maintenance/evolution, not a technical limit or rate-limit benefit.

**Q20.** Why are structured outputs (e.g., JSON schema responses) from agents particularly useful in a workflow context?

A. They are required for the workflow to save successfully
B. They ensure predictable output shape, which is especially useful when agent responses drive control flow such as routing logic or variable assignment
C. They automatically translate output into every supported locale
D. They disable the need for an End node

**Answer:** B — Structured outputs provide predictable data shape that downstream nodes (If/Else, variable assignment) can reliably consume for routing decisions.

## Apply Power Fx in Workflows

**Q21.** What is Power Fx described as in the context of Microsoft Foundry workflows?

A. A general-purpose compiled language used to write custom agent tools
B. The low-code, Excel-like language that acts as the "glue" of a workflow, used to manipulate data, evaluate conditions, and control execution flow
C. A Semantic Kernel plugin for planning
D. The YAML schema used to define node connections

**Answer:** B — Power Fx is explicitly described as the low-code, Excel-like "glue" language for data manipulation, condition evaluation, and flow control within workflows.

**Q22.** Which Power Fx formula correctly checks whether an agent's confidence score (stored in a local variable) exceeds 0.8?

A. `Local.Confidence == 0.8`
B. `IsBlank(Local.Confidence)`
C. `Local.Confidence > 0.8`
D. `Sum(Local.Confidence, 0.8)`
Also consider: this formula would be used inside which node type to branch execution?

**Answer:** C — `Local.Confidence > 0.8` returns true/false and is used precisely in If/Else nodes to branch execution based on a confidence threshold, per the module's formula reference table.

**Q23.** Which two variable scopes can Power Fx formulas reference in a Foundry workflow? (Choose two.)

A. System variables
B. Local variables
C. Global tenant variables
D. Environment variables

**Answer:** A, B — The module names exactly two scopes: System variables (contextual info about the workflow/conversation) and Local variables (data captured/created during execution). C and D are not terms used in this module.

**Q24.** Which Power Fx formula would you use to apply the `Upper` function to every `Name` field across a table of records?

A. `Upper(Local.ItemList)`
B. `ForAll(Local.ItemList, Upper(Name))`
C. `Sum(Local.ItemList, Name)`
D. `Count(Local.ItemList)`

**Answer:** B — `ForAll` is the formula shown in the module's reference table for looping over items in a list or table and applying a formula (here, `Upper(Name)`) to each.

**Q25.** Which node type in Foundry workflows uses Power Fx to iterate over a collection of items, such as a batch of support tickets, without duplicating nodes?

A. If/Else node
B. For-each node
C. Go To node
D. Invoke agent node

**Answer:** B — For-each nodes use Power Fx to iterate over collections, applying the same actions to each item, avoiding node/logic duplication for lists of inputs.

**Q26.** Which Power Fx function checks whether a table has no records, as opposed to checking whether a single value is empty?

A. `IsBlank`
B. `IsEmpty`
C. `Len`
D. `Count`

**Answer:** B — `IsEmpty(Local.ItemList)` checks whether a table has no records. `IsBlank` checks whether a variable or input value is empty, which is the key distractor distinction here.

## Maintain Workflows in Microsoft Foundry

**Q27.** What happens automatically every time a Foundry workflow is saved?

A. A new, immutable version of the workflow is created
B. The previous version is permanently deleted
C. The workflow is automatically deployed to production
D. All variables are reset to their default values

**Answer:** A — The module states: "Every time a workflow is saved, Foundry automatically creates a new, immutable version." This supports reviewing prior versions, comparing changes, and rolling back — it does not delete history or auto-deploy.

**Q28.** How are the visual canvas and YAML representations of a Foundry workflow related?

A. They are independent; changes to one have no effect on the other
B. YAML is generated once at workflow creation and never updated again
C. Changes made in either the visual canvas or the YAML view are reflected in the other
D. Only the YAML view can be edited; the canvas is read-only

**Answer:** C — The module states both representations stay in sync: "Changes in either view are reflected in the other." A, B, and D all contradict this stated behavior.

**Q29.** Which of the following are listed as best practices for maintaining/refining Foundry workflows? (Choose two.)

A. Regularly reviewing workflows for unused or redundant nodes
B. Leveraging version history to track changes and validate updates
C. Disabling versioning to reduce storage costs
D. Removing all notes before publishing to production

**Answer:** A, B — Both are explicitly listed best practices. C and D are the opposite of what the module recommends (notes and version history are encouraged, not discouraged).

**Q30.** What is the purpose of attaching notes to nodes or sections in the workflow visualizer?

A. Notes trigger automatic escalation to a human reviewer
B. Notes provide context, explain design decisions, or clarify variable usage for future maintainers
C. Notes are required for the workflow to pass validation before saving
D. Notes replace the need for a YAML representation

**Answer:** B — Notes are explicitly for documentation purposes (context, design decisions, variable usage clarification), not a functional/validation requirement.

## Use workflows in code

**Q31.** Which SDK/client do you use to establish a connection to your Microsoft Foundry project before invoking a workflow programmatically?

A. `WorkflowServiceClient`
B. `AIProjectClient`
C. `SemanticKernelClient`
D. `AgentOrchestrationClient`

**Answer:** B — The module states you "establish a connection to your Microsoft Foundry project using the `AIProjectClient`," which handles authentication and provides access to the OpenAI-compatible API.

**Q32.** In the code sample for invoking a workflow, how is the target workflow specified when calling `openai_client.responses.create(...)`?

A. Via a `workflow_id` query parameter on the conversation object
B. Via `extra_body={"agent": {"name": workflow_name, "type": "agent_reference"}}`
C. Via an environment variable read at client initialization
D. Via a separate `invoke_workflow()` method not part of the responses API

**Answer:** B — The exact code sample passes the workflow reference through `extra_body` with `"agent": {"name": workflow_name, "type": "agent_reference"}` on the `responses.create` call.

**Q33.** What does the `input` parameter of `openai_client.responses.create()` represent when invoking a Foundry workflow?

A. It is always required to be a JSON schema matching the agent's structured output
B. It is a prompt or message that drives the workflow's logic, and may be a user question, a ticket description, a data payload, or even an empty string
C. It specifies which node the workflow should start execution from
D. It is the authentication token for the `AIProjectClient`

**Answer:** B — The module explicitly lists these four possible forms of the `input` parameter, including an empty string that "simply starts the workflow without specific input."

**Q34.** Which event type indicates that the workflow finished executing and returned a final response?

A. `response.output_item.done`
B. `response.completed`
C. `workflow.finished`
D. `agent.response.final`

**Answer:** B — `response.completed` is the documented event type for workflow completion with a final response. `response.output_item.done` indicates an individual output item (such as a workflow action) completed — a distinct, narrower event.

**Q35.** How should an application handle a workflow that includes a human-in-the-loop pattern and is currently paused waiting for input?

A. The application must restart the workflow from the beginning
B. The application can send additional messages to the conversation to provide the requested input and resume workflow execution
C. The workflow automatically times out and cannot be resumed
D. The application must switch to a different `AIProjectClient` instance

**Answer:** B — The module states that for human-in-the-loop workflows, "you can send additional messages to the conversation to provide the requested input and resume workflow execution."

**Q36.** According to the module, which of the following are benefits of integrating Foundry workflows into code via the Azure AI Projects SDK? (Choose three.)

A. Embedding AI-driven workflows directly in user-facing web applications
B. Exposing workflow capabilities through REST endpoints in APIs/microservices
C. Automating workflow testing as part of CI/CD pipelines
D. Eliminating the need to design workflows visually in the Foundry portal

**Answer:** A, B, C — All three are explicitly listed benefits (web applications, APIs/microservices, testing/validation in CI/CD). D is incorrect — the module frames code integration as complementary to, not a replacement for, the visual design experience.

## Module Assessment (Knowledge check)

**Q37.** [From the official module assessment] Which type of node in a Foundry workflow is used to invoke an AI agent?

A. Logic node
B. Agent node
C. Data transformation node
D. Basic chat node

**Answer:** B — The module assessment identifies the agent-invoking node as the "Agent node" (referred to as the Invoke node/Invoke agent node in the unit content). Data transformation nodes manage variables, not agent invocation.

**Q38.** [From the official module assessment] Which node type would you use to handle multiple tickets in a workflow without duplicating nodes?

A. If/Else node
B. For-Each node
C. Send message node
D. Go To node

**Answer:** B — For-Each nodes loop over a list of items (e.g., multiple tickets), applying the same actions to each without duplicating logic.

**Q39.** [From the official module assessment] Which of the following best describes how structured agent outputs are used in workflows?

A. They are ignored once generated, since agents always handle routing automatically
B. They provide predictable data that can be stored in variables, evaluated with conditions, and trigger workflow steps
C. They replace the need for loops and If/Else nodes
D. They are only used for logging purposes and never affect execution

**Answer:** B — Structured outputs give predictable data usable in variables, conditions, and control flow — they do not eliminate the need for loops/conditionals (C is wrong) nor are they ignored or logging-only (A, D are wrong).

## Summary

**Q40.** Per the module summary, what role do variables play in a Foundry workflow?

A. They only store the final End node result
B. They capture agent outputs and other data, driving workflow decisions such as routing, escalation, or continuation
C. They are limited to storing Power Fx function definitions
D. They exist only within the Basic chat node

**Answer:** B — The summary states agents generate structured outputs "captured in variables," which drive decisions such as routing, escalation, or continuation — variables are not scoped only to specific nodes.

**Q41.** Which statement best distinguishes Foundry's agent workflow orchestration from code-first orchestration approaches like Microsoft Agent Framework or Semantic Kernel? [general Azure knowledge combined with module content]

A. Foundry workflows can only run a single agent, while Agent Framework supports multiple agents
B. Foundry workflows use a low-code visual canvas with nodes and Power Fx expressions (exportable as YAML), while Agent Framework/Semantic Kernel orchestration is written directly in code (Python/.NET)
C. Foundry workflows do not support human-in-the-loop patterns, unlike Semantic Kernel
D. Agent Framework and Semantic Kernel can only be used with Azure OpenAI, while Foundry workflows support any model

**Answer:** B — This is the key architectural distinction: Foundry workflows are a declarative, node-based/low-code layer (visual canvas + Power Fx + YAML) versus code-first orchestration SDKs. A is false (workflows support multi-agent group chat patterns); C is false (human-in-the-loop is a named Foundry workflow pattern); D is not an established distinction in the module.

**Q42.** Which Microsoft Foundry documentation topic does the module summary point to for further reading on workflows?

A. "Create a workflow" documentation under Microsoft Foundry agents concepts
B. "Deploy a model" documentation
C. "Configure content filters" documentation
D. "Manage quotas" documentation

**Answer:** A — The summary unit links to the Microsoft Foundry "Create a workflow" documentation (azure/ai-foundry/agents/concepts/workflow) as further reading.
