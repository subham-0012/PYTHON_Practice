# chapter 1

# Author=SUBHAM
# '''hello my name is SUBHAM GUPTA # triple quote can be used as a multiline comment as well as to print multiline string
#  I am a student'''
# print('''hello my name is SUBHAM GUPTA
#     I AM a student of SRM University''')
# import os
# print("Hello world")

# practice set 1

# from playsound import playsound
# playsound('play.mp3')

# import os
# print(os.listdir())


# chapter 2

# we can use triple quote to write strings in which we can use single and double quotes
# a= '''SUBHAM 'a good boy' and "a very good boy"'''
# d = None
# print(type(None))
# print("the value of 3+4 is ",3+4)
# logical operators are and or not
# typecasting=> int(a)

# to take input from user we use input function
# a=input("enter your name")
# print(a)
# a=input("enter a value")
# print(type(a))
# a=int(a)
# print(type(a))
# a=input("enter a value")
# b=input("enter another value")
# a=int(a)
# b=int(b)
# print("the value of summation of a and b is",(a+b)**3) #for calculating power


# chapter 3

# concatination in strings
# a="Good Morning, a"
# b="SUBHAM"
# c=a+b
# print(c)
# print(len(a))
# print(a.endswith(",a"))
# print(a.startswith("Good"))
# print(len(a))
# print(a[0:len(a)]) #this is splicing from 0 to 2
# print(a[:len(a)]) #this is splicing from 0 to 2
# print(a[0:]) #this is splicing from 0 to 2
# print(a[-4:-1]) #this is using negative value
# print(a[-4:-1:3]) #this is using negative value and third parameter is skipping


# chapter 4

# a=[1,3,2,4,5] #list
# print(a)
# print(a[0])
# a[0]=98 #lists are mutable
# print(a)
# we can create a list with items of different types
# a=["SUBHAM",19,True,'a',23.45]
# a[0]="GUPTA"
# print(a[0:len(a):2]) #slicing in list
# print(a)

# methods in list
# l1=[3,4,1,8,6,0]
# l2=l1.sort() # this line will print none because l1.sort() will change l1 and return none
# l1.sort() #this line will sort l1
# l1.reverse() #this line will reverse sorted l1
# l1.append(9) #this line will append at the end of l1
# l1.insert(3,8) #this line will insert 8 at index 3
# l1.insert(3,8) #this line will insert 8 at index 3
# l1.pop(3) #this line remove element at index 3
# print(l1)
# l=[]
# a=1
# n=int(input())
# for i in range(n):
#     t=[]
#     for j in range(3):
#         t.append(a)
#         a+=1
#     l.append(t)
# print(l)

# tuple
# t=(1,2,5,3) #tuple are immutable
# t1=() #empty tuple
# t2=(1,) #for creating a tuple with single element we need to give comma in last else it will be understood as a number not tuple
# print(t.count(1))
# print(t.index(5))
# print(t)


# chapter 5

# dictionary

# myDict={
#     "name":"SUBHAM",
#     "age":19,
#     "role":"student",
#     "list":[1,2,2],
#     "newDict":{"surname":{"mysurname":"Gupta"}} #nested dictionary
# }
# print(myDict["age"])
# print(myDict["list"])
# print(myDict["newDict"])
# print(myDict["newDict"])
# print(myDict["newDict"]["surname"]["mysurname"])
# methods in a dictionary
# print(myDict.keys()) #printing keys of a dictionary
# print(myDict.values()) #printing values of a dictionary
# print(myDict.items()) #printing key values of a dictionary in tuples
# updateDict={
#     "kes":"frn"
# }
# myDict.update(updateDict) #update the dictionary by adding another dictionary
# print(myDict.items())
# print(myDict["name2"]) #throws an error if key is not present
# print(myDict.get("name2")) #return none if key is not present

#sets in python
# a={1,3,4,5,"4",4.1}
# print(a)
# a={1,3,4.1,"4",4,5,1} #sets are non repetitive so this second 1 will not appear
# a={1,3,4,"4",4.0} #here length of set is 4 its not 5 bcz for python 4 and 4.0 are same
# print(a)
# a={} #this is an empty dictionary not an empty set
# an empty set can be created using below syntax
# b=set() #empty set
# b.add(4)
# b.add(7)
# b.add((7,3)) #we can add tuple in a set
# b.add([7,3]) #we cannot add list in a set
# b.add({7,3}) #we cannot add dictionary in a set
# print(b)
# print(len(b))
# b.remove(4)
# print(b.pop()) #removes a random value
# methods in sets


