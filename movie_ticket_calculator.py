class Customer:
    def __init__(self,namep,agep,is_memberp,ticket_amountp):
        self.name=namep
        self.age=agep
        self.ticket_type=None
        self.ticket_price=0.0
        self.is_member=is_memberp
        self.discount=0.0
        self.ticket_amount=ticket_amountp
        self.price_of_oneticket=0
        self.final_price=0
        self.subtotal=0

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
                     self.subtotal=self.price_of_oneticket * self.ticket_amount
                     
                     if self.is_member == True:
                        self.discount=self.subtotal * 0.1
                        self.final_price=self.subtotal - self.discount
print("Movie Ticket Calculator")

name=input("Please Enter Your Name:")
Check=False
while Check == False:
     try:
        age=int(input("Enter Age"))
        if age <= 0 or age >= 120:
          print("please enter a valid age...")
        else:
               Check=True 
     except ValueError:
          print("Please enter a number")



            
          
member=input("Are you a member:Yes or No")
Check=False
while Check == False:
    if member.lower() == "yes":
        is_member = True
        Check = True
    elif member.lower() == "no":
        is_member = False
        Check=True
    else:
        member=input("please only answer in yes or no.....")
Check=False
while Check == False:
     ticket_amount=int(input("how many tickets"))
     if ticket_amount <= 0:
          print("Invalid Ticket Number,Please Try Again (value should be greater than 0)")
     else:
          Check=True
customer_data=Customer(name,age,is_member,ticket_amount)
customer_data.set_ticket_type()
customer_data.set_ticket_price()
print("Receipt".center(20,"_"))
print(f"customer:{customer_data.name}")
print(f"Category:{customer_data.ticket_type}")
print(f"Price per ticket:{customer_data.price_of_oneticket:.2f}")
print(f"Tickets:{customer_data.ticket_amount:.2f}")
print(f"Subtotal:{customer_data.subtotal:.2f}")
print(f"Discount:{customer_data.discount:.2f}")
print(f"Amount Payable:{customer_data.final_price:.2f}")




                
  

