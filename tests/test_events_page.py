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
        self.url = "https://www.greencity.cx.ua/#/greenCity/events"
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()
        
    def test_page_load(self):
        self.assertIn("events", self.driver.current_url)

    def test_events_cards_present(self):
        cards = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'event')]"))
        )
        self.assertTrue(len(cards) > 0)

    def test_open_event(self):
        cards = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'event')]"))
        )

        cards[0].click()

        self.wait.until(EC.url_changes(self.url))

        self.assertNotEqual(self.driver.current_url, self.url)


if __name__ == "__main__":
    unittest.main()
