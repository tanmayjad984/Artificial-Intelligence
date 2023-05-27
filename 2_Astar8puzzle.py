
from queue import PriorityQueue

goal_state = ((1,2,3),(4,5,6),(7,8,0))

def heuristic(state):
    distance = 0 
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_row = (value - 1) // 3
                goal_col = (value - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    
    return distance




def get_successors(state):
    
    successors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:

                if j>0:
                    new_state = list(map(list, state))
                    new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
                    successors.append(tuple(map(tuple, new_state)))

                if j<2:
                    new_state = list(map(list, state))
                    new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
                    successors.append(tuple(map(tuple,new_state)))

                if i>0:
                    new_state = list(map(list, state))
                    new_state[i][j], new_state[i-1][j] = new_state[i-1][j] ,new_state[i][j]
                    successors.append(tuple(map(tuple, new_state)))

                if i<2:
                    new_state = list(map(list, state))
                    new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
                    successors.append(tuple(map(tuple, new_state)))

    return successors


def astar(initial_state):

    open_set = PriorityQueue()
    open_set.put((0, initial_state))

    came_from = {}

    g_score = {initial_state: 0}

    f_score = {initial_state: heuristic(initial_state)}

    while not open_set.empty():

        current_state = open_set.get()[1]

        if current_state == goal_state:

            path = []

            while current_state in came_from:
                 
                 path.append(current_state)
                 current_state= came_from[current_state]
            path.append(initial_state)
            path.reverse()
            
            return path

        for successor in get_successors(current_state):
            g = g_score[current_state] + 1
            
            if successor not in g_score or g < g_score[successor]:
                came_from[successor] = current_state
                g_score[successor] = g
                f = g + heuristic(successor)
                f_score[successor] = f
                open_set.put((f, successor))
                
    return None

initial_state = ((4,1,3), (7,2,5), (0,8,6))
path = astar(initial_state)

if path:
    print("Solution Found!")
    for state in path: 
        for row in state:
            print(row)

        print()
else:
    print("No solution found")

