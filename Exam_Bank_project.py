import random
class Account:
    def __init__(self, name, acc_number, email,password , address, account_type) -> None:
        self.name = name
        self.email = email
        self.acc_number = acc_number
        self.password = password
        self.address = address
        self.accType = account_type
        self.balance = 0
        self.total_bank_balance = 0
        self.account_number = acc_number
        self.Transaction_history = []
        self.loan = 0
        self.loan_balance = 0
        self.loan_taken = 0
        self.accounts = []

class User(Account):
    def __init__(self, name, acc_number, email,password , address, account_type):
        super().__init__(name, acc_number, email,password , address, account_type)
    
    def withdraw(self,amount):
            if amount <= self.balance:
                self.balance -= amount
                self.total_bank_balance -= amount
                self.Transaction_history.append({"type": "Withdrawal", "amount": amount})
            else:
                print("Withdrawal amount exceeded")

    def deposit(self, amount):
            self.balance += amount
            self.total_bank_balance += amount
            self.Transaction_history.append({"type": "Deposit", "amount": amount})
        
    def available_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.Transaction_history
    

    def take_loan(self,amount):
          if self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            self.total_bank_balance -= amount
            self.loan_balance += amount
          else:
            print("Loan limit reached")

    def transfer_amount(self,amount,transfer_account):
        
          if amount <= self.balance:
            transfer_account.deposit(amount)
            self.balance -= amount
            self.Transaction_history.append({"type": "Transfer", "amount": amount, "recipient_account": recipient_account.account_number})
            print(f"{amount} transferred to Account Number: {recipient_account.account_number}.")
          else:
             print("Insufficient funds")


class Admin(Account):  
    def __init__(self, name, acc_number, email,password , address, account_type) -> None:
        super().__init__(name, acc_number, email,password , address, account_type)
        

    def create_user_account(self, name, acc_number, email,password , address, account_type):  
        user = User(name, acc_number, email,password , address, account_type)  # Pass acc_number to User constructor
        self.accounts.append(user)
        print(f"Account created for {name}. Account Number: {user.account_number} Account Type : {account_type}")

    def delete_user_account(self):
        account_number = int(input("Enter Account Number to Delete: "))
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} has been deleted.")
                return
        print("Account does not exist.")

    def see_all_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Email: {account.email}, Address: {account.address}, Account Type: {account.accType}, Balance: {account.balance}")

    def total_available_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        print(f"Total Available Balance: {total_balance}")

    def total_loan_amount(self):
        print(f"Total Loan Amount: {self.total_bank_balance}")

    def toggle_loan_feature(self):
             print("Loan feature has been disabled.")


     
           
           

# Main Program
admin = Admin("Admin",1,"shahadatislamshakil507@gmail.com","password","Nai","ADMIN")
account = None
loan_future = True

