class ElementБасимова:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def dump(self):
        print(f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}")

phosphor = ElementБасимова("Helium", "H", 2)
phosphor.dump()
