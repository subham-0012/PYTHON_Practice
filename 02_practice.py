# Lecture 1

# a=input("enter the string: ")
# b=0
# for c in a:
#     if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
#         b+=1
# print(f"the number of vowels in {a} is {b}")

# a=int(input("Enter the value of a: "))
# b=int(input("Enter the value of b: "))
# c=int(input("Enter the value of c: "))
# if(a==b and a==c):
#     print("Its an equilateral triangle")
# if((a==b and a!=c)or(a==c and a!=b)or(c==b and a!=b)):
#     print("Its an isoscales triangle")
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print(area)

# a=input("Enter your name: ")
# print(f"Hi {a}!!\nWelcome to Python Class")

# import math
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print(f"The sum of a and b is : {a+b}")
# print(f"The difference of a and b is : {a-b}")
# print(f"The product of a and b is : {a*b}")
# print(f"The quotient of a and b is : {a/b}")
# print(f"The remainder of a and b is : {a%b}")
# print(f"The result of log(a) : {math.log(a,10)}")
# print(f"The power of a^b : {a**b}")

# a=int(input("Enter the amount: "))
# numberof50=int(a/50)
# numberof20=int((a%50)/20)
# numberof10=int(((a%50)%20)/10)
# numberof5=int((((a%50)%20)%10)/5)
# numberof2=int(((((a%50)%20)%10)%5)/2)
# numberof1=int(((((a%50)%20)%10)%5)%2)
# print(f"The number of 50 is {numberof50}")
# print(f"The number of 20 is {numberof20}")
# print(f"The number of 10 is {numberof10}")
# print(f"The number of 5 is {numberof5}")
# print(f"The number of 2 is {numberof2}")
# print(f"The number of 1 is {numberof1}")

# a=int(input("Enter a number: "))
# if a<0:
#     print("Enter a positive number")
# elif a>0:
#     if a%2==0:
#         print("It is an Even number")
#     else:
#         print("It is an odd number")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print("\n")

# while(True):
#     a=input("Enter the number to get the sum or type quit to exit")
#     if(a=='quit'):
#         break
#     else:
#         a=int(a)
#         if(a>1000):
#             print("Enter the value less than 1000")
#         else:
#             sum=0
#             while(a>0):
#                 sum+=(a%10)
#                 a=int(a/10)
#             print(sum)

# for i in range(1,10001):
#     sum=0
#     for j in range(1,i):
#         if(i%j==0):
#             # print(i,j)
#             sum+=j
#     if(sum==i):
#         print(i)

# fees=10000
# cost=0
# for i in range(1,15):
#     fees+=fees*.05
#     if(i==10):
#         print(f"The Tution fees after 10 years is {int(fees)}")
#     if(i>10):
#         cost+=fees
# print(f"The cost for 4 years after 10 years is {int(cost)}")

# Lecture 2

# l1=[2,9,7,5,3,74,958,25,89,14,25,47,48]
# for i in l1:
#     if(i%2==0):
#         print(i)

# l1=[]
# a=0
# while(a!=-1):
#     a=int(input("enter the number: "))
#     if(a==-1):
#         break
#     else:
#         l1.append(a)
# print(l1)
# if l1[0]>l1[1]:
#     max=l1[0]
#     max2=l1[1]
# else:
#     max=l1[1]
#     max2=l1[0]
# for i in l1:
#     if i>max:
#         max2=max
#         max=i
#     elif i>max2:
#         max2=i
# print(max2)

# l1=[]
# while(True):
#     a=int(input("enter the number: "))
#     if(a==-1):
#         break
#     else:
#         l1.append(a)
# print(l1)
# print("condition starts")
# a=int(input("Enter the number: "))
# while(a>0):
#     num=l1[0]
#     l1=l1[1:]
#     l1.append(num)
#     a-=1
# print(l1)

# l1=[]
# l2=[-1]
# a=0
# alreadypresent=0
# while(True):
#     a=int(input("enter a number: "))
#     if(a!=-1):
#         l1.append(a)
#     else:
#         break
# for item in l1:
#     for item1 in l2:
#         if(item==item1):
#             alreadypresent=1
#             break
#     if(alreadypresent):
#         break
#     else:
#         l2.append(item)
# l2=l2[1:]
# print(l2)

# l=[[1,2],[3,4],[5,6]]
# l2=[]
# for item in l:
#     for j in item:
#         l2.append(j)
# print(l2)