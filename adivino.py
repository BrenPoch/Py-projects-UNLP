## Adivina adivinador...
import random
numero_aleatorio = random.randrange(101)          ## Utilizo como argumento de la función el número 101 para generar numeros entre 0 y 100, inclusive.
gane = False       

print("Tenés 5 intentos para adivinar un número entre 0 y 100.")
intento = 1

while intento < 6 and not gane:
    numero_ingresado = int(input('Ingresa tu número: '))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! Y necesitaste {} intentos!'.format(intento))
        gane = True
    else:
        print('Mmm... No... ese número no es... Seguí intentando.\n')
        intento += 1
if not gane:
    print('Perdiste :(\nEl número era: {}\n'.format(numero_aleatorio))
