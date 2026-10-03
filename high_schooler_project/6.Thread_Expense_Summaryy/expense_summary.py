import csv,threading,os
"""Initialize Final Total Values"""
Food=0
Study=0
Transport=0
Total_Amount=0
total_valid=0
total_invalid=0
files_name=["day1.csv","day2.csv","day3.csv"]
file_total=[0,0,0]
file_valid=[0,0,0]
file_invalid=[0,0,0]
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
lock_file=threading.Lock()
"""Defining the main expense summary function"""
def expense_summary(file_name,pos):
    
    """Opening and initialising file and variables"""
    global Food,Study,Transport,Total_Amount,total_valid,total_invalid,file_total,file_valid,file_invalid
    valid=0
    invalid=0
    total=0
    with open(os.path.join(BASE_DIR,file_name),'r') as file:
        reader=csv.reader(file)
        header=next(reader)
        """Dealing with data"""
        for row in reader:
            category=row[0]
            """Sorting Valid And Invalid"""
            try:
                amount=int(row[1])
                if amount > 0 and amount % 1 == 0:
                    valid=valid+1
                    with lock_file:
                        total_valid=total_valid + 1
                else:
                    invalid=invalid + 1
                    with lock_file:
                        total_invalid=total_invalid + 1
                        continue
            except ValueError:
                invalid=invalid+1
                with lock_file:
                    total_invalid = total_invalid + 1
                    continue

            """Incrementing By Category"""

            with lock_file:
                if category == "Food":
                    Food = Food + amount
                elif category == "Study":
                    Study = Study + amount
                else:
                    Transport = Transport + amount

                """ Dealing with amount """

                Total_Amount=Total_Amount+amount
            total=total+amount
        
        """Placing all values """
        
        file_total[pos]=total
        file_valid[pos]=valid
        file_invalid[pos]=invalid
        
        
        """End of function"""

""" Initialisng Threads"""

threads=[]
ind=0
for file in files_name :
    t=threading.Thread(target= expense_summary,args=(file,ind),name=file )
    ind+=1
    threads.append(t)

"""Starting thread"""

for t in threads:
    t.start()

"""Joining thread"""
for t in threads:
    t.join()

"""Printing the summary"""

print("EXPENSE SUMMARY\nCurrency:PKR")
for i in range(3):
    print(f"{files_name[i]} : {file_valid[i]} valid , {file_invalid[i]} invalid ,total {file_total[i]}")
print("\nCATEGORY TOTALS")
print(f"Food : {Food}")
print(f"Transport : {Transport}")
print(f"Study : {Study}\n")
print(f"Valid Expenses : {total_valid}")
print(f"Invalid Rows : {total_invalid}")
print(f"Grand Total : {Total_Amount}")
            
            