# chapter 6

# conditionals in python
# '''
# if (1==2):
#     print("hello")
# elif (3==2):
#     print("hello me")
# else:
#     print("hello me new")
# '''
# a=None
# if(a is None): #a is none then this condition is executed
#     print("yes")
# else:
#     print("no")

# a=[45,35]
# if(45 in a):
#     print("yes")
# else:
#     print("no")


# chapter 7
# i=0
# while(i<=10):
#     print(i)
#     i=i+1

# l1=[3,4,1,8,6,0]
# i=0
# while(i<len(l1)):
#     print(l1[i] )
#     i+=1

# l1=[3,4,1,8,6,0]
# for new in l1:
#     print(new)

# range in python
# for i in range(10): #this prints the number from 0 to 9
#     print(i)
# for i in range(1,10): #this prints the number from 1 to 9
#     print(i)
# for i in range(1,10,2): #this prints the number from 1 to 9 with step size 2
#     print(i)

# for loop with else
# for i in range(1,10):
#     print(i)
# else: #this condn will execute after the for loop finishes
#     print("hello")
# for i in range(1,10):
#     print(i)
#     if(i==5):
#         break
# else: #here this condn will not execute because for loop finishes by break statement not by condition
#     print("hello")
# for i in range(1,10):
#     if(i==5):
#         continue
#     print(i)
# else: #this condn will execute after the for loop finishes
#     print("hello")

# i=3
# if i>0:
#     pass
# while(i>6):
#     pass
# else: #this condn will execute after the for loop finishes
#     print("hello")

# function
# def sum(a,b):
#     pass

# using fstring
# print(f"{3}+{4}={3+4}") #this way we can write number and string easily

# l1=["Subham","Shreya","Shruti","Ankit","Raj","Ravinder"]
# for name in l1:
#     if(name.startswith("S")):
#         print("Hello "+name)

# number=int(input("Enter the number"))
# i=2
# while(i<number):
#     if(number%i==0):
#         print("not a prime number")
#         break
#     i+=1
# else:
#     print("number is prime")

# number=int(input("Enter the number"))
# i=1
# sum=1
# while(i<=number):
#     sum*=i
#     i+=1
# print(sum)

# number=int(input("Enter the number"))
# for i in range(number+1):
#     print("* "*(i))

# number=int(input("Enter the number"))
# number2=number
# for i in range(1,number+1):
#     for j in range(number2):
#         print(" ", end="")
#     number2-=1
#     for j in range(1,i+1):
#         print("* ",end="")
#     print("\n")


# chapter 8

# def percent(marks):
#     return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
# mark=(1,2,3,4)
# sum=percent(mark)
# print(sum)

# def greet(name="stranger"):
#     print("hello "+name)
# greet("subham")
# greet()

# def factorial(n):
#     fact=1
#     if(n>0):
#         fact=n*factorial(n-1)
#     return fact
# print(factorial(0))


# chapter 9

# f=open("sample.txt","r") #any file name sample.txt
# data=f.read() #reading data from file
# data=f.readline() #reading a line from file
# data=f.read(5) #reading data from file with 5 characters to be read
# print(data)
# f.close()
# with open('another.txt','w') as f: #dont need to be closed
    # f.write()


# chapter 10

# it implement DRY principle
# def sum(a,b): #procedural oriented programming
#     return a+b
# print(sum(10,15))

# class Number:
#     def sum(self):
#         self.c=self.a+self.b
#         return self.c

# num=Number()
# num.a=10
# num.b=34
# s=num.sum()

# class RailwayForm:
#     formType="RailwayForm"
#     def printing(self):
#         print(self.name+self.train)

# subhamForm=RailwayForm()
# subhamForm.name="subham"
# subhamForm.train="Rajdhani express"
# subhamForm.printing()
# # print(subhamForm.formType)

# class subham:
#     def printf(self):
#         print(f"name is {self.name}")
#         print(f"age is {self.age}")
# about_subham=subham()
# about_subham.name="subham"
# about_subham.age=19
# about_subham.printf()
# class aboutme:
#     def printf(self,s=subham()):
#         print("hello")
#         print(self.name)
#         s.printf()

# newme=aboutme()
# newme.name="subham"
# newme.printf(about_subham)

# class name:
#     new="hey"
#     def hello(self):
#         print(f"hello {self.name} {self.new}")
#     @staticmethod # to use if we dont want to pass self in function
#     def newhello():
#         print("hello")
# subham=name()
# subham.name="subham"
# subham.hello()
# name.new="hey2" #to change a variable in a class
# class newname:
#     def hello(self,s=name()):
#         print(f"hello {s.name}")
# subham1=newname()
# subham1.hello(subham)

