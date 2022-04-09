from genericpath import isdir
from operator import eq
from pickle import FALSE, TRUE
from matplotlib.style import use
from numpy import equal
from graphClass import Graph
import networkx as nx
import matplotlib.pyplot as plt 

running = True

def mainFlow():
    graph = welcome()
    while(running):
        menu(graph)
            
def welcome():
    print("Bem vindo ao gerenciador de grafos:")
    print("O seu grafo terá quantos vértices inicialmente?")
    numVertices = input()
    userInput = 0
    while(userInput!=1 and userInput!=2):
        print("Grafo direcionado ou não direcionado?\n"
    "1-Direcionado\n"
    "2-Nao direcionado"
    )
        userInput = int(input())
    isDirected = True
    if(int(userInput)==2):
        isDirected=False
    graph = Graph(numVertices,isDirected)
    return graph


def menu(graph):
    print("O que você deseja agora?\n"
    "1- Inserir uma conexão\n"
    "2- Remover uma conexão\n"
    "3- Inserir um vértice\n"
    "4- Remover um vértice\n"
    "5- Busca profundidade\n"
    "6- Busca largura\n"
    "7- Conectividade \n"
    "8- Subgrafos Fortemente conexos\n"
    "9- Visualizar grafo\n"
    )
    userInput = int(input())
    while (int(userInput)>9 or int(userInput)<1):
        print("Opção inválida, digite novamente...")
        userInput = input()
    if(eq(userInput,1)):
        print("Inserindo...")
        graph.insertOrRemoveConnection(True)
    elif(eq(userInput,2)):
        print("Removendo..")
        graph.insertOrRemoveConnection(False)
    elif(eq(userInput,3)):
        print("Inserindo...")
        graph.insertVertice()
    elif(eq(userInput,4)):
        print("Removendo..")
        graph.removeVertice()
    elif(eq(userInput,5)):
        print("Buscando...")
        graph.depthSearch()
    elif(eq(userInput,6)):
        print("Buscando..")
        graph.breadthSearch()
    elif(eq(userInput,7)):
        graph.checkConnectivity()
    elif(eq(userInput,8)):
        graph.checkSubraphs()
    elif(eq(userInput,9)):
        graph.printArray()

    else:
        print("undefined")
mainFlow()


"""
# create a directed multi-graph
G = nx.MultiDiGraph()
G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 2),
    (2, 1),
])
# plot the graph
plt.figure(figsize=(8,8))
nx.draw(G, connectionstyle='arc3, rad = 0.1')
plt.show()  # pause before exiting
"""