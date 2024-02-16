from flask import *
import sql_connection as db
from flask import make_response
from flask import current_app
from openpyxl import Workbook
from datetime import datetime
import os
import io

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/')
def orders():
    #CONSULTA PARA OBTENER PEDIDOS CERRADOS
    cursor = db.database.cursor()
    cursor.execute('SELECT o.id_order, o.id_table, o.order_state, o.total_price, o.order_datetime, t.table_num FROM `order` o INNER JOIN qrtable t ON o.id_table = t.id_table WHERE o.order_state = "CERRADO"')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    closed_orders = []
    for record in my_result:
        closed_orders.append(dict(zip(column_names, record)))
    cursor.close()
    
    #CONSULTA PARA OBTENER PEDIDOS ABIERTOS
    cursor = db.database.cursor()
    cursor.execute('SELECT o.id_order, o.id_table, o.order_state, o.total_price, o.order_datetime, t.table_num FROM `order` o INNER JOIN qrtable t ON o.id_table = t.id_table WHERE o.order_state = "ABIERTO"')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    open_orders = []
    for record in my_result:
        open_orders.append(dict(zip(column_names, record)))
    cursor.close()

    #CONSULTA PARA OBTENER TODAS LAS MESAS CARGADAS
    cursor = db.database.cursor()
    cursor.execute('SELECT * from qrtable')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    registered_tables = []
    for record in my_result:
        registered_tables.append(dict(zip(column_names, record)))
    cursor.close()

    #CONSULTA PARA OBTENER ARTICULOS
    cursor = db.database.cursor()
    cursor.execute('SELECT * from articles ORDER BY article_type ASC')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    articles_fetchall = []
    for record in my_result:
        articles_fetchall.append(dict(zip(column_names, record)))
    cursor.close()

    return render_template('orders.html', open_orders=open_orders, closed_orders=closed_orders, registered_tables=registered_tables, articles_fetchall=articles_fetchall)

@orders_bp.route('/order_detail', methods=['GET'])
def order_detail():
    order_id = request.args.get('orderId') # Obtener el orderId desde la solicitud
    cursor = db.database.cursor()
    #cursor.execute('SELECT id_article, amount, order_price FROM order_det WHERE id_order = %s AND detail_state = 1', (order_id,))
    cursor.execute('''
    SELECT od.id_article, a.name, od.amount, od.order_price 
    FROM order_det od 
    JOIN articles a ON od.id_article = a.id_article 
    WHERE od.id_order = %s AND od.detail_state = 1
''', (order_id,))
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    detail_list = []
    for record in my_result:
        detail_list.append(dict(zip(column_names, record)))
    cursor.close()
    return jsonify(detail_list)

##FUNCION PARA DESCARGAR UN EXCEL CON LA INFORMACIÓN DE UN PEDIDO CERRADO (TICKET)
@orders_bp.route('/download_ticket/<int:order_id>', methods=['GET'])
def download_ticket(order_id):
    # Obtener los detalles del pedido desde la base de datos
    cursor = db.database.cursor()
    cursor.execute('SELECT id_order, total_price, order_datetime FROM `order` WHERE id_order = %s', (order_id,))
    order_details = cursor.fetchone()
    cursor.close()

    if order_details:
        # Convertir la cadena de texto en un objeto datetime
        order_datetime = datetime.strptime(order_details[2], "%Y-%m-%d %H:%M:%S")

        # Crear un nuevo libro de Excel y su hoja de cálculo
        wb = Workbook()
        ws = wb.active

        # Escribir los encabezados
        ws.append(["ALMACEN DE LA CERVEZA:", "Datos del Pedido:"])
        ws.append(["", ""])
        ws.append(["", "Número de Orden:", order_details[0]])
        ws.append(["", "Precio:", order_details[1]])
        ws.append(["", "Día y Fecha:", order_datetime.strftime("%Y-%m-%d %H:%M:%S")])

        # Crear una respuesta para descargar el archivo
        response = make_response()

        # Adjuntar el contenido del libro de Excel a la respuesta
        with io.BytesIO() as output:
            wb.save(output)
            response.data = output.getvalue()

        # Establecer los encabezados de la respuesta
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response.headers['Content-Disposition'] = 'attachment; filename="ticket_{}.xlsx"'.format(order_id)

        return response
    else:
        # Si no se encuentra el pedido, devolver un mensaje de error
        return "Pedido no encontrado", 404

