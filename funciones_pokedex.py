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
	print("1. Estadística de un equipo")
	print("2. Nombres de equipos")
	print("3. Clasificación de la liga")
	print("4. Quiniela por fecha")
	print("5. Salir")
	opcion = int(input("Dime que opción eliges: "))
	return opcion
