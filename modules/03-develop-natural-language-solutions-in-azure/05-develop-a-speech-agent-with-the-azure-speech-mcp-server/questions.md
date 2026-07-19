# Practice questions — Develop a speech agent with the Azure Speech MCP server

## Unit 1: Introduction

**Q1.** What is the release status of the Azure Speech MCP server, per this module?
A. Generally available
B. Public preview
C. Retired in favor of the classic Speech SDK
D. Not yet announced
**Answer:** B — "The Azure Speech MCP server is currently in public preview. Details described in this module are subject to change."

**Q2.** In the module's customer support scenario, what two speech tasks does the AI agent perform through a single MCP tool connection?
A. Sentiment analysis and translation of support transcripts
B. Transcribing recorded calls to text and generating audio responses for playback
C. Speaker diarization and PII redaction of caller identities
D. Language detection and named entity recognition on call transcripts
**Answer:** B — The module's example: "transcribe recorded calls to text for analysis, and generate audio responses that can be played back to customers."

## Unit 2: Understand the Azure Speech MCP server

**Q3.** How many core speech capabilities does the Azure Speech MCP server expose, and what are they?
A. Four: Speech-to-text, Text-to-speech, Speech Translation, Voice Live
B. Two: Speech-to-text (Recognize) and Text-to-speech (Synthesize)
C. Three: Recognize, Synthesize, and a separate Diarize tool
D. One: a single unified transcribe-and-synthesize tool
**Answer:** B — The module's table lists exactly two capabilities: Speech-to-text (Recognize) and Text-to-speech (Synthesize) — fewer than the four capabilities of the Language MCP server.

**Q4.** Which audio formats are explicitly listed as supported by the speech-to-text tool of the Azure Speech MCP server?
A. WAV, MP3, OGG, FLAC, MP4, M4A, AAC
B. WAV and MP3 only, per the documented format table
C. WMA, AIFF, and OPUS, per the documented format table
D. Any format, with automatic transcoding via FFmpeg
**Answer:** A — The module lists exactly: "Supports WAV, MP3, OGG, FLAC, MP4, M4A, AAC, and other common audio formats."

**Q5.** Which of these are listed as configurable options for the speech-to-text tool? (Choose three.)
A. Language selection
B. Phrase hints for improved accuracy
C. Profanity filtering
D. Speaker diarization toggle
E. Detailed or simple output formats
**Answer:** A, B, E (and C is also correct — this should be considered a 4-way "choose all that apply", but per instructions with three specified: A, B, C, E are all explicitly listed; D (speaker diarization toggle) is NOT mentioned) — The module states: "Includes options for language selection, phrase hints for improved accuracy, profanity filtering, and detailed or simple output formats." Speaker diarization is not listed as a configurable option in this module.

**Q6.** Why does the Azure Speech MCP server require an Azure Storage account, unlike the Azure Language MCP server?
A. Speech models are too large to run without cold storage caching of intermediate model weights and activations.
B. It works with audio files — generated speech is saved to Blob Storage, and transcription can read from Blob Storage via SAS URL.
C. Azure Speech requires storage for training custom acoustic models only, not for MCP calls.
D. It doesn't — this is a trick; both MCP servers require storage identically for their tool calls.
**Answer:** B — "Unlike text-only MCP tools, the Azure Speech MCP server works with audio files, which requires an Azure Storage account." Text-to-speech saves output to Blob Storage; speech-to-text can read from a SAS-URL-secured container or a public URL.

**Q7.** What permissions should the SAS token for the blob container have, per this module's prerequisites?
A. Read only, since the agent never writes generated audio
B. Read, write, add, create, and list
C. Read, execute, and delete
D. Full Storage Account Contributor RBAC role, not a SAS token
**Answer:** B — "A SAS URL for the blob container with read, write, add, create, and list permissions."

**Q8.** What Azure RBAC role(s) does the module say you need on the resource group to use the Azure Speech MCP server with an agent?
A. Reader, since the agent only queries existing resource configuration
B. Contributor or Owner
C. Storage Blob Data Reader only
D. Global Administrator
**Answer:** B — "A Foundry resource and project — you need Contributor or Owner role on the resource group."

