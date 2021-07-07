def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
   
# pytest.exe -s -v --tb=line --language=en D:\w_py\test_main_page.py
# cd C:\Users\scor1\AppData\Local\Programs\Python\Python38\Scripts\
# cd d:\Alex\Docs\GitHub\python-test-POM\
# C:\Users\scor1\AppData\Local\Programs\Python\Python38\Scripts\pytest.exe -s -v --tb=line --language=en test_main_page.py
