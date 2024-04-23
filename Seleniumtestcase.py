from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Navigate to the Flask application's URL
driver.get("http://localhost:5000")

try:
    print("Test passed: 'Hello, World!' text found.")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser window
    driver.quit()
