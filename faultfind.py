
from lib.Accounts import Accounts
# Test code
accounts_list = [
    Accounts(1, 'Premier', 2009223, '£', 3000.00, 1),
    Accounts(2, 'Savings', 3009004, '£', 5000.00, 2),
    Accounts(3, 'Black', 4332367, '£', 10000.00, 3),
    Accounts(4, 'Ruby', 2076554, '£', 11245.20, 1)
]

expected_list = [
    Accounts(1, 'Premier', 2009223, '£', 3000.00, 1),
    Accounts(2, 'Savings', 3009004, '£', 5000.00, 2),
    Accounts(3, 'Black', 4332367, '£', 10000.00, 3),
    Accounts(4, 'Ruby', 2076554, '£', 11245.20, 1)
]

for i, (account, expected_account) in enumerate(zip(accounts_list, expected_list)):
    if account != expected_account:
        print(f"Difference at index {i}:")
        print(f"Actual Account: {account}")
        print(f"Expected Account: {expected_account}")
