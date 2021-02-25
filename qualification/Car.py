class Car:
    def __init__(self, path, pathLength):
        self.path = path
        self.pathLength = pathLength

    def __str__(self):
        return ", ".join([s.name for s in self.path])

    @staticmethod
    def fromString(stringInput, allStreets: dict):
        streets = stringInput.split(" ")[1:]
        path = []
        length = 0

        for streetName in streets:
            street = allStreets[streetName]
            path.append(street)
            length += street.length

        for streetName in streets:
            street = allStreets[streetName]
            street.increaseCounterUsedByCars(1 / length)

        # Starting street:
        allStreets[streets[0]].increaseCounterStartingHere()

        return Car(path, length)
