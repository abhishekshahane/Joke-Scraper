from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
print("Random config stuff..Don't mind me")
#Config
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
options = Options()
options.add_argument("--headless")
options.add_argument("--silent")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome("./chromedriver.exe",chrome_options=chrome_options)
#Getting our jokes
print("Joke incoming.....")
web.get("https://www.reddit.com/r/Jokes/")
text1 = web.find_elements_by_xpath('//div[2]/div[2]/div[1]/a/div/h3[1]')
init=[]
jokes=[]
for value in text1:
    init.append(value.text)
print(init[0])
text2=web.find_elements_by_xpath('//div[2]/div[3]/div/div/p[1]')
for value in text2:
    jokes.append(value.text)
print(jokes[0])

web.quit()
sleep(10)
