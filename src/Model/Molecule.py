from src.Model.Atom import Atom


class Molecule:

    def __init__(self, atoms: [Atom] = None, bonds: [()] = None):
        if atoms is None:
            self.__atoms = []
            self.__bonds = []
        else:
            self.__atoms = atoms
            if bonds is None:
                self.bonds = []
            else:
                self.bonds = bonds

    def get_atoms(self):
        # TODO return copies of atoms
        return self.__atoms

    def get_bonds(self):
        # TODO return copy of bonds list
        return self.__bonds

    def add_atom(self, atom: Atom, bonded: []):
        self.__atoms.append(atom)
        for i in bonded:
            self.__bonds.append((atom.get_id(), i))

    def remove_atom(self, idt: int):
        # TODO implement 2 pointer algorithm
        for a in self.__atoms:
            if a.get_idt == idt:
                self.__atoms.remove(a)
                break
        for b in self.__bonds:
            if idt in b:
                self.__bonds.remove(b)
