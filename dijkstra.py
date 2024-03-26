from setup import *

EDGE_DISTANCE = 1

def dijkstra(grid, start):
    Q = []
    for node in start.neighbours:
        node.distance = float('inf')
        node.previous = None
