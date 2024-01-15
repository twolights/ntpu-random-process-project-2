import matplotlib.pyplot as plt

from simulation import map
from simulation import utils

LAMBDA = 0.1


def main():
    da_map = map.create_from_csv('../input/sample-nodes.csv', '../input/sample-edges.csv', LAMBDA)
    da_map.simulate(1000)
    '''
    utils.plot_map(da_map, show=False)
    path = da_map.plan_route_for(vehicle)
    for node in path:
        utils.plot_node(node, color='black', marker_size=20)
    utils.plot_node(vehicle.start, color='blue', marker_size=20)
    utils.plot_node(vehicle.end, color='orange', marker_size=20)
    plt.show()
    '''


if __name__ == '__main__':
    main()
