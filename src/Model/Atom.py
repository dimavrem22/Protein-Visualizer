from src.Model.Element import Element


class Atom:

    def __init__(self, idt: int, e: Element, x: float, y: float, z: float):
        self.__idt = idt
        self.__element = e
        self.__x = x
        self.__y = y 
        self.__z = z
        self.__labels = []

    def get_id(self):
        return self.__idt

    def get_element(self):
        return self.__element

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def get_labels(self):
        # TODO return copy
        return self.__labels

    def add_label(self, label: str):
        self.__labels.append(label)

    def remove_label(self, label: str):
        if label in self.__labels:
            self.__labels.remove(label)
