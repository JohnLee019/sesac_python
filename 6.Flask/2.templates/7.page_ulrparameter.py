from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{str(i).zfill(4)}'} for i in range (1, 101)
]
@app.route('/')
def home():
    # 기본 접속 시 1페이지로 redirect
    return redirect(url_for('index', page=1))

# http://localhost:5000/?pages=1
@app.route('/page/<int:page>')
def index(page):
    min = (page - 1) * 10
    max = min +  10

    user_per_page = users[min:max]

    if page > 1:
        prev_page = page - 1
    else:
        prev_page = None

    if max < len(users):
        next_page = page + 1
    else:
        next_page = None
    return render_template('users.html', users=user_per_page, page=page, prev_page= prev_page, next_page = next_page)

if __name__ == "__main__":
    app.run(debug=True)