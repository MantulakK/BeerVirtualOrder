from flask import Blueprint, render_template
import sql_connection as db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/orders')
def view_orders():
    try:
        cursor = db.database.cursor(dictionary=True)
        cursor.execute('SELECT o.id_order, o.order_datetime, q.table_num, od.amount, a.name AS article_name, od.order_price FROM `order` o JOIN order_det od ON o.id_order = od.id_order JOIN articles a ON od.id_article = a.id_article JOIN qrtable q ON o.id_table = q.id_table ORDER BY o.order_datetime DESC')
        orders = cursor.fetchall()
        cursor.close()
        return render_template('admin_orders.html', orders=orders)
    except Exception as e:
        return render_template('error.html', error_message=str(e))
