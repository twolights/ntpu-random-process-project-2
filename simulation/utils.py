import matplotlib.pyplot as plt
from labellines import labelLines

from simulation.map import Map, Node, Edge

MAP_WIDTH, MAP_HEIGHT = 8, 9
MAP_SIZE = 16, 10


def plot_node(node: Node, color: str, marker_size: int):
    plt.plot(node.x, node.y, 'o', color=color, markersize=marker_size)


def plot_edge(edge: Edge, color: str):
    x = edge.start.x, edge.end.x
    y = edge.start.y, edge.end.y
    label = f"{edge.load}/{edge.throughput}"
    plt.plot(x, y, '-', color=color, label=label)


def plot_map(m: Map, show: bool = True):
    plt.figure(figsize=MAP_SIZE)
    plt.xticks(range(0, MAP_WIDTH))
    plt.xlim(0, MAP_WIDTH)
    plt.yticks(range(0, MAP_HEIGHT))
    plt.ylim(0, MAP_HEIGHT)
    plt.tight_layout()
    for node in m.nodes():
        plot_node(node, color='red', marker_size=20)
    for edge in m.edges():
        plot_edge(edge, color='black')
    lines = labelLines(plt.gca().get_lines(), zorder=2.5)
    if show:
        plt.show()
