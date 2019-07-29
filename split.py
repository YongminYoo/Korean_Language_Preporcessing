from konlpy.tag import Okt
from konlpy.tag import kkma

def space(sentence):
    word = sentence.split(" ")
    return word

def morph_okt(sentence):     #Okt형태소 분석기를 사용함
    word = okt.morph(sentence)
    return word

def morph_kkma(sentence):   #kkma형태소 분석기를 
    word = kkma.morph(sentence)
    return word

