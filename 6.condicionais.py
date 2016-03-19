# condicionais

salario = int(input('Salario?'))
imposto = input('Imposto?')

if imposto == '':  # not imposto
	imposto = 27.5
else:
	imposto = float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

if imposto < 10:
	print "medio"
elif imposto < 27.5:
	print "alto"
else:
	print "muito alto"
	
situacao_imposto = "alto" if imposto > 0.27 else "baixo"  # if ternario
print situacao_imposto

print "alto" if imposto > 0.27 else "baixo"  # if ternario


