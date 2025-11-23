# Architecture Guide

This document provides an in-depth look at the architecture of the ADK agents system.

## System Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Research Supervisor                      │
│                   (ParallelAgent)                           │
│                                                             │
│  - Routes queries to appropriate sub-agents                 │
│  - Aggregates results from multiple sources                 │
│  - Coordinates parallel execution                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
         ┌────────────┴────────────┬─────────────┬─────────────┐
         │                         │             │             │
         ▼                         ▼             ▼             ▼
┌─────────────────┐   ┌──────────────────┐   ┌────────┐   ┌────────┐
│ Hacker News     │   │ GitHub Agent     │   │  Web   │   │Parquet │
│ Agent           │   │                  │   │ Search │   │ Agent  │
│ (LlmAgent)      │   │ (LlmAgent)       │   │ Agent  │   │        │
│                 │   │                  │   │        │   │        │
│ - Chrome Dev    │   │ - GitHub API     │   │ - Exa  │   │ - Data │
│   Tools         │   │   Integration    │   │   Tool │   │  Query │
└─────────────────┘   └──────────────────┘   └────────┘   └────────┘
         │                         │              │            │
         └─────────────┬───────────┴──────────────┴────────────┘
                       ▼
              ┌─────────────────┐
              │  MCP Toolsets   │
              │                 │
              │ - Chrome DevTools│
              │ - Playwright    │
              │ - Exa Search    │
              └─────────────────┘
```

## Design Principles

### 1. Separation of Concerns

Each component has a single, well-defined responsibility:

- **Router Agent**: Task delegation and result aggregation
- **Sub-Agents**: Domain-specific data gathering
- **Tools**: Low-level capabilities (web browsing, API access)
- **LLM Configuration**: Model settings and parameters

### 2. Modularity

Components are designed to be:

- **Independently testable**: Each agent can be tested in isolation
- **Loosely coupled**: Agents communicate through well-defined interfaces
- **Easily replaceable**: Components can be swapped without affecting others

### 3. Extensibility

The architecture supports easy extension:

- **New Agents**: Add sub-agents without modifying existing code
- **New Tools**: Integrate new MCP tools with minimal configuration
- **New Models**: Switch between different LLM models easily

### 4. Parallel Processing

The system leverages parallelism:

- **Concurrent Execution**: Sub-agents run simultaneously
- **Resource Efficiency**: Maximize throughput for independent tasks
- **Scalability**: Handle multiple research queries efficiently

## Component Details

### ParallelAgent (Router)

**Responsibilities:**
- Receive high-level research queries
- Determine which sub-agents to involve
- Execute sub-agents in parallel
- Aggregate and synthesize results
- Return coherent response

**Implementation Pattern:**

```python
class ResearchSupervisor(ParallelAgent):
    def __init__(self):
        super().__init__(
            model=GEMINI_MODEL,
            name="research_supervisor",
            instruction="Delegate research tasks...",
            sub_agents=[
                hacker_news_agent,
                github_agent,
                # ... other agents
            ],
        )
    
    def route_query(self, query: str) -> List[Agent]:
        """Determine which agents to activate"""
        pass
    
    def aggregate_results(self, results: List[Result]) -> Response:
        """Combine results from multiple agents"""
        pass
```

### LlmAgent (Sub-Agents)

**Responsibilities:**
- Focus on specific data source or task type
- Use appropriate tools for the task
- Return structured results
- Handle domain-specific errors

**Implementation Pattern:**

```python
class SpecializedAgent(LlmAgent):
    def __init__(self, tools: List[Tool]):
        super().__init__(
            model=GEMINI_MODEL,
            name="specialized_agent",
            instruction="Specific task instructions...",
            tools=tools,
        )
    
    def execute(self, query: str) -> Result:
        """Execute domain-specific task"""
        pass
    
    def validate_result(self, result: Result) -> bool:
        """Ensure result meets quality standards"""
        pass
```

### MCP Tools

**Responsibilities:**
- Provide low-level capabilities
- Abstract tool-specific details
- Handle connection management
- Report errors clearly

**Implementation Pattern:**

```python
def create_mcp_tool(
    name: str,
    command: str,
    args: List[str],
    env: Dict[str, str] = None
) -> MCPToolset:
    """Factory for creating MCP tools"""
    return MCPToolset(
        connection_params=StdioServerParameters(
            command=command,
            args=args,
            env=env or {},
        )
    )
