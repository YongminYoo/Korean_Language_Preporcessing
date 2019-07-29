from konlpy.tag import Okt
from konlpy.tag import Kkma


'''
Input sentence must be str format
Split by space , Split by Hannanum , Kkma , Komoran , Okt morphs which are in konlpy (Mecab morphs is not include in this code)
Requirement : konlpy => 0.5.2
'''

'''
Input sentence는 str format으로 셋팅해야합니다.
어절단위(띄어쓰기)로 split , konlpy의 Hannaum , Kkma , Okt 형태소분석 모듈을 이용해서 각 형태소 분석 단위로 split 합니다.(Mecab 형태소 분석은 이 코드에 포함되어 있지 않습니다.)
Requirement : konlpy => 0.5.2
'''


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

def hannanum(sentence):           #Using hannanum morph
    hannanum = Hannanum()
    word = hannanum.morphs(sentence)
    return word

