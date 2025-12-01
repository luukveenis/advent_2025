class Lock:
    def __init__(self):
        self.position: int = 50

    def rotate(self, op: str) -> int:
        count = int(op[1:])
        adjustment = count if op[0] == "R" else -count

        self.position = (self.position + adjustment) % 100
        return self.position


lock = Lock()

with open("input.txt", "r") as file:
    positions: list[int] = []

    for line in file:
        positions.append((lock.rotate(line.strip())))

    print(positions.count(0))
