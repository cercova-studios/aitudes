from google.adk.agents import LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import chrome_dev_tool


hacker_news_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="hacker_news_agent",
    instruction="Navigate to the Hacker News website and find the top 3 stories.",
    tools=[chrome_dev_tool],
)
