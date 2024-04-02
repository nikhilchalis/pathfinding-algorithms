from setup import *
import pygame as pg
import numpy as np

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

def astar(screen, grid, start, end, search_aggression=1):
    # initialising
    clock = pg.time.Clock()
    priority_Q = []
    visited = set()
    for row in grid:
        for node in row:
            if not node.is_barrier() and not node.is_none():
                node.distance = float('inf')
                node.previous = None
                priority_Q.append(node)
    start.distance = 0

    priority_Q.append(start)
    # FOR DEBUGGING
    # u_node = min(priority_Q, key=lambda node: node.distance)
    # u_node.update_neighbours(grid)


    
    while len(priority_Q):
        u_node = min(priority_Q, key=lambda node: node.distance)
        if u_node.state != 'start' and u_node.state != 'end':
            u_node.change_state('current')
            u_node.draw(screen)
        priority_Q.remove(u_node)
        visited.add(u_node)

        if u_node == end:
            break
        u_node.update_neighbours(grid)

        for neighbour in u_node.neighbours:
            if neighbour not in visited:
                if neighbour is not end:
                    neighbour.change_state('search')
                neighbour.draw(screen)
                #display_grid(screen, grid)
                pg.display.update()
                h_distance = heurisic(neighbour, end, aggression=search_aggression)
                if neighbour.distance > u_node.distance + EDGE_DISTANCE + h_distance:
                    neighbour.distance = u_node.distance + EDGE_DISTANCE + h_distance
                    neighbour.previous = u_node
        
       #clock.tick(FPS)

    if end.previous == None:
        print('no path found')
    else:
        prev = end.previous
        path = []
        path.append(prev)
        while prev != start:
            prev.change_state('path')
            prev = prev.previous
            path.append(prev)
    

    
def heurisic(node, destination, aggression=1):
    if aggression == 1:
        distance = np.sqrt((node.x - destination.x)**2 + (node.y - destination.y)**2)
    elif aggression == 2:
        distance = (node.x - destination.x)**2 + (node.y - destination.y)**2
    elif aggression == 3:
        distance = ((node.x - destination.x)**2 + (node.y - destination.y)**2)**2
    
    return distance





    

            
