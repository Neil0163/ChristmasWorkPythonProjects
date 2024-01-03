class CustomerRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        from lib.Customers import Customers  # Import Customers class here
        rows = self._connection.execute("SELECT * FROM customers")
        customers = []
        for row in rows:
            customer = Customers(row['id'], row['firstname'], row['lastname'], row['contactnumber'])
            customers.append(customer)
        return customers
    
    def find(self, customer_id):
        from lib.Customers import Customers  # Import Customers class here
        rows = self._connection.execute("SELECT * FROM CUSTOMERS WHERE id = %s", [customer_id])
        row = rows[0]
        return Customers(row['id'], row['firstname'], row['lastname'], row['contactnumber'])
    
    def create(self, customer):
        self._connection.execute("INSERT INTO customers(firstname, lastname, contactnumber) VALUES (%s, %s, %s)", [
            customer.firstname, customer.lastname, customer.contactnumber
        ])
        
    def delete(self, customer_id):
        self._connection.execute("DELETE FROM customers WHERE id = %s", [customer_id])
        return None
