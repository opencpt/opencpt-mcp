import asyncio


def test_import():
    import opencpt_mcp

    assert opencpt_mcp.__version__


def test_version_tool_registered():
    from opencpt_mcp.server import mcp

    names = [t.name for t in asyncio.run(mcp.list_tools())]
    assert "version" in names
