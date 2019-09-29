import sys, queue

class Grafo(object):
    def __init__(self):
        self.__grafo = {}
        self.__visitados = set()
        self.ordemVisita = ""
        self.custoProfundidade = 0
        
    def __repr__(self):
        return "Grafo: {}\n".format(self.__grafo)
    
    def init_grafo(self):
        qtd_nos = int(input("Quantidade de nós: "))
    
        for ligacao in range(qtd_nos):
            tokens = input("Digite o nó e as suas respectivas ligações, exemplo \x1B[01;93m a b 10 c 30 d 40\x1b[0m: ").split()
            no = tokens[0]
            self.__grafo[no] = {}
            
            for i in range(1, len(tokens) - 1, 2):
                self.__grafo[no][tokens[i]] = int(tokens[i + 1])
    
    def __resetContadores(self):
        self.ordemVisita = ""
        self.custoProfundidade = 0
        
    def iddfs(self, inicio, fim, profundidade): # Busca em aprofundamento iterativo - diferença é que percorre as profundidades de 0...n
        self.__resetContadores()
        
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
            
        for i in range(profundidade):
            if self.__busca_profundidade_limitada(inicio, fim, i):
                print("\x1B[01;93m[Busca de aprofundamento iterativo] Caminho:", self.ordemVisita[:len(self.ordemVisita) - 4], 
                      "\n e o seu custo é:", self.custoProfundidade, "\x1B[0m")
                return 
            
        print("\x1B[31m[Busca de aprofundamento iterativo] Não existe caminho...\x1B[0m ")
        return
    
    def dls(self, inicio, fim, profundidade): #busca em profundidade limitada - profundidade é única
        self.__resetContadores()
        
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
            
        if self.__busca_profundidade_limitada(inicio, fim, profundidade):
                print("\x1B[01;90m[Busca em profundidade limitada] Caminho:", self.ordemVisita[:len(self.ordemVisita) - 4], 
                      "\n e o seu custo é:", self.custoProfundidade, "\x1B[0m")
                return 
                
        print("\x1B[31m[Busca em profundidade limitada] Não existe caminho...\x1B[0m ")
        return 
    
    def __busca_profundidade_limitada(self, inicio, fim, profundidade): 

        if inicio == fim:
            return True
        
        if profundidade < 1:
            return False
        
        for no in self.__grafo[inicio]:
            self.ordemVisita += no + " -> "
            if self.__busca_profundidade_limitada(no, fim, profundidade - 1):
                self.custoProfundidade += self.__grafo[inicio][no]
                return True
        return False
    
    def busca_profundidade(self, vertice): # DFS
        if vertice not in self.__grafo:
             print("\x1B[31mO nó não se encontra representado no grafo\x1B[0m")
             sys.exit(1)
            
        self.__visitados.add(vertice)
        vizinhos = self.__grafo[vertice]
        
        self.ordemVisita += vertice + " -> "     
        #print("Vizinhos de {}:".format(vertice), vizinhos)
        #print("Nós que já foram visitados:", self.__visitados)
    
        for index, no in enumerate(vizinhos):
            if len(self.__visitados) == len(self.__grafo):
                return
            elif no in self.__visitados:
                #print("O {} já se encontra nos {}".format(no, self.__visitados))
                continue
            else:
                #print("Nó a ser visitado:", no)
                self.custoProfundidade += self.__grafo[vertice][no]
                self.busca_profundidade(no)
            
    def busca_extensao(self, inicio, fim): # BFS
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
        
        fila = queue.Queue()
        fila.put((0, [inicio]))
        
        while not fila.empty():
            no = fila.get()
            no_atual = no[1][len(no[1]) - 1]
            
            if fim in no[1]:
                print("\x1B[96m[Busca em extensão] Caminho encontrado: " + str(no[1]) + ", e o seu custo é: " + str(no[0]) + "\x1B[0m")
                return
            
            custo = no[0]
            for vizinho in self.__grafo[no_atual]:
                aux = no[1][:]
                aux.append(vizinho)
                fila.put((custo + self.__grafo[no_atual][vizinho], aux))
        
        print("\x1B[31m O caminho não foi encontrado \x1B[0m")
        sys.exit(1)
        

    def busca_custo_uniforme(self, inicio, fim): # BCU
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
        
        fila_prioridades = queue.PriorityQueue()
        fila_prioridades.put((0, [inicio]))
        
        while not fila_prioridades.empty():
            no = fila_prioridades.get()
            no_atual = no[1][len(no[1]) - 1]
            
            if fim in no[1]:
                print("\x1B[01;91m[Busca de custo uniforme] Caminho encontrado: " + str(no[1]) + ", e o seu custo é: " + str(no[0]) + "\x1B[0m")
                return 
            
            custo = no[0]
            for vizinho in self.__grafo[no_atual]:
                aux = no[1][:]
                aux.append(vizinho)
                fila_prioridades.put((custo + self.__grafo[no_atual][vizinho], aux))
        
        print("\x1B[31m O caminho não foi encontrado \x1B[0m")
        sys.exit(1)