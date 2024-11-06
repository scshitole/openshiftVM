import openvino_genai as ov_genai
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Set device and model path
device = "CPU"
model_path = "/home/cloud-user/open_llama_3b_v2-fp16-ov"
logging.info(f"Initializing pipeline with model path: {model_path}")

# Initialize pipeline
pipe = ov_genai.LLMPipeline(model_path, device)
logging.info("Pipeline initialized successfully")

def generate_response(prompt: str, max_length: int = 100) -> str:
    try:
        response = pipe.generate(prompt, max_length=max_length)
        logging.info(f"Prompt: {prompt}")
        logging.info(f"Response: {response}")
        return response.strip()
    except Exception as e:
        logging.error(f"Error in generate_response: {str(e)}")
        return f"Error generating response: {str(e)}"

# Testing the response directly in llama_inference.py
if __name__ == "__main__":
    test_prompt = "Tell me a fun fact"
    print("Testing generate_response with prompt:", test_prompt)
    response = generate_response(test_prompt, max_length=100)
    print("Response:", response)


