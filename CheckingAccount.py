# David Hill
# SWDV 630 WEEK 2
# CheckingAccount Class

# Program 'CheckingAccount.py' posts a series of deposit and withdrawl transactions
# to a bank checking account, to demonstrate class definition, instantiation, and method
# calling.

# 10/27/19

import datetime

class CheckingAccount:
    '''Define checking account class'''
    
    # class vars
    bank_name = 'UNITED BANKING'      # used in displaying account transactions
    num_of_accounts = 0               # running total count of accounts
    
    def __init__(self, name, address, acct_no, balance):
        self.full_name = name
        self.address = address
        self.acct_no = acct_no
        self._balance = balance
        
        CheckingAccount.num_of_accounts += 1
        
    def _setBalance(self,amount):
        self._balance = amount
        
    def getBalance(self):
        return self._balance
    
    def getName(self):
        '''extract first and last name from instance full_name var'''
        name = self.full_name.split(' ')
        return name[0]+' '+name[-1]        # '-1' means to wrap around to last name
    
    def getAddress(self):
        '''extract address components from instance address var'''
        address = self.address.split(',')
        s =  '\t' + 'Addr L1' + '\t' + address[0]  + '\n'
        s += '\t' + 'Addr L2' + '\t' + address[-2].lstrip() + ',' + address[-1] + '\n'
        return s

    def getAccountNumber(self):
        '''return account number from instance var'''
        return self.acct_no
    
    def getDate(self):
        '''print date in format: Wed Oct 30 20:21:41 2019
           URL resource is https://www.w3schools.com/python/python_datetime.asp'''
        return datetime.datetime.now().strftime('%c')
    
    def printBalance(self):
        '''URL resource is https://code-examples.net/en/q/1439d38'''
        print('Balance as of ',CheckingAccount.getDate(self)+' is ',end='')
        print('${:9,.2f}'.format(CheckingAccount.getBalance(self)))
    
    def chargeAccount(self,amount):
        '''subtract requested amount if sufficient funds in account'''
        if(CheckingAccount.getBalance(self) >= amount) :
            CheckingAccount._setBalance(self, CheckingAccount.getBalance(self)-amount)
            print('Amount of ${:9,.2f}'.format(amount), 'withdrawn')
            CheckingAccount.printBalance(self)
            print('--')
        else:
            print('* * *  Insufficient funds available  * * * ',end='')
            print('${:9,.2f}'.format(amount),end='')
            print('\t\t\tShort funds: ', '${:9,.2f}'.format(CheckingAccount.getBalance(self) - amount))
            print('--')

    def depositAccount(self,amount):
        '''deposit requested funds into account'''
        CheckingAccount._setBalance(self, CheckingAccount.getBalance(self)+amount)
        print('Amount of ${:9,.2f}'.format(amount), 'deposited')
        CheckingAccount.printBalance(self)
        print('--')
    
    def printBeginingBalance(self):
        '''print beginning balance as of this date'''
        print('Beginning Balance as of',CheckingAccount.getDate(self),
              'is','${:9,.2f}'.format(CheckingAccount.getBalance(self)),'\n')
        
    def printEndingBalance(self):
        '''print ending balance at end of transactions'''
        print('\nEnding Balance is ','${:9,.2f}'.format(CheckingAccount.getBalance(self)),'\n')
    
    @classmethod
    def displayTotalAccounts(cls):
        return cls.num_of_accounts   # class method references class var--not instance var

    def __str__(self):
        '''display account information to represent class checkingAccount'''
        s = '\t' + CheckingAccount.bank_name + '\n'
        s += 'Checking Account Information:\t' + '\n\n'
        s += '\t' + 'Name'    + '\t' + CheckingAccount.getName(self)    + '\n'
        s += '\t' + 'Acct#'   + '\t' + CheckingAccount.getAccountNumber(self) + '\n'
        s += CheckingAccount.getAddress(self)
        return s
        
def main():
    david = CheckingAccount('David Hill',
                            '234 Columbus St., Sebastian, FL. 32958',
                            '1554-00034-01',
                            1000.00)
    
    # display account info--__str__(self) is automatically called for object
    print(david)
    
    david.printBeginingBalance()
    
    # post deposit and withdrawl transactions
    david.chargeAccount(100.00)
    david.depositAccount(50.00)
    david.chargeAccount(1500.00)
    david.chargeAccount(10.00)
    david.chargeAccount(24.56)
    david.chargeAccount(90.00)
    david.depositAccount(50.00)
    david.depositAccount(150.00)
    david.chargeAccount(1500.00)
    david.chargeAccount(500.00)
    david.chargeAccount(100.00)
    david.chargeAccount(1000.00)
    
    david.printEndingBalance()
    
    '''two techniques for accessing a var
       URL resource is https://www.youtube.com/watch?v=rq8cL2XMM5M'''
    # 1. access class var directly from within instance
    # print('Total accounts printed: ' + str(david.num_of_accounts))
    
    # 2. access class var via class method
    print('Total accounts printed: ' + str(CheckingAccount.displayTotalAccounts()))
   
if __name__ == '__main__':
    main()
