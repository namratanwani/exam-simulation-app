# Develop generative AI apps that use tools

Source: https://learn.microsoft.com/en-us/training/modules/use-generative-ai-tools/

## Learning objectives

After completing this module, you'll be able to:

- Describe the capabilities of generative AI tools.
- Use the code_interpreter tool to run code and analyze data.
- Use the web_search tool to retrieve real-time information from the internet.
- Use the file_search tool to access and analyze files.
- Use the function tool to run custom code.

Module info: Beginner level, 9 units, tagged AI Engineer / Developer / Microsoft Foundry. Prerequisites: familiarity with Microsoft Foundry and generative AI models; some programming experience.

## Exam relevance

- **Build generative applications by using Foundry** → "Design workflows, tool-augmented flows, and multistep reasoning pipelines" — the module's entire subject (code_interpreter, web_search, file_search, function tools).
- **Build generative applications by using Foundry** → "Implement retrieval-augmented generation (RAG) in an application" — file_search tool + vector stores.
- **Build agents by using Foundry** → "Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions" — function tool, file_search.
- **Choose the appropriate Foundry services for generative AI and agents** → "Choose appropriate memory, tool, and knowledge integration services for agent solutions" — explicit distinction drawn between file_search and Foundry IQ for enterprise-scale needs.

**IMPORTANT exam-trap terminology note**: The generic "tools" used in Responses API prompts (`code_interpreter`, `web_search`, `file_search`, `function`) are explicitly NOT the same thing as **Foundry Tools** (the suite of Azure AI APIs like Language, Speech, Translator, Document Intelligence, Content Understanding covered in Module 1). The module states this directly: "The use of tools in generative AI model prompts shouldn't be confused with Foundry Tools; which are Azure AI APIs that you can use in your applications and agents."

## Introduction

Generative AI models operate within a knowledge boundary — they can only reason about information in their training data. Integrating **tools** unlocks capabilities beyond the model alone.

Why tools matter:
- **Access real-time information** — fetch current data, weather, stock prices, API responses not in training data.
- **Take actions** — send emails, create database records, trigger workflows.
- **Ground responses in facts** — retrieve authoritative info to reduce incorrect information/improve accuracy.
- **Extend functionality** — connect to existing systems, databases, business logic.
- **Build intelligent workflows** — chain multiple operations for complex, multi-step processes.

This module focuses on specifying tools in prompts submitted by a **client application** (tool configuration managed by the client app itself — essentially a custom assistant within app logic). This is described as a stepping stone toward **agentic AI** solutions, where model + instructions + tools are encapsulated/persisted in a named **agent** (covered via the Microsoft Foundry Agents SDK in the separate "Develop AI agents on Azure" learning path).

## What are tools?

Microsoft Foundry Models includes models capable of using tools to find information or perform tasks. Tool support is used by specifying which tools the model can use in prompts submitted through the **OpenAI Responses API**.

Workflow: search Foundry Models for a model with tool-calling capability → deploy it → build client apps that use the Responses API to submit prompts, specifying available tools.

**Tool selection**: By default, the **model itself chooses when and which tool to use**, based on the prompt. You can configure tool selection rules and use the **Instructions** (system prompt) parameter to guide this choice.

### Commonly used Responses API tools
- **code_interpreter** — a Python environment where the model can generate and run code.
- **web_search** — lets the model find general information on the Internet, grounding responses in more current data than training data.
- **file_search** — lets the model search specific files you upload to a dedicated vector search index, grounding responses in specific knowledge.
- **function** — lets the model call custom functions in your application code.

Note: these are only *some* available tools; agentic AI tool development is a growing area (see OpenAI developer guide for full tool list).

### Specifying tools in the Responses API
Tools are specified as a JSON list in the `tools` parameter of `responses.create()`:
```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

response = client.responses.create(
    model={model_deployment},
    instructions="You are a helpful AI assistant.",
    input="Find me some information about vintage computers.",
    # Specify available tools as a JSON list
    tools=[
        { 
            "type": "{tool_type}",
            "{tool-specific-setting}": "{value}",
                ...
        },
        { 
            "type": "{another_tool_type}",
            "{tool-specific-setting}": "{value}",
                ...
        }
    ]
)
print(response.output_text)
```

## Use the code_interpreter tool

Provides the model a **Python runtime** to generate and run Python code dynamically during a conversation — transforming the model "from a thinker into a doer."

**Key features**: Dynamic Python execution (sandboxed), file handling (upload/process/download CSV, JSON, images), data analysis (calculations, stats, transformations), real-time feedback (model sees execution results and can iterate/fix errors), complex problem solving (math, simulations, logic puzzles).

