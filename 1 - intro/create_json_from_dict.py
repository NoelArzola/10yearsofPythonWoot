import json

# Create a dictionary object
person_dict = {'first': 'Noel', 'last':'Arzola'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Boaz'

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json)
