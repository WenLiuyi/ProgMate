"""
# 识别png和jpg图片中的文字
Author: shq
Packages: os, easyocr
"""
import os, easyocr

# def all_specific_files(file_dir, kind):
#     """
#     # 获取文件夹下所有特定类型文件的路径
#     - kind: (str)文件拓展名
#     """
#     file_list=[]
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if file.endswith(kind): # 检验文件拓展名
#                 file_path = os.path.join(root, file)
#                 file_list.append(file_path)
#     return file_list

def all_pics(file_dir):
    """
    # 获取文件夹下所有png/jpg路径
    """
    pic_list=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'): # 检验文件拓展名
                file_path = os.path.join(root, file)
                pic_list.append(file_path)
    return pic_list

def text_clean(text_path):
    """
    # 清洗识别的文本
    
    """


def PicRecognition(file_dir):
    """
    # 识别png和jpg
    - file_dir: 文件夹路径
    """
    pics = all_pics(file_dir)
    # print(pics)
    for pic in pics:
        reader = easyocr.Reader(['en', 'ch_sim'],gpu=False)
        result = reader.readtext(pic)
        if not os.path.exists('./text/'):
            os.makedirs('./text/')
        with open('./text/'+os.path.basename(pic)+'_text.txt', 'w', encoding='utf-8') as file:
            for detection in result:
                # file.write(str(detection[1]) + '\n')
                file.write(str(detection[1]))
        print(os.path.basename(pic)+' has been recognized.')
    return 0

if __name__ == '__main__':
    file_dir = "./testfiles"
    PicRecognition(file_dir)

# #图片地址
# IMAGE_PATH = './testOCR.png' 
# #选择识别的语言，部分语言间冲突
# reader = easyocr.Reader(['en', 'ch_sim'],gpu=False)
# result = reader.readtext(IMAGE_PATH)
# with open('output easyocr.txt', 'w', encoding='utf-8') as file:
#     for detection in result:
#         file.write(str(detection[1]) + '\n')
