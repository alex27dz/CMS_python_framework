from selenium import webdriver
import time
import requests
from psutil import Process
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
'''  
def test_ui_page_load_time(url):
    start_time = time.time()

    driver = webdriver.Chrome()
    driver.get(url)

    end_time = time.time()
    page_load_time = end_time - start_time

    print(f"Page Load Time: {page_load_time} seconds")

    driver.quit()
def test_ui_response_time_for_user_action(url):
    driver = webdriver.Chrome()
    driver.get(url)

    start_time = time.time()

    # Perform user action (e.g., click a button)
    # driver.find_element_by_id("button_id").click()

    end_time = time.time()
    response_time = end_time - start_time

    print(f"UI Response Time for User Action: {response_time} seconds")

    driver.quit()
def test_ui_scrolling_performance(url):
    driver = webdriver.Chrome()
    driver.get(url)

    start_time = time.time()

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    end_time = time.time()
    scrolling_time = end_time - start_time

    print(f"UI Scrolling Performance: {scrolling_time} seconds")

    driver.quit()
def test_ui_error_handling_response_time(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # Trigger an error scenario
    # e.g., driver.find_element_by_id("nonexistent_element").click()

    start_time = time.time()

    # Handle error (if applicable)

    end_time = time.time()
    error_handling_time = end_time - start_time

    print(f"UI Error Handling Response Time: {error_handling_time} seconds")

    driver.quit()
def test_ui_error_handling_response_time(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # Trigger an error scenario
    # e.g., driver.find_element_by_id("nonexistent_element").click()

    start_time = time.time()

    # Handle error (if applicable)

    end_time = time.time()
    error_handling_time = end_time - start_time

    print(f"UI Error Handling Response Time: {error_handling_time} seconds")

    driver.quit()
def test_ui_resource_load_time(url):
    start_time = time.time()

    response = requests.get(url)

    end_time = time.time()
    resource_load_time = end_time - start_time

    print(f"UI Resource Load Time: {resource_load_time} seconds")
def test_ui_navigation_timing(url):
    driver = webdriver.Chrome()
    driver.get(url)

    navigation_timing = driver.execute_script("return window.performance.timing;")

    # Extract and print relevant timing information
    print(f"Navigation Start Time: {navigation_timing['navigationStart']}")
    print(f"Load Event Start Time: {navigation_timing['loadEventStart']}")

    driver.quit()
def test_ui_browser_memory_usage(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    process = Process(driver.service.process.pid)
    memory_usage = process.memory_info().rss / (1024 ** 2)  # Convert to megabytes

    print(f"Browser Memory Usage: {memory_usage} MB")

    driver.quit()
'''

urls_list = []


def measure_all_elements_response_time(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # Get all elements on the page
    all_elements = driver.find_elements(By.XPATH, '//*')
    total_response_time = 0
    total_elements = 0

    # Measure response time for each element
    for element in all_elements:
        start_time = time.time()

        # Wait for the element to appear
        element_location = element.location_once_scrolled_into_view
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        total_elements += 1
        print(f"Response time for {element.tag_name}: {response_time:.2f} seconds")

    # Calculate average response time
    if total_elements > 0:
        average_response_time = total_response_time / total_elements
        print(f"\nAverage response time for all elements: {average_response_time:.2f} seconds")

    # Close the browser
    driver.quit()









