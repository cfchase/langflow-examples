# test-langfuse-agent

Validates that Langfuse tracing captures agent reasoning, tool calls, and
multi-step flows from LangFlow.

## Purpose

This flow tests Langfuse tracing with a more complex agent-based flow that
includes tool usage. Agent flows produce richer traces showing the reasoning
chain, each tool invocation, and multiple LLM calls within a single run.

Tracing is automatic -- the same Langfuse environment variables that enable
tracing for simple flows also capture full agent execution details.

## Flow Topology

```
ChatInput -> Agent (OpenAI) -> ChatOutput
                |
                +-- DuckDuckGo Search (tool)
```

## Prerequisites

- LangFlow running with Langfuse tracing enabled:
  1. Start Langfuse: `make langfuse-start`
  2. Restart LangFlow to pick up Langfuse env vars: `make langflow-restart`
- `OPENAI_API_KEY` set in `config/langflow.env`
- Langfuse dev keys in `config/langflow.env` (included by default in `langflow.env.example`)
- DuckDuckGo requires no API key

## Testing

1. Import flow: `make langflow-import`
2. Open LangFlow UI at http://localhost:7860, select this flow
3. Send a search query: "What are the latest developments in LangFlow?"
4. Verify the agent searches the web and returns a synthesized answer
5. Check Langfuse dashboard for the agent trace (see below)

### Expected Trace Data

- Agent reasoning chain (thought/action/observation steps)
- Tool call inputs and outputs (DuckDuckGo search queries and results)
- Multiple LLM invocations within a single agent run
- Total token usage across all LLM calls
- Flow latency breakdown (LLM time vs tool time)

## Langfuse Dashboard

**URL:** http://localhost:3000

**Login:** `dev@localhost.local` / `devpassword123`

Traces appear automatically after each flow run. Navigate to **Traces** in the
left sidebar. Agent traces are more detailed than simple LLM traces -- expand
the trace tree to see individual tool calls and LLM generations nested under
the parent agent span.

**Note:** Known LangFlow issue [#4997](https://github.com/langflow-ai/langflow/issues/4997)
may produce multiple traces per single flow run.

## Flow JSON

The flow JSON file (`test-langfuse-agent.json`) must be created manually in LangFlow UI:

1. Open LangFlow UI at http://localhost:7860
2. Create new flow with name "test-langfuse-agent"
3. Add components:
   - ChatInput
   - Agent (OpenAI)
   - DuckDuckGo Search
   - ChatOutput
4. Configure Agent:
   - Model Name: `gpt-4o-mini`
   - OpenAI API Key: leave empty (uses global variable from langflow.env)
5. Connect DuckDuckGo Search as a tool to the Agent
6. Connect edges: ChatInput.message -> Agent.input_value, Agent.response -> ChatOutput.input_value
7. Export flow JSON and save to this directory
