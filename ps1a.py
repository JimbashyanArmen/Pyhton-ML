                     # PART A
#-----------------------------------------------------
annual_salary = int(input("Enter your annual salary: "))
partion_saved = float(input("Enter the percent of your salary to sace,as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
r = 0.04
monthly_salary = annual_salary/12
cost= total_cost * portion_down_payment 

months=1
current_savings=0
current_savings += monthly_salary*partion_saved

while current_savings < cost:
    current_savings += current_savings*r/12
    current_savings += monthly_salary*partion_saved
    months += 1
print("Number of months:", months)


