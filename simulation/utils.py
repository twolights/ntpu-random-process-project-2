import matplotlib.pyplot as plt
from labellines import labelLines

from simulation.map import Map

MAP_WIDTH, MAP_HEIGHT = 12, 10
MAP_SIZE = 16, 10


def plot_map(m: Map):
    plt.figure(figsize=MAP_SIZE)
    plt.xticks(range(0, MAP_WIDTH))
    plt.xlim(0, MAP_WIDTH)
    plt.yticks(range(0, MAP_HEIGHT))
    plt.ylim(0, MAP_HEIGHT)
    plt.tight_layout()
    for node in m.nodes():
        plt.plot(node.x, node.y, 'o', color='red', markersize=20)
    for edge in m.edges():
        x = edge.start.x, edge.end.x
        y = edge.start.y, edge.end.y
        label = f"{edge.load}/{edge.throughput}"
        plt.plot(x, y, '-', color='blue', label=label)
    lines = labelLines(plt.gca().get_lines(), zorder=2.5)
    plt.show()
