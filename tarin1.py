# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:41:56 2024

@author: thava
"""

class Train:
    def __init__(self,train_no,train_name,train_from,train_to,total_seates):
        self.train_no=train_no
        self.train_name=train_name
        self.train_from=train_from
        self.train_to=train_to
        self.total_seates=total_seates
        self.booked_seates=0
        self.passenger_list=[]
        
    def check_available(self):
        return self.total_seates-self.booked_seates
    
    def booking_t(self,p_name,p_age,p_gender,p_status="confirmed"):
        available_seates=self.check_available()
        if available_seates >0:
            self.booked_seates+=1
            self.seat_no=self.booked_seates
            self.passenger_list.append({"name":p_name,
                                        "age":p_age,
                                        "gender":p_gender,
                                        "seat":self.seat_no,
                                        "status":p_status
                                        })
            print('Hello {p_name} Your ticket is Booked. seate No is {self.seat_no}')
        else:
            print('Sorry, No seate available ')
    
    def cencle_t(self,p_name):
        for i in self.passenger_list:
            if i['name']==p_name:
                self.booked_seates-=1
                self.passenger_list.remove(i)
                print("your Ticket is cencle successfully")
            else:
                print("Passenger name is not found")
                
    def viwe_p_list(self):
        if self.passenger_list:
            print("Passenger List")
            for index,i in enumerate(self.passenger_list,1):
                print(f"{index}. Name: {i['name']} -seate No: {i['seat']}- status {i['status']}")
        else:
            print("No passangers Booked...")
 
    



while True:
    print("\t\t\t RAILWAY RESERVACTION SYSTEM ")
    print("Coimbutore To Mannagudi-----press 1")
    print("Mannargudi To Coimbutore----Press 2")
    print("Mannargudi To Chennai-------press 3")
    print("Chennai To Coimbutore-------press 4")
    print("Exit------------------------press 5")
    ch1=int(input("Select Train...."))
    if ch1==1:
        train1=Train(10001,'thava1 Express','Coimbutore','Mannargudi',100)
        break
    elif ch1==2:
        train2=Train(10002,'thava2 Express','Mannargudi','Coimbutore',100)
        break
    elif ch1==3:
        train3=Train(10003,'thava3 Express','Mannargudi','Chennai',100)
        break
    elif ch1==4:
        train4=Train(10002,'thava2 Express','Chennai','Coimbutore',100)
        break
    elif ch1==5:
        break
    else:
        print("Enter Valid Input....")

while True:
    
    print("\n1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Availability")
    print("4. View Passenger List")
    print("5. Exit")
    ch2=int(input("Enter Your Choise :"))
    if ch2==1:
        
    

    
                
                
        
                
        
            
    
        
        
        