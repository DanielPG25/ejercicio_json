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