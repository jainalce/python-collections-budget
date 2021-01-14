from . import Expense

# Class that extends list type
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def __len__(self):
        return (len(self.expenses) + len(self.overages))

    # implement append so that it only appends to self if total < budget
    def append(self, item):
        # TODO Check if item is a number
        if (self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
        # Otherwise append to the overages list and add to the overage total
        else:
            self.overages.append(item)
            self.sum_overages+=item
		
	def __iter__(self):
		iter = iter(self.expenses)
		self.iter_o = iter(self.overages)
		return self
		
	def __next__(self):
		try
			return __next__(self.iter_e)
		except StopIteration as stop:
			return __next__(self.iter_o)
			
		
	def main():
    # Using above class
    # Set starting budget to 500
    myBudgetList = BudgetList(1200)
    # Add expenses, the last expense is 100 and that goes in overages
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    # Test len()
    print('The count of all expenses: ' + str(len(myBudgetList)))
	
	for entry in myBudgetList:
		print(entry)

	if __name__ == "__main__":
    main() 
 