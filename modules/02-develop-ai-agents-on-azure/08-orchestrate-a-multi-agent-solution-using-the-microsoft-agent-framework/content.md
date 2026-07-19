# Orchestrate a multi-agent solution using the Microsoft Agent Framework

Source: https://learn.microsoft.com/en-us/training/modules/orchestrate-semantic-kernel-multi-agent-solution/

> **IMPORTANT naming note (as of this content's `ms.date`: 2026-05-29):** This Microsoft Learn module's URL slug still says "orchestrate-semantic-kernel-multi-agent-solution" and its `uid` is `learn.wwl.orchestrate-sk-multi-agent-solution`, but Microsoft has **replaced the module's actual content**. It no longer teaches Semantic Kernel's `AgentGroupChat`/`AgentChat` APIs. It now teaches the **Microsoft Agent Framework SDK** — the successor/unification of Semantic Kernel's agent APIs and AutoGen, released as the current recommended orchestration SDK. Every class name, method name, and pattern name below (`ConcurrentBuilder`, `SequentialBuilder`, `GroupChatBuilder`, `MagenticBuilder`, `WorkflowBuilder`, etc.) is **Microsoft Agent Framework**, not classic Semantic Kernel. If an exam question references older Semantic Kernel-specific orchestration class names (e.g., `AgentGroupChat`), treat those as legacy/deprecated terminology — the current Learn content and (presumably) the current AI-103 exam surface uses Microsoft Agent Framework naming. This distinction is itself high-value exam-relevant knowledge: **know that Microsoft Agent Framework is the current unified multi-agent orchestration SDK**, built to work with agents from multiple sources including **Microsoft Foundry Agent Service**.

## Learning objectives

By the end of this module, you'll be able to:
- Build AI agents using the Microsoft Agent Framework SDK
- Use tools and plugins with your AI agents
- Understand how and when to use different orchestration patterns
- Develop multi-agent solutions

Prerequisites: familiarity with Azure and the Azure portal; an understanding of generative AI.

## Exam relevance

This module maps to **Learning Path 2 ("Develop AI agents on Azure")** and primarily supports the following EXAM_SKILLS.md bullets:

- **Implement generative AI and agentic solutions (30–35%)** → **Build agents by using Foundry**:
  - "Implement orchestrated multi-agent solutions" — this is the core topic of the entire module (concurrent, sequential, handoff, group chat, and magentic orchestration patterns).
  - "Build agents that integrate retrieval, function-calling, and conversation memory" — relevant via the framework's tools/function-integration and `AgentSession` conversation-history concepts.
  - "Define agent roles, goals, conversation-tracking approach, and tool schemas" — relevant via each agent's `instructions`, `name`, and role definition when built with `create_agent`.
- **Implement generative AI and agentic solutions (30–35%)** → **Optimize and operationalize generative AI systems**:
  - "Orchestrate multiple models, flows, or hybrid LLM and rules engines" — directly supported by the workflow/executor/edge model (direct, conditional, switch-case, fan-out, fan-in edges) and by handoff orchestration's rule-based routing.
- **Plan and manage an Azure AI solution (25–30%)** → **Choose the appropriate Foundry services for generative AI and agents**:
  - "Choose appropriate memory, tool, and knowledge integration services for agent solutions" — relevant via the framework's provider-agnostic chat clients (`BaseChatClient`, `AzureOpenAIChatClient`) and built-in tools (Code Interpreter, File Search, Web Search) vs. custom function tools.

## Introduction

AI agents combine generative AI to complete tasks, but a single agent may not scale to complex tasks. A **multi-agent solution** allows agents to collaborate within the same conversation.

**Example scenario (DevOps):** a multi-agent system with four specialized agents:
- **Monitoring Agent** — ingests logs/metrics, detects anomalies via NLP, triggers alerts.
- **Root Cause Analysis Agent** — correlates anomalies with recent system changes using ML models or predefined rules to pinpoint root cause.
- **Automated Deployment Agent** — implements fixes or rolls back changes via CI/CD pipelines and deployment scripts.
- **Reporting Agent** — generates reports summarizing anomalies/root causes/resolutions, notifies stakeholders.

This modular, scalable, intelligent system reduces manual intervention and improves efficiency.

Module outcomes: build AI agents using the Microsoft Agent Framework SDK; use tools and plugins with AI agents; understand orchestration pattern types; develop multi-agent solutions.

## Understand the Microsoft Agent Framework

The **Microsoft Agent Framework** is an **open-source SDK** that enables developers to integrate AI models into applications, with comprehensive support for AI-powered agents working independently or collaborating with other agents.

It helps developers build agents that process user inputs, make decisions, and execute tasks autonomously using LLMs plus traditional programming logic. It provides structured components for AI-driven workflows so agents can interact with users, APIs, and external services.

### Core concepts

- **Agents** — intelligent, AI-driven entities capable of reasoning and executing tasks. They use LLMs, tools, and conversation history to make decisions dynamically and respond to user needs.
- **Agent orchestration** — multiple agents collaborate toward a common goal using different orchestration patterns. The framework supports several orchestration patterns with a **unified interface** for construction and invocation, so you can switch patterns without rewriting agent logic.

### Core features

- **Chat clients** — abstractions for connecting to AI services from different providers under a common interface. Supported providers include **Azure OpenAI, OpenAI, Anthropic, and more**, through the **`BaseChatClient`** abstraction.
- **Tools and function integration** — **Tools** let agents extend capabilities through custom functions and built-in services. Agents can automatically invoke tools to integrate with external APIs, execute code, search files, or access web information. The framework supports **both custom function tools and built-in tools** like **Code Interpreter, File Search, and Web Search**.
- **Conversation management** — agents maintain conversation history across interactions using **`AgentSession`**, tracking previous interactions and adapting responses. The structured message system uses **roles: USER, ASSISTANT, SYSTEM, TOOL** for persistent conversation context.

### Why use it

Robust platform for building intelligent, autonomous, collaborative AI agents. **Can integrate agents from multiple sources, including Microsoft Foundry Agent Service.** Supports multi-agent collaboration and human-agent interaction. Agents can specialize (data collection, analysis, decision-making) and orchestrate sophisticated workflows. Facilitates **human-in-the-loop** processes. **Provider-agnostic design** allows switching AI providers without changing code — from simple chatbots to complex enterprise solutions.

**Distinguishing note:** Microsoft Agent Framework is the *orchestration/development SDK* that can consume agents defined in **Microsoft Foundry Agent Service** (a hosted agent runtime) as one of multiple possible agent sources — the framework itself is not a hosting service; it's provider-agnostic SDK-level orchestration.

## Understand agent orchestration

The Microsoft Agent Framework SDK's agent orchestration framework lets you design, manage, and scale complex multi-agent workflows without manually handling agent-coordination details. Instead of one agent managing everything, combine multiple specialized agents, each with a unique role, to build more robust, adaptive systems.

Orchestrating agents together enables: parallel analyses, multi-stage processing pipelines, and dynamic context-driven handoffs between experts.

### Why multi-agent orchestration matters

Single-agent systems are limited by one set of instructions/prompt. Multi-agent orchestration lets you:
- Assign distinct skills/responsibilities/perspectives to each agent.
- Combine outputs from multiple agents to improve decision-making and accuracy.
- Coordinate workflow steps so each agent's work builds on the last.
- Dynamically route control between agents based on context or rules.

### Workflows in the Microsoft Agent Framework

**Workflows** are structured sequences of steps used to complete a task, including one or more **AI agents** plus other components, to automate complex operations. Workflows give developers control over task execution, enable multi-agent orchestration, and support **checkpointing** to save and resume workflow states.

#### Core components of a workflow

**Executors** — the main workers in a workflow. They receive input messages, perform specific actions, and produce outputs moving the workflow toward its goal. Executors can represent **AI agents** or **custom logic** components. Example: one executor analyzes a travel request; another books the flight/hotel.

**Edges** — define how messages flow between executors (logic and order of execution). Types:
- **Direct Edges** — connect one executor directly to another in sequence. Example: after an agent gathers input, the next executor processes the booking.
- **Conditional Edges** — trigger only when certain conditions are met. Example: if hotel rooms are unavailable, branch to an executor suggesting alternatives.
- **Switch-Case Edges** — route messages to different executors based on predefined conditions. Example: VIP customers routed to a premium-service executor; others follow the standard process.
- **Fan-Out Edges** — send a single message to multiple executors simultaneously. Example: one request sent to several agents — one checking flights, another checking hotels.
- **Fan-In Edges** — combine multiple messages from different executors into one for a final step. Example: after gathering hotel and flight results, a summary executor compiles a single itinerary.

**Events** — built-in events for **observability** and debugging during workflow execution:

| Event Name | Description |
|---|---|
| `WorkflowStartedEvent` | Triggered when workflow execution begins. |
| `WorkflowOutputEvent` | Emitted when the workflow produces an output. |
| `WorkflowErrorEvent` | Occurs when an error is encountered. |
| `ExecutorInvokeEvent` | Fired when an executor starts processing a task. |
| `ExecutorCompleteEvent` | Fired when an executor finishes its work. |
| `RequestInfoEvent` | Logged when an external request is issued. |

### Supported orchestration patterns (five total)

| Pattern | Behavior | Best for | Agents active at once |
|---|---|---|---|
| **Concurrent orchestration** | Broadcast the same task to multiple agents at once; collect results independently. | Parallel analysis, independent subtasks, ensemble decision making. | Many, simultaneously, independent |
| **Sequential orchestration** | Pass output from one agent to the next in a **fixed order**. | Step-by-step workflows, pipelines, progressive refinement. | One at a time, fixed order |
| **Handoff orchestration** | **Dynamically transfer control** between agents based on context or rules. | Escalation, fallback, expert routing. | One at a time, order NOT fixed/predetermined |
| **Group chat orchestration** | Coordinate a **shared conversation** among multiple agents (+ optionally a human), managed by a **chat manager** that chooses who speaks next. | Brainstorming, collaborative problem solving, consensus. | One speaks at a time in shared thread, manager-selected |
| **Magentic orchestration** | **Manager-driven**: plans, delegates, and adapts across specialized agents. | Complex, open-ended problems where the solution path evolves. | Manager dynamically assigns based on evolving plan |

These patterns are designed to be **technology-agnostic** so they can be adapted to any domain.

**Key distinguishing factors (exam-critical):**
- **Sequential vs. Handoff:** both run one agent at a time, but sequential has a **fixed, predetermined order** decided in advance; handoff **dynamically** decides the next agent based on context/rules at runtime, and the number/order of agents isn't known in advance.
- **Group chat vs. Handoff:** group chat keeps **all agents in the same shared conversation thread**, managed by a chat manager choosing who speaks next (agents mostly just contribute to conversation, not directly changing systems); handoff **fully transfers control** from one agent to another (one agent works at a time, more like a relay/transfer than a moderated discussion).
- **Group chat vs. Magentic:** group chat is a **moderated conversation** among peer agents (manager only picks next speaker / decides termination); Magentic orchestration has a **manager that actively plans, delegates subtasks, and builds/maintains a dynamic task ledger** — it's plan-driven, not just turn-selection.
- **Concurrent vs. Sequential:** concurrent = parallel/independent, no shared context needed between agents at run time; sequential = each step depends on and builds on the prior step's output.

### A unified orchestration workflow

Regardless of pattern chosen, the SDK provides one consistent flow:
1. **Define your agents** and describe their capabilities.
2. **Select and create an orchestration** pattern, optionally adding a manager agent if needed.
3. **Optionally configure callbacks or transforms** for custom input/output handling.
4. **Start a runtime** to manage execution.
5. **Invoke the orchestration** with your task.
6. **Retrieve results** in an asynchronous, nonblocking way.

(Note: per the knowledge check, the correct first step is "Define your agents and describe their capabilities" — not "select and create an orchestration pattern" or "start a runtime.")

## Use concurrent orchestration

**Concurrent orchestration** lets multiple agents work on the same task at the same time, each independently; outputs are then gathered and combined. Works well for diverse approaches/solutions — brainstorming, group decision-making, voting.

Agents work on their own and don't share results with each other (though an agent can call other AI agents by running its own orchestration as part of its process). Agents need to know which other agents are available. This pattern lets you call all registered agents every time, or choose which agents run per task.

### When to use
- Tasks that can run at the same time, via a fixed group of agents or dynamic selection.
- Task benefits from different specialized skills/approaches (technical, business, creative) that work independently but contribute to the same problem.
- Common uses: brainstorming, ensemble reasoning (combining reasoning methods), voting/consensus (quorum), speed-sensitive tasks where parallelism cuts wait time.

### When to avoid
- Agents need to build on each other's work / depend on shared context in order.
- Task requires strict sequence or predictable, repeatable results.
- Resource limits (model usage quotas) make parallel runs inefficient/impossible.
- Agents can't reliably coordinate changes to shared data/external systems concurrently.
- No clear way to resolve conflicts/contradictions between agent results.
- Combining results is too complex or lowers overall quality.

### Implementation steps (Microsoft Agent Framework)
1. **Create your chat client** — e.g., `AzureOpenAIChatClient`, with credentials to connect to your AI service provider.
2. **Define your agents** — create agent instances via the chat client's **`create_agent`** method; each agent gets specific instructions and a name defining its role/expertise.
3. **Build the concurrent workflow** — use the **`ConcurrentBuilder`** class. Add agent instances as participants via **`participants()`**, then call **`build()`**.
4. **Run the workflow** — call the workflow's **`run`** method with the task/input; runs all agents concurrently, returns events with results.
5. **Process the results** — extract outputs via **`get_outputs()`**; results contain combined conversations from all agents.
6. **Handle aggregated responses** — each message includes author name and content, so you can identify which agent produced which response.

## Use sequential orchestration

In **sequential orchestration**, agents are arranged in a **pipeline**; each agent processes the task one after another. Output from one agent becomes input for the next. Ideal for document review, data transformation pipelines, multi-stage reasoning. The run order is **fixed and decided beforehand** — agents don't decide what happens next.

### When to use
- Multi-step processes that must happen in a specific order, each step relying on the one before.
- Data workflows where each stage adds something the next stage needs.
- Stages that can't run at the same time and must run one after another.
- Situations needing gradual improvement (draft → review → polish).
- Systems where you understand each agent's performance and can tolerate delays/failures at any single step without stopping the whole process.

### When to avoid
- Stages can run independently/in parallel without hurting quality.
- A single agent could do the whole task effectively.
- Early stages may fail/produce poor output with no way to stop or correct downstream processing.
- Agents need to collaborate dynamically rather than hand off sequentially.
- Workflow needs iteration, backtracking, or dynamic routing based on intermediate results.

### Implementation steps
1. **Create your chat client** — e.g., `AzureOpenAIChatClient`.
2. **Define your agents** — via `create_agent`; each agent has instructions and a name defining its pipeline role.
3. **Build the sequential workflow** — use the **`SequentialBuilder`** class. Add participants via `participants()`, then `build()`.
4. **Run the workflow** — call the workflow's **`run_stream`** method with the task; processes through all agents sequentially, each agent's output becomes the next agent's input.
5. **Process the workflow events** — iterate through events with an async loop; look for **`WorkflowOutputEvent`** instances containing the sequential-processing results.
6. **Extract the final conversation** — collect the final conversation from workflow outputs, containing the complete history of each agent's contribution.

**Note:** Sequential orchestration uses `run_stream` (streaming) whereas Concurrent and Group Chat orchestration (as documented) use `run` + `get_outputs()`. Magentic also uses `run_stream`. Know which method pairs with which pattern for exam purposes.

## Use group chat orchestration

**Group chat orchestration** models a collaborative conversation among multiple AI agents, and optionally a human participant. A central **chat manager** controls the flow, deciding which agent responds next and when to request human input. Useful for simulating meetings, debates, collaborative problem-solving.

Supports interaction styles from free-flowing ideation to formal workflows with defined roles/approval steps. Great for human-in-the-loop setups. Typically, agents in this pattern **don't directly change running systems** — they mainly contribute to the conversation.

### When to use
- Spontaneous or guided collaboration among agents (and possibly humans).
- Iterative maker-checker loops where agents take turns creating and reviewing.
- Real-time human oversight or participation.
- Transparent/auditable conversations (all output collected in a single thread).
- Common scenarios: creative brainstorming, decision-making needing debate/consensus, cross-disciplinary dialogue, quality control/validation with multiple expert perspectives, content workflows separating creation from review.

### When to avoid
- Simple task delegation or straightforward linear pipelines suffice.
- Real-time speed requirements make discussion overhead impractical.
- Hierarchical/deterministic workflows needed without discussion.
- Chat manager can't clearly determine when the task is complete.
- Managing conversation flow becomes too complex with many agents — **recommendation: limit to three or fewer agents for easier control.**

### Maker-checker loops
A common special case: one agent (**the maker**) proposes content/solutions; another (**the checker**) reviews and critiques. The checker sends feedback to the maker, cycle repeats until satisfactory. Requires a turn-based sequence managed by the chat manager.

### Implementation steps
1. **Create your chat client** — e.g., `AzureOpenAIChatClient`.
2. **Define your agents** — via `create_agent`, with instructions/name per role.
3. **Build the group chat workflow** — use the **`GroupChatBuilder`** class. Add participants via `participants()`, then `build()`.
4. **Run the workflow** — call the workflow's **`run`** method; runs agents (per the manager's turn selection), returns events with results.
5. **Process the results** — extract via **`get_outputs()`**.
6. **Handle aggregated responses** — each message includes author name and content.

