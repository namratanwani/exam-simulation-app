# Practice questions — Develop generative AI apps that use tools

## What are tools?

**Q1.** A developer confuses the `web_search` tool used in Responses API prompts with "Foundry Tools" like Azure Language and Azure Speech. Which statement correctly clarifies the distinction per Microsoft Learn?

A. They are exactly the same thing, just described differently in different modules
B. Tools used in generative AI model prompts (code_interpreter, web_search, file_search, function) are distinct from Foundry Tools, which are Azure AI APIs used in applications and agents
C. Foundry Tools can only be used inside the code_interpreter sandbox
D. web_search is a Foundry Tool but code_interpreter is not

**Answer:** B — The module explicitly states: "The use of tools in generative AI model prompts shouldn't be confused with Foundry Tools; which are Azure AI APIs that you can use in your applications and agents." This is a classic close-naming exam trap.

**Q2.** By default, who/what decides WHEN and WHICH tool to use during a Responses API call?

A. The developer must explicitly select the tool in every request
B. The model itself chooses when to use a tool (and which one), based on the prompt — though this can be guided via Instructions and tool selection rules
C. Azure Content Safety automatically selects tools
D. Tools are always invoked in a fixed sequential order

**Answer:** B — "By default, the model chooses when to use a tool (and which one), based on the prompt. You can configure tool selection rules and use the Instructions (system prompt) parameter to guide this choice."

**Q3.** In which parameter of the `responses.create()` method are available tools specified?

A. `instructions`
B. `tools`
C. `capabilities`
D. `plugins`

**Answer:** B — Tools are specified as a JSON list in the `tools` parameter, e.g., `tools=[{"type": "{tool_type}", ...}]`.

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

A. It's required syntax for the `tools` array
B. Many models internally use the name "python tool" to identify the code_interpreter tool, so using this language in instructions improves alignment
C. "python tool" is a separate, distinct tool from code_interpreter
D. It disables the sandboxing restrictions

**Answer:** B — Best practices state: "Many models internally use the name python tool to identify the code_interpreter tool - so use this language in your instructions."

## Use the web_search tool

**Q7.** Which key feature of the web_search tool directly helps REDUCE hallucination risk?

A. Automatic query generation
B. Source-grounded responses, since answers are built from retrieved web content rather than solely from training data
C. Seamless user experience
D. Live information retrieval speed

**Answer:** B — "Reduced hallucination risk - Improve reliability by checking external sources" is listed directly, tied to building answers from retrieved content ("Source-grounded responses").

**Q8.** Which scenario is the BEST fit for the web_search tool based on the module's common use cases?

A. Locating a specific clause across a company's internal contract documents
B. Summarizing key updates on a breaking technology announcement from this week
C. Running a statistical analysis on an uploaded CSV file
D. Calling an internal API to check order status

**Answer:** B — "Current Events: Summarize key updates on a breaking technology announcement" is listed as a web_search use case. A is a file_search use case (Legal Review); C is code_interpreter (Data Analysis); D is the function tool (System Integration).

**Q9.** Which limitation of web_search means that running the SAME query twice might yield DIFFERENT results?

A. Regional network restrictions
B. Retrieved content may change over time, so repeated runs can produce different answers
C. The sandboxed environment resets between calls
D. Source quality can vary

**Answer:** B — Explicitly listed as a limitation: "Retrieved content may change over time, so repeated runs can produce different answers."

## Use the file_search tool

**Q10.** Before a model can use the file_search tool to answer questions from an uploaded PDF, which two API calls must the application make (in order)?

A. `client.responses.create()` then `client.vector_stores.create()`
B. `client.vector_stores.create()` then `client.vector_stores.files.upload_and_poll()`
C. `client.files.upload()` then `client.responses.create()`
D. `client.embeddings.create()` then `client.responses.create()`

**Answer:** B — The example first creates a vector store (`client.vector_stores.create(name="policy-docs")`), then uploads and indexes a file into it (`client.vector_stores.files.upload_and_poll(vector_store_id=..., file=...)`), before calling `responses.create()` with the `file_search` tool.

**Q11.** What does adding `include=["file_search_call.results"]` to a `responses.create()` call accomplish?

A. It forces the model to always use file_search regardless of the prompt
B. It surfaces the file_search retrieval results (matched passages) in the response for debugging/traceability
C. It uploads new files to the vector store automatically
D. It restricts the search to only PDF file types