while True:
    print("\nSelect User Type:")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    option = input("Enter your choice: ")

    if option == "1":

        print("\nLogin :- \n")
        email = input("Enter Email: ")
        password = input("Enter Password:")

        if admin.email == email:
            if admin.password == password:
                while True:
                 print("\nAdmin Options:")
                 print("1. Create another Admin Account")
                 print("2. Create User Account")
                 print("3. Delete User Account")
                 print("4. See All User Accounts")
                 print("5. Check Total Available Balance")
                 print("6. Check Total Loan Amount")
                 print("7. Toggle Loan Feature")
                 print("8. Exit")
                 admin_choice = input("Enter an Option: ")

                 if admin_choice == "1":
                  name = input("Enter Name: ")
                  email = input("Enter Email: ")
                  password = input("Enter Password:")
                  address = input("Enter Address: ")
                  account_type = "ADMIN"
                  acc_number = random.randint(100000, 999999)
                  admin.create_user_account(name, acc_number, email,password , address, account_type)
                
                 elif admin_choice == "2":
                  name = input("Enter Name: ")
                  email = input("Enter Email: ")
                  password = input("Enter Password:")
                  address = input("Enter Address: ")
                  account_type = (input("Account Type :-\n (Savings or Cuurent) :  ")).capitalize()
                  acc_number = random.randint(100000, 999999)
                  admin.create_user_account(name, acc_number, email,password , address, account_type)
                 elif admin_choice == "3":
                  admin.delete_user_account()    
                 elif admin_choice == "4":
                  admin.see_all_accounts()
                 elif admin_choice == "5":
                  admin.total_available_balance()
                 elif admin_choice == "6":
                  admin.total_loan_amount()
                 elif admin_choice == "7":
                   x =(input("Enter Loan Frature:-\n 1. OF\n 2. ON \nEnter :-"))
                   if x == '1':
                     loan_future = False
                     admin.toggle_loan_feature()
                   elif x == '2':
                     loan_future = True
                     print("Loan feature has been enabled.")

                 elif admin_choice == "8":
                     print("Exiting Admin...")
                     break
                 else:
                     print("Invalid choice. Please try again.")
            else:
                print("Wrongs Passoward!")
        else:
            print("Invalid Email!")       
            
        

    elif option == "2":
           x = int(input("1. Creat New Account\n2. Login\nOption:-"))

           if x == 1:
             print("\nCreat New Account:-\n")
             name = input("Enter Name: ")
             email = input("Enter Email: ")
             password = input("Enter Password:")
             address = input("Enter Address: ")
             account_type = (input("Account Type :-\n (Savings or Cuurent) :  ")).capitalize()
             acc_number = random.randint(100000, 999999)
             user = User(name, acc_number, email, password, address, account_type)
             admin.create_user_account(name, acc_number, email,password , address, account_type)
             account = Account(name,acc_number,email,password,address,account_type)
            
             while True:
                print("\nUser Options:")
                print("1. Create Another Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Check Available Balance")
                print("5. View Transaction History")
                print("6. Take Loan")
                print("7. Transfer Amount")
                print("8. Exit")
                user_choice = input("Enter User choice: ")

                if user_choice == "1":
                   name = input("Enter Name: ")
                   email = input("Enter Email: ")
                   password = input("Enter Password:")
                   address = input("Enter Address: ")
                   account_type = (input("Account Type :-\n (Savings or Current) :-  ")).capitalize()
                   acc_number = random.randint(100000, 999999)
                   if account_type == 'SAVINGS' or account_type == 'CURRENT': 
                    user = User(name, acc_number, email, password, address, account_type)
                    admin.create_user_account(name, acc_number, email,password , address, account_type)
                   else:
                      print(f"Wrong ! You write {account_type} type account.Right Savings or Current Account")

                elif user_choice == "2":
                  amount = float(input("Enter deposit amount: "))
                  user.deposit(amount)
                elif user_choice == "3":
                  amount = float(input("Enter withdrawal amount: "))
                  user.withdraw(amount)
                elif user_choice == "4":
                    print(f"Available Balance: {user.available_balance()}")
                elif user_choice == "5":
                  print("Transaction History:")
                  print(user.get_transaction_history())
                elif user_choice == "6":
                  if loan_future == True:
                    amount = float(input("Enter Loan Amount: "))
                    user.take_loan(amount)
                  else:
                       print("Loan Fauture don't  Avaliable")
                
                elif user_choice == "7":
                    recipient_account_number = int(input("Enter recipient's Account Number: "))
                    recipient_account = None
                    for account in admin.accounts:
                     if account.account_number == recipient_account_number:
                        recipient_account = account
                        break
                    if recipient_account:
                     amount = float(input("Enter transfer amount: "))
                     User.transfer_amount(amount, recipient_account)
                    else:
                     print("Recipient account not found.")
                elif user_choice == "8":
                 print("Exiting User...")
                 break
                else:
                 print("Invalid choice. Please try again.")

           elif x == 2:
             print("\nLogin :- \n")
             email = input("Enter Email: ")
             password = input("Enter Password:")
         

             if account.email == email:
               if account.password == password:
                  
                  while True:
                      print("\nUser Options:")
                      print("1. Create Another Account")
                      print("2. Deposit")
                      print("3. Withdraw")
                      print("4. Check Available Balance")
                      print("5. View Transaction History")
                      print("6. Take Loan")
                      print("7. Transfer Amount")
                      print("8. Exit")
                      user_choice = input("Enter User choice: ")

                      if user_choice == "1":
                       name = input("Enter Name: ")
                       email = input("Enter Email: ")
                       password = input("Enter Password:")
                       address = input("Enter Address: ")
                       account_type = (input("Account Type :-\n (Savings or Current) :-  ")).capitalize()
                       acc_number = random.randint(100000, 999999)
                       if account_type == 'SAVINGS' or account_type == 'CURRENT': 
                        user = User(name, acc_number, email, password, address, account_type)
                        admin.create_user_account(name, acc_number, email,password , address, account_type)
                       else:
                        print(f"Wrong ! You write {account_type} type account.Right Savings or Current Account")

                      elif user_choice == "2":
                        amount = float(input("Enter deposit amount: ")) 
                        user.deposit(amount)
                      elif user_choice == "3":
                          amount = float(input("Enter withdrawal amount: "))  
                          user.withdraw(amount)
                      elif user_choice == "4":
                        print(f"Available Balance: {user.available_balance()}")
                      elif user_choice == "5":
                           print("Transaction History:")
                           print(user.get_transaction_history())
                      elif user_choice == "6":
                        if loan_future == True:
                         amount = float(input("Enter Loan Amount: "))
                         user.take_loan(amount)
                        else:
                         print("Loan Fauture don't  Avaliable")
                
                      elif user_choice == "7":
                       recipient_account_number = int(input("Enter recipient's Account Number: "))
                       recipient_account = None
                       for account in admin.accounts:
                          if account.account_number == recipient_account_number:
                            recipient_account = account
                            break
                       if recipient_account:
                          amount = float(input("Enter transfer amount: "))
                          User.transfer_amount(amount, recipient_account)
                       else:
                         print("Recipient account not found.")
                      elif user_choice == "8":
                         print("Exiting User...")
                         break
                      else:
                        print("Invalid choice. Please try again.")
               
               else:
                  print("Wrongs Passoward!")
             else:
               print("Invalid Email!") 
                  
    elif option == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
