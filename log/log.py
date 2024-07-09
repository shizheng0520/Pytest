import logging

#创建日志器
logger = logging.getLogger()

#定义日志器级别
logger.setLevel(logging.INFO)

#定义日志器格式
format = logging.Formatter('%(asctime)s %(filename)s [line:%(lineo)d]%(levelname)s%(message)s')
logFile = r'C:\python_auto\unitest\log'

#创建处理器
fh = logging.FileHandler(logFile, mode = 'a', encoding = 'utf-8')

#设置处理器级别
fh.setLevel(logging.INFO)

#设置处理器格式
fh.setFormatter(format)

#添加到日志器
logger.addHandler(fh)