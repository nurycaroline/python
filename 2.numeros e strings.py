print 3+2 	#soma
print 3 * 4.2 #multiplicacao
print 4/2 	#divisao
print 5//2 	#divisao descartando fracao
print 5%2 	#divisao resto
print -4 	#negacao
print 10 ** 2 #potencia

# ---------------------------------------------------
print ("""\
Teste : bla bla
	bla bla 		bla bla
  bla bla 		bla bla
""")

# ---------------------------------------------------
st = "maracana"
print st[0]   	# primeiro caracter
print st[1:4] 	# primeiro ao 4 caracter
print st[2:] 	# a partir do 2 caracter
print st[:2]	# os 2 primeiros caracteres
print len(st)	# quantidade de caracters

# ---------------------------------------------------
print "m" in st		# True
print "x" not in st # True
print "m" + "aracana" # maracana
print "a" * 3

# ---------------------------------------------------
str = "python 3"
print str[0:7] + "2"
print str.replace("3", "2")

# ---------------------------------------------------
print st.capitalize() 	# primeira maiusculo
print st.count("a") 	# quantidade de aparicoes
print st.startswith("m") # inicia com .. ?
print st.endswith("z") 	# termina com .. ?
print "copa de 2014".split(" ")	# criacao de array
print " ".join(["Copa", "de", "2014"])	# Une arrays com " "
print "copa de 2014".replace("2014", "2018") # troca caracteres

# ---------------------------------------------------
print "%d  dias para a copa" % (99 +1)
print "{} dias para a copa".format(100)
print "{dias} dias para a copa".format(dias=100)
# ---------------------------------------------------
print '{:<60}'.format('alinhado a esquerda, ocupando 60 posicoes')
print '{:>60}'.format('alinhado a direita, ocupando 60 posicoes')
print '{:^60}'.format('centralizado, ocupando 60 posicoes')
print '{:.^80}'.format('centralizando ao alterar caracter, ocupando 80 posicoes')
