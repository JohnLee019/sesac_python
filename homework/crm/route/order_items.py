from flask import Blueprint, render_template, request
import math
import database as db 

order_items_bp = Blueprint('orderitems', __name__, template_folder='../templates')

@order_items_bp.route('/orderItems')
def orderItem():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20 
    order_items = db.get_order_items_per_page(page, items_per_page)
    order_items_count = db.get_orders_items()
    total_pages = math.ceil(len(order_items_count) / items_per_page)
    return render_template('orderItems.html', order_items=order_items, total_pages=total_pages, page=page)