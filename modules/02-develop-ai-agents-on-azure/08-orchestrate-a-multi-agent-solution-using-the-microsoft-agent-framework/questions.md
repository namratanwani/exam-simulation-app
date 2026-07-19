# Practice questions — Orchestrate a multi-agent solution using the Microsoft Agent Framework

## Introduction

**Q1.** A Learn module URL contains the slug "orchestrate-semantic-kernel-multi-agent-solution," but the page content now teaches a different SDK's class names (`ConcurrentBuilder`, `SequentialBuilder`, `MagenticBuilder`). Which SDK does the current content actually teach?
A. Semantic Kernel `AgentGroupChat`
B. Microsoft Agent Framework
C. AutoGen Core runtime
D. Azure AI Projects SDK
**Answer:** B — The module content was updated to teach the Microsoft Agent Framework SDK (the unified successor covering Semantic Kernel and AutoGen agent orchestration concepts), even though the URL slug still references "semantic-kernel." The class names in the unit content (`ConcurrentBuilder`, `SequentialBuilder`, `GroupChatBuilder`, `MagenticBuilder`, `WorkflowBuilder`) are Microsoft Agent Framework APIs, not classic Semantic Kernel APIs.

**Q2.** In the DevOps example scenario from the introduction, which agent is responsible for correlating anomalies with recent system changes to pinpoint a root cause?
A. Monitoring Agent itself
B. Root Cause Analysis Agent
C. Automated Deployment Agent
D. Reporting Agent itself
**Answer:** B — The Root Cause Analysis Agent correlates anomalies with recent system changes using ML models or predefined rules. The Monitoring Agent only detects anomalies and triggers alerts; it does not perform correlation/root-cause analysis.

**Q3.** What is the primary benefit cited for using a multi-agent solution instead of a single agent, according to the module's introduction?
A. It reduces the number of Azure regions needed for a production deployment
B. It allows agents to collaborate within the same conversation on tasks too large for a single agent
C. It eliminates the need for conversation history to be tracked or persisted at all
D. It removes the requirement for tool/function calling entirely from agents
**Answer:** B — A multi-agent solution allows agents to collaborate within the same conversation when a task is larger than realistic for a single agent. It does not relate to regions, conversation history, or tool calling.

**Q4.** [general Azure knowledge] Which statement about multi-agent systems described in the module is accurate?
A. Multi-agent systems require exactly one Azure region to operate correctly at all times
B. Multi-agent systems assign specialized roles to individual agents that collaborate toward a shared goal
C. Multi-agent systems can only be built using the Azure portal, never with an SDK
D. Multi-agent systems eliminate the need for any orchestration logic whatsoever
**Answer:** B — Each agent (e.g., Monitoring, Root Cause Analysis, Automated Deployment, Reporting) specializes in a task and the agents collaborate. Orchestration logic (patterns) is exactly what the rest of the module covers — it is not eliminated.

## Understand the Microsoft Agent Framework

**Q5.** Which abstraction in the Microsoft Agent Framework provides a common interface for connecting to AI services from different providers, including Azure OpenAI, OpenAI, and Anthropic?
A. `AgentSession`
B. `BaseChatClient`
C. `WorkflowBuilder`
D. `GroupChatManager`
**Answer:** B — Chat clients connect to AI providers under a common interface via the `BaseChatClient` abstraction. `AgentSession` manages conversation history, `WorkflowBuilder` assembles workflows, and `GroupChatManager` controls group chat turn-taking — none provide the multi-provider chat abstraction.

**Q6.** Which class in the Microsoft Agent Framework is used to maintain conversation history across multiple interactions so an agent can track previous interactions and adapt responses?
A. `ConcurrentBuilder`
B. `AgentSession`
C. `SequentialBuilder`
D. `MagenticBuilder`
**Answer:** B — `AgentSession` is the conversation-management class that maintains history across interactions. The `*Builder` classes listed are orchestration-pattern builders, unrelated to session/history management.

**Q7.** Which four roles does the Microsoft Agent Framework's structured message system use for persistent conversation context?
A. ADMIN, MEMBER, GUEST, BOT
B. USER, ASSISTANT, SYSTEM, TOOL
C. SENDER, RECEIVER, MANAGER, WORKER
D. INPUT, OUTPUT, ERROR, DEBUG
**Answer:** B — The structured message system uses roles USER, ASSISTANT, SYSTEM, and TOOL.

**Q8.** According to the module, the Microsoft Agent Framework supports which two categories of tools that agents can invoke? (Choose two.)
A. Custom function tools
B. Built-in tools like Code Interpreter, File Search, and Web Search
C. Azure Resource Manager templates
D. Kubernetes operators
**Answer:** A, B — The framework "supports both custom function tools and built-in tools like Code Interpreter, File Search, and Web Search." ARM templates and Kubernetes operators are not tool categories described in this module.

