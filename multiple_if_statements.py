country = input('What country do you live in? ')
tax = 0

# if province == 'Alberta':
#     tax = 0.05
# if province == 'Nunavut':
#     tax = 0.05
# if province == 'Ontario':
#     tax = 0.13
# print(tax)

# if province == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

# if province == 'Alberta' or province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

if country.lower == 'Canada':    
    province = input('What province/state do you live in? ')
    if province.lower in('Alberta', 'Nunavit', 'Yukon'):
        tax = 0.05
    elif province.lower == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)