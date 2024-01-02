from lib.database_connection import DatabaseConnection
from lib.CustomerRepository import CustomerRepository
from lib.AccountsRepository import AccountsRepository

connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/BankingCustomers.sql")
customer_repository = CustomerRepository(connection)

for customer in customer_repository.all():
    print(customer)
    
account_repository =AccountsRepository(connection)
    
for account in account_repository.all():
    print(account)