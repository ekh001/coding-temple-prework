#Question 1: Write a function to print "hello_USERNAME!"".
def hello_name(user_name):
    """Print a greeting to the proper username in all caps."""
    for name in user_name:
        msg = "hello_" + name.upper() + "!"
        print(msg)

usernames = ['namjoon', 'hoseok', 'yoongi']
hello_name(usernames)

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    """Print odd numbers 1-100 and return nothing."""
    current_number = 0
    while current_number <= 99:
        current_number += 1
        if current_number % 2 == 1:
            print(current_number)
current_number = 0
first_odds()

#Question 3: Return the max number of a given list. 
def max_num_in_list(a_list):
    """Return the maximum number in a given list."""
    a_list.sort()
    print(f"The maximum value in my wonderful list is: {a_list[-1]}")

a_list = [4, 3, 7, 1, 9, 62, 2, 283942, 29]
max_num_in_list(a_list) 


#Question 4: Write a function to return if the given year is a leap year. The comments on this assignment make this question slightly terrifying.
#Version_One: Non-Boolean

# def is_leap_year(a_year):
#     if (a_year % 100 == 0) and (a_year % 400 == 0):
#         print("True.")
#     elif (a_year % 100 != 0) and (a_year % 4 == 0):
#         print("True.")
#     else:
#         print("False.")

# is_leap_year(1990)

#Verson_Two: Boolean! Hopefully. Oh please.
def is_leap_year(a_year):
    """Show if a given year is a leap year."""
    if (a_year % 100 == 0) and (a_year % 400 == 0):
        return True
    elif (a_year % 100 != 0) and (a_year % 4 == 0):
        return True
    else:
        return False
print(is_leap_year(2023))

#Question 5: Return the max number of a given list. 
def is_consecutive(a_list):
    """Check to see if all numbers in a list are consecutive numbers."""
    while True:
        return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
    
a_list = [8, 7, 6, 10]
print(is_consecutive(a_list))
