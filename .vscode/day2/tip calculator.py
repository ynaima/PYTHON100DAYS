#Day2 project - Tip Calculator
print("Welcome to the tip calculator!")

#bill input
bill = float(input("What was the total bill? $\n"))

#tip percentage input
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))

number_of_people = int(input("How many people to split the bill? \n"))

#calculate total tip
tip = (tip_percentage/100) * bill

total_bill = bill + tip

#bill per person
bill_per_person = round(total_bill / number_of_people , 2)

print (f"Each person should pay: ${bill_per_person}")
