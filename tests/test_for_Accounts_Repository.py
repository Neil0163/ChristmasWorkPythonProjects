from lib.AccountsRepository import AccountsRepository
from lib.Accounts import Accounts


def test_for_all_accounts(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = AccountsRepository(db_connection)
    result = repository.all()
    assert result == [
    Accounts(1, 'Premier', 2009223, 3000, 1),
    Accounts(2, 'Savings', 3009004, 5000, 2),
    Accounts(3, 'Black', 4332367, 10000, 3),
    Accounts(4, 'Ruby', 2076554, 11245, 1)
]
    
def test_for_find_method(db_connection):
    repository = AccountsRepository(db_connection)
    result = repository.find(3)
    assert result == Accounts(3, 'Black', 4332367, 10000, 3)
    
def test_for_create(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = AccountsRepository(db_connection)
    account = Accounts(None, 'test', 2045443, 12446, 3)
    assert repository.create(account) == None
    result = repository.all()
    assert result == [
    Accounts(1, 'Premier', 2009223, 3000, 1),
    Accounts(2, 'Savings', 3009004, 5000, 2),
    Accounts(3, 'Black', 4332367, 10000, 3),
    Accounts(4, 'Ruby', 2076554, 11245, 1),
    Accounts(5, 'test', 2045443, 12446, 3)
    ]

def test_for_delete(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = AccountsRepository(db_connection)
    assert repository.delete(3) == None
    result = repository.all()
    assert result == [
    Accounts(1, 'Premier', 2009223, 3000, 1),
    Accounts(2, 'Savings', 3009004, 5000, 2),
    Accounts(4, 'Ruby', 2076554, 11245, 1)
    ]