import numpy as np
class Extension:

    def __init__(self, threshold_u):
        self.tu = threshold_u
        self._zero_day_label = 0

    def set_threshold_u(self, threshold_u):
        self.tu = threshold_u


    def predict_benign_zero_day(self,prob_anomalia):
        # True == Benign
        # False == 0 day
        return prob_anomalia <= self.tu