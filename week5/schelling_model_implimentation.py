import networkx as nx
import matplotlib.pyplot as plt
import random
n=10
G=nx.grid_2d_graph(n,n)

#print(G.nodes())
pos= dict((n,n)for n in G.nodes())#(n,n)=(key,value) of the new dict
labels= dict(((i,j),i*10+j)for i,j in G.nodes())

def display_graph(G):
    nodes_g=nx.draw_networkx_nodes(G,pos,node_color='green',nodelist=type1_node_list)
    nodes_r=nx.draw_networkx_nodes(G,pos,node_color='red',nodelist=type2_node_list)
    nodes_w=nx.draw_networkx_nodes(G,pos,node_color='white',nodelist=empty_cells)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos,labels=labels)
    plt.show()

def get_boundary_nodes(G):
    boundary_nodes_list=[]
    for ((u,v),d) in G.nodes(data=True):
        if(u==0 or v==n-1 or u==n-1 or v==0):
            boundary_nodes_list.append((u,v))
    return boundary_nodes_list

def get_neigh_for_internal(u,v):
    return([(u-1,v),(u+1,v),(u,v-1),(u,v+1),(u-1,v+1),(u+1,v-1),(u-1,v-1),(u+1,v+1)])

def get_neigh_for_boundary(u,v):
    if(u==0 and v==0):
        return([(0,1),(1,1),(1,0)])
    elif(u==n-1 and v==n-1):
        return([(n-2,n-2),(n-1,n-2),(n-2,n-1)])
    elif(u==n-1 and v==0):
        return([(u-1,v),(u,v+1),(u-1,v+1)])
    elif(u==0 and v==n-1):
        return([(u+1,v),(u+1,v-1),(u,v-1)])
    elif(u==0):
        return([(u,v-1),(u,v+1),(u+1,v),(u+1,v-1),(u+1,v+1)])
    elif(v==n-1):
        return([(u,v-1),(u-1,v),(u+1,v),(u-1,v-1),(u+1,v-1)])
    elif(u==n-1):
        return([(u-1,v),(u,v-1),(u,v+1),(u-1,v+1),(u-1,v-1)])    
    elif(v==0):
        return([(u-1,v),(u+1,v),(u,v+1),(u-1,v+1),(u+1,v+1)])
        
def get_unsatisfied_nodes_list(G,internal_nodes_list, boundary_nodes_list):
    unsatisfied_nodes_list=[]
    t=3
    for u,v in G.nodes():
        type_of_this_node=G.node[(u,v)]['type']
        
        if(type_of_this_node==0):
            continue
        else:
            similar_nodes=0
            if((u,v) in internal_nodes_list):
                neigh=get_neigh_for_internal(u,v)
            elif((u,v) in boundary_nodes_list):
                neigh=get_neigh_for_boundary(u,v)
            
            for each in neigh:
                if(G.node[each]['type']==type_of_this_node):
                    similar_nodes+=1
            if(similar_nodes<=t):
                unsatisfied_nodes_list.append((u,v))
                
    return unsatisfied_nodes_list

def make_a_node_satisfied(unsatisfied_nodes_list,empty_cells):
    if(len(unsatisfied_nodes_list)!=0):
        node_to_shift=random.choice(unsatisfied_nodes_list)
        new_position=random.choice(empty_cells)
        
        G.node[new_position]['type']=G.node[node_to_shift]['type']
        G.node[node_to_shift]['type']=0
        labels[node_to_shift],labels[node_to_shift]=labels[node_to_shift],labels[node_to_shift]
    else:
        pass
    
        
        
for (u,v) in G.nodes():
    if(u+1<=n-1 and v+1<=n-1):
        G.add_edge((u,v),(u+1,v+1))
    if(u+1<=n-1 and v-1>=0):
        G.add_edge((u,v),(u+1,v-1))
#nx.draw(G,pos, labels=labels)
#plt.show()

for ni in G.nodes():
    G.node[ni]['type']=random.randint(0,2)

type1_node_list=[ni for (ni,d) in G.nodes(data=True) if d['type']==1]
type2_node_list=[ni for (ni,d) in G.nodes(data=True) if d['type']==2]
empty_cells=[ni for (ni,d) in G.nodes(data=True) if d['type']==0]
#n for (n,d) in G.nodes(data=True)----
#it means n=node value and d= dictonary with type or contemts of nodes.
#print(type1_node_list)
#print(type2_node_list)
#print(empty_cells)
display_graph(G)

boundary_nodes_list=get_boundary_nodes(G)
internal_nodes_list=list(set(G.nodes())-set(boundary_nodes_list))

#print(boundary_nodes_list)
#print(internal_nodes_list)
unsatisfied_nodes_list=get_unsatisfied_nodes_list(G,internal_nodes_list,boundary_nodes_list)
#for i in range(1000):
while(unsatisfied_nodes_list!=[]):

    unsatisfied_nodes_list=get_unsatisfied_nodes_list(G,internal_nodes_list,boundary_nodes_list)
    #print(unsatisfied_nodes_list)
    
    make_a_node_satisfied(unsatisfied_nodes_list,empty_cells)
    
    type1_node_list=[ni for (ni,d) in G.nodes(data=True) if d['type']==1]
    type2_node_list=[ni for (ni,d) in G.nodes(data=True) if d['type']==2]
    empty_cells=[ni for (ni,d) in G.nodes(data=True) if d['type']==0]

display_graph(G)