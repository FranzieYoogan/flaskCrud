from flask import Flask
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)  # Setup the flask app by creating an instance of Flask


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin357159'
app.config['MYSQL_DB'] = 'cookies_monarch'




@cross_origin() # Remove in production
def search():
 cnx = mysql.connector.connect(user='root', password='admin357159',
                              host='127.0.0.1',
                              database='cookies_monarch',
                              use_pure=False)
 return cnx.cursor()


# Running app
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3001)