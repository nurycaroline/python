# Declaracao de funcao

def sum(a,b):
	return a + b
c = sum(1, 3)

print c

# ---------------------------------------------------
def salario_descontato_imposto(salario, imposto=27.):
	return salario - (salario * (imposto * 0.01))

print salario_descontato_imposto(5000)
print salario_descontato_imposto(5000, 0.10)
