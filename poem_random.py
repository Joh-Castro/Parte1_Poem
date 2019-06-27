from random import randrange
misPronombres=["my","your","his","her"]
misPreposiciones=["above","across","against","along","among","around","before","behind","beneath","beside","between","beyond","during","inside","onto","outside","under","underneath","upon","with","without","through"]
misSustantivos=["heart","sun","moon","thunder","fire","time","wind","sea","river","flavor","wave","willow","rain","tree","flower","field","meadow","pasture","harvest","water","father","mother","brother ","sister"]
misAdjetivos=["black","white","dark","light","bright","murky","muddy","clear"]
misVerbos=["runs","walks","stands","climbs","crawls","flows","flies","transcends","ascends","descends","sinks"]


def Linea():
	#LINE: <NOUN> OR <PREPOSITION> OR <PRONOUN>  
	Azar=randrange(3)
	if Azar==0:
		resultadoLinea= Sustantivo()
	elif Azar==1:
		resultadoLinea= Preposicion() 
	else:
		resultadoLinea= Pronombre() 

	return resultadoLinea

##########################

def Sustantivo():
	Azar2=randrange(2)
	#son 23 sustantivos
	if Azar2==0:
		resultadoSustantivo= misSustantivos[randrange(22)] + " " + misVerbos[randrange(10)]  + "."
	else:
		resultadoSustantivo= misSustantivos[randrange(22)] + " " + misPreposiciones[randrange(21)] + "." 
	
	return resultadoSustantivo

def Pronombre():
	Azar3=randrange(2)
	#son 4 pronombres
	if Azar3==0:
		resultadoPronombre= misPronombres[randrange(3)] + " " + Sustantivo()  + " " 
	else:
		resultadoPronombre= misPronombres[randrange(3)] + " " + Adjetivos()  + " " 
	
	return resultadoPronombre

def Preposicion():
	Azar4=randrange(3)
	#son 22 preposiciones
	if Azar4==0:
		resultadoPreposicion= misPreposiciones[randrange(21)] + " " + Sustantivo()  + " " 
	elif Azar4==1:
		resultadoPreposicion= misPreposiciones[randrange(21)] + " " + Pronombre()  + " " 
	else:
		resultadoPreposicion= misPreposiciones[randrange(21)] + " " + Adjetivos()  + " "
	
	return resultadoPreposicion

##########################

def Verbo():
	Azar5=randrange(2)
	#son 11 verbos
	if Azar5==0:
		resultadoVerbo= misVerbos[randrange(10)] + " " + misPreposiciones[randrange(21)] + "."
	else:
		resultadoVerbo= misVerbos[randrange(10)] + " " + misPronombres[randrange(3)] + "."

	return resultadoVerbo

def Adjetivos():
	Azar6= randrange(2)
	#son 8 adjetivos
	if Azar6==0:
		resultadoAdjetivos= misAdjetivos[randrange(7)] + " " + misSustantivos[randrange(22)] + "."
	else:
		resultadoAdjetivos= misAdjetivos[randrange(7)] + " " + misAdjetivos[randrange(7)] + "."
	
	return resultadoAdjetivos

##########################
print("Su Poema random es (Test1):")
print("-------------------")
for x in range(1,6):
	# LINE BREAAK, Cada Iteracion es una Linea
	print(Linea())
print("-------------------")
print("Realizado por: Joh-Castro.")