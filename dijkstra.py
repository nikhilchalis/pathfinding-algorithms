from setup import *

EDGE_DISTANCE = 1

'''
Pseudocode

procedure Dijkstra(G, s)
    for each vertex v in G
        dist[v] := infinity
        prev[v] := nil
    dist[s] := 0
    Q := {s}
    while Q is not empty
        u := vertex in Q with minimum dist[u]
        remove u from Q
        for each vertex v adjacent to u
            if dist[v] > dist[u] + weight(u, v)
                dist[v] := dist[u] + weight(u, v)
                prev[v] := u
'''

def dijkstra(screen, grid, start, end):
    # initialising
    
    priority_Q = []
    distances = [] # this array will return the distance and path from each 
    for row in grid:
        for node in row:
            node.distance = float('inf')
            node.previous = None
            priority_Q.append(node)
    start.distance = 0

    priority_Q.append(start)

    while len(priority_Q):
        u_node = min(priority_Q, key=lambda node: node.distance)
        if u_node == end:
            break
        u_node.change_state('search')
        display_grid(screen, grid)
        pg.display.update()
        priority_Q.remove(u_node)

        u_node.update_neighbours(grid)
        u_neighbours = u_node.neighbours

        for neighbour in u_neighbours:
            if neighbour.distance > u_node.distance + EDGE_DISTANCE:
                neighbour.distance = u_node.distance + EDGE_DISTANCE
                neighbour.previous = u_node
        
        print('here')

    '''
    for row in grid:
        for node in row:
            if node.row == start.row:
                node.change_state('search')
                display_grid(screen, grid)
                pg.display.update()
    '''
    






    

            
