"""Records and prints the expense summary of 3 files"""
import csv
import threading
import os
#Initialize Final Total Values
FOOD=0
STUDY=0
TRANSPORT=0
TOTAL_AMOUNT=0
TOTAL_VALID=0
TOTAL_INVALID=0
files_name=["day1.csv","day2.csv","day3.csv"]
file_total=[0,0,0]
file_valid=[0,0,0]
file_invalid=[0,0,0]
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
lock_file=threading.Lock()
#Defining the main expense summary function
def expense_summary(file_name,pos):

    """Opening and initialising file and variables"""
    global FOOD,STUDY,TRANSPORT,TOTAL_AMOUNT,TOTAL_AMOUNT,TOTAL_INVALID,TOTAL_VALID #pylint: disable=global-statement
    valid=0
    invalid=0
    total=0
    with open(os.path.join(BASE_DIR,file_name),'r',encoding="utf-8") as file:
        reader=csv.reader(file)
        _ = next(reader)
        #Dealing with data
        for row in reader:
            category=row[0]
            #Sorting Valid And Invalid
            try:
                amount=int(row[1])
                if amount > 0 :
                    valid=valid+1
                    with lock_file:
                        TOTAL_VALID=TOTAL_VALID + 1
                else:
                    invalid=invalid + 1
                    with lock_file:
                        TOTAL_INVALID=TOTAL_INVALID + 1
                        continue
            except ValueError:
                invalid=invalid+1
                with lock_file:
                    TOTAL_INVALID = TOTAL_INVALID + 1
                    continue

            #Incrementing By Category

            with lock_file:
                if category == "Food":
                    FOOD = FOOD + amount
                elif category == "Study":
                    STUDY = STUDY + amount
                else:
                    TRANSPORT = TRANSPORT + amount

                # Dealing with amount

                TOTAL_AMOUNT=TOTAL_AMOUNT+amount
            total=total+amount

        #Placing all values

        file_total[pos]=total
        file_valid[pos]=valid
        file_invalid[pos]=invalid


        #End of function

if __name__ == " __main__" :
    # Initialisng Threads
    threads=[]
    ind=0
    for name in files_name :
        t=threading.Thread(target= expense_summary,args=(name,ind),name=name )
        ind+=1
        threads.append(t)
    #Starting thread
    for t in threads:
        t.start()
    #Joining thread
    for t in threads:
        t.join()
    #Printing the summary
    print("EXPENSE SUMMARY\nCurrency:PKR")
    for i in range(3):
        print(f"{files_name[i]} : {file_valid[i]} valid , "
              f"{file_invalid[i]} invalid ,total {file_total[i]}")
    print("\nCATEGORY TOTALS")
    print(f"Food : {FOOD}")
    print(f"Transport : {TRANSPORT}")
    print(f"Study : {STUDY}\n")
    print(f"Valid Expenses : {TOTAL_VALID}")
    print(f"Invalid Rows : {TOTAL_INVALID}")
    print(f"Grand Total : {TOTAL_AMOUNT}\n")
