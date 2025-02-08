##Program to calculate how many months it will take to save for a down payment on a house using Python programming language trying to 
## reduce my dependancy on ai to solve problems and train my brain to think like a programmer

print("===========================================================================")
##user input for annual salary 
annual_salary = float(input("Enter your annual salary: "))
print("===========================================================================")

## user input for the portion they would like to save monthly
print("---------------------------------------------------------------------------")
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: (e.g. 0.1 for 10%) "))


## user input for the total cost of the house
total_cost = float(input("Enter the total cost of your dream house that you would like to buy:"))

"""	
function for calculating months takeng  to save for a down payment on a house

def months_to_save(annual_salary, portion_saved, total_cost):
"""	

##calculating down payment for the house
portion_down_payment = total_cost * 0.25



months = 0
current_savings = 0
monthly_salary = annual_salary / 12

while current_savings < portion_down_payment:
    current_savings += monthly_salary * portion_saved + (current_savings * 0.04)/12
    months += 1
    
print("Number of Months: ", months)