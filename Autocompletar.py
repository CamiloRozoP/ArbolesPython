class Nodo_nario():
    def __init__(self, valor,hijos = [] ):
        self.valor= valor
        self.hijos= hijos

def autocompletar(arbol):
    if arbol == None:
        return []
    else:
        return mandarHijos(arbol,0)+mandarHijos(arbol.hijos[0],0)

def mandarHijos(arbol,hijo):
    if len(arbol.hijos) == hijo+1:
        return [ultimo(arbol.hijos[hijo])]
    else:
        return [ultimo(arbol.hijos[hijo])] + mandarHijos(arbol,hijo+1)
        """mandarHijos(arbol.hijos[hijo],hijo)"""

def ultimo(arbol):
    if arbol.hijos == []:
        return arbol.valor
    else:
        return ultimo(arbol.hijos[0])

a = Nodo_nario('a',[(Nodo_nario('ab',[Nodo_nario('aba',[Nodo_nario('aban',[Nodo_nario('abano')])]),Nodo_nario('abo',[Nodo_nario('abof',[Nodo_nario('abofe')])])])),
               (Nodo_nario('ac',[Nodo_nario('act',[Nodo_nario('acto',[Nodo_nario('actor')])]),Nodo_nario('acu',[Nodo_nario('acus',[Nodo_nario('acuso')])]),Nodo_nario('aci',[Nodo_nario('acil',[Nodo_nario('acilo')])])]))])

b= Nodo_nario('a',[Nodo_nario('am'),Nodo_nario('ab')])

print(autocompletar(a))
