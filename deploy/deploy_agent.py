"""Deploy a Strands Agent to AWS Bedrock AgentCore.

This script creates an AgentCore Runtime using the bedrock-agentcore-control
boto3 client. Update the placeholder values before running.

Usage:
    python deploy/deploy_agent.py
"""

import boto3


def deploy_agent():
    """Create an AgentCore Runtime for the Strands agent."""
    client = boto3.client("bedrock-agentcore-control")

    # TODO: Replace with your actual container image URI
    container_uri = "123456789012.dkr.ecr.us-east-1.amazonaws.com/strands-agent:latest"

    # TODO: Replace with your actual IAM role ARN
    role_arn = "arn:aws:iam::123456789012:role/AgentCoreRuntimeRole"

    response = client.create_agent_runtime(
        agentRuntimeName="strands-agent-demo",
        description="Strands Agent with weather and calculator tools",
        agentRuntimeArtifact={
            "containerConfiguration": {
                "containerUri": container_uri,
            }
        },
        roleArn=role_arn,
    )

    print(f"Agent Runtime ARN: {response['agentRuntimeArn']}")
    print(f"Agent Runtime ID: {response['agentRuntimeId']}")
    print(f"Status: {response['status']}")


if __name__ == "__main__":
    deploy_agent()
