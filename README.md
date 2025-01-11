# SageMaker-Lambda Integration Example

This repository demonstrates how to deploy a Hugging Face model to AWS SageMaker and integrate it with an AWS Lambda function. It includes all necessary steps, configurations, and example payloads.

## Prerequisites

1. AWS Account.
2. AWS CLI installed and configured.
3. Python 3.10+ installed.
4. Necessary IAM roles with permissions:
   - SageMaker execution role with `sagemaker:InvokeEndpoint`.
   - Lambda execution role with `AWSLambdaBasicExecutionRole` and `sagemaker:InvokeEndpoint`.

## Steps

### 1. Model Deployment

1. Navigate to the `model_deployment/` directory.
2. Update the `config.json` file with your model details.
3. Run the `deploy_model.py` script to deploy the model to SageMaker.

```bash
cd model_deployment/
python deploy_model.py
