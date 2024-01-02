class Accounts:
    def __init__(self, id, accountname, accountnumber, accountbalance, customerid):
        self.id = id 
        self.accountname = accountname
        self.accountnumber = accountnumber
        self.accountbalance = accountbalance
        self.customerid = customerid
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__ 
    
    def __repr__(self):
        return f"Accounts({self.id}, {self.accountname}, {self.accountnumber}, {self.accountbalance}, {self.customerid})"