**Answer:** B — This parameter is used specifically to make retrieval results visible for citations/transparency and troubleshooting, consistent with the "Citations and transparency" key feature and the best practice "Include retrieval results in development... for troubleshooting."

**Q12.** A company needs an agent to access large quantities of data spread across MULTIPLE enterprise data stores at scale. What does the module recommend INSTEAD of relying solely on the file_search tool for this scenario?

A. Increasing the vector store size limit
B. Using multiple separate code_interpreter sandboxes
C. Using the Foundry IQ knowledge store solution with a Microsoft Foundry agent
D. Switching to the ChatCompletions API

**Answer:** C — The module's note states: "for enterprise-scale agents that need to access large quantities of data in multiple data stores, you should consider using the Foundry IQ knowledge store solution with a Microsoft Foundry agent." This is a key exam distinction between simple file_search grounding and enterprise-scale Foundry IQ knowledge integration.

**Q13.** Which characteristic distinguishes file_search's retrieval method from simple exact keyword matching?

A. It only searches file names, not content
B. Semantic retrieval — it finds relevant passages by meaning, not only exact keyword matches
C. It requires exact case-sensitive string matches
D. It only works with structured JSON files

**Answer:** B — "Semantic retrieval - Finds relevant passages by meaning, not only exact keyword matches" is explicitly listed as a key feature.

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

A. By checking `response.status == "function_requested"`
B. By iterating `response.output` and checking `item.type == "function_call"` and `item.name`
C. By parsing `response.output_text` for a JSON string
D. By checking `response.usage.function_calls`

**Answer:** B — The example code loops: `for item in response.output: if item.type == "function_call" and item.name == "get_time":`.

**Q17.** Which TWO best practices are explicitly recommended for the function tool to maintain safe, reliable production use? (Choose 2.)

A. Never validate function inputs — trust the model's arguments completely
B. Keep tools focused with small, single-purpose functions
C. Require explicit authorization for high-impact/sensitive operations
D. Avoid logging tool usage to reduce overhead

**Answer:** B, C — "Keep tools focused - Small, single-purpose functions are easier to control and test" and "Limit sensitive operations - Require explicit authorization for high-impact actions" are both explicit best practices. A and D directly contradict the stated best practices ("Validate function inputs - Never trust tool arguments blindly" and "Log tool usage - Track calls, latency, and failure rates").

**Q18.** A prompt like "Hello" does NOT trigger the `get_time` function in the module's example, but "What time is it?" does. What does this demonstrate about function tool behavior?

A. Functions must be manually invoked by the developer for every prompt
B. The model evaluates each prompt and decides autonomously whether a function call is needed based on user intent
C. The function tool only works with prompts containing the word "time"
D. All prompts always trigger every available function

**Answer:** B — This matches the "How it works" step: "Model evaluates the prompt - It determines whether a function call is needed," demonstrated by the differing behavior between the two example prompts.

## Cross-tool comparison

**Q19.** A developer needs the model to answer questions using only the company's internal, uploaded compliance manual, with citations to specific matched passages. Which tool is most appropriate, and why NOT web_search?

A. web_search — because it can find any content, including internal manuals published online
B. file_search — because it grounds responses in your own uploaded/indexed documents with semantic retrieval and citation support, whereas web_search only accesses public internet content
C. function — because functions can retrieve any data source
D. code_interpreter — because it can read uploaded files directly

**Answer:** B — file_search is specifically designed for document-grounded answers from uploaded files with citations, while web_search explicitly retrieves information from the public Internet, not private/internal documents. code_interpreter (D) can process uploaded files for computation but isn't designed for semantic search/grounding over document content.

**Q20.** Which tool requires your OWN application code to execute logic and is the only one of the four where the model cannot autonomously produce the final data itself (code, search results, or documents) without your app performing an intermediate step?

A. code_interpreter, since it runs in a sandbox
B. web_search, since it depends on external content
C. function, since the model only emits a structured call that your application must run before returning output
D. file_search, since it depends on a vector store

**Answer:** C — Unlike code_interpreter (executes code within the platform's sandbox) or web_search/file_search (retrieval happens within the platform), the function tool explicitly requires "Your app runs logic" as a mandatory step — the model cannot get the function's result without your application executing it and returning `function_call_output`.