@orders_bp.route('/check_open_order', methods=['GET'])
def check_open_order():
    table_num = request.args.get('table_num')  # Obtener el número de mesa de la solicitud

    # Consultar la base de datos para verificar si hay una orden ABIERTA para la mesa seleccionada
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM `order` WHERE id_table = %s AND order_state = "ABIERTO"', (table_num,))
    existing_order = cursor.fetchone()
    cursor.close()

    if existing_order:
        # Si ya hay una orden ABIERTA para la mesa seleccionada, devolver True
        return jsonify({'exists': True})
    else:
        # Si no hay una orden ABIERTA para la mesa seleccionada, devolver False
        return jsonify({'exists': False})


@orders_bp.route('/create_order', methods=['POST'])
def create_order():
    # Obtener los datos del formulario
    table_id = request.form.get('table_id')
    
    # Obtener la fecha y hora actuales
    order_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Establecer el estado del pedido como ABIERTO
    order_state = 'ABIERTO'
    
    # Insertar el nuevo pedido en la base de datos
    cursor = db.database.cursor()
    cursor.execute('INSERT INTO `order` (id_table, order_datetime, order_state, total_price) VALUES (%s, %s, %s, %s)', (table_id, order_datetime, order_state, 0))
    db.database.commit()
    cursor.close()

    # Devolver una respuesta de éxito
    return 'Pedido creado exitosamente', 200

@orders_bp.route('/create_order_detail', methods=['POST'])
def create_order_detail():
    try:
        # Obtener los datos del formulario de la solicitud AJAX
        order_id = request.form.get('order_id')
        article_id = request.form.get('article_id')
        quantity = request.form.get('quantity')  # Corregido: obtener la cantidad en lugar de amount
        single_price = request.form.get('single_price')
        
        # Verificar si los valores son válidos
        if not all([order_id, article_id, quantity, single_price]):
            raise ValueError('Faltan datos en la solicitud')
        
        # Convertir los valores a números enteros para el cálculo
        order_id = int(order_id)
        article_id = int(article_id)
        quantity = int(quantity)
        single_price = int(single_price)
        
        # Calcular el precio total del pedido
        order_price = single_price * quantity
        
        # Realizar la inserción en la tabla order_det en la base de datos
        cursor = db.database.cursor()
        cursor.execute('INSERT INTO order_det (id_order, id_article, amount, order_price, detail_state) VALUES (%s, %s, %s, %s, %s)', (order_id, article_id, quantity, order_price, 1))
        db.database.commit()
        cursor.close()

        # Devolver una respuesta de éxito
        return jsonify({'message': 'Detalle del pedido creado correctamente'}), 200
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir durante la creación del detalle del pedido
        return jsonify({'error': str(e)}), 500

@orders_bp.route('/close_order', methods=['POST'])
def close_order():
    try:
        # Obtener el ID de la orden de la solicitud AJAX
        order_id = request.form.get('order_id')
        
        # Sumar los precios de los detalles del pedido
        cursor = db.database.cursor()
        cursor.execute('SELECT SUM(order_price) FROM order_det WHERE id_order = %s', (order_id,))
        total_price = cursor.fetchone()[0]
        
        # Actualizar el estado de la orden a "CERRADO"
        cursor.execute('UPDATE `order` SET order_state = %s, total_price = %s WHERE id_order = %s', ('CERRADO', total_price, order_id))
        db.database.commit()
        cursor.close()
        
        # Devolver una respuesta de éxito
        return jsonify({'message': 'Orden cerrada correctamente'}), 200
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir durante el cierre de la orden
        return jsonify({'error': str(e)}), 500