**Q9.** Which security best practice does the module explicitly recommend for SAS URLs used with the Speech MCP server?
A. Embed them directly in agent prompts for convenience, since prompt content isn't logged anywhere by the platform.
B. Use the shortest practical expiry time, scope to a single container, and never embed them in source code, prompts, or transcripts.
C. Generate a SAS URL with no expiry so the agent never loses access mid-conversation, then rotate it quarterly.
D. Share the SAS URL via email to all team members for redundancy and easier debugging when the agent misbehaves.
**Answer:** B — "Treat SAS URLs as secrets. Use the shortest practical expiry time, scope them to a single container, and don't embed them in source code, agent prompts, or chat transcripts."

**Q10.** Which two example neural voice names does the module give for the text-to-speech capability of the Speech MCP server?
A. `en-US-JennyNeural` and `en-GB-SoniaNeural`
B. `en-US-AriaNeural` and `en-US-GuyNeural`
C. `en-US-Brian:DragonHDLatestNeural` and `en-GB-RyanNeural`
D. `es-ES-ElviraNeural` and `fr-FR-DeniseNeural`
**Answer:** A — The capabilities table states text-to-speech "supports multiple languages/voices (e.g., `en-US-JennyNeural`, `en-GB-SoniaNeural`)."

**Q11.** What output formats does the module mention for the Speech MCP server's text-to-speech capability?
A. WAV, MP3, and others
B. Only WAV, since it's the only format the synthesizer supports
C. Only MP3, since it's the most bandwidth-efficient format
D. FLAC and AAC exclusively, for lossless output quality
**Answer:** A — The capabilities table states "Output formats: WAV, MP3, others."

**Q12.** Besides scoping SAS URLs narrowly and using a short expiry, what does the module say you should do if you suspect a key or SAS URL has been exposed?
A. Wait until the natural expiry to avoid disrupting the agent
B. Rotate the key/SAS URL immediately
C. Only rotate the Foundry resource key, not the SAS URL
D. No action is needed since MCP servers are stateless
**Answer:** B — The security considerations list: "Rotate keys immediately if exposure is suspected."

## Unit 3: Connect and use the Speech MCP server with an agent

**Q13.** In Azure Storage account setup for this module, under which blade do you create a container?
A. Networking (private endpoint configuration)
B. Data storage → Containers
C. Access control (IAM)
D. Monitoring → Insights
**Answer:** B — "In the storage account, expand Data storage and select Containers."

**Q14.** When connecting the Azure Speech MCP server via the Foundry portal's Tools page, which configuration field is unique to the Speech MCP connection and NOT present for the Language MCP connection?
A. Foundry resource name
B. X-Blob-Container-Url
C. Authentication type
D. Agent selection
**Answer:** B — The Speech MCP tool connection requires an additional `X-Blob-Container-Url` field for the SAS URL, which has no equivalent in the Language MCP tool's connection settings (Foundry resource name, Authentication/credential, and agent selection are common to both).

**Q15.** What example model does the module suggest deploying for the agent's reasoning/response generation before connecting the Speech MCP server?
A. gpt-4o-mini
B. gpt-4.1
C. gpt-3.5-turbo
D. text-embedding-3-large
**Answer:** B — "Deploy a model (such as gpt-4.1) that your agent will use for reasoning and generating responses."

**Q16.** After the agent successfully performs text-to-speech via the Speech MCP tool in the playground, what does the response contain?
A. Raw audio bytes embedded directly in the chat response
B. A link to the generated audio file saved in your blob container
C. Only a confirmation message with no way to access the audio
D. An SSML transcript of the generated speech, for downstream editing
**Answer:** B — "The response includes a link to the generated audio file saved in your blob container. Select the link to listen to the synthesized speech."

**Q17.** Which of the following can be used as the source for a speech-to-text transcription request in the agent playground? (Choose two.)
A. A publicly accessible URL
B. A SAS URL pointing to a file in your blob container
C. A direct file upload attached to the chat message
D. A local file path on your development machine
**Answer:** A, B — "You can use a publicly accessible URL or a SAS URL pointing to a file in your blob container."

**Q18.** In a prompt to the Speech MCP agent, how would you request that profanity in a transcription be masked rather than removed or left raw?
A. By setting a `profanity_filter=True` flag in the client SDK code only — it cannot be requested via a natural-language prompt.
B. By specifying it in natural language in the prompt, since profanity filtering (masked, removed, or raw) is one of the tool's configurable options.
C. Profanity filtering isn't supported by the Speech MCP server at all in this current public preview release.
D. By appending `?profanity=masked` as a query string parameter directly on the audio file's SAS URL string.
**Answer:** B — The module lists "Profanity filtering: Request masked, removed, or raw profanity handling during transcription" as one of the prompt-level customizable options.

