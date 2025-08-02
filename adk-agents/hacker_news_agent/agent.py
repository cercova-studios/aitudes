from dotenv import load_dotenv
import os

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

load_dotenv()

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

LLM_API_KEY = os.environ.get("GEMINI_API_KEY")
LLM_BASE_URL = os.environ.get("GEMINI_BASE_URL")

playwright_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "@playwright/mcp@latest", "--browser=firefox--headless"],
    )
)

hacker_news_agent = LlmAgent(
    model="gemini-2.5-flash-lite",
    name="hacker_news_agent",
    instruction="Navigate to the Hacker News website and find the top 10 stories.",
    tools=[google_search, playwright_tool],
    root_agent=True,
)
