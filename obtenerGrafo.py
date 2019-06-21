# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:09:18 2019

@author: mrincon
"""
# import the necessary packages
# import argparse
# import cv2
from os import path, listdir
# import csv
from numpy import array, sqrt, where, arange, zeros, vstack
# from copy import deepcopy


# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
listaTrazos = []
trazo = []
itDibujo = 0           # < ---------------------   CAMBIAR PARA EMPEZAR POR OTRA DIBUJO



zoom = 1
MAX_DIST_MISMO_PUNTO = 6

clavesDibujo = ["CASA","CUBO","CIRCULO","CRUZ","CUADRADO","TRIANGULO","PICO","MINIMENTAL","MUELLE","REY"]
claveAnotacion = ["REF", "GRAFO1", "DOBLELINEA", "CONEXIONPASA"]
claveGrafo = "GRAFO"


dibujoAct = clavesDibujo[9]
signoAct = claveAnotacion[1]



PATH_BASE = "TEST/"
dibujosWorkingDirectory = PATH_BASE +"3_DIBUJOS/" + dibujoAct + "/"
dibujosExtension = "jpg"

signosWorkingDirectory = PATH_BASE + "3_ANOTACIONES/" + dibujoAct  + "/"
anotacion_Extension = "_" + signoAct +  ".txt"
anotacion_GRAFO = "_" + signoAct + "_"+ claveGrafo + ".txt"


comentario = ""

# if not(os.path.exists(signosWorkingDirectory)):
# 	os.mkdir(signosWorkingDirectory)


# ************************************************************************************************

def list_files(directory, extension):
	
    return (f for f in listdir(directory) if f.endswith('.' + extension))


def saveLIST(mylist, fileName):
	#data = [0,1,2,3,4,5]
	with open(fileName, "w") as file:
		   file.write(str(mylist))
def loadLIST(fileName):	
	if path.exists(fileName):
		with open(fileName, "r") as file:
			return(eval(file.readline()))
	else:
		return([])


def escalarTrazos(listaTrazos, zoom):	
	if len(listaTrazos) == 0:
		return()
	listaTrazosNew = listaTrazos.copy()
	for itTrazo in range(len(listaTrazos)):
		for itPunto in range(len(listaTrazos[itTrazo])):
			listaTrazos[itTrazo][itPunto] = (round(listaTrazos[itTrazo][itPunto][0]*zoom), round(listaTrazos[itTrazo][itPunto][1]*zoom))
	return(listaTrazosNew)


def distE(punto, listaPuntos):
	# punto y listaPuntos son dos numpy array [x,y] y [ [x0,y0], ...,[xn,yn]]
	if len(punto)==0 or len(listaPuntos)==0:
		return (array([-1]))
	dif0 = listaPuntos[:,0]-punto[0]
	dif1 = listaPuntos[:,1]-punto[1]
	return(sqrt(dif0**2+dif1**2))
	

def indMismoPunto(p2d, listap2d, MAXDIST,NUMPUNTOS):
	D = distE(p2d,listap2d)
	if D[0]==-1:
		return(array([-1]))
		
	indSame = array( where(D.ravel() <= MAXDIST ))
	#if len(indSame):
	if indSame.shape[1]:
		if NUMPUNTOS:
			return(indSame[0])
		else:
			return(indSame)
	else:
		return(array([-1]))

def puntosANumpy(listaPuntos):
	listaNew = arange(2*len(listaPuntos)).reshape(len(listaPuntos),2)
	print(listaPuntos)
	for it in range(len(listaPuntos)):
		print(it)
		listaNew[it,:] = array([listaPuntos[it][0],listaPuntos[it][1]])
		print(listaNew)
	return(listaNew)


def agruparNodos(listaTrazos, MINDIST):
	listaTrazosNew = listaTrazos.copy()
	listaPuntos = [item for sublist in listaTrazosNew for item in sublist]  # list comprehension:    para cada sublista de la lista, coger los items de la sublista

	diccNodos= agruparPuntosProximos(listaPuntos, MINDIST)
	# con list comprehension se crean listas con todos los elementos al mismo nivel.
	# si se quiere mantener la estructura hay que usar bucles for
	#listaTrazos2 = [listaNodos[item] for sublist in listaTrazos for item in sublist]
	#listaPuntos = [item for sublist in listaTrazos for item in sublist]  # list comprehension:    para cada sublista de la lista, coger los items de la sublista
	# Reasignar estructura de tramos
	for itT in range(len(listaTrazosNew)):
		for itP in range(len(listaTrazosNew[itT])):
			listaTrazosNew[itT][itP] = diccNodos[tuple(listaTrazosNew[itT][itP])]
	for itT in range(len(listaTrazosNew)):
		for itP in range(1,len(listaTrazosNew[itT])):
			listaTrazosNew[itT][itP] = diccNodos[tuple(listaTrazosNew[itT][itP])]
	return(listaTrazosNew)

def agruparPuntosProximos(listaPuntos, MINDIST):
	if len(listaPuntos)==0:
		return({})
	listanpPuntos = array(listaPuntos)
	# calcular distancias para sacar vecinos
	agrup = [0 for x in range(len(listanpPuntos))]
	for itP in range(len(listanpPuntos)):
		D = distE(listanpPuntos[itP], listanpPuntos)
		indSame = array( where(D.ravel() <= MINDIST ))
		agrup[itP] = set(indSame[0].tolist())

	#generar grupos: se va analizando si un grupo tiene intersección con otro (se utilizan conjuntos - sets)
	# si un comjunto intersecta con otro, lo absorve. Se reinicia el proceso.
	# esto sigue hasta que no hay más absorciones
	grupos = []
	gruposAct = agrup.copy()
	gAct= 0
	while(1):
		cambio = 0
		for itG in range(gAct+1,len(gruposAct)):
			if gruposAct[gAct] & gruposAct[itG]:
				gruposAct[gAct] = gruposAct[gAct] | gruposAct[itG]
				gruposActAux = [ gruposAct[0:itG] , gruposAct[itG+1:]] 
				gruposAct = [item for sublist in gruposActAux for item in sublist]
				cambio = 1
				break
		if cambio==0:
			gAct +=1
			if gAct > len(gruposAct)-1:
				break
	
	# se asigna la coordendaa del primero a todos los demás del mismo grupo
	listaNodos = {}
	for itG in range(len(gruposAct)):
		P = [items for items in gruposAct[itG]]
		puntoSel = listaPuntos[P[0]]
		for itP in gruposAct[itG]:
			listaNodos.update({(listaPuntos[itP][0],listaPuntos[itP][1]): puntoSel })
	return(listaNodos)


def obtenerGrafo(listaTrazos, MAX_DIST_MISMO_PUNTO):
	#listaTrazos = [[[1,0], [0,0],[0,1],[1,1], [2,1]],   [[1,0], [1,1], [1,2]]]
	# obtener puntos, cambiando los muy próximos al mismo punto
	# crear un diccionario para relacionar los nodos con sus coordenadas
	# poner los enlaces entre nodos siguiendo los tramos
	#listaTrazos


	listaTrazosNew = agruparNodos(listaTrazos, MAX_DIST_MISMO_PUNTO)

	listaNodos = {}
	listaArcos = []
	contNodos = 0
	# Definir diccionario para los nodos: 
	#	key = tyupla de sus coordenadas (x,y)
	#	valor = indice del nodo (contador)
	#Para los arcos puede asignarse un array en el que se vayan añadiendo los enlaces entre nodos.
	#	Los nodos se referencian por su índice
	#	Array Nx2: nodo origen - nodo destino (enlaces no direccionales)

	
	for itTramo in listaTrazosNew:
		listaPuntosAct = puntosANumpy(itTramo)   # solo se admitirán dos puntos muy juntos si están en el mismo tramo.

		# El primer tramo mete todos sus puntos y sus arcos, y en los siguientes tramos ya se tiene en cuenta los puntos/nodos que se han metido
		if listaNodos=={}:
			# meter todos los nodos y todos los arcos
			# añadir nodo 0
			contNodos = contNodos+1   # equivale a contNodos += 1
			listaNodos.update({(listaPuntosAct[0,0],listaPuntosAct[0,1]): contNodos })
			nodoPrev = listaNodos[(listaPuntosAct[0,0],listaPuntosAct[0,1])]
			
			# añadir resto de nodos y el arco con el anterior
			for itP in range(1,len(listaPuntosAct)):	
				nuevaPosNodo = (listaPuntosAct[itP,0],listaPuntosAct[itP,1])
				
				aux = listaNodos.get(nuevaPosNodo, -1)
				if  aux == -1:
					#print(itP)
					contNodos = contNodos+1   # equivale a contNodos += 1
					# añadir al diccionario de nodos
					listaNodos.update({(listaPuntosAct[itP,0],listaPuntosAct[itP,1]): contNodos })   
					# añadir arco
					listaArcos.append([listaNodos.get((listaPuntosAct[itP-1,0],listaPuntosAct[itP-1,1])), listaNodos.get(nuevaPosNodo)])
					#nodoPrev = listaNodos.get((listaPuntosAct[itP,0],listaPuntosAct[itP,1]))
					#print(listaNodos)
					#print(listaArcos)
	
				elif  nodoPrev != aux:
					listaArcos.append([ nodoPrev , aux])
				
				
				
				nodoPrev = listaNodos.get(nuevaPosNodo, -1)
				
				print(listaNodos)
				print(listaArcos)
				
	
	
	
		else:
			#print(listaNodos)
			#print(listaArcos)
			#print(listaPuntosAct)
			# posNodos contendrá un np array con las posiciones x,y de los nodos
			posNodos = array([])
			for itNodo in listaNodos.keys():
				if len(posNodos)==0:
					posNodos = array([itNodo[0],itNodo[1]])
				else:
					posNodos = vstack((posNodos,array([itNodo[0],itNodo[1]])))

			# Buscar si los nodos nuevos corresponden con alguno previo (distancia<MAX_DIST_MISMO_PUNTO)
			coincidenciasPuntos=zeros(listaPuntosAct.shape[0])
			for itP in range(listaPuntosAct.shape[0]):
				coincidenciasPuntos[itP] = indMismoPunto(listaPuntosAct[itP,:], posNodos, MAX_DIST_MISMO_PUNTO, 1)

			# Caso especial del primer nodo del tramo. Meterlo si no está próximo oa otro nodo previo	
			if coincidenciasPuntos[0]==-1:
				contNodos = contNodos+1   # equivale a contNodos += 1
				listaNodos.update({(listaPuntosAct[0,0],listaPuntosAct[0,1]): contNodos })   # añadir al diccionario
				nodoPrev = listaNodos.get((listaPuntosAct[0,0],listaPuntosAct[0,1]))   # coger valor desde el diccionario
				#puntoPrevExiste=0
			else:
				#puntoPrevExiste=1
				nodoPrev = listaNodos.get( (int(posNodos[int(coincidenciasPuntos[0]),0]),int(posNodos[int(coincidenciasPuntos[0]),1])))
	
			#procedimiento para los nodos del 2 al N del tramo
			for itP in range(1,len(listaPuntosAct)):
				#print(itP)
				# añadir nodo si no está ya.
				if coincidenciasPuntos[itP]==-1:

					nuevaPosNodo = (listaPuntosAct[itP,0],listaPuntosAct[itP,1])
					aux = listaNodos.get(nuevaPosNodo, -1)
					if  aux == -1:
						#puntoActExiste=0
						contNodos = contNodos+1   # equivale a contNodos += 1
						listaNodos.update({ nuevaPosNodo : contNodos})
						nodoAct = listaNodos.get( (listaPuntosAct[itP,0],listaPuntosAct[itP,1]) )
					else:
						nodoAct = aux

				else:
					#puntoActExiste=1
					nodoAct = listaNodos.get( (int(posNodos[int(coincidenciasPuntos[itP]),0]),int(posNodos[int(coincidenciasPuntos[itP]),1])) )	

				if nodoPrev != nodoAct:
					listaArcos.append([nodoPrev, nodoAct])
				nodoPrev = nodoAct
				#print(listaNodos)
				#print(listaArcos)
	print("----------- resultado final  ----------")
	
	print(listaNodos)
	print(listaArcos)
	return(listaNodos, listaArcos)

def salvarGrafo(listaNodos, listaArcos, fichero):	
	f = open(fichero, "w")
	f.write( "NODOS:\n")
	for key, val in listaNodos.items():
		f.write(str(val) + " - "+ str(key) + "\n")
	f.write( "\n")
	f.write( "\nARCOS:\n")
	for val in listaArcos:
		f.write( str(val[0]) + " - " + str(val[1]) + "\n")
	f.close()
