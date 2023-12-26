
# from dbConnection import *
from flask import Flask
import json
import mysql.connector



cnx = mysql.connector.connect(user='root', password='admin357159',
                                host='127.0.0.1',
                                database='cookies_monarch',
                                use_pure=False)
cursor = cnx.cursor()

query = ("SELECT userFirstName FROM users")

    
cursor.execute(query)
rows = cursor.fetchall() 
json_output = json.dumps(rows)  
json_output2 = json.dumps(json_output)
print(json_output2)



