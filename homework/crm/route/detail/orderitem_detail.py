from flask import Blueprint, render_template, request
import database as db 

orderitem_detail_bp = Blueprint('orderitem_detail', __name__, template_folder='../templates')

@orderitem_detail_bp.route('/orderitem_detail')
def orderitem_detail():
    order_id = request.args.get('id')
    orders = db.get_orders_items_id(order_id)
    return render_template('detail/orderitem_detail.html', orders=orders)