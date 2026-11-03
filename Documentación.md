
# Reto temperaturas hecho por Francisco Javier Torres Almagro.

## 1. Explora la API.

**Antes de programar, observa la información que proporciona Open-Meteo. Abre la consulta de temperaturas históricas de Jaén y examina la respuesta.**

[Histórico de temperaturas en Jaen](https://archive-api.open-meteo.com/v1/archive?latitude=37.7796&longitude=-3.7849&start_date=2025-01-01&end_date=2025-01-31&daily=temperature_2m_mean,temperature_2m_max,temperature_2m_min&timezone=Europe%2FMadrid)  

Responde:

**1. ¿Qué información proporciona el servicio?**
Muestra las temperaturas para una estación meteorológica situada a las afueras de la ciudad de Jaén durante el mes de enero de 2025.
**2. ¿Qué significan latitude y longitude?**
Son las coordenadas geográficas, concretamente situan la estación a las afueras de Jaén.
**3. ¿Qué fechas se están consultando?**
Todo el mes de enero de 2025.
**4. ¿Qué información solicitan temperature_2m_mean , temperature_2m_max y temperature_2m_min?**
La temperatura media, la máxima, y la mínima.
**5. ¿En qué formato se presenta la respuesta?**
En formato JSON.
**6. ¿Qué diferencias observas entre esa respuesta y una lista de Python?**

**7. ¿Qué ocurriría si cambiásemos end_date para consultar hasta el 15 de enero?**
Que habría menos datos de temperaturas disponibles.
**8. ¿Qué ventaja tiene consultar una API frente a introducir los datos manualmente?**
Eficiencia y velocidad, aunque también la posibilidad de automatizar procesos.
## 2. Realiza una petición desde Python.

La biblioteca requests permite realizar peticiones HTTP. Instálala desde la terminal:
```bash
python -m pip install requests
```
Crea un archivo llamado meteorologia.py y escribe este programa:
```python
import requests
url = "https://archive-api.open-meteo.com/v1/archive"
parametros = {
"latitude": 37.7796,
"longitude": -3.7849,
"start_date": "2025-01-01",
"end_date": "2025-01-31",
"daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
"timezone": "Europe/Madrid",
}
respuesta = requests.get(url, params=parametros, timeout=30)
respuesta.raise_for_status()
datos = respuesta.json()
print(datos)
```

Ejecuta el programa y observa el resultado. requests.get() envía la petición; raise_for_status() informa de errores HTTP y respuesta.json() convierte la respuesta JSON en objetos de Python. No tienes que importar json : viene incluido en Python. 
Comprueba tu comprensión:

**1. ¿Para qué sirve import requests?**
Para poder realizar la petición a la url.
**2. ¿Qué tipo de objeto es parametros?**
Un diccionario.
**3. ¿Qué diferencia hay entre url y parametros?**
Url es la parte estática y parámetros son la búsqueda dentro de la misma.
**4. ¿Qué hacen timeout=30 y raise_for_status()?**
Timeout=30 establece el tiempo límite a 30 milisegundos.
raise_for_status() sirve para saber si la conexión a la url ha sido exitosa o no dependiendo del estado que devuelva. 
**5. ¿Qué diferencia hay entre respuesta y datos?**
Respuesta está en texto plano, datos está formateado a json.
**6. ¿Qué podría ocurrir si falla la conexión o el servidor devuelve un error?**
Que no habría ninguna respuesta.
**7. ¿Por qué separamos los parámetros de la dirección URL?**
Para poder modificarlos a nuestro antojo para poder cambiar los datos recibidos según nuestras necesidades.
**8. ¿En qué se diferencia una petición GET de una petición POST?**
Una petición GET obtiene los datos o respuesta de la url.
Una petición POST manda datos a una url

## 3. Explora la estructura de los datos.

Examina el diccionario datos . Puedes empezar mostrando sus claves:

```python
print(datos.keys())
```

**1. ¿Qué valores tienen las claves latitude y longitude ?**
Latitude: 37.785587, longitude: -3.7349243
**2. ¿Qué claves contiene diarios ?**
Las fechas
**3. ¿Qué unidades se utilizan para la temperatura?**
Grados celsius.
**4. ¿Qué tipos de dato devuelven type(datos['daily']) , type(datos['daily']['time']) y type(datos['daily']["temperature_2m_mean"])?**
type(datos['daily'])=Diccionario.
type(datos['daily']['time'])=Lista.
type(datos['daily']["temperature_2m_mean"])=Lista.
**5. ¿Cuántas fechas y temperaturas has obtenido?**
31 fechas y 31 temperaturas.
**6. Comprueba que las listas de fechas, temperaturas medias, máximas y mínimas tienen la misma longitud. ¿Por qué deben coincidir?**
Porque si no habría algún dato no registrado o perdido.
**7. Muestra la primera fecha, la temperatura media del primer día y la máxima del último.**
Primera fecha:
```python
print("Primera fecha:", datos['daily']['time'][0])
Primera fecha: 2025-01-01
```
Temperatura media del primer día:
```python
print("Temperatura media del primer día:", datos['daily']["temperature_2m_mean"][0])
Temperatura media del primer día: 7.1
```
Temperatura máxima del último día:
```python
print("Temperatura máxima del último día:", datos['daily']["temperature_2m_max"][-1])
Temperatura máxima del último día: 10.5
```
**8. ¿Qué sucede si intentas acceder a una posición que no existe?**
Da un error:
```python
    print("Temperatura máxima del último día:", datos['daily']["temperature_2m_max"][-50])
                                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^
IndexError: list index out of range
```
**9. ¿Cómo comprobarías si una clave está presente antes de utilizarla?**