**Common use cases**: Data Analysis (parse CSV, generate summary stats), Math & Physics (solve differential equations, simulate physics), File Conversion (JSON ↔ CSV), Prototyping (test algorithms before formal implementation).

**Example**:
```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Get response using the code_interpreter tool
response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
    input="What is the square root of 16?",
    tools=[{"type": "code_interpreter",
            "container": {"type": "auto"}}]
)
print(response.output_text)
```
Output: `The square root of 16 is 4.` — Inspecting the response object shows the model dynamically generated and ran code like:
```python
import math
square_root = math.sqrt(16)
square_root
```

**How it works**: 1) You include `code_interpreter` in the tools array. 2) Model analyzes whether code execution is needed. 3) Model generates Python code. 4) Code runs in a sandboxed environment with access to common libraries (**pandas**, **numpy**, **math**, etc.). 5) Results returned and incorporated into the response.

**Best practices**: Be specific about data format/expected output (many models internally call this the "**python tool**" — use that language in instructions); provide domain context; validate AI-generated code before production use; monitor costs (code execution adds tokens); leverage pre-installed libraries (pandas, numpy, matplotlib); the model can see errors and attempts to fix them automatically.

**Limitations**: Sandboxed with **no external network access**; some libraries may be unavailable; **timeout limits** apply to long-running operations; **memory constraints** — massive datasets may need streaming/chunking.

## Use the web_search tool

Gives the model access to **current, external information at runtime** instead of relying solely on training data — issues a search query, reviews sources, produces a grounded answer. Useful for frequently changing facts (pricing, product releases, policy updates, current events).

**Key features**: Live information retrieval, source-grounded responses, reduced hallucination risk, automatic query generation (model decides when/how to search), seamless single-flow UX.

**Common use cases**: Current Events (summarize breaking news), Market Research (compare product features/pricing), Policy Monitoring (check regulation changes), Fact Verification (validate claims against public sources).

**Example**:
```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant. Use web search when current information is required.",
    input="What are three major announcements from Microsoft Build this week?",
    tools=[{"type": "web_search"}]
)
print(response.output_text)
```

**How it works**: 1) Include web_search tool in tools array. 2) Model evaluates if fresh data is needed. 3) Model issues one or more search queries. 4) Relevant pages selected/summarized. 5) Response combines search findings.

**Best practices**: Ask time-aware questions clearly ("latest", "current", date ranges); set expectations for reputable/official sources; request concise summaries; verify critical facts independently for high-stakes scenarios; track usage/latency (web retrieval increases response time and token usage).

**Limitations**: Results depend on public/indexable availability at query time; source quality varies (may need human review); retrieved content changes over time (repeated runs can differ); regional/policy/network restrictions may apply.

## Use the file_search tool

Lets the model retrieve relevant information from **your own uploaded documents** during a response — policy documents, manuals, contracts, internal knowledge bases — instead of relying only on general training data.

**Key features**: Document-grounded answers, semantic retrieval (by meaning, not just exact keywords), **vector store integration** (search across one or more indexed document collections), citations/transparency (matched results for debugging/traceability), better enterprise relevance.

**Common use cases**: Policy Q&A (HR policy PDFs), Support Assistants (troubleshooting guides), Legal Review (locate contract clauses), Knowledge Discovery (summarize from technical docs).

**Example**:
```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Create vector store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("expenses_policy.pdf", "rb")
)

# Get response using the file_search tool
response = client.responses.create(
    model=model_deployment,
    instructions="You are an AI assistant that provides information from HR policy documents.",
    input="What's the maximum amount I can claim for a taxi ride?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)
print(response.output_text)
```
Key API surface: `client.vector_stores.create(name=...)`, `client.vector_stores.files.upload_and_poll(vector_store_id=..., file=...)`, tool type `"file_search"` with `"vector_store_ids"` array, and the `include=["file_search_call.results"]` parameter to surface retrieval results for debugging.

**How it works**: 1) Upload documents to a vector store. 2) Include file_search in tools array with vector store IDs. 3) Model performs retrieval (searches indexed chunks). 4) Matching passages injected. 5) Model answers using retrieved document context.

**Best practices**: Use high-quality/current source files; write focused prompts; scope vector stores carefully (separate domains like HR/legal/finance); include retrieval results during development for troubleshooting; keep human review for critical workflows.

**Limitations**: Answer quality depends on document quality/coverage/chunk relevance; very large/mixed-domain stores return less focused context; updated source files require re-indexing; retrieval improves grounding but doesn't replace human review for sensitive decisions.

