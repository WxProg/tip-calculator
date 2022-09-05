#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

bill = float(input("What was the total of your bill? $"))
tip = int(input("What percentage of tip would you like to give? ")) / 100
bill_with_tip = (bill * tip) + bill
split = int(input("How many people is the bill spliting between? "))
bill_total = round(bill_with_tip / split, 2)

each_pay = f"Each person should pay: ${bill_total}"
each_pay = "{:.3f}".format(bill_with_tip/split)

print(each_pay)

print("Thank you, please come again 😊")
