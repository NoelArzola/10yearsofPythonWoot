price = input('How much did you pay? ')

if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)

country = 'CANADA'
if country.lower == 'canada': #this will convert the country to all lowercase regardless of how it's entered
    print('Oh look a Canadian')
else:
    print('You are not from Canada')    