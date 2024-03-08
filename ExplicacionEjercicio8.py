

# Definición de la función simular_inversion que toma cuatro parámetros:
# monto_inicial: la cantidad de dinero con la que se comienza la inversión
# monto_mensual: la cantidad de dinero que se añade a la inversión cada mes
# objetivo: el monto que se quiere alcanzar con la inversión
# tasa_interes: la tasa de interés mensual
def simular_inversion(monto_inicial, monto_mensual, objetivo, tasa_interes):
    meses = 0  # Variable para llevar el conteo de los meses
    monto_actual = monto_inicial  # Establece el monto actual como el monto inicial
    while monto_actual < objetivo:  # Ejecuta el bucle mientras el monto actual sea menor que el objetivo
        meses += 1  # Incrementa el contador de meses en 1
        monto_actual *= (1 + tasa_interes)  # Calcula el nuevo monto actual considerando la tasa de interés
        monto_actual += monto_mensual  # Agrega el monto mensual a la inversión
        # Imprime el monto actual formateado con dos decimales
        print(f"Mes {meses}: ${monto_actual:.2f}")
    # Retorna la cantidad de meses necesarios y el monto final alcanzado
    return meses, monto_actual

# Definición de las variables para la inversión
monto_inicial = 100
monto_mensual = 5
objetivo = 1000
tasa_interes = 0.15  # Representa una tasa de interés mensual del 15%

# Imprime información sobre la inversión
print(f"Inversión inicial: ${monto_inicial}")
print(f"Aportes mensuales: ${monto_mensual}")
print(f"Objetivo: ${objetivo}")
print(f"Tasa de interés mensual: {tasa_interes * 100}%\n")

# Llama a la función simular_inversion con los parámetros establecidos
meses_necesarios, monto_final = simular_inversion(monto_inicial, monto_mensual, objetivo, tasa_interes)

# Imprime el resultado de la simulación
print(f"\nSe necesitan {meses_necesarios} meses para alcanzar un monto acumulado de ${monto_final:.2f}.")
