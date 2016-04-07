#Author: Ami
#Date: April XX

import math

def calculate_tax(adjustedIncome):

	'''Takes a users income and outputs the money they owe in taxes for 3 plans'''
	adjustedIncome = grossIncome - 9500

	#DONE under 2,650
	if adjustedIncome <= bracket1:
		totalTaxesOwed = percentTax1 * adjustedIncome
		overflowIncome = 0

	#DONE under 27,850
	if adjustedIncome > bracket1 and adjustedIncome <= bracket2:
		totalTaxesOwed = percentTax1 * bracket1
		overflowIncome = adjustedIncome - bracket1
		totalTaxesOwed += overflowIncome * percentTax2

	#DONE under 59,900	
	if adjustedIncome > bracket2 and adjustedIncome <= bracket3:
		totalTaxesOwed = percentTax1 * bracket1	
		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
		overflowIncome = adjustedIncome - bracket2
		totalTaxesOwed += percentTax3 * overflowIncome
	

	#DONE under 134,200
	if adjustedIncome > bracket3 and adjustedIncome <= bracket4:
		totalTaxesOwed = percentTax1 * bracket1
		overflowIncome = adjustedIncome - bracket1
		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
		overflowIncome = adjustedIncomee - bracket2
		totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
		overflowIncome = adjustedIncome - bracket3
		totalTaxesOwed += percentTax4 * overflowIncome

	#DONE under 289950
	if adjustedIncome > bracket4 and adjustedIncome <= bracket5:
		totalTaxesOwed = percentTax1 * bracket1
		overflowIncome = adjustedIncome - bracket1
		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
		overflowIncome = adjustedIncome - bracket2
		totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
		overflowIncome = adjustedIncome - bracket3	
		totalTaxesOwed += percentTax4 * (bracket4 - bracket3)
		overflowIncome = adjustedIncome - bracket4
		totalTaxesOwed = percentTax5 * overflowIncome

	#DONE under infinity
	if adjustedIncome > bracket5:
		totalTaxesOwed = percentTax1 * bracket1
		overflowIncome = adjustedIncome - bracket1
		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
		overflowIncome = adjustedIncome - bracket2
		totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
		overflowIncome = adjustedIncome - bracket3	
		totalTaxesOwed += percentTax4 * (bracket4 - bracket3)
		overflowIncome = adjustedIncome - bracket4
		totalTaxesOwed += percentTax5 *(bracket5 - bracket4)
		overflowIncome = adjustedIncome - bracket5
		totalTaxesOwed += percentTax6 * overflowIncome

	return float(totalTaxesOwed)


#---------------------------------Main Program--------------------------------------------

#2000 plan
bracket1 = 2650
bracket2 = 27850
bracket3 = 59900
bracket4 = 134200
bracket5 = 289950
bracket6 = math.inf

percentTax1 = 0
percentTax2 = .15
percentTax3 = .28
percentTax4 = .31
percentTax5 = .36
percentTax6 = .396



x=1
while x == 1:
	grossIncome = input("How much money did you make? ")
	
	try:
		grossIncome = float(grossIncome)
	except ValueError:
		print("Sorry, that's not a number.")
		print("Try again")
		
	else:	

		adjustedIncome = float(grossIncome - 9500)

		percent = round(100 * (calculate_tax(adjustedIncome)/grossIncome), 2)

# 		print(grossIncome)
# 		print(adjustedIncome)
		print("Results for the 2000 plan")
		print("Taxes owed: ${}".format(calculate_tax(grossIncome)))
		print("Percent of gross: {}%".format(percent))
		print("Net income: ${}".format(grossIncome - calculate_tax(grossIncome)))
		x=0


# grossIncome = round(grossIncome, 2)
# totalTaxesOwed = round(totalTaxesOwed, 2)
# netIncome = grossIncome - totalTaxesOwed
# 
# print("Your gross income is ${}.".format(grossIncome))
# print("You owe ${} in taxes".format(totalTaxesOwed))
# print("Your net income is ${}".format(netIncome))
# 
# print("Your efficiency overflow is {}".format(overflowIncome))
