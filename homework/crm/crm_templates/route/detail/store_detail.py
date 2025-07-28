from flask import Blueprint, render_template, request
import database as db  
store_detail_bp = Blueprint('store_detail', __name__, template_folder='../templates')

@store_detail_bp.route('/store_detail')
def store_detail():
    store_id = request.args.get('id').strip()
    store = db.get_stores_by_id(store_id)
    monthly_sales = db.get_monthly_sales(store_id)
    regular_customers = db.get_regular_customers_per_store(store_id)

    return render_template('detail/store_detail.html', store=store, monthly_data=monthly_sales, regular_customers=regular_customers)
