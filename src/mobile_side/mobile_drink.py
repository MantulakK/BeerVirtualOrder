from flask import *
import sql_connection as db

mobile_drink_bp = Blueprint('mobile_drink', __name__, url_prefix='/mobile_drink')

@mobile_drink_bp.route('/')
def mobile_drink():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM articles WHERE article_type = 2')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    insert_object = []
    for record in my_result:
        insert_object.append(dict(zip(column_names, record)))
    cursor.close()
    return render_template('mobile_drink.html', articles=insert_object)

@mobile_drink_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        try:
            # Obtén los datos del artículo desde la solicitud POST
            article_id = request.form.get('article_id')
            article_name = request.form.get('article_name')
            article_price = request.form.get('article_price')
            quantity = request.form.get('quantity')
            table_number = request.form.get('table_number')
            orderdet_price = int(quantity) * float(article_price)

            # Buscar el id_table correspondiente al número de mesa
            cursor = db.database.cursor()
            cursor.execute('SELECT id_table FROM qrtable WHERE table_num = %s', (table_number,))
            result = cursor.fetchone()
            cursor.close()

            if result is None:
                return jsonify({'status': 'error', 'message': 'Mesa no encontrada'})

            id_table = result[0]

            # VERIFICAR ORDEN ABIERTA, SI HAY ORDEN ABIERTA, EL NUEVO PEDIDO VA CON EL ID DE ESA ORDEN. CASO CONTRARIO, SE CREA UNA ORDEN NUEVA.
            cursor = db.database.cursor()
            cursor.execute('SELECT id_order FROM `order` WHERE id_table = %s AND order_state = %s', (id_table, 'ABIERTO'))
            existing_order = cursor.fetchone()
            cursor.close()

            if existing_order:
                # Si hay una orden activa, usa ese ID
                order_id = existing_order[0]
            else:
                # Insertar en la tabla "order"
                cursor = db.database.cursor()
                cursor.execute('INSERT INTO `order` (id_table, order_state, total_price, order_datetime) VALUES (%s, %s, 0, NOW())', (id_table, 'ABIERTO'))
                order_id = cursor.lastrowid  # Obtiene el ID de la orden recién creada
                db.database.commit()
                cursor.close()

            # Insertar en la tabla "order_det"
            if order_id is not None:
                cursor = db.database.cursor()
                cursor.execute('INSERT INTO order_det (id_order, id_article, amount, order_price) VALUES (%s, %s, %s, %s)', (order_id, article_id, quantity, orderdet_price))
                db.database.commit()
                cursor.close()
            else:
                return jsonify({'status': 'error', 'message': 'Error al obtener el ID de la orden'})
            
            return jsonify({'status': 'success'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        # Manejo del error o redirige a una página de error
        return jsonify({'status': 'error', 'message': 'Error al agregar al carrito'})