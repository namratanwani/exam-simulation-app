# Practice questions — Develop a text analysis agent with the Azure Language MCP server

## Unit 1: Introduction

**Q1.** What is the current release status of the Azure Language MCP server, as explicitly stated in this module?
A. Generally available (GA)
B. Public preview
C. Private preview (invite-only)
D. Deprecated in favor of REST APIs
**Answer:** B — The module states: "The Azure Language MCP server is currently in public preview. Details described in this module are subject to change."

**Q2.** What is the primary benefit of exposing Azure Language capabilities through an MCP server rather than calling REST APIs/SDK methods directly for each capability?
A. MCP calls are always faster than REST calls because they use a persistent binary transport layer.
B. The agent can dynamically select and call the appropriate tool per user request without you writing per-capability routing code.
C. MCP eliminates the need for authentication since tool servers implicitly trust the connecting host.
D. MCP automatically translates all tool output into English before returning it to the agent.
**Answer:** B — The module states this approach "lets the agent dynamically select and call the appropriate language tool based on a user's request, without you needing to write specific code for each capability."

**Q3.** In the module's example scenario for analyzing multilingual customer feedback, which tasks are performed through a single MCP tool connection instead of separate integrations?
A. Detect language, identify people/places mentioned, and redact personal details
B. Translate the feedback into English and generate an executive summary
C. Classify sentiment and generate a suggested reply email draft for support staff
D. Detect language and generate a formatted PDF report for stakeholders
**Answer:** A — The module's example scenario is "analyzing multilingual customer feedback — detect language, identify people/places mentioned, redact personal details — all through a single MCP tool connection instead of separate integrations."

## Unit 2: Understand the Azure Language MCP server

**Q4.** In MCP's client-server architecture, which component is the application that runs the agent (e.g., Microsoft Foundry or a custom app)?
A. Server
B. Host
C. Client
D. Gateway
**Answer:** B — Definitions given: Host = the application that runs the agent; Client = component within the host managing MCP server connections; Server = program exposing tools/resources/prompts.

**Q5.** Which term describes an agent querying an MCP server at runtime to learn what tools are available, rather than having tool knowledge hardcoded?
A. Static tool binding
B. Dynamic tool discovery
C. Lazy tool caching
D. Runtime schema validation
**Answer:** B — Explicitly named "dynamic tool discovery" in the module.

**Q6.** Which of the following are listed as capabilities of the Azure Language MCP server in this module? (Choose three.)
A. Named Entity Recognition
B. Text Analytics for Health
C. Sentiment Analysis
D. PII Redaction
E. Key Phrase Extraction
**Answer:** A, B, D — The four listed capabilities are Language Detection, Named Entity Recognition, PII Redaction, and Text Analytics for Health. Sentiment Analysis and Key Phrase Extraction are explicitly called out as deprecated capabilities, not part of the current MCP tool catalog.

**Q7.** Which Azure Language MCP capability is new/unique to this module (i.e., not covered in the basic "Analyze text with Azure Language" module) and extracts diagnoses, medications, and symptoms from clinical text?
A. PII Redaction (structured data)
B. Language Detection
C. Text Analytics for Health
D. Named Entity Recognition
**Answer:** C — Text Analytics for Health is described as extracting and labeling medical entities such as diagnoses, medications, and symptoms from clinical text, and is not part of the earlier module's coverage.

**Q8.** What is the correct URL pattern (including API version) for the remote Azure Language MCP server endpoint?
A. `https://{foundry-resource-name}.cognitiveservices.azure.com/language/mcp?api-version=2025-11-15-preview`
B. `https://{foundry-resource-name}.services.ai.azure.com/mcp/language?api-version=2024-08-01`
C. `https://api.cognitive.microsoft.com/language/v3.1/mcp?api-version=3.1-preview.1`
D. `https://{foundry-resource-name}.openai.azure.com/language/mcp?api-version=2024-10-01-preview`
**Answer:** A — This is the exact endpoint format given in the module.

