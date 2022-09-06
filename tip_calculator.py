print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip woukd you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

split_bill = ((bill * (1 + (percent/100))) /people)

res = '%.2f' % split_bill

print(f"Each person should pay: ${res}")