# class Number:
#     def __init__(self):
#         print("employee is created") # default constructor it always take self argument and can take other alguments also
#     def sum(self):
#         self.c=self.a+self.b
#         return self.c
# num=Number()
# num.a=10
# num.b=34
# s=num.sum()
# print(s)

# class Number:
#     def __init__(slf,empname,age):
#         slf.name=empname
#         slf.age=age
#         print(f"employee is created {slf.name} with age {slf.age}") #parameterised constructor it always take self argument and can take other alguments also
#     def sum(self):
#         self.c=self.a+self.b
#         return self.c
# num=Number("subham",19)
# num.a=10
# num.b=34
# s=num.sum()
# print(s)


# chapter 11

# class subham:
#     def __init__(self):
#        print("hi")
#     def base_printf(self):
#         print(f"name is {self.name}")
#         print(f"age is {self.age}")
# # about_subham=subham()
# # about_subham.name="subham"
# # about_subham.age=19
# # about_subham.printf()
# class aboutme(subham):                  #inheritence
#     def derived_printf(self):
#         print("hello")
#         print(self.name)

# newme=aboutme()
# newme.name="subham"
# newme.age=19
# newme.base_printf()
# newme.derived_printf()

# class base:
#     def __init__(self,name):
#         self.name=name
#         print("hello base")
#     def basePrint(self,number1):
#         print(f"the number for {self.name} is {number1}")
# class derived(base):
#     def __init__(self, name,number):
#         super().__init__(number)  # calling a parameterised constrctor of base class in single inheritence here we dont give self as parameter
#         self.name=name
#         self.number=number
#         print("hello derived")
#     def derivedPrint(self):
#         print(f"the name is {self.name}")
# subham=derived("subham",10)
# subham.basePrint(5)
# subham.derivedPrint()

# class base1: #multiple inheritence
#     def __init__(self,name):
#         self.name=name
#         print("hello from base1")
#     def base1Print(self,number1):
#         print(f"the number for {self.name} is {number1}")
# class base2:
#     def __init__(self,name):
#         self.name=name
#         print("hello from base2")
#     def base2Print(self,number1):
#         print(f"the number for {self.name} is {number1}")
# class derived(base1,base2):
#     def __init__(self, name,number):
#         base1.__init__(self,name)  # calling a parameterised constrctor of base class 1 from parameterised class here we give self as parameter
#         self.name=name
#         self.number=number
#         print("hello derived")
#     def derivedPrint(self):
#         print(f"the name is {self.name}")
# subham=derived("subham",10)

# class base1: # multilevel inheritence
#     def __init__(self,name):
#         self.name=name
#         print("hello from base1")
#     def base1Print(self,number1):
#         print(f"the number for {self.name} is {number1}")
# class base2(base1):
#     def __init__(self,name):
#         super().__init__(name)
#         self.name=name
#         print("hello from base2")
#     def base2Print(self,number1):
#         print(f"the number for {self.name} is {number1}")
# class derived(base2):
#     def __init__(self, name,number):
#         super().__init__(name)  # calling a parameterised constrctor of base class 2 from parameterised class here we give self as parameter
#         self.name=name
#         self.number=number
#         print("hello derived")
#     def derivedPrint(self):
#         print(f"the name is {self.name}")
# subham=derived("subham",10)

# NOTE---->super.()functionname() #can execute the function of derived class along with base class

# class employee:
#     company="camel"
#     salary=100
#     location="Delhi"
#     def changeSalary(self,sal):
#         self.__class__.salary=sal # to change the value of class variable not instance
#     @classmethod
#     def changeSalaryofClass(cls,sal):
#         cls.salary=sal # to change the value of class variable not instance
# e=employee()
# print(e.salary)
# print(e.changeSalary(455))
# print(e.salary)
# print(employee.salary)

# class Employee:
#     company="Bharat Gas"
#     salary=5600
#     salarybonus=500
#     # totalSalary=6100 do not hardcode
#     # property decorator or getter
#     @property  #now below function is a property not a function
#     def totalSalary(self):
#         return self.salary+self.salarybonus
#     @totalSalary.setter
#     def totalSalary(self,val):
#         self.salarybonus=val-self.salary
# e=Employee()
# print(e.totalSalary)
# e.totalSalary=5800
# print(e.salary)
# print(e.salarybonus)

