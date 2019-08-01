# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:38:26 2019
Fundamentals of Programming: Python
Assignemnt #5
@author: Ajay Randhawa
"""

#Initializing my lists
task = list()
priority = list()
#Pulls in the data from the text file and strips out the new line symbol
lines = [line.rstrip('\n') for line in open('Todo.txt')]
#initializing dictionary
task_dict = {}
#the for loop removes the comma and adds the tasks and priorities into lists
for line in lines:
    split = line.split(',')
    task.append(split[0])
    priority.append(split[1])
#Converting the list into a Tuple then dictionary    
task_tuple = list(zip(task, priority))
task_dict = dict(task_tuple)

#While loop to display the menu until user chooses to exit by inputing 5
while(True):
    print ("""
           Menu of Options
           1) Show current data
           2) Add a new item
           3) Remove an existing item
           4) Save Data to File
           5) Exit Program
           """)
    strChoice = str(input("Which option would you like to perform? [1 to 5]:"))
    print()
    
    if (strChoice.strip() == "1"):
# if the user types 1, then the following lines of code are run
#table is created for the 2 lists.
        table = [task,priority] 
#Prints the the two lists as a table in different rows
        for objrow in table:
            print(objrow)
        
    elif(strChoice.strip() == "2"):
# if the user types 2, then the following lines of code are run
        task = str(input("Enter task: "))
        print()
        priority = str(input("Enter priority: "))
        print()
#New task is added to the dictionary
        task_dict.update({task:priority})
#task and priority lists are updated from the dictionary.
        task = list(task_dict.keys())
        priority = list(task_dict.values())
        
    elif(strChoice == "3"):
# if the user types 3, then the following lines of code are run
# Key is used as an reference to delete the dictionary item
        remove_key = input("Enter the task name to remove: ")
        del task_dict[remove_key]
#task and priority lists are updated from the dictionary.
        task = list(task_dict.keys())
        priority = list(task_dict.values())
        
    elif(strChoice == "4"):
# if the user types 4, then the following lines of code are run
# the table is updated to ensure latest data.
        table = [task,priority] 
        with open('Todo.txt', 'w') as f:
            for objrow in table:     
                f.write(str(objrow))
                f.write('\n')
            
    elif(strChoice.strip() == "5"):
# if the user types 5, then the following lines of code are run
# the break command exits the while loop
        break
    
    
print("Program Ended")
exit()

   
'''
Question: Is there another way to view the office hours video other than logging
into microsoft live?
'''
    


