import boto3
import json

# Grab environment variables
ENDPOINT_NAME = "your-sagemaker-endpoint-name"  # Replace with your SageMaker endpoint name
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    try:
        # Ensure the event contains the 'body' key
        if 'body' not in event:
            raise KeyError("'body' key is missing from the event")

        # Parse the input payload from the event
        input_payload = json.loads(event['body'])  # Example input: {'inputs': 'I like you. I love you'}

        # Send the payload to the SageMaker endpoint
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType='application/json',
            Body=json.dumps(input_payload)  # Convert input to JSON string
        )

        # Decode and process the response from the model
        response_content = response['Body'].read().decode('utf-8')
        result = json.loads(response_content)

        # Return the model's response
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except KeyError as e:
        # Handle missing 'body' key
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    except Exception as e:
        # Handle other exceptions
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
