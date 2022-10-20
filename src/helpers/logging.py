import logging

def log(file, text, level):
    infoLog = logging.FileHandler(file)
    infoLog.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger = logging.getLogger(file)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(infoLog)
        if (level == 'INFO'):
            logger.info(text)
        if (level == 'ERROR'):
            logger.error(text)
        if (level == 'WARNING'):
            logger.warning(text)
    infoLog.close()
    logger.removeHandler(infoLog)
    return
