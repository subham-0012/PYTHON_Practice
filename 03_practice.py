# a=0
# b=-1
# c=1
# while(c!=-1):
#     c=int(input("enter the number: "))
#     if(c>a):
#         b=a
#         a=c
#     elif(c>b):
#         b=c
# print(f"the largest is {a} and second largest is {b}")

# l1=[3,4,5,6,7,8,12,18]
# position=int(input("enter th position: "))
# for i in range(position):
#     p=l1.pop(0)
#     l1.append(p)
# print(l1)

# l1=[]
# size=int(input("enter the size of list: "))
# for i in range(0,size):
#     l1.append(int(input("enter the element: ")))
# for j in range(0,size):
#     count=0
#     for k in range(0,size):
#         if(j!=k):
#             if(l1[j]==l1[k]):
#                 count=1
#     if(count==0):
#         print(l1[j])

# l1=[[1,2],[3,4],[5,6]]
# l2=[]
# for i in l1:
#     for j in i:
#         l2.append(j)
# print(l2)

# s1="Python is fun to learn"
# s2=""
# s3=""
# for i in range(0,len(s1)):
#     if(s1[i]!=' '):
#         s2+=s1[i]
#         if(i==len(s1)-1):
#             s2+=" "
#             s2+=s3
#             s3=s2
#             s2=""
#     else:
#         s2+=" "
#         s2+=s3
#         s3=s2
#         s2=""
# print(s3)

# s1="United States of America"
# s2=""
# for i in range(0,len(s1)):
#     if(ord(s1[i])>=65 and ord(s1[i])<=90):
#         s2+=s1[i]
# print(s2)

# s1=input("enter a string: ")
# length=len(s1)
# d1={}
# for i in range(length):
#     if(d1.get(s1[i])==None):
#         d1[s1[i]]=1
#     else:
#         num=d1[s1[i]]
#         d1[s1[i]]+=1
# k=''
# l=0
# for i,j in d1.items():
#     if(j>l):
#         l=j
#         k=i
# print(k)

# num=int(input("enter the number: "))
# grade = {'A':(96,100),'B':(86,95),'C':(76,85),'D':(56,75),'E':(0,55)}
# for i,j in grade.items():
#     if(num>j[0]):
#         print(i)
#         break

# s1=input("enter a string: ")
# length=len(s1)
# d1={}
# for i in range(length):
#     if(d1.get(s1[i])==None):
#         d1[s1[i]]=1
#     else:
#         num=d1[s1[i]]
#         d1[s1[i]]+=1
# print(d1)

# s1=input("enter a string: ")
# length=len(s1)
# k=int(input("enter the kth non repeating word: "))
# d1={}
# for i in range(length):
#     if(d1.get(s1[i])==None):
#         d1[s1[i]]=1
#     else:
#         num=d1[s1[i]]
#         d1[s1[i]]+=1
# for i,j in d1.items():
#     if(j==1):
#         k-=1
#         if(k==0):
#             print(i)