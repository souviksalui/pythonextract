import unittest
import os
import certifi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Ensure proper SSL verification
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ['WDM_SSL_VERIFY'] = '0'  # Disable SSL verification for webdriver-manager

class PythonOrgSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        # options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")

        try:
            # Use manually downloaded ChromeDriver if necessary
            # cls.driver = webdriver.Chrome(service=Service("C:/path/to/chromedriver.exe"), options=options)

            # Use webdriver-manager (ensure internet access)
            cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        except Exception as e:
            raise RuntimeError(f"Failed to initialize WebDriver: {e}")

        cls.driver.get("https://www.python.org/")

    def test_search_python(self):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("Python")
        search_bar.send_keys(Keys.RETURN)

        self.assertIn("Python", self.driver.title)

        results = self.driver.find_elements(By.CSS_SELECTOR, "ul.list-recent-events.menu li a")
        self.assertGreater(len(results), 0, "No search results found")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
