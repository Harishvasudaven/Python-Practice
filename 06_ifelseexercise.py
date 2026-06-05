print("Question 1")
mark = int(input("mark : "))
if (mark>35):
    print("pass")
else :
    print("fail")

print("Question 2")
income = int(input("income :"))
if (income >7000):
    print("Not Eligible for Scholership")
else:
    print("Eligible for Scholership")

print("Question 3")
number = int(input("Enter a number :"))
if (number%3==0 and number%5==0):
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 and 5")

print("Question 4")
number=int(input("Enter a number : "))
if(number%2==1):
    print("The number is odd")
else:
    print("The number is even")

print("Question 5")
score=int(input("Enter Score:"))
if(score<35):
    print("Poor Student")
elif(35<score<70):
    print("Average Student")
elif(70<score<=100):
    print("Good Student")
else:
    print("Invalid input")
