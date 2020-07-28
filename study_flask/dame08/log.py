


import logging
logging.basicConfig(
    filename = r'text.log',
    filemode= 'a',
    level=logging.INFO,
	format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')      # filename 是将信息写入 text.log  文件中

# filename = r'text.log' 日志文件名
# filemode = 'a', 追加模式


# asctime 输出时间
# filename名字 默认文件名
# levelname 错误级别
# 输出模式
logger = logging.getLogger(__name__)


logger.debug('debug message') # 排错
logger.info('info message') # 正常信息
logger.warning('warning message') # 警告
logger.error('error message') # 错误
logger.critical('critical message') # 崩溃

# filename = r'text.log'



