FROM --platform=linux/arm64 ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy source files
COPY agent.py agent_agentcore_sdk.py agent_agentcore_custom.py ./
COPY tools/ tools/

EXPOSE 8080

# Default: SDK Integration entrypoint
CMD ["uv", "run", "python", "agent_agentcore_sdk.py"]

# To use the Custom FastAPI entrypoint instead, override CMD:
# CMD ["uv", "run", "python", "agent_agentcore_custom.py"]
