from gensim.models import word2vec
import multiprocessing
filename = '/home/kuan/Desktop/NLP/project1/data_result'

sentences = word2vec.LineSentence(filename)
model = word2vec.Word2Vec(sentences, size=300, workers=multiprocessing.cpu_count())

model.save("/home/kuan/Desktop/NLP/project1/wiki.model")
