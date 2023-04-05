import hashlib

"""
password is the user's input whose hash will be checked
against the default password's hash, passw.
"""
password  = input("Emter your password: \n->")
passw = "password123"

"""
SHA1 takes a byte and returns a hash object.
bytes() takes a string and encoding string and returns bytes.
hexdigest() returns a hexi-decimal representation of the hash.
""" 
hash_pass = hashlib.sha1(bytes(password,"ascii"))
hex_pass = hash_pass.hexdigest()

print("Your hash",hex_pass)

hash_object = hashlib.sha1(bytes(passw,"ascii"))
hex_dig = hash_object.hexdigest()

# Fake_DB acts as a representation of a database (RDBMS)
Fake_DB = [hex_dig]

if hex_pass in Fake_DB:
    print("Logged in ..........")
else:   
    print("Sorry Wrong password")
print("Actual hash",hex_dig)
