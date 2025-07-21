from flask import Blueprint, render_template, request
import math
import database as db 

items_bp = Blueprint('items', __name__, template_folder='../templates')

@items_bp.route('/items')
def items():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20 
    type = request.args.get('type', "").strip()
    print(type)
    if type:
        item_type = db.get_item_type(type)
        print(item_type)
        total_pages = math.ceil(len(item_type) / items_per_page)
        start = (page - 1) * items_per_page
        end = start + items_per_page
        items = item_type[start: end]
        return render_template('items.html', items=items, total_pages=total_pages, page=page, type=type)
    items = db.get_items_per_page(page, items_per_page)
    items_count = db.get_items()
    total_pages = math.ceil(len(items_count) / items_per_page)
    return render_template('items.html', items=items, total_pages=total_pages, page=page)
