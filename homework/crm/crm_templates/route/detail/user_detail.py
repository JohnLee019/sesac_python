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
    # print(often_bought_items)
    chart_list_name = []
    amount_bought = []
    for i in often_bought_items:
        chart_list_name.append(i['Name'])
        amount_bought.append(i['Count'])
    print(chart_list_name)
    print(amount_bought)
    return render_template('detail/user_detail.html', users=users, purchase=purchase, often_visited_list=often_visited_list, often_bought_items=often_bought_items, list = chart_list_name, amount = amount_bought)