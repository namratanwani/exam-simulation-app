# Practice questions — Develop generative AI apps that use tools

## What are tools?

**Q1.** A developer confuses the `web_search` tool used in Responses API prompts with "Foundry Tools" like Azure Language and Azure Speech. Which statement correctly clarifies the distinction per Microsoft Learn?

A. They are exactly the same thing, just described differently in different modules — but the module explicitly separates the two concepts by name and purpose
B. Tools used in generative AI model prompts (code_interpreter, web_search, file_search, function) are distinct from Foundry Tools, which are Azure AI APIs used in applications and agents
C. Foundry Tools can only be used inside the code_interpreter sandbox — this confuses two unrelated concepts and isn't stated anywhere in the module
D. web_search is a Foundry Tool but code_interpreter is not — both are prompt-level tools, and neither one is a Foundry Tool at all

**Answer:** B — The module explicitly states: "The use of tools in generative AI model prompts shouldn't be confused with Foundry Tools; which are Azure AI APIs that you can use in your applications and agents." This is a classic close-naming exam trap.

**Q2.** By default, who/what decides WHEN and WHICH tool to use during a Responses API call?

A. The developer must explicitly select the tool in every request — the module describes the opposite default behavior
B. The model itself chooses when to use a tool (and which one), based on the prompt — though this can be guided via Instructions and tool selection rules
C. Azure Content Safety automatically selects tools — Content Safety handles moderation, not tool selection, and isn't mentioned in this context
D. Tools are always invoked in a fixed sequential order — the module describes model-driven selection, not any fixed ordering

**Answer:** B — "By default, the model chooses when to use a tool (and which one), based on the prompt. You can configure tool selection rules and use the Instructions (system prompt) parameter to guide this choice."

**Q3.** In which parameter of the `responses.create()` method are available tools specified?

A. `instructions`
B. `tools`
C. `capabilities`
D. `plugins`

**Answer:** B — Tools are specified as a JSON list in the `tools` parameter, e.g., `tools=[{"type": "{tool_type}", ...}]`.

**Q21.** Which of the following is NOT one of the reasons the module gives for why tools matter in generative AI applications?

A. Access real-time information not in training data
B. Take actions such as sending emails or creating database records
C. Automatically reduce Azure OpenAI billing costs by 50%
D. Ground responses in facts to reduce incorrect information

**Answer:** C — The module lists five reasons tools matter: access real-time information, take actions, ground responses in facts, extend functionality (connect to existing systems), and build intelligent workflows (chain multi-step operations). Automatic cost reduction is not among them.

**Q22.** How does this module describe the relationship between specifying tools directly in client-application prompts and building a full agentic AI solution?

A. They are unrelated approaches with no connection — the module frames one as an explicit stepping stone toward the other
B. Specifying tools in client-application prompts is described as a stepping stone toward agentic AI, where model + instructions + tools are encapsulated/persisted in a named agent
C. Client-application tool use is deprecated in favor of agents — the module presents it as a valid earlier stage, not a deprecated approach
D. Agents cannot use the same four tools described in this module — nothing in the module states agents lose access to code_interpreter, web_search, file_search, or function

**Answer:** B — The module frames this module's approach (tools specified in prompts by a client application) as "a stepping stone toward agentic AI solutions," where the model, instructions, and tools are encapsulated and persisted as a named agent (covered in the separate agents learning path).

**Q23.** Which FOUR tools does the module describe as "commonly used" Responses API tools?

A. code_interpreter, web_search, file_search, function
B. embeddings, fine-tuning, moderation, translation
C. vector_search, image_generation, speech_to_text, text_to_speech
D. code_interpreter, function, moderation, embeddings

**Answer:** A — The module names exactly these four as commonly used tools, while noting these are only some of the available tools and that the ecosystem is growing.

## Use the code_interpreter tool

**Q4.** Which parameter in the code_interpreter tool definition specifies how the sandboxed Python execution environment is provisioned?

A. `"runtime": "python3.12"`
B. `"container": {"type": "auto"}`
C. `"sandbox_mode": "enabled"`
D. `"execution_env": "cloud"`

**Answer:** B — The example shows `tools=[{"type": "code_interpreter", "container": {"type": "auto"}}]`.

