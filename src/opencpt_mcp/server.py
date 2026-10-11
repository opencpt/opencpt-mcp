"""MCP server entry point. Tools wrap opencpt functions."""

import opencpt
from mcp.server.mcpserver import MCPServer

from opencpt_mcp import __version__

mcp = MCPServer("opencpt")


@mcp.tool()
def version() -> dict:
    """Return opencpt and opencpt-mcp versions."""
    return {"opencpt": opencpt.__version__, "opencpt_mcp": __version__}


def main() -> None:
    mcp.run()  # stdio transport


if __name__ == "__main__":
    main()
