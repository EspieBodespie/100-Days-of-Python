#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = int(input("How much is the bill?\n"))
party = int(input("How many people are in the party?\n"))
tip = int(input("How much would you like to tip? 10%, 12%, or 15%\n"))
tip_as_percent = tip / 100
tip_of_bill = tip_as_percent * bill
bill_with_tip = bill + tip_of_bill
cost_per_person = bill_with_tip / party
final_amount = "{:.2f}".format(cost_per_person)
print(f"Each person needs to pay ${final_amount}")