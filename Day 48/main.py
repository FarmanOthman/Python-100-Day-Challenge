from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the target website
driver.get('https://orteil.dashnet.org/experiments/cookie/')

# Locate the cookie element by XPath
element = driver.find_element(By.XPATH, '//*[@id="cookie"]')

# Define the clicker function to repeatedly click the element
def clicker():
    while True:
        element.click()

# Start the clicker function in a new thread
thread = threading.Thread(target=clicker)
thread.start()
