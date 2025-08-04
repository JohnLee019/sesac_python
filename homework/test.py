from flask import Flask, request, jsonify, render_template, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import secrets  # 안전한 난수
load_dotenv()

app = Flask(__name__)
app.secret_key = 'abcd1234'  # 예시. 실제로는 더 길고 비밀스럽게

app.config['MAIL_SERVER'] = os.getenv('NAVER_MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('NAVER_MAIL_PORT', '587'))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('NAVER_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('NAVER_PASSWORD')
mail = Mail(app)

@app.route('/')
def signup():
    return render_template('index.html')

@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.form.get('email', '').strip()
    if not email:
        return jsonify({"message": "이메일을 입력해 주세요."}), 400

    # 미션1. 6자리 숫자 랜덤값 만들기 (앞자리가 0이어도 항상 6자리)
    code = f"{secrets.randbelow(1_000_000):06d}"

    # 미션1-1. 세션에 우리의 랜덤 코드와 이메일 저장
    session['verify'] = {"email": email, "code": code}

    # 메일 발송
    msg = Message('회원가입 인증 코드', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f"인증 코드: {code}"
    try:
        mail.send(msg)
    except Exception as e:
        # 메일 전송이 실패해도 디버깅에 도움 되도록 안내
        return jsonify({"message": "메일 전송에 실패했습니다.", "detail": str(e)}), 500

    return jsonify({"message": "인증 코드가 전송되었습니다."})

@app.route('/verify-code', methods=['POST'])
def verify_code():
    # 미션2. 내가 보낸 코드와 같은지 확인
    email = request.form.get('email', '').strip()
    user_code = request.form.get('code', '').strip()

    saved = session.get('verify')  # 미션2-1. 세션에서 저장된 코드 꺼내기
    if not saved:
        return jsonify({"message": "인증 코드가 없습니다. 먼저 코드를 요청해 주세요."}), 400

    if saved.get('email') != email:
        return jsonify({"message": "요청한 이메일이 다릅니다."}), 400

    if saved.get('code') != user_code:
        return jsonify({"message": "인증실패"}), 400

    # 일치하면 한 번만 쓰도록 정리
    session.pop('verify', None)
    return jsonify({"message": "인증성공"})

if __name__ == '__main__':
    app.run(debug=True)
