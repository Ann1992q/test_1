import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://only.digital/projects#brief")


Name = driver.find_element_by_css_selector("[name='name']")
Name.send_keys("test 1")
Email = driver.find_element_by_css_selector("[name='email']")
Email.send_keys("test1@mail.ru")
Phone = driver.find_element_by_css_selector("[name='phone']")
time.sleep(3)
Phone.click()
time.sleep(3)
Phone.send_keys("9998887766")
Company = driver.find_element_by_css_selector("[name='company']")
Company.send_keys("World")
complex_of_works = driver.find_element_by_css_selector(".sc-60972c5f-4.bqlaSe:nth-child(2) .sc-60972c5f-6.iVzsq>label:nth-child(1)")
complex_of_works.click()
about_project = driver.find_element_by_css_selector(".sc-30c137f2-1.iQiCsE.sc-60972c5f-8.eGNoom")
about_project.send_keys("Information about the project.")
budget = driver.find_element_by_css_selector(".sc-60972c5f-5.fUfKIm > .sc-60972c5f-4.bqlaSe:nth-child(3)>.sc-60972c5f-6.iVzsq>label:nth-child(1)")
budget.click()

#Вюбираю "Социальные сети"
social_networks = driver.find_element_by_css_selector(".sc-60972c5f-5.fUfKIm>div:nth-child(4)>div>label:nth-child(3)>span")
social_networks.click()

#Чтобы пройти капчу, можно выбрать ручное решение. Сначала нужно переключиться на iframe, в котором капча
from selenium.webdriver.common.by import  By
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ищу нужный мне элемент
I_am_not_Robot = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "recaptcha-anchor")) )
print("Капча загружена. Решите капчу вручную.")
#Пауза для ручного решения капчи
time.sleep(50)#Увеличте время, если необходимо
#После решения капчи продолжите решение теста
print("Капча решена.")

#теперь анкета заполнена, можно ее отправить


driver.quit()