from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
#Config
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--silent")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome("./chromedriver.exe",chrome_options=chrome_options)
#Getting our jokes
print("Joke incoming.....")
web.get("https://www.reddit.com/r/Jokes/")
#Don't include style in the xpath, we only need to get the jokes xpath, Because pinned messages have a different xPath
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
sleep(5)
