import metis
import networkx as nx


'''
Return a networkx like Graph
'''
def to_nx_Graph(graph_city_soft_id):
    gnx = nx.Graph()
    for (a,b,c) in graph_city_soft_id:
        gnx.add_edge(a-1,b-1)
    return gnx

GNX = None
'''
Return a list of sub-graph
'''
def split_graph(graph_city_soft_id, nb):
    res = []
    len_g = len(graph_city_soft_id)
    #print(len_g)
    for i in range(0,nb):
        part0 = i * (len_g//nb)
        part1 = (i+1) * (len_g//nb)
        #print(part0, part1)
        res.append(graph_city_soft_id[part0:part1])
    return res
NB_DRONES = 4
list_graphs = split_graph(graph_city, NB_DRONES)
