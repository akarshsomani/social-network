import networkx as nx
import random
import numpy as np


def add_edges(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if(i!=j):
                r=random.random()
                if(r<p):
                    G.add_edge(i,j)
                else:
                    continue
    return G



def nodes_sorted_by_point(G,points):
    temp=np.array(points)
    temp=np.argsort(-temp)
    return temp

def random_walk(G):
    rwpoints=[0 for i in range(G.number_of_nodes())]
    nodes=list(G.nodes())
    #print(nodes)
    r=random.choice(nodes)
    #print(r)
    rwpoints[r]+=1
    neigh=list(G.out_edges(r))
    c=0
    while(c!=10000):
        if(len(neigh)==0):
            focus=random.choice(nodes)
        else:
            #print(neigh)
            r1=random.choice(neigh)
            focus=r1[1]
        rwpoints[focus]+=1
        neigh=list(G.out_edges(focus))
        c+=1
    return rwpoints




def main():
    #create a directed graph with n nodes
    G=nx.DiGraph()
    n=10
    G.add_nodes_from(range(n))
    G=add_edges(G,0.3)
    
    #perform a random walk
    points=random_walk(G)
    
    #get nodes ranking according to their random walk points value
    sorted_by_points=nodes_sorted_by_point(G,points)
    print(sorted_by_points)
    
    pr=nx.pagerank(G)
    #pr is dictonary of touples
    pr_sorted=sorted(pr.items(), key= lambda x:x[1], reverse=True)
    for i in pr_sorted:
        print(i[0],end=",")
        
main()