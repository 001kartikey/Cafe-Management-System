#define the menu of restaurant
menu = {
    "pizza":40,
    "pasta":50,
    "burger":60,
    "salad":70,
    "coffee":80
}
print("Welcome to PYTHON Restaurant")
print("Pizza : 40\nPasta : 50\nBurger : 60\nsalad : 70\ncoffee : 80") 

order_total = 0

item_1 = input("Enter the name of item you want to order = ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} added to your order")

else:
    print("Ordered item {item_1} is not available yet")


another_order = input("Do you want to add another item? (Yes/No)").lower()

if another_order == "yes":
    item_2 = input("Enter the name of second item = ").lower()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your order")

    else:
        print("ordered item {item_2} is not available")

print(f"The Total amount of items to pay is {order_total}")


