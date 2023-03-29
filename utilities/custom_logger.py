import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.info("root")
        logging.basicConfig(
            level=logging.INFO,
            filename=".//logs//automation.log",
            filemode="w",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # logger = logging.getLogger(__name__)
        # handler = logging.FileHandler('automations1.log')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        # logger.addHandler(handler)
        return logger

    @staticmethod
    def loggen_error():
        logging.info("root")
        logging.basicConfig(
            level=logging.ERROR,
            filename=".//logs//automation.log",
            filemode="w",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        # logger = logging.getLogger(__name__)
        # handler = logging.FileHandler('automations1_error.log')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        # logger.addHandler(handler)
        return logger
