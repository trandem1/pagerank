import networkx as nx

def evaluatePageRank(G,alpha):
    pr = nx.pagerank(G,alpha)
    return pr