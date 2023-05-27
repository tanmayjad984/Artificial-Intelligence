from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, node):
        self.nodes.add(node)
    
    def add_edge(self, start, end, distance):
        self.edges.setdefault(start, []).append((end, distance))
        self.edges.setdefault(end, []).append((start, distance))



def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def a_star(graph, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}

    g_score  = {start: 0}

    f_score = {start: heuristic(start, goal)}

    while not open_set.empty():

        current = open_set.get()[1]

        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, distance in graph.edges[current]:
            tentative_g_score = g_score[current] + distance

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor]= tentative_g_score
                f_score[neighbor]= tentative_g_score + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))

    return None

graph = Graph()

graph.add_node((0,0))
graph.add_node((1,2))
graph.add_node((2,3))
graph.add_node((3,1))
graph.add_node((4,4))

graph.add_edge((0,0), (1,2), 3)
graph.add_edge((0,0), (2,3), 4)
graph.add_edge((1,2), (3,1), 5)
graph.add_edge((2,3), (4,4), 2)
graph.add_edge((3,1), (4,4), 6)


start = (0,0)
goal = (4,4)
path = a_star(graph, start, goal)

if path:
    print(f"shortest paht from {start} to {goal}:")
    for node in path:
        print(node)
else:
    print(f"No that found from {start} to {goal}.")
