import json
from pathlib import Path

def generate_git_mcp_config(root_dir):
    root_path = Path(root_dir).resolve()
    mcp_servers = {}
    
    # Recursively searches all subfolders for .git directories
    for git_dir in root_path.rglob('.git'):
        if git_dir.is_dir():
            repo_path = git_dir.parent
            repo_name = repo_path.name  # Name des Projektordners als Key
            
            # Set up the MCP structure for this repo
            mcp_servers[repo_name] = {
                "command": "python",
                "args": [
                    "-m",
                    "mcp_server_git",
                    "--repository",
                    str(repo_path)  # Automatically converts the path
                ]
            }
            
    # Wrap it in the outer object
    config = {"mcpServers": mcp_servers}
    
    # `json.dumps` automatically ensures that Windows backslashes are escaped correctly (e.g., \\)
    return json.dumps(config, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    # Adjust your startup path here (the ‘r’ before the string prevents escape errors with Windows paths)
    target_directory = r"C:\Users\Admin\Dokumente\GitHub"  # Example path—please adjust as needed
    
    print(f"Searching for Git repositories in '{target_directory}'...\n")
    json_output = generate_git_mcp_config(target_directory)
    print(json_output)
