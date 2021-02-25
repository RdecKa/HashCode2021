import math


class Intersection:
    def __init__(self, id):
        self.id = id
        self.incoming = []
        self.outgoing = []
        self.schedule = []

    def __str__(self):
        incoming = ", ".join([s.name for s in self.incoming])
        outgoing = ", ".join([s.name for s in self.outgoing])
        return f"In: [{incoming}], Out: [{outgoing}]"

    def addIncoming(self, street):
        self.incoming.append(street)

    def addOutgoing(self, street):
        self.outgoing.append(street)

    def scheduleSimple(self):
        self.schedule = []
        for street in self.incoming:
            self.schedule.append((street.name, 1))

    def scheduleWeighted(self, simulationLength):
        self.schedule = []
        maxInterval = min(len(self.incoming) * 3, simulationLength)
        totalWeight = sum(
            [street.usedByCarsWeighted for street in self.incoming])
        for street in self.incoming:
            if street.usedByCars == 0:
                continue
            weight = (street.usedByCarsWeighted / totalWeight) * maxInterval
            weight = min(weight, street.usedByCars)
            self.schedule.append((street, math.ceil(weight)))

        # Sort
        self.schedule = sorted(
            self.schedule, key=lambda el: el[0].numCarsStartingHere)

    def getScheduleString(self):
        if len(self.schedule) == 0:
            return ""

        s = str(self.id) + "\n"
        s += str(len(self.schedule)) + "\n"
        for el in self.schedule:
            s += el[0].name + " " + str(el[1]) + "\n"
        return s
