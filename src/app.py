from flask import *
from flask_mysqldb import *
import os
import sql_connection as db

#ENDPOINTS ADMINISTRATIVOS
from articles import articles_bp
from orders import orders_bp
from qrcodes import qrcodes_bp
#from orderdet import orderdet_bp
from tables import tables_bp

#ENDPOINTS CLIENTE
from mobile_side.mobile_index import mobile_index_bp
from mobile_side.mobile_food import mobile_food_bp

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'templates', 'static')
app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(24)

app.register_blueprint(articles_bp)
app.register_blueprint(orders_bp)
#app.register_blueprint(orderdet_bp)
app.register_blueprint(tables_bp)
app.register_blueprint(qrcodes_bp)

app.register_blueprint(mobile_index_bp)
app.register_blueprint(mobile_food_bp)

#-- APP.ROUTE GENERA UN REDIRECCIONAMIENTO A OTRAS PESTAÑAS CREADAS. SOLO EL "(/)" INDICA LA PAGINA RAIZ PRINCIPAL.
@app.route('/')
def index():
    return render_template('index.html')

def pageDown(error):
    return render_template('404.html'), 404
    #return redirect(url_for('mainmenu'))

################################-- ESTO SIMPLEMENTE EJECUTA LA APP
if __name__ == '__main__': 
    app.register_error_handler(404, pageDown)
    # app.add_url_rule('/query_string', view_func=query_string)
    app.run(debug=True, port=5000)