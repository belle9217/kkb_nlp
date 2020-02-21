import numpy as np
from gen_vector import *

#计算向量之间的余弦相似度
def cos_sim(v1, v2):
    cos = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return 0.5 * cos + 0.5 


def knn_smooth(sv, n_neighbors):
    sv_smooth = []
    if n_neighbors * 2 + 1 > len(sv):
        return sv
    for (i, v) in enumerate(sv):
        if i < n_neighbors:
            sv_smooth.append(np.mean(sv[:n_neighbors + i + 1],axis=0))
        elif i + n_neighbors > len(sv):
            sv_smooth.append(np.mean(sv[i - n_neighbors:],axis=0))
        else:
            sv_smooth.append(np.mean(sv[i - n_neighbors:i + n_neighbors + 1], axis=0))
    return sv_smooth
    
    
#输入：title向量，sentence向量，content向量，alpha权重, n_neighbor每侧的邻居个数
#输出：0~1的值列表，表示每个句子向量与content以及title的相似程度。
def correlation(title, sentence, content, alpha, n_neighbors=2):
    #参数alpha表示title与句子相似度的贡献程度，1-alpha表示content与句子相似度的贡献程度
    results = []
    sentence_smooth = knn_smooth(sentence, n_neighbors=2)
    for s in sentence_smooth:
        corr = alpha * cos_sim(s, title) + (1 - alpha) * cos_sim(s, content)
        results.append(corr)
    return results


#对句子相似度进行排序，取出 Top_n，得到语义上最相近的n个句子。
def top_n(sim_list, n):
    if n >= len(sim_list):
        return list(len(sim_list))
    else:
        return np.argsort(-np.array(sim_list))[:n]
        

def gen_text(title, article, n_top=2):
    title_sv, sv, article_sv, original_sentences = gen_vector(title, article)
    sim_list = correlation(title_sv, sv, article_sv, alpha=0.2)
    n_list = top_n(sim_list, n_top)
    output = ''
    for i in sorted(n_list):
        output += original_sentences[i]
    if output[-1] not in r'，|。|！|？':
        output = output[:-1] + '。'
    return output
