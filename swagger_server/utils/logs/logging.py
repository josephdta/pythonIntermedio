import datetime
import logging
from logging.handlers import RotatingFileHandler


def log():
    #fecha actual del registro
    now= datetime.datetime.now()
    #formato de las fechas que maneja los logs
    format_logger= now.strftime('%Y-%m-%d')
    #inicializacion de nuestro logger
    logger=logging.getLogger('')
    #seteo del nivel de logger
    logger.setLevel(logging.INFO)

    #manejador para la creación de archivos
    handler= RotatingFileHandler(f'''logs/task-ms-{format_logger}.log''')
    formatter= logging.Formatter('%(asctime)s %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    if (logger.hasHandlers()):
        logger.handlers.clear()

    logger.addHandler(handler)
    return logger


