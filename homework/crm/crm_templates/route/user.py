from flask import Blueprint, render_template, request
import math
import database as db 

users_bp = Blueprint('users', __name__, template_folder='../templates')
@users_bp.route('/users')
def users():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20 
    users = db.get_users_per_page(page, items_per_page)
    name = request.args.get("name", "").strip()
    gender = request.args.get("gender", "").strip()
    
    if db.get_users_by_name_gender(name, gender):
        user_name_gender = db.get_users_by_name_gender(name, gender)
        total_pages = math.ceil(len(user_name_gender) / items_per_page)
        start = (page - 1) * items_per_page
        end = start + items_per_page
        users = user_name_gender[start: end]
        return render_template('index.html', users=users, total_pages=total_pages, name=name, gender=gender, page=page)
    elif db.get_users_by_name_gender(name, gender) == []:
        return '해당 사용자는 존재하지 않습니다'
