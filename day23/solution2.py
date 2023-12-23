import networkx as nx
mp=[[*l.strip()] for l in open('input.txt', 'r').readlines()]

# Turn maze into an undirected graph
G = nx.Graph()
for i in range(0,len(mp)):
    for j in range(0,len(mp[0])):
        if mp[i][j]!='#':
            if i>0 and mp[i-1][j]!='#':
                G.add_edge((i,j),(i-1,j),weight=1)
            if i<len(mp)-1 and mp[i+1][j]!='#':
                G.add_edge((i,j),(i+1,j),weight=1)
            if j>0 and mp[i][j-1]!='#':
                G.add_edge((i,j),(i,j-1),weight=1)
            if j<len(mp[0])-1 and mp[i][j+1]!='#':
                G.add_edge((i,j),(i,j+1),weight=1)
    
# To increase performance, simplify graph by collapsing all nodes with only 2 neighbors
nodes_to_remove = [n for n in G.nodes if len(list(G.neighbors(n))) == 2]
for node in nodes_to_remove:
    tot_weight=sum([G.get_edge_data(node,nb)['weight'] for nb in G.neighbors(node)])
    G.add_edge(*G.neighbors(node),weight=tot_weight)
    G.remove_node(node)

# Find simple path with maximum weight (=length in original graph)
print(max([nx.path_weight(G,sp,'weight') for sp in nx.all_simple_paths(G,(0,1),(len(mp)-1,len(mp[0])-2))]))    