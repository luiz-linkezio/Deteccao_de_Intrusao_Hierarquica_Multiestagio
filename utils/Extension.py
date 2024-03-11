import numpy as np
import time
class Extension:

    def __init__(self, threshold_u):
        self.tu = threshold_u
        self._zero_day_label = 0
        self.execution_time_list3 = []

    def set_threshold_u(self, threshold_u):
        self.tu = threshold_u

    def get_execution_time_list3(self):
        return self.execution_time_list3

    def predict_benign_zero_day(self,prob_anomalia):
        start = time.perf_counter()
        # True == Benign
        # False == 0 day
        pred =  prob_anomalia <= self.tu
        finish = time.perf_counter()
        self.execution_time_list3.append(finish - start)
        return pred