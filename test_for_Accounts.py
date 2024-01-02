from lib.Accounts import Accounts


def test_for_accounts_construct():
    accounts = Accounts(1, 'Premier', 2009223, 3000.00, 1)
    assert accounts.id == 1 
    assert accounts.accountname == 'Premier'
    assert accounts.accountnumber == 2009223
    assert accounts.accountbalance == 3000.00
    assert accounts.customerid == 1
    
def test_for_eq():
    account_1 = Accounts(1, 'Premier', 2009223,  3000, 1)
    account_2 = Accounts(1, 'Premier', 2009223,  3000, 1)
    assert account_1 == account_2
    
def test_for_formatting():
    accounts = Accounts(1, 'Premier', 2009223, 3000 , 1)
    assert str(accounts) == "Accounts(1, Premier, 2009223, 3000, 1)"