**Q9.** Besides the remote hosted MCP endpoint, what alternative deployment option does Azure Language also provide for the MCP server?
A. A Docker container only available on Azure Container Apps
B. A local MCP server you can self-host in your own environment
C. No alternative — remote is the only option
D. A managed Logic Apps connector hosted in the same resource group
**Answer:** B — The module notes "Azure Language also provides a local MCP server that you can host in your own environment," pointing to the Azure-Samples/ai-language-samples repo for setup guidance.

**Q10.** What is the key advantage of MCP's dynamic tool discovery model, per this module?
A. Tools can be added, updated, or removed server-side without modifying the agent, which always has the latest tool definitions
B. It removes the need for any authentication between the MCP client and server, since trust is implicit
C. It guarantees lower latency than direct SDK calls in every deployment region and network condition
D. It automatically caches all tool results for reuse across unrelated agent sessions and users
**Answer:** A — The module states: "This provides flexibility: tools can be added, updated, or removed on the server side without requiring changes to the agent. The agent always has access to the latest tool definitions, making it easier to maintain and scale your solution."

## Unit 3: Connect and use the Language MCP server with an agent

**Q11.** In the Foundry portal, where do you go to connect the Azure Language MCP server to an agent?
A. The **Deployments** page under model endpoint settings
B. The **Tools** page → **Connect a tool** → **Azure Language in Foundry Tools**
C. The **Evaluation** page under agent quality and safety metrics
D. The **Data** page under connected data sources and files
**Answer:** B — Steps given: navigate to Tools page, select Connect a tool, choose Azure Language in Foundry Tools from the catalog.

**Q12.** When configuring the Azure Language tool connection in the Foundry portal, what authentication credential header is specified?
A. `Authorization: Bearer`
B. `Ocp-Apim-Subscription-Key`
C. `x-api-key` (OpenAI-style header)
D. `X-MS-Client-Secret`
**Answer:** B — The module specifies "Credential (`Ocp-Apim-Subscription-Key`): The key for your Foundry project."

**Q13.** The first time an agent in the playground attempts to use a connected MCP tool, what happens?
A. It executes silently with no user interaction, logging the call only to the Azure Activity Log.
B. You're prompted to approve the tool usage (single-use, or "always approve" for that tool set).
C. The request is automatically rejected until you edit agent instructions.
D. The playground disables MCP tools by default and requires a portal setting change.
**Answer:** B — The module states you're prompted to approve, either once or via "Always approve all Azure Language in Foundry Tools tools."

**Q14.** Which SDK packages are used to build a Python client application that invokes a Foundry agent programmatically, per this module?
A. `azure-ai-textanalytics` and `azure-core`
B. `azure-ai-projects` and `azure-identity`
C. `openai` and `azure-mgmt-cognitiveservices`
D. `azure-ai-agents` and `azure-storage-blob`
**Answer:** B — The module states: "To build a client application, you use the `azure-ai-projects` and `azure-identity` packages."

**Q15.** In the client application pattern described, which method on the project client returns an OpenAI-compatible client used to call `responses.create()`?
A. `get_chat_client()`
B. `get_openai_client()`
C. `create_openai_session()`
D. `as_openai_client()`
**Answer:** B — Step 2 of the pattern: "Get an OpenAI client from the project client by calling `get_openai_client()`."

**Q16.** How do you specify which Foundry agent should handle a `responses.create()` call in the client code sample?
A. Pass an `agent_id` query parameter appended directly to the `responses.create()` request URL.
B. Pass an `extra_body={"agent_reference": {"name": ..., "type": "agent_reference"}}` argument.
C. Set an environment variable `FOUNDRY_AGENT_NAME` before initializing the project client.
D. Call `client.set_active_agent(name)` before `responses.create()`.
**Answer:** B — Shown verbatim in the code sample: `extra_body={"agent_reference": {"name": "Text-Analysis-Agent", "type": "agent_reference"}}`.

