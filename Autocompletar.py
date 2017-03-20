class Nodo_nario():
    def __init__(self, valor,hijos = [] ):
        self.valor= valor
        self.hijos= hijos

def mandarHijos(arbol, hijo):
    if len(arbol.hijos) == hijo + 1 :
        return mandarHijos(arbol.hijos[hijo],0)
    elif len(arbol.hijos) == 0:
        return [arbol.valor]
    else:
        return mandarHijos(arbol.hijos[hijo],0)+mandarHijos(arbol,hijo+1)

def buscarvalor(arbol, valor, hijo):
    if arbol.valor==valor:
        return mandarHijos(arbol,0)
    else:
        if len(arbol.hijos) == hijo + 1 :
            return buscarvalor(arbol.hijos[hijo],valor,0)
        elif len(arbol.hijos) == 0:
            return []
        else:
            return buscarvalor(arbol.hijos[hijo],valor,0)+buscarvalor(arbol,valor,hijo+1)


a = Nodo_nario('a',[(Nodo_nario('ab',[Nodo_nario('aba',[Nodo_nario('aban',[Nodo_nario('abano')])]),Nodo_nario('abo',[Nodo_nario('abof',[Nodo_nario('abofe')])])])),
               (Nodo_nario('ac',[Nodo_nario('act',[Nodo_nario('acto',[Nodo_nario('actor')])]),Nodo_nario('acu',[Nodo_nario('acus',[Nodo_nario('acuso'),Nodo_nario('acusa')])]),Nodo_nario('aci',[Nodo_nario('acil',[Nodo_nario('acilo')])])]))])

b= Nodo_nario('a',[Nodo_nario('am',[Nodo_nario('amo',[Nodo_nario('amor'),Nodo_nario('amoc'),Nodo_nario('amol')])
                                    ,Nodo_nario('ama'),Nodo_nario('ame')])
                   ,Nodo_nario('ab')])

print("Posibles palabras")
print(buscarvalor(a,"a",0))
