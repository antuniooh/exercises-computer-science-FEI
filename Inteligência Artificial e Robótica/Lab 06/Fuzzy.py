import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy.control import Antecedent, Consequent, Rule, ControlSystemSimulation


class Fuzzy():

    def __init__(self):
        self.ang = None
        self.velocidade_angul = None
        self.forc_apl = None
        self.rules = None
        self.pos_carro = None
        self.vel_carro = None
        self.ante()
        self.conse()
        self.rule()

    def conse(self):
        self.forc_apl = Consequent(np.arange(-6, 6, 0.2), 'forca_aplicada')

        self.forc_apl['NB'] = fuzz.trimf(self.forc_apl.universe, [-3.6, -2.4, -1.2])
        self.forc_apl['N'] = fuzz.trimf(self.forc_apl.universe, [-2.4, -1.2, 0])
        self.forc_apl['PB'] = fuzz.trimf(self.forc_apl.universe, [1.2, 2.4, 3.6])
        self.forc_apl['NVVB'] = fuzz.trapmf(self.forc_apl.universe, [-6, -6, -4.8, -3.6])
        self.forc_apl['NVB'] = fuzz.trimf(self.forc_apl.universe, [-4.8, -3.6, -2.4])
        self.forc_apl['PVB'] = fuzz.trimf(self.forc_apl.universe, [2.4, 3.6, 4.8])
        self.forc_apl['Z'] = fuzz.trimf(self.forc_apl.universe, [-1.2, 0, 1.2])
        self.forc_apl['P'] = fuzz.trimf(self.forc_apl.universe, [0, 1.2, 2.4])
        self.forc_apl['PVVB'] = fuzz.trapmf(self.forc_apl.universe, [3.6, 4.8, 6, 6])

    def plot_conse(self):
        self.forc_apl.view()
        plt.show()