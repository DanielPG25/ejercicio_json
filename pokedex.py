from funciones_pokedex import *

fichero=leer_json("pokedex.json")
opcion=Menu()
print()
while opcion<1 or opcion>6: 
	print("Error. Esa opción no es válida")
	print()
	opcion=Menu()
while opcion != 6:
	if opcion == 1:
		print("El ranking de los 10 mejores pokemon es: ")
		nombres,estadisticas = Ranking(fichero)
		for a,b,c in zip(nombres,estadisticas,range(1,11)):
			print(f"En la posición {c} está {a} con una suma de {b} puntos entre todas las estadisticas")
		print()
		opcion=Menu()
		print()
	if opcion == 2:
		print("Los tipos son los siguientes: Normal, Fire, Water, Grass, Electric, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dark, Dragon, Steel, Fairy")
		print()
		tipo = input("Elige uno de los mencionados anteriormente: ")
		numero = ContarTipos(tipo,fichero)
		print(f"El número de pokemon de ese tipo es {numero}")
		print()
		opcion=Menu()		
	if opcion == 3:
		cadena = input("Dime la cadena por la que quieres buscar (la primera en mayúscula): ")
		print()
		nombres=BuscarNombre(cadena,fichero)
		lista = SumarEstadisticas(fichero)
		print("Los Pokemon que empiezan por esa cadena son: ")
		for a in nombres:
			for b in lista:
				if b.get("nombre") == a:
					print(f"El pokemon {b.get('nombre')} tiene una suma de {b.get('stats')} puntos entre todas las estadísticas")
		print()
		opcion=Menu()
		print()	
	if opcion == 4:
		print("Los tipos son los siguientes: Normal, Fire, Water, Grass, Electric, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dark, Dragon, Steel, Fairy")
		print()
		tipo = input("Elige uno de los mencionados anteriormente: ")
		print()
		listap = BuscarPorTipo(tipo,fichero)
		print("Los Pokemon de ese tipo son: ")
		for b in listap:
			print(b,",",end="")
		print()
		opcion=Menu()		
	if opcion == 5:
		print("En esta opción deberas aportar el nombre de dos pokemon, por que puede ayudar si antes usas la opción 3 o 4")	
		print()
		pok1 = input("Dime el nombre del primer Pokemon (la primera en mayúscula): ")
		pok2 = input("Dime el nombre del segundo Pokemon (la primera en mayúscula): ")
		print()
		nombre1=BuscarNombre(pok1,fichero)
		nombre2=BuscarNombre(pok2,fichero)
		lista= SumarEstadisticas(fichero)
		try:
			for a in lista:
				if a.get("nombre") == nombre1[0]:
					stats1=a.get("stats")
				if a.get("nombre") == nombre2[0]:
					stats2=a.get("stats")
		except:
			print("Algún pokemon no existe")
			sys.exit(0)				
		listapok1 = AlmacenarEstadisticas(pok1,fichero)
		listapok2 = AlmacenarEstadisticas(pok2,fichero)	
		if stats1 > stats2:
			print(f"El pokemon {nombre1[0]} es más fuerte que el pokemon {nombre2[0]}")
			for a,b,c in zip(listapok1,listapok2,range(len(listapok1))):
				if a > b and c == 0:
					print(f"La vida de {pok1} es mayor que la de {pok2}")
				elif a > b and c == 1:
					print(f"El ataque físico de {pok1} es mayor que el de {pok2}")
				elif a > b and c == 2:
					print(f"La defensa física de {pok1} es mayor que la de {pok2}")
				elif a > b and c == 3:
					print(f"El ataque especial de {pok1} es mayor que el de {pok2}")
				elif a > b and c == 4:
					print(f"La defensa especial de {pok1} es mayor que la de {pok2}")
				elif a > b and c == 5:
					print(f"La velocidad de {pok1} es mayor que la de {pok2}")			 	
		elif stats1 < stats2:
			print(f"El pokemon {nombre2[0]} es más fuerte que el pokemon {nombre1[0]}")
			for a,b,c in zip(listapok1,listapok2,range(len(listapok1))):
				if b > a and c == 0:
					print(f"La vida de {pok2} es mayor que la de {pok1}")
				elif b > a and c == 1:
					print(f"El ataque físico de {pok2} es mayor que el de {pok1}")
				elif b > a and c == 2:
					print(f"La defensa física de {pok2} es mayor que la de {pok1}")
				elif b > a and c == 3:
					print(f"El ataque especial de {pok2} es mayor que el de {pok1}")
				elif b > a and c == 4:
					print(f"La defensa especial de {pok2} es mayor que la de {pok1}")
				elif b > a and c == 5:
					print(f"La velocidad de {pok2} es mayor que la de {pok1}")
		elif stats1 == stats2:
			print("Es un empate")				
		print()
		opcion=Menu()				

print("Programa finalizado")