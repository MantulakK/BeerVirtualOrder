from flask import *
import sql_connection as db

tables_bp = Blueprint('tables', __name__, url_prefix='/tables')

@tables_bp.route('/')
def tables():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM qrtable')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    insert_object = []
    for record in my_result:
        insert_object.append(dict(zip(column_names, record)))
    cursor.close()
    return render_template('tables.html', tables=insert_object)

@tables_bp.route('/create', methods=['POST'])
def create_tables():
    table_num = request.form['table_num']

    if table_num:
        cursor = db.database.cursor()

        sql_select = "SELECT * FROM qrtable WHERE table_num = %s"
        cursor.execute(sql_select, (table_num,))
        existing_table = cursor.fetchone()
        if existing_table:
            flash('Table with the same number already exists!', 'error')
        else:
            sql = "INSERT INTO qrtable (table_num) VALUES (%s)"
            data = (table_num,)  # Use a tuple for the data
            cursor.execute(sql, data)
            db.database.commit()
            flash('Table Added Successfully!', 'success')

    return redirect(url_for('tables.tables'))

@tables_bp.route('/edit/<int:id_table>', methods=['POST'])
def edit_table(id_table):
    data = request.get_json()
    table_num = data.get('tableNum')

    cursor = db.database.cursor()
    sql = "UPDATE qrtable SET table_num = %s WHERE id_table = %s"
    data = (table_num, id_table)
    cursor.execute(sql, data)
    db.database.commit()

    return jsonify({"message": "success"})
