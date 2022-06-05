from vpython import *
import math
from src.Model.Molecule import Molecule
from src.Model.MoleculeBuilder import PdbConverter
from src.View.ColorDictionary import ColorDictionary


class Visualizer:

    def __init__(self, molecule: Molecule):
        self.__molecule = molecule
        self.__all_shapes = []
        self.__backbone_shapes = []
        self.__only_backbone = False

    def render(self):
        scene = canvas(title='Protein',
                       width=800, height=600,
                       center=vector(5, 0, 0), background=color.black)

        # scene.bind('mousedown', self.only_backbone)

        button(bind=self.only_backbone, text="Backbone Toggle")

        for a in self.__molecule.get_atoms():

            c = ColorDictionary.color_dic[a.get_element().get_symbol()]
            s = sphere(canvas=scene, pos=vector(a.get_x(), a.get_y(), a.get_z()), color=c,
                       radius=(a.get_element().get_van_der_waals_radius() / 130))
            if "backbone" in a.get_labels():
                self.__backbone_shapes.append(s)
                s.color = color.magenta
            self.__all_shapes.append(s)

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

    def only_backbone(self):
        self.__only_backbone = not self.__only_backbone
        if self.__only_backbone:
            for a in self.__all_shapes:
                if a not in self.__backbone_shapes:
                    a.visible = False
        else:
            for a in self.__all_shapes:
                a.visible = True


def main():
    converter = PdbConverter()
    molecule = converter.pdb_to_molecule("/Users/dimavremenko/Documents/GitHub/Protein-Visualizer/"
                                         "src/Resources/1si4.txt")
    view = Visualizer(molecule)
    view.render()


if __name__ == "__main__":
    main()
