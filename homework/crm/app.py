from flask import Flask, render_template, request
import database as db
import math
from route.orders import orders_bp
from route.order_items import order_items_bp
from route.items import items_bp
from route.stores import stores_bp
from route.detail.user_detail import user_detail_bp
from route.detail.orderitem_detail import orderitem_detail_bp
from route.detail.order_detail import order_detail_bp
from route.detail.store_detail import store_detail_bp
from route.detail.item_detail import item_detail_bp

# 페이지 별로 뒤로 갈 수 있는 버튼 추가하기

app = Flask(__name__)
app.register_blueprint(orders_bp)
app.register_blueprint(order_items_bp)
app.register_blueprint(items_bp)
app.register_blueprint(stores_bp)
app.register_blueprint(user_detail_bp)
app.register_blueprint(orderitem_detail_bp)
app.register_blueprint(order_detail_bp)
app.register_blueprint(store_detail_bp)
app.register_blueprint(item_detail_bp)

@app.route('/')
def home():
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

if __name__ == '__main__':
    app.run(debug=True)