import mysql.connector

def connector(query):
    cnx = mysql.connector.connect(host='localhost', database='weather_data', user='root', password='')
    cursor = cnx.cursor()
    cursor.execute(query)

    results = []
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    cursor.close()
    cnx.close()

    return results