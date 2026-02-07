# test-llm-credentials

Validates that platform-provided LLM API keys are available to flows via LangFlow global variables.

## Purpose

This flow tests SETTINGS-01/SETTINGS-03: System settings (LLM API keys) are available via environment variables or LangFlow globals.

## How it works

1. ChatInput receives user message
2. OpenAI Model uses OPENAI_API_KEY from global variables (load_from_db: true)
3. ChatOutput returns the LLM response

## Prerequisites

- OPENAI_API_KEY must be set in backend/.env
- LangFlow container must be restarted after adding the key (`make langflow-restart`)
- The OPENAI_API_KEY global variable should appear in LangFlow UI under Settings > Global Variables

## Creating the Flow JSON

1. Open LangFlow UI at http://localhost:7860
2. Create new flow: ChatInput -> OpenAI Model -> ChatOutput
3. In OpenAI Model, set api_key to use Global Variable "OPENAI_API_KEY"
4. Test in playground - should get AI response
5. Export as test-llm-credentials.json to this directory

## Testing

1. Run `make langflow-import` to import this flow
2. Open LangFlow UI and navigate to this flow
3. Send any message in the playground
4. If successful, you'll get an AI response (proves API key is working)
5. If failed, check LangFlow logs for "401 Unauthorized" (API key not injected)

## Flow JSON Configuration

Key configuration in the flow JSON:
- OpenAI Model component has `openai_api_key.load_from_db: true`
- This tells LangFlow to look up the value from global variables
- The global variable name must match: OPENAI_API_KEY
