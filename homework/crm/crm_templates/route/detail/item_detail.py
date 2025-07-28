from flask import Blueprint, render_template, request
import database as db 

item_detail_bp = Blueprint('item_detail', __name__, template_folder='../templates')

@item_detail_bp.route('/item_detail')
def order_detail():
    item_id = request.args.get('id')
    item = db.get_item_by_id(item_id)
    unit_price = int(item[0]['UnitPrice'])
    print(unit_price)
    monthly_count = db.get_item_monthly_count(item_id, unit_price)
    result = []
    for i in monthly_count:
        result.append(i[1])
    print(result)
    return render_template('detail/item_detail.html', item=item, monthly_count=monthly_count, result=result)
