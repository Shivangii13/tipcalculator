print("WELCOME TO THE TIP CALCULATOR.")
bill = float(input('what was the total bill? $'))
print(bill)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
print(tip)
people = int(input('How many people split the bill?'))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"Each person should pay ${final_amount}")