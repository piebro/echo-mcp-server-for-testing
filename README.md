# echo-mcp-server-for-testing

A simple echo MCP (Model Context Protocol) Server with a simple `echo_tool` for testing MCP Clients.
It is also great as a template for new MCP Servers.

## Usage

Install [uv](https://docs.astral.sh/uv/) and add the server to an MCP config using `uvx`:

```json
{
    "name": "echo-mcp-server-for-testing",
    "command": "uvx",
    "args": [
        "echo-mcp-server-for-testing"
    ],
    "env": {
        "SECRET_KEY": "123456789"
    }
}
```

or clone the repo and use `uv` with a directory:

```json
{
    "name": "echo-mcp-server-for-testing",
    "command": "uv",
    "args": [
        "--directory",
        "path/to/root/dir/",
        "run",
        "main.py"
    ],
    "env": {
        "SECRET_KEY": "123456789"
    }
}
```

## Development

### Testing

Clone the repo and use [mcp-client-for-testing](https://github.com/piebro/mcp-client-for-testing) to test the tools of the server.

```bash
uvx mcp-client-for-testing \
    --config '
    [
        {
            "name": "echo-mcp-server-for-testing",
            "command": "uv",
            "args": [
                "--directory", 
                "path/to/root/dir/", 
                "run", 
                "main.py"
            ],
            "env": {
                "SECRET_KEY": "123456789"
            }
        }
    ]
    ' \
    --tool_call '{"name": "echo_tool", "arguments": {"message": "Hello, world!"}}'
```

### Formatting and Linting

The code is formatted and linted with ruff:

```bash
uv run ruff format
uv run ruff check --fix
```

### Building with uv

Build the package using uv:

```bash
uv build
```

### Releasing a New Version

To release a new version of the package to PyPI, create and push a new Git tag:

1. Checkout the main branch and get the current version:
   ```bash
   git checkout main
   git pull origin main
   git describe --tags
   ```

2. Create and push a new Git tag:
   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

The GitHub Actions workflow will automatically build and publish the package to PyPI when a new tag is pushed.
The python package version number will be derived directly from the Git tag.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.