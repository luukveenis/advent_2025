import sys
import re

def discover_invalid(id_range: str) -> list[int]:
    start, end = id_range.split("-")
    invalid: list[int] = []


    for i in range(int(start), int(end) + 1):
        match = re.search(r"^(\d+)\1$", str(i))
        if match:
            invalid.append(i)

    return invalid

with open(sys.argv[1], "r") as file:
    result = 0
    input = file.read().strip()

    for id_range in input.split(","):
        result += sum(discover_invalid(id_range))

    print(f"Part one: {result}")
