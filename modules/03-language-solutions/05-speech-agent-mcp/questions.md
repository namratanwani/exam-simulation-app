# Practice questions — Develop a speech agent with the Azure Speech MCP server

## Unit 1: Introduction

**Q1.** What is the release status of the Azure Speech MCP server, per this module?
A. Generally available
B. Public preview
C. Retired
D. Not yet announced
**Answer:** B — "The Azure Speech MCP server is currently in public preview. Details described in this module are subject to change."

**Q2.** In the module's customer support scenario, what two speech tasks does the AI agent perform through a single MCP tool connection?
A. Sentiment analysis and translation
B. Transcribing recorded calls to text and generating audio responses for playback
C. Speaker diarization and PII redaction
D. Language detection and named entity recognition
**Answer:** B — The module's example: "transcribe recorded calls to text for analysis, and generate audio responses that can be played back to customers."

## Unit 2: Understand the Azure Speech MCP server

**Q3.** How many core speech capabilities does the Azure Speech MCP server expose, and what are they?
A. Four: Speech-to-text, Text-to-speech, Speech Translation, Voice Live
B. Two: Speech-to-text (Recognize) and Text-to-speech (Synthesize)
C. Three: Recognize, Synthesize, and Diarize
D. One: a unified transcribe-and-synthesize tool
**Answer:** B — The module's table lists exactly two capabilities: Speech-to-text (Recognize) and Text-to-speech (Synthesize) — fewer than the four capabilities of the Language MCP server.

**Q4.** Which audio formats are explicitly listed as supported by the speech-to-text tool of the Azure Speech MCP server?
A. WAV, MP3, OGG, FLAC, MP4, M4A, AAC
B. WAV and MP3 only
C. WMA, AIFF, and OPUS
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
A. Speech models are too large to run without cold storage caching.
B. It works with audio files — generated speech is saved to Blob Storage, and transcription can read from Blob Storage via SAS URL.
C. Azure Speech requires storage for training custom acoustic models only.
D. It doesn't — this is a trick; both MCP servers require storage identically.
**Answer:** B — "Unlike text-only MCP tools, the Azure Speech MCP server works with audio files, which requires an Azure Storage account." Text-to-speech saves output to Blob Storage; speech-to-text can read from a SAS-URL-secured container or a public URL.

**Q7.** What permissions should the SAS token for the blob container have, per this module's prerequisites?
A. Read only
B. Read, write, add, create, and list
C. Read, execute, and delete
D. Full Storage Account Contributor RBAC role, not a SAS token
**Answer:** B — "A SAS URL for the blob container with read, write, add, create, and list permissions."

**Q8.** What Azure RBAC role(s) does the module say you need on the resource group to use the Azure Speech MCP server with an agent?
A. Reader
B. Contributor or Owner
C. Storage Blob Data Reader only
D. Global Administrator
**Answer:** B — "A Foundry resource and project — you need Contributor or Owner role on the resource group."

**Q9.** Which security best practice does the module explicitly recommend for SAS URLs used with the Speech MCP server?
A. Embed them directly in agent prompts for convenience.
B. Use the shortest practical expiry time, scope to a single container, and never embed them in source code, prompts, or transcripts.
C. Generate a SAS URL with no expiry so the agent never loses access.
D. Share the SAS URL via email to all team members for redundancy.
**Answer:** B — "Treat SAS URLs as secrets. Use the shortest practical expiry time, scope them to a single container, and don't embed them in source code, agent prompts, or chat transcripts."

## Unit 3: Connect and use the Speech MCP server with an agent

**Q10.** In Azure Storage account setup for this module, under which blade do you create a container?
A. Networking
B. Data storage → Containers
C. Access control (IAM)
D. Monitoring → Insights
**Answer:** B — "In the storage account, expand Data storage and select Containers."

**Q11.** When connecting the Azure Speech MCP server via the Foundry portal's Tools page, which configuration field is unique to the Speech MCP connection and NOT present for the Language MCP connection?
A. Foundry resource name
B. X-Blob-Container-Url
C. Authentication type
D. Agent selection
**Answer:** B — The Speech MCP tool connection requires an additional `X-Blob-Container-Url` field for the SAS URL, which has no equivalent in the Language MCP tool's connection settings (Foundry resource name, Authentication/credential, and agent selection are common to both).

**Q12.** What example model does the module suggest deploying for the agent's reasoning/response generation before connecting the Speech MCP server?
A. gpt-4o-mini
B. gpt-4.1
C. gpt-3.5-turbo
D. text-embedding-3-large
**Answer:** B — "Deploy a model (such as gpt-4.1) that your agent will use for reasoning and generating responses."

