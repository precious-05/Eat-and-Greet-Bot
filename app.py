# app.py - Eat and Greet Instagram DM Bot

import os
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from responses import get_response

# Load .env file
load_dotenv()

app = Flask(__name__)

# Credentials from .env file - APNI VALUES DALNA YAHAN
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

# Graph API endpoint
GRAPH_API_URL = 'https://graph.facebook.com/v18.0/me/messages'

def send_message(recipient_id, message_text):
    """Send reply to customer"""
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    payload = {
        'recipient': {'id': recipient_id},
        'message': {'text': message_text},
        'access_token': ACCESS_TOKEN
    }
    
    try:
        response = requests.post(GRAPH_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Reply sent to {recipient_id}")
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    """Main webhook handler"""
    
    # GET request - Verification for Meta
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode and token:
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print("Webhook verified successfully!")
                return challenge, 200
            else:
                return 'Verification failed', 403
        return 'Missing parameters', 400
    
    # POST request - Receive message from customer
    elif request.method == 'POST':
        body = request.json
        print(f"Received webhook: {json.dumps(body, indent=2)}")
        
        # Check if it's an Instagram message
        if body.get('object') == 'instagram':
            for entry in body.get('entry', []):
                for messaging in entry.get('messaging', []):
                    
                    # Skip messages sent by bot to avoid infinite loop
                    if messaging.get('sender', {}).get('id') == messaging.get('recipient', {}).get('id'):
                        continue
                    
                    # Skip echoes
                    if messaging.get('message', {}).get('is_echo'):
                        continue
                    
                    # Get sender ID and message
                    sender_id = messaging.get('sender', {}).get('id')
                    message_text = messaging.get('message', {}).get('text')
                    
                    if sender_id and message_text:
                        print(f"Message from {sender_id}: {message_text}")
                        
                        # Generate reply using responses.py
                        reply_text = get_response(message_text)
                        print(f"Reply: {reply_text}")
                        
                        # Send reply
                        send_message(sender_id, reply_text)
        
        return jsonify({'status': 'ok'}), 200

@app.route('/', methods=['GET'])
def home():
    """Home route to check if server is running"""
    return "Eat and Greet Instagram Bot is Running!", 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)