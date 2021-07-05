
class Employee:
    def __init__(self, id_, name, salary, address, department, email, phone):
        self.id_ = id_
        self.name = name
        self.salary = salary
        self.address = address
        self.department = department
        self.email = email
        self.phone = phone

    def print_info(self):
        print("the id is: " + str(self.id_))
        print("the name is: " + str(self.name))
        print("the salary is: " + str(self.salary))
        print("the address is: " + str(self.address))
        print("the department is: " + str(self.department))
        print("the email is: " + str(self.email))
        print("the phone is: " + str(self.phone))
        print("--------------------------------")
