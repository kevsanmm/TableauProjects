# Proyecto OpenWeather API - Tableau

Este proyecto se centra en el análisis de datos climáticos utilizando la API de OpenWeather y herramientas de visualización como Tableau. A continuación se presentan las interpretaciones y resultados clave obtenidos de los datos.

## Interpretación de Datos Climáticos

### 1. Matriz de Correlación
- **Temperatura (°C) vs Humedad (%)**: Hay una correlación negativa moderada de aproximadamente **-0.34**, lo que indica que, en general, a medida que la temperatura aumenta, la humedad tiende a disminuir. Esto puede ser esperado en climas cálidos donde el aire más caliente puede sostener más humedad, pero no necesariamente significa que haya más humedad.
  
- **Temperatura (°C) vs Velocidad del Viento (m/s)**: La correlación es ligeramente negativa (**-0.13**), lo que sugiere que no hay una relación fuerte entre la temperatura y la velocidad del viento. Esto indica que, en los datos analizados, no hay un patrón claro de cómo varía la temperatura con respecto a la velocidad del viento.
  
- **Humedad (%) vs Velocidad del Viento (m/s)**: La correlación es muy débil (**0.10**), lo que sugiere que la humedad y la velocidad del viento no están significativamente relacionadas en estos datos.

### 2. Datos de Temperatura vs Humedad por Continente
| Continente      | Temperatura Promedio (°C) | Humedad Promedio (%) |
|------------------|---------------------------|-----------------------|
| África           | 26.95                     | 56                    |
| Asia             | 23.13                     | 76.5                  |
| Australia        | 16.73                     | 75.25                 |
| Europa           | 9.42                      | 74.25                 |
| Norteamérica     | 17.96                     | 67.5                  |
| Sudamérica       | 20.54                     | 74                    |

- **África**: Con una temperatura promedio de 26.95 °C, África tiene las temperaturas más altas. La temperatura mínima registrada es de 23.79 °C y la máxima alcanza 31.42 °C, lo que refleja climas cálidos y tropicales.
  
- **Asia**: La temperatura promedio es de 23.13 °C. Con una variabilidad moderada (desviación estándar de 4.00 °C), las temperaturas oscilan entre 17.54 °C y 26.05 °C.
  
- **Australia**: Presenta una temperatura promedio de 16.73 °C con un rango entre 8.96 °C y 28.60 °C. Esto indica una diversidad climática considerable.
  
- **Europa**: La temperatura más baja, con un promedio de 9.42 °C y variando entre 6.42 °C y 11.74 °C. Esto es consistente con climas templados.
  
- **Norteamérica**: Con una temperatura promedio de 17.96 °C, las temperaturas varían de 11.95 °C a 21.46 °C, indicando un clima variado.
  
- **Sudamérica**: La temperatura promedio es de 20.54 °C, con temperaturas mínimas de 18.34 °C y máximas de 25.21 °C, sugiriendo climas cálidos y húmedos.

### 3. Datos de Temperatura vs Velocidad del Viento por Continente
| Continente      | Velocidad Promedio del Viento (m/s) |
|------------------|-------------------------------------|
| África           | 2.46                                |
| Asia             | 1.75                                |
| Australia        | 2.28                                |
| Europa           | 4.61                                |
| Norteamérica     | 4.25                                |
| Sudamérica       | 5.59                                |

- **África**: Promedio de 2.46 m/s, con un rango que va de 1.92 m/s a 3.61 m/s, sugiriendo condiciones relativamente estables.
  
- **Asia**: Con un promedio de 1.75 m/s, los vientos son generalmente suaves.
  
- **Australia**: La velocidad del viento promedio es de 2.28 m/s, mostrando un clima en su mayoría tranquilo.
  
- **Europa**: La velocidad del viento promedio de 4.61 m/s es la más alta, sugiriendo un clima más dinámico.
  
- **Norteamérica**: Promedio de 4.25 m/s, lo que sugiere la presencia de tormentas y fenómenos climáticos activos.
  
- **Sudamérica**: Presenta una velocidad de viento promedio de 5.59 m/s, con un rango que puede estar influenciado por su geografía montañosa.

## Conclusiones Generales
- **Tendencias Climatológicas**: Los datos sugieren que hay una tendencia a que las áreas más cálidas tiendan a tener menos humedad, mientras que las regiones más frías tienden a ser más húmedas.
- **Diversidad Climática**: La variabilidad de temperaturas y humedades entre continentes subraya la diversidad de climas en todo el mundo.
- **Influencia de Factores Climáticos**: La débil correlación entre las variables indica que otros factores, como la geografía y la ubicación, podrían estar influyendo en el clima más que la temperatura, la humedad o la velocidad del viento por sí solas.

Este análisis proporciona una visión general del clima en diferentes continentes y puede servir como base para discusiones más profundas sobre la climatología global.

## Información sobre la API

Este proyecto utiliza la [API de OpenWeather](https://openweathermap.org/api) para obtener datos climáticos en tiempo real. Se requiere una clave API, que se puede obtener creando una cuenta en su sitio web. Asegúrate de seguir las directrices de uso de la API y de manejar los datos con responsabilidad.

### Ejemplo de Código para Obtener Datos
Aquí hay un ejemplo de cómo se puede hacer una solicitud a la API para obtener datos climáticos:

```python
import requests

# Define tu clave API
api_key = "YOUR_API_KEY"
# Define la ciudad para la que deseas obtener datos
city = "London"
# Realiza la solicitud a la API
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
data = response.json()

print(data)
