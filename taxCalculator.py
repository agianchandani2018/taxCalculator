#Author: Ami
#Date: April XX

import math
# 
# def calculate_tax(adjustedIncome):
# 
# 	'''Takes a users income and outputs the money they owe in taxes for 3 plans'''
# 	adjustedIncome = grossIncome - 9500
# 
# 	#DONE under 2,650
# 	if adjustedIncome <= bracket1:
# 		totalTaxesOwed = percentTax1 * adjustedIncome
# 		overflowIncome = 0
# 
# 	#DONE under 27,850
# 	if adjustedIncome > bracket1 and adjustedIncome <= bracket2:
# 		totalTaxesOwed = percentTax1 * bracket1
# 		overflowIncome = adjustedIncome - bracket1
# 		totalTaxesOwed += overflowIncome * percentTax2
# 
# 	#DONE under 59,900	
# 	if adjustedIncome > bracket2 and adjustedIncome <= bracket3:
# 		totalTaxesOwed = percentTax1 * bracket1	
# 		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
# 		overflowIncome = adjustedIncome - bracket2
# 		totalTaxesOwed += percentTax3 * overflowIncome
# 	
# 
# 	#DONE under 134,200
# 	if adjustedIncome > bracket3 and adjustedIncome <= bracket4:
# 		totalTaxesOwed = percentTax1 * bracket1
# 		overflowIncome = adjustedIncome - bracket1
# 		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
# 		overflowIncome = adjustedIncomee - bracket2
# 		totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
# 		overflowIncome = adjustedIncome - bracket3
# 		totalTaxesOwed += percentTax4 * overflowIncome
# 
# 	#DONE under 289950
# 	if adjustedIncome > bracket4 and adjustedIncome <= bracket5:
# 		totalTaxesOwed = percentTax1 * bracket1
# 		overflowIncome = adjustedIncome - bracket1
# 		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
# 		overflowIncome = adjustedIncome - bracket2
# 		totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
# 		overflowIncome = adjustedIncome - bracket3	
# 		totalTaxesOwed += percentTax4 * (bracket4 - bracket3)
# 		overflowIncome = adjustedIncome - bracket4
# 		totalTaxesOwed = percentTax5 * overflowIncome
# 
# 	#DONE under infinity
# 	if adjustedIncome > bracket5:
# 		totalTaxesOwed = percentTax1 * bracket1
# 		overflowIncome = adjustedIncome - bracket1
# 		totalTaxesOwed += percentTax2 * (bracket2 - bracket1)
# 		overflowIncome = adjustedIncome - bracket2
# 		totalTaxesOwed += percentTax3 * (bracket3 - bracket2)
# 		overflowIncome = adjustedIncome - bracket3	
# 		totalTaxesOwed += percentTax4 * (bracket4 - bracket3)
# 		overflowIncome = adjustedIncome - bracket4
# 		totalTaxesOwed += percentTax5 *(bracket5 - bracket4)
# 		overflowIncome = adjustedIncome - bracket5
# 		totalTaxesOwed += percentTax6 * overflowIncome
# 
# 	return float(totalTaxesOwed)



#-----------------------------Bracket list attempt----------------------------------------


bracket1 = [2650, 8025, 8700]
bracket2 = [27850, 32550, 35350]
bracket3 = [59900, 78850, 85650]
bracket4 = [134200, 164550, 178650]
bracket5 = [289950, 357700, 388350]
#bracket6 = [math.inf, math.inf, math.inf]

percentTax1 = [0, .1, .1]
percentTax2 = [.15, .15, .15]
percentTax3 = [.28, .25, .25]
percentTax4 = [.31, .28, .28]
percentTax5 = [.36, .33, .33]
percentTax6 = [.396, .35, .35]


# plan2000 = [2650, 27850, 59900, 134200, 289950]
# plan2008 = [8025, 32550, 78850, 164550, 357700]
# plan2014 = [8700, 35350, 85650, 178650, 388350]
# 
# percent2000 = [0, .15, .28, .31, .36, .396]
# percent2008 = [.1, .15, .25, .28, .33, .35]
# percent2014 = [.1, .15, .25, .28, .33, .35]

def calculate_tax(adjustedIncome, i):

		'''Takes a users income and outputs the money they owe in taxes for 3 plans'''

