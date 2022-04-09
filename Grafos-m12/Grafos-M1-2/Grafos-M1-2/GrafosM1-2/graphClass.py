from collections import defaultdict
from array import *
from glob import glob
from turtle import color
import numpy as np
from matplotlib.pyplot import connect
from operator import contains, eq
from genericpath import isdir
from operator import eq
from matplotlib.style import use
import networkx as nx
import matplotlib.pyplot as plt 

visitedSubgraphs = set()
visited = set()
visitedBfs = []
visitedConnected = set()
queue = []
listOfSets= list()
temp = []

def dfsForConnectivity(visitedConnected,graph,node):
 if node not in visitedConnected:
        print ("Visitei", node, end=" ")
        visitedConnected.add(node)
        for neighbour in graph[node]:
            dfsForConnectivity(visitedConnected, graph, neighbour)

def dfs(visited,graph,node,lookedForNode):
    ##EXEMPLE OF GRAPH STRUCTURE
    ## { 0:[1,2] 1:[0]}
    if node not in visited:
        print ("Visitei", node, end=" ")
        visited.add(node)
        if(eq(int(node),int(lookedForNode))):
            resultToReturn = True
            return resultToReturn
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour,lookedForNode)

def bfs(visitedBfs, graph, node,lookedForNode): 
  visitedBfs.append(node)
  queue.append(node)
  if(eq(int(node),int(lookedForNode))):
    resultToReturn = True
    return resultToReturn
  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 
    for neighbour in graph[m]:
      if neighbour not in visitedBfs:
        visitedBfs.append(neighbour)
        queue.append(neighbour)
    

 

