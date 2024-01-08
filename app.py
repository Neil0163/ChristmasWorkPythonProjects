import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.CustomerRepository import CustomerRepository
from lib.Customers import Customers
from lib.Accounts import Accounts
from lib.AccountsRepository import AccountsRepository



# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
#HTML ROUTES

@app.route('/welcome')
def get_welcome():
    return render_template("welcome.html", message = "Welcome to the banking App" )

#CUSTOMER ROUTES
@app.route('/customers', methods=['POST'])
def create_customer():
    if has_invalid_customer_parameters(request.form):
        return "You need to input customer Data", 400
    connection = get_flask_database_connection(app)
    repository = CustomerRepository(connection)
    customer = Customers(
        None,
        request.form['firstname'], 
        request.form['lastname'],
        request.form['contactnumber']
    )
    repository.create(customer)
    return  '', 200

@app.route('/customers', methods=['GET'])
def get_all_customers():
    connection = get_flask_database_connection(app)
    repository = CustomerRepository(connection)
    return "\n".join([
        str(customer) for customer in repository.all()
        ])

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
        connection = get_flask_database_connection(app)
        repository = CustomerRepository(connection)
        customer = repository.find(id)  
        if customer:
                return str(customer)
        else:
                return "Customer not found", 404
            
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
        connection = get_flask_database_connection(app)
        repository = CustomerRepository(connection)
        repository.delete(id)
        return "customer deleted successfully"
    
#ACCOUNT ROUTES 
@app.route('/accounts', methods=['POST'])
def create_account():
    if has_invalid_account_parameters(request.form):
        return "You need to input Account Data", 400
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
    return  '', 200

@app.route('/accounts', methods=['GET'])
def get_all_accounts():
    connection = get_flask_database_connection(app)
    repository = AccountsRepository(connection)
    return "\n".join([
        str(account) for account in repository.all()
        ])

@app.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
        connection = get_flask_database_connection(app)
        repository = AccountsRepository(connection)
        account = repository.find(id)  # Retrieve account using repository
        if account:
                return str(account)
        else:
                return "Account not found", 404  # Handle case where customer is not found
            
@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
        connection = get_flask_database_connection(app)
        repository = AccountsRepository(connection)
        repository.delete(id)
        return "Account Deleted"
    



# == Functions== 
def has_invalid_customer_parameters(form):
    return 'firstname' not in form or 'lastname' not in form or 'contactnumber' not in form 

def has_invalid_account_parameters(form):
    return(
        'accountname' not in form
        or 'accountnumber' not in form
        or 'accountbalance' not in form
        or 'customerid' not in form
        or not form['accountnumber'].isnumeric()
        or not form['customerid'].isnumeric()
        or not form['accountbalance'].isnumeric()
    )
    
    


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(
    debug=True, # Optional but useful for now
    host="0.0.0.0" # Listen for connections directed _to_ any address
    )
    
# These lines start the app on a local machine in a virtual enviroment
#if __name__ == '__main__':
#    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
