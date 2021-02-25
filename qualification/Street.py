class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.name = name
        self.length = length

    def __str__(self):
        return f"{self.name}: {self.start} - {self.end} ({self.length})"

    @staticmethod
    def fromString(stringInput):
        B, E, name, L = stringInput.split(" ")
        return Street(int(B), int(E), name, int(L))
