from selenium.webdriver import Keys

from Generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators=FormPageLocators()
    def fill_form_fields(self):
        person=next(generated_person())
        file_name, path= generated_file()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)

        #self.element_is_visible(self.locators.GENDER).click()

        self.element_is_visible(self.locators.SUBJECTS).send_keys("Maths")
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.BIRTH_DAY).clear()
        self.element_is_visible(self.locators.BIRTH_DAY).send_keys(person.birth_date)
        self.element_is_visible(self.locators.BIRTH_DAY).send_keys(Keys.RETURN)

        #self.element_is_visible(self.locators.GENDER).send_keys(person.mobile)
        #self.element_is_visible(self.locators.GENDER).send_keys(person.mobile)
        #self.element_is_visible(self.locators.GENDER).send_keys(person.mobile)
        #self.element_is_visible(self.locators.GENDER).send_keys(person.mobile)

