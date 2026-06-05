print("Question 7")
Score=int(input("Score"))
if(Score>=70):
    Name=input("Enter Name :")
    Department=input("Enter Department :")
    Location=input("Enter Location :")
    print("You are Eligible")
else:
    print("You are Not Eligible")


print("Question 8")

salary=int(input("Enter salary : "))
age=int(input("Enter age : "))
if(salary>=20000 or age<25):
    loan=int(input("Enter loan amount : "))
    if(loan<=50000):
        print("You are eligible")
    else:
        print("Maximum loan amount is 50000")
else:
    print("Not eligible for loan")

    
print("Question 9")

mark1=int(input("mark1 : "))
mark2=int(input("mark2 : "))
mark3=int(input("mark3 : "))
mark4=int(input("mark4 : "))
mark5=int(input("mark5 : "))

add=mark1+mark2+mark3+mark4+mark5

avg=add/5

if(avg<35):
    print("Additional classes required")
else:
    print("You are good to go")
