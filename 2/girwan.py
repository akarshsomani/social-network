import networkx as nx
import matplotlib.pyplot as plt
def edge_to_remove(G):
    dict1=nx.edge_betweenness_centrality(G)
    
    list_of_touples=list(dict1.items())
    list_of_touples.sort(key=lambda x:x[1], reverse=True)
    return (list_of_touples[0][0])# gonna return a touple ((a,b))
    
def girvan(G):
    c=list(nx.connected_component_subgraphs(G))
    print(c)
    
    l=len(c)
    print('no of connected components are ,',l)
    
    while(l==1):
        G.remove_edge(*edge_to_remove(G))#((a,b))-->(a,b)
        c=list(nx.connected_component_subgraphs(G))
        
        l=len(c)
        print('no of connected components are ,',l)
    return c

G=nx.barbell_graph(10,0)

nx.draw(G)
plt.show()

c=girvan(G)
nx.draw(G)
plt.show()
for i in c:
    print(i.nodes())
