from flask import Blueprint, render_template, request
import database as db 

user_detail_bp = Blueprint('user_detail', __name__, template_folder='../templates')

@user_detail_bp.route('/user_detail')
def user_detail():
    user_id = request.args.get('id').strip()
    users = db.get_user_by_id(user_id)
    purchase = db.get_user_order_detail(user_id)
    often_visited_list = db.get_often_visited_stores_by_user(user_id)
    often_bought_items = db.get_often_bought_by_user(user_id)
    return render_template('detail/user_detail.html', users=users, purchase=purchase, often_visited_list=often_visited_list, often_bought_items=often_bought_items)