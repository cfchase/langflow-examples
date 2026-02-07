# test-google-drive

Validates that user OAuth tokens are injected into flows via the tweaks API.

## Purpose

This flow tests SETTINGS-02/SETTINGS-04: User-level settings (OAuth tokens) are available per-session.

## How it works

1. ChatInput receives user query
2. GoogleDriveSearch component has `access_token` field (empty in flow JSON)
3. Platform backend injects user's Google OAuth token via tweaks at runtime
4. GoogleDriveSearch queries user's Drive using injected token
5. ChatOutput returns search results

## Prerequisites

- User must have connected Google Drive in the platform Settings
- Token injection must be wired in chat_messages.py (Plan 02-02)
- flow_token_injection.py must have "test-google-drive" mapping (Plan 02-02)

## Creating the Flow JSON

1. Open LangFlow UI at http://localhost:7860
2. Create flow with GoogleDriveSearch component (or similar)
3. Leave access_token field empty (will be injected at runtime)
4. Export as test-google-drive.json to this directory

## Testing

1. Connect Google Drive in platform Settings (OAuth flow)
2. Run `make langflow-import` to import this flow
3. In the platform chat UI, select this flow and send a query like "list my recent documents"
4. If successful, you'll see Drive search results (proves token injection works)
5. If failed with "Missing integration", the OAuth token wasn't found
6. If failed with "401 Unauthorized", the token wasn't injected into the right field

## Token Injection Mapping

In flow_token_injection.py:
```python
"test-google-drive": {
    "google_drive": "GoogleDriveSearch.access_token",
}
```

This tells the backend to:
1. Look up user's "google_drive" OAuth token
2. Inject it into the "GoogleDriveSearch" component's "access_token" field
