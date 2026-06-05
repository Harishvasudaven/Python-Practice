print("Mini Calculator")

a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
operator=input("add/sub/mul/div:")
if(operator=="add"):
    print(a+b)
elif(operator=="sub"):
    print(a-b)
elif(operator=="mul"):
    print(a*b)
elif(operator=="div"):
    print(a/b)
else:
    print("Invalid operation")
