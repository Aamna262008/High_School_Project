import csv
from datetime import datetime ,date,timedelta
import os
headers=["ExpenseId","Date","Category","Description","Amount","Payment Method"]
file_path = os.path.join(os.path.dirname(__file__), "expense_list.csv")
try:
    with open(file_path,'r',newline="") as file:
        reader=csv.reader(file)
        expenses=list(reader)
        if expenses[0] == headers and expenses:
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
    #Expense_Id
    if  expenses:
        
        for index in range(len(expenses)-1,-1,-1):
            if not expenses[index]:
                expenses.pop(index)
            
    try:
       last_id=expenses[-1][0]
       print(f"Previous_Id{last_id}")
       expense_id=int(last_id)+1
       expense_id=str(expense_id)
    except IndexError:
        expense_id="1"
    #Date
    while True:
        try:
          date_input=input("Enter Date Of Expense(dd-mm-yyyy)....please be very careful of this format")
          current_date=date.today()
          date_input=datetime.strptime(date_input, "%d-%m-%Y").date()
          min_date=date(2000,1,1)
          if date_input < min_date :
              print(f"No date excepted below{min_date.strftime("%d-%m-%Y")}")
              continue
          elif date_input > current_date:
              print(f"No date excepted after the current date{current_date.strftime("%d-%m-%Y")}")
              continue
          else:
              break
        except (IndexError,ValueError):
            print("Invalid Format")
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
        
        try:
         choice=int(input("enter your payment method (1-3)"))
         if choice >= 1 and choice <= 3:
            method=Methods[choice-1]
            break
         else:
            print("Invalid choice please pick between 1-3")
            continue
        except ValueError:
            print("Invalid choice please pick between 1-3")
    #storing
    info=[expense_id,date_input,category,description,amount,method]
    expenses.append(info)
    print("Expense added sucessfully")
    print(f"new expense id :{expense_id}")
def view_expense():
    try:
     with open(file_path,'r',newline="") as file:
         reader=csv.reader(file)
         rows=list(reader)
         total=0
         record=-1
         for row in rows:
            record = record+1
            print(f"|{row[0]:<10}|{row[1]:<10}|{row[2]:<20}|{row[3]:<50}|{row[4]:<10}|{row[5]:<10}")
            if row == rows[0]:
                print("_"*130)
         for row in rows[1:]:
            total=total+float(row[4])
         print(f"records present:{record:<78}|Total PKR: {total}")
    except FileNotFoundError:
        print("no such file exists")
    except IndexError:
        print("No such file exists")
def search_expenses():

    global headers
    global expenses

    try:
        with open(file_path, 'r', newline="") as file:
            while True:
                print("1.Category\n2.Description")

                try:
                    search_by = int(input("What do you want to search by. Please pick either 1 or 2 "))

                    if search_by == 1 or search_by == 2:

                        if search_by == 1:
                            categories = [
                                "Food",
                                "Transport",
                                "Education",
                                "Entertainment",
                                "Shopping",
                                "Bills",
                                "Health",
                                "Other"
                            ]

                            index = 1

                            for category in categories:
                                print(f"{index}:{category}")
                                index = index + 1

                            while True:
                                try:
                                    choice = int(input("pick from 1 to 8"))

                                    if choice >= 1 and choice <= 8:
                                        category = categories[choice - 1]
                                        break
                                    else:
                                        print("invalid choice,please pick from given options.....")

                                except ValueError:
                                    print("invalid choice,please pick from given options.....")
                                    continue

                            count = 0
                            list_search = []

                            for row in expenses:
                                if row[2] == category:
                                    list_search.append(row)
                                    count = count + 1
                                else:
                                    continue

                        else:
                            search_item = input("enter description you want to search")

                            reader = csv.reader(file)
                            list_search = []
                            rows = list(reader)
                            count = 0

                            for row in rows[1:]:
                                if search_item.lower() in row[3].lower():
                                    count = count + 1
                                    list_search.append(row)
                                else:
                                    continue

                        if count == 0:
                            print("No matching data found")

                        else:
                            print(f"{count}:searches found")

                            print(
                                f"|{headers[0]:<10}|{headers[1]:<10}|"
                                f"{headers[2]:<20}|{headers[3]:<20}|"
                                f"{headers[4]:<10}|{headers[5]:<10}"
                            )

                            for row in list_search:
                                print(
                                    f"|{row[0]:<10}|{row[1]:<10}|"
                                    f"{row[2]:<20}|{row[3]:<20}|"
                                    f"{row[4]:<10}|{row[5]:<10}"
                                )

                        break

                    else:
                        print("Invalid Number (please pick between 1 or 2)")

                except ValueError:
                    print("Invalid...please only enter a number")
                    continue

    except FileNotFoundError:
        print("File does not exist")  
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
    try:
     with open(file_path,'r') as file:
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
         print("SPENDING SUMMARY".center(50,"_"))
         print(f"Grand_Total:{grand_total}")
         print(f"Total_Expenses:{num_of_expense}")
         print(f"Average Expense{avg_expense}")
         print(f"Total Expense Of Food:{total_food}")
         print(f"Total Expense Of Transport:{total_transport}")
         print(f"Total Expense Of Education:{total_education}")
         print(f"Total Expense Of Entertainment:{total_entertainment}")
         print(f"Total Expense Of Shopping:{total_shopping}")
         print(f"Total Expense Of Bills:{total_bills}")
         print(f"Total Expense Of Health:{total_health}")
         print(f"Other Expenses:{total_other}") 
         for list_ in highest_spending_category:
             print(f"Category with most amount of money spent:{list_[0]}")
         for list_ in largest_expense:
             print(f"Largest Expense:\nExpense_Id:{list_[0]}\nDate:{list_[1]}\nCategory:{list_[2]}\nDescription:{list_[3]}\nAmount:{list_[4]}\nPaymentMethod:{list_[5]}") 
    except FileNotFoundError:
       print("File does not exist") 
