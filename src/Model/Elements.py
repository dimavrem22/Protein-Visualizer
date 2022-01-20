from enum import Enum
from src.Model.Element import Element


class Elements:

    HYDROGEN = Element("H", 1, 1.00797, 2.1, 53, 37, 120)
    CARBON = Element("C", 6, 12.011, 2.5, 67, 77, 170)
    NITROGEN = Element("N", 7, 14.0067, 3.0, 56, 75, 155)
    OXYGEN = Element("O", 8, 15.9994, 3.5, 48, 73, 152)
    FLUORINE = Element("F", 9, 18.998403, 4.0, 42, 71, 147)
    SULFUR = Element("S", 16, 32.06, 2.5, 88, 102, 180)


    def get_element(self, symbol: str):
        if symbol == "H":
            return self.HYDROGEN
        elif symbol == "C":
            return self.CARBON
        elif symbol == "N":
            return self.NITROGEN
        elif symbol == "O":
            return self.OXYGEN
        elif symbol == "F":
            return self.FLUORINE
        elif symbol == "S":
            return self.SULFUR
        else:
            raise ValueError("Invalid Element Symbol")