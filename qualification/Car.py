class Car:
    def __init__(self, path, pathLength):
        self.path = path
        self.pathLength = pathLength

    def __str__(self):
        return ", ".join([s.name for s in self.path])

    @staticmethod
    def fromString(stringInput, allStreets: dict, simulationDuration):
        streets = stringInput.split(" ")[1:]
        path = []
        length = 0

        for i, streetName in enumerate(streets):
            street = allStreets[streetName]
            path.append(street)
            if i > 0:  # Car starts at the END of first street
                length += street.length

        if length <= simulationDuration:
            for streetName in streets:
                street = allStreets[streetName]
                street.increaseCounterUsedByCars(1 / length)

        # Starting street:
        allStreets[streets[0]].increaseCounterStartingHere()

        return Car(path, length)
