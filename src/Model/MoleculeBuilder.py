from src.Model.Atom import Atom
from src.Model.Elements import Elements
from src.Model.Molecule import Molecule


class PdbConverter:

    def pdb_to_molecule(self, file_path):
        f = open(file_path, "r")
        contents = f.readlines()

        molecule = Molecule()

        for line in contents:
            line = line.replace("-", " -")
            line = line.split()
            if len(line) != 0 and line[0] == "ATOM":
                if line[-1] != "H":
                    e = Elements()
                    element = e.get_element(line[-1])
                    a = Atom(int(line[1]), element, float(line[6]), float(line[7]), float(line[8]))
                    a.add_label(line[2])
                    a.add_label(line[3])
                    molecule.add_atom(a, [])
                    if line[2] in "ONCA":
                        a.add_label("backbone")
        return molecule
