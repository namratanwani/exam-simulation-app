# Develop a speech agent with the Azure Speech MCP server

Source: https://learn.microsoft.com/en-us/training/modules/develop-speech-agent-speech-mcp/

Module info: 6 Units, Intermediate level, roles: AI Engineer / Developer, products: Microsoft Foundry, Azure Speech in Foundry Tools.

> The **Azure Speech MCP server is in public preview** — details subject to change (explicitly noted, same as the Language MCP server).

## Learning objectives

- Describe the Azure Speech MCP server and the speech capabilities it exposes.
- Explain how MCP enables dynamic tool discovery and selection by AI agents.
- Set up Azure Blob Storage for audio file input and output.
- Connect the Azure Speech MCP server to an agent in Microsoft Foundry.
- Build a Python client application that invokes an agent to perform speech tasks.

Prerequisites: familiarity with Azure services and Foundry portal; experience deploying generative AI models in Foundry; some Python familiarity.

## Exam relevance

Maps to:
- **Implement text analysis solutions (10–15%)** → "Implement speech solutions" → "Implement workflows to convert speech to text and text to speech for agentic interactions" and "Integrate speech as an agent modality, including custom speech models."
- **Implement generative AI and agentic solutions (30–35%)** → "Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions."
- Also relevant to "Configure security, including managed identity, private networking, keyless credentials, and role policies" — this module is explicit about SAS URL/key security best practices.

**Key distinguishing factor vs. the Language MCP server (module 2):** The **Speech MCP server requires Azure Blob Storage** (a SAS URL for a blob container) because it works with audio files, whereas the Language MCP server (text-only) has no such storage dependency. The Speech MCP server exposes only **two** tool capabilities (speech-to-text "Recognize" and text-to-speech "Synthesize") vs. the Language MCP server's **four** (Language Detection, NER, PII Redaction, Text Analytics for Health).

## Unit 1: Introduction

Azure Speech in Foundry Tools provides speech-to-text and text-to-speech capabilities integrable into AI apps — transcribe audio to text, synthesize natural-sounding speech from text. Callable directly via Speech SDK/REST, OR exposed to an agent via the **Azure Speech Model Context Protocol (MCP) server** — lets the agent handle speech tasks from natural-language requests without per-operation routing code.

Example scenario: processing customer support calls — transcribe recorded calls for analysis, generate audio responses for playback — one MCP tool connection instead of separate transcription/synthesis integrations.

## Unit 2: Understand the Azure Speech MCP server

### What is MCP? (same definitions as the Language MCP module)

MCP = open protocol defining how AI agents interact with external tools/data sources/services. Client-server architecture:
- **Host** — application running the agent (Microsoft Foundry or custom app).
- **Client** — component within host managing MCP server connections/communication.
- **Server** — program exposing tools/resources/prompts an agent can discover/call.

**Dynamic tool discovery**: agent queries the MCP server at runtime for available tools rather than hardcoding tool knowledge. Advantage: tools can be added/updated/removed server-side without modifying the agent.

> Cross-reference: separate **"Integrate MCP Tools with Azure AI Agents"** module for general MCP architecture/custom tool integration.

### Azure Speech MCP server capabilities

Exposes **two core** speech capabilities:

| Capability | Description |
|---|---|
| **Speech-to-text (Recognize)** | Converts audio files to text using advanced speech recognition. Supports **WAV, MP3, OGG, FLAC, MP4, M4A, AAC**, and other common audio formats. Options: language selection, phrase hints for improved accuracy, profanity filtering, detailed or simple output formats. |
| **Text-to-speech (Synthesize)** | Converts text into natural-sounding audio using neural TTS voices. Supports multiple languages/voices (e.g., `en-US-JennyNeural`, `en-GB-SoniaNeural`). Output formats: WAV, MP3, others. |

Agent tool selection example: "Transcribe this audio file" → speech-to-text tool; "Generate speech from this text" → text-to-speech tool.

### How the agent selects tools

1. User sends a prompt.
2. Agent analyzes prompt, determines which speech task is needed.
3. Agent checks available MCP tools/descriptions for best match.
4. Agent calls the selected tool via MCP server, passing relevant input (audio file URL or text).
5. MCP server processes via Azure Speech, returns results (transcribed text or a link to an audio file).
6. Agent presents results in a natural-language response.

No manual routing logic needed to decide speech-to-text vs. text-to-speech.

### Storage requirements (unique to Speech MCP vs. Language MCP)

Because it works with **audio files**, the Speech MCP server requires an **Azure Storage account**:
- **Text-to-speech**: generated audio files are saved to an **Azure Blob Storage container**; the agent's response includes a link to the file.
- **Speech-to-text**: can transcribe from a **publicly accessible URL** or from an **Azure Blob Storage container accessed with a SAS URL**.

When connecting the Speech MCP server, you provide a **SAS URL** for a blob container — grants the MCP server read/write permission on that container.

> **Important (security):** Treat SAS URLs as secrets. Use the shortest practical expiry time, scope to a single container, never embed in source code/agent prompts/chat transcripts.

### Prerequisites

- An **Azure subscription**.
- A **Foundry resource and project** — need **Contributor or Owner** role on the resource group. Foundry resource includes speech capabilities.
- An **Azure Storage account** with a blob container for audio files.
- A **SAS URL** for the blob container with **read, write, add, create, and list** permissions.

### Security considerations

Uses **key-based authentication** — you provide your resource key and a blob container SAS URL. Best practices:
- Store keys/SAS URLs in a secure secret store; rotate regularly.
- Avoid embedding keys/SAS URLs in source code, scripts, or docs.
- Use shortest practical SAS expiry; scope to minimum required resource.
- Rotate keys immediately if exposure is suspected.

