from flask import Flask, request, jsonify, render_template, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import random
load_dotenv()

app = Flask(__name__)
app.secret_key = 'abcd1234'

app.config['MAIL_SERVER'] = os.getenv('NAVER_MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('NAVER_MAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('NAVER_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('NAVER_PASSWORD')
mail = Mail(app)

@app.route('/')
def signup():
    return render_template('index.html')

@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.json.get('email', "").strip()  #사용자로부터 받아오기
    print(email)
    if not email:
        return jsonify({"message": "올바른 이메일 주소가 필요합니다"}, 404)
    # 미션1. 6자리 숫자 랜덤값 만들기 
    code = (f"{random.randint(0, 999999):06d}")

    # 미션1-1. 세션에 우리의 랜덤 코드... 이메일...
    session['verify'] = code

    msg = Message('회원가입 인증 코드', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f"인증 코드: {code}"
    mail.send(msg)

    return jsonify({"message": "인증 코드가 전송되었습니다."})

@app.route('/verify-code', methods=["POST"])
def verify_code():
    #미션2. 내가 보낸 코드와 같은지 확인하고 
    # email = request.form.get("email", "").strip()
    user_code = request.form.get("code", "").strip()

    if user_code != session['code']:
        return jsonify({'message': "인증실패"})
    return jsonify({"message": "인증성공"})


    #미션2-1. 저장된 세션으로부터 코드 가져와서.. 사용자 입력, 내가 저장해둔거랑 같은지 확인...
    check = session.get['verfiy']
    if not check:
        return jsonify({"사용자와 일치하는 이메일 또는 코드가 없습니다."}, 400)
    if check['code'] != user_code:
        return jsonify({"요청한 코드가 일치하지 않습니다."}, 404)
    if check['code'] == user_code:
        return jsonify({"message": "인증성공"})

if __name__ == '__main__':
    app.run(debug=True)