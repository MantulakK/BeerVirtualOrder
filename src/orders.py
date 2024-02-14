from flask import *
import sql_connection as db
from flask import make_response
from flask import current_app
from openpyxl import Workbook
from datetime import datetime
import os


orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

# @orders_bp.route('/')
# def orders():
#     cursor = db.database.cursor()
#     cursor.execute('SELECT o.id_order, o.id_table, o.order_state, o.total_price, o.order_datetime, t.table_num FROM `order` o INNER JOIN qrtable t ON o.id_table = t.id_table WHERE o.order_state = "ABIERTO"')
#     column_names = cursor.column_names
#     my_result = cursor.fetchall()
#     insert_object = []
#     for record in my_result:
#         insert_object.append(dict(zip(column_names, record)))
#     cursor.close()
#     return render_template('orders.html', order=insert_object)

@orders_bp.route('/')
def orders():
    cursor = db.database.cursor()
    cursor.execute('SELECT o.id_order, o.id_table, o.order_state, o.total_price, o.order_datetime, t.table_num FROM `order` o INNER JOIN qrtable t ON o.id_table = t.id_table WHERE o.order_state = "CERRADO"')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    closed_orders = []
    for record in my_result:
        closed_orders.append(dict(zip(column_names, record)))
    cursor.close()
    
    # Consulta para obtener los pedidos abiertos
    cursor = db.database.cursor()
    cursor.execute('SELECT o.id_order, o.id_table, o.order_state, o.total_price, o.order_datetime, t.table_num FROM `order` o INNER JOIN qrtable t ON o.id_table = t.id_table WHERE o.order_state = "ABIERTO"')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    open_orders = []
    for record in my_result:
        open_orders.append(dict(zip(column_names, record)))
    cursor.close()
    
    return render_template('orders.html', open_orders=open_orders, closed_orders=closed_orders)

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
        ws.append(["Nombre del Negocio:", "Datos del Pedido:"])
        ws.append(["", ""])
        ws.append(["", "Número de Orden:", order_details[0]])
        ws.append(["", "Precio:", order_details[1]])
        ws.append(["", "Día y Fecha:", order_datetime.strftime("%Y-%m-%d %H:%M:%S")])

        # Obtener la ruta del directorio del escritorio
        desktop_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Guardar el libro de Excel en el escritorio
        file_path = os.path.join(desktop_dir, f"ticket_{order_id}.xlsx")
        wb.save(file_path)

        # Crear una respuesta para descargar el archivo
        response = make_response(send_file(file_path, as_attachment=True, attachment_filename=f"ticket_{order_id}.xlsx"))
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

        return response
    else:
        # Si no se encuentra el pedido, devolver un mensaje de error
        return "Pedido no encontrado", 404