
adj_list = {
    "1": ["2","3"],
    "2": ["4"],
    "3": ["2"],
    "4": ["3"]
}

color = {}
parent = {}
dfs_trav_out = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    
def dfs(u):
    color[u] = "G"
    dfs_trav_out.append(u)
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs(v)
    color[u] = "B"


dfs("3")

print(dfs_trav_out)




    


