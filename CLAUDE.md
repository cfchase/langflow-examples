# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository Purpose

This repository contains **LangFlow flows** for use with the [Multi-Agent Platform](https://github.com/cfchase/multi-agent-platform).

Flows are imported into LangFlow via the platform's `make langflow-import` command.

## Structure

```
langflow-examples/
├── <flow-name>/            # Each flow in its own directory
│   ├── <flow-name>.json    # Flow export from LangFlow
│   └── <flow-name>.metadata.yaml # Optional metadata
└── README.md
```

## Flow Files

### Flow Definition (`.json`)

Exported directly from LangFlow UI:
1. Create flow in LangFlow
2. Click "Export" → "Download JSON"
3. Save to `<flow-name>/` directory

```json
{
  "name": "Flow Name",
  "description": "What the flow does",
  "data": {
    "nodes": [...],
    "edges": [...]
  }
}
```

### Metadata (`.metadata.yaml`) - Optional

Additional information for the platform:

```yaml
name: Flow Name
description: Brief description
version: 1.0.0
author: Author Name
tags:
  - research
  - chat
requires:
  - GEMINI_API_KEY
  - OPENAI_API_KEY
```

## Workflow

### Creating a New Flow

1. Start LangFlow in the platform: `make langflow-start`
2. Open http://localhost:7860
3. Create your flow using the visual builder
4. Test in the LangFlow playground
5. Export: Click "Export" → "Download JSON"
6. Save to `<name>/<name>.json` in this repo
7. Optionally add `<name>/<name>.metadata.yaml`
8. Commit and push

### Testing Import

From the platform repo:
```bash
# Copy the example config
cp config/flow-sources.yaml.example config/flow-sources.yaml

# Import flows (pulls from this repo)
make langflow-import
```

## Conventions

- **Flow names**: Use kebab-case (e.g., `simple-ollama/simple-ollama.json`)
- **One flow per file**: Each `.json` is a single flow
- **Metadata optional**: Only add if you need platform-specific info
- **Test before committing**: Verify flows work in LangFlow playground

## Related

- [Multi-Agent Platform](https://github.com/cfchase/multi-agent-platform) - The platform that uses these flows
- [LangFlow Documentation](https://docs.langflow.org/) - Official LangFlow docs
