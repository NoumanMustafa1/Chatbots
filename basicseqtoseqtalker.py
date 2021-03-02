data=[]
robot_data=[]
human_data=[]

with open("robot_text.txt",'rb') as f:
    data=f.read()
robot_data=repr(data).encode("utf-8")
print(robot_data)
#human_text.txt
max_sentence_len=50
from keras.preprocessing.text import Tokenizer
t=Tokenizer(num_words=max_sentence_len, filters='0123456789!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\n', char_level=False, oov_token=True)

t.fit_on_texts(robot_data)
robot_wordtoindex=t.word_index
print(robot_wordtoindex)
