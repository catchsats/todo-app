filenames = ['1.doc', '1.report', '1.presentation']

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)


temp = [10,12, 14]
file = open('file.txt', 'w')
temp = [str(i) + '\n' for i in temp]
file.writelines(temp)