**Q9.** Per the module, the Microsoft Agent Framework can integrate agents from multiple sources, including which named Azure service?
A. Microsoft Foundry Agent Service
B. Azure Logic Apps workflow connector
C. Azure Functions Premium
D. Azure Bot Service channel
**Answer:** A — The text states the framework "can integrate agents from multiple sources, including Microsoft Foundry Agent Service." The other services are not mentioned in this module's unit content.

**Q10.** What key design characteristic of the Microsoft Agent Framework allows you to switch between different AI providers without changing your application code?
A. Its stateless architecture
B. Its provider-agnostic design
C. Its reliance on a single vendor SDK
D. Its use of only synchronous APIs
**Answer:** B — The module explicitly calls out the "provider-agnostic design" as what allows switching AI providers without code changes.

## Understand agent orchestration

**Q11.** Which Microsoft Agent Framework feature allows a workflow to save and resume its state?
A. Fan-in edges
B. Checkpointing
C. `ExecutorCompleteEvent`
D. `response_format`
**Answer:** B — Workflows "support checkpointing to save and resume workflow states." Fan-in edges combine messages, `ExecutorCompleteEvent` is an observability event, and `response_format` configures structured JSON agent output — none provide save/resume capability.

**Q12.** In a Microsoft Agent Framework workflow, which edge type sends a single message to multiple executors simultaneously?
A. Direct Edge
B. Conditional Edge
C. Fan-Out Edge
D. Fan-In Edge
**Answer:** C — A Fan-Out Edge sends one message to multiple executors at once (e.g., sending a request to both a flight-checking agent and a hotel-checking agent). Fan-In does the reverse (combining multiple results into one), Direct connects two executors in sequence, and Conditional triggers only when a condition is met.

**Q13.** Which workflow event is emitted when the workflow produces an output?
A. `WorkflowStartedEvent`
B. `WorkflowOutputEvent`
C. `ExecutorInvokeEvent`
D. `RequestInfoEvent`
**Answer:** B — `WorkflowOutputEvent` is emitted when the workflow produces output. `WorkflowStartedEvent` fires at execution start, `ExecutorInvokeEvent` fires when an executor starts processing, and `RequestInfoEvent` is logged when an external request is issued.

**Q14.** A workflow needs to route VIP customers to a premium-service executor while routing all other customers to a standard executor, based on a condition evaluated at runtime. Which edge type is designed for this?
A. Fan-Out Edge
B. Direct Edge connector
C. Switch-Case Edge
D. Fan-In Edge connector
**Answer:** C — Switch-Case Edges route messages to different executors based on predefined conditions, exactly matching the VIP vs. standard routing example given in the module.

**Q15.** Which orchestration pattern broadcasts the same task to multiple agents at once and collects their results independently?
A. Sequential orchestration
B. Handoff orchestration
C. Concurrent orchestration
D. Group chat orchestration
**Answer:** C — Concurrent orchestration broadcasts a task to multiple agents simultaneously and collects results independently; useful for parallel analysis, independent subtasks, or ensemble decision making.

**Q16.** Which orchestration pattern uses a manager that plans, delegates, and adapts across specialized agents for complex, open-ended problems where the solution path evolves?
A. Group chat orchestration
B. Magentic orchestration
C. Sequential orchestration
D. Concurrent orchestration
**Answer:** B — Magentic orchestration is the manager-driven approach described for complex, open-ended, evolving problems. Group chat also has a manager, but it only selects the next speaker in a shared conversation rather than actively planning/delegating via a task ledger.

**Q17.** Which two orchestration patterns run agents one at a time rather than in parallel? (Choose two.)
A. Concurrent orchestration
B. Sequential orchestration
C. Handoff orchestration
D. Group chat orchestration (during concurrent broadcast phase)
**Answer:** B, C — Sequential orchestration passes output from one agent to the next in a fixed order (one at a time); handoff orchestration transfers control so agents "work one at a time, fully handing off control." Concurrent runs agents simultaneously, and group chat is a shared conversation managed turn-by-turn but is not one of the two patterns explicitly described as strictly one-at-a-time pipelines in this pairing.

**Q18.** What is the correct first step in the Microsoft Agent Framework's unified orchestration workflow, per the module's knowledge check?
A. Start a runtime to manage execution
B. Select and create an orchestration pattern
C. Define your agents and describe their capabilities
D. Invoke the orchestration with your task
**Answer:** C — The knowledge check explicitly states the first step is "Define your agents and describe their capabilities," followed by selecting/creating the orchestration pattern, then starting a runtime, then invoking, then retrieving results.

**Q57.** What is an "executor" in a Microsoft Agent Framework workflow?
A. A class that only manages billing and cost tracking for the workflow's overall execution lifecycle
B. The main worker in a workflow — it receives input messages, performs a specific action, and produces output moving the workflow toward its goal; it can represent an AI agent or a custom logic component
C. A synonym for the chat manager used specifically inside group chat orchestration's turn-taking logic
D. A deprecated concept that has been entirely replaced by the `WorkflowBuilder` class in newer SDK versions
**Answer:** B — Executors are the main workers in a workflow, receiving input, performing an action (AI agent or custom logic), and producing output — e.g., one executor analyzes a travel request while another books the flight/hotel.

