# Name:Sounak Ray
#Roll_no:21CO119

b=input("Enter Name of person: ")
a = int(input("Enter basic salary of the person in Rs is: "))
HRA = (10*a)/100
TA = (5*a)/100
Gross = a + HRA + TA
print("Gross salary of the person in Rs is: ",Gross)
Taxes = (2*Gross)/100
Net = Gross - Taxes
print("Net salary of "+str(b)+" in Rs is: ",Net)
