from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

response = requests.post('https://api.openai.com/v1/chat/completions',
    json={
        'model':'gpt-4o',
        'messages': [
            {'role': 'user', 'content': '오늘 날씨는'}
        ]
    },
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        }
    )

response_data = response.json()
print(response_data['choices'][0]['message']['content'])