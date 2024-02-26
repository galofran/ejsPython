import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=AL12059\SQLEXPRESS;DATABASE=walmart;UID=usuario1;PWD=usuario1')
    #En mi caso mi servidor es " . " y mi base de datos se llama "Pruebaa", reemplazas por los valores que tengas
    print("Conexion Exitosa") #Ponemos este mensaje para que nos confirme la conexion
    cursor = connection.cursor()
    cursor.execute("SELECT TOP 10 * FROM Walmart_sales ORDER BY Temperature DESC;;")
    #SELECT TOP 10 * FROM Walmart_sales;
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close() #cerramos la conexion para ahorrar recursos