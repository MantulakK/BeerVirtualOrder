from flask import *
import sql_connection as db

mobile_food_bp = Blueprint('mobile_food', __name__, url_prefix='/mobile_food')

@mobile_food_bp.route('/')
def mobile_food():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM articles WHERE article_type = 1')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    insert_object = []
    for record in my_result:
        insert_object.append(dict(zip(column_names, record)))
    cursor.close()
    return render_template('mobile_food.html', articles=insert_object)