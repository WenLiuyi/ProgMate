import torch
from ltp import LTP
import os
import insert

# 默认 huggingface 下载，可能需要代理

#ltp = LTP("LTP/small")  # 默认加载 Small 模型
                        # 也可以传入模型的路径，ltp = LTP("/path/to/your/model")
                        # /path/to/your/model 应当存在 config.json 和其他模型文件

def generateObject(line,ltp_path,cur):
    ltp=LTP(ltp_path)
    # 将模型移动到 GPU 上
    if torch.cuda.is_available():
        # ltp.cuda()
        ltp.to("cuda")

    cws, pos, ner = ltp.pipeline([line], tasks=["cws", "pos", "ner"]).to_tuple()
    insert.insertTable(cws[0],pos[0],cur)

def all_texts(file_dir):
    text_list=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.endswith('.txt'):   # 检验文件拓展名
                file_path = os.path.join(file_dir, file)
                #print(file_path)
                text_list.append(file_path)
    return text_list

def read_text_all(text_dir,cur):
    texts=all_texts(text_dir)
    for text in texts:
        file=open(text,"r")
        print(text)
        file=file.readlines()
        for line in file:
            generateObject(line,"../base",cur)


'''
ltp=LTP("../base")
# 将模型移动到 GPU 上
if torch.cuda.is_available():
    # ltp.cuda()
    ltp.to("cuda")

# 法1: 自定义词表
##ltp.add_word("汤姆", freq=2)
##ltp.add_words(["外套", "外衣"], freq=2)
#ltp.add_words(["最", "短","距离"], freq=1)

#  分词 cws、词性 pos、命名实体标注 ner、语义角色标注 srl、依存句法分析 dep、语义依存分析树 sdp、语义依存分析图 sdpg
output = ltp.pipeline(["How are you?"], tasks=["cws", "pos", "ner", "srl", "dep", "sdp", "sdpg"])
# 使用字典格式作为返回结果
print(output.cws)  # print(output[0]) / print(output['cws']) # 也可以使用下标访问
print(output.pos)
print(output.sdp)

# 法2: 使用感知机算法实现的分词、词性和命名实体识别，速度比较快，但是精度略低
ltp = LTP("../legacy")
# cws, pos, ner = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks=["cws", "ner"]).to_tuple() # error: NER 需要 词性标注任务的结果
cws, pos, ner = ltp.pipeline(["单分支"], tasks=["cws", "pos", "ner"]).to_tuple()  # to tuple 可以自动转换为元组格式
# 使用元组格式作为返回结果
print(cws, pos, ner)
'''