def edit_expense():
   global expenses
     
   while True:
     try:
         id_to_edit=int(input("Enter the id you want to edit...."))
         row_to_edit=None
         
         check=0
         for row in expenses:
             
             if id_to_edit == int(row[0]):
                 row_to_edit=row
                 break
             else:
             

                check=check+1
         if row_to_edit == None:
                 print("ID NOT FOUND ")
                 break
         
         print(row_to_edit)
         
         header=list(headers)
         for x in range(0,6):
            print(f"{header[x]}:{row_to_edit[x]}")
            if x == 0:
                continue
            else:
               while True:

                 choice=input("Do you want to change this value?(please only answer in yes or no)")
                 if choice.lower() == "yes" or choice.lower() == "no":
                    break
                 else:
                    continue
               if choice.lower() == "no":
                  continue
               elif choice.lower() == "yes":
                  if x==1:
                     
                    while True:
                            try:
                              date_input=input("Enter Date Of Expense(dd-mm-yyyy)....please be very careful of this format")
                              current_date=date.today()
                              date_input=datetime.strptime(date_input, "%d-%m-%Y").date()
                              min_date=date(2000,1,1)
                              if date_input < min_date :
                                  print(f"No date excepted below{min_date.strftime("%d-%m-%Y")}")
                                  continue
                              elif date_input > current_date:
                                  print(f"No date excepted after the current date{current_date.strftime("%d-%m-%Y")}")
                                  continue
                              else:
                                  break
                            except (IndexError,ValueError):
                                print("Invalid Format")
                                continue
                    
                  elif x == 2:
                      print("REASONS OF EXPENSE:")
                      categories=["Food","Transport","Education","Entertainment","Shopping","Bills","Health","Other"]
                      index=1
                      for category in categories:
                          print(f"{index}:{category}")
                          index=index+1
                          
                      while True:
                         try:
                               choice=int(input("pick from 1 to 8"))
                              
                               if choice >= 1 and choice <= 8:
                                   
                                   category=categories[choice-1]
                                   row_to_edit[x]=category
                                   break
                               else:
                                  print("invalid choice,please pick from given options.....") 
                                  continue
                         except ValueError:
                                  print("invalid choice,please pick from given options.....")
                                  continue
                  elif x== 3:
                      while True:
                              description=input("DESCRIPTION OF EXPENSE:")
                              if description == None or description == "":
                                  print("description cannot be empty..")
                                  continue
                              else:
                                  row_to_edit[x]=description
                                  break
                      
                  elif x == 4:
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
                                  row_to_edit[x]=amount
                                  break
                  elif x == 5:
                      Methods=["Cash","Card","Online"]
                      index=1
                      for method in Methods:
                              print(f"{index}:{method}")
                              index=index+1
                      while True :
                              
                         try:
                               choice=int(input("enter your payment method (1-3)"))
                               if choice >= 1 and choice <= 3:
                                  method=Methods[choice-1]
                                  row_to_edit[x]=method
                                  break
                               else:
                                  print("Invalid choice please pick between 1-3")
                                  continue
                         except ValueError:
                                  print("Invalid choice please pick between 1-3")
                                  
         
         break     
     except (ValueError):
         print('Please make sure you only enter a number')
         continue
     except (IndexError):
         print("Index does not exist")
def delete_expense():
    global expenses
    try:
     id_to_delete=int(input("please enter id of data you want to delete"))
     index=0
     deleted_data=[]
     check = False
     for index,row in enumerate(expenses):
        try:
            if int(row[0]) == id_to_delete:
                print(row)
                check=False
                while True:
                    choice=input("Do you want to delete this data,(please only answer in yes or no)")
                    if choice.lower() == "yes":
                        deleted_data.append(row)
                        expenses.pop(index)
                        check=True

                        print("data deleted")
                        break
                    elif choice.lower() == "no" :
                        print("data not deleted")
                        check=True
                        break
                    else:
                        continue
        except (IndexError,ValueError):
            print("Please Enter Number")
     if check == False:
        print("ID not found...")

            
                        

        
    
            
    except(ValueError):
        print("Enter a number please")    
def save_data():
    
        with open(file_path,'w',newline="") as file:
            writer=csv.writer(file)
            writer.writerow(headers)
            writer.writerows(expenses)
while True:
   print(f"MENU\npick one from given option:\n1.Add Expense\n2.View Expense\n3.Search Expense\n4.See Spending Summary\n5.Edit an Expense\n6.Delete an Expense\n7.Save Contents\n8.Exit\n\n\n")
   try:            
       choice_user=int(input("What do you want to do:"))
       if choice_user >=1 and choice_user <=8:
           if choice_user == 1:
               add_expense()
               continue
           elif choice_user == 2:
               view_expense()
               continue
           elif choice_user == 3:
               search_expenses()
               continue
           elif choice_user == 4:
               spending_summary()
               continue
           elif choice_user == 5:
               edit_expense()
               continue
           elif choice_user == 6:
               delete_expense()
               continue
           elif choice_user == 7 :
               save_data()
               continue
           elif choice_user == 8:
               print("8")
               break
       else:
           print("Invalid Input(please pick between 1 and 8(numeric form only.....))")
           continue
   except ValueError:
       print("Invalid Input(please pick between 1 and 8(numeric form only.....))")
       continue     
     






         
                      
                      
                     
                     
               
            
                
                 
             
            



   
                

                



                



    






