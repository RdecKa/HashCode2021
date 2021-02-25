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

        if (self.id != 499):
            maxInterval = min(len(self.incoming) * 1, simulationLength)
            totalWeight = sum(
                [street.usedByCars for street in self.incoming])
            for street in self.incoming:
                if street.usedByCars == 0:
                    continue
                weight = (street.usedByCars / totalWeight) * maxInterval
                weight = min(weight, street.usedByCars)
                # weight = 1
                self.schedule.append((street, math.ceil(weight)))

            # Sort
            self.schedule = sorted(
                self.schedule, key=lambda el: (el[0].numCarsStartingHere, el[0].length), reverse=True)
        else:  # 499
            numStarting0 = []
            numStarting1 = []
            for street in self.incoming:
                if street.numCarsStartingHere == 0:
                    numStarting0.append(street)
                else:
                    numStarting1.append(street)

            self.schedule = []
            numStarting1 = sorted(
                numStarting1, key=lambda el: el.numCarsStartingHere + el.length, reverse=True)
            for street in numStarting1:
                weight = max(street.numCarsStartingHere/2, 1)
                self.schedule.append((street, math.ceil(weight)))

            numStarting0 = sorted(
                numStarting0, key=lambda el: el.length, reverse=False)
            for street in numStarting0:
                weight = 1
                self.schedule.append((street, weight))

    def getScheduleString(self):
        if len(self.schedule) == 0:
            return ""

        s = str(self.id) + "\n"
        s += str(len(self.schedule)) + "\n"
        for el in self.schedule:
            s += el[0].name + " " + str(el[1]) + "\n"
        return s