**Q17.** Which attribute of the `responses.create()` return value contains the agent's final natural-language answer?
A. `response.text` (legacy)
B. `response.output_text`
C. `response.content`
D. `response.result`
**Answer:** B — `print(response.output_text)` is shown in the sample.

**Q18.** To inspect exactly which MCP tools an agent called (and with what arguments) for a given request, what should you do?
A. Call `response.model_dump_json()` and inspect the full response JSON.
B. Check the Azure Activity Log for a record of the MCP tool invocation.
C. There's no way to see this — tool calls are opaque.
D. Re-run the request with an undocumented `verbose=True` parameter.
**Answer:** A — The module states you "can also inspect the full response JSON (using `response.model_dump_json()`) to see which tools the agent called."

**Q19.** When defining an MCP tool connection directly in code (rather than via the Foundry portal), which SDK class do you use, and from which package?
A. `MCPConnector` from `azure-ai-agents`
B. `MCPTool` from `azure-ai-projects.models`
C. `ToolDefinition` from `azure-ai-textanalytics`
D. `RemoteToolClient` from `azure-identity`
**Answer:** B — Code sample: `from azure.ai.projects.models import MCPTool`.

**Q20.** In the `MCPTool` code sample, which parameter restricts which specific Language tools the agent is allowed to invoke?
A. `server_label`
B. `require_approval`
C. `allowed_tools`
D. `tool_scope`
**Answer:** C — The module states: "You can also use the `allowed_tools` property on `MCPTool` to restrict which specific Language tools the agent can call."

**Q21.** What value is used for `require_approval` in the `MCPTool` code sample?
A. `"never"`
B. `"once"`
C. `"always"`
D. `"auto"`
**Answer:** C — Code sample: `require_approval="always"`.

**Q22.** A user asks the agent: "What language is this article in, and what people does it mention?" Based on the module's tool-selection description, what is the most likely agent behavior?
A. It refuses because a single MCP tool can't cover two tasks and asks the user to split the request.
B. It calls only the named entity recognition tool and silently ignores the language detection question.
C. It calls both the language detection tool and the named entity recognition tool in the same turn, then combines the results.
D. It requires two completely separate chat sessions, one per tool, since MCP can't combine them.
**Answer:** C — The module gives this exact example: "the agent might call both the language detection tool and the named entity recognition tool in the same turn."

**Q23.** Where in the Foundry portal do you find the project key needed for the `Ocp-Apim-Subscription-Key` credential when connecting the Azure Language MCP tool?
A. The project home page in the Foundry portal
B. The Azure Portal's Key Vault blade
C. The agent's System Instructions field in the playground
D. The MCP server's own admin console
**Answer:** A — The module's tip: "find the project key on the project home page in the Foundry portal."

**Q24.** When inspecting the full response JSON via `response.model_dump_json()`, which literal MCP tool names does the module show as having been called?
A. `extract_named_entities_from_text` and `detect_language_from_text`
B. `ner_tool` and `lang_detect_tool` (shorthand aliases)
C. `RecognizeEntities` and `DetectLanguage` (the older SDK method names)
D. `text_analytics_ner` and `text_analytics_language`
**Answer:** A — The module states the full response JSON reveals which tools were called, "e.g., `extract_named_entities_from_text` or `detect_language_from_text` — with arguments and per-call results."

**Q25.** In the agent playground (as opposed to inspecting code/JSON), how can you verify which MCP tools were used to produce a given agent response?
A. Review the Logs pane, which shows each MCP tool call, the input sent, and the result returned
B. There is no way to verify tool usage from the playground; you must inspect raw JSON
C. Open the browser's network tab, since the playground doesn't expose this
D. Re-run the prompt with a `--debug` flag appended to the playground request
**Answer:** A — The module states: "After the agent responds, you can review the Logs pane to see details about which tools were used" including the input sent and the result returned.

