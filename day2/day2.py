import sys
import re

def discover_invalid(id_range: str, pattern: str) -> list[int]:
    start, end = id_range.split("-")
    invalid: list[int] = []


    for i in range(int(start), int(end) + 1):
        match = re.search(pattern, str(i))
        if match:
            invalid.append(i)

    return invalid

with open(sys.argv[1], "r") as file:
    part1_result = 0
    part2_result = 0
    input = file.read().strip()

    for id_range in input.split(","):
        part1_result += sum(discover_invalid(id_range, r"^(\d+)\1$"))
        part2_result += sum(discover_invalid(id_range, r"^(\d+)\1+$"))

    print(f"Part one: {part1_result}")
    print(f"Part two: {part2_result}")
