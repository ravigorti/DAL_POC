import sys
from DAL.src.exceptions import CustomException
from DAL.src.logger import logging

if __name__ == "__main__":
    try:
        a = 1/0
        print(a)
    except Exception as e:
        logging.info("Logging started")
        raise CustomException(e, sys)
