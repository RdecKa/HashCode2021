class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.name = name
        self.length = length
        self.usedByCars = 0

    def __str__(self):
        return f"{self.name}: {self.start} - {self.end} ({self.length}) " + \
            f"[used by {self.usedByCars} cars]"

    @staticmethod
    def fromString(stringInput):
        B, E, name, L = stringInput.split(" ")
        return Street(int(B), int(E), name, int(L))

    def increaseCounterUsedByCars(self):
        self.usedByCars += 1
