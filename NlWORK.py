import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import mysql.connector
import math
stop_words = set(stopwords.words('english'))



ucomment = """ good  """

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(ucomment)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


ps = PorterStemmer()

i=0;

j=0;
for w in filtered_sentence:
    print(ps.stem(w))
    word = ps.stem(w)
    j += 1

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    cursor = conn.cursor()
    cursor.execute("SELECT *  FROM negtb WHERE words  like '%" + word + "%'  ")
    data2 = cursor.fetchone()
    if data2:
        i += 1
        uname = data2[1]

    else:
        print('Nodata')




print(i)

#print(j)

j = j/3

j = math.floor(j)
print(j)


if( j < i):
    print('1')
else:
    print('0')