**Q26.** What `server_label` value does the module's `MCPTool` code sample use for the Azure Language MCP connection?
A. `"language-mcp"`
B. `"azure-language"`
C. `"foundry-language-tool"`
D. `"language-server"`
**Answer:** B — Code sample: `mcp_tool = MCPTool(server_label="azure-language", ...)`.

## Unit 4: Exercise

**Q27.** In the hands-on exercise for this module, which of the following tasks are performed? (Choose two.)
A. Creating an AI agent in Microsoft Foundry and connecting it to the Azure Language MCP server
B. Training a custom NER model from scratch
C. Building a Python client application that performs entity recognition and PII redaction via the agent
D. Configuring Azure Kubernetes Service for the agent runtime
**Answer:** A, C — The exercise description states you create an agent, connect it to the Azure Language MCP server, test it in the playground, and build a Python client that performs tasks like entity recognition and PII redaction. Custom model training and AKS configuration are not part of this exercise.

## Scenario questions

**Q28.** You want your agent to be permitted to call only the PII redaction tool from the Azure Language MCP server — never NER or language detection — when connecting the server in code. Which `MCPTool` configuration achieves this?
A. Set `require_approval="never"` and rely on agent instructions alone
B. Use the `allowed_tools` property to restrict the tool set to the PII redaction tool
C. Create a separate MCP server instance exposing only PII redaction
D. There is no way to restrict tools; the agent always sees the full catalog
**Answer:** B — The module states `allowed_tools` on `MCPTool` "restrict[s] which specific Language tools the agent can call."

**Q29.** A teammate asks why they didn't have to write if/else routing code to decide whether to call NER vs. language detection for different user prompts. Which two module concepts explain this?
A. Dynamic tool discovery — the agent queries the MCP server for available tools/descriptions at runtime
B. The agent autonomously matches user intent to tool descriptions and can call multiple tools in one turn
C. Azure Language automatically merges all four capabilities into a single REST call
D. The Foundry portal generates routing code automatically at deployment time
**Answer:** A, B — Dynamic tool discovery means no hardcoded tool knowledge is needed, and the module's tool-selection walkthrough shows the agent analyzing the prompt, matching it to tool descriptions, and potentially calling multiple tools in one turn.

**Q30.** You're building a production client app that calls a Foundry agent connected to the Language MCP server. You want to avoid embedding a static API key in your app and instead rely on your Azure CLI login during local development, migrating to managed identity in production. Which credential should you pass to `AIProjectClient`?
A. `AzureKeyCredential`
B. `DefaultAzureCredential`
C. The `Ocp-Apim-Subscription-Key` header, set manually
D. A hardcoded `ManagedIdentityCredential` with no fallback
**Answer:** B — The module's client pattern creates the `AIProjectClient` using `DefaultAzureCredential`, which "uses Azure CLI credentials in dev" and transparently supports managed identity in Azure-hosted production environments.

**Q31.** You've connected the Azure Language MCP server both via the Foundry portal and want to also restrict tool access and require approval settings as code for repeatable deployments. Which combination of steps reflects the module's guidance?
A. Configure everything only via the portal; code-based configuration with `MCPTool` isn't supported for this MCP server in the current public preview release
B. Use `MCPTool` in code with `server_url` pointing at the `.cognitiveservices.azure.com/language/mcp` endpoint, `require_approval`, and `allowed_tools`, then pass it when creating the agent via SDK
C. Use `azure-ai-textanalytics` directly instead of MCP, since the SDK provides equivalent `allowed_tools` restriction semantics expressed as code
D. Store tool configuration in an `.env` file that the Foundry portal automatically reads and syncs into the SDK's `MCPTool` configuration on every deploy
**Answer:** B — The module shows connecting the MCP server in code as "an alternative to portal configuration" using `MCPTool` with `server_label`, `server_url`, `require_approval`, and `allowed_tools`, passed when creating the agent through the SDK.
