import logging, logging.handlers
import time

'''
TimedRotatingFileHandler构造函数声明
class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)
filename    日志文件名前缀
when        日志名变更时间单位
    'S' Seconds
    'M' Minutes
    'H' Hours
    'D' Days
    'W0'-'W6' Weekday (0=Monday)
    'midnight' Roll over at midnight
interval    间隔时间，是指等待N个when单位的时间后，自动重建文件
backupCount 保留日志最大文件数，超过限制，删除最先创建的文件；默认值0，表示不限制。
delay       延迟文件创建，直到第一次调用emit()方法创建日志文件
atTime      在指定的时间（datetime.time格式）创建日志文件。
'''

def test_TimedRotatingFileHandler(myLog):
    # 定义日志输出格式
    fmt_str = '%(asctime)s[level-%(levelname)s][%(name)s]:%(message)s'
    # 初始化
    logging.basicConfig()

    # 创建TimedRotatingFileHandler处理对象
    # 间隔5(S)创建新的名称为myLog%Y%m%d_%H%M%S.log的文件，并一直占用myLog文件。
    fileshandle = logging.handlers.TimedRotatingFileHandler('/Users/shihuajun/%s'%myLog, when='S', interval=5, backupCount=3)
    # 设置日志文件后缀，以当前时间作为日志文件后缀名。
    fileshandle.suffix = "%Y%m%d_%H%M%S.log"
    # 设置日志输出级别和格式
    fileshandle.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt_str)
    fileshandle.setFormatter(formatter)
    # 添加到日志处理对象集合
    logging.getLogger('').addHandler(fileshandle)

if __name__ == '__main__':
    test_TimedRotatingFileHandler('mylog1')
    test_TimedRotatingFileHandler('mylog2')
    # 测试在200s内创建文件多个日志文件
    for i in range(0, 100):
        logging.debug("logging.debug")
        logging.info("logging.info")
        logging.warning("logging.warning")
        logging.error("logging.error")


        time.sleep(2)
