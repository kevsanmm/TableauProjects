import requests
import csv
from datetime import datetime
import os

# Lista de ciudades, países y continentes
cities = [
    ("Tokyo", "Japan", "Asia"),
    ("Shanghai", "China", "Asia"),
    ("Delhi", "India", "Asia"),
    ("Mumbai", "India", "Asia"),
    ("Moscow", "Russia", "Europe"),
    ("London", "UK", "Europe"),
    ("Berlin", "Germany", "Europe"),
    ("Paris", "France", "Europe"),
    ("New York", "USA", "North America"),
    ("Los Angeles", "USA", "North America"),
    ("Toronto", "Canada", "North America"),
    ("Mexico City", "Mexico", "North America"),
    ("São Paulo", "Brazil", "South America"),
    ("Rio de Janeiro", "Brazil", "South America"),
    ("Buenos Aires", "Argentina", "South America"),
    ("Lima", "Peru", "South America"),
    ("Lagos", "Nigeria", "Africa"),
    ("Cairo", "Egypt", "Africa"),
    ("Kinshasa", "Democratic Republic of the Congo", "Africa"),
    ("Johannesburg", "South Africa", "Africa"),
    ("Sydney", "Australia", "Australia"),
    ("Melbourne", "Australia", "Australia"),
    ("Auckland", "New Zealand", "Australia"),
    ("Brisbane", "Australia", "Australia"),
]

api_key = "42b2beaefa540db299a19dfd2a60b80a"  # Tu API Key de OpenWeather

# Ruta absoluta para el archivo CSV
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(base_dir, "../data/raw/weather_data.csv")

# Leer el CSV existente para verificar duplicados y almacenar los datos
existing_data = {}

if os.path.exists(csv_file):
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Crear una clave única con la combinación de Ciudad y Fecha
            date = row["Timestamp"].split(" ")[0]  # Solo tomar la fecha
            unique_key = (row["City"], date)
            existing_data[unique_key] = row  # Almacenar la fila completa

# Obtener el timestamp de la última ejecución
last_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Preparar una lista para los nuevos datos
new_data = []

# Iterar sobre cada ciudad
for city, country, continent in cities:
    try:
        # Llamada a la API de OpenWeather
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extraer la información relevante
            city_name = data.get("name", "N/A")
            temperature = data["main"].get("temp", "N/A")
            humidity = data["main"].get("humidity", "N/A")
            wind_speed = data["wind"].get("speed", "N/A")
            weather = data["weather"][0].get("main", "N/A")
            description = data["weather"][0].get("description", "N/A")
            date = last_timestamp.split(" ")[0]  # Tomar solo la fecha actual
            
            # Crear una clave única con la combinación de Ciudad y Fecha
            unique_key = (city_name, date)

            # Crear una nueva fila con los datos obtenidos
            new_row = {
                "City": city_name,
                "Country": country,
                "Continent": continent,
                "Temperature (°C)": temperature,
                "Humidity (%)": humidity,
                "Wind Speed (m/s)": wind_speed,
                "Weather": weather,
                "Description": description,
                "Timestamp": last_timestamp
            }

            # Verificar si la clave ya existe en los datos existentes
            if unique_key in existing_data:
                # Reemplazar los datos de la fila existente
                existing_data[unique_key] = new_row
                print(f"Datos de {city_name} actualizados para la fecha {date}.")
            else:
                # Agregar nuevos datos
                new_data.append(new_row)
                print(f"Datos de {city_name} agregados al CSV.")

        else:
            print(f"Error al obtener datos para {city}: {data.get('message', 'Sin mensaje de error')}")
    
    except Exception as e:
        print(f"Ocurrió un error al procesar {city}: {e}")

# Escribir los datos actualizados y nuevos en el CSV
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["City", "Country", "Continent", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Weather", "Description", "Timestamp"])
    writer.writeheader()
    
    # Escribir los datos existentes (actualizados)
    for row in existing_data.values():
        writer.writerow(row)
    
    # Escribir los nuevos datos
    for row in new_data:
        writer.writerow(row)

print(f"Datos de clima actualizados en {csv_file}. Última actualización: {last_timestamp}")
