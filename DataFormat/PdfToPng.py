"""
# pdf转换png
Author: shq
packages: os, PyMuPDF, fitz, xpinyin, re

"""
import fitz, os, re
from xpinyin import Pinyin

def pdf_to_png(pdfPath, pngPath, zoom_x=5, zoom_y=5, rotation_angle=0):
    """
    # 将PDF转化为图片
    - pdfPath         pdf文件的路径
    - pngPath         图像要保存的文件夹/前缀
    - zoom_x          x方向的缩放系数
    - zoom_y          y方向的缩放系数
    - rotation_angle  旋转角度
    """
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    #if pdf.page_count:
       
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.save(pngPath + str(pg) + ".png")
    pdf.close()

def mkdir(path):
    """
    # 创建path文件夹
    """
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass

def all_pdfs(file_dir):
    """
    # 获取文件夹下所有PDF路径
    """
    pdf_list=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.endswith('.pdf'):   # 检验文件拓展名
                file_path = os.path.join(root, file)
                pdf_list.append(file_path)
    return pdf_list

def is_Chinese(text):
    """
    # 是否包含中文
    """
    chinese_pattern = re.compile('[\u4e00-\u9fa5]')
    return bool(chinese_pattern.match(text))

def pdf_to_png_all(pdfDir, zoom_x=5, zoom_y=5, rotation_angle=0):
    """
    # 将所有pdfDir文件夹下的pdf转化为png, 并保存在当前文件夹下

    """
    pdfs=all_pdfs(pdfDir)
    for pdf in pdfs:
        pdf_name = os.path.basename(pdf)
        if is_Chinese(pdf_name): # 转化为拼音
            p = Pinyin()
            pdf_name = p.get_pinyin(pdf_name)
        pdf_to_png(pdf, pdfDir+'/'+pdf_name[:-4])
        print(pdf_name+' has been converted to png.')
    return 0

if __name__ == "__main__":
    pdf_dir = "D:\\Project\\CuteShq\\ProgMate\\DataFormat\\testfiles"
    pdf_to_png_all(pdf_dir)
