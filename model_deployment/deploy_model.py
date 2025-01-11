import sagemaker
from sagemaker.huggingface import HuggingFaceModel

# Set up SageMaker session
sess = sagemaker.Session()

# Define the Hugging Face model configuration
hub = {
    'HF_MODEL_ID': 'angusleung100/GraphCodeBERT-Base-Solidity-Vulnerability',
    'HF_TASK': 'text-classification'
}

role = sagemaker.get_execution_role()

# Create Hugging Face model object
huggingface_model = HuggingFaceModel(
    env=hub,
    role=role,
    transformers_version="4.26",
    pytorch_version="1.13",
    py_version='py39',
)

# Deploy the model
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.2xlarge"
)

# Optionally, test the deployment with a payload
test_payload = {"inputs": "I like you. I love you"}  # Example input
response = predictor.predict(test_payload)
print("Prediction response:", response)
