from flask import Blueprint, render_template, request
import math
import database as db 

items_bp = Blueprint('items', __name__, template_folder='../templates')

@items_bp.route('/items')
def items():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20 
    type = request.args.get('type', "").strip()
    min_str = request.args.get('min', "").strip()
    max_str = request.args.get('max', "").strip()

    if min_str != "":
        min_price = int(min_str)
    else:
        min_price = None

    if max_str != "":
        max_price = int(max_str)
    else:
        max_price = None


    item_type = db.get_item_type(type, min_price, max_price)
    total_pages = math.ceil(len(item_type) / items_per_page)
    start = (page - 1) * items_per_page
    end = start + items_per_page
    items = item_type[start: end]
    min_price = str(min_price)
    max_price = str(max_price)
    return render_template('items.html', items=items,
    total_pages=total_pages, page=page, type=type, min=min_price, max=max_price)