## Unit 3: Connect and use the Speech MCP server with an agent

### Set up Azure Blob Storage

1. In the Azure portal, create a new **Azure Storage account** (or use existing).
2. In the storage account, expand **Data storage** → select **Containers**.
3. Create a new container (example name: **files**) for audio files.
4. Generate a **SAS token** for the container with permissions: **Read, Add, Create, Write, and List**. Set shortest practical expiry.

> Important: copy and securely store the generated SAS URL — needed when connecting the Speech MCP server.

### Create a Foundry project and agent

1. In the Foundry portal (ai.azure.com), create/use a project.
2. Deploy a model (example: **gpt-4.1**) for agent reasoning/responses.
3. Create an agent with instructions, e.g.:
   ```
   You are an AI agent that uses the Azure AI Speech tool to transcribe and generate speech.
   ```

### Connect the Azure Speech MCP server (via Foundry portal)

Via the **Tools** page:
1. Select **Tools** in navigation pane.
2. **Connect a tool** → choose **Azure Speech in Foundry Tools** from the catalog.
3. Configure:
   - **Foundry resource name** — e.g., `myproject-resource`.
   - **Bearer** (`Ocp-Apim-Subscription-Key`) — the key for your Foundry project.
   - **X-Blob-Container-Url** — the SAS URL for your blob container.
4. Wait for connection creation → **Use in an agent** → choose your agent.

> **Distinguishing auth detail vs. Language MCP:** the Language MCP tool connection used a field labeled **"Authentication: Key-based"** with credential header `Ocp-Apim-Subscription-Key`; the Speech MCP tool connection labels the same header field **"Bearer"** and additionally requires the **`X-Blob-Container-Url`** header for the SAS URL — an extra configuration field not present for Language MCP.

Tip: find the project key on the project home page in the Foundry portal.

### Test in the agent playground

**Test text-to-speech:**
```
Generate "To be or not to be, that is the question." as speech
```
First MCP tool use → approval prompt (or select **"Always approve all Azure Speech MCP Server tools"**). Response includes a link to the generated audio file in your blob container.

**Test speech-to-text:**
```
Transcribe the file at https://example.com/audio/meeting-recording.wav
```
Can use a publicly accessible URL or a SAS URL to a blob container file. Agent calls the speech-to-text tool, returns transcribed text.

### Customizing speech output (prompt-level options)

- **Voice selection** — specify a neural voice, e.g., `en-GB-SoniaNeural`, `en-US-JennyNeural`.
- **Language** — specify recognition/synthesis language, e.g., `es-ES` for Spanish.
- **Phrase hints** — domain-specific terms to improve transcription accuracy, e.g., "Azure, OpenAI, Cognitive Services."
- **Profanity filtering** — request `masked`, `removed`, or `raw` profanity handling during transcription.

Example prompt combining options:
```
Synthesize "Better a witty fool, than a foolish wit!" as speech using the voice "en-GB-SoniaNeural".
```

### Build a client application

Same pattern as the Language MCP module: Foundry SDK via **OpenAI Responses API**, packages `azure-ai-projects` and `azure-identity`.

1. Create **`AIProjectClient`** using Foundry project endpoint + **`DefaultAzureCredential`**.
2. Get OpenAI client via **`get_openai_client()`**.
3. Call **`responses.create()`**, referencing the agent by name via `extra_body`.

```python
response = openai_client.responses.create(
    input=[{"role": "user", "content": user_prompt}],
    extra_body={
        "agent_reference": {
            "name": "Speech-Agent",
            "type": "agent_reference"
        }
    },
)

print(response.output_text)
```

For text-to-speech requests, `output_text` includes a link to the generated audio file in your blob container.

### Connect the MCP server in code

```python
from azure.ai.projects.models import MCPTool

mcp_tool = MCPTool(
    server_label="azure-speech",
    server_url="https://{foundry-resource-name}.cognitiveservices.azure.com/speech/mcp",
    require_approval="always",
)
```

> **Exam-relevant detail:** the Speech MCP server URL shown here (`.../speech/mcp`) has **no `api-version` query parameter** in this module's example, unlike the Language MCP server URL which explicitly included `?api-version=2025-11-15-preview`. Note this discrepancy if a question tests exact endpoint format recall.

## Unit 4: Exercise — Use Azure Speech in an agent

Hands-on exercise (~30 minutes): create an AI agent in Microsoft Foundry, connect it to the Azure Speech MCP server, test both text-to-speech and speech-to-text capabilities in the agent playground, and build a Python client application that interacts with the agent. Requires an Azure subscription with administrative access. Delivered via external lab launch link.

## Unit 5: Knowledge check

Standard graded quiz — interactive only, no extractable content.

## Unit 6: Summary

Recap — you learned how to:
- Describe the Azure Speech MCP server and the speech capabilities it exposes.
- Explain how MCP enables dynamic tool discovery and selection by AI agents.
- Set up Azure Blob Storage for audio file input and output.
- Connect the Azure Speech MCP server to an agent in Microsoft Foundry.
- Build a Python client application that invokes an agent with speech tools using the Foundry SDK.

### Learn more links
- Azure Speech in Foundry Tools for the Azure MCP Server (`/en-us/azure/developer/azure-mcp-server/tools/ai-services-speech`)
- Connect to Model Context Protocol servers (`/en-us/azure/foundry/agents/how-to/tools/model-context-protocol`)
- Azure AI Projects SDK for Python (`/en-us/python/api/overview/azure/ai-projects-readme`)
- Azure Speech service overview (`/en-us/azure/ai-services/speech-service/overview`)
