from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Hack_Event.Test_data import data
from Hack_Event.Test_locator import locators
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Test_Project:
# Boot method to run Pytest using POM
   @pytest.fixture
   def setup(self):
      # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
      service = Service(executable_path="C:\\Users\\NANDHU\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
      self.driver = webdriver.Firefox(service=service)
      self.driver.maximize_window()
      self.wait = WebDriverWait(self.driver, 20)
      yield
      self.driver.close()
   def test_login(self,setup):
      try:
        self.driver.get(data.Data().url)
        before_url = self.driver.current_url
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().Make_appointment))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().username))).send_keys(data.Data().username)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().password))).send_keys(data.Data().password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().login_btn))).click()
        after_url= self.driver.current_url
        if before_url!= after_url:
           print('Login Successful {a}'.format(a=data.Data().username))
        else:
           print('Invalid Credential {a}'.format(a=data.Data().invalid_password))
      except TimeoutException as e:
         print(e)


   def test_Negative_case(self,setup):
       try:

           self.driver.get(data.Data().url)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().Make_appointment))).click()
           before_url = self.driver.current_url
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().username))).send_keys(data.Data().username)
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().password))).send_keys(data.Data().invalid_password)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().login_btn))).click()
           after_url = self.driver.current_url
           if before_url != after_url:
               print('Login Successful {a}'.format(a=data.Data().username))
           elif before_url == after_url:
               print('Invalid Credential {a}'.format(a=data.Data().invalid_password))
       except TimeoutException as e:
           print(e)
   def test_validation(self,setup):
       try:

           self.driver.get(data.Data().url)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().Make_appointment))).click()
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().username))).send_keys(
               data.Data().username)
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().password))).send_keys(
               data.Data().password)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().login_btn))).click()

           dropdown = Select(self.driver.find_element(By.XPATH, locators.Locators().select))
           dropdown.select_by_value("Seoul CURA Healthcare Center")
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().check_box))).click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().health_Care))).click()
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().date))).send_keys(
               data.Data().visit_data)
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().comments))).send_keys(
               data.Data().comments)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().book_appointment))).click()
           booked = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, locators.Locators().confirm)))
           if booked.is_displayed():
               print("Appointment Booked !!")
           else:
               print('Invalid Credentials!!')

           # After booking Navigate to home page
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().home_page))).click()
           current_url_page = self.driver.current_url
           if current_url_page == "https://katalon-demo-cura.herokuapp.com/":
               print("Navigate to Home Page ")

           # History option validation

       except TimeoutException as e:
           print(e)
   def test_side_menu(self,setup):
       try:
           self.driver.get(data.Data().url)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().Make_appointment))).click()
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().username))).send_keys(
               data.Data().username)
           self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Locators().password))).send_keys(
               data.Data().password)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().login_btn))).click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().menu))).click()
           menu = self.wait.until(EC.visibility_of_element_located((By.XPATH,locators.Locators().elememt)))
           list_element = menu.find_elements(By.TAG_NAME,locators.Locators.li_ele)
           for expected in data.Data().menu:
               for option in list_element:
                   if expected in option.text:
                       print(f"{expected} option is displayed.")


       except TimeoutException as e:
           print(e)
