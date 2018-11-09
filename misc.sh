src/deep/dataloader/util.py
src/deep/dataloader/corpus_reader_dialog_topic.py
/home/fyp1/ed/if_data/1short/src/deep/manage/manager.py 469
/home/fyp1/ed/if_data/1replace/src/deep/manage/manager.py 469

batch 64

src/tool/find_nearst_neighbot_all.py  //sentiment

~/ed/1/src/deep/dataloader/util.py

~/ed/1/src/tool/find_nearst_neighbot_all.py

File "/home/fyp1/ed/if_data/3yelp/src/deep/manage/algorithm.py", line 186, in beam_search_t

atof

export THEANO_FLAGS=device=cuda1,floatX=float32
nohup bash run.sh test DeleteAndRetrieve yelp > test.stdout.txt 2>test.stderr.txt &

CUDA_VISIBLE_DEVICES=0 python3 main.py \
--train_data_path dataset/train/* \
--valid_data_path dataset/valid/* \

TypeError: ('Bad input argument to theano function with name "deploy_function" at index 6 (0-based).  
\nBacktrace when that variable is created:\n\n  File "src/main.py", line 65, in <module>\n    
train_rate, valid_rate, test_rate, algo_name, charset, mode, batch_size)\n  
File "/home/fyp1/ed/if_data/3yelp_atof/src/deep/manage/model/cho_encoder_decoder_DT.py", line 67, in __init__\n    
input_params=param_dict)\n  File "/home/fyp1/ed/if_data/3yelp_atof/src/deep/algorithms/networks/cho_encoder_decoder_DT.py", line 74, in __init__\n
    self.topic = tensor.matrix(\'topic\', dtype=config.globalFloatType())\n'
	, 'TensorType(float32, matrix) cannot store accurately value [[0.5828757978222049]], it would be represented as [[0.5828758]]. 
	If you do not mind this precision loss, you can: 1) explicitly convert your data to a numpy array of dtype float32, or 2) set "allow_input_downcast=True" when calling "function".', [[0.5828757978222049]])


(py27) fyp1@kao-server1:~/ed/if_data/6yelp_theano$ nohup bash run.sh train DeleteAndRetrieve yelp > train.stdout.txt 2>train.stderr.txt &
[1] 211994


(smae) fyp1@kao-server1:~/ed/smae/1$ CUDA_VISIBLE_DEVICES=1
(smae) fyp1@kao-server1:~/ed/smae/1$ nohup python3 main.py > test.stdout.txt 2>test.stderr.txt &
[1] 211798


(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.data.orgin
  2101  48817 252172 sentiment.test.1.data.orgin
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.0.data.orgin
  2748  60777 299107 sentiment.test.0.data.orgin
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.template.orgin
  2101  48817 252172 sentiment.test.1.template.orgin
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.template.orgin.emb
    2101  1124529 13126920 sentiment.test.1.template.orgin.emb
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.template.orgin.emb.result
  21010  976309 5280435 sentiment.test.1.template.orgin.emb.result
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.template.orgin.emb.result.filter
  21010  736000 4016163 sentiment.test.1.template.orgin.emb.result.filter
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.template.orgin.emb.result.filter.result
   3792  182849 1026724 sentiment.test.1.template.orgin.emb.result.filter.result
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.template.orgin.emb.result.filter.result.result
   3792  186641 1062318 sentiment.test.1.template.orgin.emb.result.filter.result.result
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.template.orgin.emb.result.filter.result.result.final_result
  380  8236 41484 sentiment.test.1.template.orgin.emb.result.filter.result.result.final_result
(py27) fyp1@kao-server1:~/ed/if_data/12j_10000_5_ignore_rc$ wc sentiment.test.1.DeleteAndRetrieve.yelp
  380  8236 41484 sentiment.test.1.DeleteAndRetrieve.yelp

integral error
run.sh download in lab
