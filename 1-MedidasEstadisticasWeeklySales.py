import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=AL12059\SQLEXPRESS;DATABASE=walmart;UID=usuario1;PWD=usuario1')
    cursor = connection.cursor()

    #Medidas estadísticas para "Weekly Sales"
    cursor.execute("SELECT * FROM Walmart_sales")
    rows = cursor.fetchall()
    lenRows = len(rows)
    sumaVentasSemanales = 0

    for r in rows:
        sumaVentasSemanales += float(r.Weekly_Sales)     
    print(f"Media de Weekly Sales: {sumaVentasSemanales/lenRows}")

    cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY CAST(Weekly_Sales AS FLOAT)) OVER () AS Mediana_Weekly_Sales FROM Walmart_sales;")
    medianaVentas = cursor.fetchone()
    print(f"Mediana de Weekly Sales: {medianaVentas[0]}")

    cursor.execute("SELECT TOP 1 WITH TIES Weekly_Sales AS Moda_Weekly_Sales FROM Walmart_sales ORDER BY COUNT(*) OVER (PARTITION BY Weekly_Sales) DESC;")
    modaVentas = cursor.fetchone()
    print(f"Moda de Weekly Sales: {modaVentas[0]}")

    cursor.execute("SELECT STDEV(CAST(Weekly_Sales AS DECIMAL)) AS Desviacion_Estandar_Weekly_Sales FROM Walmart_sales;")
    desviacioVentas = cursor.fetchone()
    print(f"Desviación Estándar de Weekly_Sales: {desviacioVentas[0]}")
    
except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close() #cerramos la conexion para ahorrar recursos