from collections import Counter
import re


txt = open('EnglishTxt','r').read()
# print(txt)

#使用非文字字符分割
data=re.split('\W+',txt)
print(data)

#输出这篇文章内出现频率最高的10个词
most_common=Counter(data).most_common(10)
print(most_common)


