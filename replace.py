import re
#import string

#printable = set(string.printable)
files = ["form.dev.uniq.1"   ,"form.test.uniq.1"   ,"form.train.full.shuf.1", "form.dev.uniq.0"  ,"form.test.uniq.0"  ,"form.train.full.shuf.0"]
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
