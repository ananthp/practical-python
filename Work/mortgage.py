# mortgage.py
#
# Exercise 1.11

principal = 500_000.0
rate = 0.05
regular_payment = 2684.11

# months are counted from 1, i.e., the first payment happens in month 1
extra_payment_start_month = 60  # inclusive
extra_payment_end_month = 108   # also inclusive. but why?
extra_payment = 1000
total_paid = 0.0

# this still has to count from zero
months = 0
while principal > 0:
    # We increment months at the beginning so the logic looks natural.
    # Think that the month has arrived, then we proceed with payment. 
    months = months + 1
    principal = principal * (1+rate/12)

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        payment = regular_payment + extra_payment
    else:
        payment = regular_payment
    
    if principal < payment:
        payment = principal

    principal = principal - payment
    total_paid = total_paid + payment

    print(months, round(total_paid, 2), round(principal,2))

print('Total paid', total_paid)
print('Months', months)
