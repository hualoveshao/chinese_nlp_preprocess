'''
  format_str：保留汉字、数字和字母，繁体字转简体字
  seg_sentence：jieba分词去除停用词
'''

from langconv import *
import jieba

####################繁体转简体
def TraditionalToSimplified(line):          
    line=Converter("zh-hans").convert(line)
    return line

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
 """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

#保留中文，数字和字母字符
def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i)or is_number(i) or is_alphabet(i):
            content_str = content_str+i
    content_str = TraditionalToSimplified(content_str)
    return content_str

############################分词去除停用词
import jieba  
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  
  
'''
  jieba分词去除通用词
'''
def seg_sentence(sentence):  
    sentence_seged = jieba.cut(sentence.strip())  
    stopwords = stopwordslist('./stop_words.txt')  # 这里加载停用词的路径  
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:  
            if word != '\t':  
                outstr += word  
                outstr += " "  
    return outstr  
	
def save_to_disk(path_to_disk, obj, overwrite=False):
    pickle.dump(obj, open(path_to_disk, 'wb'))


def load_from_disk(path_to_disk):   
    return pickle.load(open(path_to_disk, 'rb'))

#############################################
