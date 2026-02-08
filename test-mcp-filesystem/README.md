# test-mcp-filesystem

Validates that MCP server auto-setup and MCPTools integration work end-to-end via
the multi-agent-platform.

## Purpose

This flow tests:
1. MCP server auto-setup during import (server config created via LangFlow API)
2. MCPTools component can connect to Python-based STDIO MCP server
3. Agent can use MCP tools for web fetching

## Prerequisites

- LangFlow running with platform configuration
- Python mcp-server-fetch package (installed automatically via manifest)

## Why Python MCP Server

Per Phase 4.1 decision: Use Python STDIO MCP server instead of Node.js because:
- Python is guaranteed to be available in LangFlow container
- Node.js/npx may not be installed
- mcp-server-fetch is a pip package, installed via manifest dependencies

## How it works

1. ChatInput receives user query (e.g., "Fetch content from https://example.com")
2. Agent component with MCPTools uses mcp-server-fetch to retrieve web content
3. ChatOutput returns the fetched content

## MCP Server Configuration

The MCP server is configured in flow-sources.yaml:

```yaml
mcp_servers:
  - name: server-fetch
    type: stdio
    command: python
    args:
      - "-m"
      - "mcp_server_fetch"
```

The mcp-server-fetch package is installed via manifest.yaml pip_dependencies.

## Testing

1. Import flow: `make langflow-import`
2. Verify MCP server was created: Check LangFlow UI -> Settings -> MCP
3. Open LangFlow UI, select this flow
4. Send test query: "Fetch https://httpbin.org/html"
5. Expected result: HTML content from httpbin
6. Failure indicates: MCP server not started, or MCPTools not connecting

## Credential Injection

**None required** - mcp-server-fetch uses public web access.

This is a system-level service that can be tested in the LangFlow playground
without requiring the platform chat UI.

## Flow JSON

The flow JSON file (`test-mcp-filesystem.json`) must be created manually in LangFlow UI:

1. Open LangFlow UI at http://localhost:7860
2. Create new flow with name "test-mcp-filesystem"
3. Add components: ChatInput -> Agent (with MCPTools) -> ChatOutput
4. Configure Agent:
   - Add MCPTools component
   - Select "server-fetch" MCP server
5. Connect edges appropriately
6. Export flow JSON and save to this directory

## Troubleshooting

### MCP server not found
- Verify import_flows.py has MCP auto-setup capability (Plan 04.1-01)
- Check LangFlow logs for MCP server creation errors
- Verify flow-sources.yaml has mcp_servers entry

### mcp-server-fetch not installed
- Verify manifest.yaml has pip_dependencies with mcp-server-fetch
- Check import logs for pip install output
