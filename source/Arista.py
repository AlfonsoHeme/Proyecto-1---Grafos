from source.Nodo import *
import random

class Arista:

	__aristas={}
	__grados=[]
	__nodo_A = 0
	__nodo_B = 0

	def __init__(self):
		print("")

	def setArista(self,nodo_A,nodo_B):
		if(not isinstance(nodo_B,Nodo) ):
			self.__aristas[nodo_A.getId()] = ""
		elif(nodo_A.getId() in self.__aristas):
			self.__aristas[nodo_A.getId()] += ","+str(nodo_B.getId())
		else:
			self.__aristas[nodo_A.getId()] = str(nodo_B.getId())

		self.incrementaGrado(nodo_A.getId())
		self.incrementaGrado(nodo_B.getId())
	
	def inicializaGrado(self, n):
		self.__grados = [0 for _ in range(n)]

	def incrementaGrado(self, _id):
		if(len(self.__grados) > 0):
			if(isinstance(_id,int)):
				self.__grados[_id] += 1

	def probabilidadGrado(self,nodo,d):
		return 1-(self.getGrado(nodo)/d)

	def printAristas(self):
		print(self.__aristas)

	def getAristas(self):
		return self.__aristas;

	def getIds(self):
		return self.__aristas.keys()

	def limpiaBuffer(self):
		self.__aristas.clear()
		self.__grados.clear()
		self.__nodo_A = 0
		self.__nodo_B = 0

	def getAristas(self,key):
		if("," in self.__aristas[key]):
			return self.__aristas[key].split(sep =',')
		return int(self.__aristas[key])

	def getRandomArista(self):
		pos = 0
		self.__nodo_A = random.choice(list(self.getIds()))
		if("," in self.__aristas[self.__nodo_A]):
			pos =  random.randint(0,len(self.__aristas[self.__nodo_A].split(sep =',')))
		self.__nodo_B = int(self.__aristas[self.__nodo_A].split(sep =',')[pos-1])
	
		return self

	def generaAristasNodos(self, nodos):
		for nodoA in nodos:
			for nodoB in nodos:
				if(nodoA.getId() != nodoB.getId()):
					if(not self.isParalela(nodoA.getId(),nodoB.getId())):
						self.setArista(nodoA,nodoB)


	def getGrado(self, nodo):
		return self.__grados[nodo.getId()]

	def printGrados(self):
		print(self.__grados)

	def getIdNodo_A(self):
		return self.__nodo_A

	def getIdNodo_B(self):
		return self.__nodo_B

	def isParalela(self,id_A, id_B):
		if(id_B in list(self.getIds())):
			if("," in self.__aristas[id_B]):
				return (str(id_A) in self.__aristas[id_B].split(sep =','))
			else:
				return (self.__aristas[id_B] == str(id_A))
		return False 
