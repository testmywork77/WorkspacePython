# positional, keyword, *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date = "September 2010")