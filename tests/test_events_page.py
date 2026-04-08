import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEventsPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

    def tearDown(self):
        self.driver.quit()
      
    def test_page_load(self):
        body = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        self.assertTrue(body.is_displayed())

    def test_events_exist(self):
        events = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div"))
        )
        self.assertTrue(len(events) > 0)

    def test_open_first_event(self):
        events = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a"))
        )
        events[0].click()

        self.wait.until(
            EC.url_changes("https://www.greencity.cx.ua/#/greenCity/events")
        )

        self.assertNotEqual(
            self.driver.current_url,
            "https://www.greencity.cx.ua/#/greenCity/events"
        )
