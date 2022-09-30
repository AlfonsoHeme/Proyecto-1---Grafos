import os
class File:

	dir_name = 'Grafos/'

	def toScript(self,nombreFichero,datos):
		if not os.path.exists(self.dir_name):
			os.mkdir(self.dir_name)
		with open(self.dir_name+nombreFichero, 'w') as f:
			f.write(datos)


	