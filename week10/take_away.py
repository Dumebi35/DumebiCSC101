#collect data from the user
P = int(input('What is the Principal? '))
R = int(input('What is the Rate? '))
n = int(input('What is the number of deposits '))
t = int(input('What is the time? '))
PMT = int(input('What is the PMT? '))

#print the compound interest
compound_interest_A = P * ((1 + (R/n))**(n*t))
print("The compound amount is ", compound_interest_A)

#print annuity plan amount
annuity_plan_A = PMT * ((((1 + (R/n))**(n*t))-1 )/ (R/n))
print("The annuity plan amount is", annuity_plan_A)