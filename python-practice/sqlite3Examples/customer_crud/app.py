import repository

# Add customer to Customers table
# repository.add_customer("fname99", "lname99", "email99@gmail.com")

# Delete customer from Customers table
# repository.delete_customer('5')

# Add customers to Customers table
# customerList = [
#     ('fname98', 'lname98', 'name98@gmail.com'),
#     ('fname99', 'lname99', 'name99@gmail.com')    
# ]
# repository.add_customers(customerList)

# Email LookUp
repository.email_lookup('name98@gmail.com')

# Show all the customers
# repository.get_customer_all()
