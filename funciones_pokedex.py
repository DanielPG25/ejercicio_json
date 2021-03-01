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

def Ranking(fichero):
	lista=SumarEstadisticas(fichero)
	primeroe = 0
	segundoe = 0
	terceroe = 0
	cuartoe = 0
	quintoe = 0
	sextoe = 0
	septimoe = 0
	octavoe = 0
	novenoe = 0
	decimoe = 0
	primeron = "a"
	segundon = "b"
	terceron = "c"
	cuarton = "d"
	quinton = "e"
	sexton = "f"
	septimon = "g"
	octavon = "h"
	novenon = "i"
	decimon = "j"
	for posicion in lista:
		if posicion.get("stats") > primeroe:
			segundoe = primeroe
			primeroe = posicion.get("stats")  
			segundon = primeron
			primeron = posicion.get("nombre")
		elif posicion.get("stats") > segundoe and posicion.get("stats") <= primeroe:
			terceroe = segundoe
			segundoe = posicion.get("stats")  
			terceron = segundon
			segundon = posicion.get("nombre")
		elif posicion.get("stats") > terceroe and posicion.get("stats") <= segundoe:
			cuartoe = terceroe
			terceroe = posicion.get("stats")  
			cuarton = terceron
			terceron = posicion.get("nombre")
		elif posicion.get("stats") > cuartoe and posicion.get("stats") <= terceroe:
			quintoe = cuartoe
			cuartoe = posicion.get("stats")  
			quinton = cuarton
			cuarton = posicion.get("nombre")
		elif posicion.get("stats") >	quintoe and posicion.get("stats") <= cuartoe:
			sextoe = quintoe
			quintoe = posicion.get("stats")
			sexton = quinton
			quinton = posicion.get("nombre")
		elif posicion.get("stats") > sextoe and posicion.get("stats") <= quintoe:
			septimoe = sextoe
			sextoe = posicion.get("stats")
			septimon = sexton
			sexton = posicion.get("nombre")
		elif posicion.get("stats") > septimoe and posicion.get("stats") <= sextoe:
			octavoe = septimoe
			septimoe = posicion.get("stats")
			octavon = septimon
			septimon = posicion.get("nombre")
		elif posicion.get("stats") > octavoe and posicion.get("stats") <= septimoe:
			novenoe = octavoe
			octavoe = posicion.get("stats")
			novenon = octavon
			octavon = posicion.get("nombre")
		elif posicion.get("stats") > novenoe and posicion.get("stats") <= octavoe:
			decimoe = novenoe
			novenoe = posicion.get("stats")
			decimon = novenon
			novenon = posicion.get("nombre")
		elif posicion.get("stats") > decimoe and posicion.get("stats") <= novenoe:
			decimoe = posicion.get("stats")
			decimon = posicion.get("nombre")
	nombres=[]
	estadisticas=[]
	nombres.extend([primeron,segundon,terceron,cuarton,quinton,sexton,septimon,octavon,novenon,decimon])
	estadisticas.extend([primeroe,segundoe,terceroe,cuartoe,quintoe,sextoe,septimoe,octavoe,novenoe,decimoe])
	return nombres,estadisticas

def ContarTipos(tipo,fichero):
	acum = 0									
	for b in fichero:
		if tipo in b.get("type"):
			acum=acum+1
	return acum		