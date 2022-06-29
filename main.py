import json

json_data = open('params.json')
json_load = json.load(json_data)
n_year = json_load["n"] / 12
i_perc = json_load["i"] / 100


def payment():
    total_pay = json_load["loan_amount"] * n_year * i_perc
    return total_pay


def interest_paid(months_paid):
    years_paid = months_paid / 12
    paid = json_load["loan_amount"] * years_paid * i_perc
    loan_remaining = payment() - paid
    paid_percent = paid * 100 / payment()
    print(f"Loan remaining: {round(loan_remaining)}, Percentage paid: {round(paid_percent, 2)},"
          f" Paid amount: {round(paid)}, Total loan: {round(payment())}")


interest_paid(34)
