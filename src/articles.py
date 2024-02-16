from flask import *
import sql_connection as db

articles_bp = Blueprint('articles', __name__, url_prefix='/articles')

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
    url = request.form['url']

    if name and brand and description and article_type and single_price and url:
        cursor = db.database.cursor()
        
        sql_select = "SELECT * FROM articles WHERE name = %s"
        cursor.execute(sql_select, (name,))
        existing_article = cursor.fetchone()
        if existing_article:
            flash('Item with the same name already exists!', 'error')
        else:
            sql = "INSERT INTO articles (name, brand, description, article_type, single_price, url) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (name, brand, description, article_type, single_price, url)
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
    url = request.form['url']

    if name and brand and description and article_type and single_price and url:
        cursor = db.database.cursor()
        sql = "UPDATE articles SET name = %s, brand = %s, description = %s, article_type = %s, single_price = %s,  url = %s WHERE id_article = %s"
        data = (name, brand, description, article_type, single_price, url, id_article)
        cursor.execute(sql, data)
        db.database.commit()

    return redirect(url_for('articles.articles'))