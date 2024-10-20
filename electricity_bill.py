units = int(input("Enter the number of electricity units consumed :"))

bill = 0
if units <= 50 :
    bill = units * 0.50
elif units <= 150 :
    bill = (50*0.50) + ((units - 50) * 0.75)
elif units <= 250 :
    bill = (50*0.50) + (100*0.75) + (100*1.20) + ((units - 200)* 1.50)
else :
    bill = (50*0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = bill * 0.20
total_bill = bill + surcharge
print(f"Total Electricity Bill is {total_bill} Rs")