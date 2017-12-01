# -*- coding: utf-8 -*-


class SavingAcc(object):
    def __init__(self, intial_sum, montly_transfer, nominal_interest, compounding_peridod):
        self.A = intial_sum
        self.P = montly_transfer
        self.i = nominal_interest / compounding_peridod
