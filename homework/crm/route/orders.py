from flask import Blueprint, render_template, request
import math
import database as db 

orders_bp = Blueprint('orders', __name__, template_folder='../templates')

@orders_bp.route('/orders')
def orders():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20 
    orders = db.get_orders_per_page(page, items_per_page)
    orders_count = db.get_orders()
    total_pages = math.ceil(len(orders_count) / items_per_page)
    return render_template('orders.html', orders=orders, total_pages=total_pages, page=page)
