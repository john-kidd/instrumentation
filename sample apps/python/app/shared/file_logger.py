import logging.handlers

app_logger = logging.getLogger('AppLogger')
app_logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=5)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
app_logger.addHandler(handler)


def log_info(message):
    app_logger.info(message)


def log_error(error):
    app_logger.error(error)
