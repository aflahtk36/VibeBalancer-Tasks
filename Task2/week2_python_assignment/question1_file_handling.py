file= open("data.txt","w")

file.write("This is a new file\n")
file.write("This is 2nd line\n")
file.write("This is 3rd line\n")
file.write("This is 4th line\n")
file.write("This is 5th line\n")

file.close()

file=open("data.txt","r")
print(file.read())
file.close()