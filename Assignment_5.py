#### CHALLENGE 1: Square numbers and return their sum

class points:
    def __init__(self,x,y,z):
       self.x = x
       self.y = y
       self.z = z
    def square_sum(self):   
        a = self.x *self.x
        b = self.y *self.y
        c = self.z *self.z
        total_sum= a+b+c 
        print("Total squaresum of x,y & z is :",total_sum)

x=int(input("Enter value of x: "))     
y=int(input("Enter value of y: "))    
z=int(input("Enter value of z: "))    
P1= points(x,y,z)
P1.square_sum() 




# CHALLENGE 2: Implement a Calculator Class

num1 = int(input("Enter num1: ")) 
num2 = int(input("Enter num2: ")) 
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self,num1,num2):
        return num1 + num2
    def subtract(self,num1,num2):
        return num2 - num1
    def multiply(self,num1,num2):
        return num1 * num2
    def divide(self,num1,num2):    
         return num2 / num1
           
obj = Calculator() 
print(obj.add(num1,num2))
print(obj.subtract(num1,num2))
print(obj.multiply(num1,num2))
print(obj.divide(num1,num2)) 

# CHALLENGE 3: Implement the Complete Student Class

class Student:
    def stu_details (self,name,RollNumber):
        self.__name = name
        self.__RollNumber = RollNumber
        print("Student Details: ",self.__name,self.__RollNumber)
    def setName(self,New_name):
        self.__name = New_name
    def setRollNumber(self,New_RollNumber):
        self.__RollNumber = New_RollNumber
    def getName(self):
         return  self.__name    
    def getRollNumber(self):
        return  self.__RollNumber 
   
S = Student()
name = input("Enter Student name: ")
RollNumber=int(input("Enter Student RollNumber: "))
S.stu_details(name,RollNumber)
print("Student Name: ",S.getName())
print("Student RollNumber: ",S.getRollNumber())
S.setName(input("Enter Student New_name: ")) 
S.setRollNumber(int(input("Enter Student New_RollNumber: ")))
print("New Student name : ",S.getName())
print("New Student RollNumber: ",S.getRollNumber())

# CHALLENGE 4 : Implement a Banking Account


class Account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
       
class SavingsAccount(Account):
    def __init__(self,title,balance,interestRate):
        super().__init__(title,balance)
        self.interestRate = interestRate
    def printme(self):   
        print("title:",self.title )   
        print("balance:",self.balance)
        print("interestRate:",self.interestRate)
a = SavingsAccount("Asish",'5000','5')
a.printme()  


# CHALLENGE 5 : Handling a Bank Account

class Account:  
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance
    def withdraw(self,amount):
        if amount >  self.balance:
            print("Insufficient balance: ")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")

    def deposit(self,amount):
        self.balance += amount
        print(f"${amount} has been deposited in youraccount.")
    def getbalance(self):
        print(" Current balance is $ ",self.balance)
class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestrate = interestRate 
    def interestAmount(self):
        Int_Amount =  (self.interestrate * self.balance)/100
        print("total interest ammount is :",Int_Amount)
        print("Title: ",self.title)
        print("Current balance: ",self.balance)
     
a =SavingsAccount("SBI Bank",30000,5) 
print(a.withdraw(500))
print(a.deposit(2000))
print(a.interestAmount())    





        






              

 

                    














        