from flask import *
import sql_connection as db
mobile_index_bp = Blueprint('mobile_index', __name__, url_prefix='/mobile_index')


@mobile_index_bp.route('/')
def mobile_index():
    return render_template('mobile_index.html')

