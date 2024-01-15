import csv

from .graph import Graph, Node, Edge
from .map import Map, Vehicle


def create_from_csv(nodes_filename: str, edges_filename: str, arrival_rate: float) -> Map:
    _graph = Graph()
    with open(nodes_filename, 'r') as n:
        r = csv.reader(n, delimiter=',')
        for x, y in r:
            _graph.add_node(Node(int(x), int(y)))

    with open(edges_filename, 'r') as e:
        r = csv.reader(e, delimiter=',')
        for start_x, start_y, end_x, end_y, throughput in r:
            start = (int(start_x), int(start_y))
            end = (int(end_x), int(end_y))
            _graph.add_edge_by_location(start, end, int(throughput))
            # _graph.add_edge_by_location(end, start, int(throughput))

    return Map(_graph, arrival_rate)


def simulate(m: Map, iterations: int):
    pass
