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
		listap = BuscarPorTipo(tipo,fichero)
		print("Los Pokemon de ese tipo son: ")
		for b in listap:
			print(b,",",end="")
		print()
		opcion=Menu()		

