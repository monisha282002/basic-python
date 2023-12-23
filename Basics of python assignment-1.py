#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Write a python program that takes two numbers as input and prints the largest number.

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(num1<num2):
 print( num2,"Entered second number is the largest number")
else:
 print(num1,"Entered first number is the largest number")


# In[1]:


# 2.Create a python program that asks the user for a month(1-12)and then prints the corresponding


month = int(input("Enter a month (1-12): "))

month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

# Check if the input month is valid
if 1 <= month <= 12:
    print("The corresponding month name is:", month_names[month - 1])
else:
    print("Invalid month number. Please enter a number between 1 and 12.")


# In[2]:


#3.Write a python program that determine whether a given year is leap year or not.
year=int(input("enter year:"))
if(year%4==0 or year%100!=0) and (year%400==100):
 print(year,"is a leap year")
else:
 print(year,"is not a leap year")


# In[4]:


# 4.Write a program that takes an integer as input and checks if it is positive,negative or zero.Print an appropriate answer

number=int(input("Enter the number:"))
if(number>0):
 print(number,"is a positive number")
elif(number<0):
 print(number,"is a negative number")
else:
 print("zero")


# In[6]:


# 5.Write a python program that asks the user for their age and gender.Based on their age and gender print a message like "you are a young man" or "you are a old woman"

age=int(input("Enter your age:"))
gender=str(input("Enter your gender:"))
if(age<12) and (gender=='male' or gender=='female'):
 print("you are a child")
elif(age>12 and age==19) and (gender=='male' or gender=='female'):
 print("you are a teenagers")
elif(age>19 and age<50 ) and (gender=='male'):
 print("you are a young man")
elif(age>19 and age<50 ) and (gender=='female'):
 print("you are a young woman")
elif(age>=50 and age<100) and (gender=='male'):
 print("you are a old man")
elif(age>=50 and age<100 ) and (gender=='female'):
 print("you are a old woman")
else:
 print("invalid")


# In[7]:


# 6.Create a python program that takes a temperature in celsius and convert into Fahrenheit.
temp=float(input("Enter a temperature:"))
Fahrenheit=(temp*1.8)+32
print(Fahrenheit," is Fahrenheit")


# In[1]:


# 8.Create a program ask the user for the three numbers and then print them in ascending order.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    num1, num2 = num2, num1  
if num1 > num3:
    num1, num3 = num3, num1  
if num2 > num3:
    num2, num3 = num3, num2 
    
print("The numbers in ascending order are:", num1, num2, num3)


# In[2]:


# 9.Write a program that checks if a given yearis a century year .

year=int(input("Enter the year:"))
if(year%4==0 and year%100==0):
 print(year,"is a century year")
else:
 print(year,"is a not century year")


# In[3]:


# 10.Create a program that asks the user for a number and then determine if it is odd or even.

num=int(input("Enter a number:"))
if(num%2==0):
 print(num,"is even")
else:
 print(num,"is odd")


# In[ ]:





# 
