from lib.Customers import Customers

def test_for_constructs():
    customers = Customers(1, 'Leah', 'Southern', '+447732443654')
    assert customers.id == 1
    assert customers.firstname == 'Leah'
    assert customers.lastname == 'Southern'
    assert customers.contactnumber == '+447732443654'
    
def test_for_equality():
    Customers_1 = Customers(1, 'Leah', 'Southern', '+447732443654')
    Customers_2 = Customers(1, 'Leah', 'Southern', '+447732443654')
    assert Customers_1 ==  Customers_2
    
def test_for_formatting():
    Customer= Customers(1, 'Leah', 'Southern', '+447732443654')
    assert str(Customer) == "Customers(1, Leah, Southern, +447732443654)"