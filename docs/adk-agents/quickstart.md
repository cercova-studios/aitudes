# Quick Start Guide

Get up and running with ADK agents in minutes.

## Prerequisites

Before you begin, ensure you have:

- Python 3.11 or higher
- Node.js (for MCP tools via bunx)
- Git
- A Google Cloud account (for Gemini API access)
- Exa API key (optional, for Exa search tool)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/cercova-studios/aitudes.git
cd aitudes
```

### 2. Set Up Python Environment

Using the Nix flake (recommended):

```bash
# Install Nix with flakes support if not already installed
# See https://nixos.org/download.html

# Enter the development environment
nix develop
```

Or using traditional pip:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Create .env file
cat > .env << EOF
# Exa API (optional, for web search features)
EXA_API_KEY=your_exa_api_key_here

# Google Cloud (for Gemini models)
# Option 1: Use application default credentials
# gcloud auth application-default login

# Option 2: Specify credentials file
# GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

# Development settings
AITUDES_ENV=development
LOG_LEVEL=debug
EOF
```

### 4. Install MCP Tool Dependencies

The MCP tools will be automatically installed when first used, but you can pre-install them:

```bash
# Install Chrome DevTools MCP
bunx -y chrome-devtools-mcp@latest

# Install Playwright MCP
bunx -y @playwright/mcp@latest

# Install Exa MCP (requires API key)
bunx -y exa-mcp-server
```

## Your First Agent

### Hello World Example

Create a file named `hello_agent.py`:

```python
from dotenv import load_dotenv
from research_agent.sub_agents import hacker_news_agent

# Load environment variables
load_dotenv()

# Run the agent
result = hacker_news_agent.run("What are the top 3 stories on Hacker News?")
print(result)
```

Run the script:

```bash
python hello_agent.py
```

### Understanding the Output

The agent will:
1. Navigate to Hacker News using Chrome DevTools
2. Extract the top 3 stories
3. Return the results with titles, URLs, and metadata

## Common Tasks

### Task 1: Research a Topic

Use the research supervisor to coordinate multiple sources:

```python
from dotenv import load_dotenv
from research_agent import agent as research_agent

load_dotenv()

# Research a broad topic
query = "What are the latest trends in AI agents?"
result = research_agent.run(query)

print(f"Research Results:\n{result}")
```

### Task 2: Create a Custom Agent

Build an agent tailored to your needs:

```python
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import chrome_dev_tool

load_dotenv()

# Create a custom agent
my_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="tech_news_agent",
    instruction="Find the latest technology news and summarize the top stories",
    tools=[chrome_dev_tool],
)

# Use the agent
result = my_agent.run("Get tech news from TechCrunch")
print(result)
```

### Task 3: Use Multiple Tools

Combine different tools for more capabilities:

```python
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import exa_tool, chrome_dev_tool

load_dotenv()

# Agent with search and browsing capabilities
research_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="comprehensive_researcher",
    instruction="Research topics using both search and direct website access",
    tools=[exa_tool, chrome_dev_tool],
)

result = research_agent.run("Research recent developments in quantum computing")
print(result)
```

### Task 4: Build a Parallel Agent

Coordinate multiple agents to work together:

```python
from dotenv import load_dotenv
from google.adk.agents import LlmAgent, ParallelAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import chrome_dev_tool
from research_agent.sub_agents import hacker_news_agent

load_dotenv()

# Create another specialized agent
reddit_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="reddit_agent",
    instruction="Navigate to Reddit and find top posts on a topic",
    tools=[chrome_dev_tool],
)

# Create parallel coordinator
multi_source_agent = ParallelAgent(
    model=GEMINI_MODEL,
    name="multi_source_coordinator",
    instruction="Gather information from multiple social news sources",
    sub_agents=[hacker_news_agent, reddit_agent],
)

result = multi_source_agent.run("What are people discussing about AI today?")
print(result)
```

## Project Structure

Understanding where things are:

```
aitudes/
├── adk-agents/                    # ADK agents module
│   ├── __init__.py
│   └── research_agent/           # Research agent package
│       ├── __init__.py           # Package exports
│       ├── agent.py              # Main router agent
│       ├── llm.py                # Model configuration
│       ├── sub_agents/           # Sub-agent implementations
│       │   ├── __init__.py
│       │   ├── hn_agent.py       # Hacker News agent
│       │   ├── gh_agent.py       # GitHub agent (planned)
│       │   ├── ws_agent.py       # Web search agent (planned)
│       │   └── pq_agent.py       # Parquet agent (planned)
│       └── tools/                # MCP tool configurations
│           ├── __init__.py
│           └── tools.py          # Tool definitions
│
├── docs/                         # Documentation
│   ├── README.md                # Docs overview
│   └── adk-agents/              # ADK agents docs
│       ├── README.md            # ADK agents guide
│       ├── quickstart.md        # This file
│       ├── architecture.md      # Architecture details
│       └── api-reference.md     # API documentation
│
├── .env                         # Environment variables (create this)
├── .envrc                       # direnv configuration
├── pyproject.toml              # Project dependencies
└── requirements.txt            # Pip dependencies
```

## Configuration Options

### Model Selection

Choose different Gemini models:

```python
# Fast, lightweight (default)
model = "gemini-2.5-flash-lite"

# More powerful
model = "gemini-2.0-pro"

# Use in agent
agent = LlmAgent(
    model=model,  # Your choice
    name="my_agent",
    instruction="Do something",
)
```

