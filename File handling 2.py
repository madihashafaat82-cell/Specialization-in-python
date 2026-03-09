file_read = open(r'C:\Users\User\Downloads\Codingal.txt','r')
print('File in read mode')
print(file_read.read)
file_read.close

file_write = open(r'C:\Users\User\Downloads\Codingal.txt','w')
file_write.write('File in Writing mode')
file_write.write('Hello')
file_write.close

file_append = open(r'C:\Users\User\Downloads\Codingal txt','a')
file_append.write('/n File in Append mode....')
file_append.write('My name is Rayyan')
file_append.close


