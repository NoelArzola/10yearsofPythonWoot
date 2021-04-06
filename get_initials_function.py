# This function will return the first initial of a name
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Ask someones name and return the initials
first_name = input('What is your first name? ')
first_name_initial = get_initial(first_name)

middle_name = input('What is your middle name? ')
middle_name_initial = get_initial(middle_name, False)
 
last_name = input('What is your last name? ')
last_name_initial = get_initial(last_name, False)

print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)