```

## Data Flow

### Query Processing Flow

```
1. User Query
   │
   ├─> Research Supervisor receives query
   │
   ├─> Analyze query to determine required sub-agents
   │
   ├─> Dispatch to sub-agents in parallel
   │   │
   │   ├─> Hacker News Agent
   │   │   └─> Chrome DevTools MCP
   │   │       └─> Navigate, extract data
   │   │
   │   ├─> GitHub Agent
   │   │   └─> GitHub API
   │   │       └─> Search, retrieve data
   │   │
   │   └─> Web Search Agent
   │       └─> Exa MCP
   │           └─> Search, summarize
   │
   ├─> Collect results from all agents
   │
   ├─> Aggregate and synthesize results
   │
   └─> Return comprehensive response
```

### Tool Execution Flow

```
1. Agent needs capability (e.g., web browsing)
   │
   ├─> Select appropriate MCP tool
   │
   ├─> Initialize tool connection
   │   └─> Start MCP server (bunx)
   │   └─> Establish stdio connection
   │
   ├─> Send tool request
   │   └─> Serialize parameters
   │   └─> Send via stdio
   │
   ├─> Receive tool response
   │   └─> Deserialize result
   │   └─> Validate data
   │
   ├─> Process result in agent context
   │
   └─> Return to agent for further processing
```

## Communication Patterns

### Agent Communication

**Parent to Child (Router to Sub-Agent):**

```python
# Router sends task to sub-agent
task = Task(
    query="Find GitHub repositories",
    context={"topic": "AI agents"},
    constraints={"max_results": 10}
)

result = sub_agent.execute(task)
```

**Child to Parent (Sub-Agent to Router):**

```python
# Sub-agent returns structured result
return Result(
    data=repositories,
    metadata={
        "source": "github",
        "timestamp": datetime.now(),
        "count": len(repositories)
    },
    status="success"
)
```

### Tool Communication

**Agent to Tool (via MCP):**

```python
# Agent requests tool action
tool_request = {
    "method": "navigate",
    "params": {
        "url": "https://news.ycombinator.com",
        "wait_for": "load"
    }
}

tool_response = mcp_tool.execute(tool_request)
```

**Tool to Agent (via MCP):**

```python
# Tool returns result
{
    "status": "success",
    "data": {
        "html": "<html>...",
        "screenshot": "base64_image_data",
        "metadata": {"load_time": 1.2}
    }
}
```

## State Management

### Agent State

Agents maintain minimal state:

```python
class AgentState:
    """State maintained by an agent"""
    current_task: Optional[Task] = None
    execution_history: List[Execution] = []
    metrics: ExecutionMetrics = ExecutionMetrics()
    
    def update(self, execution: Execution):
        """Update state after execution"""
        self.execution_history.append(execution)
        self.metrics.update(execution)
```

### Tool State

Tools manage connection state:

```python
class ToolState:
    """State maintained by a tool"""
    connection: Optional[Connection] = None
    ready: bool = False
    error_count: int = 0
    
    def ensure_connected(self):
        """Ensure tool is connected and ready"""
        if not self.ready:
            self.connect()
```

## Error Handling

### Error Hierarchy

```
AgentError
├── ConfigurationError
│   ├── InvalidModelError
│   ├── MissingCredentialsError
│   └── InvalidToolError
│
├── ExecutionError
│   ├── ToolExecutionError
│   ├── TimeoutError
│   └── RateLimitError
│
└── ValidationError
    ├── InvalidInputError
    └── InvalidOutputError
```

### Error Handling Strategy

**At Agent Level:**

```python
try:
    result = sub_agent.execute(query)
except ToolExecutionError as e:
    # Try fallback tool
    logger.warning(f"Primary tool failed: {e}")
    result = sub_agent.execute_with_fallback(query)
except TimeoutError as e:
    # Return partial results
    logger.error(f"Agent timeout: {e}")
    result = sub_agent.get_partial_results()
```

**At Router Level:**

```python
results = []
for agent in sub_agents:
    try:
        result = agent.execute(query)
        results.append(result)
    except Exception as e:
        # Continue with other agents
        logger.error(f"Agent {agent.name} failed: {e}")
        continue

# Aggregate whatever results we have
return aggregate(results)
```

## Performance Considerations

### Parallel Execution

**Benefits:**
- Reduced latency for multi-source queries
- Better resource utilization
- Improved user experience

**Trade-offs:**
- Increased complexity
- Resource contention
- Result synchronization overhead

### Caching Strategy

**What to Cache:**
- LLM model responses (with TTL)
- Tool connection objects (reuse)
- Frequently accessed data (e.g., popular GitHub repos)

**Cache Implementation:**

```python
from functools import lru_cache
from datetime import datetime, timedelta

