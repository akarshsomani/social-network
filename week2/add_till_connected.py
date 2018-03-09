import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy

def create_nodes(n):
    g=nx.Graph()
    g.add_nodes_from(range(n))
    return g

def add_random_edge(G):    
    v1=random.choice(list(G.nodes()))
    v2=random.choice(list(G.nodes()))    
    if(v1!=v2):
        G.add_edge(v1,v2)           
    return G
    
#A graph is connected when there is a path between every pair of vertices.
def add_till_connected(G):
    while(nx.is_connected(G)==False):
        G=add_random_edge(G)
    return G


def create_instance(n):
    G=create_nodes(n)
    G=add_random_edge(G)
    G=add_till_connected(G)
    return G.number_of_edges()
    
def avg_instance(n):
    list1=[]
    for i in range(0,100):
        list1.append(create_instance(n))
    return numpy.average(list1)



x=[]
y=[]
y1=[]
i=10
while(i<150):
    print(i)
    x.append(i)
    y.append(avg_instance(i))
    y1.append(i*(numpy.log(i))/2)
    i=i+10

plt.xlabel("no. of nodes")
plt.ylabel("no of edges for connectivity")
plt.plot(x,y)
plt.plot(x,y1)
plt.show()


