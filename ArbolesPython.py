class Nodo():
    def __init__(self, valor, izq = None, der = None):.
        self.valor= valor
        self.izquierda = izq
        self.derecha=der
        
def inorden(arbol):
    if arbol==None:
        return ""
    else:
        return inorden(arbol.izquierda)+arbol.valor+inorden(arbol.derecha)

def buscar (arbol, valor):
    if arbol== None:
        return False
    elif arbol.valor==valor:
        return True
    else:
        return buscar(arbol.izquierda,valor)+buscar (arbol.derecha,valor)

def evaluar(arbol):
    if arbol.valor=='+'
        return evaluar(arbol.izquierda)+ evaluar(arbol.derecha)
    elif arbol.valor=='-'
        return evaluar(arbol.izquierda)- evaluar(arbol.derecha)
    elif arbol.valor=='*'
        return evaluar(arbol.izquierda)* evaluar(arbol.derecha)
    elif arbol.valor=='/'
        return evaluar(arbol.izquierda)/ evaluar(arbol.derecha)
    else:
        return int(arbol.valor)


