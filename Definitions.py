class Agente:
    
    def _init_(self, identifier = None):
        self.identificador = identifier
    
    def clonar(self):
        pass
    
    def replicar(self):
        pass
        
    def combinar(self):
        pass

    def solicitar(self):
        pass
    
    def responder(self):
        pass
        
    def operar(self):
        pass


class Nodo:
    
    def _init_(self, identifier = None):
        self.identificador = identifier
        self.agente = set()


class Red:
    
    def _init_(self, identifier = None):
        self.identificador = identifier
        self.nodos = set() 
        self.agentes = set()
        self.conexiones = set()  # conjunto de tuplas binarias: ('id1','id2') 
                                    # cada una contiene los identificadores de los dos nodos que hacen el link


# Método que crea una red, un nodo sobre una red, 
# un agente en una red o una conexión entre dos nodos; par1 = identificador del objeto
def crear(par1, par2 = None, par3 = None):
    
    # Si el parámetro 1 es un entero y los otros dos no se pasaron,
    # entonces se crea una red.
    if ((type(par1) == type(int)) and (par2 == par3 == None)):
        return Red(par1)
    
    # Si el parámetro 2 es una red y el parámetro 3 no se pasó,
    # entonces se crea un nodo con el parámetro 1 como identificador.
    elif ((type(par1) == type(int)) and (type(par2) == type(Red())) and 
          (par3 == None)):
        par2.nodos.add(Nodo(par1))
    
    # Si el parámetro 1 es una red y los otros 2 son nodos,
    # entonces se crea un link entre estos.
    elif ((type(par1) == type(Red())) and (type(par2) == type(par3) == type(Nodo()))):
        par1.conexiones.add((par2.identificador, par3.identificador))
        
    # Si el parámetro 1 es un entero, el parámetro 2 una red y
    # el parámetro 3 no se especifica, entonces se crea un agente
    # con el parámetro 1 como identificador.
    elif ((type(par1) == type(int)) and (type(par2) == type(Red())) and 
          (par3 == None)):
        par1.agentes.add(Agente(par1))
    
    # si no se cumple ninguna de las especificaciones anteriores
    # se lanza un error. 
    else:
        print("error con los parámetros: configuración no encontrada")
    
            
