""" Haremos 1 ejercicio completo con cicho while """

import random

print("Adivina el número secreto entre 1 y 20.")
print("Gana el que termine con menos puntos. \n 💡 Algunos números dan 2 puntos, otros 3, y el resto 1 punto si fallas.")

rangomin = 1
rangomax = 20

numero_secreto = random.randint(rangomin, rangomax)

intentos_maximos = 5
intentos = 0
puntos = 0
adivinanza = None

Castigo2 = {random.randint(rangomin, rangomax) for _ in range(3)}
Castigo3 = {random.randint(rangomin, rangomax) for _ in range(2)}

Castigo2.discard(numero_secreto)
Castigo3.discard(numero_secreto)

print(f"Tienes {intentos_maximos} intentos para adivinar un número entre {rangomin} y {rangomax}.")
print("Recuerda que fallar da 1 punto, adicional habran números que dan 2 puntos y otros 3.")

while adivinanza != numero_secreto and intentos < intentos_maximos:
    entrada = input(f"Intento {intentos + 1}: Escribe un número: ")
    
    if not entrada.isdigit():
        print("⚠ Por favor escribe solo números.")
        continue
    
    adivinanza = int(entrada)
    intentos += 1
    
    if adivinanza == numero_secreto:
        print(f"✅ ¡Felicidades! Adivinaste en {intentos} intentos con {puntos} puntos.")
        break
    else:
        if adivinanza in Castigo3:
            puntos += 3
            print("💥 ¡Oh no! Este número tiene penalización de 3 puntos.")
        elif adivinanza in Castigo2:
            puntos += 2
            print("⚠ Este número tiene penalización de 2 puntos.")
        else:
            puntos += 1
            print("➖ Este error suma 1 punto.")
        
        if adivinanza < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

if adivinanza != numero_secreto:
    print(f"No lograste adivinar. El número secreto era {numero_secreto}.")
print(f"🏆 Puntuación final: {puntos} puntos (menos es mejor)")
