"""#NUmber Guesssing game
import random

# from sympy.codegen.ast import break_


def Number_guessing_game():
    random_number = random.randint(1,50)
    # print(random_number)
    attempt_count = 0
    print("Welcome to the Number guessing game:\n")
    flag = True
    user_input = int(input("please enter a number between 1 and 50:\n"))
    while flag:
        if user_input == random_number:
            attempt_count+=1
            print(f"You won in {attempt_count} attempts")
            flag = False
        elif user_input==(random_number-10):
            print("Too low")
            attempt_count += 1
        elif user_input==(random_number+10):
            print("Too High")
            attempt_count += 1
        elif user_input==(random_number-5) or user_input==(random_number+5):
            print("You are close")
            attempt_count += 1
        else:
            print(False)
            attempt_count+=1
    user_choice = str(input("Would you like to play again press y for yes and n for no:\n"))
    user_choice = user_choice.lower()
    if user_choice == 'y':
        Number_guessing_game()
    else:
        print("bye")


Number_guessing_game()

"""
# Practicing user input-->Todo list


# user_task_lists = []
# user_name = str(input("Please enter your name:\n"))
# file_name = f"{user_name}_tasks.txt"
# with open(file_name,'w') as file:
#       pass
# flag = True
# while flag:
#
#       user_input_task = str(input(f"Hello {user_name}!Welcome to  MasterYourDay:\n"
#             f"Add task --> Type Add \n"
#             f"View Task --> Type View \n"
#             f"Remove Task --> Type Remove \n"
#             f"Exit -->Type exit \n"))
#       try:
#             if user_input_task.lower() == "add":
#                   task_to_add = str(input("Please enter the task you want to crush:\n"))
#                   with open(file_name,'a') as file:
#                         file.write(task_to_add+'\n')
#                   user_task_lists.append(task_to_add)
#                   print(f"The task {task_to_add} has been added to the list")
#                   print()
#             elif user_input_task.lower()=="view":
#                   with open(file_name,'r') as file:
#                        content =  file.read()
#                        print(f"Hello {user_name} here are your tasks all the best")
#                        print(content)
#                        print()
#             elif user_input_task.lower()=="remove":
#                   with open(file_name,'r') as file:
#                         lines = file.readlines()
#                   if not lines:
#                         print("No tasks found!\n")
#                         continue
#                   print("\n Your tasks:")
#                   for i,task in enumerate(lines,start =1):
#                         print(f"{i}.{task.strip()}")
#                   try:
#                         choice = int(input("\n Enter the task number to remove: "))
#                         if 1<= choice <= len(lines):
#                               removed_task = lines.pop(choice-1)
#                               with open(file_name,'w') as file:
#                                     file.writelines(lines)
#                               print(f"✅ Task removed: {removed_task.strip()}\n")
#                         else:
#                               print("⚠️ Invalid task number\n")
#                   except ValueError:
#                         print("⚠️ Please enter a valid number\n")
#             elif user_input_task.lower()== "exit":
#                   flag = False
#       except (ValueError,TypeError):
#             print("Please enter a valid input")
# Project3--PhoneBook
#Contacts Menu
from email_validator import validate_email,EmailNotValidError
import re

from sympy import false

user_data = []
#helper function for number checking
def is_number(value):
    pattern = r"^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.fullmatch(pattern,value))
#helper function for email checking
def is_valid_email_library(Email):
    try:
        v = validate_email(email,check_deliverability=False)
        return True
    except EmailNotValidError as e:
        print(f"Validation error:{e}")
        return False
def delete_contact(data_to_delete):
    to_delete = input("Enter the data that you want to delete\n")
    with open(data_to_delete,"r") as files:
        lines = files.readlines()
    is_present = False
    with open(file_name,"w") as files:
        for line_to_delete in lines:
            if to_delete not in line_to_delete:
                file.write(line)
            else:
                is_present = True
    if found:
        print(f"Contact containing {to_delete} has been deleted")
    else:
        print(f"No contact found{to_delete}")
users_name = str(input("Please enter your name:\n"))
file_name = f"{users_name}_contacts.txt"
flag = True
while flag:
    print("1.Add Contact \n 2.View Contacts \n 3.Search Contacts\n4.Delete Contact\n5.Exit\n")
    choice = int(input("Enter your choice:\n"))
    if choice == 1:
        print("Please enter the following details:\n")
        name = str(input("Please enter the name that you want to delete:\n"))
        if not name.replace(" ","").isalpha():
            print("Invalid name please use only letters")
            continue
        phone_number = input("Enter phone number:")
        while not is_number(phone_number):
            print("Invalid phone number,try again.")
            phone_number = input("Enter phone number: ")
        email = input("Please enter your email:\n")
        if not is_valid_email_library(email):
            print(f"{email} is a valid email address")
            continue
        with open (file_name,"a") as file:
            file.write(f"{name},{phone_number},{email}\n")
        print(f"✅ Contact for {name} added.")
    elif choice == 2:
        print(f"\n Hello {users_name},here are your contacts:\n")
        try:
            with open(file_name,"r") as file:
                content = file.read().strip()
                print(content if content else "No contacts saved yet.")
        except FileNotFoundError:
            print("No contacts saved yet")
    elif choice == 3:
        data_to_find = input("Please enter what you want to find:\n")
        with open (file_name,"r") as file:
            found = False
            for line_num,line in enumerate(file,1):
                if data_to_find in line:
                    print(f"{data_to_find} found on line {line_num}:{line.strip()}")
                    found  = True
                if not found:
                    print(f"{data_to_find}  not found in the file")
    elif choice == 4:
        flag = False
        print("Goodbye 👋")
    else:
        print("Invalid option, try again.")