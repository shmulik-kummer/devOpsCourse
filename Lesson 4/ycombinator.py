from selenium import webdriver

# Launch Chrome browser
driver = webdriver.Chrome()

# Open Y Combinator website
driver.get("https://www.ycombinator.com/")

# Get page title
title = driver.title

# Check if title is "Y Combinator"
if title == "Y Combinator":
    print("Test passed! The title is Y Combinator.")
else:
    print(f"Test failed! The title is {title} instead of Y Combinator.")

# Close browser window
driver.quit()
