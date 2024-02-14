from flask import *
import sql_connection as db
from PIL import Image
import os
import base64
import qrcode

qrcodes_bp = Blueprint('qrcodes', __name__, url_prefix='/qrcodes')

@qrcodes_bp.route('/')
def qrcodes():
    cursor = db.database.cursor()
    cursor.execute('SELECT qr.id_qr, qr.id_table, qr.qr_code, qrtable.table_num FROM qr INNER JOIN qrtable ON qr.id_table = qrtable.id_table')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    insert_object = []
    for record in my_result:
        insert_object.append(dict(zip(column_names, record)))

    # Obtener la información de las mesas
    cursor.execute('SELECT * FROM qrtable')
    column_names_tables = cursor.column_names
    tables_result = cursor.fetchall()
    tables = [dict(zip(column_names_tables, record)) for record in tables_result]

    cursor.close()

    return render_template('qrcodes.html', qrcodes=insert_object, tables=tables)

@qrcodes_bp.route('/create', methods=['POST'])
def create_qrcodes():
    selected_table_id = request.form.get('selected_table')

    # Aquí necesitas obtener el 'table_num' asociado con el 'id_table'
    cursor = db.database.cursor()
    cursor.execute("SELECT table_num FROM qrtable WHERE id_table = %s", (selected_table_id,))
    table_num = cursor.fetchone()[0]
    cursor.close()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Aquí deberías incluir la información necesaria en el código QR (por ejemplo, la URL y la información de la mesa)
    data = f"https://2cf0-2803-a920-8c3-8000-edbe-2a58-f94b-a3c2.ngrok-free.app/mobile_index?table_num={table_num}" 
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen en tu carpeta deseada (por ejemplo, 'static')
    img_path = os.path.join('static', f'qr_mesa_{table_num}.png')
    img.save(img_path)

    # Aquí deberías guardar la información en tu base de datos (tabla 'qr')
    cursor = db.database.cursor()
    cursor.execute("INSERT INTO qr (qr_code, id_table) VALUES (%s, %s)", (img_path, selected_table_id))
    db.database.commit()
    cursor.close()

    flash('Código QR generado y guardado correctamente.', 'success')

    # Redirigir a donde sea necesario después de crear el código QR
    return redirect(url_for('qrcodes.qrcodes'))