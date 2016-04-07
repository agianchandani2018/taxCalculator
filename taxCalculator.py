#Author: Ami
#Date: April XX





#---------------------------------Main Program--------------------------------------------

#2000 plan
bracket1 = 2650
bracket2 = 27850
bracket3 = 59900
bracket4 = 134200
bracket5 = 289950
#bracketMax = infinity

percentTax1 = 0
percentTax2 = .15
percentTax3 = .28
percentTax3 = .31
percentTax4 = .36
percentTax5 = .396




grossIncome = int(input("How much money did you make? "))

if grossIncome <= bracket1:
	totalTaxesOwed = percentTax1 * grossIncome
	
if grossIncome > bracket1 and grossIncome <= bracket2:
	totalTaxesOwed = percentTax1 * bracket1
	overflowIncome = grossIncome - bracket1
	totalTaxesOwed = overflowIncome * percentTax2
	
print(grossIncome)
print(totalTaxesOwed)	






























# plan = input("Which plan are you using? ")
# income = int(input("How much gross income did you make? "))
# grossIncome = income
# 
# #untaxed = how much money you made from the top bracket
# 
# if plan == "2000":
# 
# 	if income < 2650 and income >= 0:
# 		income = income
# 		
# 	if income < 27850 and income >= 2650:
# 		untaxed = income - 2650
# 		taxedFromIncome = .85 * (untaxed)
# 				
# 	if income < 59900 and income >= 27850:
# 		taxedFromIncome = .85 * (25200)
# 		untaxed = income - 27850
# 		taxedFromIncome += .72 * (untaxed)
# 		
# 	if income < 134200 and income >= 59900:
# 		taxedFromIncome = .72 * (32050)
# 		untaxed = income - 59900
# 		taxedFromIncome += .69 * (untaxed)
# 		
# 	if income < 289950 and income >= 134200:
# 		taxedFromIncome = .69 * (74300)
# 		untaxed = income - 134200
# 		taxedFromIncome = .64 * (untaxed)
# 				
# 	if income >= 289950:
# 		taxedFromIncome = .604 * (155750)
# 		untaxed = income - 289950
# 		#taxedFromIncome = 
# 		
# 
# #elif plan == "2008":
# 
# #elif plan == "2014": 
# 
# print("Income = {}" .format(income))
# print("Untaxed = {}" .format(untaxed))
# print("Taxed from income = {}" .format(taxedFromIncome))
# 
# 
# # taxes = round(grossIncome, 2) - round(income, 2)
# # 
# # print("Your net income is ${}".format(round(income, 2)))	
# # print("You owe ${} in taxes".format(taxes))
# # 
# # percentGross = round((income / grossIncome), 2)*100
# # print("Your percent gross is {}%".format(percentGross))