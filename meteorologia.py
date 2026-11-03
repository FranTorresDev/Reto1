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
print("\n")

print(datos.keys())

print("\n")
print(type(datos['daily']))
print(type(datos['daily']['time']))
print(type(datos['daily']["temperature_2m_mean"]))
print(len(datos))
## 6. Comprueba que las listas de fechas, temperaturas medias, máximas y mínimas tienen la misma longitud. ¿Por qué deben coincidir?
print("Longitud de fechas:", len(datos['daily']['time']))
print("Longitud de temperaturas medias:", len(datos['daily']["temperature_2m_mean"]))
print("Longitud de temperaturas máximas:", len(datos['daily']["temperature_2m_max"]))
print("Longitud de temperaturas mínimas:", len(datos['daily']["temperature_2m_min"]))
print("\n")
print("Primera fecha:", datos['daily']['time'][0])
print("Temperatura media del primer día:", datos['daily']["temperature_2m_mean"][0])
print("Temperatura máxima del último día:", datos['daily']["temperature_2m_max"][-1])
# print("Temperatura máxima del último día:", datos['daily']["temperature_2m_max"][-50])
