import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=AL12059\SQLEXPRESS;DATABASE=walmart;UID=usuario1;PWD=usuario1')
    cursor = connection.cursor()

    #Medidas estadísticas para "Fuel Price"
    cursor.execute("SELECT AVG(Fuel_Price) FROM Walmart_sales")
    mediaFuelPrice = cursor.fetchone()
    print(f"Media de FUEL PRICE: {mediaFuelPrice}")
    
except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close() #cerramos la conexion para ahorrar recursos