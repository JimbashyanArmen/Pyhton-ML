
                     # PART C
#-----------------------------------------------------

annual_salary = int(input("Enter the starting salary:"))
epsilon = 100
low = 0
high = 10000
guess = int((high + low) /2)
months=1
current_savings=0
total_cost = 1000000
portion_down_payment = 0.25
cost= total_cost * portion_down_payment

def current_savings_func(i):      
    semi_annual_raise = .07
    r = 0.04
    monthly_salary = annual_salary/12
    months=1
    current_savings=0
    current_savings += monthly_salary*i/10000

    while months <36:
        current_savings += current_savings*r/12
        if months % 6 == 0:
            monthly_salary *= 1+semi_annual_raise
            
        current_savings += monthly_salary*i/10000
        months += 1
    return current_savings

if current_savings_func(high) < cost:
    print("ree years.")

guesses = 1
while abs(current_savings_func(guess) - cost) >= epsilon:
   if current_savings_func(guess) < cost:
       low = guess
   else:
       high = guess    
   guess = int((high + low)/2)
   guesses += 1    
print("Best savings rate:",guess/10000)
print("steps in bisection search:",guesses )
