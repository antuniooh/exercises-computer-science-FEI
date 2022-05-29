import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from skfuzzy.control import *
from Fuzzy import Fuzzy


class   SwingUp(Fuzzy):




    def rule(self):
        self.rules = [
            Rule(self.ang['NLS'] & self.velocidade_angul['POS'], self.forc_apl['NB']),
            Rule(self.ang['NBS'] & self.velocidade_angul['POS'], self.forc_apl['Z']),
            Rule(self.ang['SALN'] & self.velocidade_angul['POS'], self.forc_apl['N']),
            Rule(self.ang['Z'] & self.velocidade_angul['ZS'], self.forc_apl['P']),
            Rule(self.ang['SALP'] & self.velocidade_angul['NEG'], self.forc_apl['P']),
            Rule(self.ang['PBS'] & self.velocidade_angul['NEG'], self.forc_apl['Z']),
            Rule(self.ang['PLS'] & self.velocidade_angul['NEG'], self.forc_apl['PB'])
        ]

    def ante(self):
        self.velocidade_angul = Antecedent(np.arange(-10, 11, 0.1), 'vel_ang')
        self.velocidade_angul['NEG'] = fuzz.trapmf(self.velocidade_angul.universe, [-10, -10, -1, 0])
        self.velocidade_angul['ZS'] = fuzz.trapmf(self.velocidade_angul.universe, [-0.1, 0, 0, 0.1])
        self.velocidade_angul['POS'] = fuzz.trapmf(self.velocidade_angul.universe, [0, 1, 10, 10])

        self.ang = Antecedent(np.arange(0, 401, 1), 'ang')
        self.ang['NBS'] = fuzz.trimf(self.ang.universe, [30, 150, 170])
        self.ang['SALN'] = fuzz.trimf(self.ang.universe, [170, 175, 180])
        self.ang['Z'] = fuzz.trimf(self.ang.universe, [180, 180, 180])
        self.ang['SALP'] = fuzz.trimf(self.ang.universe, [180, 185, 190])
        self.ang['NLS'] = fuzz.trimf(self.ang.universe, [90, 130, 170])
        self.ang['PBS'] = fuzz.trimf(self.ang.universe, [190, 210, 330])
        self.ang['PLS'] = fuzz.trimf(self.ang.universe, [190, 230, 270])


    def plot_ante(self):
        self.ang.view()
        self.velocidade_angul.view()

    def show(self, attrs):
        input_ang,  input_velocidade_angul = attrs
        simulation = ControlSystemSimulation(ControlSystem(self.rules))
        print(f'teste: {input_ang}   {input_velocidade_angul}')
        print("\n\n\n\n\n")
        simulation.input['ang'] = input_ang
        simulation.input['vel_ang'] = input_velocidade_angul
        simulation.compute()
        print('passou')
        applied_force_value = simulation.output['forca_aplicada']
        self.ang.view(simulation)
        self.velocidade_angul.view(simulation)
        self.forc_apl.view(simulation)
        plt.show()
        return applied_force_value
