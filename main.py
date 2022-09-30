from source.Grafo import *
from source.File import *

gf = Grafo()
f = File()
nodos = [30,100,500]

f.toScript('Malla_'+str(30)+'.gv',gf.grafoMalla(6,5))
f.toScript('Malla_'+str(100)+'.gv',gf.grafoMalla(10,10))
f.toScript('Malla_'+str(500)+'.gv',gf.grafoMalla(25,20))

for tam in nodos:

	f.toScript('ErdosRenyi_'+str(tam)+'.gv',gf.grafoErdosRenyi(tam,tam*8))
	
	f.toScript('Gilbert_'+str(tam)+'.gv',gf.grafoGilbert(tam,0.35))
	
	f.toScript('Geografico_'+str(tam)+'.gv',gf.grafoGeografico(tam,0.35))

	f.toScript('DorogovtsevMendes_'+str(tam)+'.gv',gf.grafoDorogovtsevMendes(tam))
	
	f.toScript('BarabasiAlbert_'+str(tam)+'.gv',gf.grafoBarabasiAlbert(tam,3))