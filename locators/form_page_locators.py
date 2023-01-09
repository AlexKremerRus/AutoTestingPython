import random

from selenium.webdriver.common.by import By

class FormPageLocators:
    FIRST_NAME=(By.CSS_SELECTOR,"input[id='firstName']")
    LAST_NAME=(By.CSS_SELECTOR,"input[id='lastName']")
    EMAIL=(By.CSS_SELECTOR,"input[id='userEmail']")
    GENDER=(By.CSS_SELECTOR,f"label[for='gender-radio-{random.randint(1,3)}']")
    MALE_GENDER=(By.CSS_SELECTOR,"input[id='gender-radio-1']")
    FEMALE_GENDER=(By.CSS_SELECTOR,"input[id='gender-radio-2']")
    OTHER_GENDER=(By.CSS_SELECTOR,"input[id='gender-radio-3']")
    MOBILE_NUMBER=(By.CSS_SELECTOR,"input[id='userNumber']")
    BIRTH_DAY=(By.CSS_SELECTOR,"input[id='dateOfBirthInput']")

    SUBJECTS=(By.CSS_SELECTOR,"input[id='subjectsInput']")
    HOBBIES=(By.CSS_SELECTOR,f"label[for='hobbies-checkbox-{random.randint(1,3)}']")
    SPORTS_CHECK=(By.CSS_SELECTOR,"input[id='hobbies-checkbox-1']")
    READING_CHECK=(By.CSS_SELECTOR,"input[id='hobbies-checkbox-2']")
    MUSIC_CHECK=(By.CSS_SELECTOR,"input[id='hobbies-checkbox-3']")
    CHOOSE_FILE=(By.CSS_SELECTOR,"input[id='uploadPicture']")

    CURRENT_ADDRESS=(By.CSS_SELECTOR,"textarea[id='currentAddress']")
    SELECT_STATE=(By.CSS_SELECTOR,"div[id='state']")
    STATE_INPUT=(By.CSS_SELECTOR,"input[id='react-select-3-input']")
    SELECT_CITY=(By.CSS_SELECTOR,"div[id='city']")
    CITY_INPUT=(By.CSS_SELECTOR,"input[id='react-select-4-input']")
    SUBMIT=(By.CSS_SELECTOR,"button[id='submit']")

    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")