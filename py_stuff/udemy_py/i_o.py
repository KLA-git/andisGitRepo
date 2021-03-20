myfile = open('test.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())


with open("../school/scripte/courses_out.csv") as myCSV:
    content = myCSV.read()
    print(content)
    myCSV.close()
