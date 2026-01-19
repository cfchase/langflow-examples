# LangFlow Examples

Example flows and custom components for use with [Multi-Agent Platform](https://github.com/cfchase/multi-agent-platform).

## Structure

```
├── flows/           # LangFlow flow definitions (.json)
│   └── hello-gemini.json
├── components/      # Custom LangFlow components (Python)
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
    path: flows
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
| `hello-gemini` | Simple greeting flow using Google Gemini |

## Custom Components

Custom components can be added to the `components/` directory. See [LangFlow Custom Components](https://docs.langflow.org/components-custom-components) for documentation.

## Contributing

1. Create/edit flows in LangFlow UI
2. Export as JSON to `flows/`
3. Add metadata file (optional): `flows/<name>.metadata.yaml`
4. Submit PR

## License

Apache License 2.0
