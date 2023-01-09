from pages.alerts_frame_windows_page import BrowserWindowsPage
import time


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

