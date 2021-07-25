import os
from csv import DictWriter, writer
import Ex02 as data


def save_info(table_name, class_var):
    try:
        os.makedirs('Database Exercise 03')
    except FileExistsError:
        pass

    file_path = 'Database Exercise 03/' + table_name + '.csv'
    info = [val for val in vars(class_var).values()]
    headers = [key for key in vars(class_var).keys()]

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, mode='a') as f:
            writer_object = writer(f, dialect='excel')
            writer_object.writerow(info)
            f.close()
    else:
        with open(file_path, mode='w') as f:
            dw = DictWriter(f, delimiter=',', fieldnames=headers)
            dw.writeheader()
            writer_object = writer(f, dialect='excel')
            writer_object.writerow(info)
            f.close()

    print(f'The data has been save in {file_path}')

def input_data():
    while True:
        table = input('Enter the table you want to input data (done to save): ')
        table = table.capitalize()
        
        if table == 'Customers':
            name = input('Enter the customer name: ')
            contact = input('Enter the customer contact name: ')
            address = input('Enter the customer address: ')
            city = input('Enter the customer city: ')
            postal_code = input('Enter the city postal code: ')
            country = input('Enter the customer country: ')
            cus = data.Customers(name, contact, address, city, postal_code, country)
            save_info(table, cus)

        elif table == 'Employees':
            last_name = input('Enter the employee last name: ')
            first_name = input('Enter the employee first name: ')
            birth_date = input('Enter the employee birth date (DD-MM-YYYY): ')
            photo = input('Enter the file name of employee photo: ')
            notes = input('Enter notes for employee: ')
            emp = data.Employees(last_name, first_name, birth_date, photo, notes)
            save_info(table, emp)

        elif table == 'Categories':
            cat_name = input('Enter the category name: ')
            descript = input('Enter the category description: ')
            cat = data.Categories(cat_name, descript)
            save_info(table, cat)

        elif table == 'Shippers':
            ship_name = input('Enter the shipper name: ')
            phone = input('Enter the shipper phone number: ')
            ship = data.Shippers(ship_name, phone)
            save_info(table, ship)

        elif table == 'Suppliers':
            sup_name = input('Enter the supplier name: ')
            contact = input('Enter the supplier contact name: ')
            address = input('Enter the supplier address: ')
            city = input('Enter the supplier city: ')
            postal_code = input('Enter the city postal code: ')
            country = input('Enter the supplier country: ')
            phone = input('Enter the supplier phone number: ')
            sup = data.Suppliers(sup_name, contact, address, city, postal_code, country, phone)
            save_info(table, sup)

        elif table == 'Orders':
            cus_id = input('Enter customer ID: ')
            emp_id = input('Enter employee ID: ')
            order_date = input('Enter order date: ')
            shipper_id = input('Enter shipper ID: ')
            order = data.Orders(cus_id, emp_id, order_date, shipper_id)
            save_info(table, order)

        elif table == 'Products':
            prod_name = input('Enter product name: ')
            sup_id = input('Enter the supplier ID: ')
            cat_id = input('Enter the category ID: ')
            unit = input('Enter the product unit: ')
            price = input('Enter the product price: ')
            product = data.Products(prod_name, sup_id, cat_id, unit, price)
            save_info(table, product)

        elif table == 'Orderdetails':
            order_id = input('Enter the order ID: ')
            prod_id = input('Enter the product ID: ')
            quantity = input('Enter the order quantity:')
            ord_detail = data.OrderDetails(order_id, prod_id, quantity)
            save_info('OrderDetails', ord_detail)

        elif table.lower() == 'done':
    
            return False
        


input_data()
