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