import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            fname text,
            lname text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:fname, :lname, :pay)", {'fname': emp.fname, 'lname': emp.lname, 'pay': emp.pay})

def get_emps_by_name(lnamename):
    c.execute("SELECT * FROM employees WHERE lname=:lname", {'lname': lnamename})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE fname = :fname AND lname = :lname""",
                  {'fname': emp.fname, 'lname': emp.lname, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE fname = :fname AND lname = :lname",
                  {'fname': emp.fname, 'lname': emp.lname})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()