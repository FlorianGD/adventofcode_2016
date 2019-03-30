"""AoC 2016 Day 13"""

from itertools import product
from typing import Tuple

import networkx as nx

# Part 1

INPUT = 1350

test_input = 10


def compute_layout(x: int, y: int, num: int) -> int:
    """Return 0 for open, 1 for wall"""
    formula = x*(x + 3 + 2 * y) + y*(1 + y) + num
    binary = format(formula, 'b')
    result = sum(int(i) for i in binary) % 2
    return result % 2


def build_graph(xmax: int, ymax: int, num: int) -> nx.Graph:
    open_nodes = set()
    G = nx.Graph()
    # Find open nodes
    for x, y in product(range(xmax), range(ymax)):
        if compute_layout(x, y, num) == 0:
            open_nodes.add((x, y))
    G.add_nodes_from(open_nodes)
    # Find neighbors that are open
    for x, y in sorted(list(open_nodes)):
        if (x+1, y) in open_nodes:
            G.add_edge((x, y), (x+1, y))
        if (x, y+1) in open_nodes:
            G.add_edge((x, y), (x, y+1))
    return G, open_nodes


def len_shortest_path(G: nx.Graph, end: Tuple[int]) -> int:
    return len(nx.shortest_path(G, (1, 1), end)) - 1


# fewest number of steps required for you to reach 31,39
G, nodes = build_graph(80, 80, INPUT)
print(f'Solution for part 1: {len_shortest_path(G, (31, 39))}')

# Part 2
# How many locations (distinct x,y coordinates, including your starting
# location) can you reach in at most 50 steps?

total = 0
for node in nodes:
    try:
        if len_shortest_path(G, node) <= 50:
            total += 1
    except nx.NetworkXNoPath:
        pass
print(f'Solution for part 2: {total}')
