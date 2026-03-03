# Explorador de Datos de Anuncios de Vehículos

Este proyecto es una aplicación web interactiva desarrollada en Python que permite explorar un conjunto de datos de anuncios de venta de coches en los Estados Unidos. El objetivo es proporcionar una herramienta visual rápida para entender las características de los vehículos y sus precios.

## Funcionalidades
La aplicación permite al usuario visualizar datos de manera dinámica mediante:
* **Histogramas interactivos**: Al seleccionar la casilla correspondiente, se genera un gráfico que muestra la distribución del kilometraje (`odometer`) de los vehículos.
* **Gráficos de dispersión**: Permite analizar la relación entre el kilometraje y el precio de venta, ayudando a identificar tendencias de mercado.
* **Interfaz Dinámica**: Uso de casillas de verificación para mostrar u ocultar gráficos según la necesidad del usuario.

## Tecnologías Utilizadas
* **Python**: Lenguaje principal.
* **Streamlit**: Para la creación de la interfaz web.
* **Pandas**: Para la carga y manipulación del dataset.
* **Plotly Express**: Para la generación de gráficos interactivos y personalizables.

## Cómo ejecutar la aplicación localmente
1. Asegúrate de tener instalado el entorno virtual con las dependencias listadas en `requirements.txt`.
2. Ejecuta el comando:
   ```bash
   streamlit run app.py

## Enlace a la aplicación en Render
https://proyecto-vehiculos-1mzw.onrender.com