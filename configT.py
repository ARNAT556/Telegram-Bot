import random

def pass_gen(len):
    password = ''
    elements = '!@#$%^&*()_+1234567890qwertyuiop'
    for i in range(len):
        password += random.choice(elements)
    return password


print(pass_gen(10))
