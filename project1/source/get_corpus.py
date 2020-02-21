import jieba, re
import pandas as pd
import os

filename = '/home/kuan/Desktop/NLP/project1/sqlResult_1558435.csv'
data = pd.read_csv(filename, encoding='gb18030')
articles = list(data.content)

with open('/home/kuan/Desktop/NLP/project1/data','w+',encoding='utf-8') as file:
    for a in articles:
        article = ''.join(aa for aa in re.findall('\w+', str(a)))
        words = jieba.cut(article, cut_all=False)
        article_contents = ""
        for word in words:
            article_contents += word + " "
        file.write(article_contents + "\n")
        
        

input_names = ['zh_wiki_parsed_00', 'zh_wiki_parsed_01', 'data']
output_name = 'data_result'
dir = '/home/kuan/Desktop/NLP/project1'

output = open(os.path.join(dir, output_name), 'w', encoding='utf-8')
for input_name in input_names:
    input = open(os.path.join(dir, input_name))
    line = input.readline()
    while line:
        output.write(line)
        line = input.readline()
    input.close()
output.close()