**Q58.** What is the difference between a Direct Edge and a Conditional Edge in a Microsoft Agent Framework workflow?
A. A Direct Edge connects one executor directly to the next in sequence; a Conditional Edge triggers only when certain conditions are met
B. A Direct Edge triggers only under specific conditions; a Conditional Edge always fires unconditionally regardless
C. Both edge types are functionally identical in behavior; "Conditional" is simply an alias name for "Direct"
D. A Direct Edge sends messages to multiple executors at once; a Conditional Edge sends to exactly one
**Answer:** A — Direct Edges connect one executor directly to another in sequence (e.g., after gathering input, the next executor processes the booking); Conditional Edges only trigger when specific conditions are met (e.g., branching to an alternatives executor if hotel rooms are unavailable).

**Q59.** Which workflow event fires specifically when an executor starts processing a task, as distinct from the event marking the whole workflow's start?
A. `WorkflowStartedEvent`
B. `ExecutorInvokeEvent`
C. `ExecutorCompleteEvent`
D. `RequestInfoEvent`
**Answer:** B — `ExecutorInvokeEvent` fires when an individual executor starts processing a task. `WorkflowStartedEvent` marks the start of the overall workflow execution, and `ExecutorCompleteEvent` fires when an executor finishes (not starts).

**Q60.** Put the Microsoft Agent Framework's unified orchestration workflow steps in the correct order: (1) Start a runtime, (2) Define your agents and describe their capabilities, (3) Retrieve results asynchronously, (4) Select and create an orchestration pattern, (5) Invoke the orchestration with your task.
A. 2, 4, 1, 5, 3
B. 4, 2, 1, 5, 3
C. 2, 1, 4, 5, 3
D. 1, 2, 4, 5, 3
**Answer:** A — The documented order is: define your agents and describe their capabilities → select/create an orchestration pattern (optionally adding a manager) → optionally configure callbacks/transforms → start a runtime → invoke the orchestration with your task → retrieve results asynchronously.

## Use concurrent orchestration

**Q19.** Which class is used to build a concurrent orchestration workflow in the Microsoft Agent Framework SDK?
A. `SequentialBuilder`
B. `ConcurrentBuilder`
C. `GroupChatBuilder`
D. `MagenticBuilder`
**Answer:** B — `ConcurrentBuilder` creates a workflow that runs multiple agents in parallel; agents are added via `participants()` and finalized via `build()`.

**Q20.** After running a concurrent orchestration workflow, which method is used to extract the outputs containing the combined conversations from all agents?
A. `run_stream()`
B. `get_outputs()`
C. `should_terminate()`
D. `filter_results()`
**Answer:** B — `get_outputs()` extracts the outputs from the workflow events after calling `run()`. `run_stream` is used by other patterns (sequential, Magentic); `should_terminate` and `filter_results` are group chat manager methods.

**Q21.** Which scenario is explicitly listed as a reason to AVOID concurrent orchestration?
A. The task benefits from diverse specialized approaches solving the same problem
B. Agents need to build on each other's work or depend on shared context in a specific order
C. Speed matters and running agents in parallel would cut down wait time
D. You want ensemble reasoning or voting/consensus (quorum) decisions
**Answer:** B — Concurrent orchestration should be avoided when agents need to build on each other's work or depend on shared, ordered context — that scenario calls for sequential orchestration instead. The other three options are explicitly listed as reasons TO USE concurrent orchestration.

**Q22.** In the concurrent orchestration implementation steps, which method on the chat client is used to create each agent instance?
A. `create_agent`
B. `new_agent`
C. `spawn_agent`
D. `register_agent`
**Answer:** A — Agent instances are created using the chat client's `create_agent` method, with specific instructions and a name defining the agent's role.

**Q23.** True statement about how concurrent orchestration handles agent-to-agent communication:
A. Agents directly share intermediate results with each other in real time by default during execution
B. Agents work on their own and don't share results with each other, though an agent can call other agents by running its own orchestration
C. Agents must use handoff orchestration internally in order to communicate with one another during a run
D. Concurrent orchestration requires a dedicated chat manager to mediate all agent-to-agent communication
**Answer:** B — Per the module, "Agents work on their own and don't share results with each other. However, an agent can call other AI agents by running its own orchestration as part of its process." A chat manager is a group chat concept, not required for concurrent orchestration.

**Q24.** Which resource constraint is explicitly called out as a reason concurrent orchestration might be impractical?
A. Insufficient Azure region availability for the deployed agents
B. Model usage quotas making parallel runs inefficient or impossible
C. Lack of support for the `create_agent` method on the chat client
D. Inability to define agent `instructions` for each participant
**Answer:** B — The module lists "Resource limits, like model usage quotas, make running agents in parallel inefficient or impossible" as a reason to avoid concurrent orchestration.

