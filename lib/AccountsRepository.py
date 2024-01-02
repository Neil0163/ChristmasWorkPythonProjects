from lib.Accounts import Accounts

class AccountsRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM accounts")
        accounts = []
        for row in rows:
            account = Accounts(
                row['id'],
                row['accountname'],
                row['accountnumber'],
                row['accountbalance'],
                row['customerid']
            )
            accounts.append(account)
        return accounts
    
    def find(self, account_id):
        rows = self._connection.execute("SELECT * FROM ACCOUNTS WHERE id = %s", [account_id])
        row = rows[0]
        return Accounts(row['id'], row['accountname'], row['accountnumber'], row['accountbalance'], row['customerid'])
    
    def create(self, account):
        self._connection.execute("INSERT INTO accounts(accountname, accountnumber, accountbalance, customerid) VALUES (%s, %s, %s, %s)", [
            account.accountname, account.accountnumber, account.accountbalance, account.customerid
        ])
        return None

    def delete(self, account_id):
        self._connection.execute ("DELETE FROM accounts WHERE id = %s",[account_id])
        return None