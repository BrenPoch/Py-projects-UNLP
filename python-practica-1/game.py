from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]

# Cantidad de cuentas a resolver
times = 5

# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

# Se inicializan los contadores de respuestas correctas e incorrectas
correct_counter = 0
incorrect_counter = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(1, 10)     # Para evitar un ZeroDivisionError, modifico randrange() excluyendo el cero.
    operator = choice(operators)

    # Se imprime la cuenta.
    print(f"\n{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))

    # Se evalua si el resultado del usuario fue correcto o incorrecto
    match operator:
        case "+":
            correct_result = number_1 + number_2
        case "-":
            correct_result = number_1 - number_2
        case "*":
            correct_result = number_1 * number_2
        case "/":
            correct_result = number_1 / number_2
    
    if result == correct_result:
        print("El resultado es correcto")
        correct_counter += 1
    else:
        print("El resultado es incorrecto")
        incorrect_counter += 1
    
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()

# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos ese tiempo en segundos.
print(f"\nTardaste {total_time.seconds} segundos.")

# Se informa la cantidad de respuestas correctas e incorrectas
print(f"\nCantidad de respuestas correctas: {correct_counter}")
print(f"Cantidad de respuestas incorrectas: {incorrect_counter}")