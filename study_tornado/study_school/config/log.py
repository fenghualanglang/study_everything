# -*- coding: utf-8 -*-
import logging
import logging.handlers
import os

# log format
_cur_dir = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
_log_dir = os.path.normpath(os.path.join(_cur_dir, '../logs'))

logging_main = {
    'name': 'main',
    'path': '{}/main.log',
    'size': 10 * 1000 * 1000,
    'count': 10,
    'level': logging.INFO,
}

logging_sms = {
    'name': 'sms',
    'path': '{}/sms.log',
    'size': 10 * 1000 * 1000,
    'count': 10,
    'level': logging.INFO,
}

logging_push_order = {
    'name': 'push_order',
    'path': '{}/push_order.log',
    'size': 10 * 1000 * 1000,
    'count': 10,
    'level': logging.INFO,
}

logging_user = {
    'name': 'user',
    'path': '{}/user.log',
    'size': 10 * 1000 * 1000,
    'count': 10,
    'level': logging.INFO,
}

logger_sms = logging.getLogger(logging_sms['name'])
logger_main = logging.getLogger(logging_main['name'])
logger_push_order = logging.getLogger(logging_push_order['name'])
logger_user = logging.getLogger(logging_user['name'])


def setup_logger(port):
    logging_sms['path'] = logging_sms['path'].format(_log_dir, port)
    logging_main['path'] = logging_main['path'].format(_log_dir, port)
    logging_push_order['path'] = logging_push_order['path'].format(_log_dir, port)
    logging_user['path'] = logging_user['path'].format(_log_dir, port)
    _set_logger(logging_sms)
    _set_logger(logging_main)
    _set_logger(logging_push_order)
    _set_logger(logging_user)


def _set_logger(log_dict):
    handler = logging.handlers.RotatingFileHandler(
        log_dict['path'], maxBytes=log_dict['size'], backupCount=log_dict['count']
    )
    fmt = '[%(asctime)s %(levelname)s] %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger(log_dict['name'])
    logger.addHandler(handler)
    logger.setLevel(log_dict['level'])
