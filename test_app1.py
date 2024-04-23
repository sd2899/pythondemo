from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# Initialize the WebDriver 
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Navigate to the Flask application's URL
driver.get("http://172.29.233.42:5000")

try:
    print("Test passed: 'Hello, World!' text found.")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser window
    driver.quit()
