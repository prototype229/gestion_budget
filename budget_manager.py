class BudgetManager:
    def __init__(self, initial_budget):
        self.budget = initial_budget
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})
        self.budget -= amount

    def get_total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def get_remaining_budget(self):
        return self.budget
