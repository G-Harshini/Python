"""
If-Else

print("Enter correct age")
age=int(input("Enter age"))
if (age>=18):
    print("Eligible for vote")
    print("Eligible for bike ride")
else:
    print("Not eligible for vote")
    print("Not eligible for bike ride")
print("All details must be True")


If Else Elif


a=int(input("Enter a number"))
if(a==1):
    print("Mrdu")
elif(a==2):
    print("Mbu")
elif(a==3):
    print("Gitam")
else:
    print("Select another college")


Nested if



a=int(input("Enter a number"))
if(a>0):
    if(a<50):
        print("Number is lessthan 50")
    else:
        print("Number is greater than 50")
else:
    print("It is negaive number")
a=int(input("Enter A"))
b=int(input("Enter B"))
if(a==b):
    print("Both are Equal")
else:
    print("Not equal")

a=int(input("Enter a number"))
if(a%2==0):
    print("Even  number")
else:
    print("Odd number")



number=int(input("Enter number"))
if(number%5==0):
    print("Divisable by 5")

Temperature=float(input("Enter temperature"))
if(Temperature>40):
    print("High Temperature")
marks=int(input("Enter marks"))
if(marks>=40):
    print("pass")
else:
    print("Fail")
number=int(input("Enter number"))
if(number>100):
    print("Number greater than 100")
else:
    print("Number Less than 100")


a=int(input("Enter A"))
b=int(input("Enter B"))
c=int(input("Enter c"))

if(a>= b and a>=c):
    print("Largest is a=",a)
elif(b>= a and b>=c):
    print("Largest is b=",b)
else:
    print("Largest is c=",c)

Day=int(input("Enter Day"))
if(Day==1):
    print("Monday")
elif(Day==2):
    print("Tuesday")
elif(Day==3):
    print("Wednesday")
elif(Day==4):
    print("Thursday")
elif(Day==5):
    print("Friday")
elif(Day==6):
    print("Saturday")
elif(Day==7):
    print("Sunday")
else:
    print("Invalid")
a=float(input("Enter A"))
b=float(input("Enter B"))
operator=float(input("Enter operator(+ , _, *, %)"))
if (operator=="+"):
    print("a+b")
elif(operator=="-"):
    print("a-b")

    
a=input("Enter username")
b=input("Enter password")
username="Harshini"
password="Harshini@2008"
if(a==username):
    if(b==password):
        print("Login Successful")
    else:
        print("Wrong password")
else:
    print("wrong username")
Balance=10000
Amount=int(input("Enter amount need to debit"))
if(Balance>Amount):
    print("Amount Successfully Debited")
    print("Remaining Balance=", Balance-Amount)
else:
    print("Insuffiecient Balance")
marks=float(input("Enter marks"))
Attendance=float(input("Enter Attendence"))
if(marks>75):
    if(Attendance>75):
        print("Eligible for exam")
    else:
        print("Not Eligible for exam")
else:
    print("Not eligible for exam")
                         """
age=int(input("Enter age"))
Test=input("Enter Qualification")

if(age>=18):
    if(Test=="Qualified"):
        print("Issue License")
    else:
        print("Qualify Driving Test")
else:
    print("You are too young to Drive")

