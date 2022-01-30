my_file = open(r"data.txt", "w")

# for line in my_file.readlines():
#     print(line.replace('\n', ''))

# for data in my_file.read(1024):
#     print(data)

if my_file.writable():
    my_file.write("Update\n")

    strings = ["John\n", "Kate\n"]
    my_file.writelines(strings)
else:
    print("Can not write")

my_file.close()
