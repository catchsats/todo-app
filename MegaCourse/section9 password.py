password = input('Enter new password: ')

result = {}

for i in password:
    if len(password) >= 8:
        result['length'] = True
    if i.isdigit():
        result['digits'] = True
    if i.isalpha():
        result['Alpha'] = True
    if i.isalnum():
        result['special'] = True
    if i.isupper():
        result['upper'] = True
    if i.islower():
        result['lower'] = True

print(result)

if all(result):
    print('Strong Password')
else:
    print('Weak Password')