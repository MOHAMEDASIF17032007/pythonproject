from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)

# Enhanced knowledge base for the chatbot
KNOWLEDGE_BASE = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
        "responses": [
            "Hello! I'm Chat Man, your AI assistant. How can I help you today?",
            "Hi there! I'm here to assist you. What would you like to know?",
            "Greetings! I'm ready to help you with any questions you have."
        ]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you", "farewell", "exit", "quit"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Feel free to come back if you have more questions.",
            "Take care! I'll be here when you need me again."
        ]
    },
    "thanks": {
        "patterns": ["thank", "thanks", "appreciate", "grateful"],
        "responses": [
            "You're welcome! Is there anything else I can help you with?",
            "My pleasure! Feel free to ask if you need anything else.",
            "Happy to help! Let me know if you have more questions."
        ]
    },
    "capabilities": {
        "patterns": ["what can you do", "help", "capabilities", "features", "abilities"],
        "responses": [
            "I can help you with various topics including:\n- General knowledge\n- Technology\n- Science\n- History\n- Current events\n- Problem-solving\n- And much more! What would you like to know?",
            "I'm here to assist you with information, answer questions, and engage in meaningful conversations. What would you like to discuss?",
            "I can provide information, answer questions, and help with various topics. Just let me know what you're interested in!"
        ]
    },
    "technology": {
        "patterns": ["technology", "computer", "software", "hardware", "programming", "code", "python", "javascript", "ai", "artificial intelligence"],
        "responses": [
            "Technology is constantly evolving! I can help you understand various aspects of tech, from programming languages to AI and machine learning. What specific area interests you?",
            "I'm knowledgeable about many tech topics including programming, AI, software development, and more. What would you like to learn about?",
            "Technology is fascinating! I can discuss programming, AI, software development, or any other tech topic you're interested in."
        ]
    },
    "science": {
        "patterns": ["science", "physics", "chemistry", "biology", "astronomy", "space"],
        "responses": [
            "Science is amazing! I can help you understand various scientific concepts, from basic principles to advanced theories. What would you like to learn about?",
            "I'm knowledgeable about many scientific fields including physics, chemistry, biology, and astronomy. What interests you?",
            "Science is fascinating! I can discuss various scientific topics and help you understand complex concepts."
        ]
    },
    "history": {
        "patterns": ["history", "historical", "past", "ancient", "medieval", "modern"],
        "responses": [
            "History is fascinating! I can help you learn about different periods, events, and historical figures. What would you like to know?",
            "I'm knowledgeable about various historical periods and events. What specific era or topic interests you?",
            "History is full of interesting stories and lessons. I can help you explore different historical topics."
        ]
    },
    "current_events": {
        "patterns": ["news", "current events", "latest", "recent", "today", "now"],
        "responses": [
            "I can help you stay informed about current events and recent developments. What specific topic would you like to know about?",
            "I'm here to discuss current events and recent news. What would you like to learn about?",
            "I can help you understand recent developments and current events. What interests you?"
        ]
    },
    "personal": {
        "patterns": ["how are you", "how do you feel", "are you happy", "your mood"],
        "responses": [
            "I'm functioning well and ready to help you! How can I assist you today?",
            "I'm doing great and excited to help you with your questions!",
            "I'm here and ready to assist you with whatever you need!"
        ]
    },
    "default": {
        "responses": [
            "I'm not sure I understand. Could you rephrase that or ask something else?",
            "Interesting! Could you provide more details or ask a different question?",
            "I'm still learning. Could you try asking that in a different way?",
            "I want to make sure I understand you correctly. Could you rephrase that?"
        ]
    }
}

def get_response(user_input):
    user_input = user_input.lower()
    
    # Check each category in the knowledge base
    for category, data in KNOWLEDGE_BASE.items():
        if category != "default":
            # Check if any pattern matches the user input
            if any(pattern in user_input for pattern in data["patterns"]):
                return random.choice(data["responses"])
    
    # If no specific category matches, return a default response
    return random.choice(KNOWLEDGE_BASE["default"]["responses"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 