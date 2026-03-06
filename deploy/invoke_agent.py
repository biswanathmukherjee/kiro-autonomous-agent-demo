"""Invoke a deployed Strands Agent on AWS Bedrock AgentCore.

Usage:
    python deploy/invoke_agent.py --agent-runtime-arn <ARN> --prompt "What is the weather in Tokyo?"
"""

import argparse
import json

import boto3


def invoke_agent(agent_runtime_arn: str, prompt: str):
    """Invoke an AgentCore Runtime agent with the given prompt."""
    client = boto3.client("bedrock-agentcore")

    response = client.invoke_agent_runtime(
        agentRuntimeArn=agent_runtime_arn,
        payload=json.dumps({"prompt": prompt}),
    )

    result = json.loads(response["body"].read())
    print(f"Prompt: {prompt}")
    print(f"Response: {json.dumps(result, indent=2)}")


def main():
    parser = argparse.ArgumentParser(description="Invoke a deployed AgentCore agent")
    parser.add_argument(
        "--agent-runtime-arn",
        required=True,
        help="The ARN of the deployed AgentCore Runtime",
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="The prompt to send to the agent",
    )
    args = parser.parse_args()
    invoke_agent(args.agent_runtime_arn, args.prompt)


if __name__ == "__main__":
    main()
