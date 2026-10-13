# git-mcp-parser
A JSON parser that recursively searches all subdirectories starting from a given path, identifies Git repositories, and parses them into the appropriate JSON format so that you can use the [git MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/git) to make these repositories available to your AI.

## Customization

Please edit the `git_mcp_parser.py` file and change the search path / target directory:

```
target_directory = r"C:\Users\Admin\Dokumente\GitHub"  # Example path—please adjust as needed
```
