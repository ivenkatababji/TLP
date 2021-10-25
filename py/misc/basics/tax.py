import sys 
total_ctc = float(sys.argv[1]) 
 
basic = total_ctc * 0.4 
additional_allowance = total_ctc * 0.6 
employee_contribution = basic * 0.12 
employer_contribution = basic * 0.08 
PROFESSIONAL_TAX = 200 
 
total_deductions = employer_contribution + employee_contribution + PROFESSIONAL_TAX 
net_annual_salary = total_ctc - total_deductions 
net_montly_salary = net_annual_salary / 12 

#tax computation sheet 
tax = 0
slab = None
if (net_annual_salary <= 250000): 
   tax = 0 
   slab = "0 %"
elif (net_annual_salary <= 500000): 
   tax += (net_annual_salary - 250000) * 0.05 
   slab = "0.05 %"
elif net_annual_salary <= 750000: 
   tax += (net_annual_salary - 500000) * 0.10 
   slab = "0.10 %"
elif net_annual_salary <= 1000000: 
   tax += (net_annual_salary - 750000) * 0.15 
   slab = "0.15 %"
elif net_annual_salary <= 1500000: 
   tax += (net_annual_salary - 1000000) * 0.20 
   slab = "0.20 %"
else:  #net_annual_salary > 1500000 
   tax += (net_annual_salary - 1500000) * 0.30 
   slab = "0.30 %"
 
#
#Generate the Report 
#
print("Tax Computation")
print("---------------")
print("           Total CTC : {0:>15,.2f}".format(total_ctc)) 
print("               Basic : {0:>15,.2f}".format(basic)) 
print("Additional Allowance : {0:>15,.2f}".format(additional_allowance)) 
print("   Net Annual Salary : {0:>15,.2f}".format(net_annual_salary)) 
print("  Net Monthly Salary : {0:>15,.2f}".format(net_montly_salary)) 
print("           Total Tax : {0:>15,.2f}, ( slab : {1} )".format(tax, slab)) 


'''
TODO :
Format the report in such a way all the amounts are properly alligned.

Current Report
--------------

	(pyenv) $ python tax.py 1000000.0
	Tax Computation
	---------------
			   Total CTC : 1000000.0
				   Basic : 400000.0
	Additional Allowance : 600000.0
	   Net Annual Salary : 919800.0
	  Net Monthly Salary : 76650.0
			   Total Tax : 25470.0
				Tax Slab : 0.15 %



Expected Report
---------------

	(pyenv) $ python tax.py 1000000.0
	Tax Computation
	---------------
				Tax Slab : 0.15 %

			   Total CTC : 1000000.0
				   Basic :  400000.0
	Additional Allowance :  600000.0
	   Net Annual Salary :  919800.0
	  Net Monthly Salary :   76650.0
			   Total Tax :   25470.0
				

Ref :
1. https://www.kite.com/python/answers/how-to-right-align-a-number-in-python
'''