**Q5.** Which TWO of the following are explicitly listed as limitations of the code_interpreter tool? (Choose 2.)

A. No external network access in the sandboxed environment
B. Cannot process CSV files
C. Timeout limits apply to long-running operations
D. Cannot use the pandas library

**Answer:** A, C — The module lists: sandboxed with no external network access, some libraries may not be available, timeout limits apply, and memory constraints. B is false — file handling (CSV, JSON, images) is a key feature. D is false — pandas is explicitly listed as a pre-installed, leverageable library.

**Q6.** A developer instructs the model to "use the python tool to run code for math problems." Why does the module recommend using the phrase "python tool" specifically?

A. It's required syntax for the `tools` array — the `tools` array itself only ever needs `"type": "code_interpreter"`, not this phrase
B. Many models internally use the name "python tool" to identify the code_interpreter tool, so using this language in instructions improves alignment
C. "python tool" is a separate, distinct tool from code_interpreter — the module never lists it as its own tool type
D. It disables the sandboxing restrictions — nothing in the module suggests instruction wording can change sandbox behavior

**Answer:** B — Best practices state: "Many models internally use the name python tool to identify the code_interpreter tool - so use this language in your instructions."

**Q24.** Which of the following is listed among the code_interpreter tool's common use cases?

A. Summarizing breaking news from the internet
B. Data Analysis — parsing a CSV and generating summary statistics
C. Locating a specific clause in a legal contract
D. Calling an internal API to check order status

**Answer:** B — Data Analysis (parse CSV, generate summary stats) is one of the module's four code_interpreter use cases, alongside Math & Physics, File Conversion, and Prototyping. The other options are use cases for web_search, file_search, and function, respectively.

**Q25.** Per the module's "How it works" steps for code_interpreter, what happens immediately AFTER the model generates Python code, and BEFORE results are incorporated into the response?

A. The code is emailed to the developer for manual approval
B. The code runs in a sandboxed environment with access to common libraries like pandas and numpy
C. The code is translated into a different programming language
D. The Foundry portal automatically deploys the code as an Azure Function

**Answer:** B — The five-step process is: include code_interpreter in tools, model analyzes whether execution is needed, model generates Python code, code runs in the sandboxed environment (with pandas/numpy/math access), then results are returned and incorporated into the response.

**Q26.** Which of the following is an explicit code_interpreter best practice regarding AI-generated code before it's used in production?

A. Skip validation since the sandbox guarantees correctness — the module explicitly recommends validating generated code, sandboxing alone isn't treated as sufficient
B. Validate AI-generated code before production use, and monitor costs since code execution adds tokens
C. Always disable the container setting — the container config is what provisions the sandbox in the first place, not something to disable
D. Only use code_interpreter for read-only operations — no such restriction is listed among the module's best practices

**Answer:** B — The module's best practices explicitly include "validate AI-generated code before production use" and "monitor costs (code execution adds tokens)."

## Use the web_search tool

**Q7.** Which key feature of the web_search tool directly helps REDUCE hallucination risk?

A. Automatic query generation — this affects convenience, not whether answers are grounded in real sources
B. Source-grounded responses, since answers are built from retrieved web content rather than solely from training data
C. Seamless user experience — a UX benefit, not a hallucination-reduction mechanism
D. Live information retrieval speed — speed doesn't by itself make an answer more factually grounded

**Answer:** B — "Reduced hallucination risk - Improve reliability by checking external sources" is listed directly, tied to building answers from retrieved content ("Source-grounded responses").

**Q8.** Which scenario is the BEST fit for the web_search tool based on the module's common use cases?

A. Locating a specific clause across a company's internal contract documents
B. Summarizing key updates on a breaking technology announcement from this week
C. Running a statistical analysis on an uploaded CSV file
D. Calling an internal API to check order status

**Answer:** B — "Current Events: Summarize key updates on a breaking technology announcement" is listed as a web_search use case. A is a file_search use case (Legal Review); C is code_interpreter (Data Analysis); D is the function tool (System Integration).

**Q9.** Which limitation of web_search means that running the SAME query twice might yield DIFFERENT results?

