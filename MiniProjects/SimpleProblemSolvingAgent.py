from queue import PriorityQueue
import math
import random

# Romania map graph with distances

# dict of dicts OR nested dict OR values of city keys are also dist
romaniaMapGraph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Coordinates for heuristic (straight-line) distance to Bucharest
cityCoordinates = {
    'Arad': (91, 492), 'Bucharest': (400, 327), 'Craiova': (253, 288),
    'Drobeta': (165, 299), 'Eforie': (562, 293), 'Fagaras': (305, 449),
    'Giurgiu': (375, 270), 'Hirsova': (534, 350), 'Iasi': (473, 506),
    'Lugoj': (165, 379), 'Mehadia': (168, 339), 'Neamt': (406, 537),
    'Oradea': (131, 571), 'Pitesti': (320, 368), 'Rimnicu': (233, 410),
    'Sibiu': (207, 457), 'Timisoara': (94, 410), 'Urziceni': (456, 350),
    'Vaslui': (509, 444), 'Zerind': (108, 531)
}


class SimpleProblemSolvingAgent:
    def __init__(self, graph, locations): # constructor
        self.graph = graph
        self.locations = locations
    
    def heuristic(self, city1, city2):
        x1, y1 = self.locations[city1]
        x2, y2 = self.locations[city2]
        return math.hypot(x2 - x1,y2 - y1) # Euclidean distance
    
    def hill_climbing_approach(self, start, goal):
        current = start
        path = []
        path.append(current)

        cost_covered = 0 # total travel cost

        while current != goal:
            neighbours = self.graph[current]
            next_city = None
            current_h = self.heuristic(current, goal)
            best_h = current_h

            for ncity in neighbours:
                new_h = self.heuristic(ncity, goal)
                if new_h < current_h:
                    current_h = new_h
                    next_city = ncity
            
            if next_city is None:
                break

            cost_covered += self.graph[current][next_city]
            path.append(next_city)
            current = next_city

        
        if current == goal: # reached goal
            return path, cost_covered
        else:
            return path, math.inf  # didn't reach goal








    
