"""Creación de ejercicio libre"""

# Calculadora de gastos mensuales

print(" Calculadora de gastos mensuales ")
print("---------------------------------")

# EL CLIENTE INGRESARA EL VALOR O SU INGRESO MENSUAL 

ingreso = float(input("Ingrese el valor del ingreso mensual: ")) #Esta linea de codigo se realiza para el ingreso en consola del cliente

# Ingresar el nombre del gasto ejemplo: Ropa, comida, juegos, etc...

gastos = {}  # En esta linea de codigo usare un dicionario para almacenar las categorias y esto es igual Valor

while True:
    categoria = input("Ingrese el nombre del gasto (o escriba 'fin' para terminar): ").strip().lower()
    if categoria == "fin":
        break
    valor = float(input(f"Ingrese el valor para '{categoria}': "))
    gastos[categoria] = valor


# Luego de lo anterior vamos a calcular el total

total_gastos = sum(gastos.values())

# Luego vamos a calcular el saldo restante

saldo =  ingreso - total_gastos

# Ahora si viene lo bueno jajaja, calcular el porcenta de los gastos

if ingreso > 0:
    porcentaje_gasto = (total_gastos/ ingreso) * 100
else:
    porcentaje_gasto = 0

# Mostrar resultado
print("\n Resumen mensual:")
print("--------------------")
for categoria, valor in gastos.items():
    print(f"- {categoria}: ${valor:.2f}")
print(f"\n Total de ingresos: ${ingreso:.2f}")
print(f" Total de gastos: ${total_gastos:.2f}")
print(f" Porcentaje de gasto: {porcentaje_gasto:.2f}%")
print(f" Saldo restante: ${saldo:.2f}")


# 7. Mensajes de motivación y advertencia
if saldo > 0:
    print(" Buen trabajo, estás ahorrando.")
elif saldo == 0:
    print(" Estás justo, no queda dinero para ahorrar.")
else:
    print(" Estás en números rojos, cuidado con tus gastos.")