**IMPORTANT distinguishing note (exam-relevant)**: file_search is good for grounding in a specific set of documents/data files. For **enterprise-scale agents needing large quantities of data across multiple data stores**, the module recommends using the **Foundry IQ** knowledge store solution with a Microsoft Foundry agent instead — a key exam distinction between "quick document grounding via file_search" vs. "centralized, multi-source enterprise knowledge via Foundry IQ."

## Use the function tool

Also called **function calling** — lets the model decide when to call **developer-defined functions** to retrieve data or trigger actions. Critically: **the model does NOT run your business logic directly**. It returns a structured function-call request; your application code runs the function; you pass the output back to the model.

**Key features**: Structured tool calls (explicit function-call requests), developer-controlled execution, reliable integration pattern (APIs, internal services, utilities), multi-turn orchestration (return tool output, model continues reasoning), grounded responses with live system-generated data.

**Common use cases**: System Integration (call internal API for account/order details), Task Automation (trigger ticket creation, notifications), Data Lookup (query business rules/reference tables before answering).

**Example** (exposes a `get_time` function):
```python
import time
from openai import OpenAI

def get_time():
    return f"The time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"

def main():
    client = OpenAI(
        base_url={openai_endpoint},
        api_key={auth_key_or_token}
    )

    function_tools = [
        {
            "type": "function",
            "name": "get_time",
            "description": "Get the current time"
        }
    ]

    messages = [
        {"role": "developer", "content": "You are an AI assistant that provides information."},
    ]

    while True:
        prompt = input("\nEnter a prompt (or type 'quit' to exit)\n")
        if prompt.lower() == "quit":
            break

        messages.append({"role": "user", "content": prompt})

        response = client.responses.create(
            model=model_deployment,
            input=messages,
            tools=function_tools
        )

        messages += response.output

        for item in response.output:
            if item.type == "function_call" and item.name == "get_time":
                current_time = get_time()
                messages.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": current_time
                })

                response = client.responses.create(
                    model=model_deployment,
                    instructions="Answer only with the tool output.",
                    input=messages,
                    tools=function_tools
                )

        print(response.output_text)

if __name__ == '__main__':
    main()
```
Note the message role `"developer"` used for the system-level prompt in this function-calling example (distinct from `"system"` role seen elsewhere — both patterns appear in Microsoft's examples). Function-call items have `type == "function_call"`, `name`, and `call_id`; you respond with a `{"type": "function_call_output", "call_id": ..., "output": ...}` message appended to the conversation.

This example uses a single parameterless function; you can configure multiple functions, with or without parameters.

**How it works**: 1) Define tools — provide function definitions in tools array. 2) Model evaluates prompt for whether a function call is needed. 3) Model emits a function call (name + call metadata). 4) Your app runs the matching function. 5) You return a `function_call_output` item with the result. 6) Model incorporates tool results into the final answer.

**Best practices**: Keep tools focused (small, single-purpose functions); validate function inputs (never trust tool arguments blindly in production); handle errors safely (clear error outputs the model can reason about); log tool usage (calls, latency, failure rates); limit sensitive operations (require explicit authorization for high-impact actions).

**Limitations**: Model requests calls but YOUR app must run them; incorrect/unexpected arguments can occur and need validation; tool latency increases end-to-end response time; final outputs still need review for critical decisions.

## Exercise — Create a generative AI chat app that uses tools

Hands-on lab applying code_interpreter, web_search, file_search, and function tools in a Foundry-based chat application (exercise unit; no additional distinct conceptual content beyond what's covered in the preceding units).

## Cross-tool comparison (exam-critical distinctions)

| Tool | Grounds responses in | Execution location | Key risk/limitation |
|---|---|---|---|
| `code_interpreter` | Dynamically generated/executed Python code | Sandboxed cloud Python runtime (no network access) | Timeouts, memory constraints |
| `web_search` | Live public internet content | External web (search API) | Source quality varies; results change over time |
| `file_search` | Your uploaded documents (vector store) | Indexed vector search index | Quality depends on document coverage/chunking; needs re-indexing on updates |
| `function` | Your custom application code/APIs | Your own application (developer-controlled) | Model can't execute logic itself; requires developer-side validation |

All four are specified via the `tools` array parameter of `responses.create()` in the OpenAI Responses API. Do NOT confuse these prompt-level "tools" with **Foundry Tools** (Language, Speech, Translator, Document Intelligence, Content Understanding) — different concept entirely, despite similar naming.
