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
