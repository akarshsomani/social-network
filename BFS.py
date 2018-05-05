#BFS in networkx network
import networkx as nx

def BFS(G,start):
    neigh=[]
    queue=[]
    queue.append(s)
    record=[]
    record.append(s)

    while(queue != []):
        current=queue.pop(0)
        #print(current)
        neigh=list(G.neighbors(current))
        neigh.sort()
        #print(neigh)
        for i in neigh:        
            if i not in record:
                queue.append(i)
                record.append(i)
    return(record)

G=nx.erdos_renyi_graph(10,0.5)

s=int(input("Enter any start node in 0 to 9 :- "))
traversal=BFS(G,s)
print(traversal)
