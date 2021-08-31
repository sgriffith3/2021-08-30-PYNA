
my_file_data = open("example.txt", "r")
data = my_file_data.read()

print(type(data))
print(data)

my_file_data.close()


with open("ex2.txt", "r") as second_file:
    #d2 = second_file.read()
    #print(d2)
    pass
    
print(second_file.readlines())