## Use sequential orchestration

**Q25.** Which class builds a sequential orchestration workflow that executes agents one after another?
A. `ConcurrentBuilder`
B. `SequentialBuilder`
C. `HandoffBuilder`
D. `PipelineBuilder`
**Answer:** B — `SequentialBuilder` creates a workflow executing agents one after another; note there is no `HandoffBuilder` or `PipelineBuilder` class documented in this module (handoff orchestration instead uses `WorkflowBuilder` with switch-case edges).

**Q26.** Which method is called on a sequential orchestration workflow to run the task, as distinct from the `run()` method used by concurrent orchestration?
A. `run_stream`
B. `execute_async`
C. `invoke_pipeline`
D. `start_sequence`
**Answer:** A — Sequential orchestration calls the workflow's `run_stream` method. Concurrent and group chat orchestration use `run()` followed by `get_outputs()`, while sequential (and Magentic) use `run_stream` with an async loop looking for `WorkflowOutputEvent`.

**Q27.** In sequential orchestration, how is the order in which agents execute determined?
A. Dynamically, based on the content of each agent's output
B. Fixed and decided beforehand; agents don't decide what happens next
C. Randomly selected at runtime by an assigned chat manager
D. Determined by which agent has the lowest token usage
**Answer:** B — "The order in which agents run is fixed and decided beforehand, and agents don't decide what happens next." This is the key distinction from handoff orchestration, where routing is dynamic.

**Q28.** Which scenario is listed as a reason to AVOID sequential orchestration?
A. Data workflows where each stage adds something the next stage needs
B. The workflow requires iteration, backtracking, or dynamic routing based on intermediate results
C. Tasks requiring gradual improvement like drafting, reviewing, and polishing
D. Processes made up of steps that must always happen in a specific, fixed order
**Answer:** B — Needing iteration, backtracking, or dynamic routing is explicitly listed as a reason to avoid sequential orchestration (favor handoff or group chat instead). The other options are reasons TO USE sequential orchestration.

**Q29.** A pipeline requires document review, then data transformation, then a final polishing pass, always in that exact order. Which orchestration pattern is the best fit?
A. Concurrent orchestration
B. Sequential orchestration
C. Handoff orchestration
D. Magentic orchestration
**Answer:** B — A fixed, predetermined step order where each step's output feeds the next is the defining case for sequential orchestration, as opposed to handoff (dynamic, unknown order) or concurrent (parallel, independent).

**Q30.** After calling `run_stream` in a sequential orchestration workflow, what should you iterate through to find the results?
A. `WorkflowErrorEvent` instances only, ignoring all other event types
B. `WorkflowOutputEvent` instances, using an async loop
C. Only the last agent's `instructions` attribute
D. The `ConcurrentBuilder` participant list
**Answer:** B — You iterate through workflow events using an async loop and look for `WorkflowOutputEvent` instances, which contain the results from the sequential processing.

## Use group chat orchestration

**Q31.** Which class do you extend to create a custom group chat manager in the Microsoft Agent Framework?
A. `BaseChatClient`
B. `GroupChatManager`
C. `AgentSession`
D. `ConcurrentBuilder`
**Answer:** B — You create a custom manager by extending the base `GroupChatManager` class, overriding methods like `select_next_agent` and `should_terminate`.

**Q32.** What is the correct call order the group chat manager follows during each round of conversation?
A. select_next_agent → should_terminate → should_request_user_input → filter_results
B. should_request_user_input → should_terminate → filter_results → select_next_agent
C. should_terminate → filter_results → should_request_user_input → select_next_agent
D. filter_results → select_next_agent → should_terminate → should_request_user_input
**Answer:** B — The exact documented order is: `should_request_user_input`, then `should_terminate`, then (if ending) `filter_results`, then (if continuing) `select_next_agent`. This ensures user input and termination are handled before advancing the conversation.

**Q33.** What is the recommended maximum number of agents for a group chat orchestration to keep conversation flow manageable?
A. Ten or fewer
B. Three or fewer
C. Exactly five
D. There is no practical limit
**Answer:** B — The module states you should "limit to three or fewer" agents in group chat orchestration for easier control, since managing conversation flow becomes too complex with many agents.

**Q34.** In a "maker-checker" loop implemented via group chat orchestration, what is the role of the "checker" agent?
A. It proposes the initial content or solution for the checker agent to subsequently review and critique
B. It reviews and critiques the maker's output, sending feedback back to the maker until the result is satisfactory
C. It selects which agent speaks next in the conversation round, acting as the chat manager itself
D. It terminates the conversation automatically after exactly one round regardless of the result quality
**Answer:** B — The checker reviews and critiques content proposed by the maker; the cycle repeats until the result is satisfactory. The maker (not the checker) proposes content; agent-selection and termination are chat-manager responsibilities, not the checker's role.

