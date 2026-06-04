
# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service(r"C:\Users\Soham\OneDrive\Desktop\Data_science\Data_Analysis_Process\advanced-web-scraping\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get('http://google.com')
time.sleep(2)
try:
    agree_button = driver.find_element(By.XPATH, '//button[text()="I agree"]')
    agree_button.click()
    time.sleep(1)
except:
    pass
# 2️⃣ Locate search box and type "Campusx"
search_box = driver.find_element(By.NAME, 'q')  # using name="q" is reliable
search_box.send_keys('Campusx')

time.sleep(3)  # wait for results


# 3️⃣ Click the first search result
search_box.send_keys(Keys.ENTER)

time.sleep(3)  # wait for page to load

# 4️⃣ (Optional) Navigate to DSMP course page
# If the link exists on Campusx homepage
# Find first <h3> and get its parent <a>
first_result = driver.find_element(By.XPATH, '(//h3)[1]/ancestor::a')
first_result.click()

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()

time.sleep(1)
link2 = driver.find_element(by=By.XPATH, value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link2.click()
# Keep browser open for a while
time.sleep(10)