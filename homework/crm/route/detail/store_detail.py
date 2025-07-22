from flask import Blueprint, render_template, request
import database as db  # 위의 함수가 포함된 파일

store_detail_bp = Blueprint('store_detail', __name__, template_folder='../templates')

@store_detail_bp.route('/store_detail')
def store_detail():
    store_id = request.args.get('id')
    print(store_id)
    store = db.get_stores_by_id(store_id)
    monthly_sales = db.get_monthly_sales(store_id)
    print(monthly_sales)

    

    return render_template('detail/store_detail.html', store=store, monthly_data=monthly_sales)
