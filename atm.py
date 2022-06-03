from bank import Bank, SavingsAccount


# Implementation of ATM class
def raw_input(param):
    pass


class ATM(object):
    '''This class represents terminal-based
    ATM transactions.'''

    # Implementation of __init__
    def __init__(self, bank):
        self._account = None
        self._bank = bank
        self._methods = {}  # Jump table for commands
        self._methods["1"] = self._getBalance
        self._methods["2"] = self._deposit
        self._methods["3"] = self._withdraw
        self._methods["4"] = self._quit

    # Implementation of run method
    def run(self):
        '''Logs in users and processes their accounts.'''
        failureCount = 0
        # Iterate the loop
        while True:
            # Prompt user to enter name
            userName = raw_input("Enter Name : ")
            # Prompt user to enter PIN
            pin = raw_input("Enter PIN : ")
            # Load account
            self._account = self._bank.get(pin)
            # If account was not found
            # Print "Error, unrecognized PIN"
            if (self._account == None):
                # Display statement
                print("Error, unrecognized PIN")
                failureCount += 1
                # If account name does not match name
                # Print "Error, unrecognized name"
            elif (self._account.getName() != userName):
                # Display statement
                print("Error, unrecognized name")
                # Increment the failureCount
                failureCount += 1

            # If account is valid
            # Load account menu
            else:
                self._processAccount()

            # If an invalid entry was made three times
            # Print "Shutting down and calling the cops!" and end program
            if (failureCount >= 3):
                # Display statement
                print("Shutting down and calling the cops!")
                return

    # Implementation of _processAccount method
    def _processAccount(self):

        '''A menu-driven command processor for a user.'''

        # Iterate the loop
        while True:
            # Display statement
            print("1 View your balance")
            print("2 Make a deposit")
            print("3 Make a withdrawal")
            print("4 Quit\n")

            # Get the number from user
            number = raw_input("Enter a number: ")
            theMethod = self._methods.get(number, None)

            # check theMethod is equal to None or not
            if theMethod == None:
                # Display statement
                print("Unrecognized number")
            else:
                theMethod()

            if self._account == None:
                break

    # Implementation of _getBalance method
    def _getBalance(self):
        # Display statement
        print("Your balance is $", self._account.getBalance())

    # Implementation of _deposit method
    def _deposit(self):
        # Get the amount from user
        amount = float(raw_input("Enter the amount to deposit: "))
        self._account.deposit(amount)

    # Implementation of _withdraw method
    def _withdraw(self):
        # Get the amount from user
        amount = float(raw_input("Enter the amount to withdraw: "))
        message = self._account.withdraw(amount)

        if message:
            # Display statement
            print(message)

    # Implementation of _quit method
    def _quit(self):
        self._bank.save()
        self._account = None
        # Display statement
        print("Have a nice day!")


# Top-level functions
# Implementation of main metthod
def main():
    '''Instantiate an ATM and run it.'''
    bank = Bank("bank.dat")
    atm = ATM(bank)
    atm.run()

# Implementation of createBank method
def createBank(number=0):
    """Saves a bank with the specified number of accounts.
    Used during testing."""

    # create an object for Bank class
    bank = Bank()

    # Iterate the loop
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1), str(1000 + i), 100.00))
        bank.save("bank.dat")


# Creates a bank with the following names / PINS:
# Name1, 1000
# Name2, 1001
# Name3, 1002
# Name4, 1003
# Name5, 1004

createBank(5)
# call main function
main()