# operator overloading
# class Number:
#     def __init__(self,num):
#         self.num=num
#     def __add__(self,num2):
#         print("lets add")
#         return self.num+num2.num
# n1=Number(5)
# n2=Number(10)
# sum=n1+n2
# print(sum)


# chapter 12 # Exception Handling

# while(True):
#     print("press q to quit ")
#     a=input("enter a number")
#     if(a=='q'):
#         break
#     try:
#         a=int(a)
#         if(a>6):
#             print("you enter a number greater than 6")
#         else:
#             print("you enter a number less than 6")
#     except Exception as a:
#         print(a)

# zero division error
# try:
#     a= int(input("enter the numerator"))
#     b= int(input("enter the denominator"))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print("you entered zero in denominator")
# except ValueError as e:
#     print("you enter wrong value")
# except:
#     print("all other types of error are handled here")

# def increment(num):
#     try:
#         return int(num)+1
#     except Exception as e:
#         pass
#         print("exception occured")
# a=increment('asd25')
# print(a)
# print("hello")

# try with else #this else will run if try run successfully
# try:
#     a= int(input("enter the numerator"))
#     b= int(input("enter the denominator"))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print("you entered zero in denominator")
# except ValueError as e:
#     print("you enter wrong value")
# except:
#     print("all other types of error are handled here")
# else:
#     print("no error occured")

# try with finally
# try:
#     a= int(input("enter the numerator"))
#     b= int(input("enter the denominator"))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print("you entered zero in denominator")
# except ValueError as e:
#     print("you enter wrong value")
# except:
#     print("all other types of error are handled here")
#     exit()
# else:
#     print("no error occured")
# finally:
#     print("finally executed")

# def greet(name):
#     print(f"good morning, {name}")
# if __name__=="__main__": #now the below code will execute only if it is being executed in current file not getting imported in another file
#     n=input("enter your name ")
#     greet(n)

# to import a function from another file we save both file name starting with m and then do import MthenName

# global keyword
# a=54
# def func1():
#     global a # using global keyword
#     print(a)
#     a=8
# func1()
# print(a)

# enumerate function in python
# list1=[2,54,54.23,True,"SUBHAM"]
# for index,item in enumerate(list1):
#     print(index,item)

# list comprehension
# a=[3,6,7,8,9,2,4,23,75,23,123,67]
# b=[] # first method
# for item in a:
#     if(item%2==0):
#         b.append(item)
# b=[i for i in a if(i%2)==0] # second method
# print(b)

# a=int(input("enter your number "))
# b=[a*i for i in range(1,11)]
# print(b)


# chapter 13
# '''
# pip install --user virtualenv
# python -m virtualenv venv
# .\venv\Scripts\activate.ps1
# '''

# lambda functions
# def func(a):
#     return a+5

# func=lambda a:a+5
# square=lambda x:x*x
# sum=lambda a,b,c:a+b+c
# x=556
# print(func(x))
# print(square(9))
# print(sum(1,6,10))

# l=["Camera","Laptop","Phone","Ipad","Harddisk","Nvidia Graphic 3080 Card"]
# sentence=" and ".join(l)
# print(sentence)

# formatting a string
# name="SUBHAM"
# age=19
# a="This is {} and his age is {}".format(name,age)
# print(a)

# map filter and reduce
# def square(x):
#     return x*x
# l=[1,2,4]
# # # method 1
# # l1=[]
# # for item in l:
# #     l1.append(square(item))
# # print(l1)
# # method 2
# print(list(map(square,l)))

# def greater_than_5(num):
#     if(num>5):
#         return True
#     else:
#         return False
# l=[1,2,3,4,9,11,25,78,98,356,982]
# print(list(map(greater_than_5,l))) #give the results in the form of a list
# print(list(filter(greater_than_5,l)))  # give the value for which the result is true
 
# from functools import reduce
# sum=lambda a,b:a+b
# l=[1,2,3,4]
# value=reduce(sum,l) #this function perform 1 operation with 1st 2 value then the result will be processed with the next value and so on and then final value will be send
# print(value)

# Flask
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return '''<!doctype html>
# <html lang="en">
#   <head>
#     <!-- Required meta tags -->
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1">

#     <!-- Bootstrap CSS -->
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

#     <title>Hello, world!</title>
#   </head>
#   <body>
#     <h1>Hello, world!</h1>

#     <!-- Optional JavaScript; choose one of the two! -->

#     <!-- Option 1: Bootstrap Bundle with Popper -->
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

#     <!-- Option 2: Separate Popper and Bootstrap JS -->
#     <!--
#     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
#     -->
#   </body>
# </html>'''
# if __name__=="__main__":
#     app.run(debug=True)