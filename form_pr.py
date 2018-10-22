
from collections import OrderedDict
import nltk
import os
#from noun_annot import annot_noun

def annot_noun(sent):
    def is_noun(pos): return pos[:2] == 'NN' or pos[:3] == 'PRP'

    words = sent.split()
    tok_n_pos = [word + u"￨NN" if is_noun(pos) else word + u"￨na"
                 for (word, pos) in nltk.pos_tag(words)]
    return ' '.join(tok_n_pos)

data = OrderedDict()
data['meta'] = {}
data['meta']['sentence_to_index'] = OrderedDict()
data['meta']['list_index']=[]
sents = []
dataset_name = "fi/form"
suffices = ['train.0', 'train.1',
            'dev.0', 'dev.1',
            'test.0', 'test.1']
dataset_path="~/language_style_transfer/data/dataset/"
for suf in suffices:
    filename = dataset_name + suf
    data['meta'][suf]=[]
    with open(os.path.expanduser(dataset_path+dataset_name +"."+ suf)) as f:
        for line in f:
            line = line.strip()
            if line:
                # get sent_ix
                s_i = len(data['meta']['list_index'])
                s_i = str(s_i)

                # get meta
                data['meta']['list_index'] += [s_i]
                data['meta'][suf] += [s_i]

                #get sentence_to_index
                index_sent_dict={s_i: line}
                data['meta']['sentence_to_index'].update(OrderedDict(index_sent_dict))

                # get src sent
                src = nltk.word_tokenize(line)
                src = ' '.join(src)
                src_noun = annot_noun(src)
                data[s_i] = {
                    'src': src,
                    'noun': src_noun,
                    'mt_grp': suf.split('.')[0],
                    'class': suf.split('.')[1]
                }
                

#assert (len(data) - 1) == total_num_of_lines_in_all_files
#assert (len(['meta'][suf])) == total_num_of_lines_in_[suf]
#assert: a random sentence in data, check whether it's in the correct 'mt_grp'

import torch

path = "~/language_style_transfer/data/dataset/fi/form.index.torch"
torch.save(data, os.path.expanduser(path))

"""
%testing

print("len(data)-1: "+str(len(data)-1))

for suf in suffices:
    print("len(data['meta']"+suf+": "+str(len(data['meta'][suf])))

%104564 in train.1

print(data['meta']['sentence_to_index']['104564'])
print(data['104564'])

%is train.1
"""
