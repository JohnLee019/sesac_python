from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify
from openai import OpenAI

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static')
app = Flask(__name__, static_folder='public', static_url_path='')
# openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
openai = OpenAI()

reviews = [] # 사용자 후기를 저장할 DB

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')
    
    reviews.append({'rating': rating, 'opinion': opinion})
    
    return jsonify({'message':'성공적으로 저장됨'})

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'reviews': reviews})

@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():
    target_lang = request.args.get('lang', 'ko')
    print('언어', target_lang)

    all_langs = {
        'ko': '한국어',
        'eng': 'English',
        'ja': '日本語',
        'sp': 'Español'
    }

    target_lang = all_langs.get(target_lang, '한국어')
    print(target_lang)

    #미션 1. 프런트에서 보낸 언어 "코드값" 으로, 원하는 언어로 매핑을 한다.
    #미션 2. 그걸 기반으로, GPT에게 해당 언어로 요약을 만들어 달라고 한다. 

    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})

    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])
    
    # prompt = f"모든 리뷰들의 글들을 {target_lang}로 번역해서 바꿔줘. 참고로 번역 해야하는 글들은 {reviews['opinion]} 안에 있는 내용들이야"

    print("리뷰내용 통합: ", reviews_text)
    
    # 아래도 try catch 로 꼭 감싸야 함.. key가 없거나, 돈이 다 떨어졌거나, 서버가 죽었거나, 여러가지 이유로 요청에 실패할수 있음.
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user',
            'content': f'다음 리뷰 목록을 기반으로 {target_lang} 언어로 바꿔서 간결하게 한줄로 요약해 주세요.\n\n{reviews_text}'
        }]
    )
    
    summary = response.choices[0].message.content.strip()
    print("요약리뷰내용: ", summary)
    return jsonify({'summary': summary, 'averageRating': average_rating})

if __name__ == '__main__':
    app.run(port=5000, debug=True)