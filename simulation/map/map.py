from .graph import Graph


class Map:
    _graph: Graph

    def __init__(self, graph: Graph):
        self._graph = graph

    def nodes(self) -> iter:
        for node in self._graph.nodes:
            yield node

    def edges(self) -> iter:
        for edge in self._graph.edges:
            yield edge
