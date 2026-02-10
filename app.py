from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the conversational model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Store conversation history per session
conversation_history = []

@app.route('/')
def index():
    """Render the main chatbot page"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    try:
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Generate response
        response = chatbot(user_message, conversation_history)
        bot_response = response[-1]["generated_text"]
        
        # Add bot response to history
        conversation_history.append({
            "role": "bot",
            "content": bot_response
        })
        
        return jsonify({
            'response': bot_response,
            'success': True
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear conversation history"""
    global conversation_history
    conversation_history = []
    return jsonify({'success': True, 'message': 'Conversation cleared'})

if __name__ == '__main__':
    app.run(debug=True, port=5000}