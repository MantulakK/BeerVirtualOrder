from flask import *
import sql_connection as db
mobile_index_bp = Blueprint('mobile_index', __name__, url_prefix='/mobile_index')


@mobile_index_bp.route('/')
def mobile_index():
    table_num = request.args.get('table_num')
    if not table_num:
        return redirect(url_for('mobile_index.connection_denied'))
    return render_template('mobile_index.html', table_num=table_num)

@mobile_index_bp.route('/close_order', methods=['POST'])
def close_order():
    if request.method == 'POST':
        try:
            table_number = request.form.get('table_number')

            # Buscar el id_table correspondiente al número de mesa
            cursor = db.database.cursor()
            cursor.execute('SELECT id_table FROM qrtable WHERE table_num = %s', (table_number,))
            result = cursor.fetchone()

            if result is None:
                return jsonify({'status': 'error', 'message': 'Mesa no encontrada'})
            
            id_table = result[0]

            # Obtener la última orden activa para esa mesa
            cursor.execute('SELECT id_order FROM `order` WHERE id_table = %s AND order_state = %s ORDER BY order_datetime DESC LIMIT 1', (id_table, 'ABIERTO'))
            existing_order = cursor.fetchone()

            if existing_order:
                # Verificar si hay algún registro en "order_det" con detail_state en 0
                cursor.execute('SELECT COUNT(*) FROM order_det WHERE id_order = %s AND detail_state = %s', (existing_order[0], 0))
                detail_state_zero_count = cursor.fetchone()[0]

                if detail_state_zero_count > 0:
                    return jsonify({'status': 'error', 'message': 'Debe confirmar o quitar los pedidos pendientes en el CARRITO antes de cerrar la orden.'})

                # Cerrar la orden
                order_id = existing_order[0]
                cursor.execute('SELECT SUM(order_price) FROM order_det WHERE id_order = %s', (order_id,))
                total_price = cursor.fetchone()[0]

                # Cerrar la orden y actualizar el total_price
                cursor.execute('UPDATE `order` SET order_state = %s, total_price = %s WHERE id_order = %s', ('CERRADO', total_price, order_id))
                db.database.commit()
                return jsonify({'status': 'success'})
            else:
                return jsonify({'status': 'error', 'message': 'No hay una orden activa para esta mesa.'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        return jsonify({'status': 'error', 'message': 'Método no permitido'})
    
@mobile_index_bp.route('/error')
def connection_denied():
    return render_template('connection_denied.html')