class Nodo():
    def __init__(self, valor, izq = None, der = None):
        self.valor= valor
        self.izquierda = izq
        self.derecha=der
        
def inorden(arbol):
    if arbol==None:
        return ""
    else:
        return inorden(arbol.izquierda)+arbol.valor+inorden(arbol.derecha)

def posorden(arbol):
    if arbol==None:
        return ""
    else:
        return posorden(arbol.izquierda)+posorden(arbol.derecha)+arbol.valor

def buscar (arbol, valor):
    if arbol== None:
        return False
    elif arbol.valor==valor:
        return True
    else:
        return buscar(arbol.izquierda,valor)+buscar (arbol.derecha,valor)

def buscarBinario (arbol, valor):
    if arbol==None:
        return False
    if arbol.valor== valor:
        return True
    elif arbol.valor<valor:
        return buscar(arbol.izquierda,valor)
    elif arbol.valor>valor:
        return buscar(arbol.derecha,valor)

def evaluar(arbol):
    if arbol.valor=='+':
        return evaluar(arbol.izquierda)+ evaluar(arbol.derecha)
    elif arbol.valor=='-':
        return evaluar(arbol.izquierda)- evaluar(arbol.derecha)
    elif arbol.valor=='*':
        return evaluar(arbol.izquierda)* evaluar(arbol.derecha)
    elif arbol.valor=='/':
        return evaluar(arbol.izquierda)/ evaluar(arbol.derecha)
    else:
        return int(arbol.valor)

def insertar(arbol,valor):
    if arbol == None:
        return Nodo(valor)
    if int(arbol.valor) > int(valor):
        return Nodo(arbol.valor,insertar(arbol.izquierda, valor),arbol.derecha)
    else:
        return Nodo(arbol.valor,arbol.izquierda,insertar(arbol.derecha, valor)) 

a = Nodo('10',Nodo('5'),Nodo('20',Nodo('15'),Nodo('25')))
print(inorden(insertar(a,'50')))

   

