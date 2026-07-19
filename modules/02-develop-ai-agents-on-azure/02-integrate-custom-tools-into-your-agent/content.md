# Integrate custom tools into your agent

Source: https://learn.microsoft.com/en-us/training/modules/build-agent-with-custom-tools/

> Note: The module's marketing/search title is "Build an AI agent with custom tools," but the page's actual `<h1>` and TOC title is **"Integrate custom tools into your agent."** Both refer to the same module (uid `learn.wwl.build-agent-with-custom-tools`). 7 units, Intermediate level, part of the Foundry Agent Service track.

## Learning objectives

By the end of this module, you'll be able to:

- Describe the benefits of using custom tools with your agent.
- Explore the different options for custom tools.
- Build an agent that integrates custom tools using the Microsoft Foundry Agent Service.

**Prerequisites**: Familiarity with Azure/Azure portal; understanding of generative AI (see *Fundamentals of Generative AI*); prior experience with Microsoft Foundry Agent Service strongly recommended (see *Develop an AI agent with Microsoft Foundry Agent Service*).

## Exam relevance

This module maps to **Learning Path 2 — Develop AI agents on Azure**, and primarily supports the exam domain **"Implement generative AI and agentic solutions" (30–35%)**, specifically the **"Build agents by using Foundry"** skill group:

- *"Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions"* — this is the core subject of the module: OpenAPI-specified tools (APIs), Azure Functions (event-driven/custom logic), and function calling (custom functions).
- *"Build agents that integrate retrieval, function-calling, and conversation memory"* — the function-calling mechanics (`FunctionTool`, `PromptAgentDefinition`, dynamic tool selection) taught here are the concrete implementation of this bullet.
- *"Define agent roles, goals, conversation-tracking approach, and tool schemas"* — the module shows how tool JSON schemas (parameters, required fields, `additionalProperties`) are authored and attached to an agent definition.

It also touches the **"Choose the appropriate Foundry services for generative AI and agents"** skill group under *Plan and manage an Azure AI solution*, specifically *"Choose appropriate memory, tool, and knowledge integration services for agent solutions"* — by contrasting custom function tools, Azure Functions, OpenAPI tools, and Logic Apps as different integration options.

## Introduction

Microsoft Foundry Agent Service lets you build an agent without deep AI/ML expertise. Built-in tools give agents functionality for gathering knowledge and generating code, but agents often need to perform actions an AI model can't do alone. For these cases you attach a **custom tool** — based on your own code, or a third-party service/API.

**Example scenario used throughout the module**: A retail company's support team is overwhelmed by repetitive inquiries. A custom FAQ agent built with Foundry Agent Service and custom tools (e.g., to look up customer orders) frees the team to handle complex issues.

## Why use custom tools

Custom tools extend agent capability by making functionality available for the agent to invoke, depending on how it decides to respond to a user prompt (i.e., tool use is **model-driven/declarative**, not hard-coded by the developer).

**Stated benefits:**
- **Enhanced productivity**: Automate repetitive tasks and streamline workflows.
- **Improved accuracy**: Precise, consistent outputs; reduces human error.
- **Tailored solutions**: Address specific business needs and optimize processes.

**Worked example — weather/ski-resort scenario (illustrates the tool-calling flow):**
1. A user asks an agent about weather conditions at a ski resort.
2. The agent determines it has a tool that can call an external meteorological API, and invokes it.
3. The tool returns the weather report; the agent relays it to the user.

**Common scenarios for custom tools (five named use cases):**

| Scenario | Custom tool connects agent to... | Functionality | Outcome |
|---|---|---|---|
| Customer support automation | CRM system | Retrieve order histories, process refunds, real-time shipping updates | Faster query resolution, reduced support workload |
| Inventory management | Inventory management system | Check stock levels, predict restocking via historical data, auto-order from suppliers | Streamlined inventory, optimized supply chain |
| Healthcare appointment scheduling | Custom scheduling tool | Access patient records, suggest slots, send reminders | Reduced admin burden, better patient experience |
| IT Helpdesk support | Ticketing + knowledge base systems | Troubleshoot common issues, escalate complex problems, track ticket status | Faster resolution, reduced downtime |
| E-learning and training | Learning management system (LMS) | Recommend courses, track student progress, answer course questions | Enhanced learning experience, streamlined admin |

## Options for implementing custom tools

Foundry Agent Service provides **four** custom tool integration options:

- **Custom function (function calling)**: You describe the structure of custom functions to the agent; the agent returns which function(s) to call along with arguments. The agent dynamically identifies the appropriate function based on its definition. Supports custom logic/workflows across a selection of programming languages.
- **Azure Functions**: Serverless, event-driven applications with minimal overhead. Support **triggers** (determine when a function executes) and **bindings** (streamline connections to input/output data sources).
- **OpenAPI specification tools**: Connect the Azure AI Agent to an external API using an **OpenAPI 3.0 specification**. Standardized, automated, scalable API integration. OpenAPI specs describe HTTP APIs so people can understand how the API works, generate client code, create tests, and apply design standards.
- **Azure Logic Apps**: Low-code/no-code option to add workflows and connect apps, data, and services.

