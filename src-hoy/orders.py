from flask import *
import sql_connection as db

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/')
def orders():
    cursor = db.database.cursor()
    cursor.execute('SELECT o.id_order, o.id_table, o.order_state, o.total_price, o.order_datetime, t.table_num FROM `order` o INNER JOIN qrtable t ON o.id_table = t.id_table WHERE o.order_state = "ABIERTO"')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    insert_object = []
    for record in my_result:
        insert_object.append(dict(zip(column_names, record)))
    cursor.close()
    return render_template('orders.html', order=insert_object)

@orders_bp.route('/order_detail/<int:order_id>')
def order_detail(order_id):
    cursor = db.database.cursor()
    cursor.execute('SELECT id_article, amount, order_price FROM order_det WHERE id_order = %s AND detail_state = 1', (order_id,))
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    detail_list = []
    for record in my_result:
        detail_list.append(dict(zip(column_names, record)))
    cursor.close()
    return jsonify(detail_list)