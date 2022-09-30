from source.Nodo import *
from source.Arista import *

class Grafo:

	def __init__(self):
		self.Nodo = Nodo(0)		
		self.Arista = Arista();
	
	def grafoMalla(self,m,n, dirigido = False):
		self.Nodo.creaNodosXY(m,n)
		
		for _id in self.Nodo.getIds():
			n0 = self.Nodo.getNodo(_id)

			if((n0.get_i() + 1) < m):
				n1 = self.Nodo.getVecino(n0,1,0)
				self.Arista.setArista(n0,n1)
			
			if((n0.get_j() + 1) < n):
				n2 = self.Nodo.getVecino(n0,0,1)
				self.Arista.setArista(n0,n2)

		return self.getGraphivzText()


	def grafoErdosRenyi(self,n, m, dirigido=False, auto=False):
		if(m >= n-1):
			self.Nodo.creaNodos(n)
			i = 0
			while(i < m):
				n1 = self.Nodo.getRandomNodo()
				n2 = self.Nodo.getRandomNodo()
				if(n1.getId() != n2.getId()):
					if(not (self.Arista.isParalela(n1.getId(),n2.getId()) 
						or self.Arista.isParalela(n2.getId(),n1.getId()))):
						self.Arista.setArista(n1,n2)
						i +=1

			return self.getGraphivzText()
		else:
			return "-1"

	def grafoGilbert(self,n, p, dirigido=False, auto=False):
		self.Nodo.creaNodos(n)	

		for _id in range(n):
			for _id2 in range(n):
				if(_id != _id2):
					if(not self.Arista.isParalela(_id,_id2)):
						if(self.Nodo.ganaVolado(p)):
							n1 = self.Nodo.getNodo(_id)
							n2 = self.Nodo.getNodo(_id2)
							self.Arista.setArista(n1,n2)
		return self.getGraphivzText()

	def grafoGeografico(self,n, r, dirigido=False, auto=False):
		self.Nodo.creaNodosUnitario(n)
		for _id in range(n):
			for _id2 in range(n):
				if(_id != _id2):
					if(not self.Arista.isParalela(_id,_id2)):
						n1 = self.Nodo.getNodo(_id)
						n2 = self.Nodo.getNodo(_id2)
						if(self.Nodo.isCerca(n1,n2,r)):
							self.Arista.setArista(n1,n2)

		return self.getGraphivzText()

	def grafoDorogovtsevMendes(self,n, dirigido=False):
		if(n >=3):
			self.Nodo.creaNodos(3)
			self.Arista.setArista(self.Nodo.getNodo(0),self.Nodo.getNodo(1))
			self.Arista.setArista(self.Nodo.getNodo(1),self.Nodo.getNodo(2))
			self.Arista.setArista(self.Nodo.getNodo(0),self.Nodo.getNodo(2))
			id_nodo = 3
			while(id_nodo < n):
				n0 = self.Nodo.addNodo(id_nodo)
				arista = self.Arista.getRandomArista();
				n1 = self.Nodo.getNodo(arista.getIdNodo_A())
				n2 = self.Nodo.getNodo(arista.getIdNodo_B())
				self.Arista.setArista(n0,n1)
				self.Arista.setArista(n0,n2)
				id_nodo += 1
			
		return self.getGraphivzText()

	def grafoBarabasiAlbert(self,n, d, dirigido=False, auto=False):
		self.Nodo.creaNodos(d)
		self.Arista.inicializaGrado(n)
		self.Arista.generaAristasNodos(self.Nodo.getNodos())
		id_nodo = d

		while(id_nodo < n):
			n0 = self.Nodo.addNodo(id_nodo)
			for nodo in self.Nodo.getNodos():
				if(n0.getId() != nodo.getId()):
					if(self.Nodo.volado(self.Arista.probabilidadGrado(nodo,d))):
						self.Arista.setArista(n0,nodo)
			id_nodo += 1
		return self.getGraphivzText()


	


	def getGraphivzText(self):
		header = "graph {\n"
		nodos = self.Nodo.toStringIds()
		aristas =""
		cierre = "}"

		for _id in self.Arista.getIds():
			 _arista = self.Arista.getAristas(_id)
			 
			 if(not isinstance(_arista,int) and len(_arista)>1):
			 	for id_arista in _arista:
			 		aristas += "\t"+str(_id)+" -- " + str(id_arista) + ";\n"
			 else:
			 	if(_arista):
		 			aristas += "\t"+str(_id)+" -- " + str(_arista) + ";\n"
		self.Nodo.limpiaBuffer()
		self.Arista.limpiaBuffer()
		return header + nodos + aristas + cierre

	
