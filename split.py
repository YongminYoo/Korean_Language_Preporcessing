from konlpy.tag import Okt
from konlpy.tag import Kkma



def space(sentence):                #Split by space
    word = sentence.split(" ")
    return word

def morph_okt(sentence):            #Using Okt morph
    okt = Okt()
    word = okt.morph(sentence)
    return word

def morph_kkma(sentence):           #Using kkma morph
    kkma = Kkma()
    word = kkma.morph(sentence)
    return word

