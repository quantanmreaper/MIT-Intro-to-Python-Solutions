##Program to calculate how many months it will take to save for a down payment on a house using Python programming language trying to 
## reduce my dependancy on ai to solve problems and train my brain to think like a programmer

##In this part b we are going to modify the code to include the following:
       ##1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
       ##2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th month, the 18  month, and so on. 
       
print("===========================================================================")
##user input for annual salary 
annual_salary = float(input("Enter your annual salary: "))
print("===========================================================================")

## user input for the portion they would like to save monthly
print("---------------------------------------------------------------------------")
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: (e.g. 0.1 for 10%) "))


## user input for the total cost of the house
total_cost = float(input("Enter the total cost of your dream house that you would like to buy:"))


##Semi-annual raise included in this part of the problem set
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal percentage: "))

##calculating down payment for the house
portion_down_payment = total_cost * 0.25



months = 0
current_savings = 0
monthly_salary = annual_salary / 12
months_to_raise = 6

## so new salary will increase by semi_annual_raise after every 6 months  how do we program this?
while current_savings < portion_down_payment:
    ## The below condition checks if the months is a multiple of 6 and if it is greater than 0 then we increase the salary by the semi_annual rate
    if months % 6 == 0 and months >0:
        monthly_salary += monthly_salary * semi_annual_raise
    current_savings += monthly_salary * portion_saved + (current_savings * 0.04)/12
    months += 1
    
print("Number of Months: ", months) 