**Distinguishing factor (exam-relevant):** function calling = your own code/logic the agent decides to call; Azure Functions = serverless event-driven compute (triggers/bindings) already deployed in Azure; OpenAPI tools = calling a pre-existing external HTTP API described by a spec file (no custom code needed, just the spec); Logic Apps = low-code/no-code workflow connector, not a code-based integration.

## How to integrate custom tools

Custom tools can be defined multiple ways depending on scenario — e.g., existing Azure Functions, or a public OpenAPI spec.

### Function Calling

Function calling lets agents dynamically execute predefined functions based on user input — ideal for retrieving data or processing queries; can be implemented in code from within the agent. The function may call other APIs internally.

**Step 1 — define the function (Python):**

```python
import json

def recent_snowfall(location: str) -> str:
    """
    Fetches recent snowfall totals for a given location.
    :param location: The city name.
    :return: Snowfall details as a JSON string.
    """
    mock_snow_data = {"Seattle": "0 inches", "Denver": "2 inches"}
    snow = mock_snow_data.get(location, "Data not available.")
    return json.dumps({"location": location, "snowfall": snow})
```

**Step 2 — register the function with the agent via the Azure AI SDK:**

```python
# Define a function tool for the model to use
function_tool = FunctionTool(
    name="recent_snowfall",
    parameters={
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city name to check snowfall for."},
        },
        "required": ["location"],
        "additionalProperties": False
    },
    description="Get recent snowfall totals for a given location.",
    strict=True,
)

# Add the function tool to a list of tools for the agent
tools: list[Tool] = [function_tool]

# Create your agent with the toolset
agent = project_client.agents.create_version(
    name="snowfall-agent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions="You are a weather assistant tracking snowfall. Use the provided functions to answer questions.",
        tools=tools,
    )
)
```

Key SDK elements: `FunctionTool` class (params: `name`, `parameters` [JSON schema with `type`, `properties`, `required`, `additionalProperties`], `description`, `strict`), `Tool` type, `project_client.agents.create_version(...)`, `PromptAgentDefinition` (params: `model`, `instructions`, `tools`). Model used in example: `gpt-4.1`.

The agent calls `recent_snowfall` dynamically only when it determines the prompt requires info the function can supply.

### Azure Functions

Azure Functions provides serverless compute for real-time, event-driven processing (e.g., HTTP requests, queue messages).

**Example — Azure Function via storage queue trigger:**

```python
tool = AzureFunctionTool(
    azure_function=AzureFunctionDefinition(
        input_binding=AzureFunctionBinding(
            storage_queue=AzureFunctionStorageQueue(
                queue_name="STORAGE_INPUT_QUEUE_NAME",
                queue_service_endpoint="STORAGE_QUEUE_SERVICE_ENDPOINT",
            )
        ),
        output_binding=AzureFunctionBinding(
            storage_queue=AzureFunctionStorageQueue(
                queue_name="STORAGE_OUTPUT_QUEUE_NAME",
                queue_service_endpoint="STORAGE_QUEUE_SERVICE_ENDPOINT",
            )
        ),
        function=AzureFunctionDefinitionFunction(
            name="queue_trigger",
            description="Get weather for a given location",
            parameters={
                "type": "object",
                "properties": {"location": {"type": "string", "description": "location to determine weather for"}},
            },
        ),
    )
)

agent = project_client.agents.create_version(
    agent_name="MyAgent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions="You are a helpful weather assistant. Use the provided Azure Function to get weather information for a location when needed.",
        tools=[tool],
    ),
)
```

Key SDK classes: `AzureFunctionTool`, `AzureFunctionDefinition` (has `input_binding` / `output_binding` of type `AzureFunctionBinding`, and `function` of type `AzureFunctionDefinitionFunction`), `AzureFunctionStorageQueue` (params: `queue_name`, `queue_service_endpoint`). The agent communicates with the Azure Function **via a storage queue** (input queue for requests, output queue for results) — not a direct HTTP call.

### OpenAPI Specification

OpenAPI-defined tools let agents interact with external APIs via standardized specs. **Foundry Agent Service uses OpenAPI 3.0-specified tools.**

**Supported authentication types for OpenAPI 3.0 tools (exactly three):**
1. **Anonymous**
2. **API key**
3. **Managed identity**

