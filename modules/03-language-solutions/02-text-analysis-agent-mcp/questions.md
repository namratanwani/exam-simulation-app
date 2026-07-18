# Practice questions — Develop a text analysis agent with the Azure Language MCP server

## Unit 1: Introduction

**Q1.** What is the current release status of the Azure Language MCP server, as explicitly stated in this module?
A. Generally available (GA)
B. Public preview
C. Private preview (invite-only)
D. Deprecated in favor of REST APIs
**Answer:** B — The module states: "The Azure Language MCP server is currently in public preview. Details described in this module are subject to change."

**Q2.** What is the primary benefit of exposing Azure Language capabilities through an MCP server rather than calling REST APIs/SDK methods directly for each capability?
A. MCP calls are always faster than REST calls.
B. The agent can dynamically select and call the appropriate tool per user request without you writing per-capability routing code.
C. MCP eliminates the need for authentication.
D. MCP automatically translates all output into English.
**Answer:** B — The module states this approach "lets the agent dynamically select and call the appropriate language tool based on a user's request, without you needing to write specific code for each capability."

## Unit 2: Understand the Azure Language MCP server

**Q3.** In MCP's client-server architecture, which component is the application that runs the agent (e.g., Microsoft Foundry or a custom app)?
A. Server
B. Host
C. Client
D. Gateway
**Answer:** B — Definitions given: Host = the application that runs the agent; Client = component within the host managing MCP server connections; Server = program exposing tools/resources/prompts.

**Q4.** Which term describes an agent querying an MCP server at runtime to learn what tools are available, rather than having tool knowledge hardcoded?
A. Static tool binding
B. Dynamic tool discovery
C. Lazy tool caching
D. Runtime schema validation
**Answer:** B — Explicitly named "dynamic tool discovery" in the module.

**Q5.** Which of the following are listed as capabilities of the Azure Language MCP server in this module? (Choose three.)
A. Named Entity Recognition
B. Text Analytics for Health
C. Sentiment Analysis
D. PII Redaction
E. Key Phrase Extraction
**Answer:** A, B, D — The four listed capabilities are Language Detection, Named Entity Recognition, PII Redaction, and Text Analytics for Health. Sentiment Analysis and Key Phrase Extraction are explicitly called out as deprecated capabilities, not part of the current MCP tool catalog.

**Q6.** Which Azure Language MCP capability is new/unique to this module (i.e., not covered in the basic "Analyze text with Azure Language" module) and extracts diagnoses, medications, and symptoms from clinical text?
A. PII Redaction
B. Language Detection
C. Text Analytics for Health
D. Named Entity Recognition
**Answer:** C — Text Analytics for Health is described as extracting and labeling medical entities such as diagnoses, medications, and symptoms from clinical text, and is not part of the earlier module's coverage.

**Q7.** What is the correct URL pattern (including API version) for the remote Azure Language MCP server endpoint?
A. `https://{foundry-resource-name}.cognitiveservices.azure.com/language/mcp?api-version=2025-11-15-preview`
B. `https://{foundry-resource-name}.services.ai.azure.com/mcp/language`
C. `https://api.cognitive.microsoft.com/language/v3.1/mcp`
D. `https://{foundry-resource-name}.openai.azure.com/language/mcp`
**Answer:** A — This is the exact endpoint format given in the module.

**Q8.** Besides the remote hosted MCP endpoint, what alternative deployment option does Azure Language also provide for the MCP server?
A. A Docker container only available on Azure Container Apps
B. A local MCP server you can self-host in your own environment
C. No alternative — remote is the only option
D. A Logic Apps connector
**Answer:** B — The module notes "Azure Language also provides a local MCP server that you can host in your own environment," pointing to the Azure-Samples/ai-language-samples repo for setup guidance.

## Unit 3: Connect and use the Language MCP server with an agent

**Q9.** In the Foundry portal, where do you go to connect the Azure Language MCP server to an agent?
A. The **Deployments** page
B. The **Tools** page → **Connect a tool** → **Azure Language in Foundry Tools**
C. The **Evaluation** page
D. The **Data** page
**Answer:** B — Steps given: navigate to Tools page, select Connect a tool, choose Azure Language in Foundry Tools from the catalog.

**Q10.** When configuring the Azure Language tool connection in the Foundry portal, what authentication credential header is specified?
A. `Authorization: Bearer`
B. `Ocp-Apim-Subscription-Key`
C. `x-api-key`
D. `X-MS-Client-Secret`
**Answer:** B — The module specifies "Credential (`Ocp-Apim-Subscription-Key`): The key for your Foundry project."

