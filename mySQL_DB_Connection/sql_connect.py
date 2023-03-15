# Testing the connection between python and MySQL

import mysql.connector
from mysql.connector import Error
import sys
import re

def main_menu():
    print("What do you want to do with the database?\n")
    print("1. Insert a record")
    print("2. Modify a record")
    print("3. Delete a record")
    print("4. Show all Records")
    print("5. Exit the connection to the database.")

def sub_menu():
    print("\nWhich table do you want to insert/modify/delete data into or from?\n")
    print("1. ADMINS")
    print("2. SPONSORS")
    print("3. DRIVERS")
    print("4. POINTS")
    print("5. ORDERS")
    print("6. PRODUCTS")
    print("7. Back to main menu")

def modify_data(connection, table_name):
    cursor = connection.cursor()
    record_id = input("Enter the ID of the record you want to modify: ")

    # Check if the record exists
    cursor.execute(f"SELECT * FROM {table_name} WHERE {table_name[:-1]}ID = %s", (record_id,))
    result = cursor.fetchone()
    if result is None:
        print("Record not found.")
        return

    # Get the new values for the record, excluding the ID field
    print("Enter the new values for the record:")
    fields = [field[0] for field in cursor.description if not field[0].endswith("ID")]
    values = []
    for field in fields:
        value = input(f"{field}: ")
        values.append(value)

    # Update the record
    query = f"UPDATE {table_name} SET {', '.join([f'{field} = %s' for field in fields])} WHERE {table_name[:-1]}ID = %s"
    values.append(record_id)
    cursor.execute(query, values)
    connection.commit()
    print(f"{cursor.rowcount} record(s) updated.")

# function to delete a record from a table based on user input
def delete_record(table_name):
    cursor = db.cursor()
    if table_name == "POINTS":
        points_id = input(f"Enter the PointsID of the {table_name} record you want to delete: ")
        driver_id = input(f"Enter the DriverID of the {table_name} record you want to delete: ")
        sql = f"DELETE FROM {table_name} WHERE PointsID = %s AND DriverID = %s"
        val = (points_id, driver_id)
    else:
        table_id = input(f"Enter the ID of the {table_name} record you want to delete: ")
        sql = f"DELETE FROM {table_name} WHERE {table_name[:-1]}ID = %s"
        val = (table_id, )
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, f"record(s) deleted from {table_name} table")

def view_all_records():
    tables = ['ADMINS', 'SPONSORS', 'DRIVERS', 'POINTS', 'ORDERS', 'PRODUCTS']

    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchall()

        print(f"\n{table} Table:")
        for row in result:
            if table == 'DRIVERS':
                driver_id = row[0]
                cursor.execute(f"SELECT COUNT(*) FROM DRIVER_SPONSORS WHERE DriverID = {driver_id}")
                sponsor_count = cursor.fetchone()[0]
                print(f"{row} - Sponsor Count: {sponsor_count}")
            else:
                print(row)
    
