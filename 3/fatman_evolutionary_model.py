import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time

def create_graph():
    G=nx.Graph()    
    G.add_nodes_from(range(1,101))
    return G

def visualize(G,t):
    time.sleep(1)
    labeldict=get_labels(G)
    nodesize=get_size(G)
    color=get_colors(G)
    nx.draw(G,labels=labeldict,node_size=nodesize,node_color=color)
    plt.savefig('evolution.jpg')
    plt.clf()
    plt.cla()
    nx.write_gml(G,'evolution_'+str(t)+'.gml')
    #or simply plt.show()
    
def assign_bmi(G):
    for each in G.nodes():
        G.node[each]['name']=random.randint(15,40)
        G.node[each]['type']='person'
   
def get_labels(G):
    dict1={}
    for each in G.nodes():
        dict1[each]=G.node[each]['name']
        #print(dict1[each])
    #print(dict1)
    return dict1

def get_size(G):
    array1=[]
    for each in G.nodes():
        if(G.node[each]['type']=='person'):
            array1.append(G.node[each]['name']*10)
        else:
            array1.append(500)
    return array1

def add_foci_nodes(G):
    n=G.number_of_nodes()
    i=n+1
    foci_nodes=['gym','eatout','movie_club','karate_club','yoga_club']
    for j in range(5):
        G.add_node(i)
        G.node[i]['name']=foci_nodes[j]
        G.node[i]['type']='foci'
        i+=1
        
        
def get_colors(G):
    c=[]
    for i in G.nodes():
        if(G.node[i]['type']=='person'):
            if(G.node[i]['name']==15):
                c.append('yellow')
            elif(G.node[i]['name']==40):
                c.append('green')
            else:
                c.append('blue')
        else:
            c.append('red')
    return c

def get_person_nodes(G):
    p=[]
    for i in G.nodes():
        if(G.node[i]['type']=='person'):
            p.append(i)
    return p

def get_foci_nodes(G):
    f=[]
    for i in G.nodes():
        if(G.node[i]['type']=='foci'):
            f.append(i)
    return f

def add_foci_edges(G):
    foci_nodes=get_foci_nodes(G)
    person_nodes=get_person_nodes(G)
    #print(foci_nodes)
    #print(person_nodes)
    for i in person_nodes:
        r=random.choice(foci_nodes)
        G.add_edge(i,r)
        
def homophily(G):
    pnodes=get_person_nodes(G)
    for u in pnodes:
        for v in pnodes:
            if(u!=v):
                diff=abs(G.node[u]['name']-G.node[v]['name'])
                p=1/(diff+1000)
                r=random.uniform(0,1)
                if(r<p):
                    G.add_edge(u,v)
def cmn(u,v,G):
    nu=set(G.neighbors(u))
    nv=set(G.neighbors(v))
    return(len(nu & nv))



def closure(G):
    array1=[]
    for u in G.nodes():
        for v in G.nodes():
            if(u!=v and G.node[u]['type']=='person' or G.node[v]['type']=='person' ):
                k=cmn(u,v,G)
                p=1-math.pow(1-0.01,k)
                tmp=[]
                tmp.append(u)
                tmp.append(v)
                tmp.append(p)
                array1.append(tmp)
    #print(array1)
    for i in array1:
        u=i[0]
        v=i[1]
        p=i[2]
        r=random.uniform(0,1)
        if r<p:
            G.add_edge(u,v)

def change_bmi(G):
    fnodes=get_foci_nodes(G)
    for i in fnodes:
        if(G.node[i]['name']=='eatout'):
            for j in G.neighbors(i):
                if(G.node[j]['name']!=40):
                    G.node[j]['name']=G.node[j]['name'] + 1
        if(G.node[i]['name']=='gym'):
            for j in G.neighbors(i):
                if(G.node[j]['name']!=15):
                    G.node[j]['name']=G.node[j]['name'] - 1
        
         
  
G=create_graph()
assign_bmi(G)
add_foci_nodes(G)#to add interest field in the nodes
add_foci_edges(G)
time.sleep(10)
visualize(G,0)
#nx.write_gml(G,'evolution_0.gml')
for t in range(1,10):    
    homophily(G)
    closure(G)
    change_bmi(G)
    visualize(G,t+1)
