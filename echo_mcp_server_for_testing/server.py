import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Echo")


@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    SECRET_KEY = os.getenv("SECRET_KEY", "No secret key found")
    return f"Tool echo: {message}. The environment variable SECRET_KEY is: {SECRET_KEY}"


def main():
    mcp.run()


if __name__ == "__main__":
    main()
