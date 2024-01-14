from typing import List, Optional
import heapq

import numpy as np

from .graph import Edge, Node, Graph


class Vehicle:
    _start: Node
    _current: Node
    _end: Node
    _next_hop_edge: Optional[Edge]

    def __init__(self, start: Node, end: Node):
        self._start = start
        self._current = start
        self._end = end
        self._next_hop_edge = None


class TrafficGenerator:
    _graph: Graph
    _generator: np.random.Generator
    _lambda: float

    def __init__(self, graph: Graph, arrival_rate: float):
        self._graph = graph
        self._generator = np.random.default_rng()
        self._lambda = arrival_rate

    def generate(self) -> iter:
        num_vehicles = self._generator.poisson(self._lambda)
        for i in range(num_vehicles):
            start = np.random.choice(self._graph.nodes)
            end = np.random.choice(self._graph.nodes)
            while start == end:
                end = np.random.choice(self._graph.nodes)
            yield Vehicle(start, end)


class Map:
    _graph: Graph
    _arrival_rate: float
    _vehicles: List[Vehicle]

    def __init__(self, graph: Graph, arrival_rate: float):
        self._graph = graph
        self._arrival_rate = arrival_rate

    def nodes(self) -> iter:
        for node in self._graph.nodes:
            yield node

    def edges(self) -> iter:
        for edge in self._graph.edges:
            yield edge

    def plan_route_for(self, vehicle: Vehicle):
        # Dijkstra's routing algorithm
        weights = {node: float('inf') for node in self.nodes()}
        weights[vehicle._start] = 0

        pq = [(0, vehicle._start)]
        while pq:
            current_weight, current_node = heapq.heappop(pq)
            if current_weight > weights[current_node]:
                continue

            for edge in current_node.outgoing_edges:
                neighbor = edge.end
                distance = current_weight + edge.weight()

                if distance < weights[neighbor]:
                    weights[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        path = []
        current_node = vehicle._end
        while current_node != vehicle._start:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path.append(vehicle._start)
        path.reverse()
        return path
