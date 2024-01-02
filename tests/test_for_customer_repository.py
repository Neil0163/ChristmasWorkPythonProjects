from lib.Customers import Customers
from lib.CustomerRepository import CustomerRepository

def test_for_list_all_customers(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = CustomerRepository(db_connection)
    result = repository.all()
    assert result == [
        Customers(1, 'Leah', 'Southern', '+447732443654'),
        Customers(2, 'John', 'Doe', '+447932445396'),
        Customers(3, 'Alan', 'Carr', '+447921124786')
    ]
    
def test_for_find_method(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = CustomerRepository(db_connection)
    result = repository.find(2)
    assert result == Customers(2, 'John', 'Doe', '+447932445396')
    
def test_for_create(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = CustomerRepository(db_connection)
    customer = Customers(None, 'test', 'test', '+447732443655')
    repository.create(customer)
    result = repository.all()
    assert result == [
        Customers(1, 'Leah', 'Southern', '+447732443654'),
        Customers(2, 'John', 'Doe', '+447932445396'),
        Customers(3, 'Alan', 'Carr', '+447921124786'),
        Customers(4, 'test', 'test', '+447732443655')
    ]

def test_for_delete(db_connection):
    db_connection.seed("seeds/BankingCustomers.sql")
    repository = CustomerRepository(db_connection)
    assert repository.delete(3) == None
    result = repository.all()
    assert result == [
        Customers(1, 'Leah', 'Southern', '+447732443654'),
        Customers(2, 'John', 'Doe', '+447932445396')
        ]
        