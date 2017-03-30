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
                    (Nodo_nario('ac',[Nodo_nario('act',[Nodo_nario('acto',[Nodo_nario('actor')])]),Nodo_nario('acu',[Nodo_nario('acus',[Nodo_nario('acuso')])]),Nodo_nario('aci',[Nodo_nario('acil',[Nodo_nario('acilo')])])])),
                    (Nodo_nario('ad',[Nodo_nario('ado',[Nodo_nario('adob',[Nodo_nario('adobe'),Nodo_nario('adobo')]),Nodo_nario('ador',[Nodo_nario('adoro')])])]))])
e = Nodo_nario('e',[(Nodo_nario('eb',[Nodo_nario('ebr',[Nodo_nario('ebri',[Nodo_nario('ebrio')])]),Nodo_nario('eba',[Nodo_nario('eban',[Nodo_nario('ebano')])])])),
                    (Nodo_nario('ec',[Nodo_nario('ech',[Nodo_nario('echa',[Nodo_nario('echar'),Nodo_nario('echad')]),Nodo_nario('eche',[Nodo_nario('echen')])])])),
                    (Nodo_nario('ed',[Nodo_nario('edi',[Nodo_nario('edit',[Nodo_nario('edito')])]),Nodo_nario('edu',[Nodo_nario('educ',[Nodo_nario('educa')])])]))])
i = Nodo_nario('i',[(Nodo_nario('id',[Nodo_nario('ide',[Nodo_nario('idea',[Nodo_nario('ideal')])]),Nodo_nario('ido',[Nodo_nario('idol',[Nodo_nario('idolo')])])])),
                    (Nodo_nario('il',[Nodo_nario('ilu',[Nodo_nario('ilus',[Nodo_nario('iluso'),Nodo_nario('ilusa')]),Nodo_nario('ilud',[Nodo_nario('ilude')])])])),
                    (Nodo_nario('in',[Nodo_nario('inf',[Nodo_nario('infl',[Nodo_nario('inflo')])]),Nodo_nario('ing',[Nodo_nario('ingl',[Nodo_nario('ingle')])]),Nodo_nario('inp',[Nodo_nario('inpu',[Nodo_nario('input')])])]))])
o = Nodo_nario('o',[(Nodo_nario('ob',[Nodo_nario('obe',[Nodo_nario('obes',[Nodo_nario('obeso')])]),Nodo_nario('obl',[Nodo_nario('oble',[Nodo_nario('oblea')])])])),
                    (Nodo_nario('oi',[Nodo_nario('oir',[Nodo_nario('oira',[Nodo_nario('oiran'),Nodo_nario('oiras')]),Nodo_nario('oirl',[Nodo_nario('oirlo')])])])),
                    (Nodo_nario('oj',[Nodo_nario('oja',[Nodo_nario('ojal',[Nodo_nario('ojala')])]),Nodo_nario('oje',[Nodo_nario('ojea',[Nodo_nario('ojear')])]),Nodo_nario('oji',[Nodo_nario('ojit',[Nodo_nario('ojito')])])]))])
u = Nodo_nario('u',[(Nodo_nario('ub',[Nodo_nario('ubi',[Nodo_nario('ubic',[Nodo_nario('ubica')])])])),
                    (Nodo_nario('un',[Nodo_nario('uni',[Nodo_nario('unic',[Nodo_nario('unica'),Nodo_nario('unico')]),Nodo_nario('unid',[Nodo_nario('unido')])])])),
                    (Nodo_nario('ur',[Nodo_nario('ura',[Nodo_nario('uran',[Nodo_nario('urano')])]),Nodo_nario('urg',[Nodo_nario('urgi',[Nodo_nario('urgia')])]),Nodo_nario('urn',[Nodo_nario('urna',[Nodo_nario('urnas')])])]))])

print("Posibles palabras")
print(buscarvalor(a,"a",0))
