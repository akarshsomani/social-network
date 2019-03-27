import networkx as nx
import matplotlib.pyplot as plt
import random

def plot_distribution(G):
    print(nx.degree(G))
    all_degree=list(dict((nx.degree(G))).values())
    
    unique_degree=list(set(all_degree))
    unique_degree.sort()
    nodes_with_degree=[]
    for i in unique_degree:
        nodes_with_degree.append(all_degree.count(i))
    
    plt.plot(unique_degree,nodes_with_degree)
    plt.xlabel("Degrees")
    plt.ylabel("No. of nodes")
    plt.title("Degree distribution")
    plt.show()

n= int(input())

p=float(input())

G=nx.Graph()

G.add_nodes_from(range(1,n+1))

for i in G.nodes():
    for j in G.nodes():
        if(i<j):
            r=random.random()
            if(r<p):
                G.add_edge(i,j)
#        pos=nx.circular_layout(G)
#        nx.draw(G,pos,with_labels=1)
#        plt.show()
plot_distribution(G)        