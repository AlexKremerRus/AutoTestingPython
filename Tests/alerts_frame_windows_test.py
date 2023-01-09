from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage
import time


class AlertPage:
    pass


class TesteAlertFrameWimdow:
    class TestBrowserWindows:
        def test_new_tab(self,driver):
            new_tab_page = BrowserWindowsPage(driver,"https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result=new_tab_page.check_opened_new_tab()
            assert text_result=="This is a sample page" , 'значения не совпадают'
            #time.sleep(2)

        def test_new_window(self,driver):
            new_window_page = BrowserWindowsPage(driver,"https://demoqa.com/browser-windows")
            new_window_page.open()
            text_result=new_window_page.check_opened_new_tab()
            assert text_result=="This is a sample page", 'значения не совпадают'

    class TestAlertsPage:

        def test_see_alert(self,driver):
            alert_page=AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            alert_text=alert_page.check_see_alert()
            assert alert_text=='You clicked a button'

        def test_after_5_sec_alert(self,driver):
            alert_page=AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            alert_text=alert_page.check_alert_appear_5_sec()
            assert alert_text=='This alert appeared after 5 seconds'

        def test_confirm_alert(self,driver):
            alert_page=AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            alert_text=alert_page.check_confirm_alert()
            assert alert_text=='You selected Ok'

        def test_prompt_alert(self,driver):
            alert_page=AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            text, alert_text=alert_page.check_prompt_alert()
            assert alert_text==f'You entered {text}'
