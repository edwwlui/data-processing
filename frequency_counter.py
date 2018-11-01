from collections import Counter
import os

dataset_name = "ye/sentiment"
suffices = ['dev.0', 'dev.1','train.0', 'train.1']
dataset_path = "~/language_style_transfer/data/dataset/"
save_path="~/ed/smae/SMAE/dataset/"
save_name="vocab.txt"
word_list=[]
for suf in suffices:
    filename = dataset_name + suf
    with open(os.path.expanduser(dataset_path + dataset_name + "." + suf)) as f:
        for line in f:
            line = line.strip()
            if line:
                for word in line.split(" "):
                    word_list.append(word)

with open(os.path.expanduser(save_path + save_name ),"w") as fw:
    counts = Counter(word_list)
    for tuple in counts.most_common():
        fw.write(tuple[0]+" "+str(tuple[1])+"\n")


