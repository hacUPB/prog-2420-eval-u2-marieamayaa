# Problema 1
## Análisis
[Análisis](https://www.canva.com/design/DAGPVQEeh_8/F5SzCVhVqq-KLxCGnzGquA/edit?utm_content=DAGPVQEeh_8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) 
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
# Problema 2
## Análisis
[Análisis](https://www.canva.com/design/DAGPb3NKrg0/nCDSEGZ5hhvOO5kJ0lquUw/edit?utm_content=DAGPb3NKrg0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
## Pseudocódigo
```
Inicio
    Leer altitud_actual
    Leer coeficiente_arrastre
    Leer altitud_minima
    Leer perdida_minima
    Definir cont= 0
    Definir altitud_perdida = 0
    Definir altitud_ini=0

    Mientras
        altitud_actual > altitud_minima 
        altitud_perdida > perdida_minima
        contador_orbitas == 0 
        Hacer
        contador_orbitas = contador_orbitas + 1
        altitud_perdida = coeficiente_arrastre * altitud_actual
        altitud_ini = altitud_actual - altitud_perdida
        coeficiente_arrastre = coeficiente_arrastre + 0.0001
        Si
             altitud_perdida <= perdida_minima 
            Imprimir "El satélite se ha estabilizado en órbita."
            Imprimir "Altitud final: " + altitud_actual
            Imprimir "Número de órbitas completadas: " + contador_orbitas
            Simo
                Imprimir "El satélite ha reingresado en la atmósfera terrestre."
                Imprimir "Número total de órbitas completadas: " + contador_orbitas
            Fin sino
        Fin si
    Fin mientras
Fin
```




