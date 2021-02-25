class Car:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return ", ".join([s.name for s in self.path])

    @staticmethod
    def fromString(stringInput, allStreets: dict):
        streets = stringInput.split(" ")[1:]
        path = []
        for streetName in streets:
            street = allStreets[streetName]
            path.append(street)
            street.increaseCounterUsedByCars()

        # Starting street:
        allStreets[streets[0]].increaseCounterStartingHere()

        return Car(path)
