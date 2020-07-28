






import logging
# 创建一个logging对象
logger = logging.getLogger()
# 创建一个文件对象  创建一个文件对象,以UTF-8 的形式写入 标配版.log 文件中
handler = logging.FileHandler('test1.log',encoding='utf-8')
# 配置显示格式  可以设置两个配置格式  分别绑定到文件和屏幕上
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
handler.setFormatter(formatter)  # 将格式绑定到两个对象上


logger.addHandler(handler)   # 将两个句柄绑定到logger
# logger.addHandler(sh)

logger.setLevel(10)   # 总开关
handler.setLevel(10)  # 写入文件的从10开始


# 创建一个屏幕对象
# sh = logging.StreamHandler()
# sh.setFormatter(formatter)
# sh.setLevel(30)  # 在屏幕显示的从30开始

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')









