from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # from fields

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    EXPAND_BUTTON_LIST = (By.CSS_SELECTOR, 'button[title = "Toggle"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class ="rct-icon rct-icon-check"]')
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")
    ITEMS_LIST_RADIOBUTTON = (By.CSS_SELECTOR, "label[class='custom-control-label']")


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    CLOSE = (By.CSS_SELECTOR, 'button[class="close"]')

    # tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    # delete
    NO_ROWS = (By.CSS_SELECTOR, 'div[class="rt-noData"]')

    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label = "rows per page"]')


class ButtonsPageLocators:
    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")  # вопрос

    RESULT_DOUBLE_BUTTON = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RESULT_RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    RESULT_CLICK_ME_BUTTON = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")  # вопрос


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")
    NOT_FOUND = (By.CSS_SELECTOR, "a[id='invalid-url']")
