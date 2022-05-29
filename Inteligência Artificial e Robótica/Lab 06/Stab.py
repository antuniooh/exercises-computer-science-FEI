import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from skfuzzy.control import *
from Fuzzy import Fuzzy


class Stab(Fuzzy):

    def ante(self):
        self.ang = Antecedent(np.arange(-30, 30, 0.5), 'angulo')

        self.ang['NVB'] = fuzz.trapmf(self.ang.universe, [-30, -30, -18, -12])
        self.ang['NB'] = fuzz.trimf(self.ang.universe, [-16.5, -10.5, -4.5])
        self.ang['N'] = fuzz.trimf(self.ang.universe, [-9, -4.5, 0])
        self.ang['PB'] = fuzz.trimf(self.ang.universe, [4.5, 10.5, 16.5])
        self.ang['PVB'] = fuzz.trapmf(self.ang.universe, [12, 18, 30, 30])
        self.ang['ZO'] = fuzz.trimf(self.ang.universe, [-3, 0, 3])
        self.ang['P'] = fuzz.trimf(self.ang.universe, [0, 4.5, 9])

        self.velocidade_angul = Antecedent(np.arange(-6, 6, 0.1), 'velocidadeAngular')

        self.velocidade_angul['NB'] = fuzz.trapmf(self.velocidade_angul.universe, [-6, -6, -4.2, -1.7])
        self.velocidade_angul['N'] = fuzz.trimf(self.velocidade_angul.universe, [-3.6, -1.7, 0])
        self.velocidade_angul['ZO'] = fuzz.trimf(self.velocidade_angul.universe, [-1.7, 0, 1.7])
        self.velocidade_angul['P'] = fuzz.trimf(self.velocidade_angul.universe, [0, 1.7, 3.6])
        self.velocidade_angul['PB'] = fuzz.trapmf(self.velocidade_angul.universe, [1.7, 4.2, 6, 6])

        self.pos_carro = Antecedent(np.arange(-0.4, 0.4, 0.05), 'posicaocarro')

        self.pos_carro['NBIG'] = fuzz.trapmf(self.pos_carro.universe, [-0.4, -0.4, -0.3, -0.15])
        self.pos_carro['NEG'] = fuzz.trimf(self.pos_carro.universe, [-0.3, -0.15, 0])
        self.pos_carro['Z'] = fuzz.trimf(self.pos_carro.universe, [-0.15, 0, 0.15])
        self.pos_carro['POS'] = fuzz.trimf(self.pos_carro.universe, [0, 0.15, 0.3])
        self.pos_carro['PBIG'] = fuzz.trapmf(self.pos_carro.universe, [0.15, 0.3, 0.4, 0.4])

        self.vel_carro = Antecedent(np.arange(-1, 1, 0.1), 'Velcarro')

        self.vel_carro['NEG'] = fuzz.trapmf(self.vel_carro.universe, [-1, -1, -0.1, 0])
        self.vel_carro['ZERO'] = fuzz.trimf(self.vel_carro.universe, [-0.1, 0, 0.1])
        self.vel_carro['POS'] = fuzz.trapmf(self.vel_carro.universe, [0, 0.1, 1, 1])

    def rule(self):
        self.rules = [
            Rule(self.pos_carro['NBIG'] & self.vel_carro['NEG'], self.forc_apl['PVVB']),
            Rule(self.pos_carro['NEG'] & self.vel_carro['NEG'], self.forc_apl['PVB']),
            Rule(self.pos_carro['Z'] & self.vel_carro['NEG'], self.forc_apl['PB']),
            Rule(self.pos_carro['Z'] & self.vel_carro['ZERO'], self.forc_apl['Z']),
            Rule(self.pos_carro['Z'] & self.vel_carro['POS'], self.forc_apl['NB']),
            Rule(self.pos_carro['POS'] & self.vel_carro['POS'], self.forc_apl['NVB']),
            Rule(self.pos_carro['PBIG'] & self.vel_carro['POS'], self.forc_apl['NVVB']),
            Rule(self.ang['NVB'] & self.velocidade_angul['NB'], self.forc_apl['NVVB']),
            Rule(self.ang['NVB'] & self.velocidade_angul['N'], self.forc_apl['NVVB']),
            Rule(self.ang['NVB'] & self.velocidade_angul['ZO'], self.forc_apl['NVB']),
            Rule(self.ang['NVB'] & self.velocidade_angul['P'], self.forc_apl['NB']),
            Rule(self.ang['NVB'] & self.velocidade_angul['PB'], self.forc_apl['N']),
            Rule(self.ang['NB'] & self.velocidade_angul['NB'], self.forc_apl['NVVB']),
            Rule(self.ang['NB'] & self.velocidade_angul['N'], self.forc_apl['NVB']),
            Rule(self.ang['NB'] & self.velocidade_angul['ZO'], self.forc_apl['NB']),
            Rule(self.ang['NB'] & self.velocidade_angul['P'], self.forc_apl['N']),
            Rule(self.ang['NB'] & self.velocidade_angul['PB'], self.forc_apl['Z']),
            Rule(self.ang['N'] & self.velocidade_angul['NB'], self.forc_apl['NVB']),
            Rule(self.ang['N'] & self.velocidade_angul['N'], self.forc_apl['NB']),
            Rule(self.ang['N'] & self.velocidade_angul['ZO'], self.forc_apl['N']),
            Rule(self.ang['N'] & self.velocidade_angul['P'], self.forc_apl['Z']),
            Rule(self.ang['N'] & self.velocidade_angul['PB'], self.forc_apl['P']),
            Rule(self.ang['ZO'] & self.velocidade_angul['NB'], self.forc_apl['NB']),
            Rule(self.ang['ZO'] & self.velocidade_angul['N'], self.forc_apl['N']),
            Rule(self.ang['ZO'] & self.velocidade_angul['ZO'], self.forc_apl['Z']),
            Rule(self.ang['ZO'] & self.velocidade_angul['P'], self.forc_apl['P']),
            Rule(self.ang['ZO'] & self.velocidade_angul['PB'], self.forc_apl['PB']),
            Rule(self.ang['P'] & self.velocidade_angul['NB'], self.forc_apl['N']),
            Rule(self.ang['P'] & self.velocidade_angul['N'], self.forc_apl['Z']),
            Rule(self.ang['P'] & self.velocidade_angul['PB'], self.forc_apl['PVB']),
            Rule(self.ang['PB'] & self.velocidade_angul['NB'], self.forc_apl['Z']),
            Rule(self.ang['PB'] & self.velocidade_angul['N'], self.forc_apl['P']),
            Rule(self.ang['PB'] & self.velocidade_angul['ZO'], self.forc_apl['PB']),
            Rule(self.ang['PB'] & self.velocidade_angul['P'], self.forc_apl['PVB']),
            Rule(self.ang['PB'] & self.velocidade_angul['PB'], self.forc_apl['PVVB']),
            Rule(self.ang['PVB'] & self.velocidade_angul['NB'], self.forc_apl['P']),
            Rule(self.ang['PVB'] & self.velocidade_angul['N'], self.forc_apl['PB']),
            Rule(self.ang['PVB'] & self.velocidade_angul['ZO'], self.forc_apl['PVB']),
            Rule(self.ang['P'] & self.velocidade_angul['ZO'], self.forc_apl['P']),
            Rule(self.ang['P'] & self.velocidade_angul['P'], self.forc_apl['PB']),
            Rule(self.ang['PVB'] & self.velocidade_angul['P'], self.forc_apl['PVVB']),
            Rule(self.ang['PVB'] & self.velocidade_angul['PB'], self.forc_apl['PVVB'])
        ]

    def plot_ante(self):
        self.ang.view()
        self.velocidade_angul.view()
        self.pos_carro.view()
        self.vel_carro.view()
        plt.show()

    def show(self, attrs):
        input_ang,  input_velocidade_angul, input_pos_carro, input_vel_carro = attrs
        simulation = ControlSystemSimulation(ControlSystem(self.rules))
        simulation.input['angulo'] = input_ang
        simulation.input['posicaocarro'] = input_pos_carro
        simulation.input['Velcarro'] = input_vel_carro
        simulation.input['velocidadeAngular'] = input_velocidade_angul
        simulation.compute()
        forc_apl_value = simulation.output['forca_aplicada']
        self.ang.view(simulation)
        self.velocidade_angul.view(simulation)
        self.pos_carro.view(simulation)
        self.vel_carro.view(simulation)
        self.forc_apl.view(simulation)
        plt.show()
        return forc_apl_value
