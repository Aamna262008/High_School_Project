import csv
from datetime import datetime
import os
headers=["ExpenseId","Date","Category","Description","Amount","Payment Method"]
try:
    with open("expense_list.csv",'r',newline="") as file:
        reader=csv.reader(file)
        expenses=list(reader)
        if expenses and expenses[0] == headers:
            expenses.pop(0)
except FileNotFoundError:
    expenses=[]
except PermissionError:
    print("file not readable")
    expenses=[]

def add_expense():
    global expenses
    global file
    global headers
    try:
        last_id=int(expenses[-1][0])
        expense_id=last_id+1
        
        
    except (ValueError,IndexError):
        expense_id="1"
        




        


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
        try:
          choice=int(input("pick from 1 to 8"))
        
          if choice >= 1 and choice <= 8:
             check=True
             category=categories[choice-1]
          else:
            print("invalid choice,please pick from given options.....") 
        except ValueError:
            print("invalid choice,please pick from given options.....")
            continue
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
        try:
         if choice >= 1 and choice <= 3:
            method=Methods[choice-1]
            break
         else:
            print("Invalid choice please pick between 1-3")
            continue
        except ValueError:
            print("Invalid choice please pick between 1-3")
    #storing
    info=[expense_id,date,category,description,amount,method]
    expenses.append(info)
    print("Expense added sucessfully")
    print(f"new expense id :{expense_id}")
    #loading into file 
    with open("expense_list.csv",'w',newline="") as write:
        writer=csv.writer(write)
        writer.writerow(headers)
        writer.writerows(expenses)
def view_expense():
    with open("expense_list.csv",'r',newline="") as file:
        reader=csv.reader(file)
        rows=list(reader)
        for row in rows:
            
            print(f"|{row[0]:<10}|{row[1]:<10}|{row[2]:<20}|{row[3]:<20}|{row[4]:<10}|{row[5]:<10}")
            if row == rows[0]:
                print("_"*100)
def search_expenses():

    global headers
    with open("expense_list.csv",'r',newline="")as file:
        while True:
         print("1.Category\n2.Description")
         try:
             search_by=int(input("What do you want to search by.Please pick either 1 or 2 "))
             if search_by != 1 and search_by != 2:
                 print("invalid...")
                 continue
             else:break
         except ValueError:
             print("Invalid...please only enter a number")
             continue
         
        if search_by == 1:
            categories=["Food","Transport","Education","Entertainment","Shopping","Bills","Health","Other"]
            index=1
            for category in categories:
                    print(f"{index}:{category}")
                    index=index+1
            check=False
            while check == False:
                    try:
                      choice=int(input("pick from 1 to 8"))
                    
                      if choice >= 1 and choice <= 8:
                         check=True
                         category=categories[choice-1]
                      else:
                        print("invalid choice,please pick from given options.....") 
                    except ValueError:
                        print("invalid choice,please pick from given options.....")
                        continue   
            count=0
            reader=csv.reader(file)
            rows=list(reader)
            list_search=[]
            for row in rows[1:] :
               if row[2] == category:
                list_search.append(row)
                count=count+1
               else:
                continue
            
        else:
            search_item=input("enter description you want to search")
            reader=csv.reader(file)
            list_search=[]
            rows=list(reader)
            count=0
            for row in rows[1:]:
                if search_item.lower() in row[3].lower():
                    count=count+1

                    list_search.append(row)
                else:
                    continue
        if count == 0 :
            print("No matching data found")
        else:
            print(f"{count}:searches found")
            print(f"|{headers[0]:<10}|{headers[1]:<10}|{headers[2]:<20}|{headers[3]:<20}|{headers[4]:<10}|{headers[5]:<10}")
            for row in list_search:
                print(f"|{row[0]:<10}|{row[1]:<10}|{row[2]:<20}|{row[3]:<20}|{row[4]:<10}|{row[5]:<10}")
def spending_summary():
    grand_total=0
    num_of_expense=0
    avg_expense=0
    total_food=0
    total_transport=0
    total_education=0
    total_entertainment=0
    total_shopping=0
    total_bills=0
    total_health=0
    total_other=0
    expense_list=[]
    category_expense_list=[]
    highest_spending_category=[]
    max_expense=[]
    largest_expense=[]
    with open("expense_list.csv",'r') as file:
        reader=csv.reader(file)
        rows=list(reader)
        for row in rows[1:]:
            grand_total=grand_total + float(row[4])
            expense_list.append(float(row[4]))

       
            num_of_expense=num_of_expense+1
            if row[2] == "Food"  :
                total_food = total_food + float(row[4])
            elif row[2] == "Transport" :
               total_transport = total_transport + float(row[4])
            elif row[2] == "Education":
                total_education=total_education+float(row[4])
            elif row[2] == "Entertainment" :
                total_entertainment=total_entertainment+float(row[4])
            elif row[2] == "Shopping":
                total_shopping=total_shopping+float(row[4])
            elif row[2] =="Bills":
                total_bills=total_bills+float(row[4])
            elif row[2] == "Health":
                total_health=total_health+float(row[4])
            elif row[2] == "Other":
                total_other=total_other+float(row[4])
        category_expense_list=[("Food",total_food),("Transport",total_transport),("Education",total_education),("Entertainment",total_entertainment),("Shopping",total_shopping),("Bills",total_bills),("Health",total_health),("Other",total_other)]
        highest=max(category[1] for category in category_expense_list)
        for category,amount in category_expense_list:
           if amount == highest:
             
             highest_spending_category.append((category,amount))
        try:
           max_expense=max(expense_list)
        except ValueError:
            print("Empty File")
        for row in rows[1:]:
            if float(row[4]) == max_expense:
                largest_expense.append(row)
        try:
            avg_expense=grand_total/num_of_expense
        except ZeroDivisionError:
            print("No expense") 
        print(f"Grand_Total:{grand_total}")
        print(f"Total_Expenses:{num_of_expense}")
        print(f"Total Expense Of Food:{total_food}")
        print(f"Total Expense Of Transport:{total_transport}")
        print(f"Total Expense Of Education:{total_education}")
        print(f"Total Expense Of Entertainment:{total_entertainment}")
        print(f"Total Expense Of Shopping:{total_shopping}")
        print(f"Total Expense Of Bills:{total_bills}")
        print(f"Total Expense Of Health:{total_health}")
        print(f"Other Expenses:{total_other}") 
        for list_ in highest_spending_category:
            print(f"Category with most amount of money spent:{list_}")
        for list_ in largest_expense:
            print(f"Largest Expense\n{list_}")  
               

            


  

            



   
                

                



                



    






