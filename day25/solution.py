import math, itertools as it, networkx as nx

diagram=dict((l[:l.index(':')],l[l.index(':')+1:].split())for l in open('input.txt', 'r').readlines())
G = nx.Graph()
for l in open('input.txt', 'r').readlines():
    c1=l[:l.index(':')]
    for c2 in l[l.index(':')+1:].split():
        G.add_edge(c1,c2)

# find the 6 nodes with highest https://en.wikipedia.org/wiki/Betweenness_centrality
bc=nx.betweenness_centrality(G)
highest=sorted(bc.values())[-6:]
bridges=[k for k,v in bc.items() if v in highest]

for b1,b2 in it.combinations(bridges,2):
    if G.has_edge(b1,b2):
        G.remove_edge(b1,b2)        
print(math.prod(G.subgraph(c).number_of_nodes() for c in nx.connected_components(G)))