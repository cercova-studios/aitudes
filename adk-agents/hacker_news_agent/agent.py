from dotenv import load_dotenv
import os

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

load_dotenv()

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
os.environ["GOOGLE_API_KEY"] = os.environ.get("GEMINI_API_KEY")

playwright_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="npx",
        args=["-y", "@playwright/mcp@latest", "--browser=firefox--headless"],
    )
)

hacker_news_agent = LlmAgent(
    model="gemini-2.5-flash-lite",
    name="hacker_news_agent",
    instruction="Navigate to the Hacker News website and find the top 3 stories.",
    tools=[playwright_tool],
)
