import networkx as nx

"""
tao ra mot do thi co huong
"""
def buildDiGraph():
    G = nx.DiGraph()
    return G

"""
them canh vao do thi
"""
def addEdgeToGraph(G,source,dests):
    for url in dests:
        G.add_edge(source,url)
    return G
