from math import prod
from time import perf_counter

from typing import Iterator


def parse_input():
    with open("./data/day8.txt") as file:
        return [[int(c) for c in line.strip()] for line in file]


def is_visible(tree:int, tree_lines) -> bool:
    return any(tree>max(tree_line,default=-1) for tree_line in tree_lines)


def trees_in_sight(tree:int, tree_line) -> bool:
    return next((dist for dist, next_tree in enumerate(tree_line, start=1) \
                 if next_tree>=tree), len(tree_line))


def scenic_score(tree:int, tree_lines) -> int:
    return prod(trees_in_sight(tree, tree_line) for tree_line in tree_lines)


def solutions() -> Iterator[int]:
    forrest = parse_input()
    translated_forrest = list(zip(*forrest))

    visible_tree_count = 0
    max_scenic_score = 0
    for row, tree_row in enumerate(forrest):
        for col, tree_col in enumerate(translated_forrest):
            tree = tree_col[row]
            tree_lines = (tree_row[:col][::-1], tree_row[col+1:],
                          tree_col[:row][::-1], tree_col[row+1:])

            visible_tree_count += is_visible(tree, tree_lines)

            sc = scenic_score(tree, tree_lines)
            max_scenic_score = max(max_scenic_score, sc)
    yield visible_tree_count
    yield max_scenic_score


answer = solutions()

t0 = perf_counter()
print("Answer 1:",next(answer))
print("Answer 2:",next(answer))
print(f"Executed in {perf_counter()-t0:.2f} s")