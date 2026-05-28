usernames = ['satya narayana', 'venkat narayana',  'run narayana', 'walk narayana']

for index, name in enumerate(usernames):
    usernames[index] = name.replace(' ', '_')

print(usernames)