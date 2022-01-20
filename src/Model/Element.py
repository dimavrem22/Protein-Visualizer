class Element:

    def __init__(self, symbol: str, atomic_number: int, avg_mass: float, en: float, atomic_radius: int,
                 covalent_radius: int, van_der_waals_radius: int):
        self.__symbol = symbol
        self.__atomic_number = atomic_number
        self.__avg_mass = avg_mass
        self.__electronegativity = en
        self.__atomic_radius = atomic_radius
        self.__covalent_radius = covalent_radius
        self.__van_der_waals_radius = van_der_waals_radius

    def get_symbol(self):
        return self.__symbol

    def get_atomic_number(self):
        return self.__atomic_number

    def get_avg_mass(self):
        return self.__avg_mass

    def get_electronegativity(self):
        return self.__symbol

    def get_atomic_radius(self):
        return self.__atomic_radius

    def get_covalent_radius(self):
        return self.__covalent_radius

    def get_van_der_waals_radius(self):
        return self.__van_der_waals_radius

    #
    # def get_max_valency(self):
    #     return self.__max_valency
