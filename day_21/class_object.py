#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 21

#Exercises: Level 1

class Statistics:
    def __init__(self, data):
        self.data = data
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        if n % 2 == 0:
            # average of middle two elements
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            # middle element
            return sorted_data[n//2]
    
    def mode(self):
        freq = {}
        for x in self.data:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        mode = max(freq, key=freq.get)
        return {'mode': mode, 'count': freq[mode]}
    
    def std(self):
        import math
        mean = self.mean()
        variance = sum((x - mean)**2 for x in self.data) / (self.count() - 1)
        return math.sqrt(variance)
    
    def var(self):
        mean = self.mean()
        return sum((x - mean)**2 for x in self.data) / (self.count() - 1)
    
    def freq_dist(self):
        freq = {}
        for x in self.data:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        freq_dist = [(freq[x]/self.count()*100, x) for x in freq]
        return sorted(freq_dist, reverse=True)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

stats = Statistics(ages)

print('Count:', stats.count()) # 25
print('Sum: ', stats.sum()) # 744
print('Min: ', stats.min()) # 24
print('Max: ', stats.max()) # 38
print('Range: ', stats.range()) # 14
print('Mean: ', stats.mean()) # 30.0
print('Median: ', stats.median()) # 29
print('Mode: ', stats.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', stats.std()) # 4.215
print('Variance: ', stats.var()) # 17.729166666666668
print('Frequency Distribution: ', stats.freq_dist())  # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# Exercises: Level 2

class PersonAccount:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        print(f"{self.first_name} {self.last_name}'s Account Info:")
        print(f"Incomes: {self.incomes}")
        print(f"Expenses: {self.expenses}")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expense: {self.total_expense()}")
        print(f"Account Balance: {self.account_balance()}")

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income() - self.total_expense()


# Create a PersonAccount instance
person = PersonAccount("Mubarak", "Daha")

# Add some incomes and expenses
person.add_income("Salary", 5000)
person.add_income("Bonus", 1000)
person.add_expense("Rent", 1500)
person.add_expense("Groceries", 500)

# Get account information and balance
person.account_info()