**Q35.** Which class is used to build a group chat orchestration workflow?
A. `GroupChatBuilder`
B. `ChatManagerBuilder`
C. `ConversationBuilder`
D. `MagenticBuilder`
**Answer:** A — `GroupChatBuilder` creates the workflow; agents are added as participants via `participants()` then finalized with `build()`.

**Q36.** According to the module, in group chat orchestration, do agents typically directly modify running systems?
A. Yes, agents primarily execute changes to external systems directly during the conversation
B. No — agents typically don't directly change running systems; they mainly contribute to the conversation
C. Only the chat manager can modify systems directly, never the individual agents
D. This behavior is determined exclusively by the `response_format` parameter on each agent
**Answer:** B — The module states: "Typically, agents in this pattern don't directly change running systems—they mainly contribute to the conversation." This distinguishes group chat from patterns like handoff, where an agent in control might invoke tools that act on external systems.

**Q37.** Which scenario is explicitly listed as a reason to AVOID group chat orchestration?
A. Real-time human oversight or participation is needed
B. The chat manager can't clearly determine when the task is complete
C. Iterative maker-checker loops are useful for the task
D. The task benefits from cross-disciplinary dialogue
**Answer:** B — "The chat manager can't clearly determine when the task is complete" is explicitly listed as a reason to avoid group chat orchestration. The other three are reasons TO USE it.

## Use handoff orchestration

**Q38.** Handoff orchestration routing logic is typically implemented using which structure in the Microsoft Agent Framework?
A. Fan-out edges only, broadcasting to every possible specialist simultaneously
B. A switch-case structure that routes tasks based on classification results
C. A chat manager selecting the next speaker based on conversation context
D. A fixed, hardcoded sequence of agent calls determined at design time
**Answer:** B — "This routing is done using a switch-case structure that routes the task to different agents based on classification results," built with `WorkflowBuilder`, `Case` objects, and switch-case edge groups.

**Q39.** Which parameter is configured on an agent to enable structured JSON output used for handoff classification?
A. `temperature`
B. `response_format`
C. `max_tokens`
D. `top_p` sampling parameter
**Answer:** B — Agents are configured with specific instructions and the `response_format` parameter for structured JSON output, which is parsed by Pydantic models into a typed routing object.

**Q40.** In a handoff orchestration switch-case routing setup, what is the purpose of always including a Default case?
A. To improve model latency during classification requests
B. To act as a fallback for unexpected/unclassified scenarios
C. To force all incoming messages to route to the first agent
D. To disable the classification agent once routing begins
**Answer:** B — A Default case is always included as a fallback for unexpected scenarios not matched by any specific Case condition.

**Q41.** Which two orchestration patterns are most clearly distinguished by whether the sequence/number of agents is known in advance? (Choose two.)
A. Sequential orchestration (order fixed and known in advance)
B. Handoff orchestration (order/number of agents not necessarily known in advance)
C. Concurrent orchestration
D. Magentic orchestration
**Answer:** A, B — Sequential orchestration has agents in a fixed order decided beforehand, while handoff orchestration is used precisely when "the number or order of agents can't be determined in advance." This is the key exam distinction between the two "one agent at a time" patterns.

**Q42.** Which scenario is explicitly listed as a reason to AVOID handoff orchestration?
A. Expertise requirements emerge dynamically during processing
B. The involved agents and their order are known upfront and fixed
C. Multiple-domain problems require different specialists working sequentially
D. You can define clear signals or rules for when to transfer control
**Answer:** B — If agents and order are known/fixed upfront, sequential orchestration is more appropriate; this is explicitly listed as a reason to avoid handoff. Options A, C, and D are reasons TO USE handoff orchestration.

**Q43.** Which executor role in a handoff orchestration workflow is responsible for saving incoming data to shared state and forwarding it to the classification agent?
A. Transformation executor
B. Handler executor
C. Input storage executor
D. Terminal executor
**Answer:** C — The input storage executor "saves incoming data to shared state and forwards to classification agent." The transformation executor converts the classification agent's JSON response into a typed routing object; handler executors process specific classification outcomes; the terminal executor yields final output.

**Q44.** Which class is used to connect executors with regular edges and add the switch-case edge group in a handoff orchestration workflow?
A. `HandoffBuilder`
B. `WorkflowBuilder`
C. `RoutingBuilder`
D. `ClassificationBuilder`
**Answer:** B — `WorkflowBuilder` is used to connect executors and add the switch-case edge group; there is no `HandoffBuilder`, `RoutingBuilder`, or `ClassificationBuilder` class documented for this module.

