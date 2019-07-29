from konlpy.tag import Okt
from konlpy.tag import Kkma



def space(sentence):                #Split by space
    word = sentence.split(" ")
    return word

def okt(sentence):            #Using Okt morph
    okt = Okt()
    word = okt.morphs(sentence)
    return word

def kkma(sentence):           #Using kkma morph
    kkma = Kkma()
    word = kkma.morphs(sentence)
    return word

