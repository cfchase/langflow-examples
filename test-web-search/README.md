# test-web-search

Validates that web search works end-to-end via the multi-agent-platform.

## Purpose

This flow tests DuckDuckGo web search integration using LangFlow's built-in
DuckDuckGo Search component. DuckDuckGo is preferred because it requires no API key.

## Prerequisites

- LangFlow running with platform configuration
- No API key required (DuckDuckGo is free)

## Fallback Options

If DuckDuckGo doesn't work:
1. **Tavily** - Requires TAVILY_API_KEY in langflow.env
2. **Google Custom Search** - Requires GOOGLE_API_KEY + GOOGLE_CSE_ID

## How it works

1. ChatInput receives user search query
2. DuckDuckGo Search component executes search (no API key needed)
3. ChatOutput returns search results

## Testing

1. Import flow: `make langflow-import`
2. Open LangFlow UI, select this flow
3. Send test query: "What is LangFlow?"
4. Expected result: Search results about LangFlow
5. Failure indicates: Network issues or DuckDuckGo component problems

## Credential Injection

**None required** - DuckDuckGo does not require API keys.

This is a system-level service that can be tested in the LangFlow playground
without requiring the platform chat UI.

## Flow JSON

The flow JSON file (`test-web-search.json`) must be created manually in LangFlow UI:

1. Open LangFlow UI at http://localhost:7860
2. Create new flow with name "test-web-search"
3. Add components: ChatInput -> DuckDuckGo Search -> ChatOutput
4. Configure DuckDuckGo Search:
   - max_results: 5
5. Connect edges: ChatInput.message -> DuckDuckGo.query -> ChatOutput.input_value
6. Export flow JSON and save to this directory
