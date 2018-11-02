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


(py27) fyp1@kao-server1:~/ed/if_data/4yelp_numpy_test$  nohup bash run.sh test DeleteAndRetrieve yelp > test.stdout.txt 2>test.stderr.txt &
[1] 205016
