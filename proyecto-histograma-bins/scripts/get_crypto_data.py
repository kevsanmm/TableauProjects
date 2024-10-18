import os
import requests
import pandas as pd

# Define la criptomoneda que quieres analizar y el número de días de datos
crypto_id = "bitcoin"  # Puedes cambiarlo a otra criptomoneda como 'ethereum', 'litecoin', etc.
vs_currency = "usd"
days = 90  # Días de backfilling

# URL de la API de CoinGecko
api_url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
params = {
    "vs_currency": vs_currency,
    "days": days
}

# Obtener datos de la API
response = requests.get(api_url, params=params)
if response.status_code == 200:
    data = response.json()
else:
    raise Exception(f"Error al obtener datos: {response.status_code}")

# Crear un DataFrame con los precios históricos
prices = data["prices"]  # Precios históricos
df = pd.DataFrame(prices, columns=["timestamp", "price"])

# Convertir el timestamp de Unix a fecha legible
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Definir ruta absoluta para guardar el CSV
output_path = "/Users/alexandersandoval/Documents/GitHub/TableauProjects/proyecto-histograma-bins/data/raw/crypto_data.csv"

# Guardar los datos en un archivo CSV
df.to_csv(output_path, index=False)

print(f"Datos de {crypto_id} guardados en {output_path}")
