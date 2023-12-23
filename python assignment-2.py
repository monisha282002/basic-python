#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python for loop that prints the numbers from 1 to 10.

for i in range (1,11):
        print(i,end=' ')



# In[ ]:


2. Create a list of fruits (e.g., ["apple", "banana", "cherry"]) and write a for loop to print each fruit in the list.
 
fruits=['apple','orange','grapes','pineapple']
for i in fruits:
     print(i)





# In[3]:


# 3. Write a Python program that calculates the sum of all even numbers from 1 to 50 using a for loop.

sum=0
for i in range(1,50):
     if(i%2==0):
         sum=sum+i
print(sum)


# In[8]:


# 4. Create a list of integers, and using a for loop, find and print the largest number in the list.

max=0
list=[10,28,2,14,60,30,4]
for i in list:
    if i>max:
        max=i
print(max)


# In[16]:


# 5. Write a Python program that uses a for loop to find and print all the prime numbers between 1 and 100. A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

for i in range(1,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')


# In[17]:


# 6. Write a Python program that takes a list of dictionaries, where each dictionary represents a person with keys "name" and "age." Find and print the average age of all the people in the list.

def average_age(people):
    total_age = 0
    count = 0
    for person in people:
        total_age = total_age + person["age"]
        count = count + 1
    if count == 0:
        return "No people in the list"
    else:
        return total_age / count

people = [
    {"name": "abc", "age": 29},
    {"name": "efg", "age": 50},
    {"name": "hij", "age": 30},
]
print(average_age(people))


# In[18]:


# 7. Create a dictionary representing a simple inventory system for a store. Implement afunction that allows you to update the quantity of items in the inventory by specifying theitem name and the new quantity.

inventory = {
    "pen": 50,
    "pencil": 30,
    "eraser": 20,
    "book": 100,
    "sticker": 50,
}

def update_inventory(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
    else:
        print(f"Error: Item '{item_name}' not found in the inventory.")

update_inventory("pen", 60)
update_inventory("book", 70)
# Print the updated inventory
print(inventory)


# In[ ]:




