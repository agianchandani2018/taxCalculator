#Author: Ami
#Date: April XX





#---------------------------------Main Program--------------------------------------------


plan = input("Which plan are you using? ")
income = int(input("How much gross income did you make? "))
grossIncome = income


if plan == "2000":

	if income < 2650 and income >= 0:
		income = income
		
	if income < 27850 and income >= 2650:
		income -= 2650
		income = income * .85
		
	if income < 59900 and income >= 27850:
		income -= 2650
		income = income * .85
		income = income * .72
		
	if income < 134200 and income >= 59900:
		income -= 2650
		income = income * .85
		income = income * .72
		income = income * .69
		
	if income < 289950 and income >= 134200:
		income -= 2650
		income = income * .85
		income = income * .72
		income = income * .69
		income = income * .64
#		print("Your income is {}".format(income))	
		
	if income >= 289950:
		income -= 2650
		income = income * .85
		income = income * .72
		income = income * .69
		income = income * .64
		income = income * .604
	

#elif plan == "2008":

#elif plan == "2014": 


taxes = round(grossIncome, 2) - round(income, 2)

print("Your net income is ${}".format(round(income, 2)))	
print("You owe ${} in taxes".format(taxes))

percentGross = round((income / grossIncome), 2)*100
print("Your percent gross is {}%".format(percentGross))