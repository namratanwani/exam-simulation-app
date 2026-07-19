# Gaps and anomalies — Learning Path 2 (Develop AI agents on Azure)

No unit fetches failed across any of the 9 modules — all content.md/questions.md pairs are complete and grounded in successfully fetched Microsoft Learn pages.

The item below is not a fetch failure but a **content/naming divergence worth flagging** for anyone using these notes to study:

## Modules 07 and 08 — Microsoft Learn has replaced "Semantic Kernel" content with "Microsoft Agent Framework" content

- **07-agent-framework-semantic-kernel** (source URL slug: `develop-ai-agent-with-semantic-kernel`) — the live module title is now **"Develop an AI agent with Microsoft Agent Framework"**. The page contains almost no Semantic Kernel SDK detail (no `Kernel`, `ChatCompletionAgent`, `KernelFunction`, or plugin/skill classes). Semantic Kernel is mentioned exactly once, as lineage: "Microsoft Agent Framework is the next generation of both Semantic Kernel and AutoGen, built by the same teams." content.md documents this prominently and was written faithfully from the actual published content (Microsoft Agent Framework), not fabricated Semantic Kernel material.
- **08-multi-agent-orchestration** (source URL slug: `orchestrate-semantic-kernel-multi-agent-solution`, `uid: learn.wwl.orchestrate-sk-multi-agent-solution`) — same situation. The module no longer teaches Semantic Kernel's `AgentGroupChat`/`AgentChat` APIs; it teaches the **Microsoft Agent Framework SDK**'s five orchestration patterns (concurrent, sequential, handoff, group chat, magentic) via `ConcurrentBuilder`, `SequentialBuilder`, `GroupChatBuilder`, `WorkflowBuilder` (handoff), and `MagenticBuilder`.

**Why this matters for exam prep:** if other AI-103 study material (or older exam dumps) references classic Semantic Kernel class names like `AgentGroupChat`, treat that as outdated relative to the current Microsoft Learn content (both pages carry 2026 `ms.date` values, i.e. this is the current, actively maintained version of the path). The current curriculum — and presumably the current exam surface — uses **Microsoft Agent Framework** naming for multi-agent orchestration, while **Foundry Agent Service** remains the separate, managed hosting runtime that the framework can target as one of several supported agent providers. Both content.md files call this out explicitly at the top of the document.

No other gaps to report.
