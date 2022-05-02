class customer():
    usercount=0
    def __init__(s,ids,fname,email,contact,password):
        s.ids=ids
        s.fname=fname
        s.email=email
        s.contact=contact
        s.password=password
        s.balance=0
        s.acc_no=s.fname+str(s.contact)+"sbi"
        print("Your Account no.:",s.acc_no)
        
##        v=(s.fname+str(s.contact)+"sbi")
##        print(v)

        
  
##        
##        def showinfo(s):
##            print(f"Name of Customer :{s.fname}")
##            print(f"Email id: {s.email}")
##            print(f"Contact No.: {s.contact}")
##            print(f"Account NO.: {s.acc_no}")
##            
##            print(showinfo(s))
##

        customer.usercount+=1

    def __str__(s):
        return s.fname+'    '+s.email+'    '+str(s.contact)+'    '+str(s.balance)+'  '+str(s.acc_no)

   

class bank(customer):
    blist=[]
    def __init__(s):
        s.execute()

    def login(s):
        
        acc=str(input("Enter Your Account Number : "))
        password=str(input("Enter Your  Pasword : "))
        for i in s.blist:
            if i.acc_no==acc and i.password==password:
                print("Login Successfully")
                
               
                while(True):
                    print("1 : Customer Details : ")
                    print('2 : Deposit : ')
                    print('3 : Withdraw : ')
                    print('4 : Balance : ')
                    print('5 : Exit : ')
                    
                    num=(input('Enter choice :'))
                    if num=="1":
                        print(i)
                        
                    elif num=="2":
                        
                        depoamt=int(input('Enter Amount For Deposit :'))
            
                        i.balance=i.balance+depoamt
                        
                        print(depoamt,'Deposited Successfully')
                        
                    elif num=="3":
                        widamt=int(input('Enter Amount For Withdraw :'))
                        i.balance=i.balance-widamt
                        
                        print(widamt,'Withdrawed Successfully')
                        
                    elif num=="4":
                        
                        print('Your Balance :',i.balance)
                                
                    else:
                        break

            else:
                print('Please Enter Valid Credentials')
        




    def execute(s):

        while(True):
            print("1 : Register")
            print("2 : login")
            print("3 : Exit")

            x=input("Enter the choice: ")

            if x=="1":
                ids=str(input("Enter new id: "))
                name=str(input("Enter the name: "))
                email=str(input("Enter the email: "))
                contact=int(input("Enter the contact No: "))
                passw=str(input("enter the password: "))
                t=customer(ids,name,email,contact,passw)
                s.blist.append(t)
                
                print("customer details added successfully")
                
                

            elif x=="2":
                s.login()

            elif x=="3":
                break
        

b=bank()
            
