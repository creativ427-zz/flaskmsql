import mysql.connector
 
config = {
     'user' : 'root',
     'password' : '123456',
     'host' : 'localhost'
    }

db = mysql.connector.connect(**config)
cursor = db.cursor()