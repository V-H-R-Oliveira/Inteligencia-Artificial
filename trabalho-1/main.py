from grafo import Grafo
import sys 

# https://medium.com/kredo-ai-engineering/search-algorithms-part-2-uninformed-search-algorithms-1-be5583a2f1e1
# http://www.dainf.ct.utfpr.edu.br/~tacla/IA/011a-Busca-Cega.pdf

if __name__ == "__main__":
    if len(sys.argv) == 4:
        grafo = Grafo()
        grafo.init_grafo()
        inicio = sys.argv[1]
        fim = sys.argv[2]
        profundidade = int(sys.argv[3])
        grafo.busca_custo_uniforme(inicio, fim)
        grafo.busca_extensao(inicio, fim)
        grafo.busca_profundidade(inicio)
        print("\x1B[01;95m[Busca em profundidade] Ordem de visita da busca em profundidade {}\n e o seu custo é {}\x1B[0m".format( 
               grafo.ordemVisita[:len(grafo.ordemVisita) - 4], grafo.custoProfundidade))
        grafo.dls(inicio, fim, profundidade)
        grafo.iddfs(inicio, fim, profundidade)
    else:
        print("Usage python3 {} <inicio> <fim> <profundidade>".format(sys.argv[0]))
        sys.exit(1)