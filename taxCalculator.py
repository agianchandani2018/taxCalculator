#Author: Ami
#Date: April XX

import math




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


grossIncome = float(input("How much money did you make? "))
adjustedIncome = grossIncome - 9500

#DONE under 2,650
if adjustedIncome <= bracket1:
	totalTaxesOwed = percentTax1 * grossIncome
	overflowIncome = 0

#DONE under 27,850
if adjustedIncome > bracket1 and adjustedIncome <= bracket2:
	totalTaxesOwed = percentTax1 * bracket1
	overflowIncome = grossIncome - bracket1
	totalTaxesOwed += overflowIncome * percentTax2

#DONE under 59,900	
if adjustedIncome > bracket2 and adjustedIncome <= bracket3:
	
	totalTaxesOwed = percentTax1 * bracket1	
	totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
	overflowIncome = grossIncome - bracket2
	totalTaxesOwed += percentTax3 * overflowIncome
	

#DONE under 134,200
if adjustedIncome > bracket3 and adjustedIncome <= bracket4:
	totalTaxesOwed = percentTax1 * bracket1
	overflowIncome = grossIncome - bracket1
	totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
	overflowIncome = grossIncome - bracket2
	totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
	overflowIncome = grossIncome - bracket3
	totalTaxesOwed += percentTax4 * overflowIncome

#DONE under 289950
if adjustedIncome > bracket4 and adjustedIncome <= bracket5:
	totalTaxesOwed = percentTax1 * bracket1
	overflowIncome = grossIncome - bracket1
	totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
	overflowIncome = grossIncome - bracket2
	totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
	overflowIncome = grossIncome - bracket3	
	totalTaxesOwed += percentTax4 * (bracket4 - bracket3)
	overflowIncome = grossIncome - bracket4
	totalTaxesOwed = percentTax5 * overflowIncome

#DONE under infinity
if adjustedIncome > bracket5:
	totalTaxesOwed = percentTax1 * bracket1
	overflowIncome = grossIncome - bracket1
	totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
	overflowIncome = grossIncome - bracket2
	totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
	overflowIncome = grossIncome - bracket3	
	totalTaxesOwed += percentTax4 * (bracket4 - bracket3)
	overflowIncome = grossIncome - bracket4
	totalTaxesOwed += percentTax5 *(bracket5 - bracket4)
	overflowIncome = grossIncome - bracket5
	totalTaxesOwed += percentTax6 * overflowIncome

return totalTaxesOwed





grossIncome = round(grossIncome, 2)
totalTaxesOwed = round(totalTaxesOwed, 2)
netIncome = grossIncome - totalTaxesOwed

print("Your gross income is ${}.".format(grossIncome))
print("You owe ${} in taxes".format(totalTaxesOwed))
print("Your net income is ${}".format(netIncome))

print("Your efficiency overflow is {}".format(overflowIncome))
