from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import locators
from Event.excel_function import Healthcare
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

file = "C:\\Users\\NANDHU-PC HOME\\PycharmProjects\\pythonProject\\PageObjectModel\\Event\\test_data1.xlsx"
sheet_number = 'Sheet1'
s = Healthcare(file, sheet_number)


rows = s.row_count()
print(rows)


try:

    for row in range(2, rows+1):
    # Username and Password from the Excel File
        username = s.read_data(row, 6)
        password = s.read_data(row, 7)
        date = s.read_data(row,4)
        service = Service(executable_path="C:\\Users\\NANDHU\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)

        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()
        before_url = driver.current_url
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 20)

        # driver.find_element(By.XPATH, locators.Locators().Make_appointment).click()

        wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().Make_appointment))).click()
        cookie_before = driver.get_cookies()[0]['value']
        wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().username))).send_keys(username)
        wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().password))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().login_btn))).click()


        after_url = driver.current_url
        cookie_after = driver.get_cookies()[0]['value']



        if "https://katalon-demo-cura.herokuapp.com/#appointment" in driver.current_url:
            for i in range(2, rows):
                comments = s.read_data(i,5)
                wait.until(EC.presence_of_element_located((By.XPATH,locators.Locators().comments))).send_keys(comments)
                break


            wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().check_box))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().date))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().date_select))).click()

            wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().book_appointment))).click()

            print('SUCCESS : login with {a}'.format(a=username))
            print("Appointment booked!!")
            s.write_data(row, 8, "TEST PASS")
            driver.close()
        else:
            print("FAIL : login failure with {a}".format(a=password))
            s.write_data(row, 8, "TEST FAIL")
            driver.close()
        driver.quit()



except NoSuchElementException or TimeoutException as e:
       print(e)






