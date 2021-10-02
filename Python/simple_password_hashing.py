
# procedure is - first take password and store its hash(hashedPassword)
# now user on login give userPassword - check if this password matches with the hashedPassword

def encrypt(password): 
    hashed = 0
    for digit in password: 
        hashed ^= int(digit)
    
    return hashed

def decrypt(hashedPassword, userPassword):
    for digit in userPassword: 
        hashedPassword ^= int(digit)
    
    if(hashedPassword == 0):
        return 1
    return 0



password = input("give pin: ")

hashedPassword = encrypt(password)

print(f"the hash generated is {hashedPassword}")

userPassword = input("give password to check if valid: ")

if(decrypt(hashedPassword, userPassword)):
    print("Yes! password matched")
else: 
    print("Opps! the password is incorrect")

