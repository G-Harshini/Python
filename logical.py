#Logical operators are
#1.and 
age=25
Citizen=True
print(age>=18 and citizen == True)

age=16
Citizen=True
print(age>=18 and citizen == True)

#2.or
hascard=False
hascash=True
print(hascard or hascash)

#3.not
is_logged_in=True
print(not is_logged_in)

#atm eligibele
balance=100000
withdraw=5000
print(withdraw>0 and withdraw<=balance)

#students scholorship eligibility
marks=float(input("Enter marks"))
attendance=float(input("enter attendance"))
eligible=(marks>=85 and attendance>=75)