**Q11.** The first time an agent in the playground attempts to use a connected MCP tool, what happens?
A. It executes silently with no user interaction.
B. You're prompted to approve the tool usage (single-use, or "always approve" for that tool set).
C. The request is automatically rejected until you edit agent instructions.
D. The playground disables MCP tools by default and requires a portal setting change.
**Answer:** B — The module states you're prompted to approve, either once or via "Always approve all Azure Language in Foundry Tools tools."

**Q12.** Which SDK packages are used to build a Python client application that invokes a Foundry agent programmatically, per this module?
A. `azure-ai-textanalytics` and `azure-core`
B. `azure-ai-projects` and `azure-identity`
C. `openai` and `azure-mgmt-cognitiveservices`
D. `azure-ai-agents` and `azure-storage-blob`
**Answer:** B — The module states: "To build a client application, you use the `azure-ai-projects` and `azure-identity` packages."

**Q13.** In the client application pattern described, which method on the project client returns an OpenAI-compatible client used to call `responses.create()`?
A. `get_chat_client()`
B. `get_openai_client()`
C. `create_openai_session()`
D. `as_openai()`
**Answer:** B — Step 2 of the pattern: "Get an OpenAI client from the project client by calling `get_openai_client()`."

**Q14.** How do you specify which Foundry agent should handle a `responses.create()` call in the client code sample?
A. Pass an `agent_id` query parameter in the URL.
B. Pass an `extra_body={"agent_reference": {"name": ..., "type": "agent_reference"}}` argument.
C. Set an environment variable `FOUNDRY_AGENT_NAME`.
D. Call `client.set_active_agent(name)` before `responses.create()`.
**Answer:** B — Shown verbatim in the code sample: `extra_body={"agent_reference": {"name": "Text-Analysis-Agent", "type": "agent_reference"}}`.

**Q15.** Which attribute of the `responses.create()` return value contains the agent's final natural-language answer?
A. `response.text`
B. `response.output_text`
C. `response.content`
D. `response.result`
**Answer:** B — `print(response.output_text)` is shown in the sample.

**Q16.** To inspect exactly which MCP tools an agent called (and with what arguments) for a given request, what should you do?
A. Call `response.model_dump_json()` and inspect the full response JSON.
B. Check the Azure Activity Log.
C. There's no way to see this — tool calls are opaque.
D. Re-run the request with `verbose=True`.
**Answer:** A — The module states you "can also inspect the full response JSON (using `response.model_dump_json()`) to see which tools the agent called."

**Q17.** When defining an MCP tool connection directly in code (rather than via the Foundry portal), which SDK class do you use, and from which package?
A. `MCPConnector` from `azure-ai-agents`
B. `MCPTool` from `azure-ai-projects.models`
C. `ToolDefinition` from `azure-ai-textanalytics`
D. `RemoteToolClient` from `azure-identity`
**Answer:** B — Code sample: `from azure.ai.projects.models import MCPTool`.

**Q18.** In the `MCPTool` code sample, which parameter restricts which specific Language tools the agent is allowed to invoke?
A. `server_label`
B. `require_approval`
C. `allowed_tools`
D. `tool_scope`
**Answer:** C — The module states: "You can also use the `allowed_tools` property on `MCPTool` to restrict which specific Language tools the agent can call."

**Q19.** What value is used for `require_approval` in the `MCPTool` code sample?
A. `"never"`
B. `"once"`
C. `"always"`
D. `"auto"`
**Answer:** C — Code sample: `require_approval="always"`.

**Q20.** A user asks the agent: "What language is this article in, and what people does it mention?" Based on the module's tool-selection description, what is the most likely agent behavior?
A. It refuses because a single MCP tool can't cover two tasks.
B. It calls only the named entity recognition tool and ignores the language question.
C. It calls both the language detection tool and the named entity recognition tool in the same turn, then combines the results.
D. It requires two completely separate chat sessions, one per tool.
**Answer:** C — The module gives this exact example: "the agent might call both the language detection tool and the named entity recognition tool in the same turn."

## Unit 4: Exercise

**Q21.** In the hands-on exercise for this module, which of the following tasks are performed? (Choose two.)
A. Creating an AI agent in Microsoft Foundry and connecting it to the Azure Language MCP server
B. Training a custom NER model from scratch
C. Building a Python client application that performs entity recognition and PII redaction via the agent
D. Configuring Azure Kubernetes Service for the agent runtime
**Answer:** A, C — The exercise description states you create an agent, connect it to the Azure Language MCP server, test it in the playground, and build a Python client that performs tasks like entity recognition and PII redaction. Custom model training and AKS configuration are not part of this exercise.
