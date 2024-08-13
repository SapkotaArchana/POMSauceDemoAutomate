import logging


def log_details():
    logging.basicConfig(filename="test.log",
                        format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO
                        )
    return logging.getLogger()


logger = log_details()

# a = 4
# b = 3
# if a > b:
#     print("Archana")
#     logger.info("A is > than B, Hence archana got printed")
#
# logger.info("Program execution ended")

