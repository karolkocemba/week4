# This file supplements the bank_accounts.py file by defining the BankAccount class
# needed to make it run

class BankAccount:

	def __init__(self):
		self.balance = 0.0
	
	def deposit(self, amount):
		self.balance += float(amount)
		
	def withdraw(self, amount):
		if amount<= self.balance:
			self.balance -= float(amount)

	def transfer (self, amount, account):
		if amount <= self.balance:
			self.withdraw(amount)
			account.deposit(amount)