### Tool Selection

Available MCP tools:

```python
from research_agent.tools import (
    chrome_dev_tool,    # Chrome DevTools - web browsing
    playwright_tool,    # Playwright - advanced automation
    exa_tool,          # Exa - AI search
)

# Use what you need
tools = [chrome_dev_tool]           # Just browsing
tools = [exa_tool]                  # Just search
tools = [exa_tool, chrome_dev_tool] # Both
```

### Environment Variables

Key environment variables:

```bash
# Required for Exa tool
EXA_API_KEY=your_key

# Google Cloud authentication (choose one)
# Option 1: Default credentials (recommended)
# Run: gcloud auth application-default login

# Option 2: Service account
GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json

# Optional development settings
AITUDES_ENV=development
LOG_LEVEL=debug
PYTHONDONTWRITEBYTECODE=1
```

## Troubleshooting

### Issue: Module not found

**Error:**
```
ModuleNotFoundError: No module named 'google.adk'
```

**Solution:**
```bash
# Ensure you're in the correct environment
nix develop  # If using Nix
# OR
source venv/bin/activate  # If using venv

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: MCP tool fails to start

**Error:**
```
Failed to start MCP tool: chrome-devtools-mcp
```

**Solution:**
```bash
# Check Node.js and bunx are installed
node --version
bunx --version

# If not, install bunx
npm install -g bun

# Manually test the tool
bunx -y chrome-devtools-mcp@latest --help
```

### Issue: Authentication errors

**Error:**
```
google.auth.exceptions.DefaultCredentialsError
```

**Solution:**
```bash
# Set up Google Cloud authentication
gcloud auth application-default login

# Or set credentials file
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```

### Issue: Exa API errors

**Error:**
```
EXA_API_KEY not found
```

**Solution:**
```bash
# Get API key from https://exa.ai/
# Add to .env file
echo "EXA_API_KEY=your_key_here" >> .env

# Reload environment
source .env  # Or restart your script
```

### Issue: Agent timeout

**Error:**
```
TimeoutError: Agent execution timed out
```

**Solution:**
```python
# Increase timeout
result = agent.run(query, timeout=60)  # 60 seconds

# Or implement retry logic
from time import sleep

max_retries = 3
for i in range(max_retries):
    try:
        result = agent.run(query)
        break
    except TimeoutError:
        if i < max_retries - 1:
            sleep(2 ** i)  # Exponential backoff
        else:
            raise
```

## Next Steps

Now that you're up and running:

1. **Explore Examples**: Check out more examples in the [main documentation](./README.md#examples)
2. **Learn the Architecture**: Understand how things work in the [Architecture Guide](./architecture.md)
3. **API Reference**: Dive deep into the [API Reference](./api-reference.md)
4. **Build Custom Agents**: Create agents tailored to your needs
5. **Contribute**: Add new agents or improve existing ones

## Additional Resources

- [Main Documentation](./README.md) - Comprehensive guide
- [Architecture Guide](./architecture.md) - System design
- [API Reference](./api-reference.md) - Complete API docs
- [Development Guide](../../DEVELOPMENT_GUIDE.md) - Development workflow
- [Agent Guidelines](../../AGENT.md) - Agent development best practices

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [main documentation](./README.md)
3. Check existing GitHub issues
4. Open a new issue with:
   - Your environment (OS, Python version)
   - Error messages
   - Steps to reproduce
   - Expected vs actual behavior

## Example Projects

### Project 1: News Aggregator

```python
# news_aggregator.py
from dotenv import load_dotenv
from google.adk.agents import ParallelAgent, LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.sub_agents import hacker_news_agent
from research_agent.tools import chrome_dev_tool

load_dotenv()

# Create additional news agents
tech_news = LlmAgent(
    model=GEMINI_MODEL,
    name="tech_news",
    instruction="Get top stories from TechCrunch",
    tools=[chrome_dev_tool],
)

# Coordinator
news_aggregator = ParallelAgent(
    model=GEMINI_MODEL,
    name="news_aggregator",
    instruction="Aggregate news from multiple tech sources",
    sub_agents=[hacker_news_agent, tech_news],
)

# Run daily
if __name__ == "__main__":
    result = news_aggregator.run("What are today's top tech stories?")
    print(result)
```

### Project 2: Research Assistant

```python
# research_assistant.py
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import exa_tool, chrome_dev_tool

load_dotenv()

# Create research assistant
assistant = LlmAgent(
    model=GEMINI_MODEL,
    name="research_assistant",
    instruction="""
    You are a research assistant. When given a topic:
    1. Search for recent articles and papers
    2. Visit key websites for detailed information
    3. Summarize findings with sources
    4. Highlight key insights and trends
    """,
    tools=[exa_tool, chrome_dev_tool],
)

# Interactive mode
if __name__ == "__main__":
    while True:
        topic = input("\nResearch topic (or 'quit' to exit): ")
        if topic.lower() == 'quit':
            break
        
        print("\nResearching...\n")
        result = assistant.run(f"Research: {topic}")
        print(result)
```

## Success! 🎉

You're now ready to build with ADK agents. Start experimenting, building, and contributing!

Remember:
- Start simple, then add complexity
- Use the documentation when stuck
- Experiment with different tools and models
- Share your creations with the community

Happy coding! 🚀
