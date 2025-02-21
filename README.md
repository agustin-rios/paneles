
# Solar Panel Calculation Tool

Este repositorio contiene una herramienta para calcular cuántos paneles solares caben en un área determinada. La herramienta se desarrolló inicialmente en un Jupyter Notebook y luego se integró en una aplicación web con Flask generado con IA para facilitar su uso.

## Estructura del Proyecto

El repositorio se organiza de la siguiente manera:

- `src.ipynb`: Jupyter Notebook que contiene el código experimental y pasos seguidos para resolver el problema.
- `app.py`: Aplicación Flask que ofrece una interfaz web para interactuar con la herramienta.
- `templates/index.html`: Plantilla HTML para la interfaz de usuario de la aplicación web.

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone <url_del_repositorio>
   cd <nombre_del_repositorio>
   ```

2. **Instalar dependencias**:

   Asegúrate de tener un entorno virtual configurado y luego instala las dependencias necesarias.

   ```bash
   pip install Flask
   ```

3. **Ejecutar la aplicación Flask**:

   Para ejecutar la aplicación localmente, usa el siguiente comando:

   ```bash
   python app.py
   ```

   La aplicación estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Uso

### Jupyter Notebook

El archivo `src.ipynb` contiene el código experimental que puedes ejecutar en tu entorno local de Jupyter Notebook. Este archivo te permitirá experimentar con los cálculos directamente.

### Aplicación Web

La aplicación Flask proporciona una interfaz fácil de usar para interactuar con el cálculo de paneles solares. Al acceder a la página principal (`index.html`), podrás ingresar las dimensiones del área y obtener el número de paneles que caben en ese espacio.
