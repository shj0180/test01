import time
import datetime
import DB2

localtime= time.asctime()
# print(localtime)
import random
localtime2 = time.strftime("%H:%M:%S",time.localtime())
# print(localtime2)


timeNow = datetime.datetime.now()
# %f 毫秒
time = timeNow.strftime('%Y%m%d%H%M%S%f')
print(time)

# r = random.random()
# print(int(r*1000))