#NEED TO EDIT THIS LINE EVERY TIME THE LIST CHANGES	
	#for i in range(3):
	
		if grossIncome >= 9500:
			adjustedIncome = grossIncome - 9500
		else:
			adjustedIncome = grossIncome - 0	

		#DONE under 2,650
		if adjustedIncome <= bracket1[i]:
			totalTaxesOwed = percentTax1[i] * adjustedIncome
			overflowIncome = 0

		#DONE under 27,850
		if adjustedIncome > bracket1[i] and adjustedIncome <= bracket2[i]:
			totalTaxesOwed = percentTax1[i] * bracket1[i]
			overflowIncome = adjustedIncome - bracket1[i]
			totalTaxesOwed += overflowIncome * percentTax2[i]

		#DONE under 59,900	
		if adjustedIncome > bracket2[i] and adjustedIncome <= bracket3[i]:
			totalTaxesOwed = percentTax1[i] * bracket1[i]	
			totalTaxesOwed += percentTax2[i] * (bracket2[i] - bracket1[i])
			overflowIncome = adjustedIncome - bracket2[i]
			totalTaxesOwed += percentTax3[i] * overflowIncome
	

		#DONE under 134,200
		if adjustedIncome > bracket3[i] and adjustedIncome <= bracket4[i]:
			totalTaxesOwed = percentTax1[i] * bracket1[i]
			overflowIncome = adjustedIncome - bracket1[i]
			totalTaxesOwed += percentTax2[i] * (bracket2[i] - bracket1[i])
			overflowIncome = adjustedIncome - bracket2[i]
			totalTaxesOwed += percentTax3[i] * (bracket3[i] - bracket2[i])
			overflowIncome = adjustedIncome - bracket3[i]
			totalTaxesOwed += percentTax4[i] * overflowIncome

		#DONE under 289950
		if adjustedIncome > bracket4[i] and adjustedIncome <= bracket5[i]:
			totalTaxesOwed = percentTax1[i] * bracket1[i]
			overflowIncome = adjustedIncome - bracket1[i]
			totalTaxesOwed += percentTax2[i] * (bracket2[i] - bracket1[i])
			overflowIncome = adjustedIncome - bracket2[i]
			totalTaxesOwed += percentTax3[i] * (bracket3[i] - bracket2[i])
			overflowIncome = adjustedIncome - bracket3[i]	
			totalTaxesOwed += percentTax4[i] * (bracket4[i] - bracket3[i])
			overflowIncome = adjustedIncome - bracket4[i]
			totalTaxesOwed = percentTax5[i] * overflowIncome

		#DONE under infinity
		if adjustedIncome > bracket5[i]:
			totalTaxesOwed = percentTax1[i] * bracket1[i]
			overflowIncome = adjustedIncome - bracket1[i]
			totalTaxesOwed += percentTax2[i] * (bracket2[i] - bracket1[i])
			overflowIncome = adjustedIncome - bracket2[i]
			totalTaxesOwed += percentTax3[i] * (bracket3[i] - bracket2[i])
			overflowIncome = adjustedIncome - bracket3[i]
			totalTaxesOwed += percentTax4[i] * (bracket4[i] - bracket3[i])
			overflowIncome = adjustedIncome - bracket4[i]
			totalTaxesOwed += percentTax5[i] *(bracket5[i] - bracket4[i])
			overflowIncome = adjustedIncome - bracket5[i]
			totalTaxesOwed += percentTax6[i] * overflowIncome

		return float(totalTaxesOwed)





#---------------------------------Main Program--------------------------------------------

#2000 plan
# bracket1 = 2650
# bracket2 = 27850
# bracket3 = 59900
# bracket4 = 134200
# bracket5 = 289950
# bracket6 = math.inf
# 
# percentTax1 = 0
# percentTax2 = .15
# percentTax3 = .28
# percentTax4 = .31
# percentTax5 = .36
# percentTax6 = .396



# bracket1 = [2650, 8025, 8700]
# bracket2 = [27850, 32550, 35350]
# bracket3 = [59900, 78850, 85650]
# bracket4 = [134200, 164550, 178650]
# bracket5 = [289950, 357700, 388350]
# bracket6 = math.inf
# 
# percentTax1 = [0, .1, .1]
# percentTax2 = [.15, .15, .15]
# percentTax3 = [.28, .25, .25]
# percentTax4 = [.31, .28, .28]
# percentTax5 = [.36, .33, .33]
# percentTax6 = [.396, .35, .35]

# plan2000 = [2650, 27850, 59900, 134200, 289950]
# plan2008 = [8025, 32550, 78850, 164550, 357700]
# plan2014 = [8700, 35350, 85650, 178650, 388350]
# 
# percent2000 = [0, .15, .28, .31, .36, .396]
# percent2008 = [.1, .15, .25, .28, .33, .35]
# percent2014 = [.1, .15, .25, .28, .33, .35]



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

	#	percent = round(100 * (calculate_tax(adjustedIncome)/grossIncome), 2)

		tax2000 = calculate_tax(grossIncome, 0)
		tax2008 = calculate_tax(grossIncome, 1)
		tax2014 = calculate_tax(grossIncome, 2)
		
		percent2000 = round(100 * (tax2000/grossIncome), 2)
		percent2008 = round(100 * (tax2008/grossIncome), 2)
		percent2014 = round(100 * (tax2014/grossIncome), 2)

		print()
		print("Results for the 2000 plan")
		print("Taxes owed: ${}".format(tax2000))
		print("Percent of gross: {}%".format(percent2000))
		print("Net income: ${}".format(grossIncome - tax2000))
		print()
		
		print("Results for the 2008 plan")
		print("Taxes owed: ${}".format(tax2008))
		print("Percent of gross: {}%".format(percent2008))
		print("Net income: ${}".format(grossIncome - tax2008))
		print()

		print("Results for the 2014 plan")
		print("Taxes owed: ${}".format(tax2014))
		print("Percent of gross: {}%".format(percent2014))
		print("Net income: ${}".format(grossIncome - tax2014))
		print()
		
		x=0


# print("Your efficiency overflow is {}".format(overflowIncome))



