import pyodbc
import numpy as np

try:
# Configuración de la conexión a la base de datos
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=AL12059\SQLEXPRESS;DATABASE=walmart;UID=usuario1;PWD=usuario1')
    print("Conexion Exitosa")
    cursor = connection.cursor()
    # Ejemplo de datos, reemplázalos con tu propia consulta SQL
    cursor.execute("SELECT CAST(Temperature AS FLOAT) AS Temperature, CAST(Fuel_Price AS FLOAT) AS Fuel_Price, CAST(Unemployment AS FLOAT) AS Unemployment FROM Walmart_sales;")
    resultados = cursor.fetchall()
    # Extraer columnas específicas
    temperature = [row.Temperature for row in resultados if row.Temperature is not None]
    fuel_price = [row.Fuel_Price for row in resultados if row.Fuel_Price is not None]
    unemployment = [row.Unemployment for row in resultados if row.Unemployment is not None]

    # Verificar si hay datos antes de realizar cálculos
    if temperature:
        # Percentiles y Cuartiles para Temperature
        p25_temp = np.percentile(temperature, 25)
        p50_temp = np.percentile(temperature, 50)
        p75_temp = np.percentile(temperature, 75)
        q1_temp = np.percentile(temperature, 25)
        q2_temp = np.percentile(temperature, 50)
        q3_temp = np.percentile(temperature, 75)
        # Imprimir resultados para Temperature
        print(f"Percentiles para Temperature: P25={p25_temp}, P50={p50_temp}, P75={p75_temp}")
        print(f"Cuartiles para Temperature: Q1={q1_temp}, Q2={q2_temp}, Q3={q3_temp}")
    else:
        print("No hay datos válidos para Temperature.")
        
        if fuel_price:
        # Rango Interquartílico (IQR) para Fuel_Price
            iqr_fuel = np.percentile(fuel_price, 75) - np.percentile(fuel_price, 25)
            print(f"Rango Interquartílico (IQR) para Fuel_Price: {iqr_fuel}")
        else:
            print("No hay datos válidos para Fuel_Price.")
    if unemployment:
        # Varianza y Coeficiente de Variación para Unemployment
        varianza_unemployment = np.var(unemployment)
        cv_unemployment = (np.std(unemployment) / np.mean(unemployment)) * 100
        print(f"Varianza para Unemployment: {varianza_unemployment}")
        print(f"Coeficiente de Variación para Unemployment: {cv_unemployment}")
    else:
        print("No hay datos válidos para Unemployment.")
    
except Exception as ex:
        print(ex)
finally:
    if connection:
        connection.close() 