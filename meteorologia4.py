# Apartado 4

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

temperaturasMedias = datos['daily']["temperature_2m_mean"]
temperaturasMinimas = datos['daily']["temperature_2m_min"]
temperaturasMaximas = datos['daily']["temperature_2m_max"]

print("Temperaturas mínimas:\n",temperaturasMinimas)
print("Temperaturas máximas:\n",temperaturasMaximas)
print("Temperaturas medias:\n",temperaturasMedias)

# Ejercicio 1
print("Cinco primeras temperaturas: ", temperaturasMedias[:5])
print("Cinco últimas temperaturas: ", temperaturasMedias[-5:])

# Ejercicio 2
print("Número de valores de la lista: ", len(temperaturasMedias))

# Ejercicio 3
temperaturaMasAlta = max(temperaturasMaximas)
print("La temperatura más alta es: ", temperaturaMasAlta)

temperaturaMasBaja = min(temperaturasMinimas)
print("La temperatura más baja es: ", temperaturaMasBaja)

print("Diferencia entre la temperatura más baja y la más alta: ", temperaturaMasAlta-temperaturaMasBaja)

# Ejercicio 4 y 5
numDiasTempMayor15 = 0
numDiasTempMenor10 = 0

temperaturasMayor15=[]
temperaturasMenor10=[]

for temperatura in temperaturasMinimas:
    if temperatura>15:
        numDiasTempMayor15+=1
        temperaturasMayor15.append(temperatura)
    if temperatura<10:
        numDiasTempMenor10+=1
        temperaturasMenor10.append(temperatura)

for temperatura in temperaturasMaximas:
    if temperatura>15:
        numDiasTempMayor15+=1
        temperaturasMayor15.append(temperatura)
    if temperatura<10:
        numDiasTempMenor10+=1
        temperaturasMenor10.append(temperatura)

for temperatura in temperaturasMedias:
    if temperatura>15:
        numDiasTempMayor15+=1
        temperaturasMayor15.append(temperatura)
    if temperatura<10:
        numDiasTempMenor10+=1
        temperaturasMenor10.append(temperatura)

print("Número de días con temperatura mayor a 15ºC:", numDiasTempMayor15)
print("Número de días con temperatura menor a 10ºC:", numDiasTempMenor10)

print("Temperaturas superiores a 15ºC:", temperaturasMayor15)
print("Temperaturas inferiores a 10ºC:", temperaturasMenor10)

# Ejercicio 6

boolTemperaturasMinSup0 = all(temperatura>0 for temperatura in temperaturasMinimas)
boolTemperaturasMaxSup0 = all(temperatura>0 for temperatura in temperaturasMaximas)
boolTemperaturasMedSup0 = all(temperatura>0 for temperatura in temperaturasMedias)
boolTemperaturasSup0 = boolTemperaturasMinSup0&boolTemperaturasMaxSup0&boolTemperaturasMedSup0
if boolTemperaturasMaxSup0:
    print("Todas las temperaturas son mayores que 0")