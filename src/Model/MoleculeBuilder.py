from src.Model.Atom import Atom
from src.Model.Elements import Elements
from src.Model.Molecule import Molecule


class PdbConverter:

    def pdb_to_molecule(self, file_path):
        f = open(file_path, "r")
        contents = f.readlines()

        molecule = Molecule()

        for line in contents:
            line = line.split()
            if line[0] == "ATOM":

                e = Elements()
                element = e.get_element(line[-1])
                a = Atom(int(line[1]), element, float(line[6]), float(line[7]), float(line[8]))
                a.add_label(line[2])
                a.add_label(line[3])
                molecule.add_atom(a, [])
                if line[2] in "ONCA":
                    a.add_label("backbone")

        return molecule

    def pdb_normalized(self, filepath):
        f = open(filepath, "r")
        contents = f.read()
        f.close()

        contents = contents.replace("-", " -")
        f = open(filepath, "w")
        f.truncate()
        f.write(contents)
        f.close()
