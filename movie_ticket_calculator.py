class customer:
    def __init__(self,namep,agep,Is_memberp,Ticket_Amountp):
        self.name=namep
        self.age=agep
        self.Is_member= Is_memberp
        self.ticket_type=None
        self.ticket_price=0.0
        self.Is_member=Is_memberp
        self.InitialPrice=0.0
        self.Discount=0.0
        self.Ticket_Amount=Ticket_Amountp
        self.price_of_oneticket=0
    
    def set_ticket_type(self):
                if self.age <= 4:
                    self.ticket_type="Small Child"
                elif self.age >= 5 and self.age <= 12:
                    self.ticket_type="Child"
                elif self.age >= 13 and self.age <= 59:
                    self.ticket_type="Adult"
                else:
                 self.ticket_type="Senior Citizen"
    def set_ticket_price(self):
                     if self.ticket_type == "Small Child":
                        self.ticket_price=0.0
                     elif self.ticket_type =="Child":
                        self.ticket_price=500.0
                     elif self.ticket_type =="Adult":
                        self.ticket_price=1000.0
                     else:
                        self.ticket_price=600.0
                     self.price_of_oneticket=self.ticket_price
                     self.ticket_price=self.ticket_price * self.Ticket_Amount
                     self.InitialPrice=self.ticket_price
                     if self.Is_member == True:
                        self.Discount=self.ticket_price * 0.1
                        self.ticket_price=self.ticket_price - self.Discount
print("Movie Ticket Calculator")

name=input("Please Enter Your Name:")
Check=False
while Check == False:
     age=int(input("Enter Age"))
     if age <= 0 or age >= 120:
          print("please enter a valid age...")
     else:
          Check=True
          
          
member=input("Are you a member:Yes or No")
Check=False
while Check == False:
    if member.lower() == "yes":
        Is_member = True
        Check = True
    elif member.lower() == "no":
        Is_member = False
        Check=True
    else:
        member=input("please only answer in yes or no.....")

Ticket_Amount=int(input("how many tickets"))
Customer=customer(name,age,Is_member,Ticket_Amount)
Customer.set_ticket_type()
Customer.set_ticket_price()
print("Reciept".center(20,"_"))
print(f"customer:{Customer.name}")
print(f"Category:{Customer.ticket_type}")
print(f"Price per ticket:{Customer.price_of_oneticket}")
print(f"Tickets:{Customer.Ticket_Amount}")
print(f"Subtotal:{Customer.InitialPrice}")
print(f"Discount:{Customer.Discount}")
print(f"Amount Payable:{Customer.ticket_price}")




                
  