class Graph(object):
    def __init__(self, vertices, directed):
        self.vertices = int(vertices)
        self.directed = directed
        self.arr = self.createArray()


    def checkSubraphs(self):
        print("Checando conectividade")
 
        initialPoint = int(0)
        if(initialPoint>self.arr.shape[0] or initialPoint<0):
            return "Erro, digite um vertice valido"
        graph = self.graphToDict()
        node = initialPoint
        dfsForConnectivity(visitedSubgraphs,graph,node)
        if(len(visitedSubgraphs)!=self.arr.shape[0]):
            listOfSets.append(visitedSubgraphs.copy())
            remainingNodes = set(visitedSubgraphs) ^ set(self.helperFunction())
            remainingNodes= list(remainingNodes)
            weakVertices = list()
            print("Ainda faltam vertices... ",remainingNodes)
            for i in (remainingNodes):
                visitedSubgraphs.clear()
                dfsForConnectivity(visitedSubgraphs,graph,i)
                listOfSets.append(visitedSubgraphs.copy())
            for x in range(len(listOfSets)):
                if((len(listOfSets[x]))<2):
                    weakVertices.append(listOfSets[x].copy())
                    ##listOfSets.remove(listOfSets[x])
            removeDuplicatedItensWeakList = []
            [removeDuplicatedItensWeakList.append(x) for x in weakVertices if x not in removeDuplicatedItensWeakList]
            for x in removeDuplicatedItensWeakList:
                listOfSets.remove(x)
            removeDuplicatedItensList = []

            [removeDuplicatedItensList.append(x) for x in listOfSets if x not in removeDuplicatedItensList]
            print("\n Os subgrafos com conexoes fortes sao", removeDuplicatedItensList)
            print("\n Os subgrafos com conexoes fracas sao", removeDuplicatedItensWeakList)
        else:
            print("Grafo conexo")
    def checkConnectivity(self):
        print("Checando conectividade")
        print("Qual o ponto inicial de busca?")
        initialPoint = int(input())
        if(initialPoint>self.arr.shape[0] or initialPoint<0):
            return "Erro, digite um vertice valido"

        graph = self.graphToDict()
        node = initialPoint
        result = dfsForConnectivity(visitedConnected,graph,node)
        print(visitedConnected)
        if(len(visitedConnected)!=self.arr.shape[0]):
            print("Grafo desconexo")
        else:
            print("Grafo Conexo")



    def graphToDict(self):
        ##TURNS THE MATRIX OF 1 AND 0 INTO A DICTONARY OF THE INDEXES
        graph = {}
        for i in range(self.arr.shape[0]):
            graph[i]=[]
            for j in range(self.arr.shape[0]):
                if(self.arr[i][j]!=0):
                    graph[i].append(j)
        print(graph)
        return graph
    def helperFunction(self):
        arrayOfIndexes = []
        for i in range(self.arr.shape[0]):
            arrayOfIndexes.append(i)
        return arrayOfIndexes


    
    def depthSearch(self):
        print("Qual vertice voce esta procurando?")
        searchVertice = int(input())
        print("Qual o ponto inicial de busca?")
        initialPoint = int(input())
        if(initialPoint>self.arr.shape[0] or initialPoint<0):
            return "Erro, digite um vertice valido"

        graph = self.graphToDict()
        node = initialPoint
        result = dfs(visited,graph,node,searchVertice)
        if(eq(result,True)):
            print("\nEncontrado")
            return
        if(len(visited)!=self.arr.shape[0]):
            remainingNodes = set(visited) ^ set(self.helperFunction())
            remainingNodes= list(remainingNodes)
            print("Ainda faltam vertices... ",remainingNodes)
            for i in range(len(remainingNodes)):
                result = dfs(visited,graph,remainingNodes[i],searchVertice)
                if(searchVertice in visited):
                    print("\nEncontrei, foram encontrados ", visited)
                    return
            print("\nNao encontrado, foram encontrados ", visited)
            return

    def breadthSearch(self):          
        print("Busca por largura")
        print("Qual vertice voce esta procurando?")
        searchVertice = int(input())
        print("Qual o ponto inicial de busca?")
        initialPoint = int(input())
        if(initialPoint>self.arr.shape[0] or initialPoint<0):
            return "Erro, digite um vertice valido"

        graph = self.graphToDict()
        node = initialPoint
        result = bfs(visitedBfs,graph,node,searchVertice)
        if(eq(result,True)):
            print("\nEncontrado")
            return
        if(len(visitedBfs)!=self.arr.shape[0]):
            remainingNodes = set(visitedBfs) ^ set(self.helperFunction())
            remainingNodes= list(remainingNodes)
            print("Ainda faltam vertices... ",remainingNodes)
            for i in range(len(remainingNodes)):
                result = bfs(visitedBfs,graph,remainingNodes[i],searchVertice)
                if(searchVertice in visitedBfs):
                    print("\nEncontrei, foram encontrados ", visitedBfs)
                    return
            print("\nNao encontrado, foram encontrados ", visitedBfs)
            return



    def printEdges(self):
        print(self.edges)

    def insertVertice(self):
        ##SHAPE = (1,1) - (2,2)
        self.arr=np.insert(self.arr,self.arr.shape[0],0,axis=0)
        self.arr=np.insert(self.arr, self.arr.shape[1], 0, axis=1)

                
    def removeVertice(self):
        print("Qual vertice voce deseja excluir?")
        vertice = int(input())
        if(self.arr.shape[1]>=vertice and self.arr.shape[0]>=vertice):
            self.arr = np.delete(self.arr,vertice,1)
            self.arr = np.delete(self.arr,vertice,0)
        else:
            print("Erro, vertice inexistente")        
        
    def insertOrRemoveConnection(self, insert):
        print("Numero do primeiro item:")
        x = int(input())
        y= 999
        while(not eq(y,-1)):
            print("LOOP: Selecione os itens que fazem relacao com o PRINCIPAL - Digite -1 para cancelar")
            y = int(input())
            if(eq(x,y)):
                print("O vertice nao pode ser o mesmo")
            elif((x<=self.arr.shape[0] or y<=self.arr.shape[0]) and not(eq(y,-1))):
                if(eq(insert, True)):
                    print("Conexao gerada")
                    self.arr[x][y] =1
                    if(eq(self.directed,False)):
                        self.arr[y][x] = 1
                else:
                    print("Conexao removida")
                    self.arr[x][y] =0
                    if(eq(self.directed,False)):
                        self.arr[y][x] = 0
            else:
                print("Vertice inexistente")


    def createArray(self):
        s = (self.vertices,self.vertices)
        s = np.zeros((s),dtype=int)
        return s

    def printArray(self):
        print(self.arr)
        printTuple = ()
        arrayOfTuples = []
        if(self.directed==True):
            G = nx.MultiDiGraph()
        if(self.directed==False):
            G = nx.MultiGraph()
        ##Creating nodes
        for x in range(self.arr.shape[0]):
            G.add_node(x)
        ##adding connections
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                if(eq(self.arr[i][j],1)):
                    t=(i,j)
                    arrayOfTuples.append(t)
        printTuple = (arrayOfTuples)                 
        print(printTuple)
        G.add_edges_from(printTuple)
        plt.figure(figsize=(8,8))
        nx.draw(G,  with_labels=True ,connectionstyle='arc3, rad = 0.1')
        plt.show()  # pause before exiting


    