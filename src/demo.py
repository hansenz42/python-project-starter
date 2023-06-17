from component.ConfigManager import config_manager
from component.LogManager import log_manager

# 读取 log_level 配置
log_level = config_manager.get_value(['log_level'])

# 获取日志
log = log_manager.get_logger('main')

log.debug(f'current log level is {log_level}')