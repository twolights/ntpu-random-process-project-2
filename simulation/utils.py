import matplotlib.pyplot as plt

from simulation.map import Map

MAP_WIDTH, MAP_HEIGHT = 10, 10
MAP_SIZE = MAP_WIDTH, MAP_HEIGHT


def plot_map(m: Map):
    plt.figure(figsize=MAP_SIZE)
    plt.xticks(range(0, MAP_WIDTH))
    plt.xlim(0, MAP_WIDTH)
    plt.yticks(range(0, MAP_HEIGHT))
    plt.ylim(0, MAP_HEIGHT)
    for node in m.nodes():
        plt.plot(node.x, node.y, 'o', color='red')
    for edge in m.edges():
        plt.plot([edge.start.x, edge.end.x], [edge.start.y, edge.end.y], '-', color='blue')
    plt.show()
