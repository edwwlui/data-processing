import re
#import string

#printable = set(string.printable)
files = ["sentiment.dev.0", "sentiment.dev.1", "sentiment.test.0", "sentiment.test.1", "sentiment.train.0",
         "sentiment.train.1"]
for file in files:
    with open(file, "r") as fi:
        for line in fi:
            line = line.replace("´", "")
            line = line.replace("é", "e")
            line = line.replace("…", "dotdotdot")
            line = line.replace("\u200b", "u200b")
            line = line.replace("¢", "c")
            line = line.replace("™", "TM")
            line = line.replace("©", "c")
            line = line.replace("Ü", "U")
            line = line.replace("ö", "o")
            line = line.replace("?", "r")
            line = line.replace("ü", "u")
            line = line.replace("¿", "?")
            line = line.replace("ó", "o")
            line = line.replace("®", "R")
            line = line.replace("?", "a")
            line = line.replace("?", "e")
            line = line.replace("è", "e")
            line = re.sub(r'[^\x00-\x7f]', r'', line)
            #line = filter(lambda x: x in printable, line)
            with open("../" + file, "a") as fo:
                fo.write(line)
