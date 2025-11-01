# API Reference

Complete API reference for the ADK agents module.

## Core Classes

### ParallelAgent

Coordinates multiple sub-agents to execute tasks in parallel.

#### Constructor

```python
ParallelAgent(
    model: str,
    name: str,
    instruction: str,
    sub_agents: List[LlmAgent],
    **kwargs
)
```

**Parameters:**

- `model` (str): The LLM model to use (e.g., "gemini-2.5-flash-lite")
- `name` (str): Unique identifier for the agent
- `instruction` (str): High-level instruction describing the agent's role
- `sub_agents` (List[LlmAgent]): List of sub-agents to coordinate
- `**kwargs`: Additional configuration parameters

**Example:**

```python
from google.adk.agents import ParallelAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.sub_agents import hacker_news_agent

router = ParallelAgent(
    model=GEMINI_MODEL,
    name="research_supervisor",
    instruction="Coordinate research across multiple sources",
    sub_agents=[hacker_news_agent],
)
```

#### Methods

##### `run(query: str, **kwargs) -> Response`

Execute the agent with a given query.

**Parameters:**
- `query` (str): The user query or task to execute
- `**kwargs`: Additional runtime parameters

**Returns:**
- `Response`: Aggregated response from all sub-agents

**Example:**

```python
result = router.run("What are the trending topics in AI?")
print(result)
```

##### `add_sub_agent(agent: LlmAgent) -> None`

Add a new sub-agent to the parallel agent.

**Parameters:**
- `agent` (LlmAgent): The sub-agent to add

**Example:**

```python
new_agent = LlmAgent(...)
router.add_sub_agent(new_agent)
```

### LlmAgent

Single-purpose agent with specific capabilities and tools.

#### Constructor

```python
LlmAgent(
    model: str,
    name: str,
    instruction: str,
    tools: Optional[List[MCPToolset]] = None,
    **kwargs
)
```

**Parameters:**

- `model` (str): The LLM model to use
- `name` (str): Unique identifier for the agent
- `instruction` (str): Specific task instruction for the agent
- `tools` (Optional[List[MCPToolset]]): List of MCP tools available to the agent
- `**kwargs`: Additional configuration parameters

**Example:**

```python
from google.adk.agents import LlmAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import chrome_dev_tool

agent = LlmAgent(
    model=GEMINI_MODEL,
    name="web_scraper",
    instruction="Navigate websites and extract information",
    tools=[chrome_dev_tool],
)
```

#### Methods

##### `run(query: str, **kwargs) -> Response`

Execute the agent with a given query.

**Parameters:**
- `query` (str): The task to execute
- `**kwargs`: Additional runtime parameters

**Returns:**
- `Response`: The agent's response

**Example:**

```python
result = agent.run("Get the top 5 stories from Hacker News")
```

### MCPToolset

Wrapper for Model Context Protocol tools.

#### Constructor

```python
MCPToolset(
    connection_params: StdioServerParameters
)
```

**Parameters:**

- `connection_params` (StdioServerParameters): Configuration for the MCP tool connection

**Example:**

```python
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
import os

tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "chrome-devtools-mcp@latest", "--headless=true"],
    )
)
```

#### Methods

##### `execute(request: Dict) -> Dict`

Execute a tool request.

**Parameters:**
- `request` (Dict): The tool request parameters

**Returns:**
- `Dict`: The tool response

### StdioServerParameters

Configuration for stdio-based MCP tool connections.

#### Constructor

```python
StdioServerParameters(
    command: str,
    args: List[str],
    env: Optional[Dict[str, str]] = None
)
```

**Parameters:**

- `command` (str): The command to execute (e.g., "bunx", "node")
- `args` (List[str]): Command-line arguments
- `env` (Optional[Dict[str, str]]): Environment variables for the process

**Example:**

```python
params = StdioServerParameters(
    command="bunx",
    args=["-y", "exa-mcp-server", "--tools=web_search_exa"],
    env={"EXA_API_KEY": os.getenv("EXA_API_KEY")}
)
```

## Pre-configured Agents

### hacker_news_agent

Agent for retrieving information from Hacker News.

**Module:** `research_agent.sub_agents.hn_agent`

**Type:** `LlmAgent`

**Capabilities:**
- Navigate to Hacker News website
- Extract top stories
- Retrieve story details and comments

**Tools:**
- `chrome_dev_tool`: Chrome DevTools MCP for web navigation

**Usage:**

```python
from research_agent.sub_agents import hacker_news_agent

result = hacker_news_agent.run("Get the top 3 stories from Hacker News")
```

### github_agent

Agent for searching and analyzing GitHub repositories.

**Module:** `research_agent.sub_agents.gh_agent`

**Type:** `LlmAgent`

