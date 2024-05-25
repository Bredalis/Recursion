
# Busqueda del dato
# Manera Iterativa

lista = [11, 12, 13, 14, 15, 16, 17]

def busqueda_iterativa(lista, dato):

	bajo = 0
	alto = len(lista) - 1
	centro = (bajo + alto) // 2

	while bajo <= alto:

		if lista[centro] == dato:
			return centro

		elif lista[centro] < dato:
			bajo = centro + 1

		else:
			alto = centro - 1

		centro = (bajo + alto) // 2

	return -1

# Manera Recursiva

def busqueda_recursiva(lista, bajo, alto, dato):

	if bajo > alto:
		return -1

	centro = (bajo + alto) // 2

	if lista[centro] == dato:
		return centro

	elif lista[centro] < dato:
		return busqueda_recursiva(lista, centro + 1, alto, dato)

	else:
		return busqueda_recursiva(lista, bajo, centro - 1, dato)

for i in range(10, 19):

	print(f"Iterativa: {i} _ {busqueda_iterativa(lista, i)}")
	print(f"Recursiva: {i} _ {busqueda_recursiva(lista, 0, len(lista) - 1, i)}")