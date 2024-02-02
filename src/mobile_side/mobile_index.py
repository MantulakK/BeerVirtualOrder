from flask import *
import sql_connection as db
mobile_index_bp = Blueprint('mobile_index', __name__, url_prefix='/mobile_index')


@mobile_index_bp.route('/')
def mobile_index():
    table_num = request.args.get('table_num')
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