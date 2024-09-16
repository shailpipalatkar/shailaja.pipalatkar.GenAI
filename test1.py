import random

class BankAccount:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = random.randint(1000, 100000)  # Random balance between 1000 and 100000
        self.transactions = []
    
    def perform_transactions(self, months):
        for _ in range(months):
            # Random number of transactions for each month (1 to 5)
            for _ in range(random.randint(1, 5)):
                amount = random.randint(100, 5000)
                transaction_type = random.choice(['deposit', 'withdrawal'])
                if transaction_type == 'deposit':
                    self.balance += amount
                    self.transactions.append(f"Deposited: {amount}")
                else:
                    self.balance -= amount
                    self.transactions.append(f"Withdrew: {amount}")
        
    def __repr__(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance}"

# Create 100 accounts
accounts = [BankAccount(i) for i in range(1, 101)]

# Perform random transactions for each account
for account in accounts:
    months = random.randint(1, 12)
    account.perform_transactions(months)

# Sort accounts by balance
sorted_accounts = sorted(accounts, key=lambda x: x.balance)

# Display sorted accounts
for account in sorted_accounts:
    print(account)
