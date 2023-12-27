import time
import sys

#Defining function to simulate typing effect
def typewrite(str):
    for letters in str:
        time.sleep(0.04)
        sys.stdout.write(letters)
        sys.stdout.flush()

#Displaying welcome messages
typewrite("\nHello there!\n")
time.sleep(0.5)
typewrite("Welcome to Aman's Vending Machine\n")

#Setting menu of available food and beverage items
vending_inventory = {
    "Food": {
        "A1": {"Name": "Twix", "Cost": 3.00, "Stock": 15},
        "A2": {"Name": "Chocolate Wafers", "Cost": 5.00, "Stock": 8},
        "A3": {"Name": "Strawberry Wafers", "Cost": 5.00, "Stock": 8},
        "A4": {"Name": "Hello Panda", "Cost": 3.50, "Stock": 15}
    },

    "Beverages": {
        "B1": {"Name": "Mango Juice", "Cost": 2.00, "Stock": 15},
        "B2": {"Name": "Strawberry Milk", "Cost": 2.50, "Stock": 12},
        "B3": {"Name": "Chocolate Milk", "Cost": 2.50, "Stock": 12},
        "B4": {"Name": "Iced Tea", "Cost": 4.00, "Stock": 10}
    }
}

#Displaying food menu
print("\n")
typewrite("SELECT YOUR FOOD AND BEVERAGES\n")
print("\n")
print("                               * Food *")

food_options = vending_inventory["Food"]

for code, food in food_options.items():
    typewrite(f"{code}. {food['Name']} - AED{food['Cost']} \n")

#Displaying beverage menu
print()
print("                               * Beverages *")
beverage_options = vending_inventory["Beverages"]
for code, drink in beverage_options.items():
    typewrite(f"{code}. {drink['Name']} - AED{drink['Cost']} \n")

#while loop for the purchasing
while True:
    selected_code = input("Enter the code of the item you want to purchase: ")

    if selected_code in food_options:
        selected_item = food_options[selected_code]
    elif selected_code in beverage_options:
        selected_item = beverage_options[selected_code]
    else:
        print("Invalid code. Please try again.")
        continue
#Above section is to check whether the code that the user inputted is in the menu
    
    if selected_item['Stock'] <= 0:
        print("Out of stock. Please choose another item.")
        continue

    cash_inserted = float(input("Enter the amount of money you are inserting: "))

    if cash_inserted < selected_item['Cost']:
        print("Not enough money. Please try again.")
        continue

    change = cash_inserted - selected_item['Cost']
    selected_item['Stock'] -= 1  #Deducting one from stock
    typewrite(f"Dispensing {selected_item['Name']}. Your change is AED{change:.2f} \n")

    if input("Do you want to buy another item? (yes/no): ").lower() != 'yes': #If user hits no the program ends
        break

typewrite("Thank you! Enjoy your food :)\n")

