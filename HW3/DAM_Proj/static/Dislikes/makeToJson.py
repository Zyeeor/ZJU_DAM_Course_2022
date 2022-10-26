import os
for filename in os.listdir("./"):
    #print(file)
    type = os.path.splitext(filename)[1]
    if type == '.txt':
        name = os.path.splitext(filename)[0]
        file = open(filename)
        text = file.readlines()
        file.close()
        file = open(name+".json", 'w')
        file.write("{\n")
        file.write('\t\"name\": \"' + name + "\",\n")
        file.write('\t\"lyrics\":\"')
        for i in text:
            for j in i:
                if j != '\n':
                    file.write(j)
            file.write("\\n")
        file.write("\"\n}")
        file.close()
        
