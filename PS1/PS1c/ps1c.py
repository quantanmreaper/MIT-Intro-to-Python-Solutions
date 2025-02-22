'''
 In this part of the problem we are going to use bisection search algorithm to find 
n the best rate of savings to achieve a down payment on a $1M house in 
36 months.

Problem Breakdown:
1. We need to determine the best savings rate (as a percentage of salary) to save enough for 
a $1M house within 36 months.
2. The down payement is 25% of the house price - $250,000.
3. The savings must be withing $100 of the required down payment.
4. The salary increments every 6 months by 7% which is the new semi annual rate.
5. The savings grow with an annual reutrn of 4%


## We are going to use BISECTION SEARCH AS REQUIRED 
'''


##monthly_salary = annual_salary / 12
##portion_saved = float(input("Enter the percent of your salary to save, as a decimal: (e.g. 0.1 for 10%) "))

""" 
totalhouse_cost = 1000000
down_payment = totalhouse_cost * 0.25
semi_annual_raise = 0.07
annual_return_rate = 0.04
epsilon = 100 """ # The margin of error for the bisection search it 
# epsilon ensures that time is not wasted searching for an exact match when an approximate match is good enough.
# absence of epsilon will result in infinite search if the exact match is not found.


## Function to implement the simulation for 36 months
""" def simulate_savings(annual_salary, portion_saved):
    current_savings = 0
    monthly_salary = annual_salary / 12  # Start with the base salary

    for month in range(1, 37):  # Loop for 36 months
        current_savings += (current_savings * 0.04) / 12  # Monthly investment return
        current_savings += monthly_salary * portion_saved  # Add saved amount

        if month % 6 == 0:  # Apply semi-annual raise every 6 months
            monthly_salary += monthly_salary * semi_annual_raise

    return current_savings  # Return the total savings after 36 months

    
## implementing the bisection search below
def bisection_search_implementation(annual_salary):
    low = 0 ##  represents the lower bound of the savings rate 0% savings rate
    high = 10000 ## represents the upper bound of the savings rate 100%  savings rate
    steps = 0
    ##portion_saved = (low + high) // 2 in while loop later
    
    ## First check if the saving is possible with 100% savings rate
    if simulate_savings(annual_salary, 1.0) < down_payment:
        print("It is not possible to save for the down payment in 36 months")
        return None, -1
    
    while (high - low) > 1:
        mid = (low + high) // 2
        portion_saved = mid / 10000 ## convert to percentage
        
        current_savings = simulate_savings(annual_salary, portion_saved)
        
        if (current_savings < down_payment) <= epsilon:
            return portion_saved, steps
        elif current_savings < down_payment:
            low = mid
        else:
            high = mid
        steps +=1
    return None, steps


annual_salary = float(input("Enter your annual salary: "))

best_rate, steps = bisection_search_implementation(annual_salary)

if best_rate:
    print(f"Best savings rate: {best_rate: .4f}")
    print(f"Steps in bisection search: {steps}")
elif steps == -1:
    print("It is not possible to save for the down payment in 36 months") """
    
    
totalhouse_cost = 1000000
down_payment = totalhouse_cost * 0.25
semi_annual_raise = 0.07
annual_return_rate = 0.04
epsilon = 100  

## Function to implement the simulation for 36 months
def simulate_savings(annual_salary, portion_saved):
    current_savings = 0
    monthly_salary = annual_salary / 12  

    for month in range(1, 37):  
        current_savings += (current_savings * annual_return_rate) / 12  
        current_savings += monthly_salary * portion_saved  

        if month % 6 == 0:  
            monthly_salary += monthly_salary * semi_annual_raise

    return current_savings  

## Implementing the bisection search below
def bisection_search_implementation(annual_salary):
    low = 0  
    high = 10000  
    steps = 0  

    if simulate_savings(annual_salary, 1.0) < down_payment:
        print("It is not possible to save for the down payment in 36 months")
        return None, -1  

    while (high - low) > 1:
        mid = (low + high) // 2
        portion_saved = mid / 10000  

        current_savings = simulate_savings(annual_salary, portion_saved)

        if abs(current_savings - down_payment) <= epsilon:  # FIXED THIS LINE
            return portion_saved, steps  
        elif current_savings < down_payment:
            low = mid
        else:
            high = mid

        steps += 1  

    return None, steps  

annual_salary = float(input("Enter your annual salary: "))

best_rate, steps = bisection_search_implementation(annual_salary)

if best_rate:
    print(f"Best savings rate: {best_rate:.4f}")
    print(f"Steps in bisection search: {steps}")
elif steps == -1:
    print("It is not possible to save for the down payment in 36 months.")
