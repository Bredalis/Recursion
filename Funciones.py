
from time import perf_counter

# Funciones Recursivas

def recursiva(numero):
	print("Recursiva:\n")

	if numero == 0:
		print(numero)

	else:
		print(numero)
		recursiva(numero - 1)

def factorizacion_recursiva(numero):
	print("\nFactorizacion recursiva: \n")

	if numero == 0 or numero == 1:
		return 1

	return numero * factorizacion_recursiva(numero - 1)

# Funcion Iterativa

def factorizacion_iteractiva(numero):
	print("\nFactorizacion Iteractiva: \n")

	if numero == 0 or numero == 1:
		print(1)

	resultado = 1

	for i in range(2, numero + 1):		
		resultado *= i

	return resultado

inicio = perf_counter()

for i in range(10):
	print(i, factorizacion_iteractiva(i), factorizacion_recursiva(i))
	recursiva(i)

final = perf_counter()

print("Tiempo:", "%0.4f" % (final - inicio))