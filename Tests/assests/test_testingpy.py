import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from PageObjects.Directory import Directory
from utilities.BaseClass import BaseClass
from PageObjects.DashBoard import DashBoard


class Testing(BaseClass):
    def test_testin(self):
        log = self.getLogger()
        dashBoard = DashBoard(self.driver)
        dash = dashBoard.time_at_work()
        log.info("Getting all details")
        dashBoard.my_actions()
        dashBoard.quick_launch()
        dashBoard.buzz_latest()
        dashBoard.employees_on_leave_today()
        dashBoard.employees_distribution_sub_unit()
        dashBoard.employees_distribution_location()

    def test_dir(self):
        directo = Directory(self.driver)
        directo.search_by_name(sen="pet", text1="Peter Mac Anderson")
        directo.search()
        directo.filter_by_job_title(title="Automaton Tester")
        directo.filter_by_location(location="Texas R&D")
