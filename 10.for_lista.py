# For Lista

lista = ["mei", "simples"]

# ---------------------------------------------------
for l in lista:
	print l

# ---------------------------------------------------
for l in lista:
	if l.startswith("s"):
		print "inicia com s: " + l

# ---------------------------------------------------		
for l in lista:
	if l.startswith("s"):		
		continue
	else: 
		print "nao inicia com s: " + l
		
# ---------------------------------------------------
for i in range(5):
	print i

# ---------------------------------------------------
for i, l in enumerate(lista):
	print i,l