from flask import Flask,request,render_template,redirect,url_for
from flaskext.mysql import MySQL
import yaml

app = Flask(__name__)


mysql = yaml.full_load(open('db.yaml' ))
app.config['MYSQL_DATABASE_USER'] = mysql['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = mysql['mysql_password']
app.config['MYSQL_DATABASE_DB'] = mysql['mysql_db']
app.config['MYSQL_DATABASE_HOST'] = mysql['mysql_host']
mysql = MySQL(app)

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        #id = request.form['id']
        title = request.form['title']
        author = request.form['author']
        publisher = request.form['publisher']
        year_published = request.form['year']

        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO books (title,author,publisher,year_published) VALUES(%s, %s, %s, %s)"
        result = cursor.execute(sql, (title,author,publisher,year_published))
        conn.commit()
        if result:
            return redirect ("/view")
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/view")
def view():
    conn = mysql.connect()
    cursor = conn.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    if cursor.rowcount < 1:
        return render_template("view.html", msg="No info found")
    else:
        rows = cursor.fetchall()
        return render_template("view.html", rows=rows)



if __name__ == '__main__':
    app.run(debug=True)