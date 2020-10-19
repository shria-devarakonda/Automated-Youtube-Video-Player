from selenium import webdriver
import time
#time is necessary, otherwise it will play the first vid on the homepage

path = r"C:\Users\shria\Desktop\Stuff\chromedriver_win32\chromedriver.exe"
#edit path according to your chromedriver.exe path


def plays():
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("http://www.youtube.com")

    inputElem = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    #above, search bar id xpath, this will be same for you too
    
    inputElem.send_keys('Exo')
    #above, search term to fill in, you can modify according to your taste

    Btn=driver.find_element_by_css_selector('#search-icon-legacy.ytd-searchbox')
    #above, find the button, below click the button
    Btn.click()
    
    time.sleep(5)
    #sleep otherwise it will play first vid on homepage before your search result is displayed
    
    inputElem1 = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
    inputElem1.click()

    time.sleep(15)
    #above, time duration for video to play
    
    driver.close()

for _ in range(5):
    #a loop in case you want this repeated, just an extra
    plays()
