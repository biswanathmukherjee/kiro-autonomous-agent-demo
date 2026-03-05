from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agent import create_agent

app = FastAPI(title="Strands Agent - AgentCore Custom Deployment")

agent = create_agent()


class InvocationInput(BaseModel):
    prompt: str


class InvocationRequest(BaseModel):
    input: InvocationInput


class InvocationOutput(BaseModel):
    message: str
    timestamp: str
    model: str


class InvocationResponse(BaseModel):
    output: InvocationOutput


class HealthResponse(BaseModel):
    status: str


@app.get("/ping", response_model=HealthResponse)
def ping():
    """Health check endpoint required by AgentCore."""
    return HealthResponse(status="healthy")


@app.post("/invocations", response_model=InvocationResponse)
def invocations(request: InvocationRequest):
    """Handle agent invocation requests."""
    prompt = request.input.prompt
    if not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    result = agent(prompt)
    return InvocationResponse(
        output=InvocationOutput(
            message=result.message,
            timestamp=datetime.now(timezone.utc).isoformat(),
            model="strands-agent",
        )
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
