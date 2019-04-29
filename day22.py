"""AoC 2016: Day 22"""

import pandas as pd

# Part 1

usage = pd.read_csv("./day22_input.txt", header=1, sep=r"\s+")

# Data wrangling
nodes = (
    usage["Filesystem"]
    .str.extract(r"(?P<x>\d+)-y(?P<y>\d+)")
    .astype(int)
    .apply(tuple, axis="columns")
    .rename("node")
)

usage = pd.concat(
    [
        nodes,
        usage.loc[:, "Size":"Avail"]  # type: ignore
        .apply(lambda x: x.str.slice(stop=-1), axis="columns")  # remove trailing T
        .astype("int"),
    ],
    axis="columns",
)

# I want to know the number of couple of nodes A & B such that node A is not
# empty, A != B and used A  is <= Avail B
# I add an extra key to allow for a cartesian product, and then filter_on.

viable_pairs = (
    pd.merge(usage.assign(key=1), usage.assign(key=1), how="outer", on="key")
    .drop("key", axis="columns")
    .query("node_x != node_y")
    .query("Used_x > 0")
    .query("Used_x <= Avail_y")
    .reset_index(drop=True)
)

print(f"Solution for part 1: {len(viable_pairs)}")

# Part 2

usage["category"] = "Average"
usage.loc[usage["Used"] == 0, "category"] = "Empty"
usage.loc[usage["Size"] >= 500, "category"] = "Large"
usage.loc[usage["node"] == (30, 0), "category"] = "Goal"
usage2 = usage.replace({"Empty": "_", "Average": ".", "Large": "#", "Goal": "G"})

for r in usage2.sort_values(by=["y", "x"]).itertuples():
    if r.x == 0:
        print("\n", end="")
    print(r.category, end="")

# All the large nodes are at the same row: 15, making a "wall". The empty node
# is at (13, 27). THe goal is at (30, 0). We need to move it up to just next to
# the goal, and then move the goal by rotating around : swap empty and goal,
# and then move the empty down, left, left and up.

# First, move empty up to the wall
wall_node = usage2.query('category == "#"')["node"].values[0]
empty_node = usage.query('category == "Empty"')["node"].values[0]
moves = empty_node[1] - (wall_node[1] + 1)
current_empty = (empty_node[0], wall_node[1] + 1)

# Then move left to bypass the wall
moves += current_empty[0] - wall_node[0] + 1
current_empty = (wall_node[0] - 1, current_empty[1])

# Then move up to the top
moves += current_empty[1]
current_empty = (current_empty[0], 0)

# Then moves next to the goal, i.e. at position 29
moves += 29 - current_empty[0]
current_empty = (29, 0)

# Next, swap the values around until the goal is at position (0, 0). A swap
# is 5 moves, and it ends with the empty node next to the goal, and the goal
# shifted one value to the left. We need to do it 29 times.
moves += 29 * 5

# And finally, move the goal to node (0, 0)
moves += 1

print(f"Solution for part 2: {moves}")
