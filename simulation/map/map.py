from typing import List, Optional, Tuple
import heapq

import numpy as np

from .graph import Edge, Node, Graph


class Vehicle:
    start: Node
    current: Node
    end: Node
    next_hop_edge: Optional[Edge]

    def __init__(self, start: Node, end: Node):
        self.start = start
        self.current = start
        self.end = end
        self.next_hop_edge = None


class TrafficGenerator:
    _graph: Graph
    _generator: np.random.Generator
    _lambda: float

    def __init__(self, graph: Graph, arrival_rate: float):
        self._graph = graph
        self._generator = np.random.default_rng()
        self._lambda = arrival_rate

    def generate_single(self) -> Vehicle:
        choices = self._generator.choice(self._graph.nodes, 2, replace=False)
        start, end = choices[0], choices[1]
        return Vehicle(start, end)

    def generate(self) -> iter:
        num_vehicles = self._generator.poisson(self._lambda)
        for i in range(num_vehicles):
            yield self.generate_single()


class Map:
    _graph: Graph
    _arrival_rate: float
    _vehicles: List[Vehicle]
    _traffic_generator: TrafficGenerator

    def __init__(self, graph: Graph, arrival_rate: float):
        self._graph = graph
        self._arrival_rate = arrival_rate
        self._traffic_generator = TrafficGenerator(graph, arrival_rate)

    def nodes(self) -> iter:
        for node in self._graph.nodes:
            yield node

    def edges(self) -> iter:
        for edge in self._graph.edges:
            yield edge

    def plan_route_for(self, vehicle: Vehicle):
        # Dijkstra's routing algorithm
        weights = {node: float('inf') for node in self.nodes()}
        weights[vehicle.start] = 0

        visited = set()
        previous = {node: None for node in self.nodes()}

        while len(visited) < self._graph.total_nodes():
            current_node = min(
                (node for node in self.nodes() if node not in visited),
                key=lambda node: weights[node]
            )
            visited.add(current_node)

            for edge in current_node.outgoing_edges:
                neighbor = edge.end
                new_weight = weights[current_node] + edge.weight()
                if new_weight < weights[neighbor]:
                    weights[neighbor] = new_weight
                    previous[neighbor] = current_node

        path = []
        current_node = vehicle.end
        while current_node != vehicle.start:
            path.append(current_node)
            current_node = previous[current_node]
        path.append(vehicle.start)
        path.reverse()
        return path

    def _find_next_hop_edge(self, vehicle: Vehicle) -> Tuple[Node, Edge]
        path = self.plan_route_for(vehicle)
        next_hop = path[1]
        if vehicle.next_hop_edge is not None:
            vehicle.next_hop_edge.load -= 1
        for edge in vehicle.current.outgoing_edges:
            if edge.end == next_hop:
                edge.load +=1
                return next_hop, edge
        raise Exception("Next hop edge not found")

    def _next_iteration(self):
        for vehicle in self._vehicles:
            if vehicle.current == vehicle.end:
                self._vehicles.remove(vehicle)
                continue
            next_hop, edge = self._find_next_hop_edge(vehicle)
        for vehicle in self._traffic_generator.generate():
            self._vehicles.append(vehicle)

    def simulate(self, iterations: int):
        for i in range(iterations):
            self._next_iteration()
