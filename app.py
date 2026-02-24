from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv
from resume_data import resume_data, system_prompt

# load environment variables from .env file (if present)
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Groq client with your API key stored in environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set. Please configure it in the .env file or environment variables.")
client = Groq(api_key=GROQ_API_KEY)

# Store conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Add user message to conversation history
        conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Keep only the last 10 messages to manage context
        if len(conversation_history) > 10:
            conversation_history.pop(0)
        
        # Create messages for the API call
        messages = [
            {"role": "system", "content": system_prompt}
        ] + conversation_history
        
        # Call Groq API
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        # Get AI response
        ai_response = response.choices[0].message.content
        
        # Add AI response to conversation history
        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })
        
        return jsonify({
            'response': ai_response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/clear-chat', methods=['POST'])
def clear_chat():
    global conversation_history
    conversation_history = []
    return jsonify({'status': 'success', 'message': 'Chat history cleared'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)