class ResultCache:
    def __init__(self, ttl_seconds: int = 300):
        self.cache = {}
        self.ttl = timedelta(seconds=ttl_seconds)
    
    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            result, timestamp = self.cache[key]
            if datetime.now() - timestamp < self.ttl:
                return result
        return None
    
    def set(self, key: str, value: Any):
        self.cache[key] = (value, datetime.now())
```

### Resource Management

**Connection Pooling:**

```python
class ToolPool:
    """Manage pool of tool connections"""
    def __init__(self, tool_factory, pool_size: int = 5):
        self.pool = [tool_factory() for _ in range(pool_size)]
        self.available = queue.Queue()
        for tool in self.pool:
            self.available.put(tool)
    
    def acquire(self) -> Tool:
        return self.available.get()
    
    def release(self, tool: Tool):
        self.available.put(tool)
```

## Security Considerations

### Credential Management

**Best Practices:**
- Store credentials in environment variables
- Never commit credentials to version control
- Use secret management services in production
- Rotate credentials regularly

**Implementation:**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Secure settings management"""
    exa_api_key: str
    google_credentials: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

### Input Validation

**Sanitize User Input:**

```python
def validate_query(query: str) -> str:
    """Validate and sanitize user query"""
    # Length check
    if len(query) > 10000:
        raise ValueError("Query too long")
    
    # Content check
    if contains_malicious_content(query):
        raise ValueError("Invalid query content")
    
    return query.strip()
```

### Rate Limiting

**Implement Rate Limits:**

```python
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = timedelta(seconds=window_seconds)
        self.requests = []
    
    def check_limit(self) -> bool:
        now = datetime.now()
        # Remove old requests outside window
        self.requests = [r for r in self.requests if now - r < self.window]
        
        if len(self.requests) >= self.max_requests:
            return False
        
        self.requests.append(now)
        return True
```

## Testing Strategy

### Unit Testing

**Test Individual Components:**

```python
def test_hacker_news_agent():
    """Test HN agent in isolation"""
    agent = hacker_news_agent
    result = agent.execute("Get top stories")
    
    assert result.status == "success"
    assert len(result.data) > 0
    assert all(isinstance(story, Story) for story in result.data)
```

### Integration Testing

**Test Component Interactions:**

```python
def test_research_supervisor():
    """Test agent coordination"""
    supervisor = router_agent
    result = supervisor.run("Research AI agents")
    
    # Verify multiple sources were used
    assert len(result.sources) > 1
    assert "hacker_news" in result.sources
```

### Mock Tools for Testing

**Use Mock MCP Tools:**

```python
class MockMCPTool(MCPToolset):
    """Mock tool for testing"""
    def execute(self, request):
        return {
            "status": "success",
            "data": self._generate_mock_data()
        }
```

## Deployment Architecture

### Development Environment

```
Developer Machine
├── adk-agents source code
├── .env with credentials
├── Local MCP tools (bunx)
└── Python environment
```

### Production Environment

```
Production System
├── Docker Container
│   ├── Application code
│   ├── Python runtime
│   └── Node.js for MCP tools
│
├── Secret Store
│   └── API keys, credentials
│
├── Monitoring
│   ├── Metrics collection
│   └── Log aggregation
│
└── Load Balancer
    └── Route requests to instances
```

## Future Architecture Enhancements

### Planned Improvements

1. **Event-Driven Architecture**
   - Move to event-based communication
   - Enable real-time updates
   - Support streaming responses

2. **Persistent State**
   - Store conversation history
   - Enable multi-turn interactions
   - Support session resumption

3. **Distributed Execution**
   - Deploy agents across multiple servers
   - Implement work queues
   - Scale horizontally

4. **Enhanced Monitoring**
   - Real-time dashboards
   - Performance metrics
   - Alert system

## Conclusion

The ADK agents architecture is designed for:
- **Modularity**: Easy to understand and modify
- **Scalability**: Supports growth and increasing complexity
- **Reliability**: Robust error handling and recovery
- **Maintainability**: Clear separation of concerns
- **Extensibility**: Simple to add new capabilities

This architecture provides a solid foundation for building sophisticated AI agent systems while maintaining code quality and developer productivity.
