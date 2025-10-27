from google.adk.agents import ParallelAgent
from .llm import GEMINI_MODEL
from dotenv import load_dotenv
from .sub_agents import hacker_news_agent

load_dotenv()


router_agent = ParallelAgent(
    model=GEMINI_MODEL,
    name="research_supervisor",
    instruction="Delegate research tasks to the respective subagents.",
    sub_agents=[hacker_news_agent],
)
