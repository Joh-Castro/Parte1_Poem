from random import randrange
mis_pronombres = ("my","your","his","her")
mis_preposiciones = ("above","across","against","along","among",
                    "around","before","behind","beneath","beside",
                    "between","beyond","during","inside","onto",
                    "outside","under","underneath","upon","with",
                    "without","through")
mis_sustantivos = ("heart","sun","moon","thunder","fire","time",
                  "wind","sea","river","flavor","wave","willow",
                  "rain","tree","flower","field","meadow","pasture",
                  "harvest","water","father","mother","brother","sister")
mis_adjetivos = ("black","white","dark","light","bright","murky","muddy","clear")
mis_verbos = ("runs","walks","stands","climbs","crawls","flows","flies",
	         "transcends","ascends","descends","sinks")

def linea():
	#LINE: <NOUN> OR <PREPOSITION> OR <PRONOUN>  
	Azar = randrange(3)
	if Azar == 0:
		resultado_linea = sustantivo()
	elif Azar == 1:
		resultado_linea = preposicion() 
	else:
		resultado_linea = pronombre() 

	return resultado_linea

##########################

def sustantivo():
	#NOUN: Lista de Sustantivos <VERB> OR <PREPOSITION> OR $END 
	Azar2 = randrange(3)
	if Azar2 == 0:
		resultado_sustantivo = mis_sustantivos[randrange(len(mis_sustantivos))] + " " + verbo() 
	elif Azar2 == 1:
		resultado_sustantivo = mis_sustantivos[randrange(len(mis_sustantivos))] + " " + preposicion() 
	else:
		resultado_sustantivo = mis_sustantivos[randrange(len(mis_sustantivos))] #$END
	
	return resultado_sustantivo

def pronombre():
	#PRONOUN: Lista de Pronombres <NOUN> OR <ADJECTIVE> 
	Azar3 = randrange(2)
	if Azar3 == 0:
		resultado_pronombre = mis_pronombres[randrange(len(mis_pronombres))] + " " + sustantivo() 
	else:
		resultado_pronombre = mis_pronombres[randrange(len(mis_pronombres))] + " " + adjetivo() 
	
	return resultado_pronombre

def preposicion():
	#PREPOSITION: Lista de Preposiciones <NOUN> OR <PRONOUN> OR <ADJECTIVE> 
	Azar4 = randrange(3)
	if Azar4 == 0:
		resultado_preposicion = mis_preposiciones[randrange(len(mis_preposiciones))] + " " + sustantivo() 
	elif Azar4 == 1:
		resultado_preposicion = mis_preposiciones[randrange(len(mis_preposiciones))] + " " + pronombre() 
	else:
		resultado_preposicion = mis_preposiciones[randrange(len(mis_preposiciones))] + " " + adjetivo() 
	
	return resultado_preposicion

##########################

def verbo():
	#VERB: Lista de Verbos <PREPOSITION> OR <PRONOUN> OR $END 
	Azar5 = randrange(3)
	if Azar5 == 0:
		resultado_verbo = mis_verbos[randrange(len(mis_verbos))] + " " + preposicion() 
	elif Azar5 == 1:
		resultado_verbo = mis_verbos[randrange(len(mis_verbos))] + " " + pronombre() 
	else:
		resultado_verbo = mis_verbos[randrange(len(mis_verbos))] #$END


	return resultado_verbo

def adjetivo():
	#ADJECTIVE: Lista de Adjetivos <NOUN> OR <ADJECTIVE> OR $END 
	Azar6 = randrange(3)
	if Azar6 == 0:
		resultado_adjetivo = mis_adjetivos[randrange(len(mis_adjetivos))] + " " + sustantivo() 
	elif Azar6 == 1:
		resultado_adjetivo = mis_adjetivos[randrange(len(mis_adjetivos))] + " " + adjetivo() 
	else:
		resultado_adjetivo = mis_adjetivos[randrange(len(mis_adjetivos))] #$END
	
	return resultado_adjetivo

##########################

print("Su Poema random es (Test1):")
print("-------------------")
for x in range(1,6):
	#POEM: <LINE> <LINE> <LINE> <LINE> <LINE> 
	print(linea())
	#$LINEBREAK, Cada Iteracion es una Linea del Poema
print("-------------------")
print("Realizado por: Joh-Castro.")