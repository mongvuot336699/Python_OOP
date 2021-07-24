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



class Order:
    """
    This class containt information such as:
    OrderID, CusID, Employ_id, Order_date, Shipper_id
    """

    def __init__(self, order_id, customer_id,
                 employee_id, order_date, shipper_id):
        self.OrderId = order_id
        self.CustomerId = customer_id
        self.EmployeeId = employee_id
        self.OrderDate = order_date
        self.ShippingId = shipper_id


class OrderDetail:
    """
    This class containt information such as:
    OrderDetailID, OrderId, ProductId, Quantity    
    """

    def __init__(self, order_detail_id, order_id, product_id, quantity):
        self.OrderDetailId = order_detail_id
        self.OrderId = order_id
        self.ProductId = product_id
        self.Quantity = quantity


class Shipper:
    """
    This class containt information about shipper_id, shipper_name, Phone
    """

    def __init__(self, shipper_id, shipper_name, phone):
        self.ShipperId = shipper_id
        self.ShipperName = shipper_name
        self.Phone = phone


class Supplier:
    """
    This class contain information about SupplierId, ContactName, Address,
    City, PostalCode, Country, Phone
    """

    def __init__(self, supperlier_id, contact_name, address,
                 city, postal_code, country, phone):
        self.SupperlierId = supperlier_id
        self.ContactName = contact_name
        self.Address = address
        self.City = city
        self.PostalCode = postal_code
        self.Country = country
        self.Phone = phone


class Product:
    """
    This class contain information about ProductID, SupplierID, CatergoryID, Unit, Price
    """

    def __init__(self, product_id, product_name, supplier_id, catergory_id, unit, price):
        self.ProductId = product_id
        self.ProductName = product_name
        self.SupplierId = supplier_id
        self.CatergoryId = catergory_id
        self.Unit = unit
        self.Price = price
