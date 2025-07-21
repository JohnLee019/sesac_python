from flask import Blueprint, render_template, request
import database as db 

user_detail_bp = Blueprint('user_detail', __name__, template_folder='../templates')

@user_detail_bp.route('/user_detail')
def user_detail():
    user_id = request.args.get('id')
    users = db.get_user_by_id(user_id)
    purchase = db.get_user_order_detail(user_id)
    return render_template('detail/user_detail.html', users=users, purchase=purchase)