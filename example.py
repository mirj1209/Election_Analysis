# Create a variable called 'name' that holds a string
from tkinter.tix import INTEGER
from unicodedata import name


name = "george"
# Create a variable called 'country' that holds a string
country = "Uganda"

# Create a variable called 'age' that holds an integer
age = 99

# Create a variable called 'hourly_wage' that holds an integer
Hourly_wage = 10.75

# Calculate the daily wage for the user
daily_wage = Hourly_wage*8

# Create a variable called 'satisfied' that holds a boolean
satisfied = False

# Print out "Hello <name>!"
print("hello" + str(name))

# Print out what country the user entered
print(f"{country}")

# Print out the user's age
print(age)

# With an f-string, print out the daily wage that was calculated
print(f"The daily wage is {daily_wage}")

# With an f-string, print out whether the users were satisfied
print(f"Is the user satisfied{satisfied}")
