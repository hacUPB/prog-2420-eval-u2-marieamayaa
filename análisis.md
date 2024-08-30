# Problema 1
## Análisis
![Análisis](Reservas.jpg) 
## Pseudocódigo
``` 
Inicio
    Leer titulo 
    Leer nombre
    Imprimir titulo + " " + nombre + " ", ¡Bienvenido a FastFast Airlines!"
    Leer origen 
    Leer destino 
    Leer dia_semana
    Leer dia_mes
    Definir distancia
    Definir costo

    Si
        origen == "Medellín" Y destino == "Bogotá"
        O origen == "Bogotá" Y destino == "Medellín" 
        Entonces
        distancia = 240
        Sino 
            Si 
            origen == "Medellín" Y destino == "Cartagena"
            O origen == "Cartagena" Y destino == "Medellín" 
            Entonces
            distancia = 461
            Sino
                Si
                 origen == "Bogotá" Y destino == "Cartagena" 
                 O origen == "Cartagena" Y destino == "Bogotá" 
                 Entonces
                distancia = 657
                Fin Si
            Fin Si
        Fin Si
    Fin Si

    Si
        distancia<400
        Entonces
        dia_semana=="lunes", "martes","miercoles", "jueves"
        costo= 79.900
        dia_semana="viernes", "sabado", "domingo"
        costo= 119.900
        Sino
            dia_semana=="lunes","martes","miercoles","jueves"
            costo= 156.900
            dia_semana=="viernes","sabado", "domingo"
            costo=213.000
        Fin Sino
    Fin Si 

    Imprimir"¿Prefiere un asiento en el pasillo, junto a la ventana, o no tiene preferencia? (pasillo/ventana/ninguno):"
    Leer preferencia_asiento

    Si 
        preferencia_asiento == "pasillo" 
        Entonces
        asiento_letra = "C"
        Sino
            Si
            preferencia_asiento == "ventana" 
            Entonces
            asiento_letra = "A"
            Sino
            asiento_letra = "B"
        Fin Si
    Fin si

    asiento_numero = random.randint(1, 29)
    asiento_asignado = asiento_numero + asiento_letra

    Imprimir "Nombre completo: " + titulo + " " + nombre + " " + origen+""+destino+""+dia_semana+""+dia_mes+""+costo""+asiento_asignado+""
Fin
```



