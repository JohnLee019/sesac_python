from flask import Blueprint, render_template, request
import math
import database as db 

users_bp = Blueprint('users', __name__, template_folder='../templates')
@users_bp.route('/users')
def users():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20 
    users = db.get_users_per_page(page, items_per_page)

    #검색 기능
    name = request.args.get("name", "").strip()
    gender = request.args.get("gender", "").strip()
    # print(f"성별은: {gender}")
    if name or gender:
        if db.get_users_by_name_gender(name, gender):
            user_name_gender = db.get_users_by_name_gender(name, gender)
            # print(user_name)
            # print(len(user_name))
            # print(db.get_users_by_name_gender(name, gender))
            total_pages = math.ceil(len(user_name_gender) / items_per_page)
            start = (page - 1) * items_per_page
            end = start + items_per_page
            users = user_name_gender[start: end]
            # print(total_pages)
            return render_template('index.html', users=users, total_pages=total_pages, name=name, gender=gender, page=page)
        
        elif db.get_users_by_name_gender(name, gender) == []:
            return '해당 사용자는 존재하지 않습니다'
    # print(f"name: {name} gender: {gender}")

    #그냥 유저 목록 보여주기 
    user_count = db.get_user_count()
    total_pages = math.ceil(user_count / items_per_page)
    return render_template('index.html', users=users, total_pages=total_pages, page=page)