**Q61.** In a handoff orchestration workflow, what two things do "guard conditions" on handler executors verify, and what construct is used together with them to build routing logic?
A. Guard conditions verify Azure region availability for the executor; used together with `ConcurrentBuilder`'s participant list
B. Guard conditions verify correct message processing for a given handler; used together with `Case` objects in switch-case edge groups (built via factory functions generating condition checkers per classification value)
C. Guard conditions verify billing limits for the overall workflow; used together with the `GroupChatManager` base class
D. Guard conditions are unrelated to handoff orchestration entirely and are assumed to only apply to Magentic orchestration
**Answer:** B — Handler executors use guard conditions to verify correct message processing. Routing logic is built via factory functions that generate condition checkers for each classification value, examined by conditions used with `Case` objects inside switch-case edge groups (with a Default case as fallback).

## Use Magentic orchestration

**Q45.** What artifact does the Magentic manager build and refine as the workflow progresses, recording goals, subgoals, and execution plans?
A. A static configuration file
B. A dynamic task ledger
C. A `response_format` schema
D. A `GroupChatManager` subclass
**Answer:** B — The module states: "A dynamic task ledger is built and refined as the workflow progresses, recording goals, subgoals, and execution plans."

**Q46.** Which class is used to build a Magentic orchestration workflow?
A. `MagenticBuilder`
B. `PlannerBuilder`
C. `TaskLedgerBuilder`
D. `ManagerBuilder`
**Answer:** A — `MagenticBuilder` creates the Magentic orchestration; you add agent participants, configure the event callback with streaming mode, and set up the standard manager.

**Q47.** Which parameters are configured on the "standard manager" in Magentic orchestration to control orchestration behavior? (Choose three.)
A. Maximum round count
B. Stall count
C. Reset count
D. Vector index dimension
**Answer:** A, B, C — The standard manager's behavior is controlled via "maximum round count, stall count, and reset count." Vector index dimension is unrelated to Magentic orchestration (it's a search/embedding concept, not covered in this module).

**Q48.** Which agent class example is given for defining specialized agents in Magentic orchestration?
A. `ChatAgent`
B. `FunctionAgent`
C. `ToolAgent`
D. `RoutingAgent`
**Answer:** A — The module gives the example: "Create agent instances (for example, `ChatAgent`) with specific instructions and chat clients."

**Q49.** Which method is called to run a Magentic orchestration workflow, matching the pattern used by sequential orchestration?
A. `run` synchronous call
B. `run_stream`
C. `execute`
D. `invoke_sync`
**Answer:** B — Magentic orchestration calls `run_stream` with the complex task, the same streaming method used by sequential orchestration (as opposed to `run()` + `get_outputs()` used by concurrent and group chat).

**Q50.** Which scenario is explicitly listed as a reason to AVOID Magentic orchestration?
A. The problem is complex or open-ended with no predetermined solution path
B. Speed is the priority, since this method emphasizes planning over fast execution
C. A documented plan of approach is needed for human review
D. Agents have tools that can directly interact with external systems
**Answer:** B — Magentic orchestration emphasizes planning over fast execution, so it should be avoided when speed is the priority. Options A, C, and D are reasons TO USE Magentic orchestration.

**Q51.** How does Magentic orchestration primarily differ from group chat orchestration, even though both use a "manager" concept?
A. Magentic orchestration cannot use `ChatAgent` instances for its specialized agents at all, unlike group chat
B. The Magentic manager actively plans, delegates subtasks, and maintains a dynamic task ledger, whereas the group chat manager mainly selects the next speaker and decides termination/user-input timing
C. Group chat orchestration does not support a manager concept at all in this framework, unlike Magentic
D. Magentic orchestration only supports a single agent participant in the workflow, unlike group chat
**Answer:** B — Group chat orchestration's manager selects who speaks next and decides termination/human-input timing within a shared conversation; the Magentic manager goes further by actively planning, delegating subtasks to specialized agents, and building/adapting a dynamic task ledger — a plan-driven rather than turn-selection role.

**Q62.** In Magentic orchestration, what does the async event handling callback need to handle, per the module's implementation steps?
A. Only final results — intermediate events are not exposed to the callback at all
B. Orchestrator messages, agent streaming updates, agent messages, and final results
C. Only Azure Monitor alert events triggered by the workflow's execution
D. Only `WorkflowErrorEvent` instances raised during orchestration failures
**Answer:** B — Step 2 of the Magentic implementation is to set up an event handling callback that handles different event types during orchestration: orchestrator messages, agent streaming updates, agent messages, and final results.

**Q63.** What does the module say the Magentic orchestration process emphasizes, beyond simply delivering a final solution?
A. Minimizing token usage above all else in every orchestration run, even at the cost of solution quality
B. Building and documenting the approach (via the dynamic task ledger) as much as delivering the final solution
C. Running all agents exclusively inside Azure Container Apps for isolation and cost tracking purposes
D. Avoiding any use of streaming responses throughout the entire orchestration process end to end
**Answer:** B — The module states: "The process emphasizes building and documenting the approach as much as delivering the final solution," reflected in the dynamic task ledger that records goals, subgoals, and execution plans as the workflow progresses.

