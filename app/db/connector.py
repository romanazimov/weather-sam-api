import mysql.connector

def connector(query):
    cnx = mysql.connector.connect(host='localhost', database='weather_data', user='root', password='')
    cursor = cnx.cursor(dictionary=True)

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    cnx.close()

    return results