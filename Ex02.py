class Customer:

    def __init__(self, id, name, contact, address, city, postal_code, country):
        self.id = id
        self.name = name
        self.contact = contact
        self.address = address
        self.city = city
        self.postalcode = postal_code
        self.country = country


class Categories:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class Employees:
    def __init__(self, id, last_name, first_name, birth_date, photo, notes):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.photo = photo
        self.notes = notes
        

class Orders:
    def __init__(self, id, customer_id, employee_id, order_date, shipper_id):
        self.id = id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.shipper_id = shipper_id
