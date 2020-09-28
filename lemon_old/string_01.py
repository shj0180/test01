a="afsf"
b=a.upper()
print(b)

# 1.查找字符
c=a.find("f",0,-1)
print(c)
c=a.find("d")
print(c)

# 2.替换---count为替换几次，如字符串中有2个f，1就是只替换一个
str1=a.replace("f","c",1)
print(str1)

# 3.去掉头尾的空格
eg1="  ds$f*s*af  "
s1=eg1.strip()
print(s1)

# 4.切片,  大于等于1    小于3
num="0123456789"
# n[0] n[1] n[2] n[3]
num2=num[1:3]
print("num2:%s"%num2)

num1=num[::2]
print("num1:%s"%num1)

num1=num[1:5:2]
print(num1)

# -1是向左移动切片，起始位置默认从最后一个开始：-1或不填写，-2就是从字符串的最后第二位向左切片到4前结束，不包括4
num3=num[-2:4:-1]
print(num3)

# 查看unicode码
lzi = '上'
print('unicode码:%s'%ord(lzi))
num = 19978
print(chr(num))

t = '''333 535  435 5435 435 34 5435 43 6 46 45 6 3456 54 6 456 43 3432'''
t1 = t.replace(' ','\n')
print(t1)

count = 1
def countqq(count):

    str1 = '多少'
    count += 1
    str1.join(count)


countqq(4)
