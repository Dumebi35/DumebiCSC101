#Python programme that finds simple interest

P = 1000
R = 1
T = 2

#simple interest
A = (P * (1 + ((R/100) * T)))
print('Amount is', A)
SI = A - P
print('Simple Interest is', SI)