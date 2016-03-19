# loops com while

salario = int(input('Salario? '))
imposto = 27.

while imposto > 0.:
	imposto = float(input('imposto ou 0 para sair: '))
	if not imposto: 
		imposto = 27.
	elif imposto == '0':
		break
	else:
		imposto = float(imposto)
	print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))