**Q19.** When connecting the Azure Speech MCP server via the Foundry portal's Tools page, the credential field for the same `Ocp-Apim-Subscription-Key` value is labeled differently than in the Language MCP connection. What is it labeled?
A. "Bearer"
B. "API Key"
C. "Subscription"
D. "Token"
**Answer:** A — The module notes: "the Language MCP tool connection used a field labeled 'Authentication: Key-based'... the Speech MCP tool connection labels the same header field 'Bearer.'"

**Q20.** Which prompt-level option would you use to improve transcription accuracy for domain-specific terms like "Azure, OpenAI, Cognitive Services"?
A. Profanity filtering
B. Phrase hints
C. Language selection
D. Output format selection
**Answer:** B — "Phrase hints: Domain-specific terms to improve transcription accuracy, for example, 'Azure, OpenAI, Cognitive Services.'"

**Q21.** To transcribe or synthesize Spanish speech via the Speech MCP agent, which prompt-level option would you specify, and what example value does the module give?
A. Language, e.g., `"es-ES"`
B. Voice, e.g., `"es-ES-Neural"`
C. A `locale` header, e.g., `"ES"`
D. Phrase hints, e.g., `"hola"`
**Answer:** A — "Language: Specify recognition/synthesis language, e.g., es-ES for Spanish."

**Q22.** Which packages are used to build a Python client application for the speech agent, matching the pattern from the Language MCP module?
A. `azure-cognitiveservices-speech` and `azure-storage-blob`
B. `azure-ai-projects` and `azure-identity`
C. `openai` and `azure-mgmt-storage`
D. `azure-ai-speech-agents` and `requests`
**Answer:** B — Same pattern as the Language MCP module: "you use the azure-ai-projects and azure-identity packages."

**Q23.** How is the target agent specified when calling `responses.create()` in the client code sample?
A. Via a `model` parameter set directly to the agent's deployment name
B. Via `extra_body={"agent_reference": {"name": "Speech-Agent", "type": "agent_reference"}}`
C. Via an `agent_id` header sent alongside every request to the endpoint
D. It's inferred automatically from the project endpoint URL at connection time
**Answer:** B — Shown verbatim in the code sample.

**Q24.** Which SDK class, from which package, is used to define the Speech MCP tool connection directly in code (rather than via the Foundry portal)?
A. `SpeechMCPConnector` from `azure-cognitiveservices-speech`
B. `MCPTool` from `azure.ai.projects.models`
C. `AgentToolBuilder` from `azure-ai-agents`
D. `RemoteTool` from `azure-identity`
**Answer:** B — `from azure.ai.projects.models import MCPTool`, same class used for the Language MCP server in the earlier module.

**Q25.** What is the `server_url` value shown in this module's `MCPTool` code sample for the Speech MCP server, and how does it differ from the Language MCP server's URL shown in an earlier module?
A. `https://{foundry-resource-name}.cognitiveservices.azure.com/speech/mcp` — with no `api-version` query parameter shown, unlike the Language MCP URL which included `?api-version=2025-11-15-preview`
B. They are identical except for the resource name; both share the exact same path structure and identical query parameters throughout the URL
C. The Speech MCP URL requires an extra `region` path segment that the Language MCP URL doesn't include anywhere in its structure at all, per this module
D. The Speech MCP URL uses the `.services.ai.azure.com` domain instead of the `.cognitiveservices.azure.com` domain used by the Language MCP endpoint
**Answer:** A — The module's code sample shows `server_url="https://{foundry-resource-name}.cognitiveservices.azure.com/speech/mcp"` without an `api-version` parameter, in contrast to the Language MCP module's URL which explicitly appended `?api-version=2025-11-15-preview`.

## Unit 4: Exercise

**Q26.** What does the hands-on exercise for this module have you build and test? (Choose two.)
A. An AI agent connected to the Azure Speech MCP server, tested for both text-to-speech and speech-to-text in the playground
B. A Python client application that interacts with the agent
C. A custom acoustic model trained on your own voice samples
D. A Kubernetes deployment for scaling the Speech MCP server
**Answer:** A, B — The exercise description: "you create an AI agent in Microsoft Foundry, connect it to the Azure Speech MCP server, test text-to-speech and speech-to-text capabilities in the agent playground, and build a Python client application that interacts with the agent."

