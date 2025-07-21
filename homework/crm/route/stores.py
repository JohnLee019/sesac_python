from flask import Blueprint, render_template, request
import math
import database as db 

stores_bp = Blueprint('stores', __name__, template_folder='../templates')

@stores_bp.route('/stores')
def store():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 20
    name = request.args.get('storename', "").strip()
    area = request.args.get('area', "").strip()
    district = request.args.get('district', "").strip()
    full_area = f"{area} {district}".strip()
    print(district)

    if name or area or district:
        print(db.get_store_name_area(name, area, district, full_area))
        if db.get_store_name_area(name, area, district, full_area):
            store_name_area = db.get_store_name_area(name, area, district, full_area)
            total_pages = math.ceil(len(store_name_area) / items_per_page)
            start = (page - 1) * items_per_page
            end = start + items_per_page
            stores = store_name_area[start: end]
            return render_template('stores.html', stores=stores, total_pages=total_pages, page=page, name=name, area=area, district=district)
        else:
            return "해당 상점은 존재하지 않습니다"

    stores_count = db.get_stores()
    stores = db.get_stores_per_page(page, items_per_page)
    total_pages = math.ceil(len(stores_count) / items_per_page)
    return render_template('stores.html', stores=stores, total_pages=total_pages, page=page)