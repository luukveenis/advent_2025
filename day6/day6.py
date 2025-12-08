import sys
from functools import reduce
from itertools import groupby

# Turns the input matrix into a list of standard mathematical operations
# ie: [[1, 2], [3, 4], [+, *]] -> ["1 + 2", "3 * 4"]
def build_expressions(input: list[str]) -> list[str]:
    words = [line.split() for line in input]
    transposed = list(zip(*words))
    return [f" {t[-1]} ".join(t[:-1]) for t in transposed]

# Similar to part 1 above, except we need to transpose the characters to
# effectively "rotate" the input 90 degrees counter clockwise
def rtl_expressions(input: list[str]) -> list[str]:
    chars = [list(l) for l in input]
    transposed = list(zip(*chars))[::-1]
    lines = ["".join(l).strip() for l in transposed]

    grouped = groupby(lines, key=lambda x: x == "")
    groups = [list(group) for is_empty, group in grouped if not is_empty]

    expressions = []

    for group in groups:
        operator = group[-1][-1]
        group[-1] = group[-1][:-1]

        expressions.append(f" {operator} ".join(group))

    return expressions

# Take a list of math expressions, evaluate them, and sum the results
def evaluate(expressions: list[str]) -> int:
    return reduce(lambda acc, t: acc + eval(t), expressions, 0)



lines = []

with open(sys.argv[1], "r") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

part1_expressions = build_expressions(lines)
part2_expressions = rtl_expressions(lines)

print(f"Part 1: {evaluate(part1_expressions)}")
print(f"Part 2: {evaluate(part2_expressions)}")

