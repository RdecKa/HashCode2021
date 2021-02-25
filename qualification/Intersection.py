class Intersection:
    def __init__(self):
        self.incoming = []
        self.outgoing = []

    def __str__(self):
        incoming = ", ".join([s.name for s in self.incoming])
        outgoing = ", ".join([s.name for s in self.outgoing])
        return f"In: [{incoming}], Out: [{outgoing}]"

    def addIncoming(self, street):
        self.incoming.append(street)

    def addOutgoing(self, street):
        self.outgoing.append(street)
