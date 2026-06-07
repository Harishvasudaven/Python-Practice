for i in range(1,5):
    print(i)


for i in range(1,11):
    print(i,"X2=",2*i)

print("Question 1")

a=int(input("A="))
b=int(input("B="))
for i in range(a,b):
    print(i)

print("Question 2")

for i in range(1,11):
    if(i%2==0):
        print(i)

print("Question 3: Count the number of evn numbers from 1 to 10")

count=0
for i in range (1,11):
    
    if (i%2==0):
        count=count+1
print(count)
