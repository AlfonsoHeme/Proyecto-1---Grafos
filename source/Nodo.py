import random 
import math

class Nodo:
	__id_nodo = 0
	__nodeName = ""
	__i = 0
	__j =0
	__nodos={}
	__strNodo = ""

	def __init__(self,id_nodo,i = 0,j = 0):
		self.__id_nodo = id_nodo
		self.__nodeName = str(i) + "." + str(j)
		self.__i = i
		self.__j = j

	def get_i(self):
		return self.__i

	def get_j(self):
		return self.__j

	def get_idNodo(self):
		return self.__id_nodo

	def getId(self):
		return self.__id_nodo

	def getKey(self,nodo,i=0, j=0):
		return str(nodo.get_i()+i)+"."+str(nodo.get_j()+j)

	def getIds(self):
		return self.__nodos.keys()

	def getNodo(self,key):
		return self.__nodos[key]

	def addNodo(self, id_nodo):
		self.__nodos[id_nodo]  = Nodo(id_nodo)
		self.setToString(id_nodo)
		return self.__nodos[id_nodo]

	def getVecino(self,nodo,i,j):
		return self.__nodos[self.getKey(nodo,i,j)];

	def ganaVolado(self,probabilidad):
		return random.random() >= probabilidad

	def volado(self,probabilidad):
		return random.random() <= probabilidad

	def getCoordenadas(self):
		coordenadas = [get_i(),get_j()]
		return coordenadas

	def getNodos(self):
		return self.__nodos.values()

	def limpiaBuffer(self):
		self.__nodos.clear()
		self.__id_nodo = 0
		self.__nodeName = ""
		self.__i = 0
		self.__j =0
		self.__nodos={}
		self.__strNodo = ""

	def isCerca(self,nodo_a, nodo_b, r):
		d = math.sqrt((nodo_a.get_i()-nodo_b.get_i())**2+(nodo_a.get_j()-nodo_b.get_j())**2)
		#print(str(d)+ " - "+ str(r) + " : " +str(d<=r))
		return d<=r


	#Genera m * n nodos de coordenada con key m.n
	def creaNodosXY(self,m,n):
		self.__i = m
		self.__j = n
		nodo = 0;
		i = 0;
		j = 0;
	
		while(nodo < m*n):
			if(j < n and i < m):
				self.__nodos[str(i) + "." + str(j)] = (Nodo(nodo,i,j))
				self.setToString(nodo)
				j += 1
				nodo +=1;
			else:
				j = 0;
				i += 1

	#Genera nodos con posicion 0 < i, j < 1
	def creaNodosUnitario(self,n):
		for id_nodo in range(n):	
			self.__nodos[id_nodo] = (Nodo(id_nodo,random.random(),random.random()))
			self.setToString(id_nodo)

	#Genera nodos y su key es el Id del Nodo
	def creaNodos(self,m):
		for nodo in range(m):	
			self.__nodos[nodo] = (Nodo(nodo))
			self.setToString(nodo)
	
	#Regresa un nodo aleatorio 
	def getRandomNodo(self):
		r = random.choice(list(self.getIds()))
		return self.__nodos[r]
	
	def setToString(self,idNodo):
		self.__strNodo += str("\t"+str(idNodo)+" [label = "+str(idNodo)+"]\n")

	def toStringIds(self):
		return self.__strNodo