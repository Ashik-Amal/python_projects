

print("Bank Account System")
print("1.Show Account Balance")
print("2.Deposit")
print("3.withdraw")
print("4.Exit")






check = False
class Bank:
    def __init__(n,balance):
        n.balance = balance
    def Deposit(n):
        
        deposit = int(input("Enter the amount to be deposited:"))
        n.balance += deposit
        print(f'₹{n.balance} has been deposited to your account')
        
        
        
       
    def withdraw (n):
        withdraww = int(input("Enter the amount to be Withdrawn:"))
        n.balance -= withdraww
        
        print(f'₹{withdraww} has been withdrawn from your account,avail balance is {n.balance}')
        
        
    def Showdetails(n):
       
        print(f'The total available balance is ₹ {n.balance}')
        
        
    def exit(n):
        print("Thank you, Have a nice day !!")
        
class account_holder :
    acc_holder_details =[
        
        {"m_name":"sanil","m_id":101801,"m_details":100001},
    
        {"m_name":"niju","m_id":101802,"m_details":100002},
        
        {"m_name":"mathew","m_id":101803,"m_details":100003},
        
        {"m_name":"Adit","m_id":101804,"m_details":100004}
        
        ]
    
    
    def __init__(m,m_name,m_id,m_details):
        m.m_name = m_name
        
        m.m_id = m_id
        
        m.m_details = m_details
        for i in acc_holder_details:
            if i["m_id"]== m_id:
                check = True
                print("Account access success")
        
        
        
        
        
        
acc_holder_details =[
        
        {"m_name":"sanil","m_id":101801,"m_details":100001},
    
        {"m_name":"niju","m_id":101802,"m_details":100002},
        
        {"m_name":"mathew","m_id":101803,"m_details":100003},
        
        {"m_name":"Adit","m_id":101804,"m_details":100004}
        
        ]

obj1 = Bank(0)
m_id =int(input("enter your id:"))
obj2 = account_holder(m_id)


    
while  True :
    

    a = int(input("Choose any (1-4): "))
    if a ==1:
        
       obj1.Showdetails()
       
    elif a == 2:
        obj1.Deposit()
        
    elif a == 3:
        obj1.withdraw()
        
    elif a == 4:
         obj1.exit()
         break

       
