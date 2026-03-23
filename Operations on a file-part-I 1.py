file_r = open(r'C:\Users\User\Desktop\Codingal\Specialization in python\Rayyan.txt','r')
print('File in reading mode')
file_r.close()


file_w = open(r'C:\Users\User\Desktop\Codingal\Specialization in python\Rayyan.txt','w')
file_w.write('filein Wrting mode')
file_w.write("I am Rayyan")
file_w.close()

file_a = open(r'C:\Users\User\Desktop\Codingal\Specialization in python\Rayyan.txt','a')
file_a.write("I am the student of the Codingal")
file_a.close()