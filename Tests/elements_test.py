import time

# from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            # output_per_addr="1"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox in output_result, "Выбранные данные не равны списку выбранных"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.clock_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.clock_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.clock_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()

            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

    class TestWebTable:
        def test_web_table_add_person(self,
                                      driver):  # можно переписать и разбить функцию адд нью персон на несколько (нажатие адд, заполнение полей, нажать сабмит) а внутри теста вести через цикл с рандомом
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            # time.sleep(5)
            table_result = web_table_page.check_new_added_person()
            # print(new_person)
            # print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            firstname = web_table_page.add_new_person()[0]
            # time.sleep(0.1)
            web_table_page.search_some_person(firstname)
            # time.sleep(0.1)
            table_result = web_table_page.check_search_person()
            # time.sleep(0.5)
            # firstname_2="sdfsdf"
            assert firstname in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            # web_table_page.update_person_info()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            time.sleep(2)
            row = web_table_page.check_search_person()
            # print(age)
            # print(row)
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            # web_table_page.update_person_info()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

            # assert age in row, "the person card has not been changed"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_same_rows()
            assert count == [5, 10, 20, 25, 50, 100], "the number of rows is the table has not been change"

    class TestButtonsPage:
        # сделать из одного теста три на каждую кнопку
        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            # double = buttons_page.click_on_different_button("double")
            # right = buttons_page.click_on_different_button("right")
            # click = buttons_page.click_on_different_button("click")
            double = buttons_page.double_click()
            right = buttons_page.right_click()
            click = buttons_page.click()
            # print()
            # print(double)
            # print(right)
            # print(click)
            assert double == "You have done a double click", "No double click"
            assert right == "You have done a right click", "No Right click"
            assert click == "You have done a dynamic click", "No click"


class TestLinkPage:
    def test_check_link(self, driver):
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        print(href_link, current_url)
        assert href_link == current_url

    def test_broken_link(self, driver):
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()
        response_code = str(links_page.check_broken_link('https://demoqa.com/bad-request'))
        assert response_code == '400'

class TestUploadAndDownload:

    def test_upload_file(self, driver):
        UpADown_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
        UpADown_page.open()
        file_name, result =UpADown_page.upload_file()
        assert file_name==result , "the file is not the same "

    def test_download_file(self,driver):
        UpADown_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
        UpADown_page.open()
