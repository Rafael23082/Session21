class foodRA:

    def __init__(self,name,pounds):
        self.name=name
        self.pounds=pounds
        self.__price=(self.__pricelist())
        self.__total=(self.__total())

    def __pricelist(self):
        if self.name == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.name == "Wagyu Steaks":
            self.__price = 450.00
        elif self.name == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.name == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.name == "Moose Cheese":
            self.__price = 487.20
        elif self.name == "White Truffles":
            self.__price = 3600.00
        elif self.name == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.name == "La Bonnotte Potatoes":
            self.__price = 270.81
        else:
            self.__price = 0.0

    def total(self):
        return self.pounds*self.__price