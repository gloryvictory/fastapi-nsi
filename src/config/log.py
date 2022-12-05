import logging as log
import os

from src.config import settings


def set_logger():
    for handler in log.root.handlers[:]:  # Remove all handlers associated with the root logger object.
        log.root.removeHandler(handler)

    log_folder = settings.FOLDER_OUT
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    file_log = str(os.path.join(log_folder, settings.FILE_LOG))  # from cfg.file

    if os.path.isfile(file_log):  # Если выходной LOG файл существует - удаляем его
        os.remove(file_log)
    log.basicConfig(filename=file_log, format=settings.FILE_LOG_FORMAT, level=log.INFO,
                    filemode='w')
    log.info(file_log)
    return log