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
FMT_SPEC = "{0:,.2f}"
#FMT_SPEC = "{0:.2f}"
max_len = len( FMT_SPEC.format(total_ctc) )

def fmt_num(val, max_len):
    return FMT_SPEC.format(val).rjust(max_len)

print("Tax Computation")
print("---------------")
print("           Total CTC : {0}".format(fmt_num(total_ctc, max_len)))
print("               Basic : {0}".format(fmt_num(basic, max_len)))
print("Additional Allowance : {0}".format(fmt_num(additional_allowance, max_len)))
print("   Net Annual Salary : {0}".format(fmt_num(net_annual_salary, max_len)))
print("  Net Monthly Salary : {0}".format(fmt_num(net_montly_salary, max_len))) 
print("           Total Tax : {0}, ( slab : {1} )".format(fmt_num(tax, max_len), slab)) 


'''
Format the report in such a way all the amounts are properly alligned.
Also have control to print number with or without comman seperation.

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


TODO:

Align in such a way it leaves no left padding for the biggest number.

Problem :
a. For a big number, the alignment is not preserved.

	$ python tax.py 3000000000000000
	Tax Computation
	---------------
			   Total CTC : 3,000,000,000,000,000.00
				   Basic : 1,200,000,000,000,000.00
	Additional Allowance : 1,800,000,000,000,000.00
	   Net Annual Salary : 2,759,999,999,999,800.00
	  Net Monthly Salary : 229,999,999,999,983.34
			   Total Tax : 827,999,999,549,940.00, ( slab : 0.30 % )

b. For a smaller number, the alignment preserved but lot of leading empty space.
	$ python tax.py 300000
	Tax Computation
	---------------
			   Total CTC :      300,000.00
				   Basic :      120,000.00
	Additional Allowance :      180,000.00
	   Net Annual Salary :      275,800.00
	  Net Monthly Salary :       22,983.33
			   Total Tax :        1,290.00, ( slab : 0.05 % )


Expected Result :

	$ python tax.py 3000000000000000
	Tax Computation
	---------------
			   Total CTC : 3,000,000,000,000,000.00
				   Basic : 1,200,000,000,000,000.00
	Additional Allowance : 1,800,000,000,000,000.00
	   Net Annual Salary : 2,759,999,999,999,800.00
	  Net Monthly Salary :   229,999,999,999,983.34
			   Total Tax :   827,999,999,549,940.00, ( slab : 0.30 % )


	$ python tax.py 300000
	Tax Computation
	---------------
			   Total CTC : 300,000.00
				   Basic : 120,000.00
	Additional Allowance : 180,000.00
	   Net Annual Salary : 275,800.00
	  Net Monthly Salary :  22,983.33
			   Total Tax :   1,290.00, ( slab : 0.05 % )


'''


