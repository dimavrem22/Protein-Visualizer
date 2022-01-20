from vpython import *
import math
from src.Model.Molecule import Molecule
from src.Model.MoleculeBuilder import PdbConverter
from src.View.ColorDictionary import ColorDictionary


class Visualizer:

    def __init__(self, molecule: Molecule):
        self.__molecule = molecule

    def render(self):
        scene = canvas(title='Protein',
                   width=800, height=800,
                   center=vector(5, 0, 0), background=color.black)

        # scene.bind('mousedown', self.process)

        for a in self.__molecule.get_atoms():
            if "backbone" in a.get_labels():
                c = color.magenta
            else:
                c = ColorDictionary.color_dic[a.get_element().get_symbol()]
            sphere(canvas=scene, pos=vector(a.get_x(), a.get_y(), a.get_z()), color=c,
                   radius=(a.get_element().get_van_der_waals_radius()/130))

    # def process(self, ev):
    #     x = ev.pos.x
    #     y = ev.pos.y
    #     z = ev.pos.z
    #     print(ev.event, ev.which, x, y, z)
    #     print(self.find_closest_atom(x, y, z).get_labels())

    def find_closest_atom(self, x, y, z):
        min_dist = math.inf
        result = 0
        for a in self.__molecule.get_atoms():
            dist = math.sqrt((x - a.get_x()) ** 2 + (y - a.get_y()) ** 2 + (z - a.get_z()) ** 2)
            if dist < min_dist:
                result = a
                min_dist = dist
        return result



def main():
    converter = PdbConverter()
    # converter.pdb_normalized("/Users/dimavremenko/PycharmProjects/Molecules/src/Resources/2os3.txt")
    molecule = converter.pdb_to_molecule("/Users/dimavremenko/PycharmProjects/Molecules/src/Resources/2os3.txt")
    v = Visualizer(molecule)
    v.render()


if __name__ == "__main__":
    main()
