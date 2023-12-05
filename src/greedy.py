import pandas as pd


class Greedy:
    def __init__(self):
        self.state_machine = {
            'CV01': True,
            'CV02': True,
            'FPA01': True,
            'FPA02': True,
            'RH01': True,
            'CC01': True,
            'CC02': True,
            'CL03': True,
            'CL11': True,
            'CL15': True,
            'CL21': True
        }

        self.time_machine = {
            'CV01': 0,
            'CV02': 0,
            'FPA01': 0,
            'FPA02': 0,
            'RH01': 0,
            'CC01': 0,
            'CC02': 0,
            'CL03': 0,
            'CL11': 0,
            'CL15': 0,
            'CL21': 0
        }

        self.history_machine = {
            'CV01': [],
            'CV02': [],
            'FPA01': [],
            'FPA02': [],
            'RH01': [],
            'CC01': [],
            'CC02': [],
            'CL03': [],
            'CL11': [],
            'CL15': [],
            'CL21': []
        }

        self.time = 0

    def run(self, data: pd.DataFrame):
        pass
