from flask import Flask, render_template, session
from route.orders import orders_bp
from route.order_items import order_items_bp
from route.items import items_bp
from route.stores import stores_bp
from route.detail.user_detail import user_detail_bp
from route.detail.orderitem_detail import orderitem_detail_bp
from route.detail.order_detail import order_detail_bp
from route.detail.store_detail import store_detail_bp
from route.detail.item_detail import item_detail_bp
from route.user import users_bp

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
app.register_blueprint(users_bp)

users = [
    {'id': '이홍민', 'pw': 'password'}
]

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')