**Q13.** After the agent successfully performs text-to-speech via the Speech MCP tool in the playground, what does the response contain?
A. Raw audio bytes embedded directly in the chat response
B. A link to the generated audio file saved in your blob container
C. Only a confirmation message with no way to access the audio
D. An SSML transcript of the generated speech
**Answer:** B — "The response includes a link to the generated audio file saved in your blob container. Select the link to listen to the synthesized speech."

**Q14.** Which of the following can be used as the source for a speech-to-text transcription request in the agent playground? (Choose two.)
A. A publicly accessible URL
B. A SAS URL pointing to a file in your blob container
C. A direct file upload attached to the chat message
D. A local file path on your development machine
**Answer:** A, B — "You can use a publicly accessible URL or a SAS URL pointing to a file in your blob container."

**Q15.** In a prompt to the Speech MCP agent, how would you request that profanity in a transcription be masked rather than removed or left raw?
A. By setting a `profanity_filter=True` flag in code only — it cannot be requested via prompt.
B. By specifying it in natural language in the prompt, since profanity filtering (masked, removed, or raw) is one of the tool's configurable options.
C. Profanity filtering isn't supported by the Speech MCP server.
D. By appending `?profanity=masked` to the audio file URL.
**Answer:** B — The module lists "Profanity filtering: Request masked, removed, or raw profanity handling during transcription" as one of the prompt-level customizable options.

**Q16.** Which packages are used to build a Python client application for the speech agent, matching the pattern from the Language MCP module?
A. `azure-cognitiveservices-speech` and `azure-storage-blob`
B. `azure-ai-projects` and `azure-identity`
C. `openai` and `azure-mgmt-storage`
D. `azure-ai-speech-agents` and `requests`
**Answer:** B — Same pattern as the Language MCP module: "you use the azure-ai-projects and azure-identity packages."

**Q17.** How is the target agent specified when calling `responses.create()` in the client code sample?
A. Via a `model` parameter set to the agent's deployment name
B. Via `extra_body={"agent_reference": {"name": "Speech-Agent", "type": "agent_reference"}}`
C. Via an `agent_id` header
D. It's inferred automatically from the project endpoint
**Answer:** B — Shown verbatim in the code sample.

**Q18.** Which SDK class, from which package, is used to define the Speech MCP tool connection directly in code (rather than via the Foundry portal)?
A. `SpeechMCPConnector` from `azure-cognitiveservices-speech`
B. `MCPTool` from `azure.ai.projects.models`
C. `AgentToolBuilder` from `azure-ai-agents`
D. `RemoteTool` from `azure-identity`
**Answer:** B — `from azure.ai.projects.models import MCPTool`, same class used for the Language MCP server in the earlier module.

**Q19.** What is the `server_url` value shown in this module's `MCPTool` code sample for the Speech MCP server, and how does it differ from the Language MCP server's URL shown in an earlier module?
A. `https://{foundry-resource-name}.cognitiveservices.azure.com/speech/mcp` — with no `api-version` query parameter shown, unlike the Language MCP URL which included `?api-version=2025-11-15-preview`
B. They are identical except for the resource name
C. The Speech MCP URL requires a `region` path segment that Language MCP does not
D. The Speech MCP URL uses `.services.ai.azure.com` instead of `.cognitiveservices.azure.com`
**Answer:** A — The module's code sample shows `server_url="https://{foundry-resource-name}.cognitiveservices.azure.com/speech/mcp"` without an `api-version` parameter, in contrast to the Language MCP module's URL which explicitly appended `?api-version=2025-11-15-preview`.

## Unit 4: Exercise

**Q20.** What does the hands-on exercise for this module have you build and test? (Choose two.)
A. An AI agent connected to the Azure Speech MCP server, tested for both text-to-speech and speech-to-text in the playground
B. A Python client application that interacts with the agent
C. A custom acoustic model trained on your own voice samples
D. A Kubernetes deployment for scaling the Speech MCP server
**Answer:** A, B — The exercise description: "you create an AI agent in Microsoft Foundry, connect it to the Azure Speech MCP server, test text-to-speech and speech-to-text capabilities in the agent playground, and build a Python client application that interacts with the agent."

## Unit 5–6: Knowledge check / Summary

**Q21.** According to the module summary, which infrastructure element did you learn to set up specifically to support the Azure Speech MCP server (that is not required for the Language MCP server)?
A. A Cosmos DB account
B. Azure Blob Storage for audio file input and output
C. An Azure Kubernetes Service cluster
D. A Virtual Network with private endpoints
**Answer:** B — The summary explicitly lists "Set up Azure Blob Storage for audio file input and output" as a learning objective/outcome unique to this module.
