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

def  assign_values(G):
    points=[100 for i in range(G.number_of_nodes())]
    return points

    
def distribute(G,points):
    previous=points
    new=[0 for i in range(len(points))]
    
    for i in G.nodes():
        neigh=G.out_edges(i)
        #print(i,neigh)
        if(len(neigh)==0):
            new[i]+=previous[i]
        else:
            share=previous[i]/len(neigh)
            for each in neigh:                
                new[each[1]]+=share
        
    return G,new

def manage_sink(G,points):
    add=100*0.2
    for i in range(len(points)):
        points[i]*=0.8
        points[i]+=add
    return points
    
def convergence(G,points):    
    while(1):
        G,new=distribute(G,points)
        new=manage_sink(G,new)
        new1=list(np.multiply(new,10000).astype(int))
        points1=list(np.multiply(points,10000).astype(int))
        if(new1==points1):
            break
        else:
            points=new
        #print(new1)
    return G,points


         
def nodes_sorted_by_point(G,points):
    temp=np.array(points)
    temp=np.argsort(-temp)
    return temp


def main():
    #create a directed graph with n nodes
    G=nx.DiGraph()
    n=10
    G.add_nodes_from(range(n))
    G=add_edges(G,0.3)
    
    #assign 100 points to each node
    points= assign_values(G)
    print(points)
    #keep distributing points till it converges
    G,points=convergence(G,points)
    print(points)
    
    #get nodes ranking according to their points value
    sorted_by_points=nodes_sorted_by_point(G,points)
    print(sorted_by_points)
    
    pr=nx.pagerank(G)
    #pr is dictonary of touples
    pr_sorted=sorted(pr.items(), key= lambda x:x[1], reverse=True)
    for i in pr_sorted:
        print(i[0],end=",")
    
    




main()
