import json
import sys

def leer_json(fichero):
	try:
		with open(fichero) as f:
			datos=json.load(f)
		return(datos)
	except:
		print("Error al leer el fichero")
		sys.exit(0)

def Menu():
	print("1. Top 10 Pokemon")
	print("2. Contar tipos de Pokemon")
	print("3. Buscar Pokemon por nombre")
	print("4. Buscar Pokemon por tipo")
	print("5. Combate")
	print("6. Salir")
	opcion = int(input("Dime que opción eliges: "))
	return opcion

def SumarEstadisticas(fichero):
	lista=[]
	for a in fichero:
		nombrebase = {}
		nombrebase["nombre"] = a.get("name").get("english")
		nombrebase["stats"] = (a.get("base").get("HP")) + (a.get("base").get("Attack")) + (a.get("base").get("Defense")) + (a.get("base").get("Sp. Attack")) + (a.get("base").get("Sp. Defense")) + (a.get("base").get("Speed"))
		lista.append(nombrebase)
	return lista	