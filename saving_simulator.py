# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


class SavingAcc(object):
    def __init__(self, intial_sum, monthly_transfer, nominal_interest,
                 compounding_peridod):
        self.A = np.float32(intial_sum)
        self.P = np.float32(monthly_transfer)
        self.i = np.float32(nominal_interest / compounding_peridod)
        self.Bs = list()
        self.rate_yearly = np.round(nominal_interest * 100, 1)

    def simulate_at_n(self, n):
        B_at_n = self.A * np.power((1 + self.i), n) + \
            (self.P / self.i) * (np.power(1 + self.i, n) - 1)
        return B_at_n

    def simulate_for_one_year(self):
        self.months = range(1, 13)
        self.saving_months = map(self.simulate_at_n, self.months)

    @staticmethod
    def autolabel(rects, ax):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2.,
                1.05 * height,
                '%d' % int(height),
                ha='center',
                va='bottom')

    def plot_one_year_saving(self):
        self.simulate_for_one_year()
        fix, ax = plt.subplots(figsize=(14, 5))
        data_to_plot = list(self.months)
        y_pos = np.arange(len(data_to_plot))

        bar = plt.bar(
            y_pos, list(self.saving_months), align='center', alpha=0.5)
        plt.xticks(y_pos, data_to_plot)
        plt.ylabel('Total Value in Account')
        plt.title(
            'Interest {i}%, Intial deposit {A}EUR, Monthly deposit {P}EUR'.
            format(i=self.rate_yearly, A=self.A, P=self.P))
        self.autolabel(bar, ax)
        plt.show()


saving = SavingAcc(1000, 300, 0.01, 12)
saving.plot_one_year_saving()
