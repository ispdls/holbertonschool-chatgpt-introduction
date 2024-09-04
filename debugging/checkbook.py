class Checkbook:
    """
    A simple checkbook class for managing a bank account balance.
    
    Attributes:
    balance (float): The current balance of the checkbook.

    Methods:
    deposit(amount):
        Deposits a specified amount into the checkbook.
    withdraw(amount):
        Withdraws a specified amount from the checkbook, if sufficient funds are available.
    get_balance():
        Prints the current balance of the checkbook.
    """

    def __init__(self):
        """
        Initializes a new Checkbook instance with a balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the given amount into the checkbook.

        Parameters:
        amount (float): The amount of money to deposit. Must be positive.

        Prints:
        - Confirmation of the deposited amount.
        - The updated balance.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the given amount from the checkbook if there are sufficient funds.

        Parameters:
        amount (float): The amount of money to withdraw. Must be positive.

        Prints:
        - Confirmation of the withdrawn amount if successful.
        - An error message if funds are insufficient.
        - The updated balance or the same balance if withdrawal fails.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))
def main():
    """
    Runs a simple command-line interface for interacting with the Checkbook class.
    
    The user can choose to deposit, withdraw, check the balance, or exit the program.

    Commands:
    - deposit: Prompts for an amount to deposit and adds it to the balance.
    - withdraw: Prompts for an amount to withdraw and subtracts it from the balance if sufficient funds are available.
    - balance: Displays the current balance.
    - exit: Exits the program.
    
    The loop continues until the user enters 'exit'.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the program.")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $").strip())
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $").strip())
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
