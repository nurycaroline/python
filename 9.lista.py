#listas

print [1,2,3,4,5]
print ["salario", "imposto"]
print [1, "salario"]
print [[1,2,3], "salario", 10]

# ---------------------------------------------------

lista = ["salario", "imposto", "altos", "baixos"]
print lista[0]
print lista[-1]
print lista[2:4]

# ---------------------------------------------------

lista[2] = "ALTOS"
lista[3] = "BAIXOS"
print lista
lista[0:2] = ["IMPOSTOS", "SALARIOS"]
print lista

# ---------------------------------------------------
lista = []

if lista:
	print "nunca sou executado"
else:
	print "sempre sou executado"