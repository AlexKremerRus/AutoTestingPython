import time

from pages.form_page import FormPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            form_page=FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            person_info=form_page.fill_form_fields()
            result=form_page.form_result()
            print(result[0], result[1])
            print(person_info.firstname,person_info.lastname,person_info.email)
            assert [person_info.firstname+' '+ person_info.lastname,person_info.email] == [result[0], result[1]] , "Имя\фамилия\емейл не совпадают"
            #time.sleep(5)
