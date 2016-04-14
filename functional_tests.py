from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from distutils.dist import warnings
from time import sleep

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #安妮听说有一个很酷的在线待办事项应用
        #她去看了这个应用的首页
        self.browser.get('http://localhost:8000');
        #她注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', head_text)
        
        #她被邀请直接输入一个to-do事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')   
        #sleep(5)
        
        #她在一个文本框中输入了“Buy a new nipple”
        #安妮的爱好是喝奶
        inputbox.send_keys('Buy a new nipple')
        
        #她按回车键后，页面更新了
        #待办事项表格中显示了“1：Buy a new nipple”
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1:Buy a new nipple' for row in rows),
                        "New to-do item did not appear in table")
        
        #页面中又显示了一个文本框，可以输入其他的待办事项
        #她输入了“Use a new nipple to drink water”
        #安妮做事很有条理
            
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()

#页面再次更新，她的清单中显示了这两个待办事项


#安妮想知道这个网站是否会记住她的清单


#她看到网站为她生成了一个唯一的URL
#而且页面中有一些文字解说这个功能


#她访问那个URL,发现她的待办事项列表还在


#她很满意，去睡觉了

#browser.quit();


