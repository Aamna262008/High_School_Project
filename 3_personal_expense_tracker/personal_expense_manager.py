import csv
from datetime import datetime
import os
headers=["ExpenseId","Date","Category","Description","Amount","Payment Method"]
try:
    with open("expenselist.csv",'r') as file:
        reader=csv.reader(file)
        expenses=list(reader)
except FileNotFoundError:
    expenses=[]
except PermissionError:
    print("file not readable")
    expenses=[]

def add_expense():
    global expenses
    global file
    try:
        last_id=int(expenses[-1][0])
        expense_id=last_id+1
        
        
    except IndexError:
        expense_id="1"
        print(expense_id)




        


    #DATE
    check=False
    while check == False:
        date=input("date of expense(DD-MM-YYYY)please take care of format")
        try:
            datetime.strptime(date, "%d-%m-%Y")
            check=True
    
            break
        except ValueError as e:
            continue
            
    #Category
    print("REASONS OF EXPENSE:")
    categories=["Food","Transport","Education","Entertainment","Shopping","Bills","Health","Other"]
    index=1
    for category in categories:
        print(f"{index}:{category}")
        index=index+1
    check=False
    while check == False:
        choice=int(input("pick from 1 to 8"))
        if choice >= 1 and choice <= 8:
            check=True
            category=categories[choice-1]
        else:
            print("invalid choice,please pick from given options.....")
    #Description
    while True:
        description=input("DESCRIPTION OF EXPENSE")
        if description == None or description == "":
            print("description cannot be empty..")
            continue
        else:
            break
    #Amount
    while True:
        try:
            amount=float(input("please enter amount:"))
            
        except ValueError:
            print("please enter number")
        
            continue
        if amount <= 0 :
            print("invalid amout(amount should always be greater than zero)")
            continue
        else:
            break
    #Payment Method
    Methods=["Cash","Card","Online"]
    index=1
    for method in Methods:
        print(f"{index}:{method}")
        index=index+1
    while True :
        choice=int(input("enter your payment method (1-3)"))
        if choice >= 1 and choice <= 3:
            method=Methods[choice-1]
            break
        else:
            print("Invalid choice please pick between 1-3")
            continue
    #storing
    info=[expense_id,date,category,description,amount,method]
    expenses.append(info)
    print(f"new expense id :{expense_id}")
    #loading into file
    with open
   


                



    






