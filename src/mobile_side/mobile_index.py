from flask import *
import sql_connection as db
mobile_index_bp = Blueprint('mobile_index', __name__, url_prefix='/mobile_index')


@mobile_index_bp.route('/')
def mobile_index():
    table_num = request.args.get('table_num')
    return render_template('mobile_index.html', table_num=table_num)

