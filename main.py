from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Set up the Chrome driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# Open the website
driver.get('https://hprera.nic.in/PublicDashboard')

# Wait for the page to load
driver.implicitly_wait(10)

# Navigate to the 'Registered Projects' section
driver.find_element(
    By.XPATH, '//*[@id="tab_project_main-filtered-data"]/ul/li[1]/a').click()
time.sleep(2)  # Wait for the page to load

project_details = []

for i in range(0, 6):

    project_detail = {}

    # Click on RERANUMBER button to open details
    button = driver.find_element(
        By.XPATH, f'//*[@id="reg-Projects"]/div/div/div[{i+1}]/div/div/a')
    button.click()
    time.sleep(2)

    # Extract project details
    project_detail['GSTIN No'] = driver.find_element(By.XPATH, '//*[text()="GSTIN No."]/following-sibling::td/span').text
    project_detail['PAN No'] = driver.find_element(By.XPATH, '//*[text()="PAN No."]/following-sibling::td/span').text
    project_detail['Name'] = driver.find_element(By.XPATH, '//*[text()="Name"]/following-sibling::td').text
    project_detail['Permanent Address'] = driver.find_element(By.XPATH, '//*[text()="Permanent Address"]/following-sibling::td/span').text

    # Click on close button to close to move next 
    close_btn = driver.find_element(
        By.XPATH, '//*[@id="modal-data-display-tab_project_main"]/div/div/div[1]/button')
    close_btn.click()
    time.sleep(2)

    project_details.append(project_detail)

    # To prevent stale element reference exception
    time.sleep(2)

# Close the driver
driver.quit()

# Print the project details
for idx, detail in enumerate(project_details):
    print(f"Project {idx + 1}:")
    for key, value in detail.items():
        print(f"{key}: {value}")
    print("-" * 20)

# Write the project details to a CSV file
csv_file = "project_details.csv"
csv_columns = ['GSTIN No', 'PAN No', 'Name', 'Permanent Address']

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in project_details:
            writer.writerow(data)
except IOError:
    print("I/O error")

print(f"Project details have been written to {csv_file}")
