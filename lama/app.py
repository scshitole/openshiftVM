from flask import Flask, render_template, request, jsonify
from llama_inference import generate_response
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('prompt', '')
        
        if not user_input:
            return jsonify({'error': 'Empty prompt'}), 400

        print(f"Received prompt: {user_input}")
        
        # Generate response using Llama model
        response = generate_response(user_input)
        
        # Log the response for debugging
        print(f"Generated response: {response}")
        
        return jsonify({'response': response})
    except Exception as e:
        print("Exception in /generate endpoint:")
        print(traceback.format_exc())
        return jsonify({'error': 'An error occurred while processing your request'}), 500

# Optional: Uncomment for debugging Flask app directly
# if __name__ == "__main__":
#     app.run(debug=True)


