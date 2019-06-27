from random import randrange
misPronombres = ("my","your","his","her")
misPreposiciones = ("above","across","against","along","among",
                    "around","before","behind","beneath","beside",
                    "between","beyond","during","inside","onto",
                    "outside","under","underneath","upon","with",
                    "without","through")
misSustantivos = ("heart","sun","moon","thunder","fire","time",
                  "wind","sea","river","flavor","wave","willow",
                  "rain","tree","flower","field","meadow","pasture",
                  "harvest","water","father","mother","brother ","sister")
misAdjetivos = ("black","white","dark","light","bright","murky","muddy","clear")
misVerbos = ("runs","walks","stands","climbs","crawls","flows","flies",
	         "transcends","ascends","descends","sinks")

def Linea():
	#LINE: <NOUN> OR <PREPOSITION> OR <PRONOUN>  
	Azar = randrange(3)
	if Azar == 0:
		resultadoLinea = Sustantivo()
	elif Azar == 1:
		resultadoLinea = Preposicion() 
	else:
		resultadoLinea = Pronombre() 

	return resultadoLinea

##########################

def Sustantivo():
	Azar2 = randrange(2)
	if Azar2 == 0:
		resultadoSustantivo = misSustantivos[randrange(len(misSustantivos))] + " " + misVerbos[randrange(len(misVerbos))]  
	else:
		resultadoSustantivo = misSustantivos[randrange(len(misSustantivos))] + " " + misPreposiciones[randrange(len(misPreposiciones))] 
	
	return resultadoSustantivo

def Pronombre():
	Azar3 = randrange(2)
	if Azar3 == 0:
		resultadoPronombre = misPronombres[randrange(len(misPronombres))] + " " + Sustantivo()  + " " 
	else:
		resultadoPronombre = misPronombres[randrange(len(misPronombres))] + " " + Adjetivos()  + " " 
	
	return resultadoPronombre

def Preposicion():
	Azar4 = randrange(3)
	if Azar4 == 0:
		resultadoPreposicion = misPreposiciones[randrange(len(misPreposiciones))] + " " + Sustantivo()  + " " 
	elif Azar4 == 1:
		resultadoPreposicion = misPreposiciones[randrange(len(misPreposiciones))] + " " + Pronombre()  + " " 
	else:
		resultadoPreposicion = misPreposiciones[randrange(len(misPreposiciones))] + " " + Adjetivos()  + " "
	
	return resultadoPreposicion

##########################

def Verbo():
	Azar5 = randrange(2)
	if Azar5 == 0:
		resultadoVerbo = misVerbos[randrange(len(misVerbos))] + " " + misPreposiciones[randrange(len(misPreposiciones))] 
	else:
		resultadoVerbo = misVerbos[randrange(len(misVerbos))] + " " + misPronombres[randrange(len(misPronombres))] 

	return resultadoVerbo

def Adjetivos():
	Azar6 = randrange(2)
	if Azar6 == 0:
		resultadoAdjetivos = misAdjetivos[randrange(len(misAdjetivos))] + " " + misSustantivos[randrange(len(misSustantivos))] 
	else:
		resultadoAdjetivos = misAdjetivos[randrange(len(misAdjetivos))] + " " + misAdjetivos[randrange(len(misAdjetivos))] 
	
	return resultadoAdjetivos

##########################

print("Su Poema random es (Test1):")
print("-------------------")
for x in range(1,6):
	# LINE BREAAK, Cada Iteracion es una Linea del Poema
	print(Linea())
print("-------------------")
print("Realizado por: Joh-Castro.")