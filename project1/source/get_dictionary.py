import gensim
import json
model = gensim.models.Word2Vec.load('/home/kuan/Desktop/NLP/project1/wiki.model')

def get_dictionary():
    d_path = '/home/kuan/Desktop/NLP/project1/data_result'
    word_count = {}
    total = 0
    count = 1
    with open(d_path, 'r') as f:
        line = f.readline()
        while line:
            print('Processing line {}'.format(count))
            words = line.split(' ')
            for word in words:
                total += 1
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
            line = f.readline()
            count += 1
    for word in word_count:
        word_count[word] /= total
    return word_count

dictionary = get_dictionary()

with open('dictionary.json', 'w+') as f:
    json.dump(dictionary, f, ensure_ascii=False)
    f.write('\n')
