class Customers:
    def __init__(self, id, firstname, lastname, contactnumber):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.contactnumber = contactnumber
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Customers({self.id}, {self.firstname}, {self.lastname}, {self.contactnumber})"
    
    