### Customizing the group chat manager
Create a custom manager by extending the base **`GroupChatManager`** class. Lets you control:
- How conversation results are filtered/summarized.
- How the next agent is selected.
- When to request user input.
- When to terminate the conversation.

### Group chat manager call order (exam-critical — exact sequence per round)
1. **`should_request_user_input`** — checks if human input is needed before the next agent responds.
2. **`should_terminate`** — determines if the conversation should end (e.g., max rounds reached).
3. **`filter_results`** — if ending, summarizes/processes the final conversation.
4. **`select_next_agent`** — if continuing, chooses the next agent to speak.

This order ensures user input and termination conditions are handled **before** advancing the conversation. Override these methods in a custom manager to change behavior.

## Use handoff orchestration

**Handoff orchestration** lets AI agents **transfer control to one another** based on task context or user requests. Each agent can "hand off" the conversation to another agent with the right expertise. Ideal for customer support, expert systems, dynamic delegation scenarios.

Fits scenarios where the best agent isn't known upfront, or task requirements clarify during processing. Unlike parallel patterns, agents work **one at a time**, fully handing off control from one to the next.

### When to use
- Tasks need specialized knowledge/tools, but the number/order of agents can't be determined in advance.
- Expertise requirements emerge dynamically during processing (routing triggered by content analysis).
- Multi-domain problems requiring different specialists working sequentially.
- Clear signals/rules exist for when an agent should transfer control and to whom.

