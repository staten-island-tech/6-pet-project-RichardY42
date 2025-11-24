
# Word Problem: The School Portal Login System
# Your school is creating a new online portal for students to sign up for accounts. The login system needs a function that accepts two pieces of information from the user:
# Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.


def isvalid(email, paswor):
    if not isinstance(email,str) or not isinstance(paswor,str):
        return "the email and password is not valid, must be string"
    if "@" not in email:
        return "Not valid email, nust have @ symbol"
    if len(paswor)<8:
        return "your password must be at least eight characters long"
    if not any(i.isdigit() for i in paswor):
        return "your password must have a number"
    if not any(i.isupper() for i in paswor):
        return "your password must have a uppercase letter"


    
    return {"email":email, "password":paswor}
print(isvalid("test123@gamer.com","F2d8layf"))