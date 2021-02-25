class Car:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return ", ".join([str(s) for s in self.path])

    @staticmethod
    def fromString(stringInput, allStreets: dict):
        streets = stringInput.split(" ")[1:]
        path = []
        for streetName in streets:
            path.append(allStreets[streetName])
        return Car(path)
