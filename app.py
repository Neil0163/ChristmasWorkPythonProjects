import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.CustomerRepository import CustomerRepository
from lib.Customers import Customers
from lib.Accounts import Accounts
from lib.AccountsRepository import AccountsRepository



# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
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

# == Functions== 
def has_invalid_customer_parameters(form):
    return 'firstname' not in form or 'lastname' not in form or 'contactnumber' not in form 
    
    


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))