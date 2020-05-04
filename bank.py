class Account():
	def __init__(self,owner,balance=0):
		self.owner=owner
		self.balance=balance

	def __str__(self):
		return f"Account holder name is : {self.owner}\nBalance   :Rs. {self.balance} "

	def deposit(self,amount):
		self.balance+=amount
		print(f"Rs. {amount} is deposited")

	def withdraw(self,amount):
		if amount >= self.balance:
			print("insufficient balance!!")
		else:
			print(f"Rs.{amount} is withdrawl")
			self.balance-=amount

accnt1=Account('rahmat',500)
print(accnt1)
accnt1.deposit(500)
accnt1.withdraw(800)
accnt1.withdraw(300)


		
