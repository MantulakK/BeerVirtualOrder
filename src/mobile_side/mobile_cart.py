from flask import *
import sql_connection as db
mobile_cart_bp = Blueprint('mobile_cart', __name__, url_prefix='/mobile_cart')


@mobile_cart_bp.route('/')
def mobile_cart():
    table_num = request.args.get('table_num')
    if not table_num:
        return redirect(url_for('mobile_index.connection_denied'))

    try:
        # Buscar el id_table correspondiente al número de mesa
        cursor = db.database.cursor()
        cursor.execute('SELECT id_table FROM qrtable WHERE table_num = %s', (table_num,))
        result = cursor.fetchone()

        if result is None:
            return jsonify({'status': 'error', 'message': 'Mesa no encontrada'})
        
        id_table = result[0]

        # Obtener la última orden activa para esa mesa
        cursor.execute('SELECT id_order FROM `order` WHERE id_table = %s AND order_state = %s ORDER BY order_datetime DESC LIMIT 1', (id_table, 'ABIERTO'))
        existing_order = cursor.fetchone()

        if existing_order:
            # Obtener los detalles de la orden
            order_id = existing_order[0]
            #cursor.execute('SELECT * FROM order_det WHERE id_order = %s', (order_id,))
            cursor.execute('SELECT od.id_article, od.amount, od.order_price, od.detail_state, a.name FROM order_det od INNER JOIN articles a ON od.id_article = a.id_article WHERE od.id_order = %s', (order_id,))
            order_details = cursor.fetchall()
            # Calcular el precio total del pedido
            total_price = sum(float(detail[2]) for detail in order_details)

            return render_template('mobile_cart.html', table_num=table_num, order_details=order_details, total_price=total_price)
        else:
            return render_template('mobile_cart.html', table_num=table_num, order_details=None, total_price=0)

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

#FUNCION PARA REALIZAR EL PEDIDO DE ARTÍCULOS
@mobile_cart_bp.route('/checkout', methods=['POST'])
def checkout():
    if request.method == 'POST':
        try:
            table_num = request.json.get('table_num')

            # Buscar el id_table correspondiente al número de mesa
            cursor = db.database.cursor()
            cursor.execute('SELECT id_table FROM qrtable WHERE table_num = %s', (table_num,))
            result = cursor.fetchone()

            if result is None:
                return jsonify({'status': 'error', 'message': 'Mesa no encontrada'})
            
            id_table = result[0]

            # Obtener la última orden activa para esa mesa
            cursor.execute('SELECT id_order FROM `order` WHERE id_table = %s AND order_state = %s ORDER BY order_datetime DESC LIMIT 1', (id_table, 'ABIERTO'))
            existing_order = cursor.fetchone()

            if existing_order:
                # Obtener los detalles de la orden
                order_id = existing_order[0]
                
                # Actualizar el estado detail_state a 1
                cursor.execute('UPDATE order_det SET detail_state = 1 WHERE id_order = %s', (order_id,))
                db.database.commit()

                return jsonify({'status': 'success'})
            else:
                return jsonify({'status': 'error', 'message': 'No hay una orden activa para esta mesa.'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        return jsonify({'status': 'error', 'message': 'Método no permitido'})

#FUNCION PARA ELIMINAR PEDIDOS DE ARTÍCULOS
@mobile_cart_bp.route('/remove_item', methods=['POST'])
def remove_item():
    if request.method == 'POST':
        try:
            data = request.json
            item_id = data.get('item_id')
            table_num = data.get('table_num')  # Obtener table_num del cuerpo de la solicitud

            # Verificar si el número de mesa está especificado
            if not table_num:
                return jsonify({'status': 'error', 'message': 'Número de mesa no especificado'})

            cursor = db.database.cursor()
            cursor.execute('SELECT id_table FROM qrtable WHERE table_num = %s', (table_num,))
            result = cursor.fetchone()

            if result is None:
                return jsonify({'status': 'error', 'message': 'Mesa no encontrada'})
            
            id_table = result[0]

            cursor.execute('SELECT id_order FROM `order` WHERE id_table = %s AND order_state = %s ORDER BY order_datetime DESC LIMIT 1', (id_table, 'ABIERTO'))
            existing_order = cursor.fetchone()

            if existing_order:
                order_id = existing_order[0]
                
                # Eliminar el artículo del carrito
                cursor.execute('DELETE FROM order_det WHERE id_order = %s AND id_article = %s', (order_id, item_id))
                db.database.commit()
                
                # Recalcular el precio total después de eliminar el artículo
                cursor.execute('SELECT * FROM order_det WHERE id_order = %s', (order_id,))
                order_details = cursor.fetchall()
                total_price = sum(detail[5] for detail in order_details)  # Calcular el precio total
            else:
                order_details = []
                total_price = 0.0

            return jsonify({'status': 'success', 'order_details': order_details, 'total_price': total_price})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        return jsonify({'status': 'error', 'message': 'Método no permitido'})

#FUNCIÓN PARA CAMBIAR CANTIDADES
@mobile_cart_bp.route('/change_amount', methods=['POST'])
def change_amount():
    if request.method == 'POST':
        try:
            data = request.json
            item_id = data.get('item_id')
            new_amount = data.get('new_amount')
            table_num = request.args.get('table_num')  # Obtener table_num de los argumentos de la solicitud

            # Verificar si el número de mesa está especificado
            if not table_num:
                return jsonify({'status': 'error', 'message': 'Número de mesa no especificado'})

            cursor = db.database.cursor()

            # Obtener el id_order correspondiente al número de mesa
            cursor.execute('SELECT id_table FROM qrtable WHERE table_num = %s', (table_num,))
            result = cursor.fetchone()

            if result is None:
                return jsonify({'status': 'error', 'message': 'Mesa no encontrada'})

            id_table = result[0]

            # Obtener la última orden activa para esa mesa
            cursor.execute('SELECT id_order FROM `order` WHERE id_table = %s AND order_state = %s ORDER BY order_datetime DESC LIMIT 1', (id_table, 'ABIERTO'))
            existing_order = cursor.fetchone()

            if existing_order:
                order_id = existing_order[0]

                # Actualizar la cantidad del artículo en la tabla order_det
                cursor.execute('UPDATE order_det SET amount = %s WHERE id_order = %s AND id_article = %s', (new_amount, order_id, item_id))
                db.database.commit()

                return jsonify({'status': 'success'})
            else:
                return jsonify({'status': 'error', 'message': 'No hay una orden activa para esta mesa.'})

        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        return jsonify({'status': 'error', 'message': 'Método no permitido'})