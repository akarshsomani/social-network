import networkx as nx
import matplotlib.pyplot as plt

def check_exixtance(H,d):
    f=0#there is no node of deg<=d
    for i in H.nodes():
        if(H.degree(i)<=d):
            f=1
            break
    return f

def find(H,it):
    set1=[]
    for i in H.nodes():
        if(H.degree(i)<=it):
            set1.append(i)
    return set1


G=nx.Graph()
G.add_edges_from([(1,2),(1,12),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])

H=G.copy()
it=1
tmp=[]#for the bucket being filled currently
buckets=[]#list of lists(buckets)
while(1):
    flag=check_exixtance(H,it)
    if(flag==0):
        it+=1
        buckets.append(tmp)
        tmp=[]#start with fresh bucket
    if(flag==1):
        node_set=find(H,it)
        for each in node_set:
            H.remove_node(each)
            tmp.append(each)
    if(H.number_of_nodes()==0):
        buckets.append(tmp)
        break
print(buckets)
        

nx.draw(G, with_labels=1)
plt.show()