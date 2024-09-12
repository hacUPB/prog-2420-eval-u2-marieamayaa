# Información del usuario
título =input ('Ingrese su título (sr o sra):')
nombre = input('Ingrese su nombre y apellido:')
print(f'¡Bienvenido a Fast Airlines {título} {nombre}!')

# Selección de vuelo
import datetime

semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado","domingo"]
hoy= datetime.datetime.now()

fecha = input("Ingrese la fecha del viaje en formato dd/mm/aaaa ")
fecha_sis = datetime.datetime.strptime(fecha, "%d/%m/%Y")

dia= fecha_sis.weekday()
m= 240
n=461
p=657
i = 'semana'
j= 'fin de semana'

origen =input('Ingrese su ciudad de origen (Bogota, Medellin, Cartagena):').lower()
destino =input('Ingrese su ciudad de destino(Bogota, Medellin, Cartagena):').lower()
if origen == 'bogotá' and destino == 'medellin' or origen == 'medellin' and destino == 'bogota':
    distancia = m
elif origen =='medellin' and destino =='cartagena' or origen == 'cartagena' and destino =='medellin':
    distancia = n
else:
    distancia = p


if fecha_sis.weekday():
    dia= i
else:
    dia = j

if distancia < 400 and dia == i:
    precio = 79900
elif distancia < 400 and dia == j:
    precio = 119900
elif distancia > 400 and dia == i:
    precio = 156900
else:
    precio= 213000

# Asignación de asiento
from random import randint 

ubicación=input('Tiene preferencia de asiento(ventana, pasillo, sin preferencia):').lower()
if ubicación=='ventana':
    ubi='a'
elif ubicación=='pasillo':
    ubi='c'
else:
    ubi='b'

núm_asiento = randint(1,29)


# salida
print(f'nombre completo:{nombre}')
print(f'origen:{origen.capitalize()}')
print(f'destino:{destino.capitalize()}')
print(f'fecha:{fecha_sis.date()}')
print(f'precio del boleto:{precio}')
print(f'asiento: {núm_asiento} {ubi}')

