from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# URL of the website
url = "https://ilthermo.boulder.nist.gov"

# chrome_driver_path = 'c:/web/chromedriver.exe'
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'

# Start the browser
options = webdriver.ChromeOptions()
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Access the search page
driver.get(url)

sbutton = driver.find_element(By.ID, "sbutton")
sbutton.click()

# Wait for the dialog to appear and interact with the form elements
wait = WebDriverWait(driver, 90)
sDialog = wait.until(EC.presence_of_element_located((By.ID, "sDialog")))

# Fill in the year input field
yearbox = driver.find_element(By.CSS_SELECTOR, "input#year")
yearbox.send_keys("2019")

# You can fill in other form elements similarly...

# Click on the "Submit" button
submbutt = driver.find_element(By.ID, "submbutt")
submbutt.click()


# Wait for the search results to load
try:
    grid_locator = (By.CSS_SELECTOR, "#dsgrid .dgrid-row")
    wait.until(EC.presence_of_element_located(grid_locator))
except TimeoutException:
    print("No search results found within the specified time.")
    driver.quit()
    # exit()

# Retrieve the data from the grid
try:
    first_row = driver.find_element(*grid_locator)
    columns = first_row.find_elements(By.CSS_SELECTOR, ".dgrid-cell")
    for column in columns:
        print(column.text)
except NoSuchElementException:
    print("No elements found in the grid.")
finally:
    # Close the WebDriver
    driver.quit()

 #Retrieve data from all rows in the grid
try:
    grid_locator = (By.CSS_SELECTOR, "#dsgrid .dgrid-row")
    rows = driver.find_elements(*grid_locator)
    for row in rows:
        columns = row.find_elements(By.CSS_SELECTOR, ".dgrid-cell")
    for column in columns:
        print(column.text)
except NoSuchElementException:
        print("No elements found in the grid.")
finally:
    driver.quit()