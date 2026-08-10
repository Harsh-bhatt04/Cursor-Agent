from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Coding Agent")


@mcp.tool()
def hello(name: str) -> str:
    """Say hello."""
    return f"Hello {name}!"


if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run()