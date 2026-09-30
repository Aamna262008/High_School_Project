import threading , time,os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
a=threading.Lock()
total_words=0
file_list=["study.txt","shopping.txt","reminders.txt"]
final_list=[0,0,0]
total_file=0
def word_count(file_name,pos):
    global total_words,final_list,total_file
    with open(os.path.join(BASE_DIR,file_name),'r') as file:
        data=file.read()
    words=data.split()
    count=len(words)
    final=(f"{file_name}:{count}")
    with a:
        total_words= total_words + count
        total_file=total_file+1
        final_list[pos]=count
        
if __name__ =="__main__":
    study=threading.Thread(target=word_count,args=('study.txt',0))
    shopping=threading.Thread(target=word_count,args=('shopping.txt',1))
    reminder=threading.Thread(target=word_count,args=('reminders.txt',2))
   
    study.start()
    reminder.start()
    shopping.start()
    study.join()
    reminder.join()
    shopping.join()
    print("Word Summary".center(20,"*"))
    for i in range(3):
        print(f"{file_list[i]}:{final_list[i]}")
        
    print(f"Total Files: {total_file}")
    print(f"Total Words : {total_words}")
  