**Status:** Defined in module structure (implementation in progress)

**Planned Capabilities:**
- Search GitHub repositories
- Analyze repository metrics
- Retrieve code samples

### web_search_agent

Agent for performing web searches.

**Module:** `research_agent.sub_agents.ws_agent`

**Type:** `LlmAgent`

**Status:** Defined in module structure (implementation in progress)

**Planned Capabilities:**
- Semantic web search
- Content summarization
- Source verification

### parquet_agent

Agent for querying Parquet data files.

**Module:** `research_agent.sub_agents.pq_agent`

**Type:** `LlmAgent`

**Status:** Defined in module structure (implementation in progress)

**Planned Capabilities:**
- Query Parquet files
- Data analysis
- Statistical summaries

### router_agent

Top-level parallel agent for coordinating research tasks.

**Module:** `research_agent.agent`

**Type:** `ParallelAgent`

**Sub-agents:**
- `hacker_news_agent`
- Additional agents as they are implemented

**Usage:**

```python
from research_agent import agent as router_agent

result = router_agent.run("Research the latest developments in AI")
```

## Pre-configured Tools

### chrome_dev_tool

Chrome DevTools MCP for browser automation.

**Module:** `research_agent.tools.tools`

**Type:** `MCPToolset`

**Configuration:**
```python
MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "chrome-devtools-mcp@latest", "--headless=true", "--isolated=true"],
    )
)
```

**Capabilities:**
- Navigate to URLs
- Execute JavaScript
- Extract DOM elements
- Take screenshots

**Example:**

```python
from research_agent.tools import chrome_dev_tool

# Used automatically by agents that include it in their tools list
agent = LlmAgent(
    model=GEMINI_MODEL,
    name="browser_agent",
    instruction="Browse the web and extract information",
    tools=[chrome_dev_tool],
)
```

### playwright_tool

Playwright MCP for advanced browser automation.

**Module:** `research_agent.tools.tools`

**Type:** `MCPToolset`

**Configuration:**
```python
MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "@playwright/mcp@latest", "--browser=firefox", "--headless"],
    )
)
```

**Capabilities:**
- Multi-browser support (Firefox, Chromium, WebKit)
- Network interception
- Mobile emulation
- File upload/download
- Advanced selectors

**Example:**

```python
from research_agent.tools import playwright_tool

agent = LlmAgent(
    model=GEMINI_MODEL,
    name="advanced_browser",
    instruction="Perform complex web interactions",
    tools=[playwright_tool],
)
```

### exa_tool

Exa AI-powered search MCP.

**Module:** `research_agent.tools.tools`

**Type:** `MCPToolset`

**Configuration:**
```python
MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "exa-mcp-server", "--tools=get_code_context_exa,web_search_exa,"],
        env={"EXA_API_KEY": os.getenv("EXA_API_KEY")},
    )
)
```

**Capabilities:**
- Semantic web search
- Code context retrieval
- Content summarization
- Source ranking

**Example:**

```python
from research_agent.tools import exa_tool

agent = LlmAgent(
    model=GEMINI_MODEL,
    name="search_agent",
    instruction="Search the web for relevant information",
    tools=[exa_tool],
)
```

## Configuration

### GEMINI_MODEL

Default Gemini model configuration.

**Module:** `research_agent.llm`

**Type:** `str`

**Value:** `"gemini-2.5-flash-lite"`

**Usage:**

```python
from research_agent.llm import GEMINI_MODEL

# Use default model
agent = LlmAgent(
    model=GEMINI_MODEL,
    name="my_agent",
    instruction="Do something",
)

# Or override with a different model
agent = LlmAgent(
    model="gemini-2.0-pro",
    name="my_agent",
    instruction="Do something",
)
```

## Type Definitions

### Response

Agent response type (from Google ADK).

**Attributes:**
- `content` (str): The response text
- `metadata` (Dict): Additional metadata about the response
- `status` (str): Response status (e.g., "success", "error")

### Task

Task definition for agents.

**Attributes:**
- `query` (str): The task query or instruction
- `context` (Dict): Additional context for the task
- `constraints` (Dict): Constraints or parameters for execution

### Result

Result from agent execution.

**Attributes:**
- `data` (Any): The result data
- `metadata` (Dict): Metadata about the execution
- `status` (str): Execution status
- `errors` (List[str]): Any errors encountered

## Error Types

### AgentError

Base exception for agent-related errors.

**Subclasses:**
- `ConfigurationError`: Configuration-related errors
- `ExecutionError`: Execution-related errors
- `ValidationError`: Validation-related errors

**Example:**

```python
from google.adk.agents import AgentError

try:
    result = agent.run(query)
except AgentError as e:
    print(f"Agent error: {e}")
```

