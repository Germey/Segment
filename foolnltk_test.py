import fool

string = '这个把手该换了，我不喜欢日本和服，别把手放在我的肩膀上，工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'

result = fool.cut(string)
print(result)

result = fool.pos_cut(string)
print(result)
_, ners = fool.analysis(string)
print(ners)