### When to avoid
- Involved agents and their order are known upfront and fixed (→ use sequential instead).
- Task routing is simple and rule-based, not needing dynamic interpretation.
- Poor routing decisions might frustrate users.
- Multiple operations must run at the same time (→ use concurrent instead).
- Difficult to avoid infinite handoff loops or excessive bouncing between agents.

### Implementation (control workflows / switch-case routing)
Handoff orchestration is implemented using **control workflows**: each agent processes the task in sequence, and based on its output, the workflow decides which agent to call next via a **switch-case structure** routing on classification results.

1. **Set up data models and chat client**
   - Create your chat client for connecting to AI services.
   - Define **Pydantic models** for AI agents' structured JSON responses.
   - Create simple data classes for passing information between workflow steps.
   - Configure agents with specific instructions and the **`response_format`** parameter for structured JSON output.
2. **Create specialized executor functions**
   - **Input storage executor** — saves incoming data to shared state, forwards to the classification agent.
   - **Transformation executor** — converts the agent's JSON response into a typed routing object.
   - **Handler executors** — separate executors per classification outcome, with **guard conditions** to verify correct message processing.
3. **Build routing logic**
   - Create factory functions generating condition checkers for each classification value.
   - Design conditions examining incoming messages, returning true for specific classification results.
   - Use conditions with **`Case`** objects in switch-case edge groups.
   - Always include a **Default case** as fallback for unexpected scenarios.
