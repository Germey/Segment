from snownlp import SnowNLP

string = '这个把手该换了，我不喜欢日本和服，别把手放在我的肩膀上，工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'

s = SnowNLP(string)
result = s.words
print(len(result), '/'.join(result))

print('Tags:', list(s.tags))
print('Sentiments:', s.sentiments)
print('Pinyin:', s.pinyin)



print('Keywords:', s.keywords(2))
print('Summary:', s.summary(2))
print('TF:', s.tf)
print('IDF:', s.idf)