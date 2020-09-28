import logging

logger = logging.getLogger('')
logger.setLevel(level=logging.INFO)

def setLogName(name):
    handler = logging.FileHandler(name, mode='w')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', '%a, %d %b %Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

if __name__ == "__main__":
    setLogName('/Users/shihuajun/test_log.txt')
    logger.info("start func111")
    logger.info("start func222")
    logger.info("start func333")

    setLogName('/Users/shihuajun/test_log2.txt')
    logger.info("start func551")
    logger.info("start func5522")
    logger.info("start func355")


