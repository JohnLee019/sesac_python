from flask import Flask, render_template, request
import database as db
import math

app = Flask(__name__)

@app.route('/')
def home():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20 
    users = db.get_users_per_page(page, items_per_page)

    #검색 기능
    name = request.args.get("name", "").strip()
    gender = request.args.get("gender", "").strip()

    if name or gender:
        if db.get_users_by_name(name):
            user_name = db.get_users_by_name(name)
            # print(user_name)
            # print(len(user_name))
            total_pages = math.ceil(len(user_name) / items_per_page)
            users = user_name[page: (items_per_page +page)]
            # print(total_pages)
            return render_template('index.html', users=users, total_pages=total_pages, name=name, gender=gender)
        else:
            return '해당 이름의 사용자는 존재하지 않습니다'
    # print(f"name: {name} gender: {gender}")

    #그냥 유저 목록 보여주기
    user_count = db.get_user_count()
    total_pages = math.ceil(user_count / items_per_page)
    return render_template('index.html', users=users, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)