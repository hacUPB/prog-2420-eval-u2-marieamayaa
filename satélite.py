altitud_ini=int(input('Ingrese la altitud inicial del satélite (Km):'))
coeficiente_arrastre=float(input('Ingrese el coeficiente de arrastre inicial(por ejemplo, 0.01):'))
altitud_min=int(input('Ingrese la altitud mínima de seguridad antes que el satélite se desintegre(Km):'))
altitud_actual = altitud_ini
orbitas_completadas = 0
while altitud_actual > altitud_min:
    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual -= altitud_perdida
    coeficiente_arrastre += 0.0001
    orbitas_completadas += 1
if altitud_actual <= altitud_min:
    print(f'El satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.')
    print(f'Número total de órbitas completadas: {orbitas_completadas}')

    



