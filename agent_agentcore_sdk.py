from bedrock_agentcore.runtime import BedrockAgentCoreApp

from agent import create_agent

app = BedrockAgentCoreApp()
agent = create_agent()


@app.entrypoint
def invoke(payload):
    """Handle incoming agent invocation requests via AgentCore SDK."""
    user_message = payload.get("prompt", "Hello")
    result = agent(user_message)
    return {"result": result.message}


if __name__ == "__main__":
    app.run()
