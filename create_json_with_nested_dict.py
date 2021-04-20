import json

# Create a dictionary object
person_dict = {'first': 'Noel', 'last':'Arzola'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Boaz'

# create a staff dictionary
# assign a person to a staff position of program manager
staff_dict ={}
staff_dict['Full-Stack Developer']=person_dict
# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)