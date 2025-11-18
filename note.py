def isvalid(email, paswor):
    if "@" not in email:
        return "Not valid email"
    #print("test")
    if not isinstance(email,str):
        return "the email is not valid"
    return {"email":email, "password":paswor}
print(isvalid("test123@gamer.com",1))