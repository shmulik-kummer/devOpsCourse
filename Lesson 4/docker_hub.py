from selenium import webdriver

# Launch Chrome browser
driver = webdriver.Chrome()

# Open Docker Hub website
driver.get("https://hub.docker.com/")

# Get page title
title = driver.title

# Check if title is "Docker Hub Container Image Library | App Containerization"
if title == "Docker Hub Container Image Library | App Containerization":
    print("Test passed! The title is Docker Hub Container Image Library | App Containerization.")
else:
    print(f"Test failed! The title is {title} instead of Docker Hub Container Image Library | App Containerization.")

# Close browser window
driver.quit()