A. Regional network restrictions — this affects whether a query can run at all, not why identical queries diverge
B. Retrieved content may change over time, so repeated runs can produce different answers
C. The sandboxed environment resets between calls — that's a code_interpreter concept, web_search has no sandbox
D. Source quality can vary — a separate concern from why the SAME query yields different results over time

**Answer:** B — Explicitly listed as a limitation: "Retrieved content may change over time, so repeated runs can produce different answers."

**Q27.** Per the module's "How it works" steps for web_search, what happens after the model issues one or more search queries?

A. The model immediately halts and asks the user for clarification
B. Relevant pages are selected and summarized, then the response combines the search findings
C. The query is stored permanently in the vector store
D. The model switches automatically to the file_search tool

**Answer:** B — The steps are: include web_search in tools, model evaluates if fresh data is needed, model issues search queries, relevant pages are selected/summarized, and the response combines search findings.

**Q28.** Which TWO of the following are explicit web_search best practices? (Choose 2.)

A. Ask time-aware questions clearly, using terms like "latest," "current," or specific date ranges
B. Never verify critical facts, since web_search results are always authoritative
C. Verify critical facts independently for high-stakes scenarios
D. Avoid tracking usage or latency, since web_search has no performance impact

**Answer:** A, C — The module's best practices include asking time-aware questions clearly and verifying critical facts independently for high-stakes scenarios. B and D contradict the module, which recommends verification and notes that web retrieval increases response time/token usage (so tracking usage/latency is advised).

**Q29.** Which web_search limitation reflects the fact that results are constrained by what search engines can actually see and index at the moment of the query?

A. Regional/policy/network restrictions may apply
B. Results depend on public/indexable availability at query time
C. Timeout limits apply to long-running operations
D. Some libraries may be unavailable