## Exercise / Knowledge check / Summary

**Q52.** In the module's hands-on exercise, what two agents are created to collaborate on triaging and resolving issues found in system log files?
A. A monitoring agent and a reporting agent
B. An incident manager agent and a devops agent
C. A maker agent and a checker agent
D. A classification agent and a handler agent
**Answer:** B — The exercise has you "create an incident manager agent and a devops agent that collaborates to fix the issues," built using Azure AI Agents and the Microsoft Agent Framework.

**Q53.** Per the module's own knowledge check, which orchestration pattern is most suitable for brainstorming and collaborative problem solving among multiple agents?
A. Sequential
B. Magentic
C. Group Chat
D. Concurrent
**Answer:** C — The knowledge check's stated correct answer is Group Chat. Magentic is better suited to complex, open-ended, evolving problems requiring a plan/ledger; sequential and concurrent don't foster the shared, moderated discussion group chat provides.

**Q54.** Which five orchestration patterns does the module's summary list as having been covered?
A. Concurrent, sequential, handoff, group chat, and magentic
B. Concurrent, parallel, cascading, round-robin, and magentic
C. Sequential, handoff, broadcast, consensus, and adaptive
D. Concurrent, sequential, escalation, voting, and magentic
**Answer:** A — The summary explicitly lists: "concurrent, sequential, handoff, group chat, and magentic" as the five orchestration patterns covered.

**Q55.** According to the module summary, what does the Microsoft Agent Framework SDK provide that lets you define agents, run orchestrations, handle structured data, and retrieve results asynchronously?
A. A unified interface
B. A separate SDK per orchestration pattern
C. A manual REST API only, with no SDK abstraction
D. A required dependency on Semantic Kernel's `AgentGroupChat` class
**Answer:** A — The summary states the SDK "provides a unified interface for defining agents, running orchestrations, handling structured data, and retrieving results asynchronously." It is explicitly one SDK across all patterns, not per-pattern SDKs, and does not require the legacy Semantic Kernel `AgentGroupChat` class.

**Q56.** [general Azure knowledge] After completing a hands-on Microsoft Learn exercise that provisions real Azure resources (such as Azure AI Agents in the multi-agent exercise), what best-practice cleanup step should you take once you're done exploring?
A. Leave all resources running indefinitely for future reference
B. Delete the Azure resources created during the exercise to avoid ongoing cost
C. Downgrade the resources to a free tier automatically after the exercise
D. Export the resources to an ARM template and delete only the resource group tags
**Answer:** B — The module explicitly tips: "After completing the exercise... delete the Azure resources that you created during the exercise." This is standard Azure cost-hygiene practice for any provisioned lab resources.

## Scenario-based questions

**Q64.** For the DevOps scenario from the introduction (Monitoring Agent → Root Cause Analysis Agent → Automated Deployment Agent → Reporting Agent), each agent's work strictly depends on the previous agent's completed output, and the pipeline always runs in that exact order. Which orchestration pattern and builder class fit best, and which run method would be used?
A. Concurrent orchestration, `ConcurrentBuilder`, `run()` — since all four agents should analyze the incident independently at the same time
B. Sequential orchestration, `SequentialBuilder`, `run_stream()` — since the order is fixed and each agent's output feeds the next
C. Handoff orchestration, `WorkflowBuilder`, `run_stream()` — since the number of agents involved isn't known in advance
D. Group chat orchestration, `GroupChatBuilder`, `run()` — since a chat manager should pick which agent speaks next
**Answer:** B — This is a textbook fixed, predetermined pipeline (monitoring → root cause → deployment → reporting), which is exactly what sequential orchestration is for: `SequentialBuilder`, participants added in order, and `run_stream()` (not `run()`, which concurrent and group chat use) processes through all agents sequentially.

**Q65.** A support system needs to: (1) let a classification agent inspect an incoming ticket and route it, via structured JSON output and switch-case logic, to exactly one of several specialist agents whose identity isn't known until classification happens, then (2) once a specialist resolves the issue, run three independent quality-review agents in parallel on the final response and combine their scores. Which two orchestration patterns and builders are needed for parts 1 and 2 respectively?
A. Part 1: Handoff orchestration via `WorkflowBuilder` with `response_format`-driven classification, `Case` objects, and a Default case; Part 2: Concurrent orchestration via `ConcurrentBuilder`, `participants()`, `run()`, and `get_outputs()`
B. Part 1: Sequential orchestration via `SequentialBuilder` with a fixed agent order; Part 2: Magentic orchestration via `MagenticBuilder` and a dynamic task ledger
C. Part 1: Group chat orchestration via `GroupChatBuilder` with a moderating manager; Part 2: Handoff orchestration via `WorkflowBuilder` and switch-case edges
D. Both parts should use Magentic orchestration via `MagenticBuilder` and its task ledger, since it's assumed to be the most general-purpose pattern available
**Answer:** A — Part 1 matches handoff orchestration exactly: classification-based dynamic routing where the number/order of downstream agents isn't fixed, implemented with `WorkflowBuilder`, `response_format` for structured JSON, `Case` objects in a switch-case edge group, and a Default fallback case. Part 2 matches concurrent orchestration: broadcasting the same task (reviewing the final response) to multiple independent agents and collecting/combining their results via `ConcurrentBuilder` → `participants()` → `build()` → `run()` → `get_outputs()`.

