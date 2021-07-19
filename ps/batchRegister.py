import random
from time import sleep
from selenium import webdriver

class BatchRegister:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'xxx' #此为测试换的账号注册地址
        self.driver.maximize_window()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def register(self,teacherTel='12211221122',username='胡二四',password='hxd123456',parentTel='12212345572'):
        self.driver.get(url=self.url)
        self.driver.find_element_by_class_name('change-code').click()
        self.driver.find_element_by_link_text('立即注册').click()
        self.driver.find_element_by_class_name('image').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/input').send_keys(teacherTel)
        self.driver.find_element_by_class_name('JS-agreement').click()
        self.driver.find_element_by_link_text('注册学生账号').click()
        sleep(1)
        self.driver.find_element_by_link_text('新用户').click()
        self.driver.find_element_by_xpath('//*[@id="allSearchClazzItem"]/div[3]/span[1]').click()
        self.driver.find_element_by_xpath('//*[@id="allSearchClazzItem"]/div[3]/div[2]/span[1]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="register_template"]/div[2]/div[2]/div/ul[2]/li[1]/input').send_keys(
            username)
        self.driver.find_element_by_xpath('//*[@id="register_template"]/div[2]/div[2]/div/ul[2]/li[2]/input').send_keys(
            password)
        self.driver.find_element_by_xpath('//*[@id="register_template"]/div[2]/div[2]/div/ul[2]/li[3]/input').send_keys(
            password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="register_template"]/div[2]/div[2]/div/ul[2]/li[4]/input').send_keys(
            parentTel)
        self.driver.find_element_by_xpath('//*[@id="studentGetCheckCodeBtn"]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="register_template"]/div[2]/div[2]/div/ul[2]/li[5]/input').send_keys(
            '1234')
        self.driver.find_element_by_link_text('完成注册').click()
        sleep(3)
        self.driver.quit()

