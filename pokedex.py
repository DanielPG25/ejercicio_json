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
