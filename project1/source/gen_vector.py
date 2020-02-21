import re
import jieba
import gensim
from sentence2vector import *

#去除句子中的冗余信息
def clean_sentence(line):
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('《', '')
    line = line.replace('》', '')
    line = line.replace('「', '')
    line = line.replace('」', '')
    line = line.replace('『', '')
    line = line.replace('』', '')
    line = line.replace('（', '')
    line = line.replace('）', '')
    line = line.replace('【', '')
    line = line.replace('】', '')
    line = line.replace('、','')
    line = line.replace('……', '')
    line = line.replace('“', '')
    line = line.replace('”', '')
    line = line.replace('‘', '')
    line = line.replace('’', '')
    line = line.replace('\'', '')
    line = line.replace('\'', '')
    return line

#根据标题和文章内容，生成标题向量，句子向量列表，和文章内容向量
#input: title->str, article->str
#output: title_sv->vector, sv_list->list of vector, airticle_sv->vector, origin_sentences->str
def gen_vector(title, article):
    model = gensim.models.Word2Vec.load('/home/kuan/Desktop/NLP/project1/wiki.model')
    #按照以下标点符号分割句子
    reg_str = r'，|。|！|？'
    sentences = re.split(reg_str, article)
    symbols = re.findall(reg_str, article)
    original_sentences = [s1 + s2 for s1, s2 in zip(sentences, symbols)]
    clean_sentences = [clean_sentence(s) for s in sentences if s != '']
    article_word_list = []
    sv_list = []
    for sentence in clean_sentences:
        word_list = []
        s_cut = list(jieba.cut(sentence))
        for word in s_cut:
            word_list.append(Word(word, model.wv[word]))
            article_word_list.append(Word(word, model.wv[word]))
        sv_list.append(sentence2vec(Sentence(word_list), embedding_size=300, a=0.001))
    article_sv = sentence2vec(Sentence(article_word_list), embedding_size=300, a=0.001)

    clean_title = ''.join(re.split(reg_str, clean_sentence(title)))
    title_cut = list(jieba.cut(clean_title))
    word_list = []
    title_list = []
    for word in title_cut:
        word_list.append(Word(word, model.wv[word]))
    title_sv = sentence2vec(Sentence(word_list), embedding_size=300, a=0.001)
    return title_sv, sv_list, article_sv, original_sentences
