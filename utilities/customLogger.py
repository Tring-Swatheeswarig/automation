import logging
import sys
import re

class ColorFilter(logging.Filter):
    color_pattern = re.compile(r'\x1b\[\d+m')

    def filter(self, record):
        record.msg = self.color_pattern.sub('', record.msg)
        return True

class ColorConsoleHandler(logging.StreamHandler):
    def emit(self, record):
        record.msg = ColorFilter.color_pattern.sub('', record.msg)
        super().emit(record)

class ColorFileHandler(logging.FileHandler):
    def emit(self, record):
        record.msg = ColorFilter.color_pattern.sub('', record.msg)
        super().emit(record)

class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        console_handler = ColorConsoleHandler(stream=sys.stderr)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        file_handler = ColorFileHandler(".//Logs//automation.log")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        logging.root.addHandler(console_handler)
        logging.root.addHandler(file_handler)
        logging.root.setLevel(logging.INFO)
        return logging.getLogger()
