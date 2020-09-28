import configparser

config = configparser.ConfigParser()
config.read('configparser_01.ini')

# 获取section的名称
allsec = config.sections()
print(allsec)

# 获取某一section下的option
op = config.options('section1')
print(op)

# 获取item
it = config.items('section1')
print(it)

# 获取指定  getboolen  getfloat
zd = config.get('section1','k1')
print(zd,type(zd))

zd2 = config.getint('section2','k3')
print(zd2,type(zd2))









