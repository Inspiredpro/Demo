from transformers import pipeline

def create_local_chatbot():
    """Create a chatbot using Hugging Face transformers (runs locally)"""  
    
    # Load a conversational model
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
    
    print("🤖 Local Conversational AI Chatbot")
    print("Type 'quit' to exit\n")
    
    conversation_history = []
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Generate response
        response = chatbot(user_input, conversation_history)
        bot_response = response[-1]["generated_text"]
        
        print(f"\nChatbot: {bot_response}\n")
        
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "bot", "content": bot_response})

if __name__ == "__main__":
    create_local_chatbot()