from selenium import webdriver
from selenium.webdriver.chrome.options import Options


opt=Options()
opt.add_argument("--headless")

driver=webdriver.Chrome(chrome_options=opt)
driver.set_window_size(width=1920,height=200)
#设置宽度 否则太小显示不出来东西
driver.get("https://store.steampowered.com/")

driver.get_screenshot_as_file(str(1)+".png")



#driver.switch_to.frame("contentFrame")

data=driver.find_element_by_id("home_maincap_v7").\
find_element_by_class_name("carousel_items").\
find_elements_by_tag_name("a")
import time
recommend=[]
for i in range(len(data)):
    game_name=data[i].find_element_by_class_name("info").\
    find_element_by_class_name("app_name").find_element_by_css_selector("div").text
    while game_name=="":
        print("wait")
        time.sleep(2)
        #等待steam自动切换
        game_name=data[i].find_element_by_class_name("info").\
        find_element_by_class_name("app_name").find_element_by_css_selector("div").text
    game_id=data[i].get_attribute("data-ds-appid")
    recommend.append([game_name,game_id])
    print(i)

import datetime
today=datetime.datetime.now().strftime("%Y/%m/%d %H%M")
import csv
csv_file=open(today+"_steam_recommend.csv","w",newline="",encoding="utf-8")
writer=csv.writer(csv_file)
writer.writerow(["游戏名称","游戏id"])
for i in recommend:
    writer.writerow(i)
csv_file.close()

driver.close()