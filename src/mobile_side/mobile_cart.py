from flask import *
import sql_connection as db
mobile_cart_bp = Blueprint('mobile_cart', __name__, url_prefix='/mobile_cart')


@mobile_cart_bp.route('/')
def mobile_index():
    return render_template('mobile_cart.html')

