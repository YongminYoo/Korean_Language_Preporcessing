# Korean_Language_Preporcessing

한국어 자연어 처리를 위한 pre-processing code 입니다. 외부 라이브러리들(konlpy,nltk 등..)을 사용하여 코드를 구성하였습니다. 따라서 한국어 자연어처리를 처음 접하시거나 한국어 자연어처리에 익숙하지 않으신 분들이 참고하시면 좋을 것 같습니다.

 
# Contents

### <b>**Clean Text**</b></br>
**clean.py**<br>
1-1. 한글과 띄어쓰기와 의미있는 특수문자를 제외한 모든 글자 

</br>
### <b>**Tokenizer**</b></br>
**tokenizer.py**<br>
2-1. 어절단위 tokenize(tokenize by space) </br>
2-2. Konlpy의 Okt 형태소분석기를 사용해서 tokenize (tokenize by Okt morphs)</br>
2-3. Konlpy의 kkma 형태소분석기를 사용해서 tokenize (tokenize by Kkma morphs)</br>
2-4. Konlpy의 Hannanum 형태소분석기를 사용해서 tokenize (tokenize by Hannanum morphs)</br>


