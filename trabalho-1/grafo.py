import sys, queue, collections

class Grafo(object):
    def __init__(self):
        self.__grafo = {}
        self.__visitados = set()
        self.__ordemVisita = ""
        self.__custo = 0
        
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
        self.__ordemVisita = ""
        self.__custo = 0
        
    def iddfs(self, inicio, fim, profundidade): # Busca em aprofundamento iterativo - diferença é que percorre as profundidades de 0...n
        self.__resetContadores()
        
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
            
        for i in range(profundidade):
            if self.__busca_profundidade_limitada(inicio, fim, i):
                print("\x1B[01;93m[Busca de aprofundamento iterativo] Caminho: " + self.__ordemVisita[:len(self.__ordemVisita) - 4] + ", e o seu custo é:", self.__custo, "\x1B[0m")
                return 
            
        print("\x1B[31m[Busca de aprofundamento iterativo] Não existe caminho...\x1B[0m ")
        return
    
    def dls(self, inicio, fim, profundidade): #busca em profundidade limitada - profundidade é única
        self.__resetContadores()
        
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
            
        if self.__busca_profundidade_limitada(inicio, fim, profundidade):
                print("\x1B[01;90m[Busca em profundidade limitada] Caminho: " + self.__ordemVisita[:len(self.__ordemVisita) - 4] + ", e o seu custo é:", self.__custo, "\x1B[0m")
                return 
                
        print("\x1B[31m[Busca em profundidade limitada] Não existe caminho...\x1B[0m ")
        return 
    
    def __busca_profundidade_limitada(self, inicio, fim, profundidade): 

        if inicio == fim:
            self.__ordemVisita += inicio + " <- "
            return True
        
        if profundidade < 1:
            return False
        
        for no in self.__grafo[inicio]:
            if self.__busca_profundidade_limitada(no, fim, profundidade - 1):
                self.__ordemVisita += inicio + " <- "
                self.__custo += self.__grafo[inicio][no]
                return True
        return False
    
    def busca_profundidade(self, inicio, fim): # DFS
        if inicio not in self.__grafo or fim not in self.__grafo:
             print("\x1B[31mO nó ou os nós não se encontram representados no grafo\x1B[0m")
             sys.exit(1)
            
        self.__visitados.add(inicio)
        vizinhos = self.__grafo[inicio]
        
        self.__ordemVisita += inicio + " -> "
        
        if inicio == fim:
                print("\x1B[01;95m[Busca em profundidade] Ordem de visita da busca em profundidade: {}, e o seu custo é {}\x1B[0m".format(
                    self.__ordemVisita[:len(self.__ordemVisita) - 4], self.__custo))
                return
    
        for index, no in enumerate(vizinhos):
            if no in self.__visitados:
                continue
            else:
                self.__custo += self.__grafo[inicio][no]
                self.busca_profundidade(no, fim)
            
    def busca_extensao(self, inicio, fim): # BFS
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
        
        self.__resetContadores()
        dequeue = collections.deque([])
        visitados = set()
        visitados.add(inicio)
        dequeue.append(inicio)
    
        while len(dequeue) != 0:
            atual = dequeue.popleft()
            self.__ordemVisita += atual + " -> "
             
            if atual == fim:
                print("\x1B[96m[Busca em extensão] Caminho encontrado: " + self.__ordemVisita[:len(self.__ordemVisita) - 4] + ", e o seu custo é: " + str(self.__custo) + "\x1B[0m")
                return 

            for vizinho in self.__grafo[atual]:
                if vizinho not in visitados:
                    self.__custo += self.__grafo[atual][vizinho]
                    visitados.add(vizinho)
                    dequeue.append(vizinho)
        
        print("\x1B[31m O caminho não foi encontrado \x1B[0m")
        sys.exit(1)
             
    def busca_custo_uniforme(self, inicio, fim): # BCU
        if inicio not in self.__grafo or fim not in self.__grafo:
            print("\x1B[31mOs nós ou algum nó não se encontra representado no grafo\x1B[0m")
            sys.exit(1)
        
        self.__resetContadores()
        
        fila_prioridades = queue.PriorityQueue()
        fila_prioridades.put((0, [inicio]))
        
        while not fila_prioridades.empty():
            no = fila_prioridades.get()
            no_atual = no[1][len(no[1]) - 1]
            
            if fim in no[1]:
                self.__custo = str(no[0])
                for no in no[1]:
                    self.__ordemVisita += no + " -> "
                    
                print("\x1B[01;91m[Busca de custo uniforme] Caminho encontrado: " + self.__ordemVisita[:len(self.__ordemVisita) - 4] + ", e seu custo é: " + self.__custo + "\x1B[0m")
                return 
            
            custo = no[0]
            for vizinho in self.__grafo[no_atual]:
                aux = no[1][:]
                aux.append(vizinho)
                fila_prioridades.put((custo + self.__grafo[no_atual][vizinho], aux))
        
        print("\x1B[31m O caminho não foi encontrado \x1B[0m")
        sys.exit(1)