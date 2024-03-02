import json
import mysql.connector

def get_db_config():
    with open('Settings.json') as f:
        return json.load(f)

def execute_query(query):
    db_config = get_db_config()
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
