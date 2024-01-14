from __future__ import annotations

from typing import List, Dict, Tuple


class Graph:
    nodes: List[Node]
    edges: List[Edge]
    nodes_map: Dict[Tuple[int, int], Node]

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.nodes_map = {}

    def add_node(self, node: Node):
        self.nodes_map[(node.x, node.y)] = node
        self.nodes.append(node)

    def add_edge_by_nodes(self, start: Node, end: Node, throughput: int):
        edge = Edge(start, end, throughput)
        self.edges.append(edge)
        start.outgoing_edges.append(edge)

    def add_edge_by_location(self, start: Tuple[int, int], end: Tuple[int, int], throughput: int):
        self.add_edge_by_nodes(self.nodes_map[start], self.nodes_map[end], throughput)


class Node:
    x: int
    y: int
    outgoing_edges: List[Edge]

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.outgoing_edges = []

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Node{str(self)}"


class Edge:
    start: Node
    end: Node
    throughput: int
    load: int

    def __init__(self, start: Node, end: Node, throughput: int):
        self.start = start
        self.end = end
        self.throughput = throughput
        self.load = 0

    def weight(self) -> float:
        if self.throughput == self.load:
            return float("inf")
        return 1 / (self.throughput - self.load)

    def __str__(self):
        return f"{self.start} -> {self.end} ({self.throughput})"

    def __repr__(self):
        return f"Edge{str(self)}"
