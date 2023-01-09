from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON=(By.CSS_SELECTOR, "button[id='tabButton']")
    TITLE_NEW_TAB=(By.CSS_SELECTOR,"h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON=(By.CSS_SELECTOR, "button[id='windowButton']")


class AlertsPageLocators:
    SEE_ALERT_BUTTON=(By.CSS_SELECTOR, "button[id='alertButton']")
    APPEAR_ALERT_AFTER_5_SEC_BUTTON=(By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON=(By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_BOX_ALERT_BUTTON=(By.CSS_SELECTOR, "button[id='promtButton']")
    RESULT_TEXT_CONFIRM=(By.CSS_SELECTOR, "span[id='confirmResult']")
    RESULT_TEXT_PROMPT=(By.CSS_SELECTOR,"span[id='promptResult']")