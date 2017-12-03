# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


class NotAllowed(Exception):
    pass


class SavingAcc(object):
    def __init__(self, intial_sum, monthly_transfer, nominal_interest,
                 compounding_peridod, length_of_simulation):
        self.A = np.float32(intial_sum)
        self.P = np.float32(monthly_transfer)
        self.i = np.float32(nominal_interest / compounding_peridod)
        self.Bs = list()
        self.rate_yearly = np.round(nominal_interest * 100, 1)
        self.months = range(1, length_of_simulation + 1)
        self.saving_months = list(
            map(lambda x: self.simulate_at_n(x, self.A, self.i, self.P),
                self.months))

    def get_amount_at_month_n(self, n):
        return self.saving_months[n - 1]

    @staticmethod
    def simulate_at_n(n, A, i, P):
        B_at_n = A * np.power((1 + i), n) + \
            (P / i) * (np.power(1 + i, n) - 1)
        return B_at_n

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

    def withdraw(self, n, amount):
        raise NotAllowed("Withdrawal not allowed")

    def plot_one_year_saving(self):
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


class SavingAccWithdrawal(SavingAcc):
    def withdraw(self, month_n, amount):
        self.saving_months[month_n
                           - 1] = self.saving_months[month_n - 1] - amount
        rest_of_the_years = self.months[month_n::]
        # Recalculate for the rest of the year
        saving_for_the_rest_of_the_year = map(
            lambda x: self.simulate_at_n(x - month_n, self.saving_months[month_n - 1], self.i, self.P),
            rest_of_the_years)
        # Substitute results
        self.saving_months[month_n::] = saving_for_the_rest_of_the_year