4. **Assemble the workflow**
   - Use **`WorkflowBuilder`** to connect executors with regular edges.
   - Add a switch-case edge group for routing based on classification results.
   - Configure the workflow to follow the first matching case, or fall back to default.
   - Set up a terminal executor to yield the final output.

## Use Magentic orchestration

**Magentic orchestration** is a flexible, general-purpose multi-agent pattern for **complex, open-ended tasks** requiring dynamic collaboration. Uses a dedicated **Magentic manager** to coordinate a team of specialized agents. The manager decides which agent acts next based on evolving context, task progress, and agent capabilities.

The Magentic manager maintains shared context, tracks progress, and adapts the workflow in real time — breaking down complex problems, assigning subtasks, iteratively refining solutions. The process emphasizes **building and documenting the approach as much as delivering the final solution**. A **dynamic task ledger** is built and refined as the workflow progresses, recording goals, subgoals, and execution plans.

### When to use
- Problem is complex/open-ended with no predetermined solution path.
- Input/feedback from multiple specialized agents needed to shape a valid solution.
- System must generate a documented plan of approach for human review.
- Agents have tools that can directly interact with external systems/resources.
- A step-by-step, dynamically built execution plan adds value before running the tasks.

### When to avoid
- Solution path is fixed/deterministic.
- No need to produce a ledger or plan of approach.
- Task is simple enough for a lighter-weight orchestration pattern.
- Speed is the priority (this pattern emphasizes planning over fast execution).
- Frequent stalls or loops without a clear resolution path are expected.

