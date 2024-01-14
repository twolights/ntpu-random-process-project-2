from simulation import map
from simulation import utils


def main():
    da_map = map.create_from_csv('../input/nodes.csv', '../input/edges.csv')
    utils.plot_map(da_map)


if __name__ == '__main__':
    main()
