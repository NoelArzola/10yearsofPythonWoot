import json

# Create a dictionary object
person_dict = {'first': 'Noel', 'last':'Arzola'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Boaz'

# Create a list object of programming languages 
languages_list = ['Python','JavaScript']

# Add list object to dictionary for the languages key
person_dict['languages']= languages_list

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json)