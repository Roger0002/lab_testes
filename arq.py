import sys

lista = sys.argv

print("Lista bonita")
print(lista)

lista_final = []

for l in lista:
	for i in l:
		aaa = lista_final.append(i)

print(lista_final)
