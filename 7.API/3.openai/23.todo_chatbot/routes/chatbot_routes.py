from flask import Blueprint, request, jsonify
chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/api/chat', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    question = data.get('userInput') 
    return jsonify({'chatbot': f'[BOT] {question}'})