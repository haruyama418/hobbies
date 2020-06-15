  
import requests
from selenium import webdriver



url = "https://notify-api.line.me/api/notify"
api_token = "GFIJdjPV4l3qZIMe75hzvRxsnstwLTecRY1AO9b0Jtk" # 発行したトークン
headers = {"Authorization": "Bearer " + api_token}

from selenium import webdriver
browser = webdriver.Safari()
browser.implicitly_wait(10) 
browser.get('https://weathernews.jp/s/forecast/?area=TOKYO')
elem = browser.find_element_by_xpath('//*[@id="main"]/section/div[1]/div[2]/p[2]/text()')

elem=elem.text
print(elem) 


#elem_user_id=browser.find_element_by_id('username_input')
#elem_user_id.send_keys('19F1110011G')
#elem_pass=browser.find_element_by_id('password_input')
#elem_pass.send_keys('Kiruha418')
#browser.implicitly_wait(10) 
#btn=browser.find_element_by_xpath('//*[@id="login_button_area"]/input')
#log_btn = btn.find_element_by_value("Login")
#btn.click()

#contents= browser.find_element_by_xpath('//*[@id="courselistweekly"]/table/tbody/tr[5]/td[3]/div/div/img[1]')

#try:
    #judge = contents.find_element_by_title('未提出の課題があります。')
#except:
    #print('未提出の課題はないです。')

browser.quit()




messages = elem

message = messages
payload = {'message': message}
r = requests.post(url, headers=headers, params=payload)

