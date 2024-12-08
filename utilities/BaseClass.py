import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


#This will be used to call the fixture instaed of declaring the fixture in all the files to use in the classes of other files
@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger