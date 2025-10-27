# ADK Agents Documentation

This documentation covers the Agent Development Kit (ADK) agents built with Google's ADK framework.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Research Agent](#research-agent)
- [Sub-Agents](#sub-agents)
- [Tools](#tools)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Examples](#examples)

## Overview

The ADK agents module (`adk-agents`) provides a collection of specialized agents built using Google's Agent Development Kit. These agents leverage the Gemini models and various tools to perform research and data gathering tasks.

### Key Features

- **Modular Design**: Agents are composed of sub-agents with specific responsibilities
- **Parallel Processing**: ParallelAgent allows concurrent execution of sub-agents
- **MCP Integration**: Integration with Model Context Protocol (MCP) tools
- **Extensible Architecture**: Easy to add new agents and tools

## Architecture

The ADK agents follow a hierarchical architecture:

```
research_agent (ParallelAgent)
├── Router & Supervisor
└── Sub-Agents (LlmAgent)
    ├── Hacker News Agent
    ├── GitHub Agent
    ├── Web Search Agent
    └── Parquet Agent
```

### Core Components

1. **Router Agent**: Top-level ParallelAgent that delegates tasks to specialized sub-agents
2. **Sub-Agents**: Specialized LlmAgents focused on specific data sources or tasks
3. **Tools**: MCP toolsets providing capabilities like web browsing and search
4. **LLM Configuration**: Shared Gemini model configuration

## Research Agent

The research agent is a parallel agent that coordinates multiple sub-agents to perform comprehensive research tasks.

### Structure

```python
from google.adk.agents import ParallelAgent
from .llm import GEMINI_MODEL
from .sub_agents import hacker_news_agent

router_agent = ParallelAgent(
    model=GEMINI_MODEL,
    name="research_supervisor",
    instruction="Delegate research tasks to the respective subagents.",
    sub_agents=[hacker_news_agent],
)
```

### Features

- **Parallel Execution**: Runs multiple sub-agents concurrently
- **Task Delegation**: Routes research queries to appropriate sub-agents
- **Result Aggregation**: Combines results from multiple sources

### Usage

```python
from research_agent import agent

# Use the research agent
result = agent.run("Find the top stories on Hacker News")
```

## Sub-Agents

The research agent includes several specialized sub-agents:

### Hacker News Agent

**Purpose**: Navigate to Hacker News and retrieve top stories

**File**: `adk-agents/research_agent/sub_agents/hn_agent.py`

```python
from google.adk.agents import LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import chrome_dev_tool

hacker_news_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="hacker_news_agent",
    instruction="Navigate to the Hacker News website and find the top 3 stories.",
    tools=[chrome_dev_tool],
)
```

**Capabilities**:
- Web navigation using Chrome DevTools
- Story extraction and ranking
- Content summarization

### GitHub Agent

**Purpose**: Search and analyze GitHub repositories

**File**: `adk-agents/research_agent/sub_agents/gh_agent.py`

**Status**: Defined in module structure (implementation in progress)

### Web Search Agent

**Purpose**: Perform general web searches

**File**: `adk-agents/research_agent/sub_agents/ws_agent.py`

**Status**: Defined in module structure (implementation in progress)

### Parquet Agent

**Purpose**: Query and analyze Parquet data files

**File**: `adk-agents/research_agent/sub_agents/pq_agent.py`

**Status**: Defined in module structure (implementation in progress)

## Tools

The agents use Model Context Protocol (MCP) tools for various capabilities:

### Available Tools

#### Chrome DevTools MCP

**Purpose**: Browser automation and web scraping

```python
chrome_dev_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "chrome-devtools-mcp@latest", "--headless=true", "--isolated=true"],
    )
)
```

**Capabilities**:
- Headless browser navigation
- DOM inspection and interaction
- JavaScript execution
- Screenshot capture

#### Playwright MCP

**Purpose**: Advanced browser automation

```python
playwright_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "@playwright/mcp@latest", "--browser=firefox", "--headless"],
    )
)
```

**Capabilities**:
- Multi-browser support (Firefox, Chromium, WebKit)
- Network interception
- Mobile emulation
- File upload/download

#### Exa Search MCP

**Purpose**: AI-powered web search and code context retrieval

```python
exa_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "exa-mcp-server", "--tools=get_code_context_exa,web_search_exa,"],
        env={"EXA_API_KEY": os.getenv("EXA_API_KEY")},
    )
)
```

**Capabilities**:
- Semantic web search
- Code context extraction
- Content summarization

### Adding New Tools

To add a new MCP tool:

1. Define the tool in `tools/tools.py`:

```python
new_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "your-mcp-server"],
        env={"API_KEY": os.getenv("YOUR_API_KEY")},
    )
)
```

2. Add the tool to an agent:

```python
agent = LlmAgent(
    model=GEMINI_MODEL,
    name="your_agent",
    instruction="Your agent instructions",
    tools=[new_tool],
)
```

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js (for MCP tools via bunx)
- Required environment variables:
  - `EXA_API_KEY` (for Exa search)
  - Google Cloud credentials (for Gemini)

### Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up environment variables:

```bash
# Create .env file
echo "EXA_API_KEY=your_key_here" > .env
```

3. Install MCP tool dependencies:

```bash
# These will be automatically installed when agents run
# But you can pre-install them:
bunx -y chrome-devtools-mcp@latest
bunx -y @playwright/mcp@latest
bunx -y exa-mcp-server
```

### Basic Usage

```python
from dotenv import load_dotenv
from research_agent import agent

# Load environment variables
load_dotenv()

# Run the research agent
result = agent.run("Research the latest AI developments")
print(result)
```

## Configuration

### LLM Configuration

The default model is configured in `llm.py`:

```python
GEMINI_MODEL = "gemini-2.5-flash-lite"
```

To use a different model, update this configuration or override when creating agents:

```python
from google.adk.agents import LlmAgent

custom_agent = LlmAgent(
    model="gemini-2.0-pro",  # Override default
    name="custom_agent",
    instruction="Your instructions",
)
```

### Environment Variables

Required environment variables:

- `EXA_API_KEY`: API key for Exa search service
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to Google Cloud credentials (if not using default)

Optional environment variables:

- `AITUDES_ENV`: Development environment (development/production)
- `LOG_LEVEL`: Logging level (debug/info/warning/error)

## Examples

### Example 1: Simple Research Query

```python
from dotenv import load_dotenv
from research_agent import agent

load_dotenv()

# Research a topic
result = agent.run("What are the top stories on Hacker News today?")
print(result)
```

### Example 2: Creating a Custom Agent

```python
from google.adk.agents import LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import exa_tool

# Create a custom research agent
custom_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="code_researcher",
    instruction="Search for code examples and provide context about their usage.",
    tools=[exa_tool],
)

# Use the custom agent
result = custom_agent.run("Find examples of FastAPI middleware implementation")
print(result)
```

### Example 3: Parallel Agent with Multiple Sub-Agents

```python
from google.adk.agents import ParallelAgent, LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.sub_agents import hacker_news_agent

# Create additional sub-agents
tech_news_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="tech_news_agent",
    instruction="Find latest tech news from various sources",
)

# Create parallel agent
multi_source_agent = ParallelAgent(
    model=GEMINI_MODEL,
    name="multi_source_researcher",
    instruction="Gather information from multiple sources and synthesize results.",
    sub_agents=[hacker_news_agent, tech_news_agent],
)

# Run parallel research
result = multi_source_agent.run("What are the current AI trends?")
```

## Advanced Topics

### Agent Composition

Agents can be composed hierarchically:

```python
# Level 1: Specialized agents
data_agent = LlmAgent(...)
web_agent = LlmAgent(...)

# Level 2: Domain-specific coordinator
tech_coordinator = ParallelAgent(
    sub_agents=[data_agent, web_agent]
)

# Level 3: Top-level orchestrator
master_agent = ParallelAgent(
    sub_agents=[tech_coordinator, other_coordinator]
)
```

### Error Handling

Implement robust error handling:

```python
try:
    result = agent.run(query)
except Exception as e:
    logger.error(f"Agent execution failed: {e}")
    # Implement fallback logic
```

### Performance Optimization

- Use parallel agents for independent tasks
- Cache frequently accessed data
- Implement timeouts for long-running operations
- Monitor token usage with Gemini models

## Best Practices

1. **Clear Instructions**: Provide specific, actionable instructions to agents
2. **Tool Selection**: Choose appropriate tools for the task
3. **Error Handling**: Always implement error handling and fallbacks
4. **Environment Management**: Use `.env` files for sensitive credentials
5. **Testing**: Test agents with various inputs before production use
6. **Monitoring**: Log agent activities and track performance metrics
7. **Resource Management**: Be mindful of API rate limits and costs

## Troubleshooting

### Common Issues

**Issue**: MCP tools fail to start

**Solution**: Ensure Node.js and bunx are properly installed:
```bash
node --version
bunx --version
```

**Issue**: Authentication errors with Google Cloud

**Solution**: Verify credentials are properly configured:
```bash
echo $GOOGLE_APPLICATION_CREDENTIALS
# Should point to valid credentials file
```

**Issue**: Exa API errors

**Solution**: Check API key is set:
```bash
echo $EXA_API_KEY
# Should display your API key
```

## API Reference

### Core Classes

#### ParallelAgent

```python
ParallelAgent(
    model: str,
    name: str,
    instruction: str,
    sub_agents: List[LlmAgent],
)
```

Coordinates multiple sub-agents to execute tasks in parallel.

#### LlmAgent

```python
LlmAgent(
    model: str,
    name: str,
    instruction: str,
    tools: List[MCPToolset] = None,
)
```

Single-purpose agent with specific capabilities and tools.

#### MCPToolset

```python
MCPToolset(
    connection_params: StdioServerParameters
)
```

Wraps Model Context Protocol tools for agent use.

## Future Enhancements

Planned improvements to the ADK agents:

- [ ] Complete implementation of GitHub Agent
- [ ] Complete implementation of Web Search Agent
- [ ] Complete implementation of Parquet Agent
- [ ] Add agent state persistence
- [ ] Implement agent conversation history
- [ ] Add metrics and monitoring dashboard
- [ ] Create agent testing framework
- [ ] Add more MCP tool integrations
- [ ] Implement agent chaining and workflows

## Contributing

To contribute new agents or improvements:

1. Follow the existing agent structure
2. Add comprehensive documentation
3. Include usage examples
4. Write tests for new functionality
5. Submit a pull request with clear description

## Resources

- [Google ADK Documentation](https://cloud.google.com/vertex-ai/docs/agents)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Aitudes Main Documentation](../../README.md)

## Support

For questions or issues:

- Check the [Troubleshooting](#troubleshooting) section
- Review the [Development Guide](../../DEVELOPMENT_GUIDE.md)
- Open an issue on GitHub
- Refer to the [Agent Development Guidelines](../../AGENT.md)
