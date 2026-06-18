print("Welcome to tip calculator!")
bill = int(input("What is the bill "))
tip = int(input("How much would you like to tip?"))
split = int(input("How many people are splitting"))

tip_total = bill * tip / 100
final_bill = tip_total + bill 
split_bill = final_bill / split

print ( f" total bill is {split_bill:.2f}")