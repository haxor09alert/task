# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         print(x)
#         print("Inside the function y",y)
#     inner()
#     print("z",z)
# outer()        

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         nonlocal z
#         z=z+1
#         print(x)
#         print("Inside the function y",y)
#     inner()
#     print("z",z)
# outer()        


# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         global y
#         y=y+1
#         print(x)
#         print("Inside the function y",y)
#     inner()
#     print("z",z)
# outer()        


# x=10
# def outer():
#     x=8
#     def inner():
#         x=4
#         print(x)
#         print("Inside the function x",x)
#     inner()
#     print("x",x)
# outer()        



#from tkinter import X


# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("inner:",x)
#     inner()
#     print("outer:",x)
# outer()        



# result= lambda n1,n2,n3:(n1+n2+n3,n1*n2*n3)
# print("Sum of three values:",result(10,20,25))


# add_sub=lambda x,y: (x+y,x-y)
# a,b= add_sub(5,2)
# print(a)
# print(b)


# li=[5,7,23,97,54,62,77,23,73,61]
# square_list=list(map(lambda x: x**2,li))

# print(square_list)


# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)


# data=[1,2,3,4,5,5,6,6,9,10]
# var=list(filter(lambda x: x%3==0,data))
# print(var)

# from functools import reduce

# li = [5,8,10,20,50,100]
# sum = reduce((lambda x,y: x+y), li)
# print(sum)



###########################################################

## TASK 3 ##
###########################################################
###########################################################


# TO PRINT MULTIPLICATION TABLE OF GIVEN NUMBER.
# number = int(input ("Enter the number to print mulclipation table: "))
# print ("The Multiplication Table of", number, "is")
# for i in range(1, 11):
#   print (number, 'x', i, '=', number * i)

# TO PRINT FIRST 10 NATURAL NUMBER.
# i = 1
# while i<=10:
#     print(i)
#     i+=1

# TO PRINT FIRST 10 EVEN NUMBERS.
# i = 2
# while i<=20:
#     print(i)
#     i+=2


# TO PRINT FIRST 10 ODD NUMBERS.
# i = 1
# while i <= 20:
#     print(i)
#     i+=2

#WRITE PYTHON PROGRAM TO PRINT SERIES: 10 20 30 ..... 300.
# i = 10
# while i<=300:
#     print(i , end="")
#     i = i + 10

#WRITE PYTHON PROGRAM TO PRINT SERIES: 105 98 .... 7.
# i = 105
# while i >= 7:
#     print(i, end = " ")
#     i = i - 7

#PYTHON PROGRAM TO PRINT THE REVERSED OF GIVEN LIST. a = [1,2,3,4]
# a= [1,2,3,4]
# b=[]
# length=len(a)
# while length > 0:
#     b.append(a[length-1])
#     length = length - 1
# print('Reversed list:', b)


#PYTHON PROGRAM TO PRINT REVERSE OF A STRING. a="python"
# a = "python"
# print ("The original string  is : ",str)
# reverse_a = ""
# i = len(a)
# while i > 0:
#     reverse_a += a[ i - 1 ]
#     i = i - 1
# print ("The reversed string using a while loop is : ",reverse_a)

#PYTHON PROGRAM TO PRINT FACTORIAL OF GIVEN NUMBER INPUT BY USER.
# num = int(input("enter a number: "))
# f = 1
# i = 1
# while i <= num:
#     f = f * i
#     i = i + 1
# print("factorial of ", num, " is ", f)

##############################
########################
# def add(a,b):
#     print(a+b)
# if__name__ =="__gii__":
#     add(3,7)    

# a=dir(math) 
# print(a)

##############
#####SQRT#####
##############

# import math
# a=20
# print(math.sqrt(a))


# from math import sqrt
# import math 
# print(sqrt(9))
# print(sqrt(16))
# print(sqrt(25))


# import random
# list1=[1,2,3,4,5,6]
# print(random.choice(list1))


# import random
# r1=random.randint(5,15)
# print("random number between 5 and 15 is % s" %(r1))
# r2=random.randint(-10,-2)
# print("random numnber between -19 and -2 is %d"%(r2))


# import random
# sample_list=[1,2,3,4,5]
# print("Original list:")
# print(sample_list)
# # first suffle
# random.shuffle(sample_list)
# print("/n After the first suffle:")
# print(sample_list)
# # second suffle
# random.shuffle(sample_list)
# print("/n After the first suffle:")
# print(sample_list)


# import random
# for i in range(50):
#     print(random.randint(20,50))

# import random
# a=[]
# for i in range(20):
#     a.append(random.randint(1,20))
# print("list:",a)    

# import datetime
# x= datetime.datetime.now()
# print(x)


# import datetime
# from re import A
# from time import strftime
# x= datetime.datetime.now()
# print(x.year)
# print(x,strftime("%A"))

