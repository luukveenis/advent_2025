import sys
from functools import reduce

# Turns the input matrix into a list of standard mathematical operations
# ie: [[1, 2], [3, 4], [+, *]] -> ["1 + 2", "3 * 4"]
def build_expressions(input: list[list[str]]) -> list[str]:
    transposed = list(zip(*input))
    return [f" {t[-1]} ".join(t[:-1]) for t in transposed]


lines = []

with open(sys.argv[1], "r") as file:
    for line in file:
        lines.append(line.strip().split())

expressions = build_expressions(lines)
part1_result = reduce(lambda acc, t: acc + eval(t), expressions, 0)

print(f"Part 1: {part1_result}")