**Answer:** B — This is listed verbatim as a limitation: "Results depend on public/indexable availability at query time." (A is a separate, also-listed limitation about regional/policy/network restrictions; C and D are code_interpreter limitations, not web_search's.)

## Use the file_search tool

**Q10.** Before a model can use the file_search tool to answer questions from an uploaded PDF, which two API calls must the application make (in order)?

A. `client.responses.create()` then `client.vector_stores.create()`
B. `client.vector_stores.create()` then `client.vector_stores.files.upload_and_poll()`
C. `client.files.upload()` then `client.responses.create()`
D. `client.embeddings.create()` then `client.responses.create()`

**Answer:** B — The example first creates a vector store (`client.vector_stores.create(name="policy-docs")`), then uploads and indexes a file into it (`client.vector_stores.files.upload_and_poll(vector_store_id=..., file=...)`), before calling `responses.create()` with the `file_search` tool.

**Q11.** What does adding `include=["file_search_call.results"]` to a `responses.create()` call accomplish?

A. It forces the model to always use file_search regardless of the prompt — `include` only affects what's returned, not tool selection
B. It surfaces the file_search retrieval results (matched passages) in the response for debugging/traceability
C. It uploads new files to the vector store automatically — that's handled by `upload_and_poll`, a separate call entirely
D. It restricts the search to only PDF file types — nothing about `include` filters by file type

**Answer:** B — This parameter is used specifically to make retrieval results visible for citations/transparency and troubleshooting, consistent with the "Citations and transparency" key feature and the best practice "Include retrieval results in development... for troubleshooting."

**Q12.** A company needs an agent to access large quantities of data spread across MULTIPLE enterprise data stores at scale. What does the module recommend INSTEAD of relying solely on the file_search tool for this scenario?

A. Increasing the vector store size limit
B. Using multiple separate code_interpreter sandboxes
C. Using the Foundry IQ knowledge store solution with a Microsoft Foundry agent
D. Switching to the ChatCompletions API

**Answer:** C — The module's note states: "for enterprise-scale agents that need to access large quantities of data in multiple data stores, you should consider using the Foundry IQ knowledge store solution with a Microsoft Foundry agent." This is a key exam distinction between simple file_search grounding and enterprise-scale Foundry IQ knowledge integration.

**Q13.** Which characteristic distinguishes file_search's retrieval method from simple exact keyword matching?

A. It only searches file names, not content — the opposite is true; file_search indexes and searches document content
B. Semantic retrieval — it finds relevant passages by meaning, not only exact keyword matches
C. It requires exact case-sensitive string matches — that describes basic keyword matching, which is what file_search moves beyond
D. It only works with structured JSON files — the module's example uses an unstructured PDF, not JSON

**Answer:** B — "Semantic retrieval - Finds relevant passages by meaning, not only exact keyword matches" is explicitly listed as a key feature.

**Q30.** Which of the following is listed among file_search's common use cases?

A. Policy Q&A — answering questions from HR policy PDFs
B. Solving differential equations
C. Comparing product features and pricing from the public web
D. Triggering a support-ticket creation workflow

**Answer:** A — Policy Q&A (HR policy PDFs) is one of file_search's four listed use cases, alongside Support Assistants, Legal Review, and Knowledge Discovery. The other options belong to code_interpreter, web_search, and function, respectively.

**Q31.** Why does the module recommend scoping vector stores carefully — for example, keeping separate stores for HR, legal, and finance documents — rather than combining everything into one large store?

A. Azure enforces a hard limit of one document per vector store
B. Very large or mixed-domain stores return less focused context, reducing answer quality
C. Separate stores are required for billing purposes
D. The Responses API rejects vector stores larger than 1 file

**Answer:** B — The module lists as a limitation: "very large/mixed-domain stores return less focused context," and correspondingly recommends "scope vector stores carefully (separate domains like HR/legal/finance)" as a best practice.

**Q32.** If the source documents behind a file_search vector store are updated (e.g., a policy PDF is revised), what does the module say must happen for the tool to reflect the changes?

A. Nothing; the vector store automatically detects and re-indexes changed files in real time
B. Updated source files require re-indexing
C. The entire Foundry project must be redeployed
D. The `include` parameter must be changed to `"auto_reindex"`

**Answer:** B — Explicitly listed as a limitation: "updated source files require re-indexing."

## Use the function tool

**Q14.** In the function tool pattern, who is responsible for actually EXECUTING the business logic of the requested function?

A. The model executes the function directly within its sandbox
B. The developer's application code — the model only returns a structured function-call request
C. Azure Functions runtime automatically, with no application code involved
D. The Foundry portal executes it via a built-in orchestrator

**Answer:** B — "The model doesn't run your business logic directly. Instead, it returns a structured function call, your code runs the function, and then you pass the function output back to the model." This is the central concept of function calling and a common exam point.

**Q15.** After your application runs a requested function, which message type must be appended to the conversation to return the result to the model?

A. `{"type": "function_result", "value": ...}`
B. `{"type": "function_call_output", "call_id": ..., "output": ...}`
C. `{"role": "function", "content": ...}`
D. `{"type": "tool_response", "id": ...}`

**Answer:** B — The example code appends exactly `{"type": "function_call_output", "call_id": item.call_id, "output": current_time}` to the messages list before requesting a follow-up response.

**Q16.** How does the application code determine that the model wants to call a specific function, per the example in the module?

A. By checking `response.status == "function_requested"` — no such status value or field appears anywhere in the example
B. By iterating `response.output` and checking `item.type == "function_call"` and `item.name`
C. By parsing `response.output_text` for a JSON string — the example checks structured `item.type`, not a text field
D. By checking `response.usage.function_calls` — `usage` tracks token counts, not function-call detection

**Answer:** B — The example code loops: `for item in response.output: if item.type == "function_call" and item.name == "get_time":`.

**Q17.** Which TWO best practices are explicitly recommended for the function tool to maintain safe, reliable production use? (Choose 2.)

A. Never validate function inputs — trust the model's arguments completely
B. Keep tools focused with small, single-purpose functions
C. Require explicit authorization for high-impact/sensitive operations
D. Avoid logging tool usage to reduce overhead

**Answer:** B, C — "Keep tools focused - Small, single-purpose functions are easier to control and test" and "Limit sensitive operations - Require explicit authorization for high-impact actions" are both explicit best practices. A and D directly contradict the stated best practices ("Validate function inputs - Never trust tool arguments blindly" and "Log tool usage - Track calls, latency, and failure rates").

**Q18.** A prompt like "Hello" does NOT trigger the `get_time` function in the module's example, but "What time is it?" does. What does this demonstrate about function tool behavior?

A. Functions must be manually invoked by the developer for every prompt — that would make the differing example behavior impossible, since no manual invocation happens
B. The model evaluates each prompt and decides autonomously whether a function call is needed based on user intent
C. The function tool only works with prompts containing the word "time" — a narrower rule than what the module actually describes about intent-based evaluation
D. All prompts always trigger every available function — contradicted directly by "Hello" not triggering `get_time`

**Answer:** B — This matches the "How it works" step: "Model evaluates the prompt - It determines whether a function call is needed," demonstrated by the differing behavior between the two example prompts.

**Q33.** In the module's function tool example, the initial system-level prompt is set using `{"role": "developer", "content": "You are an AI assistant..."}`. What does the module note about this role name?

A. `"developer"` is invalid and would cause an API error — the example uses it successfully, so it's clearly a valid role value
B. `"developer"` is used here for the system-level prompt, distinct from the `"system"` role seen elsewhere in the module — both patterns appear in Microsoft's examples
C. `"developer"` grants the message elevated administrative permissions over the model — the module never describes any permission or privilege tied to a role name
D. `"developer"` can only be used with the code_interpreter tool — the role name is unrelated to which tool is configured in the `tools` array

**Answer:** B — The module explicitly notes this role-naming nuance: `"developer"` is used for the system-level prompt in the function-calling example, distinct from `"system"` used elsewhere, and states both patterns appear in Microsoft's examples — a subtle exam-relevant detail.

**Q34.** Which TWO of the following are listed among the function tool's common use cases? (Choose 2.)

A. Task Automation — triggering ticket creation or notifications
B. Data Lookup — querying business rules or reference tables before answering
C. Fact Verification — validating claims against public sources
D. Math & Physics — solving differential equations

**Answer:** A, B — Task Automation and Data Lookup are two of the function tool's three listed use cases (alongside System Integration). Fact Verification is a web_search use case; Math & Physics is a code_interpreter use case.

**Q35.** Which limitation applies specifically to the function tool, distinguishing it from tools whose retrieval/execution happens entirely within the platform?

A. Tool latency increases end-to-end response time, because your application must run the function before the model can continue
B. No external network access is available — this describes the sandboxed code_interpreter environment, not the function tool
C. Results may change between runs due to live content changes — this is a web_search limitation about content changing over time, not something specific to function
D. Answer quality depends on document chunking — this describes file_search's vector-store retrieval quality, not function's execution model

**Answer:** A — The module lists "tool latency increases end-to-end response time" as a function-tool limitation, since your app must execute the function and return output before the model can finish. B is a code_interpreter limitation, C is a web_search limitation, and D is a file_search limitation.

## Cross-tool comparison

**Q19.** A developer needs the model to answer questions using only the company's internal, uploaded compliance manual, with citations to specific matched passages. Which tool is most appropriate, and why NOT web_search?

A. web_search — because it can find any content, including internal manuals published online — but web_search explicitly accesses only public internet content, not private uploaded documents
B. file_search — because it grounds responses in your own uploaded/indexed documents with semantic retrieval and citation support, whereas web_search only accesses public internet content
C. function — because functions can retrieve any data source — functions only execute developer-written logic, they don't do semantic document retrieval on their own
D. code_interpreter — because it can read uploaded files directly — it processes files for computation, not for citation-backed semantic search

**Answer:** B — file_search is specifically designed for document-grounded answers from uploaded files with citations, while web_search explicitly retrieves information from the public Internet, not private/internal documents. code_interpreter (D) can process uploaded files for computation but isn't designed for semantic search/grounding over document content.

**Q20.** Which tool requires your OWN application code to execute logic and is the only one of the four where the model cannot autonomously produce the final data itself (code, search results, or documents) without your app performing an intermediate step?

A. code_interpreter, since it runs in a sandbox — but that sandbox executes fully within the platform, the model still gets its result without any app-side step
B. web_search, since it depends on external content — retrieval still happens within the platform, not via your own application code
C. function, since the model only emits a structured call that your application must run before returning output
D. file_search, since it depends on a vector store — the vector search itself runs within the platform, requiring no app-side execution step

**Answer:** C — Unlike code_interpreter (executes code within the platform's sandbox) or web_search/file_search (retrieval happens within the platform), the function tool explicitly requires "Your app runs logic" as a mandatory step — the model cannot get the function's result without your application executing it and returning `function_call_output`.

**Q36.** Matching each tool to WHERE its grounding activity actually executes: which pairing is correct?

A. code_interpreter → your own application; function → sandboxed cloud Python runtime — this swaps the two pairings the module actually describes, putting each tool in the wrong execution environment
B. code_interpreter → sandboxed cloud Python runtime (no network access); web_search → external web via search API; file_search → indexed vector search index; function → your own application (developer-controlled)
C. All four tools execute exclusively inside the Foundry-managed sandbox — function specifically executes in your own application, not any managed sandbox, which the module states explicitly
D. web_search → your own application; file_search → external web — this also swaps two of the module's actual pairings, reversing where each tool's retrieval genuinely happens

**Answer:** B — This is the module's cross-tool comparison table exactly: code_interpreter executes in a sandboxed cloud Python runtime with no network access, web_search hits the external web via a search API, file_search queries an indexed vector search index, and function executes in your own developer-controlled application.

## Scenario-based questions

**Q37.** A developer builds a client app where the model must (1) read an uploaded CSV of sales figures and compute month-over-month growth, then (2) call an internal API to log the computed growth rate into a business system. Which combination of tools and execution responsibilities is correct?

A. Use `web_search` for both steps, since it can access any external system — web_search only retrieves public internet content, it can't compute over an uploaded CSV or reach a private internal API at all
B. Use `code_interpreter` for the CSV computation (executed in the sandboxed Python runtime) and `function` for logging to the internal API (executed by the developer's own application code after receiving a structured function-call request)
C. Use `file_search` for both steps, since CSVs are files — file_search performs semantic document retrieval over indexed text, not numeric computation or API calls to internal systems
D. Use `function` for both steps, since functions can do arbitrary computation and I/O — the module treats code_interpreter as the designated tool for sandboxed data computation, reserving function for developer-executed actions like logging

**Answer:** B — code_interpreter is designed for dynamic data analysis/computation on uploaded files within its sandbox, while writes to internal/business systems must go through the function tool, where the model only requests the call and the developer's application actually executes it.

**Q38.** A support chatbot needs to (1) answer questions from the company's internal, uploaded troubleshooting guides, and (2) also check whether a related software bug was reported in recent public news, reducing the risk of stating outdated information. Which two tools should be combined, and what is the key grounding difference between them?

A. code_interpreter and function — both execute developer-controlled logic, but neither performs semantic document retrieval or live web grounding at all
B. file_search (grounds in your own uploaded/indexed documents via semantic retrieval) and web_search (grounds in live public internet content, reducing hallucination on time-sensitive facts)
C. web_search for both, since it can find internal documents if they're indexed by any search engine — web_search explicitly accesses public internet content, not private uploaded documents
D. file_search for both, since troubleshooting and news are both "documents" — file_search only searches what's been uploaded/indexed, it has no access to live public news

**Answer:** B — file_search grounds answers in the company's own uploaded/indexed documents (with citations), while web_search grounds answers in current external internet content — the two tools ground responses in fundamentally different sources, which is why both are needed here.

**Q39.** A team's design doc says: "Our agent uses Foundry Tools including code_interpreter and web_search." A reviewer flags this sentence as technically imprecise. What is the correct terminology distinction, per the module?

A. There is no imprecision; Foundry Tools and Responses API tools are the same thing — this is exactly the conflation the module explicitly warns against, since the two names describe entirely separate concepts despite the shared word "tools"
B. code_interpreter and web_search are Responses API prompt-level tools, distinct from "Foundry Tools" (like Azure Language, Speech, Translator, Document Intelligence, Content Understanding) — the sentence conflates the two despite similar naming
C. Foundry Tools refers only to code_interpreter, not web_search — neither one is actually a Foundry Tool at all, so drawing any line between them on this basis is beside the point entirely
D. code_interpreter is a Foundry Tool but web_search is not — both are prompt-level Responses API tools, not Foundry Tools, so neither one qualifies as a Foundry Tool under the module's terminology

**Answer:** B — The module explicitly warns against this exact conflation: prompt-level tools (code_interpreter, web_search, file_search, function) are a different concept from Foundry Tools (the suite of Azure AI APIs), despite the shared word "tools."

**Q40.** An enterprise wants an agent that can ground responses in a small, well-defined internal FAQ document set today, but is already planning to scale to dozens of large, cross-departmental data stores within a year. What does the module suggest about tool/architecture choice across this growth path?

A. file_search alone will always scale to any number of data stores with no architectural change needed — the module explicitly recommends Foundry IQ once scale grows toward enterprise level
B. Start with file_search for the current small/well-defined document set; as the number/scale of data stores grows toward enterprise scale, consider Foundry IQ with a Microsoft Foundry agent instead
C. Use code_interpreter for all document grounding regardless of scale — code_interpreter is for sandboxed computation, not semantic document grounding at any scale
D. Use web_search once the internal documents are published publicly, to avoid the re-indexing limitation — publishing internal documents publicly isn't a solution the module suggests anywhere

**Answer:** B — This matches the module's explicit distinction: file_search suits grounding in a specific set of documents, but for enterprise-scale needs across multiple data stores, Foundry IQ with a Foundry agent is the recommended path.

**Q41.** A developer exposes a `cancel_subscription` function to the model via the function tool. To follow the module's best practices for safe production use, which combination of safeguards should they implement?

A. Trust all model-provided arguments as-is, and let the function execute immediately with no logging — this directly contradicts two explicit function-tool best practices
B. Validate the function's input arguments before executing, require explicit authorization for this high-impact/sensitive operation, and log the call (latency/failure rate) for auditing
C. Skip validation since code_interpreter's sandbox already protects the app — code_interpreter's sandbox is unrelated to the function tool, which has no such sandbox at all
D. Disable the `function` tool entirely, since no safeguards are possible — the module lists concrete safeguards (validation, authorization, logging) rather than recommending disabling the tool

**Answer:** B — This combines three explicit function-tool best practices: validate function inputs (never trust tool arguments blindly), limit sensitive operations (require explicit authorization for high-impact actions), and log tool usage (track calls, latency, failure rates) — all directly relevant to a destructive action like canceling a subscription.

**Q42.** By default the model decides which tool (if any) to use for a given prompt. A developer wants the model to strongly prefer file_search over web_search whenever a user asks about "company policy," without removing the model's general autonomy to pick tools for other prompts. How should they achieve this per the module?

A. Remove web_search from the `tools` array entirely, permanently — that would remove the model's general autonomy to pick tools for other, unrelated prompts, which the developer explicitly wants to preserve
B. Use the `instructions` (system prompt) parameter to guide tool selection behavior, e.g. directing the model to prefer file_search for company-policy questions, while both tools remain available for other prompts
C. This is not possible; tool selection can never be influenced by developers — the module explicitly states tool selection can be guided via the Instructions parameter and configurable selection rules
D. Call `client.vector_stores.create()` with a `force_tool` parameter — no such parameter exists on that call, which only creates a vector store and has nothing to do with guiding tool choice

**Answer:** B — The module states you can "configure tool selection rules and use the Instructions (system prompt) parameter to guide this choice" — the recommended way to bias behavior without hard-removing a tool's availability.

**Q43.** An assistant needs to, within one conversation flow: look up a live stock price (not in training data), compute a moving average from an uploaded price-history CSV, answer a question from an uploaded internal risk-policy PDF, and log the analysis result via an internal API. Which `tools` array configuration correctly supports all four needs?

A. `tools=[{"type": "function"}]` only, since functions can do everything — function only executes developer-written logic, it can't fetch live prices, run sandboxed computation, or search a vector store on its own
B. `tools=[{"type": "web_search"}, {"type": "code_interpreter", "container": {"type": "auto"}}, {"type": "file_search", "vector_store_ids": [...]}, {"type": "function", "name": "log_analysis", "description": "..."}]`
C. `tools=[{"type": "code_interpreter"}]` only, since it has network access for live data — code_interpreter's sandbox explicitly has no external network access
D. `tools=[{"type": "file_search"}]` only, since vector stores can hold live stock data — vector stores hold indexed documents you've uploaded, not live market data feeds

**Answer:** B — Each requirement maps to a distinct tool: web_search for live/current external data, code_interpreter for sandboxed computation on the uploaded CSV, file_search for grounding in the uploaded internal PDF via a vector store, and function for the developer-controlled action of logging to an internal API — all four can be specified together in the same `tools` array.
