import re

email = input("What is your email? ").strip()

# if re.search(r"^[^@]+@[^@]+\.edu$", email): # solution ".+@.+" alt "..*@..*"
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # instead of lower()
    print("Valid")
else:
    print("Invalid")

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# # if username and "." in domain:
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")