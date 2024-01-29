from flask import *
import sql_connection as db

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/')
def orders():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM mainorder')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    insert_object = []
    for record in my_result:
        insert_object.append(dict(zip(column_names, record)))
    cursor.close()
    return render_template('orders.html', orders=insert_object)

@orders_bp.route('/create', methods=['POST'])
def create_order():
    description = request.form['description']
    order_price = request.form['order_price']

    if description and order_price:
        cursor = db.database.cursor()
        
        sql_select = "SELECT * FROM mainorder WHERE description = %s"
        cursor.execute(sql_select, (description,))
        existing_order = cursor.fetchone()
        if existing_order:
            flash('Order with the same name already exists!', 'error')
        else:
            sql = "INSERT INTO mainorder (description, order_price) VALUES (%s, %s)"
            data = (description, order_price)
            cursor.execute(sql, data)
            db.database.commit()
            flash('Order added successfully!', 'success')

    return redirect(url_for('orders.orders'))

@orders_bp.route('/edit/<string:id_mainorder>', methods=['POST'])
def edit_orders(id_mainorder):
    description = request.form['description']
    order_price = request.form['order_price']

    if description and order_price:
        cursor = db.database.cursor()
        sql = "UPDATE mainorder SET description = %s, order_price = %s WHERE id_mainorder = %s"
        data = (description, order_price, id_mainorder)
        cursor.execute(sql, data)   
        db.database.commit()

    return redirect(url_for('orders.orders'))