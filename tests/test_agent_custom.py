"""Tests for the custom FastAPI agent endpoint."""

from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient


@patch("agent_agentcore_custom.create_agent")
def test_ping(mock_create_agent):
    """Test the health check endpoint."""
    mock_create_agent.return_value = MagicMock()

    import agent_agentcore_custom

    client = TestClient(agent_agentcore_custom.app)
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@patch("agent_agentcore_custom.agent")
def test_invocations_valid_prompt(mock_agent):
    """Test the invocations endpoint with a valid prompt."""
    mock_result = MagicMock()
    mock_result.message = {
        "role": "assistant",
        "content": [{"text": "The weather in Tokyo is sunny."}],
    }
    mock_agent.return_value = mock_result

    import agent_agentcore_custom

    client = TestClient(agent_agentcore_custom.app)
    response = client.post(
        "/invocations",
        json={"input": {"prompt": "What is the weather in Tokyo?"}},
    )
    assert response.status_code == 200
    data = response.json()
    assert "output" in data
    assert data["output"]["message"] == "The weather in Tokyo is sunny."
    assert data["output"]["model"] == "strands-agent"
    assert "timestamp" in data["output"]


@patch("agent_agentcore_custom.agent")
def test_invocations_missing_prompt(mock_agent):
    """Test the invocations endpoint with missing prompt field."""
    import agent_agentcore_custom

    client = TestClient(agent_agentcore_custom.app)
    response = client.post(
        "/invocations",
        json={"input": {}},
    )
    assert response.status_code == 422


@patch("agent_agentcore_custom.agent")
def test_invocations_missing_input(mock_agent):
    """Test the invocations endpoint with missing input field."""
    import agent_agentcore_custom

    client = TestClient(agent_agentcore_custom.app)
    response = client.post(
        "/invocations",
        json={},
    )
    assert response.status_code == 422
