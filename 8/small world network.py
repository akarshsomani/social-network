#myopic search

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def add_edges(G):#based on watts strogats model
    list_nodes=list(G.nodes())
    #print(type(list_nodes))
    n=len(list_nodes)
    #print(list_nodes)
    for i in range(0,len(list_nodes)):
#        print(i)
#        print(list_nodes[0])
#        print(list_nodes[i], list_nodes[i-1])
        G.add_edge(list_nodes[i], list_nodes[i-1])
        G.add_edge(list_nodes[i], list_nodes[i-2])
        target=i+1
        if(target>n-1):
            target=target-n
            
        G.add_edge(list_nodes[i], target)
        target=i+2
        if(target>n-1):
            target=target-n
            
        G.add_edge(list_nodes[i], target)
    return G

def add_long_link(G):
    list_nodes=list(G.nodes())
    v1=random.choice(list_nodes)
    v2=random.choice(list_nodes)
    while(v1==v2):
        v1=random.choice(list_nodes)
        v2=random.choice(list_nodes)
    G.add_edge(v1,v2)
    return G

def plot_diameter_variation(G):
    x=[0]
    y=[nx.diameter(G)]
    t=0
    while(t<=G.number_of_nodes()/10):
        G=add_long_link(G)
        t+=1
        x.append(t)
        y.append(nx.diameter(G))
        
    plt.xlabel('Number of weak ties added')
    plt.ylabel('Diameter')
    plt.plot(x,y)
    plt.show()
    return

def find_best_neighbor(G, c, v):
    dis=G.number_of_nodes()
    for i in G.neighbors(c):
        dis1=len(nx.shortest_path(H,source=i, target=v))#H is the graph without any long range links.
        if(dis1<dis):
            dis=dis1
            choice=i
    return choice

def myopic_search(G,u,v):
    path=[u]
    current=u
    while(1):
        w=find_best_neighbor(G, current, v)
        path.append(w)
        current=w
        if(current==v):
            break
    return path
    
def set_path_colors(G,p,p1):
    c=[]
    for each in G.nodes():
        if(each==p[0]):
            c.append('red')
        if(each==p[len(p)-1]):
            c.append('red')
        if(each in p and each in p1 and each!=p1[0] and each!=p1[len(p1)-1]):
            c.append('yellow')
        if(each in p and each not in p1):
            c.append('blue')
        if(each in p1 and each not in p):
            c.append('green')
        if(each not in p and each not in p1):
            c.append('grey')
    return c
        
def plot_myopicVSoptimal(G):
    m=[]#path length coresponding to the myopic search
    o=[]#path length coresponding to the optimal search
    x=[]#each point on x axis is one pair of nodes -(0,50),(1,51)...(49,99)
    t=0
    for u in range(0,G.number_of_nodes()//2 -1):
        v=u+G.number_of_nodes()//2
        p=myopic_search(G,u,v)
        p1=nx.shortest_path(G,source=u,target=v)
        m.append(len(p))
        o.append(len(p1))
        x.append(t)
        t+=1   
    plt.plot(x,m,'r')
    plt.plot(x,o,'b')
    plt.show()
    return 

def plot_time_complexity():
    x1=[]
    y1=[]
    for i in [100,200,300,400,500,600,700,800,900,1000]:
        G=nx.Graph()
        G.add_nodes_from(range(0,i))
        G=add_edges(G)
        H=G.copy()
        t=0
        while(t<=G.number_of_nodes()/10):
            G=add_long_link(G)
            t+=1
        m=[]#path length coresponding to the myopic search   
        for u in range(0,G.number_of_nodes()//2 -1):
            v=u+G.number_of_nodes()//2
            p=myopic_search(G,u,v)        
            m.append(len(p))
            
        y1.append(np.average(m))
        x1.append(G.number_of_nodes())
        print(G.number_of_nodes(),np.average(m))
    plt.plot(x1,y1)
    plt.show()
    
G=nx.Graph()
G.add_nodes_from(range(0,100))

G=add_edges(G) #add ties based on homoplily(watts strogats model)

#for i in G.nodes():
#    print(i, tuple(G.neighbors(i)))
    
#G=add_long_link(G)#add weak ties

H=G.copy()
plot_diameter_variation(G)

plot_myopicVSoptimal(G)

p=myopic_search(G,0,49)
p1=nx.shortest_path(G,source=0,target=49)
colors=set_path_colors(G,p,p1)

nx.draw(G, with_labels=1, node_color=colors)
plt.show()

plot_time_complexity()

