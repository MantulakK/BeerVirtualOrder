from flask import *
import sql_connection as db
import os

articles_bp = Blueprint('articles', __name__, url_prefix='/articles')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@articles_bp.route('/')
def articles():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM articles')
    column_names = cursor.column_names
    my_result = cursor.fetchall()
    insert_object = []
    for record in my_result:
        insert_object.append(dict(zip(column_names, record)))
    cursor.close()
    return render_template('articles.html', articles=insert_object)

@articles_bp.route('/create', methods=['POST'])
def create_article():
    name = request.form['name']
    brand = request.form['brand']
    description = request.form['description']
    article_type = request.form['article_type']
    single_price = request.form['single_price']

    if name and brand and description and article_type and single_price:
        cursor = db.database.cursor()
        
        sql_select = "SELECT * FROM articles WHERE name = %s"
        cursor.execute(sql_select, (name,))
        existing_article = cursor.fetchone()
        if existing_article:
            flash('Item with the same name already exists!', 'error')
        else:
            sql = "INSERT INTO articles (name, brand, description, article_type, single_price) VALUES (%s, %s, %s, %s, %s)"
            data = (name, brand, description, article_type, single_price)
            cursor.execute(sql, data)
            db.database.commit()
            flash('Item added successfully!', 'success')

    return redirect(url_for('articles.articles'))

@articles_bp.route('/edit/<string:id_article>', methods=['POST'])
def edit_article(id_article):
    name = request.form['name']
    brand = request.form['brand']
    description = request.form['description']
    article_type = request.form['article_type']
    single_price = request.form['single_price']

    if name and brand and description and article_type and single_price:
        cursor = db.database.cursor()
        sql = "UPDATE articles SET name = %s, brand = %s, description = %s, article_type = %s, single_price = %s WHERE id_article = %s"
        data = (name, brand, description, article_type, single_price, id_article)
        cursor.execute(sql, data)
        db.database.commit()

    return redirect(url_for('articles.articles'))

@articles_bp.route('/upload_image', methods=['POST'])
def upload_image():
    if 'imageFile' not in request.files:
        return jsonify({'error': 'No se seleccionó ninguna imagen'}), 400

    image = request.files['imageFile']

    if image.filename == '':
        return jsonify({'error': 'No se seleccionó ninguna imagen'}), 400

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        img_path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(img_path)
        save_image_path_in_database(img_path)
        return jsonify({'imagePath': img_path}), 200

    return jsonify({'error': 'Formato de imagen no permitido'}), 400

def save_image_path_in_database(img_path):
    if img_path:
        cursor = db.database.cursor()
        sql = "INSERT INTO articles (img_path) VALUES (%s)"
        data = (img_path,)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()