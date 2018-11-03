import os

dataset_name = "ye/sentiment"
suffices = ['dev.0', 'dev.1','train.0', 'train.1']
dataset_path = "~/language_style_transfer/data/dataset/"
save_path="~/ed/smae/SMAE/dataset/train/"
save_name="sentiment"
for suf in suffices:
    filename = dataset_name + suf
    with open(os.path.expanduser(dataset_path + dataset_name + "." + suf)) as f:
        for line in f:
            line = line.strip()
            if line:
                with open(os.path.expanduser(save_path + save_name + "." + suf + ".json"), 'a') as fw:
                    string_to_write = ""
                    string_to_write += '{"review": "' + line
                    if (suf[-1] == "1"):  # negative->0 score
                        string_to_write += '", "score": "5"'
                    elif (suf[-1] == "0"):  # negative->0 score
                        string_to_write += '", "score": "1"'
                    fw.write(string_to_write+', "weight": "0.5", "reward": "1"}'+"\n")