# Establishing a connection with the SQL database
# Fill in the user, password, host, and databse fields
try:
    db = mysql.connector.connect(
    user='team06',
    password='szvwwLrefLpcYb3WAdUU',
    host='team06-database.cobd8enwsupz.us-east-1.rds.amazonaws.com',
    database='USERS'
    )
    if db.is_connected():
        db_Info = db.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        # Create a cursor object to access and navigate the SQL databse
        cursor = db.cursor()
        
        while True:
            main_menu()
            option_choice = input("Enter your choice: ")
            
            # Check if user entered a valid option
            if option_choice not in ['1', '2', '3', '4', '5']:
                print("Invalid input. Please enter a valid option.")
                continue

            if option_choice == '5':
                break

            if option_choice == '1':
                sub_menu()
                table_choice = input("Enter table number: ")

                # Check if user entered a valid option
                if table_choice not in ['1', '2', '3', '4', '5', '6', '7']:
                    print("Invalid input. Please enter a valid option.")
                    continue

                # Exit sub-menu
                if table_choice == '7':
                    continue

                # Get input data for chosen table
                if table_choice == '1':
                    # Grab the AdminID of ADMINS table
                    cursor.execute("SELECT MAX(AdminID) FROM ADMINS")
                    result = cursor.fetchone()
                    admin_id = result[0] + 1 if result[0] else 1

                    last_name = input("Enter last name: ")
                    first_name = input("Enter first name: ")
                    
                    # Prompt user for unique email
                    while True:
                        email = input("Enter email: ")
                        cursor.execute(f"SELECT * FROM ADMINS WHERE Email='{email}'")
                        if cursor.fetchone():
                            print("Error: Email already taken.")
                        else:
                            break

                    # Prompt user for unique username
                    while True:
                        user_name = input("Enter user name: ")
                        cursor.execute(f"SELECT * FROM ADMINS WHERE UserName='{user_name}'")
                        if cursor.fetchone():
                            print("Error: User name already taken.")
                        else:
                            break

                    # Prompt user for password and validate against constraint
                    while True:
                        password = input("Enter password: ")
                        if len(password) < 8:
                            print("Password must be at least 8 characters long")
                        elif not any(char.isdigit() for char in password):
                            print("Password must contain at least one digit")
                        elif not any(char.islower() for char in password):
                            print("Password must contain at least one lowercase letter")
                        elif not any(char.isupper() for char in password):
                            print("Password must contain at least one uppercase letter")
                        elif not any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for char in password):
                            print("Password must contain at least one special character")
                        else:
                            break
                        
                    # Prompt user to enter a valid phone number
                    while True:
                        phone_number = input("Enter phone number: ")
                        if len(phone_number) == 10:
                            break
                        else:
                            print("Error: Phone number must be 10 digits long.")
                        
                    # Construct SQL query and execute
                    sql_query = f"INSERT INTO ADMINS (AdminID, LastName, FirstName, Email, UserName, PasswordHash, PhoneNumber) VALUES ('{admin_id}', '{last_name}', '{first_name}', '{email}', '{user_name}', '{password}', '{phone_number}')"

                    # Execute query with user input as parameters
                    cursor.execute(sql_query)
                        
                    # Print the executed SQL query
                    print("Executed SQL query: ", sql_query)
                    
                    # Commit the changes to the database
                    db.commit()
                            
                elif table_choice == '2':
                    # Get the sponsor_id from SPONSORS Table
                    cursor.execute("SELECT MAX(SponsorID) FROM SPONSORS")
                    result = cursor.fetchone()
                    sponsor_id = result[0] + 1 if result[0] else 1

                    # Get AdminID for foreign key
                    while True:
                        admin_id = input("Enter AdminID for sponsor: ")
                        # Check if the entered AdminID exists in ADMINS table
                        cursor.execute(f"SELECT AdminID FROM ADMINS WHERE AdminID={admin_id}")
                        result = cursor.fetchone()
                        if result:
                            break
                        else:
                            print("Error: AdminID does not exist.")

                    last_name = input("Enter last name: ")
                    first_name = input("Enter first name: ")
                    
                    # Prompt user for unique email
                    while True:
                        email = input("Enter email: ")
                        cursor.execute(f"SELECT * FROM ADMINS WHERE Email='{email}'")
                        if cursor.fetchone():
                            print("Error: Email already taken.")
                        else:
                            break

                    # Prompt user for unique username
                    while True:
                        user_name = input("Enter user name: ")
                        cursor.execute(f"SELECT * FROM ADMINS WHERE UserName='{user_name}'")
                        if cursor.fetchone():
                            print("Error: User name already taken.")
                        else:
                            break
                    
                    # Prompt user for password and validate against constraint
                    while True:
                        password = input("Enter password: ")
                        if len(password) < 8:
                            print("Password must be at least 8 characters long")
                        elif not any(char.isdigit() for char in password):
                            print("Password must contain at least one digit")
                        elif not any(char.islower() for char in password):
                            print("Password must contain at least one lowercase letter")
                        elif not any(char.isupper() for char in password):
                            print("Password must contain at least one uppercase letter")
                        elif not any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for char in password):
                            print("Password must contain at least one special character")
                        else:
                            break

                    # Prompt user to enter a valid phone number
                    while True:
                        phone_number = input("Enter phone number: ")
                        if len(phone_number) == 10:
                            break
                        else:
                            print("Error: Phone number must be 10 digits long.")

                    sponsor_catalog = input("Enter sponsor catalog: ")
                    sponsor_title = input("Enter sponsor title: ")

                    # Construct SQL query and execute
                    sql_query = f"INSERT INTO SPONSORS (SponsorID, AdminID, LastName, FirstName, Email, UserName, PasswordHash, PhoneNumber, SponsorCatalog, SponsorTitle) VALUES ('{sponsor_id}', '{admin_id}', '{last_name}', '{first_name}', '{email}', '{user_name}', '{password}', '{phone_number}', '{sponsor_catalog}', '{sponsor_title}')"

                    # Execute query with user input as parameters
                    cursor.execute(sql_query)
                        
                    # Print the executed SQL query
                    print("Executed SQL query: ", sql_query)
                    
                    # Commit the changes to the database
                    db.commit()

                elif table_choice == '3':
                    # Get the driver_id from DRIVERS Table
                    cursor.execute("SELECT MAX(DriverID) FROM DRIVERS")
                    result = cursor.fetchone()
                    driver_id = result[0] + 1 if result[0] else 1

                    # Get AdminID for foreign key
                    while True:
                        admin_id = input("Enter AdminID for driver: ")
                        cursor.execute(f"SELECT AdminID FROM ADMINS WHERE AdminID = {admin_id}")
                        if cursor.fetchone():
                            break
                        else:
                            print("Invalid AdminID. Please enter a valid AdminID.")

                    last_name = input("Enter last name: ")
                    first_name = input("Enter first name: ")

                    # Prompt user for unique email
                    while True:
                        email = input("Enter email: ")
                        cursor.execute(f"SELECT * FROM DRIVERS WHERE Email='{email}'")
                        if cursor.fetchone():
                            print("Error: Email already taken.")
                        else:
                            break

                    # Prompt user for unique username
                    while True:
                        user_name = input("Enter user name: ")
                        cursor.execute(f"SELECT * FROM DRIVERS WHERE UserName='{user_name}'")
                        if cursor.fetchone():
                            print("Error: User name already taken.")
                        else:
                            break

                    # Prompt user for password and validate against constraint
                    while True:
                        password = input("Enter password: ")
                        if len(password) < 8:
                            print("Password must be at least 8 characters long")
                        elif not any(char.isdigit() for char in password):
                            print("Password must contain at least one digit")
                        elif not any(char.islower() for char in password):
                            print("Password must contain at least one lowercase letter")
                        elif not any(char.isupper() for char in password):
                            print("Password must contain at least one uppercase letter")
                        elif not any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for char in password):
                            print("Password must contain at least one special character")
                        else:
                            break

                    # Prompt user to enter a valid phone number
                    while True:
                        phone_number = input("Enter phone number: ")
                        if len(phone_number) == 10:
                            break
                        else:
                            print("Error: Phone number must be 10 digits long.")

                    # Insert driver data into DRIVERS table
                    cursor.execute(f"INSERT INTO DRIVERS (DriverID, AdminID, LastName, FirstName, Email, UserName, PasswordHash, PhoneNumber) VALUES ({driver_id}, {admin_id}, '{last_name}', '{first_name}', '{email}', '{user_name}', '{password}', '{phone_number}')")
                    
                    # Prompt user to enter sponsor information
                    while True:
                        sponsor_id = input("Enter SponsorID for driver (press enter to skip): ")
                        if not sponsor_id:
                            break
                        cursor.execute(f"SELECT SponsorID FROM SPONSORS WHERE SponsorID = {sponsor_id}")
                        if cursor.fetchone():
                            # Insert driver-sponsor relationship data into DRIVER_SPONSORS table
                            cursor.execute(f"INSERT INTO DRIVER_SPONSORS (DriverID, SponsorID) VALUES ({driver_id}, {sponsor_id})")
                        else:
                            print("Invalid SponsorID. Please enter a valid SponsorID.")
                    
                    # Commit the changes to the database
                    db.commit()

                
                elif table_choice == '4':
                    # Get the points_id from POINTS Table
                    cursor.execute("SELECT MAX(PointsID) FROM POINTS")
                    result = cursor.fetchone()
                    points_id = result[0] + 1 if result[0] else 1

                    # Get DriverID for foreign key
                    driver_id = input("Enter DriverID for order: ")
                    while not driver_id.isnumeric():
                        driver_id = input("Invalid input. Enter DriverID for order: ")
                    driver_id = int(driver_id)
                    
                    point_date = input("Enter date when points were distributed: ")
                    reason = input("Enter reason for giving points: ")
                    
                    # Loop until a valid input for points is provided
                    while True:
                        try:
                            points = int(input("Enter total points given: "))
                            if points >= 0:
                                break
                            else:
                                print("Points must be a non-negative integer.")
                        except ValueError:
                            print("Points must be a non-negative integer.")

                    # Construct SQL query and execute
                    sql_query = f"INSERT INTO POINTS (PointsID, DriverID, PointDate, Reason, Points) VALUES ('{points_id}', '{driver_id}', '{point_date}', '{reason}', '{points}')"
                    
                   # Execute query with user input as parameters
                    cursor.execute(sql_query)

                    # Print the executed SQL query
                    print("Executed SQL query: ", sql_query)

                    # Commit the changes to the database
                    db.commit()

                elif table_choice == '5':
                    while True:
                        # Get the order_id from ORDERS
                        cursor.execute("SELECT MAX(OrderID) FROM ORDERS")
                        result = cursor.fetchone()
                        order_id = result[0] + 1 if result[0] else 1
                        
                        # Get DriverID and SponsorID for foreign keys
                        # Get SponsorID for foreign key
                        sponsor_id = input("Enter SponsorID for product: ")
                        while not sponsor_id.isnumeric():
                            sponsor_id = input("Invalid input. Enter SponsorID for product: ")
                        sponsor_id = int(sponsor_id)
                        
                        # Get DriverID for foreign key
                        driver_id = input("Enter DriverID for order: ")
                        while not driver_id.isnumeric():
                            driver_id = input("Invalid input. Enter DriverID for order: ")
                        driver_id = int(driver_id)

                        # Construct SQL query and execute
                        sql_query = f"INSERT INTO ORDERS (OrderID, SponsorID, DriverID) VALUES ('{order_id}', '{sponsor_id}', '{driver_id}')"
                        
                        # Execute query with user input as parameters
                        cursor.execute(sql_query)

                        # Print the executed SQL query
                        print("Executed SQL query: ", sql_query)

                        # Commit the changes to the database
                        db.commit()
            
                elif table_choice == '6':
                    # Get the sponsor_id from the database connection
                    cursor.execute("SELECT MAX(ProductID) FROM PRODUCTS")
                    result = cursor.fetchone()
                    product_id = result[0] + 1 if result[0] else 1
                                    
                    # Get SponsorID for foreign key
                    sponsor_id = input("Enter SponsorID for product: ")
                    while not sponsor_id.isnumeric():
                        sponsor_id = input("Invalid input. Enter SponsorID for product: ")
                    sponsor_id = int(sponsor_id)

                    # Get Price
                    price = input("Enter Price: ")
                    while not re.match(r'^\d+(\.\d{1,2})?$', price):
                        price = input("Invalid input. Enter Price: ")
                    price = float(price)

                    # Get Quantity
                    quantity = input("Enter Quantity: ")
                    while not quantity.isnumeric():
                        quantity = input("Invalid input. Enter Quantity: ")
                    quantity = int(quantity)
                    
                     # Construct SQL query and execute
                    sql_query = f"INSERT INTO PRODUCTS (ProductID, SponsorID, Price, Quantity) VALUES ('{product_id}', '{sponsor_id}', '{price}', '{quantity}')"
                        

                    # Execute query with user input as parameters
                    cursor.execute(sql_query)

                    # Print the executed SQL query
                    print("Executed SQL query: ", sql_query)

                    # Commit the changes to the database
                    db.commit()
     
            if option_choice == '2':
                sub_menu()
                table_choice = input("Enter table number: ")

                # Check if user entered a valid option
                if table_choice not in ['1', '2', '3', '4', '5', '6', '7']:
                    print("Invalid input. Please enter a valid option.")
                    continue
                
                # Modify data
                if table_choice == '1':
                    modify_data(db, "ADMINS")
                elif table_choice == '2':
                    modify_data(db, "SPONSORS")
                elif table_choice == '3':
                    modify_data(db, "DRIVERS")
                elif table_choice == '4':
                    modify_data(db, "POINTS")
                elif table_choice == '5':
                    modify_data(db, "ORDERS")
                elif table_choice == '6':
                    modify_data(db, "PRODUCTS")
                # Exit sub-menu
                else:
                    continue
                
                # Commit changes
                db.commit()
                    
            if option_choice == '3':
                sub_menu()
                table_choice = input("Enter table number: ")

                # Check if user entered a valid option
                if table_choice not in ['1', '2', '3', '4', '5', '6', '7']:
                    print("Invalid input. Please enter a valid option.")
                    continue

                if table_choice == '1':
                    delete_record("ADMINS")
                elif table_choice == '2':
                    delete_record("SPONSORS")
                elif table_choice == '3':
                    delete_record("DRIVERS")
                elif table_choice == '4':
                    delete_record("POINTS")
                elif table_choice == '5':
                    delete_record("ORDERS")
                elif table_choice == '6':
                    delete_record("PRODUCTS")
                # Exit sub-menu
                else:
                    continue
                
                # Commit changes
                db.commit()
                
            if option_choice == '4':
                view_all_records()
        
        db.commit()
        cursor.close()
        db.close()
        print("MySQL connection is closed")
    
except Error as e:
    print("Error while connecting to MySQL", e)