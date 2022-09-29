import os
for filename in os.listdir("./"):
    type = os.path.splitext(filename)[1]
    if (type == '.lrc'):
        name = os.path.splitext(filename)[0]
        os.rename(filename, name+'.'+'txt')