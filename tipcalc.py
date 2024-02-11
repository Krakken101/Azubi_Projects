#Asanka Hotel Tip Calculator
# Define a function to calculate tip amount
def calculate_tip(charge):
    tip = charge * 0.18
    return tip

# Define a function to calculate sales tax amount
def calculate_sales_tax(charge):
    tax = charge * 0.07
    return tax

# Function to calculate total meal cost including tip and tax
def calculate_total_cost(charge):
    tip = calculate_tip(charge)
    tax = calculate_sales_tax(charge)
    total_cost = charge + tip + tax
    return total_cost

# Main program
if __name__ == "__main__":
    # Input charge for food
    charge_for_food = float(input("Charge for food = $"))
    
    # Calculate tip
    tip_amount = calculate_tip(charge_for_food)
    print(f"Tip = ${tip_amount:.2f}")
    
    # Calculate sales tax
    sales_tax_amount = calculate_sales_tax(charge_for_food)
    print(f"Sales tax = ${sales_tax_amount:.2f}")
    
    # Calculate total cost
    total_cost = calculate_total_cost(charge_for_food)
    print(f"Grand total = ${total_cost:.2f}")