### ToolExecutionError

Exception raised when a tool execution fails.

**Example:**

```python
try:
    result = agent.run(query)
except ToolExecutionError as e:
    print(f"Tool execution failed: {e}")
    # Implement fallback logic
```

### TimeoutError

Exception raised when an operation times out.

**Example:**

```python
try:
    result = agent.run(query, timeout=30)
except TimeoutError:
    print("Agent execution timed out")
    # Handle timeout
```

## Utility Functions

### load_dotenv

Load environment variables from .env file.

**Module:** `python-dotenv`

**Usage:**

```python
from dotenv import load_dotenv

load_dotenv()  # Load from .env in current directory
load_dotenv("/path/to/.env")  # Load from specific file
```

## Best Practices

### Agent Initialization

```python
# Good: Clear, specific instruction
agent = LlmAgent(
    model=GEMINI_MODEL,
    name="github_search",
    instruction="Search GitHub for repositories matching the query criteria and return the top 10 results with their metadata",
    tools=[github_tool],
)

# Avoid: Vague instruction
agent = LlmAgent(
    model=GEMINI_MODEL,
    name="search",
    instruction="Search for stuff",
    tools=[github_tool],
)
```

### Tool Selection

```python
# Good: Choose appropriate tools for the task
web_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="web_researcher",
    instruction="Research topics using web search and browsing",
    tools=[exa_tool, chrome_dev_tool],  # Both search and browsing
)

# Avoid: Including unnecessary tools
web_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="web_researcher",
    instruction="Research topics using web search",
    tools=[exa_tool, chrome_dev_tool, playwright_tool],  # Too many similar tools
)
```

### Error Handling

```python
# Good: Comprehensive error handling
from google.adk.agents import AgentError, TimeoutError

try:
    result = agent.run(query)
except TimeoutError:
    logger.error("Agent timed out, using cached results")
    result = cache.get(query)
except ToolExecutionError as e:
    logger.error(f"Tool failed: {e}, trying fallback")
    result = agent.run_with_fallback(query)
except AgentError as e:
    logger.error(f"Agent error: {e}")
    raise

# Avoid: Generic exception handling
try:
    result = agent.run(query)
except Exception as e:
    print(f"Error: {e}")  # Loses error context
```

### Resource Management

```python
# Good: Proper resource cleanup
from contextlib import contextmanager

@contextmanager
def agent_session(agent):
    try:
        yield agent
    finally:
        agent.cleanup()  # If cleanup method exists

with agent_session(my_agent) as agent:
    result = agent.run(query)

# Or with explicit cleanup
try:
    result = agent.run(query)
finally:
    # Clean up resources
    agent.close_connections()
```

## Examples

### Creating a Custom Research Agent

```python
from google.adk.agents import LlmAgent, ParallelAgent
from research_agent.llm import GEMINI_MODEL
from research_agent.tools import exa_tool, chrome_dev_tool

# Create specialized agents
news_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="news_researcher",
    instruction="Search for recent news articles on the given topic",
    tools=[exa_tool],
)

tech_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="tech_researcher",
    instruction="Research technical documentation and code examples",
    tools=[exa_tool, chrome_dev_tool],
)

# Create coordinator
research_coordinator = ParallelAgent(
    model=GEMINI_MODEL,
    name="research_coordinator",
    instruction="Coordinate research across news and technical sources",
    sub_agents=[news_agent, tech_agent],
)

# Use the coordinator
result = research_coordinator.run("Research the latest developments in quantum computing")
```

### Custom Tool Integration

```python
import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Create custom tool
custom_api_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command="bunx",
        args=["-y", "my-custom-mcp-server"],
        env={
            "API_KEY": os.getenv("MY_API_KEY"),
            "API_ENDPOINT": "https://api.example.com"
        }
    )
)

# Use in agent
custom_agent = LlmAgent(
    model=GEMINI_MODEL,
    name="custom_agent",
    instruction="Use the custom API to fetch data",
    tools=[custom_api_tool],
)
```

## Changelog

### Current Version

**Features:**
- ParallelAgent for coordinating sub-agents
- LlmAgent for single-purpose tasks
- MCP tool integration (Chrome DevTools, Playwright, Exa)
- Research agent with Hacker News support

**In Progress:**
- GitHub agent implementation
- Web search agent implementation
- Parquet agent implementation

**Planned:**
- Additional MCP tool integrations
- Agent state persistence
- Conversation history
- Metrics and monitoring
- Enhanced error handling

## See Also

- [Architecture Guide](./architecture.md) - System architecture and design
- [README](./README.md) - Getting started guide
- [Google ADK Documentation](https://cloud.google.com/vertex-ai/docs/agents)
- [MCP Documentation](https://modelcontextprotocol.io/)
