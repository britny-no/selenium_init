# from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# linux 환경에서 필요한 option
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')


chrome_driver_path="/Users/nojeong-u/Desktop/selenium/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)


driver.get("https://www.naver.com")
print(driver.current_url) 

