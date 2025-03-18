class Bus:
    def __init__(self, number, RKey, Driver):
        self.number = number
        self.RKey = RKey
        self.Driver = Driver


class Company:
    def __init__(self, Bus, max_bus):
        self.Bus = Bus
        self.max_bus = max_bus
        self.Buses = []

    def add_bus(self, Bus):
        if len(self.Buses) < self.max_bus:
            self.Buses.append(Bus)
            return True
        return False

Bus1 = Bus("2010", "Y", "Greg")
Bus2 = Bus("2001", "P", "Tom")
Bus3 = Bus("2020", "130", "Peter")
Bus4 = Bus("2009", "P", "Rile")

Company1 = Company("Bus Company", 3)

Company1.add_bus(Bus1)
Company1.add_bus(Bus2)
Company1.add_bus(Bus3)
Company1.add_bus(Bus4)


for Bus in Company1.Buses:
    print(Bus.number, Bus.RKey, Bus.Driver)