# Strands Agent - AgentCore Demo

A sample project demonstrating how to build an AI agent using the [Strands Agents SDK](https://github.com/strands-agents/sdk-python) and deploy it to [AWS Bedrock AgentCore](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html).

## Prerequisites

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/) package manager
- AWS account with Bedrock access (for deployment)
- Docker (for container builds)

## Project Structure

```
.
├── agent.py                    # Core agent definition with custom tools
├── agent_agentcore_sdk.py      # SDK Integration entrypoint (BedrockAgentCoreApp)
├── agent_agentcore_custom.py   # Custom FastAPI entrypoint (/invocations, /ping)
├── tools/
│   ├── __init__.py
│   ├── weather.py              # Weather lookup tool (mock data)
│   └── calculator.py           # Calculator tool (expression evaluator)
├── deploy/
│   ├── deploy_agent.py         # Boto3 script to create AgentCore Runtime
│   └── invoke_agent.py         # Boto3 script to invoke a deployed agent
├── tests/
│   ├── test_tools.py           # Unit tests for custom tools
│   └── test_agent_custom.py    # Integration tests for FastAPI endpoints
├── Dockerfile                  # ARM64 container for AgentCore deployment
├── pyproject.toml              # Project configuration and dependencies
└── README.md
```

## Local Development

### Setup

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest tests/ -v

# Lint code
uv run ruff check .
```

### Running Locally

**Custom FastAPI server:**

```bash
uv run python agent_agentcore_custom.py
```

This starts a server on port 8080 with:
- `GET /ping` - Health check
- `POST /invocations` - Agent invocation

Example request:

```bash
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"input": {"prompt": "What is the weather in Tokyo?"}}'
```

## Custom Tools

This project includes two example tools built with the `@tool` decorator from Strands:

- **get_weather** (`tools/weather.py`): Returns mock weather data for known cities (New York, London, Tokyo, Paris, Sydney).
- **calculate** (`tools/calculator.py`): Evaluates simple mathematical expressions safely.

You can add your own tools by creating new functions with the `@tool` decorator and registering them in `agent.py`.

## Deployment Approaches

AgentCore supports two deployment patterns. This project includes both:

### 1. SDK Integration (`agent_agentcore_sdk.py`)

Uses the `bedrock-agentcore` SDK with `BedrockAgentCoreApp` and `@app.entrypoint` decorator. This is the simpler approach where the SDK handles HTTP routing.

### 2. Custom FastAPI (`agent_agentcore_custom.py`)

Implements a standard FastAPI server with `/invocations` (POST) and `/ping` (GET) endpoints. This gives full control over request/response handling, middleware, and error formatting.

## Docker

Build the container image (ARM64 for AgentCore):

```bash
docker build -t strands-agent-demo .
```

Run locally:

```bash
# SDK entrypoint (default)
docker run -p 8080:8080 strands-agent-demo

# Custom FastAPI entrypoint
docker run -p 8080:8080 strands-agent-demo uv run python agent_agentcore_custom.py
```

## AgentCore Deployment

1. Build and push your Docker image to Amazon ECR.
2. Update the placeholder values in `deploy/deploy_agent.py` (container URI, IAM role ARN).
3. Run the deployment script:

```bash
uv run python deploy/deploy_agent.py
```

4. Invoke the deployed agent:

```bash
uv run python deploy/invoke_agent.py \
  --agent-runtime-arn <your-agent-runtime-arn> \
  --prompt "What is the weather in New York?"
```

## Testing

```bash
# Run all tests
uv run pytest tests/ -v

# Run only tool tests
uv run pytest tests/test_tools.py -v

# Run only endpoint tests
uv run pytest tests/test_agent_custom.py -v
```

## Links

- [Strands Agents SDK](https://github.com/strands-agents/sdk-python)
- [Strands Agents Tools](https://github.com/strands-agents/tools-python)
- [AWS Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html)
