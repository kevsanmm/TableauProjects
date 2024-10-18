# Análisis de Precios de Bitcoin

Este proyecto tiene como objetivo analizar el comportamiento del precio de Bitcoin utilizando datos históricos. A través de este análisis, se han implementado categorías de precios y se han identificado tendencias clave.

## Estructura del Proyecto

- **`data_analysis.ipynb`**: Notebook que contiene el análisis de los datos de precios.
- **`data/`**: Carpeta que contiene los datos utilizados en el análisis.

## Conceptos Clave

1. **timestamp**
   - **Descripción**: Marca de tiempo que indica cuándo se registró el precio de Bitcoin.
   - **Importancia**: Fundamental para el análisis de series temporales, permitiendo observar cambios a lo largo del tiempo.

2. **price**
   - **Descripción**: Precio de Bitcoin en el momento indicado.
   - **Importancia**: Variable principal del análisis, base para tendencias y comparaciones.

3. **daily_change**
   - **Descripción**: Cambio porcentual del precio en comparación con el período anterior.
   - **Fórmula**: 
     \[
     \text{daily_change} = \left( \frac{\text{price actual} - \text{price anterior}}{\text{price anterior}} \right) \times 100
     \]
   - **Importancia**: Indica la volatilidad diaria del precio.

4. **moving_average_7**
   - **Descripción**: Media móvil de 7 días del precio de Bitcoin.
   - **Importancia**: Ayuda a suavizar fluctuaciones diarias y a identificar tendencias a largo plazo.

5. **max_price**
   - **Descripción**: Indica si el precio actual es el máximo en una ventana de 7 días.
   - **Importancia**: Útil para identificar picos de demanda.

6. **min_price**
   - **Descripción**: Indica si el precio actual es el mínimo en una ventana de 7 días.
   - **Importancia**: Ayuda a detectar oportunidades de compra.

7. **price_category**
   - **Descripción**: Clasificación del precio de Bitcoin en diferentes categorías.
   - **Importancia**: Facilita el análisis visual del comportamiento del precio.

## Ajuste de Bins de Precios

Se han ajustado los bins para categorizar los precios de la siguiente manera:

```python
bins = [59000, 60000, 62000, 64000, 66000, 68000, 70000]
labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High', 'Ultra High']
df['price_category'] = pd.cut(df['price'], bins=bins, labels=labels)
```

## Hallazgos Clave

- **Rangos de Precios**: Los nuevos bins abarcan el rango de precios desde el mínimo de 59,019 hasta el máximo de 67,936.

- **Categorías de Precio**:
  - **Very Low**: 59,000 - 60,000
  - **Low**: 60,001 - 62,000
  - **Medium**: 62,001 - 64,000
  - **High**: 64,001 - 66,000
  - **Very High**: 66,001 - 68,000
  - **Ultra High**: Más de 68,000 (sin datos en este rango).

- **Distribución de Valores**: Las categorías reflejan una buena variedad en los precios, destacando "Low", "Medium", "High", y "Very High".

- **Uso en Visualizaciones**: La columna `price_category` se puede usar para segmentar el análisis de precios y resaltar tendencias.

- **Columna `valley`**: Indica si el precio es un mínimo relativo, útil para identificar puntos de reversión.

## Conclusión

Este análisis proporciona una base sólida para entender el comportamiento del precio de Bitcoin y resaltar patrones y tendencias en el mercado de criptomonedas.
