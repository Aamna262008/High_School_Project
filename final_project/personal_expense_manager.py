import csv
from datetime import datetime
try:
    file=open("expense_list.csv","r")
    add_data=open("expense_list.csv","a")
except PermissionError:
    print("file cannot be read")
except FileNotFoundError:
    add_data=open("expense_list.csv","w")
    writer=csv.writer(add_data)
    writer.writerow(["ExpenseId","Date","Category","Description","Amount","Payment method"])


def add_expense():
    global file 
    read_data=file.read()
    #EXPENSE ID
    try:
        expense_id=str(int(read_data[-1][0])+1)
    except ValueError:
        expense_id="1"
    except IndexError:
         writer=csv.writer(add_data)
         writer.writerow(["ExpenseId","Date","Category","Description","Amount","Payment method"])

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
        if description == None:
            print("description cannot be empty..")
            continue
        else:
            break
    #Amount
    while True:
        amount=float(input("please enter amount:"))
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
            print("invalid choice pick between 1-3")
            
            continue
        else:
            method=Methods[choice-1]
    
            break
    info=[expense_id,date,category,description,amount,method]
    writer=csv.writer(add_data)
    writer.writerow(info)
add_expense()




