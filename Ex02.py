class Customers:
    """
    This class contain the CustomerID, CustomerName, ContactName,
    Address, City, PostalCode and Country from Customers table
    """

    __id = 0
    def __init__(self, name, contact, address, city, postal_code, country):
        Customers.__id += 1
        self.CustomerId = Customers.__id
        self.CustomerName = name
        self.ContactName = contact
        self.Address = address
        self.City = city
        self.Postal_code = postal_code
        self.Country = country


class Employees:
    """
    This class contain EmployeeID, LastName, FirstName,
    BirthDate, Photo and Notes from Employees table
    """

    __id = 0
    def __init__(self, last_name, first_name, birth_date, photo, notes):
        Employees.__id += 1
        self.EmployeeID = Employees.__id
        self.LastName = last_name
        self.FirstName = first_name
        self.BirthDate = birth_date
        self.Photo = photo
        self.Notes = notes


class Categories:
    """
    This class contain CategoryID, CategoryName
    and Description from Categories table
    """

    __id = 0
    def __init__(self, name, description):
        Categories.__id += 1
        self.CategoryID = Categories.__id
        self.CategoryName = name
        self.Description = description


class Shippers:
    """
    This class containt ShipperID, ShipperName and Phone
    from Shippers table
    """

    __id = 0
    def __init__(self, name, phone):
        Shippers.__id += 1
        self.ShipperID = Shippers.__id
        self.ShipperName = name
        self.Phone = phone


class Suppliers:
    """
    This class contains SupplierID, SupplierName, ContactName, Address,
    City, PostalCode, Country and Phone from Suppliers table
    """

    __id = 0
    def __init__(self, name, contact_name, address,
                 city, postal_code, country, phone):
        Suppliers.__id += 1
        self.SupplierID = Suppliers.__id
        self.SupplierName = name
        self.ContactName = contact_name
        self.Address = address
        self.City = city
        self.PostalCode = postal_code
        self.Country = country
        self.Phone = phone


class Orders:
    """
    This class contain OrderID, CustomerID, EmployeeID,
    OrderDate and ShipperID from Orders table
    """
    
    __id = 0
    def __init__(self, cus_id, employ_id, order_date, shipper_id):
        Orders.__id += 1
        self.OrderID = Orders.__id
        self.CustomerID = cus_id
        self.EmployeeID = employ_id
        self.OrderDate = order_date
        self.ShipperID = shipper_id


class Products:
    """
    This class contains ProductID, SupplierID, CatergoryID,
    Unit and Price from Products table
    """

    __id = 0
    def __init__(self, product_name, sup_id, cat_id, unit, price):
        Products.__id += 1
        self.ProductID = Products.__id
        self.ProductName = product_name
        self.SupplierID = sup_id
        self.CatergoryID = cat_id
        self.Unit = unit
        self.Price = price


class OrderDetails:
    """
    This class containt OrderDetailID, OrderId, ProductId, Quantity
    from OrderDetails table
    """

    __id = 0
    def __init__(self, ord_id, prod_id, quantity):
        OrderDetails.__id += 1
        self.OderDetailID = OrderDetails.__id
        self.OrderID = ord_id
        self.ProductID = prod_id
        self.Quantity = quantity