**Q66.** A solution architect is comparing this module's Microsoft Agent Framework orchestration patterns against the separate Foundry visual workflow builder (nodes, Power Fx, YAML canvas) covered in another module. Both can implement multi-agent coordination and human-in-the-loop pauses. What is the key architectural distinction between the two, per the naming-note guidance in this module and the cross-module distinguishing note?
A. There is no distinction at all; they are assumed to be the same underlying product marketed under two different names by Microsoft, with identical authoring surfaces and identical class names shared between them
B. Microsoft Agent Framework is a code-first SDK (Python/.NET) where you write orchestration logic directly against classes like `ConcurrentBuilder`/`SequentialBuilder`/`GroupChatBuilder`/`WorkflowBuilder`/`MagenticBuilder`; the Foundry visual workflow builder is a low-code, node-based canvas (with Power Fx expressions and YAML export) built in the Foundry portal — an exam question describing a visual canvas or drag-and-drop nodes points to Foundry workflows, while one describing Python/C# orchestration classes points to Microsoft Agent Framework
C. Microsoft Agent Framework only works with Azure OpenAI models per this option, while Foundry workflows are assumed to work with any model provider instead, making provider support the real distinguishing factor between the two
D. Foundry workflows require Semantic Kernel's `AgentGroupChat` class internally to function correctly, while Microsoft Agent Framework supposedly does not depend on any Semantic Kernel class at all in its implementation
**Answer:** B — This module's own naming note and the cross-referenced module distinction establish that Microsoft Agent Framework is code-first SDK-level orchestration, while Foundry agent workflows are the separate low-code visual/YAML orchestration layer — both can achieve similar multi-agent and human-in-the-loop patterns but through fundamentally different authoring surfaces (code vs. canvas).

**Q67.** A moderated brainstorming session needs three specialized agents (legal, marketing, engineering) to discuss a product launch decision together in a shared thread, with a human able to weigh in at key moments, and the conversation should end once consensus is reached or after a maximum number of rounds. Which orchestration pattern fits, which manager methods govern the per-round flow, and what agent-count guidance should the architect follow?
A. Magentic orchestration; the governing methods are assumed to be `plan()` and `delegate()`; no agent-count limit is assumed to apply to this pattern at all
B. Group chat orchestration; each round follows `should_request_user_input` → `should_terminate` → (`filter_results` or `select_next_agent`); limit to three or fewer agents for easier control
C. Handoff orchestration; the governing methods are `classify()` and `route()`; unlimited agents are assumed to be supported in this pattern
D. Sequential orchestration; the governing methods are assumed to be `create_agent()` and `run_stream()`; exactly three agents are assumed to be strictly required
**Answer:** B — This is the group chat orchestration use case (shared conversation, human-in-the-loop, consensus-seeking with three peer specialists). The manager's documented per-round call order is `should_request_user_input` → `should_terminate` → `filter_results` (if ending) or `select_next_agent` (if continuing), and the module recommends limiting group chat to three or fewer agents for manageable conversation flow — which this three-agent scenario satisfies exactly.

**Q68.** An open-ended R&D problem has no predetermined solution path: multiple specialized agents (data scientist, domain expert, systems engineer) must be dynamically assigned subtasks as understanding of the problem evolves, and stakeholders want a documented plan showing how the solution was reached, not just the final answer. Which orchestration pattern fits, which class builds it, and what artifact does its manager maintain?
A. Sequential orchestration; built with `SequentialBuilder` and a fixed agent order; no artifact is assumed to be produced beyond the plain final output text
B. Concurrent orchestration; built with `ConcurrentBuilder` and parallel participants; the manager is assumed to maintain only a static configuration file
C. Magentic orchestration; `MagenticBuilder`; a dynamic task ledger recording goals, subgoals, and execution plans, maintained by the Magentic manager (configured with parameters like maximum round count, stall count, and reset count)
D. Handoff orchestration; built with `WorkflowBuilder` and switch-case routing; the manager is assumed to maintain only a `response_format` JSON schema
**Answer:** C — This is the defining Magentic orchestration scenario: complex, open-ended, evolving problem requiring dynamic delegation across specialists, built via `MagenticBuilder`, run with `run_stream`, and governed by a standard manager (max round count, stall count, reset count) that builds and refines a dynamic task ledger — explicitly emphasizing documenting the approach alongside the final solution, unlike the other four patterns.
