from flask import Blueprint, render_template, request
import database as db 

order_detail_bp = Blueprint('orders_detail', __name__, template_folder='../templates')

@order_detail_bp.route('/orders_detail')
def order_detail():
    order_id = request.args.get('id')
    print(order_id)
    order_detail = db.get_order_detail(order_id)
    print(order_detail)
    return render_template('detail/orders_detail.html', order_detail=order_detail)