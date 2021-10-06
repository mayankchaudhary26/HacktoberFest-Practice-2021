# wallace leonel | Wallace Leonel Pereira | fatec são paulo
# criando uns programinhas por ai :) 
# https://github.com./wallaceleonel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GitHubBot:
  def __init__(self, /, username, password):
    self.username = username
    self.password = password

    self.driver = webdriver.Chrome()

  
  def closeBrowser(self):
    self.driver.close()
  

  def login(self):
    # GitHub direct URL
    driver = self.driver
    driver.get('https://github.com/')
    time.sleep(0)
    # "//a[href='https://github.com/login']"
    login_btn = driver.find_element_by_link_text("Sign in")
    login_btn.click()
    time.sleep(2)
    # "//input[@name='login']"
    user = driver.find_element_by_xpath("//input[@name='login']")
    user.clear()
    user.send_keys(self.username)
    # "//input[@name='password']"
    passw = driver.find_element_by_xpath("//input[@name='password']")
    passw.clear()
    passw.send_keys(self.password)
    passw.send_keys(Keys.RETURN)
    time.sleep(2)
  

  def new_repository(self, /,repo_name='My-Repository-Name', pp='Private'):
    driver = self.driver
    # "//a[@class='btn btn-sm btn-primary text-white']"
    repo_url = driver.find_element_by_link_text("New")
    repo_url.click()
    time.sleep(2)
    # Enter repository name
    # "//input[@name='repository[name]']"
    new_repo = driver.find_element_by_xpath("//input[@name='repository[name]']")
    new_repo.clear()
    new_repo.send_keys(repo_name)
    time.sleep(2)
    # To define if repository visibility is 'public' or 'private'
    if pp == 'Private':
      # Private
      priv_vis = driver.find_element_by_xpath("//input[@id='repository_visibility_private']")
      priv_vis.click()
      time.sleep(2)
    elif pp == 'Public':
      # Public
      priv_vis = driver.find_element_by_xpath("//input[@id='repository_visibility_public']")
      priv_vis.click()
      for i in range(1, 2):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)
      # To create README
      read_me = driver.find_element_by_xpath("//input[@id='repository_auto_init']")
      read_me.click()
      time.sleep(1)
    else:
      # Private
      priv_vis = driver.find_element_by_xpath("//input[@id='repository_visibility_private']")
      priv_vis.click()
      time.sleep(2)
    # To create the final repo
    repo_btn_creator = driver.find_element_by_xpath("//button[@class='btn btn-primary first-in-line']")
    repo_btn_creator.click()
    time.sleep(1)


esau_ig = GitHubBot('<username>', '<password>')
esau_ig.login()
esau_ig.new_repository()
