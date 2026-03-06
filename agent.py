from strands import Agent

from tools import calculate, get_weather

SYSTEM_PROMPT = "You are a helpful AI assistant with access to weather and calculator tools."


def create_agent() -> Agent:
    """Create and return a Strands Agent configured with custom tools."""
    return Agent(
        system_prompt=SYSTEM_PROMPT,
        tools=[get_weather, calculate],
    )
