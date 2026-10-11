# opencpt-mcp

[MCP](https://modelcontextprotocol.io) server exposing [opencpt](https://pypi.org/project/opencpt/) CPT (cone penetration test) analysis tools to LLM clients.

```bash
uvx opencpt-mcp
```

## Claude Code

```bash
claude mcp add opencpt -- uvx opencpt-mcp
```

## Claude Desktop

```json
{
  "mcpServers": {
    "opencpt": {
      "command": "uvx",
      "args": ["opencpt-mcp"]
    }
  }
}
```

Early placeholder release. Tools under development.
