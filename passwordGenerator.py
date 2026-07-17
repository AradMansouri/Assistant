from password_generator import PasswordGenerator

pwo = PasswordGenerator()
pwo.minlen = 8
pwo.maxlen = 30

def generate_password(length):
    return pwo.non_duplicate_password(length)
    
