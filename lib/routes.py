from lib.database_connection import get_flask_database_connection
from lib.CustomerRepository import CustomerRepository
from lib.Customers import Customers
from lib.Accounts import Accounts
from lib.AccountsRepository import AccountsRepository
from flask import request


# You won't need to nest your routes in app.py in a method like this

def apply_routes(app):
    # GET /customer
    # Returns a list of customers
    # Try it:
    #   ; curl http://localhost:5001/customers
    @app.route('/customers', methods=['GET'])
    def get_all_customers():
        connection = get_flask_database_connection(app)
        repository = CustomerRepository(connection)
        return "\n".join([
        str(customer) for customer in repository.all()
        ])
    # GET /customers/<id>
    # Returns a single customer
    #   ; curl http://localhost:5001/customers/1
    @app.route('/customers/<int:id>', methods=['GET'])
    def get_customer(id):
        connection = get_flask_database_connection(app)
        repository = CustomerRepository(connection)
        customer = repository.find(id)  # Retrieve customer using repository
        if customer:
                return str(customer)
        else:
                return "Customer not found", 404  # Handle case where customer is not found
    # POST /customers
    # Creates a new customer
    # Try it:
    #   ; curl -X POST -d "firstname=Lucy&lastname=Smith&contactnumber=+447932443245" http://localhost:5001/customers
    @app.route('/customers', methods=['POST'])
    def create_customer():
        connection = get_flask_database_connection(app)
        repository = CustomerRepository(connection)
        customer = Customers(
        None,
        request.form['firstname'], 
        request.form['lastname'],
        request.form['contactnumber']
    )
    # DELETE /customers/<id>
    # Deletes a customer
    # Try it:
    #   ; curl -X DELETE http://localhost:5001/customers/1
    @app.route('/customers/<int:id>', methods=['DELETE'])
    def delete_customer(id):
        connection = get_flask_database_connection(app)
        repository = CustomerRepository(connection)
        repository.delete(id)
        return "customer deleted successfully"
    
    #curl http://localhost:5001/accounts
    @app.route('/accounts', methods=['GET'])
    def get_all_accounts():
        connection = get_flask_database_connection(app)
        repository = AccountsRepository(connection)
        return "\n".join([
                str(account) for account in repository.all()
        ])
    #curl http://localhost:5001/accounts/2
    @app.route('/accounts/<int:id>', methods=['GET'])
    def get_account(id):
        connection = get_flask_database_connection(app)
        repository = AccountsRepository(connection)
        account = repository.find(id)  # Retrieve account using repository
        if account:
                return str(account)
        else:
                return "Account not found", 404  # Handle case where customer is not found
    
    #curl -X POST -d "accountname=Black&accountnumber=2003455&accountbalance=50000&customerid=1" http://localhost:5001/accounts
    @app.route('/accounts', methods=['POST'])
    def create_account():
        connection = get_flask_database_connection(app)
        repository = AccountsRepository(connection)
        account = Accounts(
        None,
        request.form['accountname'],
        request.form['accountnumber'],
        request.form['accountbalance'],
        request.form['customerid']
    )
        repository.create(account)
        return "Account Created"
        
    #curl -X DELETE http://localhost:5001/accounts/5
    @app.route('/accounts/<int:id>', methods=['DELETE'])
    def delete_account(id):
        connection = get_flask_database_connection(app)
        repository = AccountsRepository(connection)
        repository.delete(id)
        return "Account Deleted"
