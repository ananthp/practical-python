# pcost.py
#
# Exercise 1.27

f = open('Data/portfolio.csv', 'rt')
headers = next(f)

total_cost = 0
for line in f:
    row = line.strip().split(',')
    total_cost = total_cost + int(row[1]) * float(row[2])

print('Cost of the portfolio is ', total_cost)
