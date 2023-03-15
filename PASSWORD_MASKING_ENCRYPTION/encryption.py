import hashlib
import maskpass #pip install maskpass


# prompts the user for a password in the terminal, shielding the characters with *
pwd = maskpass.askpass(prompt="enter a password: ", mask="*")

print(pwd)

# encrypts string to hexidecimal byte form which cannot be translated to the original
encrypt_pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()

print(encrypt_pwd)