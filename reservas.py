# Información del usuario
título =input ('Ingrese su título (sr o sra):')
nombre = input('Ingrese su nombre y apellido:')
print(f'¡Bienvenido a Fast Airlines {título} {nombre}!')

# Selección de vuelo
m= 240
n=461
p=657
i = 'semana'
j= 'fin de semana'

origen =input('Ingrese su ciudad de origen (Bogota, Medellin, Cartagena):').lower()
destino =input('Inngrese su ciudad de destino(Bogota, Medellin, Cartagena):').lower()
día_sem =input('Ingrese el día de la semana en el que desea viajar (lunes a domingo):').lower()
día_mes=input('Ingrese el día del mes en el que desea viajar (1 a 30):')

if origen == 'bogotá' and destino == 'medellin' or origen == 'medellin' and destino == 'bogota':
    distancia = m
elif origen =='medellin' and destino =='cartagena' or origen == 'cartagena' and destino =='medellin':
    distancia = n
else:
    distancia = p


if día_sem == 'lunes' or día_sem== 'martes' or día_sem== 'miercoles' or día_sem=='jueves':
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
print(f'origen:{origen}')
print(f'destino:{destino}')
print(f'fecha de vuelo:{día_sem} {día_mes}')
print(f'precio del boleto:{precio}')
print(f'asiento: {núm_asiento} {ubi}')

