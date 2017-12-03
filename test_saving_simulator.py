# -*- coding: utf-8 -*-
import pytest
from savingaccount.saving_simulator import (SavingAcc, SavingAccWithdrawal,
                                            NotAllowed)


def test_simulate_yearly():
    # Initial deposit 120000 SEK
    # Compounding every 1 month, interest 7.2%
    # Average 1 period deposit 0 SEK
    saving = SavingAcc(120000, 0, 0.072, 12, 48)
    val = saving.saving_months[-1]
    assert 159913 == round(val)
    val_36th = saving.get_amount_at_month_n(36)
    assert 148836 == round(val_36th)


def test_normal_account_no_withdrawal():
    saving = SavingAcc(120000, 0, 0.072, 12, 48)
    with pytest.raises(NotAllowed):
        saving.withdraw(10, 100)


def test_withdrawal():
    saving = SavingAccWithdrawal(1000, 500, 0.072, 12, 48)
    # Withdraw 2000EUR in the 5th month
    saving.withdraw(5, 2000)
    assert round(saving.get_amount_at_month_n(5)) == 1561
    # Saving account without regular deposit
    # Initial deposit 120000 SEK
    # Compounding every 1 month, interest 7.2%
    # Average 1 period deposit 0 SEK
    saving = SavingAccWithdrawal(120000, 0, 0.072, 12, 48)
    # Withdraw 20000 SEK in the 18th month
    saving.withdraw(18, 20000)
    assert round(saving.get_amount_at_month_n(48)) == 135982


def test_simulate_at_n():
    # Saving account without regular deposit
    # Initial deposit 120000 SEK
    # Compounding every 1 month, interest 7.2%
    # Average 1 period deposit 0 SEK
    saving = SavingAcc(120000, 0, 0.072, 12, 48)
    val = saving.simulate_at_n(36, saving.A, saving.i, saving.P)
    assert 148836 == round(val)
    # Saving account with regular deposit
    # Initial deposit 100 EUR
    # Compounding every 2 weeks, interest 1.4%
    # Average 1 period deposit 50 EUR
    saving = SavingAcc(1000, 50, 0.014, 24, 24)
    val = saving.simulate_at_n(24, saving.A, saving.i, saving.P)
    assert 2222 == round(val)
