import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=AL12059\SQLEXPRESS;DATABASE=walmart;UID=usuario1;PWD=usuario1')
    
    cursor = connection.cursor()
    # Calcular medidas estadísticas para 'Temperature'
    cursor.execute("SELECT AVG(CAST(Fuel_Price AS FLOAT)) FROM Walmart_sales;")
    mediaFuelPrice= cursor.fetchone()
    print(f"Media de Fuel Price: {mediaFuelPrice[0]}")

    cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY CAST(Fuel_Price AS FLOAT)) OVER () AS Mediana_FuelPrice FROM Walmart_sales;")
    medianaFuelPrice = cursor.fetchone()
    print(f"Mediana de Fuel Price: {medianaFuelPrice[0]}")

    cursor.execute("SELECT TOP 1 WITH TIES Fuel_Price AS Moda_FuelPrice FROM Walmart_sales ORDER BY COUNT(*) OVER (PARTITION BY Fuel_Price) DESC;")
    modaFuelPrice = cursor.fetchone()
    print(f"Moda de Fuel Price: {modaFuelPrice[0]}")
    
    cursor.execute("SELECT STDEV(CAST(Fuel_Price AS DECIMAL)) AS Desviacion_Estandar_FuelPrice FROM Walmart_sales;")
    desviacionFuelPrice = cursor.fetchone()
    print(f"Desviación Estándar de Temperature: {desviacionFuelPrice[0]}")

except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()