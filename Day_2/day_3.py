bill = 0

print("Welcome to Piza Delivery Service! ")

order = input("Would you like to order a pizza y or n ")

if order == "y":
    size = input("Good! Do you want a Small, Medium or Large Pizza?")
    if size == "small":
        bill = 15
        print(bill)
    elif size == "medium":
        bill = 20
        print(bill)
    elif size == "large":
        bill = 25    
    toppings = input("Do you want toppings?")
    if toppings == "y" and size == "small":
        bill = bill + 2
    if toppings == "y" and size == "medium":
        bill = bill + 3 
    if toppings == "y" and size == "large": 
        bill = bill + 3 

    extra_cheese = input("Do you want extra cheese?")
    if extra_cheese == "y":
        bill = bill + 1
    print(bill)
else:
    print("Get out.")








# size = input("What size would you like to order? Small is $15, Medium is $20, and Large is $25 ")

# if size == "small":
#     print("Good choice, that'll be $15.")
#     bill = 15
#     print(bill)
# elif size == "medium":
#     print("Good choice, that'll be $20")
# elif size == "large":
#     print("You biggie back, that'll be $25")
# else:
#     print("bruh.")

# pepperoni = input("Would you like to add pepperoni onto your piza? y or n ? ")
# if pepperoni == "y":
#     print("Good choice!")
#     if size == "small":
#         bill +2
#     else:
#         bill += 3
# else:
#     print("Okay!")

# cheese = input(" Would you like to add extra cheese? y or n ? ")
# if cheese == "y":
#     print("Are you lactose intolerant?")
#     bill +1 
# else:
#     print("Okay!") 
    
    