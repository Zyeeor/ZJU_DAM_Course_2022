import os
for filename in os.listdir("./"):
    type = os.path.splitext(filename)[1]
    if type != '.txt':
        continue
    file = open(filename)
    text = file.readlines()
    count = 0
    for i in text:
        if 'ar:' in i:
            count = count + 1
            print(i)
    print("number: ", count)