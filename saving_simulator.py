# -*- coding: utf-8 -*-
import numpy as np


class SavingAcc(object):
    def __init__(self, intial_sum, montly_transfer, nominal_interest,
                 compounding_peridod):
        self.A = np.float32(intial_sum)
        self.P = np.float32(montly_transfer)
        self.i = np.float32(nominal_interest / compounding_peridod)
        self.Bs = list()

    def simulate_at_n(self, n):
        B_at_n = self.A * np.power((1 + self.i), n) + \
            (self.P / self.i) * (np.power(1 + self.i, n) - 1)
        return B_at_n


saving = SavingAcc(120000, 0, 0.072, 12)
print(saving.simulate_at_n(36))
