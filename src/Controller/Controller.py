from src.Model.Molecule import Molecule
from src.View.Visualizer import Visualizer


class Controller:

    def __init__(self, molecule: Molecule, view: Visualizer):
        self.__molecule = molecule
        self.__visualizer = view

    def execute(self):
        pass

    def action_performed(self, command: str, event=None):
        pass
