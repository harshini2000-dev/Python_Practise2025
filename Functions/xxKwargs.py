# demo for *args
# demo for **Kwargs

def order_pizza(size, *toppings, **order_details):
    print(f"You have ordered a {size} pizza with toppings: ")
    # print(toppings) # prints tuple ('Olives', 'Capsicum', 'BellPeppers')
    for item in toppings:
        print(f" - {item}")
    
    # print(details) # prints dictionary {'payment': 'Online', 'tip': 5}
    print("Other details: ")
    for key,value in order_details.items():
        print(f" - {key} : {value}")

order_pizza('Large', "Olives", "Capsicum", "BellPeppers", payment = 'Online', tip = 5)