import bcrypt

password = 'MyPassWord'

bytePwd = password.encode('utf-8')
# Generate salt
# Generate a separate salt for each for better security
mySalt = bcrypt.gensalt()

# Hash password
hashedPassword = bcrypt.hashpw(bytePwd, mySalt)
print(hashedPassword)
