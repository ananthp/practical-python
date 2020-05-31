# mortgage.py
#
# Exercise 1.8

principal = 500_000.0
rate = 0.05
regular_payment = 2684.11
extra = 1000
total_paid = 0.0

months = 0

while principal > 0:
    if months < 12:
        payment = regular_payment + extra
    else:
        payment = regular_payment

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months + 1

print('Total paid', total_paid)
print('Months', months)