## Unit 5–6: Knowledge check / Summary

**Q27.** According to the module summary, which infrastructure element did you learn to set up specifically to support the Azure Speech MCP server (that is not required for the Language MCP server)?
A. A Cosmos DB account for storing conversation history
B. Azure Blob Storage for audio file input and output
C. An Azure Kubernetes Service cluster
D. A Virtual Network with private endpoints
**Answer:** B — The summary explicitly lists "Set up Azure Blob Storage for audio file input and output" as a learning objective/outcome unique to this module.

## Scenario questions

**Q28.** You want to connect the Speech MCP server entirely via code (not the portal) and restrict it so the agent can only call the text-to-speech tool, requiring approval every time. Which configuration fits?
A. `MCPTool(server_label="azure-speech", server_url=".../speech/mcp", require_approval="always", allowed_tools=[<synthesize tool id>])`
B. Configure only in the portal; code-based restriction isn't supported for the Speech MCP server in this release
C. Set `require_approval="never"` and rely purely on agent instructions to avoid the speech-to-text tool
D. Restrict access by using a separate, dedicated Blob Storage container per individual tool call
**Answer:** A — Like the Language MCP server, `MCPTool` supports `require_approval` and `allowed_tools` to restrict which tools the agent can call, configured in code as an alternative to the portal.

**Q29.** A support-call app needs a SAS token that lets the Speech MCP server both read audio for transcription and write generated audio back to Blob Storage, while following this module's security guidance. What should you do?
A. Use a read-only SAS token and embed it directly in the agent's system instructions for the sake of convenience and simplicity
B. Generate a SAS token with read, write, add, create, and list permissions; treat it as a secret with short expiry, and never embed it in source code, prompts, or transcripts
C. Grant full Storage Account Contributor RBAC to the agent's managed identity instead of a scoped SAS token, with no expiry set
D. Skip SAS configuration entirely since the MCP server uses managed identity for blob access by default in every deployment
**Answer:** B — The module's prerequisites specify a SAS URL with "read, write, add, create, and list permissions," and its security considerations require treating it as a secret with short expiry and never embedding it in code, prompts, or transcripts.

**Q30.** Comparing the Language MCP module and this Speech MCP module, which structural differences does this module explicitly call out?
A. Speech MCP requires Blob Storage/a SAS URL and labels its portal auth field "Bearer" (vs. Language MCP's "Authentication: Key-based"); Speech MCP's example `server_url` omits the `api-version` query parameter that Language MCP's includes
B. Speech MCP doesn't support the code-based `MCPTool` connection method at all, unlike the Language MCP server does in the earlier module
C. Speech MCP uses a completely different SDK package instead of `azure-ai-projects` for its client application, per this module's code samples
D. Speech MCP agents cannot be tested in the agent playground at all, only through custom client code written against the raw REST endpoints
**Answer:** A — These are the two explicit "distinguishing detail" call-outs in this module: the auth field label difference plus the `X-Blob-Container-Url` requirement, and the missing `api-version` parameter in the Speech MCP server URL example.

**Q31.** You're building a client app that both transcribes an uploaded meeting recording and synthesizes a spoken summary back to the user, using the Foundry SDK pattern from this module. Which sequence of steps matches the module's guidance?
A. Create `AIProjectClient` with `DefaultAzureCredential`, get an OpenAI client via `get_openai_client()`, then call `responses.create()` twice — once per task — referencing the agent by name via `extra_body["agent_reference"]`
B. Create a `TextAnalyticsClient` and call `recognize_pii_entities` for both the transcription and summary generation tasks in sequence
C. Use `SpeechRecognizer` and `SpeechSynthesizer` directly instead of going through the agent at all, bypassing MCP and the agent framework entirely
D. A single `responses.create()` call cannot invoke MCP tools at all; you must always fall back to the plain REST API directly instead
**Answer:** A — The module's client pattern is common to both tasks: build the `AIProjectClient`/OpenAI client once, then call `responses.create()` with the appropriate prompt and agent reference for each task, letting the agent route to the Recognize or Synthesize MCP tool as needed.
