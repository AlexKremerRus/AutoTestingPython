import random
import time

from Generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 23
        while count != 0:

            item = item_list[random.randint(1, 15)]
            if count > 0:

                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)

            data.append(title_item.text)
        return str(data).lower().replace(' ', '').replace('.doc', '')

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    # клик рандом

    def clock_on_the_radio_button(self, choise):
        choises = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choises[choise]).click()

    # def click_random_button(self):
    #     button_item_list = self.elements_are_vissible(self.locators.BUTTON_ITEMS_LIST)
    #     count =5
    #     while count != 0:
    #
    #         item = button_item_list[random.randint(1, 2)]
    #         if count > 0:
    #
    #             self.go_to_element(item)
    #             item.click()
    #             count -= 1
    #         else:
    #             break
    # проверить что проставилось

    def get_output_result(self):
        return self.element_is_present((self.locators.OUTPUT_RESULT)).text

    # проверить что написано
    # ассерт


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    #
    # def add_new_person_click(self):
    #
    # def add_new_person_data(self):
    #
    # def add_new_person_submit(self):

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        time.sleep(0.1)
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)

        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        # сделать для рандомных данных не только для возраста
        # print(person_info)
        # rand=random.randint(1, 8)
        # person = {0:"full_name", 1:"person_info.firstname", 2:"person_info.lastname", 3:"person_info.age", 4:"person_info.department", 5:"person_info.salary", 6:"person_info.email", 7:"person_info.current_address", 8:"person_info.permanent_address" }
        # сделать для рандома ( не только возраст менять)
        # print(person[rand])
        age = person_info.age
        # print(Age)
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):

        return self.element_is_present(self.locators.NO_ROWS).text

    def select_up_to_same_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.RESULT_DOUBLE_BUTTON)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.RESULT_RIGHT_CLICK_BUTTON)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.RESULT_CLICK_ME_BUTTON)

    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
        return self.check_clicked_on_the_button(self.locators.RESULT_DOUBLE_BUTTON)

    def right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.locators.RESULT_RIGHT_CLICK_BUTTON)

    def click(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
        return self.check_clicked_on_the_button(self.locators.RESULT_CLICK_ME_BUTTON)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text
