file1 = open(r'C:\Users\User\Desktop\Codingal\Specialization in python\codingal.txt','r')
file2 = open(r'C:\Users\User\Desktop\Codingal\Specialization in python\Codingal updated.txt' , 'w')

for line in file1.readlines():
    #Reading only those lines that do not begin with "I"
    if not (line.startswith('I')):

        print(line)

        file2.write(line)

file2.close()
file1.close()        