**Example spec file (`weather_openapi.json`):**

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "get weather data",
    "description": "Retrieves current weather data for a location based on wttr.in.",
    "version": "v1.0.0"
  },
  "servers": [
    {
      "url": "https://wttr.in"
    }
  ],
  "auth": [],
  "paths": {
    "/{location}": {
      "get": {
        "description": "Get weather information for a specific location",
        "operationId": "GetCurrentWeather",
        "parameters": [
          {
            "name": "location",
            "in": "path",
            "description": "City or location to retrieve the weather for",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
          "name": "format",
          "in": "query",
          "description": "Always use j1 value for this parameter",
          "required": true,
          "schema": {
            "type": "string",
            "default": "j1"
          }
        }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "404": {
            "description": "Location not found"
          }
        },
        "deprecated": false
      }
    }
  },
  "components": {
    "schemes": {}
  }
}
```

Note: the top-level `openapi` field in the example spec is `"3.1.0"`, but the module text explicitly says Foundry Agent Service "uses OpenAPI 3.0 specified tools" and OpenAPI specification tools connect via an "OpenAPI 3.0 specification" — treat 3.0 as the documented/exam-relevant version even though the sample JSON shows 3.1.0.

**Registering the OpenAPI tool in the agent definition:**

```python
from azure.ai.projects.models import OpenApiTool, OpenApiAnonymousAuthDetails

with open(weather_asset_file_path, "r") as f:
      openapi_weather = cast(dict[str, Any], jsonref.loads(f.read()))

tool = OpenApiTool(
    openapi=OpenApiFunctionDefinition(
        name="get_weather",
        spec=openapi_weather,
        description="Retrieve weather information for a location.",
        auth=OpenApiAnonymousAuthDetails(),
    )
)

agent = project_client.agents.create_version(
    agent_name="openapi-agent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions="You are a weather assistant. Use the API to fetch weather data.",
        tools=[openapi_tool],
    ),
)
```

Key SDK classes: `OpenApiTool`, `OpenApiFunctionDefinition` (params: `name`, `spec`, `description`, `auth`), `OpenApiAnonymousAuthDetails` (one of the three auth-detail classes corresponding to anonymous/API key/managed identity auth types), imported from `azure.ai.projects.models`.

### Key conceptual point — declarative tool use

> One of the concepts related to agents and custom tools that developers often have difficulty with is the **declarative** nature of the solution. You don't need to write code that explicitly *calls* your custom tool functions — **the agent itself decides to call tool functions** based on messages in prompts. By providing the agent with functions that have meaningful names and well-documented parameters, the agent can "figure out" when and how to call the function all by itself.

This declarative behavior applies to **all three** tool types covered (function calling, Azure Functions, OpenAPI tools) — the developer registers/describes the tool; the model decides at runtime whether and how to invoke it.

## Exercise - Build an agent with custom tools

Hands-on exercise (~30 minutes): create an agent in code and connect a tool definition to a custom tool function. Launched via an external Microsoft Learn sandbox link (requires Azure subscription; free account includes 30 days of credits if you don't already have one). Tip given: after completing the exercise, delete the Azure resources created during it to avoid ongoing cost.

## Module assessment

The official knowledge-check unit posed three questions (options and correct answers as shown/inferred from page structure — first listed option is correct in Learn module conventions of this type):

1. **What are custom tools, and how can they help you develop effective agents with Microsoft Foundry Agent Service?**
   - Callable functions that an agent can use to extend its capabilities. *(correct concept per module content)*
   - Extensions for Visual Studio Code that make it easier to create and deploy agents. *(distractor)*
   - Fine-tuned models that the agent can use to generate custom output. *(distractor)*

2. **You need to integrate functionality from an OpenAPI 3.0-based web service into an agent solution. What should you do?**
   - Add the JSON schema of the web service to the agent's instructions. *(distractor)*
   - Rewrite the web service as a Python function and hard-code it in your agent app. *(distractor)*
   - Add the web service as an OpenAPI specification tool to the agent definition. *(correct — matches "Options for implementing custom tools" and "How to integrate custom tools" units)*

3. **Your agent application code includes a local function that you want the agent to call. What kind of tool should you add to the agent's definition?**
   - Function calling *(correct — matches "Function Calling" section: for functions defined/callable within your own agent app code)*
   - Code interpreter *(distractor — this is a built-in tool, not a custom tool, and not covered in this module)*
   - Azure Functions *(distractor — for externally deployed serverless functions, not local in-app functions)*

## Summary

Custom tools in Foundry Agent Service boost productivity and provide tailored business solutions — optimizing processes for specific needs and producing better agent responses. The techniques covered enable businesses to generate marketing materials, improve communications, and analyze market trends more effectively. The range of tool options — from Azure Functions to OpenAPI specifications — enables intelligent, event-driven applications built on well-established patterns already used across industries.

**Further reading (as listed on the page):**
- [AI Agents for beginners — tool use](https://github.com/microsoft/ai-agents-for-beginners/blob/main/04-tool-use/README.md)
- [Microsoft Foundry Agent Service function calling](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/function-calling)
- [Introduction to Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)
- [OpenAPI Specification](https://swagger.io/specification/)
