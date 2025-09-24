#  defining the menu of the restuarent:

menu = {
    'samosa': 10,
    'pizza': 250,
    'fried-rice': 130,
    'noodles': 140,
    'pancakes': 70,
    'momos': 120,
}

# print("Menu loaded with", len(menu), "items.")
# print("Menu items:", menu)

print("Welcome to the Restaurant!")

print(" samosa : 10\n pizza': 250\n fried-rice': 130\n noodles': 140\n pancakes': 70 \n momos': 120 ")  # Accessing the price of samosa from the menu

order_total = 0

item = input("Enter the item you want to order ")

if item in menu:
    order_total = order_total + menu[item]
    print(f"{item} added to your order. Price: {menu[item]}")
else:
    print(f"Sorry, we don't have {item} on the menu.")

another_item = input("Do you want another items ? (yes/no) ")
if another_item =="yes":
    item2 = input("Enter the item you want to order ")
    if item2 in menu:
        order_total = order_total + menu[item2]
        print(f"{item} added to your order. Price: {menu[item2]}")
    else:
        print(f"Sorry, we don't have {item2} on the menu.")

print(f"Your total order amount is: {order_total}")