### Implementation steps
1. **Define specialized agents** — e.g., **`ChatAgent`** instances with specific instructions and chat clients; each has a specialized role/capability.
2. **Set up event handling callback** — an async callback handling different event types during orchestration: orchestrator messages, agent streaming updates, agent messages, final results.
3. **Build the Magentic workflow** — use the **`MagenticBuilder`** class. Add agent instances as participants, configure the event callback with **streaming mode**, and set up the **standard manager** with parameters like **max round count** and **stall limits**.
4. **Configure the standard manager** — coordinates agent collaboration using a chat client for planning/progress tracking. Configure parameters: **maximum round count, stall count, reset count** to control orchestration behavior.
5. **Run the workflow** — call **`run_stream`** with the complex task; the workflow dynamically plans, delegates to appropriate agents, coordinates collaboration.
6. **Process workflow events** — async loop; handle event types including **`WorkflowOutputEvent`** (final results).
7. **Extract the final result** — collect final output containing the complete solution developed collaboratively.

## Exercise — Develop a multi-agent solution

Hands-on exercise: build an application using the **Microsoft Agent Framework** that automatically triages and resolves issues in system log files. Using **Azure AI Agents**, you create an **incident manager agent** and a **devops agent** that collaborate to fix issues. (~30 minutes, external lab environment.) Tip given: delete Azure resources created during the exercise once finished.

## Knowledge check (module's own questions, with correct answers as marked by the page)

1. **What's the first step in the Microsoft Agent Framework's unified orchestration workflow?**
   Correct answer: **Define your agents and describe their capabilities** (not "Select and create an orchestration pattern," not "Start a runtime to manage execution").
2. **For brainstorming and collaborative problem solving among multiple agents, which orchestration pattern is most suitable?**
   Correct answer: **Group Chat** (not Magentic, not Sequential).
3. **Which pattern dynamically transfers control between agents based on context or rules?**
   Correct answer: **Handoff** (not Concurrent, not Sequential).

## Summary

This module covered designing and managing multi-agent orchestration workflows using the **Microsoft Agent Framework SDK**. Multi-agent systems offer advantages over single-agent approaches: improved scalability, specialization, and collaborative problem solving. Five orchestration patterns were covered — **concurrent, sequential, handoff, group chat, and magentic** — each with guidance on when/how to use it. The SDK provides a **unified interface** for defining agents, running orchestrations, handling structured data, and retrieving results asynchronously, enabling flexible, reliable, maintainable multi-agent workflows.

Further reading pointer given by Microsoft: **Microsoft Agent Framework SDK documentation** at `/en-us/agent-framework/overview/agent-framework-overview`.
