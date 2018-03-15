import jieba

string = '这个把手该换了，我不喜欢日本和服，别把手放在我的肩膀上，工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'
result = jieba.lcut(string)
print(len(result), '/'.join(result))

result = jieba.lcut(string, cut_all=True)
print(len(result), '/'.join(result))

result = jieba.lcut_for_search(string)
print(len(result), '/'.join(result))

jieba.add_word('日本和服')
result = jieba.lcut(string)
print(len(result), '/'.join(result))

import jieba.posseg as pseg

words = pseg.lcut(string)
print(list(map(lambda x: list(x), words)))