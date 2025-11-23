import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from dotenv import load_dotenv

load_dotenv()

EXA_API_KEY = os.getenv("EXA_API_KEY")
if not EXA_API_KEY:
    raise ValueError(
        "EXA_API_KEY environment variable is required for exa_tool. "
        "Please set it in your .env file or environment."
    )

exa_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "exa-mcp-server", "--tools=get_code_context_exa,web_search_exa"],
        env={"EXA_API_KEY": EXA_API_KEY},
    )
)

playwright_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "@playwright/mcp@latest", "--browser=firefox", "--headless"],
    )
)

chrome_dev_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "chrome-devtools-mcp@latest", "--headless=true", "--isolated=true"],
    )
)
