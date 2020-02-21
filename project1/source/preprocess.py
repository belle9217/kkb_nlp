import re
import jieba
import os

def get_stopwords():
    stop_word = set()
    with open('/home/kuan/Desktop/NLP/project1/zh_stopwords') as f:
        for word in f:
            stop_word.add(word.strip('\n'))
    return stop_word

#提取<doc>和</doc>之间的内容，并进行分词操作
def parse_wiki(input_file_name, output_file_name):
    reg = '[^<doc.*>$]|[^</doc>$]'
    file = open(input_file_name, 'r', encoding='utf-8')
    output = open(output_file_name, 'w+', encoding='utf-8')
    content_line = file.readline()
    article_contents = ""
    stop_words = get_stopwords()
    count = 0

    while content_line:
        match_obj = re.match(reg, content_line)
        content_line = content_line.strip('\n')
        content_line = rplc(content_line)
        if len(content_line) > 0:
            if match_obj:
                words = jieba.cut(content_line, cut_all=False)
                for word in words:
                    if word not in stop_words:
                        article_contents += word + " "
            else:
                if len(article_contents) > 0:
                    count += 1
                    print("Writing {} article into file {}".format(count, output_file_name))
                    output.write(article_contents + '\n')
                    article_contents = ""
        content_line = file.readline()
    output.close()
    file.close()

#去除特殊符号
def rplc(line):
    line = line.replace('(','')
    line = line.replace(')','')
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.replace('《','')
    line = line.replace('》','')
    line = line.replace('「','')
    line = line.replace('」','')
    line = line.replace('『','')
    line = line.replace('』','')
    line = line.replace('（','')
    line = line.replace('）','')
    return line

def main():
    dir = '/home/kuan/Desktop/NLP/project1/'
    file1 = os.path.join(dir, 'zh_wiki_00')
    file2 = os.path.join(dir, 'zh_wiki_01')
    out1 = os.path.join(dir, 'zh_wiki_parsed_00')
    out2 = os.path.join(dir, 'zh_wiki_parsed_01')
    parse_wiki(file1, out1)
    parse_wiki(file2, out2)

if __name__ == '__main__':
    main()
