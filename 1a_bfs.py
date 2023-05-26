from queue import Queue

adj_list = {
    "1": ["2","3"],        # Define the tree
    "2": ["4"],
    "3": ["2"],
    "4": ["3"]
}

visited = {}       # Initialised to track the visisted node and their nodes.
parent = {} 
bfs_trav_out = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False   #each value is set to False to indicate that no nodes have been visited yet. 
    parent[node] = None    # The parent dictionary is initialized with all nodes as keys, and their values are set to None.

# source node is declared below.
# The source_node variable is set to the starting node for the BFS traversal. In this case, it is set to "1".
source_node = "1"
visited[source_node] = True
queue.put(source_node)

while not queue.empty():
    u = queue.get()
    bfs_trav_out.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            queue.put(v)

print(bfs_trav_out)
        
    