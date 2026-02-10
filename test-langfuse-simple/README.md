# test-langfuse-simple

Validates that Langfuse tracing captures basic LLM interactions from LangFlow.

## Purpose

This flow tests that Langfuse tracing is working end-to-end. When Langfuse
environment variables are configured (via `langflow.env`), all LangFlow
executions are automatically traced -- no per-flow configuration needed.

This simple flow sends a prompt to an LLM and returns the response, producing
a minimal trace in Langfuse with input, output, token counts, and latency.

## Flow Topology

```
ChatInput -> OpenAI Model -> ChatOutput
```

## Prerequisites

- LangFlow running with Langfuse tracing enabled:
  1. Start Langfuse: `make langfuse-start`
  2. Restart LangFlow to pick up Langfuse env vars: `make langflow-restart`
- `OPENAI_API_KEY` set in `config/langflow.env`
- Langfuse dev keys in `config/langflow.env` (included by default in `langflow.env.example`)

## Testing

1. Import flow: `make langflow-import`
2. Open LangFlow UI at http://localhost:7860, select this flow
3. Send a test message: "Hello, what is 2+2?"
4. Verify response appears in ChatOutput
5. Check Langfuse dashboard for the trace (see below)

### Expected Trace Data

- Input prompt text
- LLM completion text
- Token counts (prompt + completion)
- Latency (ms)
- Model name (e.g., `gpt-4o-mini`)

## Langfuse Dashboard

**URL:** http://localhost:3000

**Login:** `dev@localhost.local` / `devpassword123`

Traces appear automatically after each flow run. Navigate to **Traces** in the
left sidebar to see all captured executions. Each trace shows the full
input/output chain with timing and token usage.

**Note:** Known LangFlow issue [#4997](https://github.com/langflow-ai/langflow/issues/4997)
may produce multiple traces per single flow run.

## Flow JSON

The flow JSON file (`test-langfuse-simple.json`) must be created manually in LangFlow UI:

1. Open LangFlow UI at http://localhost:7860
2. Create new flow with name "test-langfuse-simple"
3. Add components: ChatInput -> OpenAI Model -> ChatOutput
4. Configure OpenAI Model:
   - Model Name: `gpt-4o-mini`
   - OpenAI API Key: leave empty (uses global variable from langflow.env)
5. Connect edges: ChatInput.message -> OpenAI.input_value, OpenAI.text_output -> ChatOutput.input_value
6. Export flow JSON and save to this directory
