import os
import sys
import unittest
from path_dir import log_dir
import logging

class BaseCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        log_path = os.path.join(log_dir,"{}.log".format(self.__name__))
        self.logger = self.add_logger(self.__name__,log_path,logging.INFO)

    @staticmethod
    def add_logger(log_name, log_file_path, log_level):
        # 创建一个logging
        logger = logging.getLogger(log_name)
        logger.setLevel(log_level)
        # 创建一个hander，用于写入日志文件
        fh = logging.FileHandler(log_file_path)
        fh.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        return logger

    def log_cur_name(self):
        return str(sys._getframe().f_back.f_code.co_name)

    def tearDown(self) -> None:
        pass

