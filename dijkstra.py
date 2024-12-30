from heapq import *
import copy
import math  # for math.inf

###############################################################################
def printAdjacency(adjacency: list[ list[int] ]) -> None:
    ''' prints an adjacency matrix in easy-to-read format
    Parameters:
        adjacency: a 2D list of edge weights for a graph
    '''
    print("     ", end = "")
    for col in range(len(adjacency)):
        print(f"{(col + 1):>3} ", end = '')
    print('\n    ', end = '')
    print('----' * len(adjacency))
    for row in range(len(adjacency)):
        print(f"{(row + 1):>3} |", end = '')
        for col in range(len(adjacency[row])):
            value = adjacency[row][col]
            if value == math.inf: value = "∞"
            print(f"{value:>3} ", end = '')
        print()
    print('    ', end = '')
    print('----' * len(adjacency))

###############################################################################
def dijkstra(adjacency: list[ list[int] ], start: int, dest: int) -> tuple[int, list[int]]:
    ''' implements Dijkstra's algorithm on the graph represented by the given
        2D adjacency matrix, finding the shortest path from vertex with index
        start to vertex with index dest, returning the cost/distance of that
        shortest path
    Args:
        adjacency: a 2D adjacency matrix representing the graph, with entries
                    corresponding to edge weights
        start: the index (between 0 and # vertices - 1) of the origin
        dest:  the index (between 0 and # vertices - 1) of the destination
    Returns:
        a tuple consisting of:
            - the length of the shortest path from start to dest
            - a list of vertices on the shortest path, from start to dest
    '''
    v = len(adjacency)  
    d = [math.inf] * v
    d[start] = 0
    U = {start}  
    u = start

    #path reconstruction to length of v
    prev = [math.inf] * v
    
    while u != dest: #stop once destination vertex is added
        for vi in range(v):
            if vi not in U and adjacency[u][vi] != math.inf:
                if d[u] + adjacency[u][vi] < d[vi]: #min calculation
                    d[vi] = d[u] + adjacency[u][vi]
                    prev[vi] = u #for path constrution
        
        #find next closest vertex
        min_dist = math.inf
        for vi in range(v): #consider only unvisited verticies
            if vi not in U and d[vi] < min_dist:
                u = vi
                min_dist = d[vi]
        if u == -1: #no reachable vertices left
            break

        U.add(u)

    #reconstruct path, start to dest
    path = []
    if d[dest] != math.inf:  
        while dest != math.inf:
            path.append(dest)
            dest = prev[dest]
        path.reverse()

    return d[path[-1]], path


###############################################################################
def showPath(path: list[int]) -> None:
    ''' function to display the results of a (presumably shortest) path using
        the integer vertices in the given list
    Parameters:
        path: a list of integers corresponding to, in order, vertices on the
            path; presumes that given vertices are in [0, # vertices - 1]
    '''
    result = ""
    for index in path:
        result += f"v{index + 1}->"
    result = result[:-2]  # trim last "->"
    print('\t' + result)
    print()

###############################################################################
def main() -> None:
    num_vertices = 6
    # build a 2D adjacency matrix for 6 vercies, with undirected edges
    # having weights shown below
    adj = [[math.inf] * num_vertices for i in range(num_vertices)]
    adj[0][1] = adj[1][0] = 7
    adj[0][3] = adj[3][0] = 2
    adj[1][2] = adj[2][1] = 2
    adj[1][4] = adj[4][1] = 3
    adj[2][5] = adj[5][2] = 4
    adj[3][4] = adj[4][3] = 1
    adj[4][5] = adj[5][4] = 10

    printAdjacency(adj)
    start = input("Enter a starting vertex ('q' to quit): ")
    while len(start) > 0 and start[0].lower() != 'q':
        end = input("Enter a destination vertex ('q' to quit): ")
        if len(end) > 0 and end[0].lower() == 'q': break
        try:
            start = int(start) - 1
            end   = int(end) - 1
            if 0 <= start < num_vertices and \
               0 <= end   < num_vertices:
                distance, path = dijkstra(adj, start, end)
                print(f"\nThe shortest path from {start + 1} to {end + 1} is length {distance}")
                showPath(path)
            else:
                print(f"Invalid indices: {start}, {end}")
        except:
            pass
        start = input("Enter a starting vertex ('q' to quit): ")
 
 
if __name__ == "__main__":
    main()
    
