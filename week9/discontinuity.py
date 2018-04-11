import networkx as nx
import matplotlib.pyplot as plt
import random as r

def remove_random_node(G1):
    nodes=list(G1.nodes())
    selected_node=r.choice(nodes)
    G1.remove_node(selected_node)
    return G1


def remove_selective_node(G2):
    degrees=dict(G2.degree())
    #print(degrees)
    nodes=sorted(degrees.items(), key= lambda x:x[1], reverse=True)
    G2.remove_node(nodes[0][0])
    return G2

def main():
    G=nx.erdos_renyi_graph(1000,0.015)
    
    print(nx.info(G))
    
    print("is graph connected? ",nx.is_connected(G))
    
    G1=G.copy()
    count1=0
    while(nx.is_connected(G1)):
        G1=remove_random_node(G1)
        count1+=1
        #print("is G1 connected? ",nx.is_connected(G1))
    print("number of iterations for G1 to be disconnected = ", count1)
    
    G2=G.copy()
    count2=0
    while(nx.is_connected(G2)):
        G2=remove_selective_node(G2)
        count2+=1
        #print("is G2 connected? ",nx.is_connected(G2))
    print("number of iterations for G2 to be disconnected = ", count2)
    
main()   
        
    