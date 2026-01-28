# LangFlow Examples

Example flows for use with [Multi-Agent Platform](https://github.com/cfchase/multi-agent-platform).

## Structure

```
├── simple-ollama/       # Simple Ollama agent example
│   └── simple-ollama.json
└── README.md
```

## Usage

### Import into Multi-Agent Platform

Add this repository to your `config/flow-sources.yaml`:

```yaml
sources:
  - name: examples
    type: git
    url: https://github.com/cfchase/langflow-examples
```

Then run:

```bash
make langflow-import
```

### Manual Import

1. Start LangFlow: `make langflow-start`
2. Open http://localhost:7860
3. Click "Import" and select a flow JSON file

## Flows

| Flow | Description |
|------|-------------|
| `simple-ollama` | Simple agent with calculator and URL tools using local Ollama |

## Contributing

1. Create/edit flows in LangFlow UI
2. Export as JSON to `<flow-name>/<flow-name>.json`
3. Add metadata file (optional): `<flow-name>/<flow-name>.metadata.yaml`
4. Submit PR

## License

Apache License 2.0
