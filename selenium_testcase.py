from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Initialize the WebDriver 
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver = webdriver.Firefox("/snap/bin/firefox/")

# Navigate to the Flask application's URL
driver.get("http://172.29.233.42:5000")

try:
    print("Test passed: 'Hello, World!' text found.")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser window
    driver.quit()
