import numpy as np
from sklearn.decomposition import PCA
from get_word_freqency import *


#定义Word类和Sentence类
class Word:
    def __init__(self, text, vector):
        self.text = text
        self.vector = vector

    def __str__(self):
        return self.text + ' : ' + str(self.vector)


class Sentence:
    def __init__(self, word_list):
        self.word_list = word_list

    def len(self):
        return len(self.word_list)

    def __str__(self):
        word_list_str = [word.text for word in self.word_list]
        return ''.join(word_list_str)


#利用SIF生成句子向量
def sentence2vec(sentence, embedding_size, a):
    sentence_vector = np.zeros(embedding_size)
    sentence_length = sentence.len()
    for word in sentence.word_list:
        aa = a / (a + get_word_frequency(word.text))
        sentence_vector = np.add(sentence_vector, np.multiply(aa, word.vector))
    sentence_vector = np.divide(sentence_vector, sentence_length)
        
    pca = PCA()
    pca.fit([sentence_vector])
    u = pca.components_[0]
    
    uuTv = np.multiply(np.multiply(u, u.T), sentence_vector)
    sv = np.subtract(sentence_vector, uuTv)
    return sv
